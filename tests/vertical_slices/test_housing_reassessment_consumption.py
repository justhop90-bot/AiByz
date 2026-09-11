"""Static contract tests for the housing REASSESS consumer.

These tests validate source ownership and generation invariants only. They do not
claim target-build runtime qualification.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SOURCE / name).read_text(encoding="utf-8")


def test_housing_publishes_generation_keyed_reassess():
    housing = read("AEGIS-housing-construction-v0.per")
    assert "aegis-hc-reassess-generation 764" in housing
    assert "aegis-hc-reassess-valid 765" in housing
    assert "aegis-hc-reassess-generation != aegis-hc-generation" in housing
    assert "up-modify-goal aegis-hc-reassess-generation g:= aegis-hc-generation" in housing


def test_civilian_demand_acknowledges_housing_once():
    demand = read("AEGIS-civilian-demand-v0.per")
    assert "aegis-civ-housing-reassess-generation 776" in demand
    assert "aegis-civ-housing-reassess-valid 777" in demand
    assert "aegis-hc-reassess-valid == 1" in demand
    assert "aegis-hc-reassess-generation == aegis-hc-generation" in demand
    assert "aegis-civ-housing-reassess-generation != aegis-hc-reassess-generation" in demand
    assert "up-modify-goal aegis-civ-housing-reassess-generation g:= aegis-hc-reassess-generation" in demand
    assert "set-goal aegis-hc-reassess-valid 0" in demand


def test_housing_ack_does_not_advance_civilian_generation():
    demand = read("AEGIS-civilian-demand-v0.per")
    section = demand.split("Consume the housing-construction REASSESS publication exactly once.", 1)[1]
    section = section.split("; Consume only a qualified civilization-state generation", 1)[0]
    assert "aegis-civ-demand-generation" not in section
    assert "aegis-cs-generation" not in section
    assert "g:+" not in section


def test_new_civilian_generation_remains_owned_by_civilization_state():
    demand = read("AEGIS-civilian-demand-v0.per")
    assert "aegis-cs-valid == 1" in demand
    assert "aegis-cs-generation != aegis-civ-demand-generation" in demand
    assert "up-modify-goal aegis-civ-demand-generation g:= aegis-cs-generation" in demand
    assert "up-modify-goal aegis-civ-demand-generation g:+" not in demand
    assert "set-goal aegis-civ-demand-generation" not in demand


def test_housing_admission_requires_new_demand_and_no_active_lifecycle():
    housing = read("AEGIS-housing-construction-v0.per")
    assert "aegis-hc-generation != aegis-civ-demand-generation" in housing
    assert "aegis-hc-valid == 0" in housing
    assert "aegis-hc-request-id g:= aegis-civ-demand-generation" in housing


def test_housing_authorization_is_single_use():
    housing = read("AEGIS-housing-construction-v0.per")
    assert "aegis-hc-authorization-valid == 1" in housing
    assert "(build house)" in housing
    assert "set-goal aegis-hc-authorization-valid 0" in housing


def test_housing_world_evidence_cannot_be_promoted_without_causal_evidence():
    housing = read("AEGIS-housing-construction-v0.per")
    assert "aegis-hc-world-evidence == 1" in housing
    assert "aegis-hc-causal-evidence == 1" in housing
    assert "aegis-hc-failure-causality-unproven" in housing


def test_no_housing_reassess_controller_exists():
    names = [p.name.lower() for p in SOURCE.glob("*.per")]
    assert not any("housing-reassess-controller" in name for name in names)
    assert not any("reassessment-controller" in name for name in names)
