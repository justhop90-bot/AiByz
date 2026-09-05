import json
from pathlib import Path

from replay_causal_analyzer import analyze


def test_id_presence_is_only_correlation(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    evidence = tmp_path / "evidence.jsonl"
    report_path = tmp_path / "report.json"
    rows = [
        {"op": "ACTION", "payload": ["DE_QUEUE", {"player_id": 1, "unit_id": 38, "sequence": 5}]},
        {"op": "SYNC", "payload": [10, None, {"objects": [{"id": 38}]}]},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    report = analyze(source, evidence)
    assert report["correlations"] == 1
    event = json.loads(evidence.read_text(encoding="utf-8").strip())
    assert event["relation"] == "CORROBORATED_ID_PRESENCE"
    assert report["semantic_boundary"]["accepted"] == "NOT_PROVABLE_BY_THIS_ANALYZER"
    assert report["semantic_boundary"]["available"] == "NOT_PROVABLE_BY_THIS_ANALYZER"
    assert report["semantic_boundary"]["effective"] == "NOT_PROVABLE_BY_THIS_ANALYZER"


def test_missing_identity_remains_unknown(tmp_path: Path):
    source = tmp_path / "body.jsonl"
    evidence = tmp_path / "evidence.jsonl"
    rows = [
        {"op": "ACTION", "payload": ["BUILD", {"player_id": 1, "building_id": 70, "sequence": 5}]},
        {"op": "SYNC", "payload": [10, None, {"objects": [{"id": 999}]}]},
    ]
    source.write_text("\n".join(json.dumps(row) for row in rows), encoding="utf-8")
    report = analyze(source, evidence)
    event = json.loads(evidence.read_text(encoding="utf-8").strip())
    assert event["semantic_status"] == "UNKNOWN"
    assert event["evidence_level"] == "replay_insufficient"
    assert report["semantic_status_counts"]["UNKNOWN"] == 1
