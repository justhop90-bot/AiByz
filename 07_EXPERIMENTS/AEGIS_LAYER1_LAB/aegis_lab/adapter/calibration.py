"""Pre-causal calibration checks for the AoE2DE adapter."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json

from .build_guard import verify_executable
from .scenario_contract import ScenarioContract


@dataclass(frozen=True)
class CalibrationReport:
    passed: bool
    checks: dict[str, bool]
    reasons: list[str]

    def write(self, path: str) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps({"passed": self.passed, "checks": self.checks, "reasons": self.reasons}, indent=2) + "\n", encoding="utf-8")


def preflight(executable: str, expected_sha256: str, scenario: ScenarioContract) -> CalibrationReport:
    checks: dict[str, bool] = {}
    reasons: list[str] = []
    try:
        verify_executable(executable, expected_sha256)
        checks["build_identity"] = True
    except (FileNotFoundError, RuntimeError) as error:
        checks["build_identity"] = False
        reasons.append(str(error))
    try:
        scenario.validate()
        checks["scenario_contract"] = True
    except (FileNotFoundError, ValueError) as error:
        checks["scenario_contract"] = False
        reasons.append(str(error))
    checks["causal_promotion"] = False
    reasons.append("Calibration is instrumentation validation only; it cannot promote a Layer 1 causal claim.")
    return CalibrationReport(all(checks.values()) and not reasons, checks, reasons)
