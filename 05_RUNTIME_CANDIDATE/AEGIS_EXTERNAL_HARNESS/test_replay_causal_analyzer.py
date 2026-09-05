import json
from pathlib import Path

from replay_causal_analyzer import analyze


def test_temporal_correlation_is_not_completion(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    evidence = tmp_path / "evidence.jsonl"
    rows = [
        {"op": "ACTION", "payload": ["DE_QUEUE", {"player_id": 1, "unit_id": 38, "sequence": 5}]},
        {"op": "SYNC", "payload": [10, None, {}]},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    report = analyze(source, evidence)
    assert report["temporal_correlations"] == 1
    event = json.loads(evidence.read_text(encoding="utf-8").strip())
    assert event["semantic_status"] == "TEMPORALLY_CORRELATED"
    assert event["evidence_level"] == "replay_temporal_only"
    assert event["action_replay_time_ms"] == 0
    assert event["observed_replay_time_ms"] == 10
    assert report["semantic_boundary"]["created"] == "NOT_PROVABLE"
    assert report["semantic_boundary"]["available"] == "NOT_PROVABLE"
    assert report["semantic_boundary"]["effective"] == "NOT_PROVABLE"


def test_sync_only_advances_clock(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    evidence = tmp_path / "evidence.jsonl"
    rows = [
        {"op": "SYNC", "payload": [13, None, {}]},
        {"op": "ACTION", "payload": ["BUILD", {"player_id": 1, "building_id": 70, "sequence": 5}]},
        {"op": "SYNC", "payload": [104, None, {}]},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    report = analyze(source, evidence)
    event = json.loads(evidence.read_text(encoding="utf-8").strip())
    assert event["action_replay_time_ms"] == 13
    assert event["observed_replay_time_ms"] == 117
    assert event["elapsed_ms_after_action"] == 104
    assert report["records"]["syncs"] == 2
