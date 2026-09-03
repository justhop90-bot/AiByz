"""Evidence-preserving artifact collection.

Collection is intentionally boring: copy/record bytes, hash them, and keep
experiment provenance. Interpretation belongs elsewhere.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def capture_file(source: str, run_dir: str, label: str) -> dict[str, str | int]:
    src = Path(source).resolve()
    if not src.is_file():
        raise FileNotFoundError(src)
    dst_dir = Path(run_dir).resolve()
    dst_dir.mkdir(parents=True, exist_ok=True)
    safe_label = "".join(c if c.isalnum() or c in "._-" else "_" for c in label)
    dst = dst_dir / safe_label
    shutil.copy2(src, dst)
    return {
        "label": safe_label,
        "path": str(dst),
        "size": dst.stat().st_size,
        "sha256": sha256_file(dst),
    }


def write_artifact_manifest(run_dir: str, artifacts: list[dict[str, object]]) -> str:
    target = Path(run_dir).resolve() / "artifact_manifest.json"
    target.write_text(json.dumps(artifacts, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return str(target)
