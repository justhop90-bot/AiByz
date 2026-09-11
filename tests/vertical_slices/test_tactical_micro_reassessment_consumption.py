"""Static contract tests for Tactical Micro REASSESS consumption.

These tests validate source ownership and generation/evidence invariants only.
They do not claim target-build AoE2DE runtime qualification.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SOURCE / name).read_text(encoding="utf-8")


def test_micro_verification_publishes_generation_keyed_reassess():
    mv = read("AEGIS-micro-verification-v0.per")
    assert "aegis-mv-reassess-generation 770" in mv
    assert "aegis-mv-reassess-valid 771" in mv
    assert "aegis-mv-reassess-generation != aegis-mv-generation" in mv
    assert "up-modify-goal aegis-mv-reassess-generation g:= aegis-mv-generation" in mv


def test_micro_control_owns_downstream_reassess_acknowledgement():
    mc = read("AEGIS-micro-control-v0.per")
    assert "aegis-mc-reassess-generation 784" in mc
    assert "aegis-mc-reassess-valid 785" in mc
    assert "aegis-mv-reassess-valid == 1" in mc
    assert "aegis-mv-reassess-generation == aegis-mv-generation" in mc
    assert "aegis-mc-reassess-generation != aegis-mv-reassess-generation" in mc
    assert "up-modify-goal aegis-mc-reassess-generation g:= aegis-mv-reassess-generation" in mc
    assert "set-goal aegis-mc-reassess-valid 0" in mc


def test_reassess_does_not_create_micro_control_generation():
    mc = read("AEGIS-micro-control-v0.per")
    assert "up-modify-goal aegis-mc-generation g:= aegis-mv-reassess-generation" not in mc
    assert "up-modify-goal aegis-mc-generation g:+" not in mc
    assert "aegis-wm-valid == 1" in mc
    assert "aegis-mc-generation != aegis-wm-generation" in mc
    assert "up-modify-goal aegis-mc-generation g:= aegis-wm-generation" in mc


def test_new_world_frame_cannot_replace_active_micro_request():
    mc = read("AEGIS-micro-control-v0.per")
    assert "aegis-mc-valid == 0" in mc
    assert "aegis-mc-generation != aegis-wm-generation" in mc


def test_reassess_ack_is_not_strategy_selection():
    mc = read("AEGIS-micro-control-v0.per")
    ack_start = mc.index("Tactical Micro REASSESS")
    ack_end = mc.index("Threat recovery", ack_start)
    ack = mc[ack_start:ack_end]
    assert "set-goal aegis-mc-intent" not in ack
    assert "set-goal aegis-mc-stage" not in ack


def test_micro_verification_does_not_promote_unknown_to_success():
    mv = read("AEGIS-micro-verification-v0.per")
    assert "aegis-mv-result aegis-mv-result-unknown" in mv
    assert "set-goal aegis-mv-world-evidence 1" in mv
    # Causal evidence remains explicitly unproven in this vertical.
    assert "set-goal aegis-mv-causal-evidence 1" not in mv
    assert "set-goal aegis-mv-causal-evidence 0" in mv


def test_no_central_reassessment_controller_source_exists():
    names = [p.name.lower() for p in SOURCE.glob("*.per")]
    assert not any("reassess-controller" in name for name in names)
    assert not any("reassessment-controller" in name for name in names)
