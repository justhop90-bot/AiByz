"""Static contract tests for downstream REASSESS consumption.

These tests intentionally validate architecture/ownership rules without claiming
that pure .per runtime behavior has been qualified in target-build execution.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm"

VERTICALS = {
    "worker_economy": [
        "AEGIS-worker-task-verification-v0.per",
        "AEGIS-economic-demand-v0.per",
        "AEGIS-worker-target-selection-v0.per",
    ],
    "villager_production": [
        "AEGIS-civilian-lifecycle-reconciler-v0.per",
        "AEGIS-civilian-demand-v0.per",
        "AEGIS-villager-production-v0.per",
    ],
    "housing": [
        "AEGIS-housing-construction-v0.per",
        "AEGIS-civilian-demand-v0.per",
    ],
    "age_transition": [
        "AEGIS-research-age-v0.per",
        "AEGIS-civilization-state-v0.per",
    ],
    "anti_cavalry": [
        "AEGIS-cavalry-response-v0.per",
        "AEGIS-scouting-threat-v0.per",
    ],
    "tactical_micro": [
        "AEGIS-micro-verification-v0.per",
        "AEGIS-micro-control-v0.per",
    ],
    "military_production": [
        "AEGIS-military-production-v0.per",
    ],
}

REASSESS_RANGES = {
    "worker_economy": (760, 761),
    "villager_production": (762, 763),
    "housing": (764, 765),
    "age_transition": (766, 767),
    "anti_cavalry": (768, 769),
    "tactical_micro": (770, 771),
    "military_production": (772, 773),
}


def read(path: str) -> str:
    return (SOURCE / path).read_text(encoding="utf-8")


def test_all_registered_verticals_have_local_reassess_publishers():
    for vertical, files in VERTICALS.items():
        publisher = read(files[0])
        gen, valid = REASSESS_RANGES[vertical]
        assert f"reassess-generation {gen}" in publisher
        assert f"reassess-valid {valid}" in publisher
        assert "reassess-generation !=" in publisher
        assert "set-goal" in publisher and "reassess-valid 1" in publisher


def test_publishers_are_idempotent_on_lifecycle_generation():
    for files in VERTICALS.values():
        publisher = read(files[0])
        assert "reassess-generation !=" in publisher
        assert "g:= aegis-" in publisher


def test_civilian_demand_acknowledges_villager_reassess_once():
    demand = read("AEGIS-civilian-demand-v0.per")
    assert "aegis-civ-reassess-generation 774" in demand
    assert "aegis-civ-reassess-valid 775" in demand
    assert "aegis-vr-reassess-valid == 1" in demand
    assert "aegis-vr-reassess-generation == aegis-vr-generation" in demand
    assert "aegis-civ-reassess-generation != aegis-vr-reassess-generation" in demand
    assert "up-modify-goal aegis-civ-reassess-generation g:= aegis-vr-reassess-generation" in demand
    assert "set-goal aegis-civ-reassess-valid 1" in demand
    assert "set-goal aegis-vr-reassess-valid 0" in demand


def test_civilian_demand_new_generation_is_upstream_only():
    demand = read("AEGIS-civilian-demand-v0.per")
    assert "aegis-cs-valid == 1" in demand
    assert "aegis-cs-generation != aegis-civ-demand-generation" in demand
    assert "up-modify-goal aegis-civ-demand-generation g:+" not in demand
    assert "set-goal aegis-civ-demand-generation" not in demand
    assert "up-modify-goal aegis-civ-demand-generation g:= aegis-cs-generation" in demand


def test_villager_production_cannot_replace_an_active_request():
    vp = read("AEGIS-villager-production-v0.per")
    assert "aegis-vp-valid == 0" in vp
    assert "aegis-vp-generation != aegis-civ-demand-generation" in vp
    assert "aegis-vp-request-id g:= aegis-civ-demand-generation" in vp


def test_villager_production_authorization_is_single_use():
    vp = read("AEGIS-villager-production-v0.per")
    assert "aegis-vp-authorization-valid == 1" in vp
    assert "set-goal aegis-vp-authorization-valid 0" in vp
    assert "up-train escrow-state c: villager" in vp


def test_villager_completion_does_not_promote_pending_without_causal_evidence():
    vr = read("AEGIS-civilian-lifecycle-reconciler-v0.per")
    assert "aegis-vr-causal-evidence == 1" in vr
    assert "set-goal aegis-vr-causal-evidence 0" in vr
    assert "set-goal aegis-vr-stage aegis-vr-stage-confirmed" in vr
    # The source contains no writer that establishes causal evidence yet.
    assert vr.count("aegis-vr-causal-evidence") == 3


def test_villager_reassess_publishes_lifecycle_generation():
    vr = read("AEGIS-civilian-lifecycle-reconciler-v0.per")
    assert "aegis-vr-reassess-generation 762" in vr
    assert "aegis-vr-reassess-valid 763" in vr
    assert "aegis-vr-reassess-generation != aegis-vr-generation" in vr
    assert "up-modify-goal aegis-vr-reassess-generation g:= aegis-vr-generation" in vr


def test_reassess_contract_forbids_direct_strategy_selection():
    doc = (ROOT / "docs" / "AEGIS_REASSESSMENT_CONSUMPTION_PASS_2026-09-11.md").read_text(
        encoding="utf-8"
    )
    assert "never select the next strategy at the reassessment boundary" in doc
    assert "No module owns all seven reassessment signals" in doc


def test_military_production_remains_candidate_blocked():
    registry = (ROOT / "schemas" / "AEGIS-VERTICAL-SLICE-CONTRACTS-1.0.json").read_text(
        encoding="utf-8"
    )
    assert '"military_production"' in registry
    assert '"status":"CANDIDATE_BLOCKED"' in registry
    assert '"qualification_status":"NOT_QUALIFIED"' in registry


def test_no_global_reassessment_controller_source_exists():
    names = [p.name.lower() for p in SOURCE.glob("*.per")]
    assert not any("reassess-controller" in name for name in names)
    assert not any("reassessment-controller" in name for name in names)
