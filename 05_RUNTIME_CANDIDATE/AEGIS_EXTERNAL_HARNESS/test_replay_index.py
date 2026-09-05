import json
from pathlib import Path

from replay_index import build_index


def test_replay_index_preserves_command_boundary(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    events = tmp_path / "events.jsonl"
    report = tmp_path / "report.json"
    rows = [
        {"op": "SYNC", "payload": [13, 1, {"current_time": 1000}]},
        {"op": "ACTION", "payload": ["DE_QUEUE", {"player_id": 1, "unit_id": 38, "object_ids": [7], "sequence": 1200}]},
        {"op": "ACTION", "payload": ["BUILD", {"player_id": 1, "building_id": 70, "object_ids": [7], "x": 10.0, "y": 20.0, "sequence": 1300}]},
        {"op": "ACTION", "payload": ["MOVE", {"player_id": 1, "object_ids": [7], "x": 11.0, "y": 21.0, "sequence": 1400}]},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    result = build_index(source, events)
    assert result["records_by_operation"]["ACTION"] == 3
    assert result["lifecycle_commands_indexed"] == 2
    assert result["first_replay_time_observed"] == 1000
    parsed = [json.loads(line) for line in events.read_text(encoding="utf-8").splitlines()]
    assert [row["command"] for row in parsed] == ["DE_QUEUE", "BUILD"]
    assert all(row["semantic_status"] == "ISSUED" for row in parsed)
    assert all(row["event_kind"] == "COMMAND_ISSUED" for row in parsed)


def test_replay_index_does_not_infer_completion(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    events = tmp_path / "events.jsonl"
    report = tmp_path / "report.json"
    source.write_text(json.dumps({
        "op": "ACTION",
        "payload": ["DE_QUEUE", {"player_id": 1, "unit_id": 38, "sequence": 5}],
    }), encoding="utf-8")
    result = build_index(source, events)
    assert result["semantic_boundary"]["pending_to_created"] == "NOT_INFERRED"
    assert result["semantic_boundary"]["created_to_available"] == "NOT_INFERRED"
    assert result["semantic_boundary"]["effective"] == "NOT_INFERRED"
