from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "AegisProm"


def read(name: str) -> str:
    return (SRC / name).read_text(encoding="utf-8")


def test_certified_reservation_namespace_is_exact():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    expected = {
        806: "aegis-pr-generation",
        807: "aegis-pr-state",
        808: "aegis-pr-reservation-id",
        809: "aegis-pr-owner",
        810: "aegis-pr-request-id",
        811: "aegis-pr-authorization-id",
        812: "aegis-pr-authorization-generation",
        813: "aegis-pr-valid",
        814: "aegis-pr-expiry",
        815: "aegis-pr-resource-key",
        816: "aegis-pr-unit-line",
        817: "aegis-pr-release-reason",
    }
    for slot, symbol in expected.items():
        assert f"(defconst {symbol} {slot})" in pr


def test_reservation_state_machine_and_release_reasons_exist():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    for state in (
        "aegis-pr-state-free",
        "aegis-pr-state-reserved",
        "aegis-pr-state-in-flight",
        "aegis-pr-state-release-pending",
        "aegis-pr-state-released",
    ):
        assert state in pr
    for reason in (
        "aegis-pr-release-completed",
        "aegis-pr-release-failed",
        "aegis-pr-release-expired",
        "aegis-pr-release-stale-generation",
        "aegis-pr-release-superseded",
    ):
        assert reason in pr


def test_reservation_never_executes_physical_production():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    assert "up-train" not in pr
    assert "up-research" not in pr
    assert "set-goal aegis-mp-causal-evidence" not in pr
    assert "set-goal aegis-cr-causal-evidence" not in pr


def test_reservation_is_bound_to_producer_authorization():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    for producer in ("aegis-mp", "aegis-cr"):
        assert f"{producer}-valid == 1" in pr
        assert f"{producer}-authorization-valid == 1" in pr
        assert f"{producer}-authorization-generation == aegis-st-generation" in pr
        assert f"{producer}-authorization-id == {producer}-request-id" in pr


def test_reservation_is_exclusive_and_identity_bound():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    assert "aegis-pr-state == aegis-pr-state-free" in pr
    assert "aegis-pr-valid == 0" in pr
    assert "aegis-pr-reservation-id" in pr
    assert "aegis-pr-owner" in pr
    assert "aegis-pr-request-id" in pr
    assert "aegis-pr-authorization-id" in pr
    assert "aegis-pr-authorization-generation" in pr
    assert "aegis-pr-resource-key" in pr
    assert "aegis-pr-unit-line" in pr


def test_stale_generation_and_expiry_fail_closed():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    assert "aegis-pr-authorization-generation != aegis-st-generation" in pr
    assert "set-goal aegis-pr-release-reason aegis-pr-release-stale-generation" in pr
    assert "aegis-pr-expiry == 0" in pr
    assert "set-goal aegis-pr-release-reason aegis-pr-release-expired" in pr


def test_producer_physical_dispatch_requires_reservation():
    mp = read("AEGIS-military-production-v0.per")
    cr = read("AEGIS-cavalry-response-v0.per")
    for content, owner in (
        (mp, "aegis-pr-owner-military-production"),
        (cr, "aegis-pr-owner-cavalry-response"),
    ):
        assert "aegis-pr-state == aegis-pr-state-reserved" in content
        assert "aegis-pr-valid == 1" in content
        assert f"aegis-pr-owner == {owner}" in content
        assert "aegis-pr-request-id" in content
        assert "aegis-pr-authorization-id" in content
        assert "aegis-pr-authorization-generation" in content
        assert "aegis-pr-resource-key == aegis-pr-resource-spearman-line" in content
        assert "aegis-pr-unit-line == aegis-pr-unit-spearman-line" in content


def test_reservation_release_is_identity_checked_and_idempotent():
    pr = read("AEGIS-production-reservation-authority-v0.per")
    assert "aegis-pr-reservation-id == aegis-pr-request-id" in pr
    assert "aegis-pr-request-id == aegis-pr-authorization-id" in pr
    assert "aegis-pr-authorization-generation == aegis-pr-generation" in pr
    assert "aegis-pr-state aegis-pr-state-released" in pr
    assert "aegis-pr-valid != 0" in pr
