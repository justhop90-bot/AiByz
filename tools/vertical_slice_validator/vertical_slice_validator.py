from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REGISTRY_PATH = Path(__file__).resolve().parents[2] / "schemas" / "AEGIS-VERTICAL-SLICE-CONTRACTS-1.0.json"


class ContractError(ValueError):
    """Raised when the authoritative registry is malformed."""


def load_registry(path: Path = REGISTRY_PATH) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        registry = json.load(handle)
    if registry.get("registry_id") != "AEGIS-VERTICAL-SLICE-CONTRACTS-1.0":
        raise ContractError("Unexpected vertical-slice registry identity.")
    if not isinstance(registry.get("contracts"), dict) or not registry["contracts"]:
        raise ContractError("Authoritative registry contains no contracts.")
    return registry


def _error(code: str, message: str) -> dict[str, str]:
    return {"error_code": code, "message": message}


def validate_vertical_slice(trace: dict[str, Any], registry: dict[str, Any] | None = None) -> dict[str, Any]:
    """Validate evidence against the authoritative contract selected by vertical_id.

    The trace is evidence only. It cannot define expected stages, owners,
    evidence requirements, or allowed transitions.
    """
    registry = registry or load_registry()
    errors: list[dict[str, str]] = []

    vertical_id = trace.get("vertical_id")
    if not vertical_id:
        return {"qualified": False, "errors": [_error("VSL-011", "Trace must identify vertical_id.")]}

    contract = registry["contracts"].get(vertical_id)
    if contract is None:
        return {"qualified": False, "errors": [_error("VSL-012", f"Unknown vertical_id {vertical_id!r}.")]}

    for field in {"expected_stages", "owners", "required_evidence", "allowed_transitions"}:
        if field in trace:
            errors.append(_error("VSL-013", f"Trace cannot define authoritative contract field {field!r}."))

    expected = contract["stages"]
    events = trace.get("events", [])
    if not isinstance(events, list):
        return {"qualified": False, "vertical_id": vertical_id, "contract_version": contract["version"], "errors": errors + [_error("VSL-014", "Trace events must be a list.")]}

    stages = [e.get("stage") for e in events]
    positions = {stage: index for index, stage in enumerate(stages) if stage is not None}

    for stage in expected:
        if stage not in stages:
            errors.append(_error("VSL-001", f"Required stage {stage!r} is missing."))

    transitions = contract["allowed_transitions"]
    for left, right in zip(stages, stages[1:]):
        if left is None or right is None:
            errors.append(_error("VSL-015", "Every event must have a recognized stage."))
            continue
        if right not in transitions.get(left, []):
            errors.append(_error("VSL-016", f"Forbidden transition {left!r} -> {right!r}."))

    for left, right in zip(expected, expected[1:]):
        if left in positions and right in positions and positions[left] > positions[right]:
            errors.append(_error("VSL-002", f"Stage {right!r} occurs before {left!r}."))

    generation = trace.get("generation")
    request_ids: set[str] = set()
    authorization_events: dict[str, dict[str, Any]] = {}
    required_evidence = contract["required_evidence"]
    owners = contract["owners"]

    for event in events:
        stage = event.get("stage")
        if stage not in expected:
            errors.append(_error("VSL-017", f"Stage {stage!r} is not part of vertical {vertical_id!r}."))
            continue

        if generation is None or event.get("generation") != generation:
            errors.append(_error("VSL-008", "Event generation does not match trace generation."))

        if not event.get("owner"):
            errors.append(_error("VSL-018", f"Stage {stage!r} lacks state-owner evidence."))
        elif event["owner"] != owners[stage]:
            errors.append(_error("VSL-019", f"Stage {stage!r} names non-authoritative owner {event['owner']!r}."))

        evidence_type = event.get("evidence_type")
        allowed_evidence = required_evidence.get(stage, [])
        if evidence_type not in allowed_evidence:
            errors.append(_error("VSL-020", f"Stage {stage!r} has evidence type {evidence_type!r}; allowed: {allowed_evidence}."))

        rid = event.get("request_id")
        if stage == "AUTHORIZATION":
            if not rid:
                errors.append(_error("VSL-021", "Authorization lacks request identity."))
            else:
                authorization_events[rid] = event

        if stage == "PHYSICAL_REQUEST":
            if not event.get("authorized"):
                errors.append(_error("VSL-003", "Physical request lacks authorization."))
            if not rid:
                errors.append(_error("VSL-022", "Physical request lacks request identity."))
            elif rid in request_ids:
                errors.append(_error("VSL-009", f"Duplicate request {rid!r}."))
            else:
                request_ids.add(rid)
                authorization = authorization_events.get(rid)
                if authorization is None:
                    errors.append(_error("VSL-023", f"Physical request {rid!r} has no preceding authorization."))
                elif authorization.get("generation") != event.get("generation"):
                    errors.append(_error("VSL-024", f"Authorization for request {rid!r} is stale."))
                elif authorization.get("expires_at") is not None and event.get("sequence") is not None and event["sequence"] > authorization["expires_at"]:
                    errors.append(_error("VSL-025", f"Authorization for request {rid!r} is expired."))

        if stage == "ENGINE_ACCEPTED_PENDING":
            if not rid:
                errors.append(_error("VSL-004", "Pending state lacks request identity."))
            elif rid not in request_ids:
                errors.append(_error("VSL-026", f"Pending request {rid!r} has no physical request."))

        if stage == "WORLD_STATE_VERIFIED":
            if not event.get("world_state_evidence"):
                errors.append(_error("VSL-005", "Verification lacks world-state evidence."))
            if evidence_type in {"SYNTHETIC_TEST", "STATIC_SOURCE", "COMPOSED", "INFERRED"}:
                errors.append(_error("VSL-027", "World-state verification requires target-build runtime or engine-specific evidence."))

        if event.get("strategic_success") and stage != "WORLD_STATE_VERIFIED":
            errors.append(_error("VSL-006", "Success was claimed before verification."))
        if event.get("outcome") == "UNKNOWN" and event.get("credited"):
            errors.append(_error("VSL-007", "Unknown outcome received credit."))
        if event.get("outcome") == "FAILED" and event.get("credited"):
            errors.append(_error("VSL-010", "Failed outcome received credit."))

    return {"qualified": not errors, "vertical_id": vertical_id, "contract_version": contract["version"], "errors": errors}
