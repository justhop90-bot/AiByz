from __future__

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterator

SCHEMA = "AEGIS-REPLAY-CAUSAL-v1"
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


def _walk_ids(value: Any) -> set[int]:
    found: set[int] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"object_id", "id", "unit_id", "building_id", "technology_id"} and isinstance(item, int):
                found.add(item)
            found.update(_walk_ids(item))
    elif isinstance(value, list):
        for item in value:
            found.update(_walk_ids(item))
    return found


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


def analyze(input_path: Path, output_path: Path, window_records: int = 2000) -> dict[str, Any]:
    pending: list[dict[str, Any]] = []
    evidence: list[dict[str, Any]] = []
    sync_seen = 0
    action_seen = 0
    for row in rows(input_path):
        op = row.get("op")
        payload = row.get("payload")
        if op == "SYNC" and isinstance(payload, list):
            sync_seen += 1
            state = payload[2] if len(payload) > 2 else None
            if isinstance(state, dict):
                visible_ids = _walk_ids(state)
                for action in pending:
                    target = action["target_id"]
                    relation = "UNKNOWN"
                    if isinstance(target, int) and target in visible_ids:
                        relation = "CORROBORATED_ID_PRESENCE"
                    evidence.append({
                        "action_line": action["line_no"],
                        "action_command": action["command"],
                        "action_sequence": action.get("sequence"),
                        "sync_line": row["_line_no"],
                        "relation": relation,
                        "target_id": target,
                        "evidence_level": "replay_correlated" if relation != "UNKNOWN" else "replay_insufficient",
                        "semantic_status": "CORRELATED" if relation != "UNKNOWN" else "UNKNOWN",
                    })
                pending.clear()
        elif op == "ACTION" and isinstance(payload, list) and len(payload) == 2:
            command, data = payload
            if isinstance(command, str) and isinstance(data, dict):
                action_seen += 1
                if command in LIFECYCLE:
                    pending.append({
                        "line_no": row["_line_no"],
                        "command": command,
                        "sequence": data.get("sequence"),
                        "target_id": _action_target(command, data),
                        "player_id": data.get("player_id"),
                    })
                    if len(pending) > window_records:
                        pending = pending[-window_records:]
    counts: dict[str, int] = {}
    for event in evidence:
        counts[event["semantic_status"]] = counts.get(event["semantic_status"], 0) + 1
    report = {
        "schema": SCHEMA,
        "input": str(input_path),
        "input_sha256": sha256_file(input_path),
        "records": {"actions": action_seen, "syncs": sync_seen},
        "correlations": len(evidence),
        "semantic_status_counts": counts,
        "semantic_boundary": {
            "command_issued": "PROVABLE_FROM_ACTION",
            "accepted": "NOT_PROVABLE_BY_THIS_ANALYZER",
            "queued_pending": "NOT_PROVABLE_BY_THIS_ANALYZER",
            "created": "ONLY_ID_PRESENCE_CORRELATION_WHEN_EXPLICITLY_OBSERVED",
            "available": "NOT_PROVABLE_BY_THIS_ANALYZER",
            "effective": "NOT_PROVABLE_BY_THIS_ANALYZER",
        },
        "policy": "ID presence is corroboration, not proof of creation, availability, or effectiveness.",
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
