"""Static source-contract tests for Anti-Cavalry REASSESS consumption.

These tests validate ownership, generation identity, one-shot consumption,
and namespace safety. They do not claim target-build AoE2DE qualification.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SOURCE / name).read_text(encoding="utf-8")


def test_anti_cavalry_publisher_exists_and_is_generation_keyed():
    cr = read("AEGIS-cavalry-response-v0.per")
    assert "aegis-cr-reassess-generation 768" in cr
    assert "aegis-cr-reassess-valid 769" in cr
    assert "aegis-cr-reassess-generation != aegis-cr-generation" in cr
    assert "up-modify-goal aegis-cr-reassess-generation g:= aegis-cr-generation" in cr


def test_scouting_threat_owns_downstream_acknowledgement():
    st = read("AEGIS-scouting-threat-v0.per")
    assert "aegis-st-reassess-generation 782" in st
    assert "aegis-st-reassess-valid 783" in st
    assert "aegis-cr-reassess-valid == 1" in st
    assert "aegis-cr-reassess-generation == aegis-cr-generation" in st
    assert "aegis-st-reassess-generation != aegis-cr-reassess-generation" in st
    assert "up-modify-goal aegis-st-reassess-generation g:= aegis-cr-reassess-generation" in st
    assert "set-goal aegis-st-reassess-valid 1" in st
    assert "set-goal aegis-cr-reassess-valid 0" in st


def test_reassess_does_not_create_a_new_threat_generation():
    st = read("AEGIS-scouting-threat-v0.per")
    assert "up-modify-goal aegis-st-generation g:+" not in st
    assert "up-modify-goal aegis-st-generation g:= aegis-cr" not in st
    assert "up-modify-goal aegis-st-generation g:= aegis-wm-generation" in st


def test_new_threat_generation_remains_world_model_owned():
    st = read("AEGIS-scouting-threat-v0.per")
    assert "aegis-wm-valid == 1" in st
    assert "aegis-st-generation != aegis-wm-generation" in st
    assert "up-modify-goal aegis-st-generation g:= aegis-wm-generation" in st


def test_anti_cavalry_active_request_protection_remains_intact():
    cr = read("AEGIS-cavalry-response-v0.per")
    assert "aegis-cr-valid == 0" in cr
    assert "aegis-cr-generation != aegis-st-generation" in cr
    assert "aegis-cr-request-id g:= aegis-st-generation" in cr


def test_anti_cavalry_authorization_is_single_use():
    cr = read("AEGIS-cavalry-response-v0.per")
    assert "aegis-cr-authorization-valid == 1" in cr
    assert "set-goal aegis-cr-authorization-valid 0" in cr
    assert "up-train escrow-state c: spearman-line" in cr


def test_anti_cavalry_confirmation_remains_fail_closed_on_causality():
    cr = read("AEGIS-cavalry-response-v0.per")
    assert "aegis-cr-causal-evidence == 1" in cr
    assert "set-goal aegis-cr-causal-evidence 0" in cr
    assert "set-goal aegis-cr-stage aegis-cr-stage-confirmed" in cr
    assert cr.count("aegis-cr-causal-evidence") == 3


def test_namespace_repairs_are_registered():
    st = read("AEGIS-scouting-threat-v0.per")
    cr = read("AEGIS-cavalry-response-v0.per")
    namespace = (ROOT / "docs" / "AEGIS_GOAL_NAMESPACE_MAP_2026-09-11.md").read_text(encoding="utf-8")
    assert "642–649 | ST" in namespace
    assert "782–783 | ST" in namespace
    assert "650 | CR" in namespace
    assert "defconst aegis-st-generation 642" in st
    assert "defconst aegis-cr-failure 650" in cr


def test_no_central_reassessment_controller_is_introduced():
    names = [p.name.lower() for p in SOURCE.glob("*.per")]
    assert not any("reassess-controller" in name for name in names)
    assert not any("reassessment-controller" in name for name in names)
