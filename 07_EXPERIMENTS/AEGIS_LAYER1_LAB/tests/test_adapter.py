from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

LAB_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LAB_ROOT))

from aegis_lab.adapter.artifacts import capture_file
from aegis_lab.adapter.build_guard import verify_executable
from aegis_lab.adapter.observer import read_observation


class AdapterTests(unittest.TestCase):
    def test_build_guard_accepts_exact_hash(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.bin"
            path.write_bytes(b"AEGIS-FIXTURE")
            identity = verify_executable(
                str(path),
                "44199A0E4009918B7C3EB51883C9B5064C1B27728E56AB7A930235094E3DDB90",
            )
            self.assertEqual(identity.size, 13)

    def test_observer_rejects_wrong_experiment(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "observation.json"
            path.write_text(
                json.dumps({
                    "experiment_id": "OTHER",
                    "phase": "S0",
                    "timestamp": "2026-09-03T00:00:00+00:00",
                    "measurements": {"probe": 1},
                }),
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                read_observation(str(path), "EXPECTED")

    def test_artifact_capture_hashes_copy(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.txt"
            source.write_text("raw observation\n", encoding="utf-8")
            result = capture_file(str(source), str(Path(tmp) / "run"), "raw.txt")
            self.assertEqual(result["size"], 15)
            self.assertTrue(Path(str(result["path"])).is_file())


if __name__ == "__main__":
    unittest.main()
