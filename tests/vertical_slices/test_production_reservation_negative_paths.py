from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "AegisProm"
RESERVATION = SRC / "AEGIS-production-reservation-authority-v0.per"


def read() -> str:
    return RESERVATION.read_text(encoding="utf-8")


def rule_containing(content: str, marker: str) -> str:
    start = content.find(marker)
    assert start >= 0, f"missing marker: {marker}"
    end = content.find("; ----------------", start + len(marker))
    if end < 0:
        end = len(content)
    return content[start:end]


def test_reservation_authority_rules_remain_well_formed():
    content = read()
    assert "(defrule" in content
    assert "\ndefrule" not in content


def test_cr_grant_requires_explicit_spearman_unit_binding():
    content = read()
    grant = rule_containing(content, "; ------------------------------ grant: CR")
    assert "aegis-cr-unit == aegis-pr-unit-spearman-line" in grant
    assert "set-goal aegis-pr-state aegis-pr-state-reserved" in grant


def test_wrong_unit_cannot_reach_cr_reservation_state():
    content = read()
    grant = rule_containing(content, "; ------------------------------ grant: CR")
    assert "aegis-cr-unit == aegis-pr-unit-spearman-line" in grant
    assert grant.count("set-goal aegis-pr-state aegis-pr-state-reserved") == 1


def test_stale_generation_fences_reserved_and_in_flight():
    content = read()
    assert "aegis-pr-authorization-generation != aegis-st-generation" in content
    stale = rule_containing(content, "; ------------------------- stale / expiry fences")
    assert "aegis-pr-release-stale-generation" in stale
    assert "aegis-pr-state-release-pending" in stale


def test_zero_expiry_fails_closed_without_silent_renewal():
    content = read()
    expiry = rule_containing(content, "; ------------------------- stale / expiry fences")
    assert "aegis-pr-expiry == 0" in expiry
    assert "aegis-pr-release-expired" in expiry
    assert "aegis-pr-state-release-pending" in expiry
    assert "aegis-pr-expiry g:=" not in expiry


def test_duplicate_request_cannot_claim_a_nonfree_resource():
    content = read()
    for producer in ("aegis-mp", "aegis-cr"):
        grant = rule_containing(content, f"; ------------------------------ grant: {'MP' if producer == 'aegis-mp' else 'CR'}")
        assert "aegis-pr-state == aegis-pr-state-free" in grant
        assert "aegis-pr-valid == 0" in grant
    assert content.count("aegis-pr-state == aegis-pr-state-free") >= 2
    assert content.count("aegis-pr-valid == 0") >= 2


def test_release_requires_identity_and_generation_continuity():
    content = read()
    release = rule_containing(content, "; ------------------------------- release")
    assert "aegis-pr-reservation-id == aegis-pr-request-id" in release
    assert "aegis-pr-request-id == aegis-pr-authorization-id" in release
    assert "aegis-pr-authorization-generation == aegis-pr-generation" in release
    assert "set-goal aegis-pr-state aegis-pr-state-released" in release


def test_invalid_release_cannot_release_active_reservation():
    content = read()
    release = rule_containing(content, "; ------------------------------- release")
    assert "aegis-pr-state == aegis-pr-state-release-pending" in release
    assert "aegis-pr-state == aegis-pr-state-reserved" not in release
    assert "aegis-pr-state == aegis-pr-state-in-flight" not in release


def test_repeated_release_is_idempotent():
    content = read()
    release = rule_containing(content, "; ------------------------------- release")
    assert "set-goal aegis-pr-valid 0" in release
    assert "aegis-pr-state == aegis-pr-state-released" in content
    assert "aegis-pr-valid != 0" in content
