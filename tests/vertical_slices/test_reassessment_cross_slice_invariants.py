from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "AegisProm"

PUBLISHERS = [
    ("AEGIS-worker-task-verification-v0.per", 760, 761),
    ("AEGIS-civilian-lifecycle-reconciler-v0.per", 762, 763),
    ("AEGIS-housing-construction-v0.per", 764, 765),
    ("AEGIS-research-age-v0.per", 766, 767),
    ("AEGIS-cavalry-response-v0.per", 768, 769),
    ("AEGIS-micro-verification-v0.per", 770, 771),
    ("AEGIS-military-production-v0.per", 772, 773),
]

CONSUMERS = [
    ("AEGIS-civilian-demand-v0.per", 774, 775, "aegis-vr-reassess-valid"),
    ("AEGIS-civilian-demand-v0.per", 776, 777, "aegis-hc-reassess-valid"),
    ("AEGIS-worker-role-vector-v0.per", 778, 779, "aegis-wtv-reassess-valid"),
    ("AEGIS-civilization-state-v0.per", 780, 781, "aegis-ra-reassess-valid"),
    ("AEGIS-scouting-threat-v0.per", 782, 783, "aegis-cr-reassess-valid"),
    ("AEGIS-micro-control-v0.per", 784, 785, "aegis-mv-reassess-valid"),
    ("AEGIS-scouting-threat-v0.per", 786, 787, "aegis-mp-reassess-valid"),
]


def text(name):
    return (SRC / name).read_text(encoding="utf-8")


def test_all_publisher_slots_exist_in_source():
    for name, generation, valid in PUBLISHERS:
        content = text(name)
        assert f"{generation}" in content
        assert f"{valid}" in content


def test_all_consumer_slots_exist_in_source():
    for name, generation, valid, upstream_token in CONSUMERS:
        content = text(name)
        assert f"{generation}" in content
        assert f"{valid}" in content
        assert upstream_token in content


def test_no_reassess_publisher_selects_strategy():
    for name, _, _ in PUBLISHERS:
        content = text(name)
        assert "reassess-generation" in content
        for line in content.splitlines():
            if "reassess-valid 1" in line:
                assert "intent" not in line
                assert "strategy" not in line


def test_tactical_verification_does_not_write_micro_control_valid():
    content = text("AEGIS-micro-verification-v0.per")
    assert "set-goal aegis-mc-valid 0" not in content
    assert "up-modify-goal aegis-mc-valid" not in content


def test_micro_control_owns_tactical_lifecycle_closure():
    content = text("AEGIS-micro-control-v0.per")
    assert "aegis-mv-reassess-valid == 1" in content
    assert "set-goal aegis-mc-valid 0" in content


def test_reassess_does_not_increment_consumer_generation():
    targets = {
        "AEGIS-civilian-demand-v0.per",
        "AEGIS-worker-role-vector-v0.per",
        "AEGIS-civilization-state-v0.per",
        "AEGIS-scouting-threat-v0.per",
        "AEGIS-micro-control-v0.per",
    }
    for name in targets:
        assert "reassess-generation g:+" not in text(name)


def test_no_monolithic_reassessment_controller():
    reassess_modules = []
    for path in SRC.glob("*.per"):
        content = path.read_text(encoding="utf-8")
        if "reassess-valid" in content:
            reassess_modules.append(path.name)
    assert len(reassess_modules) >= 7
    assert not any("reassessment-controller" in name.lower() for name in reassess_modules)
