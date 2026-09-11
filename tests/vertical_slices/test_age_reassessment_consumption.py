from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm" / "AEGIS-civilization-state-v0.per"
RA_SOURCE = ROOT / "AegisProm" / "AEGIS-research-age-v0.per"
WM_SOURCE = ROOT / "AegisProm" / "AEGIS-foundation.per"


def test_age_reassess_consumer_namespace_is_registered_in_source():
    text = SOURCE.read_text(encoding="utf-8")
    assert "(defconst aegis-cs-age-reassess-generation 780)" in text
    assert "(defconst aegis-cs-age-reassess-valid 781)" in text


def test_age_reassess_requires_exact_published_identity():
    text = SOURCE.read_text(encoding="utf-8")
    assert "(up-compare-goal aegis-ra-reassess-valid == 1)" in text
    assert "(up-compare-goal aegis-ra-reassess-generation == aegis-ra-generation)" in text
    assert "(up-compare-goal aegis-ra-generation == aegis-cs-generation)" in text


def test_age_reassess_is_one_shot_and_consumes_publisher_token():
    text = SOURCE.read_text(encoding="utf-8")
    assert "(up-modify-goal aegis-cs-age-reassess-generation g:= aegis-ra-reassess-generation)" in text
    assert "(set-goal aegis-cs-age-reassess-valid 1)" in text
    assert "(set-goal aegis-ra-reassess-valid 0)" in text


def test_age_reassess_cannot_create_a_new_world_or_civilization_generation():
    text = SOURCE.read_text(encoding="utf-8")
    block = text[text.index("; Age-transition REASSESS acknowledgement."):]
    assert "g:+" not in block
    assert "aegis-wm-generation" not in block.split("; A fresh World Model generation supersedes", 1)[0]


def test_new_civilization_generation_still_comes_from_world_model():
    text = SOURCE.read_text(encoding="utf-8")
    assert "(up-compare-goal aegis-wm-valid == 1)" in text
    assert "(up-compare-goal aegis-cs-generation != aegis-wm-generation)" in text
    assert "(up-modify-goal aegis-cs-generation g:= aegis-wm-generation)" in text


def test_age_transition_publisher_remains_generation_keyed():
    text = RA_SOURCE.read_text(encoding="utf-8")
    assert "(defconst aegis-ra-reassess-generation 766)" in text
    assert "(defconst aegis-ra-reassess-valid 767)" in text
    assert "aegis-ra-reassess-generation != aegis-ra-generation" in text


def test_age_transition_reassessment_does_not_claim_causal_success():
    text = RA_SOURCE.read_text(encoding="utf-8")
    assert "aegis-ra-causal-evidence" in text
    assert "aegis-ra-world-evidence" in text
    assert "set-goal aegis-ra-causal-evidence 1" not in text


def test_world_model_age_authority_remains_blocked_and_is_not_silently_promoted():
    text = WM_SOURCE.read_text(encoding="utf-8")
    assert "(set-goal aegis-wm-age 0)" in text
    assert "(up-get-fact current-age" not in text


def test_no_central_reassessment_controller_is_introduced():
    text = SOURCE.read_text(encoding="utf-8")
    assert "strategy" not in text[text.index("; Age-transition REASSESS acknowledgement."):]
