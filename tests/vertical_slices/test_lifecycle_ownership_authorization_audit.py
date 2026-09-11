from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SRC / name).read_text(encoding="utf-8")


def test_all_seven_reassess_boundaries_remain_present():
    publishers = {
        "AEGIS-worker-task-verification-v0.per": (760, 761),
        "AEGIS-civilian-lifecycle-reconciler-v0.per": (762, 763),
        "AEGIS-housing-construction-v0.per": (764, 765),
        "AEGIS-research-age-v0.per": (766, 767),
        "AEGIS-cavalry-response-v0.per": (768, 769),
        "AEGIS-micro-verification-v0.per": (770, 771),
        "AEGIS-military-production-v0.per": (772, 773),
    }
    for name, slots in publishers.items():
        content = read(name)
        for slot in slots:
            assert f"{slot}" in content
        assert "reassess-valid 1" in content


def test_reassess_consumers_are_unique_and_exact():
    consumers = [
        ("AEGIS-civilian-demand-v0.per", "aegis-vr-reassess-valid", 774, 775),
        ("AEGIS-civilian-demand-v0.per", "aegis-hc-reassess-valid", 776, 777),
        ("AEGIS-worker-role-vector-v0.per", "aegis-wtv-reassess-valid", 778, 779),
        ("AEGIS-civilization-state-v0.per", "aegis-ra-reassess-valid", 780, 781),
        ("AEGIS-scouting-threat-v0.per", "aegis-cr-reassess-valid", 782, 783),
        ("AEGIS-micro-control-v0.per", "aegis-mv-reassess-valid", 784, 785),
        ("AEGIS-scouting-threat-v0.per", "aegis-mp-reassess-valid", 786, 787),
    ]
    for name, publisher_token, generation_slot, valid_slot in consumers:
        content = read(name)
        assert str(generation_slot) in content
        assert str(valid_slot) in content
        assert f"{publisher_token} == 1" in content
        assert f"set-goal {publisher_token} 0" in content


def test_tactical_micro_lifecycle_owner_closes_itself():
    mc = read("AEGIS-micro-control-v0.per")
    mpa = read("AEGIS-micro-physical-adapter-v0.per")
    mv = read("AEGIS-micro-verification-v0.per")

    assert "set-goal aegis-mc-valid 0" in mc
    assert "aegis-mv-reassess-valid == 1" in mc
    assert "aegis-mpa-dispatch-valid == 1" in mc
    assert "aegis-mpa-dispatch-generation == aegis-mc-request-generation" in mc

    # Physical adapter owns dispatch evidence, not MC lifecycle state.
    assert "set-goal aegis-mc-stage" not in mpa
    assert "set-goal aegis-mc-valid" not in mpa
    assert "up-modify-goal aegis-mc-attempts" not in mpa

    # Verification must not close or invalidate MC.
    assert "set-goal aegis-mc-valid 0" not in mv
    assert "up-modify-goal aegis-mc-valid" not in mv


def test_military_production_selector_is_explicitly_initialized():
    mp = read("AEGIS-military-production-v0.per")
    assert "set-goal aegis-mp-unit aegis-mp-unit-spearman" in mp
    assert "aegis-mp-unit == aegis-mp-unit-spearman" in mp
    assert "aegis-mp-unit == aegis-mp-unit-camel" not in mp.split("; ----------------------------- initialization", 1)[1].split("; ------------------------------ grant", 1)[0]


def test_military_production_has_explicit_single_use_authorization():
    mp = read("AEGIS-military-production-v0.per")
    for symbol in (
        "aegis-mp-request-id",
        "aegis-mp-authorization-id",
        "aegis-mp-authorization-generation",
        "aegis-mp-authorization-valid",
        "aegis-mp-authorization-expiry",
    ):
        assert symbol in mp

    assert "set-goal aegis-mp-authorization-valid 1" in mp
    assert "set-goal aegis-mp-authorization-valid 0" in mp
    assert "aegis-mp-authorization-generation == aegis-st-generation" in mp
    assert "aegis-mp-authorization-id == aegis-mp-request-id" in mp
    assert "up-train escrow-state c: spearman-line" in mp


def test_housing_does_not_mutate_civilian_policy_owner():
    hc = read("AEGIS-housing-construction-v0.per")
    assert "set-goal aegis-civ-housing-demand" not in hc
    assert "up-modify-goal aegis-civ-housing-demand" not in hc


def test_physical_actions_have_current_authorization_boundaries():
    vp = read("AEGIS-villager-production-v0.per")
    hc = read("AEGIS-housing-construction-v0.per")
    wtc = read("AEGIS-worker-task-command-v0.per")
    cr = read("AEGIS-cavalry-response-v0.per")
    ra = read("AEGIS-research-age-v0.per")
    mp = read("AEGIS-military-production-v0.per")
    mpa = read("AEGIS-micro-physical-adapter-v0.per")

    assert "aegis-vp-authorization-valid == 1" in vp
    assert "set-goal aegis-vp-authorization-valid 0" in vp
    assert "aegis-hc-authorization-valid == 1" in hc
    assert "set-goal aegis-hc-authorization-valid 0" in hc
    assert "aegis-wtc-authorization-valid == 1" in wtc
    assert "set-goal aegis-wtc-authorization-valid 0" in wtc
    assert "aegis-cr-authorization-valid == 1" in cr
    assert "set-goal aegis-cr-authorization-valid 0" in cr
    assert "aegis-ra-authorization-valid == 1" in ra
    assert "set-goal aegis-ra-authorization-valid 0" in ra
    assert "aegis-mp-authorization-valid == 1" in mp
    assert "set-goal aegis-mp-authorization-valid 0" in mp
    assert "aegis-me-authorized == 1" in mpa
    assert "set-goal aegis-me-authorized 0" in mpa


def test_no_reassess_generation_shortcut_or_strategy_selection():
    for path in SRC.glob("*.per"):
        content = path.read_text(encoding="utf-8")
        if "reassess-valid" not in content:
            continue
        assert "reassess-generation g:+" not in content
        for line in content.splitlines():
            if "reassess-valid 1" in line:
                assert "intent" not in line
                assert "strategy" not in line


def test_no_monolithic_reassessment_controller():
    names = [p.name.lower() for p in SRC.glob("*.per") if "reassess-valid" in p.read_text(encoding="utf-8")]
    assert len(names) >= 7
    assert not any("reassessment-controller" in name for name in names)
