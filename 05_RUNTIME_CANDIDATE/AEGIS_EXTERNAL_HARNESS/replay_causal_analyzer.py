from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterator

SCHEMA = "AEGIS-REPLAY-CAUSAL-v2"
LIFECYCLE = {"BUILD", "DE_QUEUE", "RESEARCH", "DELETE"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def rows(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid JSON at line {line_no}: {exc}") from exc
            if isinstance(row, dict):
                row["_line_no"] = line_no
                yield row


def _action_target(command: str, data: dict[str, Any]) -> int | None:
    keys = ["target_id"]
    if command == "DE_QUEUE":
        keys.insert(0, "unit_id")
    elif command == "BUILD":
        keys.insert(0, "building_id")
    elif command == "RESEARCH":
        keys.insert(0, "technology_id")
    for key in keys:
        if isinstance(data.get(key), int):
            return data[key]
    return None


def analyze(input_path: Path, output_path: Path, window_syncs: int = 8) -> dict[str, Any]:
    elapsed_ms = 0
    sync_seen = 0
    action_seen = 0
    lifecycle_seen = 0
    pending: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []

    for row in rows(input_path):
        op = row.get("op")
        payload = row.get("payload")
        if op == "SYNC" and isinstance(payload, list):
            increment = payload[0] if payload and isinstance(payload[0], int) else 0
            elapsed_ms += increment
            sync_seen += 1
            for action in pending:
                evidence.append({
                    "action_line": action["line_no"],
                    "action_command": action["command"],
                    "action_sequence": action.get("sequence"),
                    "action_replay_time_ms": action["replay_time_ms"],
                    "observed_sync_line": row["_line_no"],
                    "observed_replay_time_ms": elapsed_ms,
                    "elapsed_ms_after_action": elapsed_ms - action["replay_time_ms"],
                    "syncs_after_action": sync_seen - action["sync_ordinal"],
                    "target_id": action.get("target_id"),
                    "semantic_status": "TEMPORALLY_CORRELATED",
                    "evidence_level": "replay_temporal_only",
                })
            pending.clear()
        elif op == "ACTION" and isinstance(payload, list) and len(payload) == 2:
            command, data = payload
            if isinstance(command, str) and isinstance(data, dict):
                action_seen += 1
                if command in LIFECYCLE:
                    lifecycle_seen += 1
                    pending.append({
                        "line_no": row["_line_no"],
                        "command": command,
                        "sequence": data.get("sequence"),
                        "target_id": _action_target(command, data),
                        "player_id": data.get("player_id"),
                        "replay_time_ms": elapsed_ms,
                        "sync_ordinal": sync_seen,
                    })
                    if len(pending) > window_syncs:
                        pending = pending[-window_syncs:]

    report = {
        "schema": SCHEMA,
        "input": str(input_path),
        "input_sha256": sha256_file(input_path),
        "records": {"actions": action_seen, "syncs": sync_seen},
        "lifecycle_commands": lifecycle_seen,
        "temporal_correlations": len(evidence),
        "semantic_boundary": {
            "command_issued": "PROVABLE_FROM_ACTION",
            "replay_time": "PROVABLE_FROM_CUMULATIVE_SYNC_INCREMENT",
            "accepted": "NOT_PROVABLE",
            "queued_pending": "NOT_PROVABLE",
            "created": "NOT_PROVABLE",
            "available": "NOT_PROVABLE",
            "effective": "NOT_PROVABLE",
        },
        "policy": "Temporal adjacency is measurement only; it is never promoted to world-state causality.",
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(json.dumps(item, sort_keys=True) for item in evidence) + ("\n" if evidence else ""), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    report = analyze(args.input, args.evidence)
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
