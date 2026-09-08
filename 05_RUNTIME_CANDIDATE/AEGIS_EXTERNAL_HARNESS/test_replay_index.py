import json
from pathlib import Path

from replay_index import build_index


def test_replay_index_preserves_command_boundary(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    events = tmp_path / "events.jsonl"
    rows = [
        {"op": "SYNC", "payload": [13, 1, {}]},
        {"op": "ACTION", "payload": ["DE_QUEUE", {"player_id": 1, "unit_id": 38, "object_ids": [7], "sequence": 1200}]},
        {"op": "SYNC", "payload": [104, 1, {}]},
        {"op": "ACTION", "payload": ["BUILD", {"player_id": 1, "building_id": 70, "object_ids": [7], "x": 10.0, "y": 20.0, "sequence": 1300}]},
        {"op": "ACTION", "payload": ["MOVE", {"player_id": 1, "object_ids": [7], "x": 11.0, "y": 21.0, "sequence": 1400}]},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    result = build_index(source, events)
    assert result["records_by_operation"]["ACTION"] == 3
    assert result["lifecycle_commands_indexed"] == 2
    assert result["replay_duration_raw_units"] == 117
    assert result["temporal_boundary"]["millisecond_claim"] == "NOT_MADE"
    parsed = [json.loads(line) for line in events.read_text(encoding="utf-8").splitlines()]
    assert [row["command"] for row in parsed] == ["DE_QUEUE", "BUILD"]
    assert parsed[0]["nearest_prior_sync_elapsed_raw"] == 13
    assert parsed[1]["nearest_prior_sync_elapsed_raw"] == 117
    assert parsed[0]["action_sequence"] == 1200
    assert parsed[1]["action_sequence"] == 1300
    assert parsed[0]["source_line"] == 2
    assert parsed[1]["source_line"] == 4
    assert all(row["semantic_status"] == "ISSUED" for row in parsed)
    assert all(row["event_kind"] == "COMMAND_ISSUED" for row in parsed)


def test_replay_index_does_not_infer_completion(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    events = tmp_path / "events.jsonl"
    source.write_text(json.dumps({
        "op": "ACTION",
        "payload": ["DE_QUEUE", {"player_id": 1, "unit_id": 38, "sequence": 5}],
    }), encoding="utf-8")
    result = build_index(source, events)
    assert result["semantic_boundary"]["pending_to_created"] == "NOT_INFERRED"
    assert result["semantic_boundary"]["created_to_available"] == "NOT_INFERRED"
    assert result["semantic_boundary"]["effective"] == "NOT_INFERRED"
