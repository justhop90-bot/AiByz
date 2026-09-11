"""Cross-record semantic validator for ACAP-PROMOTION-1.0.

Permanent validator component; not a runtime/.per probe.
"""
from __future__ import annotations
import json
from typing import Any

ERROR_SCHEMA_VERSION = "ACAP-PROMOTION-ERROR-1.0"
DIRECT = "DIRECT"


def _error(code: str, message: str, target: dict[str, Any], refs: tuple[str, ...] = (), *, severity: str = "BLOCKING", resolution: str = "BLOCK_PROMOTION") -> dict[str, Any]:
    return {
        "schema_version": ERROR_SCHEMA_VERSION,
        "error_id": f"acap-{code.lower()}-{len(refs)}",
        "error_code": code,
        "validation_layer": "CROSS_RECORD_EVIDENCE",
        "severity": severity,
        "resolution": resolution,
        "message": message,
        "target": target,
        "evidence_references": [{"reference_type": "RAW_EVIDENCE_RECORD", "reference_id": ref} for ref in refs],
    }


def validate_cross_record(promotion: dict[str, Any], evidence_records: list[dict[str, Any]]) -> dict[str, Any]:
    """Validate identity, range containment, contradictions, and fail-closed behavior."""
    target = promotion["target"]
    build_fingerprint = promotion["build"]["build_fingerprint"]
    refs = promotion.get("evidence_references", [])
    by_id = {str(record["record_id"]): record for record in evidence_records}
    errors: list[dict[str, Any]] = []
    relevant: list[dict[str, Any]] = []

    for reference in refs:
        record_id = str(reference["reference_id"])
        evidence = by_id.get(record_id)
        if evidence is None:
            errors.append(_error("EVD-001", f"Evidence record {record_id!r} cannot be resolved.", target, (record_id,)))
            continue
        relevant.append(evidence)
        if evidence.get("goal_id") != target["goal_id"]:
            errors.append(_error("EVD-003", "Evidence goal_id does not exactly match the promotion target.", target, (record_id,)))
        if evidence.get("operation") != target["operation"]:
            errors.append(_error("EVD-004", "Evidence operation does not exactly match the promotion target.", target, (record_id,)))
        if evidence.get("build_fingerprint") != build_fingerprint:
            errors.append(_error("EVD-006", "Evidence build_fingerprint does not exactly match the promotion build.", target, (record_id,)))

    qualifying = [
        evidence for evidence in relevant
        if evidence.get("goal_id") == target["goal_id"]
        and evidence.get("operation") == target["operation"]
        and evidence.get("build_fingerprint") == build_fingerprint
        and evidence.get("evidence_strength") == DIRECT
        and evidence.get("runtime_result") is not None
    ]

    claim = target.get("value_range")
    if claim is not None:
        values = [e["observed_value"] for e in qualifying if isinstance(e.get("observed_value"), int) and not isinstance(e.get("observed_value"), bool)]
        if not values:
            errors.append(_error("EVD-014", "No qualifying direct runtime observations establish the demonstrated range.", target, tuple(e["record_id"] for e in relevant)))
        else:
            demonstrated_minimum, demonstrated_maximum = min(values), max(values)
            if claim["minimum"] < demonstrated_minimum or claim["maximum"] > demonstrated_maximum:
                errors.append(_error("EVD-013", "Claimed range exceeds the directly demonstrated range.", target, tuple(e["record_id"] for e in qualifying)))
            for boundary in (claim["minimum"], claim["maximum"]):
                if boundary not in values:
                    errors.append(_error("EVD-009", f"Required claimed boundary {boundary} lacks a qualifying observation.", target, tuple(e["record_id"] for e in qualifying)))

    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for evidence in qualifying:
        key = (evidence["goal_id"], evidence["operation"], evidence["build_fingerprint"])
        groups.setdefault(key, []).append(evidence)
    for group in groups.values():
        results = {json.dumps(e.get("runtime_result"), sort_keys=True) for e in group}
        if len(results) > 1:
            errors.append(_error("EVD-012", "Relevant evidence records contain contradictory runtime results.", target, tuple(e["record_id"] for e in group), severity="CONFLICT", resolution="MARK_UNRESOLVED"))

    return {"qualified": not errors, "errors": errors}


__all__ = ["validate_cross_record", "ERROR_SCHEMA_VERSION"]
