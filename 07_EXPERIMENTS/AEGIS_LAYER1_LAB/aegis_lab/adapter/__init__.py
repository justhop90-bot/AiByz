"""AoE2DE-specific Layer 1 experiment adapter."""

from .build_guard import BuildIdentity, verify_executable
from .runtime_controller import AoE2DERuntime, RuntimeResult
from .scenario_contract import ScenarioContract, write_contract
from .scenario_provider import (
    build_p0a_calibration_fixture,
    load_qualified_parser,
    validate_p0a_fixture,
)

__all__ = [
    "AoE2DERuntime",
    "BuildIdentity",
    "RuntimeResult",
    "ScenarioContract",
    "verify_executable",
    "write_contract",
    "build_p0a_calibration_fixture",
    "load_qualified_parser",
    "validate_p0a_fixture",
]
