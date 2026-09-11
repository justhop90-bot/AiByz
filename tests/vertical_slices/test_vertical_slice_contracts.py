import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "vertical_slice_validator"))
from vertical_slice_validator import load_causal_contract, load_registry, validate_vertical_slice


REGISTRY = load_registry()
CAUSAL = load_causal_contract()
SLICES = REGISTRY["contracts"]


def causal_payload(vertical_id, generation, request_id):
    spec = CAUSAL["verticals"][vertical_id]
    world = {name: True for name in spec["world_evidence"]}
    engine = {name: True for name in spec["required_engine_evidence"]}
    attribution = {name: True for name in spec["attribution_predicates"]}
    baseline = {name: 1 for name in spec["required_baseline"]}
    return {
        "request_id": request_id,
        "authorization_id": request_id,
        "action_generation": generation,
        "baseline": baseline,
        "engine_evidence": engine,
        "world_evidence": world,
        "expected_transition": {"kind": spec["expected_transition"]},
        "attribution": attribution,
        "causal_state": "CONFIRMED",
        "confirmation": {"confirmed": True, "strategic_success": False},
    }


def valid_trace(vertical_id, generation=1):
    contract = SLICES[vertical_id]
    events = []
    request_id = "req-physical"
    for sequence, stage in enumerate(contract["stages"]):
        if stage == "OBSERVE":
            evidence_type = "STATIC_SOURCE"
        elif stage in {"CLASSIFY", "DEMAND", "FEASIBILITY", "AUTHORIZATION"}:
            evidence_type = "COMPOSED"
        else:
            evidence_type = "TARGET_BUILD_RUNTIME"
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
            event["request_id"] = request_id
            event["world_state_evidence"] = True
            if vertical_id in CAUSAL["verticals"]:
                event["causal_evidence"] = causal_payload(vertical_id, generation, request_id)
        elif stage == "REASSESS":
            event["reassessment_published"] = True
            event["reassessment_generation"] = generation
        events.append(event)
    return {"vertical_id": vertical_id, "generation": generation, "events": events}


class TestAuthoritativeVerticalSliceContracts(unittest.TestCase):
    def test_registry_contains_six_qualification_slices_and_one_candidate(self):
        self.assertEqual(set(SLICES), {"worker_economy", "villager_production", "housing", "age_transition", "anti_cavalry", "tactical_micro", "military_production"})
        qualification_slices = {name for name, contract in SLICES.items() if contract.get("status") == "QUALIFICATION_SLICE"}
        candidates = {name for name, contract in SLICES.items() if contract.get("candidate") is True}
        self.assertEqual(qualification_slices, {"worker_economy", "villager_production", "housing", "age_transition", "anti_cavalry", "tactical_micro"})
        self.assertEqual(candidates, {"military_production"})

    def test_causal_contract_defines_all_six_verticals(self):
        self.assertEqual(set(CAUSAL["verticals"]), {"villager_production", "housing", "anti_cavalry", "age_transition", "tactical_micro", "military_production"})
        self.assertTrue(CAUSAL["universal_rules"]["attribution_required"])
        self.assertTrue(CAUSAL["universal_rules"]["unknown_is_not_success"])

    def test_military_production_candidate_is_blocked_by_selector_initialization(self):
        contract = SLICES["military_production"]
        self.assertTrue(contract["candidate"])
        self.assertEqual(contract["status"], "CANDIDATE_BLOCKED")
        self.assertEqual(contract["qualification_status"], "NOT_QUALIFIED")
        self.assertIn("SELECTOR_INITIALIZATION", contract["blockers"])
        self.assertIn("aegis-mp-unit", contract["blocker_detail"])
        self.assertIn("AEGIS-military-production-v0.per", contract["physical_component"])

    def test_complete_trace_uses_registry_and_causal_contract(self):
        for vertical_id in SLICES:
            with self.subTest(slice=vertical_id):
                result = validate_vertical_slice(valid_trace(vertical_id))
                self.assertTrue(result["contract_valid"], result["errors"])

    def test_candidate_trace_can_be_contract_valid_but_never_qualified(self):
        result = validate_vertical_slice(valid_trace("military_production"))
        self.assertTrue(result["contract_valid"], result["errors"])
        self.assertFalse(result["promotion_eligible"])
        self.assertFalse(result["qualified"])

    def test_trace_cannot_shadow_authoritative_contract(self):
        broken = valid_trace("housing")
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
        broken = valid_trace("worker_economy")
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
        verified["evidence_type"] = "STATIC_SOURCE"
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
        self.assertFalse(result["contract_valid"])
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
            expected = "VSL-007" if outcome == "UNKNOWN" else "VSL-010"
            self.assertIn(expected, {e["error_code"] for e in result["errors"]})

    def test_nonterminal_trace_is_rejected(self):
        broken = valid_trace("villager_production")
        broken["events"].pop()
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-001", {e["error_code"] for e in result["errors"]})
        self.assertIn("VSL-028", {e["error_code"] for e in result["errors"]})

    def test_missing_causal_evidence_is_rejected(self):
        broken = valid_trace("villager_production")
        verified = next(e for e in broken["events"] if e["stage"] == "WORLD_STATE_VERIFIED")
        verified.pop("causal_evidence")
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-041", {e["error_code"] for e in result["errors"]})

    def test_world_delta_cannot_become_causal_confirmation(self):
        broken = valid_trace("military_production")
        causal = next(e for e in broken["events"] if e["stage"] == "WORLD_STATE_VERIFIED")["causal_evidence"]
        causal["causal_state"] = "CONFIRMED"
        causal["attribution"]["pending_belongs_to_request"] = False
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-052", {e["error_code"] for e in result["errors"]})
        self.assertIn("VSL-053", {e["error_code"] for e in result["errors"]})

    def test_causal_identity_must_match_request(self):
        broken = valid_trace("housing")
        causal = next(e for e in broken["events"] if e["stage"] == "WORLD_STATE_VERIFIED")["causal_evidence"]
        causal["request_id"] = "different-request"
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-044", {e["error_code"] for e in result["errors"]})

    def test_reassessment_publication_is_required(self):
        broken = valid_trace("housing")
        broken["events"][-1].pop("reassessment_published")
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-029", {e["error_code"] for e in result["errors"]})

    def test_reassessment_generation_must_match_lifecycle(self):
        broken = valid_trace("anti_cavalry", generation=12)
        broken["events"][-1]["reassessment_generation"] = 11
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-030", {e["error_code"] for e in result["errors"]})

    def test_reassessment_cannot_select_strategy(self):
        broken = valid_trace("tactical_micro")
        broken["events"][-1]["reassessment_strategy"] = "ENGAGE"
        result = validate_vertical_slice(broken)
        self.assertFalse(result["contract_valid"])
        self.assertIn("VSL-031", {e["error_code"] for e in result["errors"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)

