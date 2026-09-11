from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm" / "AEGIS-military-production-v0.per"


def read():
    return SOURCE.read_text(encoding="utf-8")


def test_count_increase_cannot_confirm_military_production():
    text = read()
    assert "aegis-mp-stage-world-observed" in text
    assert "aegis-mp-stage-causally-confirmed" in text
    assert "aegis-mp-causal-evidence" in text
    assert "aegis-mp-causal-attribution == 1" in text
    assert "aegis-mp-observed > aegis-mp-baseline" in text
    world_rule = text.index("(up-compare-goal aegis-mp-observed > aegis-mp-baseline)")
    causal_rule = text.index("(up-compare-goal aegis-mp-causal-attribution == 1)")
    assert world_rule < causal_rule


def test_request_bound_attribution_producer_requires_independent_alternative_clear():
    text = read()
    assert "aegis-mp-causal-alternative-producer-clear 805" in text
    producer_start = text.index("; Request-bound attribution producer.")
    producer_end = text.index("; Causal confirmation requires every request-bound attribution predicate.")
    producer = text[producer_start:producer_end]
    required = [
        "aegis-mp-causal-request-id == aegis-mp-request-id",
        "aegis-mp-causal-authorization-id == aegis-mp-authorization-id",
        "aegis-mp-causal-generation == aegis-mp-generation",
        "aegis-mp-causal-dispatch-observed == 1",
        "aegis-mp-causal-pending-observed == 1",
        "aegis-mp-causal-pending-resolved == 1",
        "aegis-mp-causal-world-transition == 1",
        "aegis-mp-causal-alternative-producer-clear == 1",
        "set-goal aegis-mp-causal-attribution 1",
    ]
    for predicate in required:
        assert predicate in producer


def test_causal_confirmation_requires_request_bound_chain():
    text = read()
    required = [
        "aegis-mp-causal-request-id == aegis-mp-request-id",
        "aegis-mp-causal-authorization-id == aegis-mp-authorization-id",
        "aegis-mp-causal-generation == aegis-mp-generation",
        "aegis-mp-causal-dispatch-observed == 1",
        "aegis-mp-causal-pending-observed == 1",
        "aegis-mp-causal-pending-resolved == 1",
        "aegis-mp-causal-world-transition == 1",
        "aegis-mp-causal-attribution == 1",
    ]
    for predicate in required:
        assert predicate in text


def test_causal_evidence_is_not_manufactured_by_count_delta():
    text = read()
    world_start = text.index("; World evidence is deliberately separated")
    causal_start = text.index("; Request-bound attribution producer.")
    world_rule = text[world_start:causal_start]
    assert "set-goal aegis-mp-causal-evidence 1" not in world_rule
    assert "set-goal aegis-mp-causal-attribution 1" not in world_rule


def test_attribution_is_not_manufactured_without_alternative_clear():
    text = read()
    producer_start = text.index("; Request-bound attribution producer.")
    producer_end = text.index("; Causal confirmation requires every request-bound attribution predicate.")
    producer = text[producer_start:producer_end]
    assert "aegis-mp-causal-alternative-producer-clear == 1" in producer
    assert "set-goal aegis-mp-causal-alternative-producer-clear 1" not in producer


def test_reassessment_only_publishes_causal_confirmation_or_failure():
    text = read()
    reassess = text[text.index("; Canonical reassessment boundary."):]
    assert "aegis-mp-stage-causally-confirmed" in reassess
    assert "aegis-mp-stage-failed" in reassess
    assert "aegis-mp-stage-world-observed" not in reassess


def test_candidate_remains_not_promoted_by_acap_repair():
    text = read()
    assert "Candidate only" in text
    assert "qualification/promotion remains blocked" in text
