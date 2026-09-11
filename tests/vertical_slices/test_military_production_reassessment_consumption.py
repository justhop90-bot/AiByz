from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SRC / name).read_text(encoding="utf-8")


def test_military_production_publishes_reassessment():
    text = read("AEGIS-military-production-v0.per")
    assert "(defconst aegis-mp-reassess-generation 772)" in text
    assert "(defconst aegis-mp-reassess-valid 773)" in text
    assert "aegis-mp-stage == aegis-mp-stage-causally-confirmed" in text
    assert "aegis-mp-stage == aegis-mp-stage-failed" in text


def test_scouting_threat_owns_military_production_acknowledgement():
    text = read("AEGIS-scouting-threat-v0.per")
    assert "(defconst aegis-st-mp-reassess-generation 786)" in text
    assert "(defconst aegis-st-mp-reassess-valid 787)" in text
    assert "aegis-mp-reassess-valid == 1" in text
    assert "aegis-mp-reassess-generation == aegis-mp-generation" in text
    assert "aegis-st-mp-reassess-generation != aegis-mp-reassess-generation" in text
    assert "aegis-st-mp-reassess-generation g:= aegis-mp-reassess-generation" in text
    assert "aegis-mp-reassess-valid 0" in text


def test_military_reassess_cannot_advance_scouting_generation():
    text = read("AEGIS-scouting-threat-v0.per")
    block = text[text.index("; Military Production is downstream"):]
    block = block[:block.index("; A fresh World Model generation")]
    assert "aegis-st-generation g:= aegis-mp" not in block
    assert "aegis-st-generation g:+" not in block
    assert "aegis-wm-generation" not in block


def test_new_scouting_generation_remains_world_model_owned():
    text = read("AEGIS-scouting-threat-v0.per")
    assert "aegis-wm-valid == 1" in text
    assert "aegis-st-generation != aegis-wm-generation" in text
    assert "aegis-st-generation g:= aegis-wm-generation" in text


def test_reassess_ack_is_one_shot_and_generation_exact():
    text = read("AEGIS-scouting-threat-v0.per")
    start = text.index("; Military Production is downstream")
    end = text.index("; A fresh World Model generation")
    block = text[start:end]
    assert block.count("aegis-mp-reassess-valid == 1") == 1
    assert block.count("aegis-st-mp-reassess-generation != aegis-mp-reassess-generation") == 1
    assert block.count("aegis-st-mp-reassess-generation g:= aegis-mp-reassess-generation") == 1
    assert block.count("aegis-mp-reassess-valid 0") == 1


def test_military_production_selector_is_initialized_before_authorization():
    text = read("AEGIS-military-production-v0.per")
    init_start = text.index("; ----------------------------- initialization")
    grant_start = text.index("; Physical production requires producer authorization")
    init = text[init_start:grant_start]
    assert "set-goal aegis-mp-unit aegis-mp-unit-spearman" in init
    assert init.index("set-goal aegis-mp-unit aegis-mp-unit-spearman") < init.index("set-goal aegis-mp-stage aegis-mp-stage-idle")


def test_military_production_reassess_does_not_select_strategy():
    text = read("AEGIS-scouting-threat-v0.per")
    start = text.index("; Military Production is downstream")
    end = text.index("; A fresh World Model generation")
    block = text[start:end]
    forbidden = [
        "aegis-st-threat aegis-st-threat-cavalry",
        "aegis-st-threat aegis-st-threat-none",
        "aegis-st-confidence",
    ]
    for token in forbidden:
        assert token not in block


def test_namespace_registration_is_unique():
    ns = (ROOT / "docs/AEGIS_GOAL_NAMESPACE_MAP_2026-09-11.md").read_text(encoding="utf-8")
    assert "| 772–773 | MP |" in ns
    assert "| 782–783 | ST |" in ns
    assert "| 784–785 | MC |" in ns
    assert "| 786–787 | ST |" in ns
    assert "| 788–792 | MP |" in ns
    assert "| 793–794 | MPA |" in ns
    assert "| 795–805 | MP |" in ns
    assert "795–805" in ns


def test_no_central_reassessment_controller_introduced():
    assert not (SRC / "AEGIS-reassessment-controller-v0.per").exists()
