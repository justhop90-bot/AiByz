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
    """Validate a trace against the authoritative registry contract.

    ``contract_valid`` means the trace conforms structurally to the selected
    contract. ``qualified`` is a promotion-level result and additionally
    requires target-build runtime/engine-specific verification and registry
    promotion eligibility. A candidate or blocked contract cannot qualify even
    when a trace is structurally complete.

    REASSESS is a publication boundary, not a strategy controller. The final
    event must carry the same lifecycle generation and explicitly state that a
    reassessment token was published by the registry-defined REASSESS owner.
    """
    registry = registry or load_registry()
    errors: list[dict[str, str]] = []

    vertical_id = trace.get("vertical_id")
    if not vertical_id:
        return {"qualified": False, "contract_valid": False, "errors": [_error("VSL-011", "Trace must identify vertical_id.")]}

    contract = registry["contracts"].get(vertical_id)
    if contract is None:
        return {"qualified": False, "contract_valid": False, "vertical_id": vertical_id, "errors": [_error("VSL-012", f"Unknown vertical_id {vertical_id!r}.")]}

    for field in {"expected_stages", "owners", "required_evidence", "allowed_transitions"}:
        if field in trace:
            errors.append(_error("VSL-013", f"Trace cannot define authoritative contract field {field!r}."))

    expected = contract["stages"]
    events = trace.get("events", [])
    if not isinstance(events, list):
        return {"qualified": False, "contract_valid": False, "vertical_id": vertical_id, "contract_version": contract["version"], "errors": errors + [_error("VSL-014", "Trace events must be a list.")]}

    stages = [event.get("stage") for event in events]
    positions = {stage: index for index, stage in enumerate(stages) if stage is not None}

    for stage in expected:
        if stage not in stages:
            errors.append(_error("VSL-001", f"Required stage {stage!r} is missing."))

    required_terminal_stage = registry.get("common", {}).get("required_terminal_stage")
    if required_terminal_stage and (not stages or stages[-1] != required_terminal_stage):
        errors.append(_error("VSL-028", f"Trace must terminate at required terminal stage {required_terminal_stage!r}."))

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
    runtime_evidence_seen = False

    for event in events:
        stage = event.get("stage")
        if stage not in expected:
            errors.append(_error("VSL-017", f"Stage {stage!r} is not part of vertical {vertical_id!r}."))
            continue

        if generation is None or event.get("generation") != generation:
            errors.append(_error("VSL-008", "Event generation does not match trace generation."))

        owner = event.get("owner")
        if not owner:
            errors.append(_error("VSL-018", f"Stage {stage!r} lacks state-owner evidence."))
        elif owner != owners[stage]:
            errors.append(_error("VSL-019", f"Stage {stage!r} names non-authoritative owner {owner!r}."))

        evidence_type = event.get("evidence_type")
        allowed_evidence = required_evidence.get(stage, [])
        if evidence_type not in allowed_evidence:
            errors.append(_error("VSL-020", f"Stage {stage!r} has evidence type {evidence_type!r}; allowed: {allowed_evidence}."))
        if evidence_type in {"TARGET_BUILD_RUNTIME", "ENGINE_SPECIFIC"}:
            runtime_evidence_seen = True

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
            if evidence_type not in {"TARGET_BUILD_RUNTIME", "ENGINE_SPECIFIC"}:
                errors.append(_error("VSL-027", "World-state verification requires target-build runtime or engine-specific evidence."))

        if event.get("strategic_success") and stage != "WORLD_STATE_VERIFIED":
            errors.append(_error("VSL-006", "Success was claimed before verification."))
        if event.get("outcome") == "UNKNOWN" and event.get("credited"):
            errors.append(_error("VSL-007", "Unknown outcome received credit."))
        if event.get("outcome") == "FAILED" and event.get("credited"):
            errors.append(_error("VSL-010", "Failed outcome received credit."))

    if required_terminal_stage == "REASSESS" and stages and stages[-1] == "REASSESS":
        reassess = events[-1]
        if reassess.get("reassessment_published") is not True:
            errors.append(_error("VSL-029", "REASSESS must explicitly publish a reassessment token."))
        if reassess.get("reassessment_generation") != generation:
            errors.append(_error("VSL-030", "REASSESS token generation must equal the lifecycle generation."))
        if reassess.get("reassessment_strategy") is not None:
            errors.append(_error("VSL-031", "REASSESS publisher cannot select the next strategy."))

    contract_valid = not errors
    promotion_eligible = (
        contract.get("status") == "QUALIFICATION_SLICE"
        and contract.get("candidate") is not True
        and contract.get("qualification_status") != "NOT_QUALIFIED"
        and not contract.get("blockers")
    )
    qualified = (
        contract_valid
        and promotion_eligible
        and runtime_evidence_seen
        and any(
            event.get("stage") == "WORLD_STATE_VERIFIED"
            and event.get("evidence_type") in {"TARGET_BUILD_RUNTIME", "ENGINE_SPECIFIC"}
            for event in events
        )
    )

    return {
        "qualified": qualified,
        "contract_valid": contract_valid,
        "promotion_eligible": promotion_eligible,
        "vertical_id": vertical_id,
        "contract_version": contract["version"],
        "errors": errors,
    }
