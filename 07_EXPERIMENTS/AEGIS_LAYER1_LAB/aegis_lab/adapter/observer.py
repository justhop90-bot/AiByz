"""Strict ingestion boundary for observations produced by a runtime probe.

The adapter never converts missing observations into zeroes and never treats a
successful process exit as an observation of game state.
"""
from __future__ import annotations

from pathlib import Path
import json


REQUIRED = {"experiment_id", "phase", "timestamp", "measurements"}


def read_observation(path: str, expected_experiment_id: str) -> dict[str, object]:
    source = Path(path).resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    data = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Observation root must be an object")
    missing = REQUIRED.difference(data)
    if missing:
        raise ValueError(f"Observation missing required fields: {sorted(missing)}")
    if data["experiment_id"] != expected_experiment_id:
        raise ValueError("Observation experiment_id does not match requested experiment")
    if not isinstance(data["measurements"], dict):
        raise ValueError("Observation measurements must be an object")
    return data


def append_observation(path: str, observation: dict[str, object]) -> None:
    target = Path(path).resolve()
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(observation, sort_keys=True) + "\n")
