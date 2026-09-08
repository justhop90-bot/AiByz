import json
import tempfile
from pathlib import Path

import harness


def test_manifest_rejects_injection_flag():
    data = {
        "schema_version": "1.0",
        "experiment_id": "X",
        "build": {"executable": "x.exe", "sha256": "0" * 64},
        "launch": {"args": ["-TEST_HARNESS_COMM=x"], "timeout_seconds": 1},
        "evidence_policy": {"allow_injection": False, "allow_memory_write": False},
    }
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "m.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        try:
            harness.load_manifest(p)
        except ValueError as exc:
            assert "prohibited" in str(exc)
        else:
            raise AssertionError("forbidden native harness flag was accepted")


def test_manifest_accepts_safe_profile():
    data = {
        "schema_version": "1.0",
        "experiment_id": "X",
        "build": {"executable": "x.exe", "sha256": "0" * 64},
        "launch": {"args": ["-SKIPINTRO"], "timeout_seconds": 1},
        "evidence_policy": {"allow_injection": False, "allow_memory_write": False},
    }
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "m.json"
        p.write_text(json.dumps(data), encoding="utf-8")
        assert harness.load_manifest(p)["experiment_id"] == "X"
