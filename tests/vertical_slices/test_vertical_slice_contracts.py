import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "vertical_slice_validator"))
from vertical_slice_validator import load_registry, validate_vertical_slice


REGISTRY = load_registry()
SLICES = REGISTRY["contracts"]
CONTRACT_FIELDS = {"expected_stages", "owners", "required_evidence", "allowed_transitions"}


def valid_trace(vertical_id, generation=1, evidence_type="SYNTHETIC_TEST"):
    contract = SLICES[vertical_id]
    events = []
    request_id = "req-physical"
    for sequence, stage in enumerate(contract["stages"]):
        event = {
            "stage": stage,
            "generation": generation,
            "owner": contract["owners"][stage],
            "evidence_type": evidence_type,
            "sequence": sequence,
        }
        if stage == "AUTHORIZATION":
            event["request_id"] = request_id
            event["expires_at"] = sequence + 2
        elif stage == "PHYSICAL_REQUEST":
            event.update(authorized=True, request_id=request_id)
        elif stage == "ENGINE_ACCEPTED_PENDING":
            event["request_id"] = request_id
        elif stage == "WORLD_STATE_VERIFIED":
            event["world_state_evidence"] = True
            event["evidence_type"] = "TARGET_BUILD_RUNTIME"
        events.append(event)
    return {"vertical_id": vertical_id, "generation": generation, "events": events}


class TestAuthoritativeVerticalSliceContracts(unittest.TestCase):
    def test_registry_contains_exactly_six_bounded_verticals(self):
        self.assertEqual(set(SLICES), {
            "worker_economy",
            "villager_production",
            "housing",
            "age_transition",
            "anti_cavalry",
            "tactical_micro",
        })

    def test_complete_trace_uses_registry_not_trace_declared_stages(self):
        for vertical_id in SLICES:
            with self.subTest(slice=vertical_id):
                result = validate_vertical_slice(valid_trace(vertical_id))
                self.assertTrue(result["contract_valid"], result["errors"])

    def test_trace_cannot_shadow_authoritative_contract(self):
        for vertical_id in SLICES:
            with self.subTest(slice=vertical_id):
                broken = valid_trace(vertical_id)
                broken["expected_stages"] = []
                broken["owners"] = {}
                broken["required_evidence"] = {}
                broken["allowed_transitions"] = {}
                result = validate_vertical_slice(broken)
                self.assertFalse(result["contract_valid"])
                self.assertIn("VSL-013", {e["error_code"] for e in result["errors"]})

    def test_unknown_vertical_is_rejected(self):
        result = validate_vertical_slice({"vertical_id": "invented_slice", "events": []})
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-012", {e["error_code"] for e in result["errors"]})

    def test_missing_vertical_is_rejected(self):
        result = validate_vertical_slice({"events": []})
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-011", {e["error_code"] for e in result["errors"]})

    def test_forbidden_transition_is_rejected(self):
        for vertical_id in SLICES:
            with self.subTest(slice=vertical_id):
                broken = valid_trace(vertical_id)
                stages = [e["stage"] for e in broken["events"]]
                stages[1], stages[2] = stages[2], stages[1]
                for event, stage in zip(broken["events"], stages):
                    event["stage"] = stage
                result = validate_vertical_slice(broken)
                self.assertFalse(result["contract_valid"])
                self.assertIn("VSL-016", {e["error_code"] for e in result["errors"]})

    def test_owner_is_authoritative(self):
        broken = valid_trace("housing")
        broken["events"][0]["owner"] = "invented.owner"
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-019", {e["error_code"] for e in result["errors"]})

    def test_evidence_requirement_is_authoritative(self):
        broken = valid_trace("villager_production")
        broken["events"][0]["evidence_type"] = "INFERRED"
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-020", {e["error_code"] for e in result["errors"]})

    def test_pending_requires_physical_request_identity(self):
        broken = valid_trace("villager_production")
        pending = next(e for e in broken["events"] if e["stage"] == "ENGINE_ACCEPTED_PENDING")
        pending.pop("request_id")
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-004", {e["error_code"] for e in result["errors"]})

    def test_verification_requires_runtime_evidence(self):
        broken = valid_trace("housing")
        verified = next(e for e in broken["events"] if e["stage"] == "WORLD_STATE_VERIFIED")
        verified["evidence_type"] = "SYNTHETIC_TEST"
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-020", {e["error_code"] for e in result["errors"]})
        self.assertIn("VSL-027", {e["error_code"] for e in result["errors"]})

    def test_synthetic_contract_test_is_not_promotion(self):
        broken = valid_trace("anti_cavalry")
        for event in broken["events"]:
            if event["stage"] != "WORLD_STATE_VERIFIED":
                event["evidence_type"] = "SYNTHETIC_TEST"
        result = validate_vertical_slice(broken)
        self.assertTrue(result["contract_valid"], result["errors"])
        self.assertFalse(result["qualified"])

    def test_stale_generation_is_rejected(self):
        broken = valid_trace("age_transition", generation=9)
        broken["events"][0]["generation"] = 8
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-008", {e["error_code"] for e in result["errors"]})

    def test_expired_authorization_is_rejected(self):
        broken = valid_trace("housing")
        authorization = next(e for e in broken["events"] if e["stage"] == "AUTHORIZATION")
        physical = next(e for e in broken["events"] if e["stage"] == "PHYSICAL_REQUEST")
        authorization["expires_at"] = physical["sequence"] - 1
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-025", {e["error_code"] for e in result["errors"]})

    def test_duplicate_physical_request_is_rejected(self):
        broken = valid_trace("worker_economy")
        request = next(e for e in broken["events"] if e["stage"] == "PHYSICAL_REQUEST")
        broken["events"].insert(broken["events"].index(request) + 1, dict(request))
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-009", {e["error_code"] for e in result["errors"]})

    def test_unknown_and_failed_outcomes_receive_no_credit(self):
        for outcome in ("UNKNOWN", "FAILED"):
            broken = valid_trace("tactical_micro")
            broken["events"][-1].update(outcome=outcome, credited=True)
            result = validate_vertical_slice(broken)
            self.assertFalse(result["contract_valid"])
            self.assertIn("VSL-007" if outcome == "UNKNOWN" else "VSL-010", {e["error_code"] for e in result["errors"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
