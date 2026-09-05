from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import time
from pathlib import Path
from typing import Any

SCHEMA = "AEGIS-REPLAY-COLLECT-v1"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def candidates(root: Path, started_at: float, build_version: str) -> list[Path]:
    if not root.exists():
        return []
    rows = []
    for path in root.glob("*.aoe2record"):
        try:
            stat = path.stat()
        except OSError:
            continue
        if stat.st_mtime >= started_at and build_version in path.name:
            rows.append(path)
    return sorted(rows, key=lambda p: p.stat().st_mtime, reverse=True)


def collect(root: Path, output_dir: Path, started_at: float, build_version: str) -> dict[str, Any]:
    matches = candidates(root, started_at, build_version)
    output_dir.mkdir(parents=True, exist_ok=True)
    if not matches:
        return {
            "schema": SCHEMA,
            "status": "NOT_FOUND",
            "root": str(root),
            "started_at": started_at,
            "build_version": build_version,
            "candidates": [],
        }

    source = matches[0]
    destination = output_dir / source.name
    shutil.copy2(source, destination)
    return {
        "schema": SCHEMA,
        "status": "COLLECTED",
        "source": str(source),
        "destination": str(destination),
        "bytes": destination.stat().st_size,
        "sha256": sha256_file(destination),
        "source_mtime": source.stat().st_mtime,
        "candidate_count": len(matches),
        "candidates": [str(p) for p in matches],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--started-at", type=float, default=time.time())
    parser.add_argument("--build-version", default="101.103.48987.0")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    result = collect(args.root, args.output_dir, args.started_at, args.build_version)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "COLLECTED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
