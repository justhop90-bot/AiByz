"""Machine-readable contract for controlled AoE2DE experiment setup.

The adapter refuses to infer scenario state from a filename or replay. A
future scenario provider must satisfy this contract before native execution.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class ScenarioContract:
    scenario_path: str
    player_slot: int
    observer_slot: int | None
    fact_probe: str
    initial_state: dict[str, object]
    mutation: dict[str, object]
    timing: list[int]

    def validate(self) -> None:
        path = Path(self.scenario_path)
        if not path.is_file():
            raise FileNotFoundError(f"Scenario artifact not found: {path}")
        if not 1 <= self.player_slot <= 8:
            raise ValueError("player_slot must be in 1..8")
        if self.observer_slot is not None and not 1 <= self.observer_slot <= 8:
            raise ValueError("observer_slot must be in 1..8")
        if not self.fact_probe:
            raise ValueError("fact_probe is required")
        if not self.timing or any(t < 0 for t in self.timing):
            raise ValueError("timing must contain non-negative offsets")


def write_contract(contract: ScenarioContract, path: str) -> None:
    contract.validate()
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(asdict(contract), indent=2, sort_keys=True) + "\n", encoding="utf-8")
