#!/usr/bin/env python3
"""Executable tests for ACAP-PROMOTION-1.0 cross-record semantics."""
from __future__ import annotations
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "acap_validator"))
from acap_promotion_validator import validate_cross_record

BASE_PROMOTION = {
    "schema_version": "ACAP-PROMOTION-1.0",
    "target": {"goal_id": 740, "operation": "set-goal", "value_range": {"minimum": 10, "maximum": 20}},
    "build": {"build_fingerprint": "BUILD-A"},
    "evidence_references": [],
}


def evidence(record_id, value, *, runtime_result="PASS", goal_id=740, operation="set-goal", build_fingerprint="BUILD-A", strength="DIRECT"):
    return {"record_id": record_id, "goal_id": goal_id, "operation": operation, "build_fingerprint": build_fingerprint, "evidence_strength": strength, "runtime_result": runtime_result, "observed_value": value}


def promotion(*record_ids, **target_overrides):
    result = copy.deepcopy(BASE_PROMOTION)
    result["target"].update(target_overrides)
    result["evidence_references"] = [{"reference_type": "RAW_EVIDENCE_RECORD", "reference_id": record_id} for record_id in record_ids]
    return result


class TestACAPCrossRecordSemantics(unittest.TestCase):
    def test_exact_identity_and_full_range_qualifies(self):
        result = validate_cross_record(promotion("r1", "r2"), [evidence("r1", 10), evidence("r2", 20)])
        self.assertTrue(result["qualified"])
        self.assertEqual(result["errors"], [])

    def test_claimed_range_inside_demonstrated_range_qualifies(self):
        result = validate_cross_record(promotion("r1", "r2", value_range={"minimum": 12, "maximum": 18}), [evidence("r1", 10), evidence("r2", 20)])
        self.assertTrue(result["qualified"])

    def test_claimed_lower_bound_outside_demonstrated_range_fails_closed(self):
        result = validate_cross_record(promotion("r1", "r2", value_range={"minimum": 9, "maximum": 20}), [evidence("r1", 10), evidence("r2", 20)])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-013", {e["error_code"] for e in result["errors"]})

    def test_claimed_upper_bound_outside_demonstrated_range_fails_closed(self):
        result = validate_cross_record(promotion("r1", "r2", value_range={"minimum": 10, "maximum": 21}), [evidence("r1", 10), evidence("r2", 20)])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-013", {e["error_code"] for e in result["errors"]})

    def test_goal_id_mismatch_fails_closed(self):
        result = validate_cross_record(promotion("r1", "r2"), [evidence("r1", 10, goal_id=741), evidence("r2", 20)])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-003", {e["error_code"] for e in result["errors"]})

    def test_operation_mismatch_fails_closed(self):
        result = validate_cross_record(promotion("r1", "r2"), [evidence("r1", 10, operation="goal"), evidence("r2", 20)])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-004", {e["error_code"] for e in result["errors"]})

    def test_build_fingerprint_mismatch_fails_closed(self):
        result = validate_cross_record(promotion("r1", "r2"), [evidence("r1", 10, build_fingerprint="BUILD-B"), evidence("r2", 20)])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-006", {e["error_code"] for e in result["errors"]})

    def test_multiple_identity_mismatches_are_not_coerced(self):
        result = validate_cross_record(promotion("r1", "r2"), [evidence("r1", 10, goal_id=741, operation="goal", build_fingerprint="BUILD-B"), evidence("r2", 20)])
        codes = {e["error_code"] for e in result["errors"]}
        self.assertFalse(result["qualified"])
        self.assertTrue({"EVD-003", "EVD-004", "EVD-006"}.issubset(codes))

    def test_contradictory_runtime_results_fail_closed(self):
        result = validate_cross_record(promotion("r1", "r2"), [evidence("r1", 10, runtime_result="PASS"), evidence("r2", 20, runtime_result="FAIL")])
        self.assertFalse(result["qualified"])
        conflict = [e for e in result["errors"] if e["error_code"] == "EVD-012"]
        self.assertEqual(len(conflict), 1)
        self.assertEqual(conflict[0]["severity"], "CONFLICT")
        self.assertEqual(conflict[0]["resolution"], "MARK_UNRESOLVED")
        self.assertGreaterEqual(len(conflict[0]["evidence_references"]), 2)

    def test_missing_evidence_fails_closed(self):
        result = validate_cross_record(promotion("missing"), [])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-001", {e["error_code"] for e in result["errors"]})

    def test_non_direct_evidence_cannot_promote(self):
        result = validate_cross_record(promotion("r1"), [evidence("r1", 10, strength="INFERRED")])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-014", {e["error_code"] for e in result["errors"]})

    def test_missing_claim_boundary_fails_closed(self):
        result = validate_cross_record(promotion("r1", "r2", value_range={"minimum": 10, "maximum": 20}), [evidence("r1", 10), evidence("r2", 15)])
        self.assertFalse(result["qualified"])
        self.assertIn("EVD-009", {e["error_code"] for e in result["errors"]})


if __name__ == "__main__":
    unittest.main(verbosity=2)
