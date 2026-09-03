"""Fail-closed identity checks for the controlled AoE2DE executable."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class BuildIdentity:
    path: str
    sha256: str
    size: int


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def verify_executable(path: str, expected_sha256: str) -> BuildIdentity:
    """Verify the executable before any runtime launch is permitted."""
    executable = Path(path).resolve()
    if not executable.is_file():
        raise FileNotFoundError(f"AoE2DE executable not found: {executable}")
    actual = sha256_file(executable)
    expected = expected_sha256.strip().upper()
    if actual != expected:
        raise RuntimeError(
            "Controlled build identity mismatch: "
            f"expected {expected}, observed {actual}"
        )
    return BuildIdentity(str(executable), actual, executable.stat().st_size)
