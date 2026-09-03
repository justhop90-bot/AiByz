"""AoE2DE-specific Layer 1 experiment adapter."""

from .build_guard import BuildIdentity, verify_executable
from .runtime_controller import AoE2DERuntime, RuntimeResult
from .scenario_contract import ScenarioContract, write_contract

__all__ = [
    "AoE2DERuntime",
    "BuildIdentity",
    "RuntimeResult",
    "ScenarioContract",
    "verify_executable",
    "write_contract",
]
