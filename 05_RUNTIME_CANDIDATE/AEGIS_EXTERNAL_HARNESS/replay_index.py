from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Any

SCHEMA = "AEGIS-REPLAY-INDEX-v3"
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


def normalize_action(record_ordinal: int, source_line: int, sequence: int,
                     command: str, data: dict[str, Any],
                     prior_sync_elapsed_raw: int, ordinal: int) -> dict[str, Any]:
    target = None
    if command == "BUILD":
        target = data.get("building_id")
    elif command == "RESEARCH":
        target = data.get("technology_id")
    elif command == "DE_QUEUE":
        target = data.get("unit_id")
    return {
        "ordinal": ordinal,
        "record_ordinal": record_ordinal,
        "source_line": source_line,
        "action_sequence": sequence,
        "nearest_prior_sync_elapsed_raw": prior_sync_elapsed_raw,
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
    sync_elapsed_raw_total = 0
    sync_payloads_with_state = 0
    ordinal = 0
    record_ordinal = 0
    previous_sequence: int | None = None
    sequence_regressions = 0
    equal_adjacent_sequence_pairs = 0

    for source_line, row in iter_rows(input_path):
        record_ordinal += 1
        op = row.get("op")
        op_counts[str(op)] += 1
        payload = row.get("payload")
        if op == "SYNC" and isinstance(payload, list):
            sync_count += 1
            # mgz-fast payload[0] is the parser's elapsed-time increment.
            # Its physical unit is deliberately not asserted here.
            increment = payload[0] if payload and isinstance(payload[0], int) else 0
            sync_elapsed_raw_total += increment
            if len(payload) > 2 and isinstance(payload[2], dict) and payload[2]:
                sync_payloads_with_state += 1
        elif op == "ACTION" and isinstance(payload, list) and len(payload) == 2:
            command, data = payload
            if isinstance(command, str) and isinstance(data, dict):
                action_counts[command] += 1
                sequence = data.get("sequence")
                if isinstance(sequence, int):
                    if previous_sequence is not None:
                        if sequence < previous_sequence:
                            sequence_regressions += 1
                        if sequence == previous_sequence:
                            equal_adjacent_sequence_pairs += 1
                    previous_sequence = sequence
                if command in LIFECYCLE_ACTIONS:
                    ordinal += 1
                    normalized.append(normalize_action(
                        record_ordinal,
                        source_line,
                        int(sequence) if isinstance(sequence, int) else -1,
                        command,
                        data,
                        sync_elapsed_raw_total,
                        ordinal,
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
        "sync_payloads_with_nonempty_metadata": sync_payloads_with_state,
        "replay_duration_raw_units": sync_elapsed_raw_total,
        "lifecycle_commands_indexed": len(normalized),
        "action_sequence_monotonic_on_observed_records": sequence_regressions == 0,
        "action_sequence_regressions": sequence_regressions,
        "equal_adjacent_action_sequence_pairs": equal_adjacent_sequence_pairs,
        "semantic_boundary": {
            "ACTION": "COMMAND_ISSUED_ONLY",
            "SYNC": "ELAPSED_TIME_INCREMENT_ONLY",
            "world_object_state": "NOT_PRESENT_IN_CALIBRATION_SYNC_PAYLOADS",
            "pending_to_created": "NOT_INFERRED",
            "created_to_available": "NOT_INFERRED",
            "effective": "NOT_INFERRED",
        },
        "temporal_boundary": {
            "action_sequence": "RAW_ACTION_SEQUENCE_FIELD",
            "nearest_prior_sync_elapsed_raw": "CUMULATIVE_PARSER_TIME_BEFORE_ACTION; NOT_ACTION_TIMESTAMP",
            "replay_duration_raw_units": "SUM_OF_SYNC_PAYLOAD_0; PHYSICAL_UNIT_UNQUALIFIED",
            "millisecond_claim": "NOT_MADE",
        },
        "evidence_policy": "Replay ACTION records establish issued commands; SYNC establishes parser time progression. Neither alone proves world-state completion.",
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
