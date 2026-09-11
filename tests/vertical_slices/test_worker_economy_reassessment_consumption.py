"""Static contract tests for worker-economy REASSESS consumption.

These tests validate source-level ownership and evidence-preserving generation
rules. They do not claim target-build runtime qualification.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SOURCE / name).read_text(encoding="utf-8")


def test_worker_role_vector_owns_worker_economy_reassess_acknowledgement():
    wrv = read("AEGIS-worker-role-vector-v0.per")
    assert "aegis-wrv-reassess-generation 778" in wrv
    assert "aegis-wrv-reassess-valid 779" in wrv
    assert "aegis-wtv-reassess-valid == 1" in wrv
    assert "aegis-wtv-reassess-generation == aegis-wtv-generation" in wrv
    assert "aegis-wrv-reassess-generation != aegis-wtv-reassess-generation" in wrv
    assert "up-modify-goal aegis-wrv-reassess-generation g:= aegis-wtv-reassess-generation" in wrv
    assert "set-goal aegis-wrv-reassess-valid 0" in wrv


def test_worker_role_vector_generation_remains_upstream_owned():
    wrv = read("AEGIS-worker-role-vector-v0.per")
    assert "aegis-wrc-valid == 1" in wrv
    assert "aegis-wrv-generation != aegis-wrc-generation" in wrv
    assert "up-modify-goal aegis-wrv-generation g:= aegis-wrc-generation" in wrv
    assert "up-modify-goal aegis-wrv-generation g:+" not in wrv
    assert "set-goal aegis-wrv-generation" not in wrv


def test_worker_role_vector_resets_ack_on_new_census_generation():
    wrv = read("AEGIS-worker-role-vector-v0.per")
    assert "set-goal aegis-wrv-reassess-valid 0" in wrv
    assert "up-modify-goal aegis-wrv-observed-at g:= aegis-wrc-observed-at" in wrv


def test_worker_verification_publisher_remains_idempotent():
    wtv = read("AEGIS-worker-task-verification-v0.per")
    assert "aegis-wtv-reassess-generation 760" in wtv
    assert "aegis-wtv-reassess-valid 761" in wtv
    assert "aegis-wtv-reassess-generation != aegis-wtv-generation" in wtv
    assert "up-modify-goal aegis-wtv-reassess-generation g:= aegis-wtv-generation" in wtv
    assert "set-goal aegis-wtv-reassess-valid 1" in wtv


def test_worker_economy_chain_waits_for_new_census_before_new_demand():
    wrc = read("AEGIS-worker-role-census-v0.per")
    wrv = read("AEGIS-worker-role-vector-v0.per")
    ed = read("AEGIS-economic-demand-v0.per")
    eda = read("AEGIS-economic-demand-arbitration-v0.per")
    wts = read("AEGIS-worker-target-selection-v0.per")
    wtc = read("AEGIS-worker-task-command-v0.per")

    assert "up-modify-goal aegis-wrc-generation g:+ 1" in wrc
    assert "aegis-wrv-generation != aegis-wrc-generation" in wrv
    assert "aegis-ed-generation != aegis-wrv-generation" in ed
    assert "aegis-eda-generation != aegis-ed-generation" in eda
    assert "aegis-wts-generation != aegis-eda-generation" in wts
    assert "aegis-wtc-generation != aegis-wts-generation" in wtc
    assert "aegis-wtc-valid == 0" in wtc


def test_worker_economy_preserves_pending_and_causal_uncertainty():
    wtv = read("AEGIS-worker-task-verification-v0.per")
    assert "aegis-wtv-result-unknown 0" in wtv
    assert "aegis-wtv-stage-confirmed" in wtv
    assert "aegis-wtv-stage-failed" in wtv
    assert "aegis-wtv-failure-identity-mismatch 4" in wtv
    assert "aegis-wtv-result aegis-wtv-result-task-observed" in wtv


def test_no_worker_economy_reassess_controller_exists():
    names = [p.name.lower() for p in SOURCE.glob("*.per")]
    assert not any("reassess-controller" in name for name in names)
    assert not any("reassessment-controller" in name for name in names)
