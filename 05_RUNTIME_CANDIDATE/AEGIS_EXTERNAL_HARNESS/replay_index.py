from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any, TextIO

SCHEMA = "AEGIS-REPLAY-INDEX-v1"
LIFECYCLE_ACTIONS = {"BUILD", "DE_QUEUE", "RESEARCH", "DELETE"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_rows(path: Path) -> Any:
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                yield line_no, json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at line {line_no}: {exc}") from exc


def normalize_action(sequence: int, command: str, data: dict[str, Any],
                     last_sync_time: int | None, ordinal: int) -> dict[str, Any]:
    target = None
    if command == "BUILD":
        target = data.get("building_id")
    elif command == "RESEARCH":
        target = data.get("technology_id")
    elif command == "DE_QUEUE":
        target = data.get("unit_id")
    return {
        "ordinal": ordinal,
        "sequence": sequence,
        "replay_time": last_sync_time,
        "event_kind": "COMMAND_ISSUED",
        "command": command,
        "player_id": data.get("player_id"),
        "actor_ids": data.get("object_ids", []),
        "target_id": data.get("target_id"),
        "target_type": target,
        "coordinates": [data[x] for x in ("x", "y")] if "x" in data and "y" in data else None,
        "evidence_level": "replay_action",
        "semantic_status": "ISSUED",
    }


def build_index(input_path: Path, output_path: Path) -> dict[str, Any]:
    action_counts: Counter[str] = Counter()
    op_counts: Counter[str] = Counter()
    normalized: list[dict[str, Any]] = []
    sync_count = 0
    nonempty_sync_count = 0
    last_sync_time: int | None = None
    first_time: int | None = None
    last_time: int | None = None
    ordinal = 0

    for _, row in iter_rows(input_path):
        op = row.get("op")
        op_counts[str(op)] += 1
        payload = row.get("payload")
        if op == "SYNC" and isinstance(payload, list) and len(payload) > 2:
            sync_count += 1
            state = payload[2]
            if isinstance(state, dict):
                value = state.get("current_time")
                if isinstance(value, int):
                    last_sync_time = value
                    first_time = value if first_time is None else first_time
                    last_time = value
                    nonempty_sync_count += 1
        elif op == "ACTION" and isinstance(payload, list) and len(payload) == 2:
            command, data = payload
            if isinstance(command, str) and isinstance(data, dict):
                action_counts[command] += 1
                if command in LIFECYCLE_ACTIONS:
                    ordinal += 1
                    normalized.append(normalize_action(
                        int(data.get("sequence", -1)), command, data,
                        last_sync_time, ordinal,
                    ))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as fh:
        for event in normalized:
            fh.write(json.dumps(event, sort_keys=True) + "\n")

    return {
        "schema": SCHEMA,
        "input": str(input_path),
        "input_sha256": sha256_file(input_path),
        "records_by_operation": dict(op_counts),
        "actions_by_command": dict(action_counts),
        "sync_records": sync_count,
        "sync_records_with_current_time": nonempty_sync_count,
        "first_replay_time_observed": first_time,
        "last_replay_time_observed": last_time,
        "lifecycle_commands_indexed": len(normalized),
        "semantic_boundary": {
            "ACTION": "COMMAND_ISSUED_ONLY",
            "SYNC": "AGGREGATE_SNAPSHOT_ONLY",
            "pending_to_created": "NOT_INFERRED",
            "created_to_available": "NOT_INFERRED",
            "effective": "NOT_INFERRED",
        },
        "evidence_policy": "Replay observations do not prove acceptance or world-state completion without corroborating evidence.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    report = build_index(args.input, args.events)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
