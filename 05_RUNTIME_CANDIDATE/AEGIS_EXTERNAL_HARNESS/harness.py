from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "1.0"
FORBIDDEN_FLAGS = ("-TEST_HARNESS_COMM", "-TEST_HARNESS_ADDRESS")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unsupported harness manifest schema")
    policy = data.get("evidence_policy", {})
    if policy.get("allow_injection") is not False:
        raise ValueError("injection is prohibited by the default harness profile")
    if policy.get("allow_memory_write") is not False:
        raise ValueError("memory modification is prohibited by the default harness profile")
    args = data.get("launch", {}).get("args", [])
    forbidden = [a for a in args if any(a.startswith(x) for x in FORBIDDEN_FLAGS)]
    if forbidden:
        raise ValueError(f"embedded test-harness controls are prohibited: {forbidden}")
    return data


def capture_build(manifest: dict[str, Any]) -> dict[str, Any]:
    exe = Path(manifest["build"]["executable"]).resolve()
    if not exe.is_file():
        raise FileNotFoundError(exe)
    digest = sha256_file(exe)
    expected = manifest["build"]["sha256"].lower()
    return {
        "path": str(exe),
        "sha256": digest,
        "expected_sha256": expected,
        "sha256_match": digest == expected,
        "size": exe.stat().st_size,
    }


def run(manifest_path: Path, output_root: Path) -> int:
    manifest = load_manifest(manifest_path)
    build = capture_build(manifest)
    run_dir = output_root / manifest["experiment_id"]
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
    (run_dir / "build.json").write_text(
        json.dumps(build, indent=2), encoding="utf-8"
    )
    if not build["sha256_match"]:
        verdict = "FAIL_HARNESS"
        reason = "executable fingerprint mismatch"
        _write_verdict(run_dir, verdict, reason)
        return 2

    args = [manifest["build"]["executable"], *manifest["launch"]["args"]]
    start = time.time()
    try:
        proc = subprocess.Popen(
            args,
            cwd=manifest["launch"].get("working_directory") or None,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=os.environ.copy(),
        )
    except OSError as exc:
        _write_verdict(run_dir, "FAIL_HARNESS", f"launch failed: {exc}")
        return 3

    try:
        stdout, stderr = proc.communicate(
            timeout=float(manifest["launch"]["timeout_seconds"])
        )
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        proc.kill()
        stdout, stderr = proc.communicate()
        timed_out = True

    elapsed = time.time() - start
    (run_dir / "stdout.log").write_text(stdout or "", encoding="utf-8")
    (run_dir / "stderr.log").write_text(stderr or "", encoding="utf-8")
    lifecycle = {
        "pid": proc.pid,
        "returncode": proc.returncode,
        "timed_out": timed_out,
        "elapsed_seconds": elapsed,
    }
    (run_dir / "lifecycle.json").write_text(
        json.dumps(lifecycle, indent=2), encoding="utf-8"
    )

    # Process success is never treated as semantic/runtime success.
    if timed_out:
        verdict = "FAIL_RUNTIME_BEHAVIOR"
        reason = "supervisor timeout"
    else:
        verdict = "OBSERVED_WITH_LIMITATIONS"
        reason = "retail process lifecycle observed; semantic postconditions require replay evidence"
    _write_verdict(run_dir, verdict, reason)
    return 0 if not timed_out else 4


def _write_verdict(run_dir: Path, verdict: str, reason: str) -> None:
    payload = {
        "verdict": verdict,
        "reason": reason,
        "evidence_level": "runtime_observed" if verdict != "FAIL_HARNESS" else "harness_failure",
    }
    (run_dir / "verdict.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: harness.py <manifest.json> <output-root>", file=sys.stderr)
        return 64
    return run(Path(argv[1]), Path(argv[2]))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
