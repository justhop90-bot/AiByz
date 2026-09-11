from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "schemas" / "AEGIS-VERTICAL-SLICE-CONTRACTS-1.0.json"
CAUSAL_PATH = ROOT / "schemas" / "ACAP-CAUSAL-EVIDENCE-0.1.json"


class ContractError(ValueError):
    """Raised when an authoritative contract is malformed."""


def load_registry(path: Path = REGISTRY_PATH) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        registry = json.load(handle)
    if registry.get("registry_id") != "AEGIS-VERTICAL-SLICE-CONTRACTS-1.0":
        raise ContractError("Unexpected vertical-slice registry identity.")
    if not isinstance(registry.get("contracts"), dict) or not registry["contracts"]:
        raise ContractError("Authoritative registry contains no contracts.")
    return registry


def load_causal_contract(path: Path = CAUSAL_PATH) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        contract = json.load(handle)
    if contract.get("schema_id") != "ACAP-CAUSAL-EVIDENCE-0.1":
        raise ContractError("Unexpected ACAP causal-evidence contract identity.")
    if contract.get("status") != "NORMATIVE":
        raise ContractError("ACAP causal-evidence contract must be normative.")
    if not isinstance(contract.get("verticals"), dict):
        raise ContractError("ACAP causal-evidence contract contains no vertical definitions.")
    return contract


def _error(code: str, message: str) -> dict[str, str]:
    return {"error_code": code, "message": message}


def _validate_causal_evidence(
    vertical_id: str,
    event: dict[str, Any],
    causal_contract: dict[str, Any],
    errors: list[dict[str, str]],
) -> None:
    """Validate the causal-evidence boundary of a WORLD_STATE_VERIFIED event."""
    spec = causal_contract["verticals"].get(vertical_id)
    if spec is None:
        errors.append(_error("VSL-040", f"No ACAP causal-evidence contract exists for {vertical_id!r}."))
        return

    causal = event.get("causal_evidence")
    if not isinstance(causal, dict):
        errors.append(_error("VSL-041", "WORLD_STATE_VERIFIED requires an ACAP causal_evidence object."))
        return

    required_fields = causal_contract["required_evidence_fields"]
    for field in required_fields:
        if field not in causal:
            errors.append(_error("VSL-042", f"Causal evidence is missing required field {field!r}."))

    state = causal.get("causal_state")
    if state not in causal_contract["causal_state_values"]:
        errors.append(_error("VSL-043", f"Invalid causal_state {state!r}."))

    request_id = event.get("request_id")
    if causal.get("request_id") != request_id:
        errors.append(_error("VSL-044", "Causal request identity does not match WORLD_STATE_VERIFIED request identity."))

    generation = event.get("generation")
    if causal.get("action_generation") != generation:
        errors.append(_error("VSL-045", "Causal action_generation does not match lifecycle generation."))

    authorization = causal.get("authorization_id")
    if not authorization:
        errors.append(_error("VSL-046", "Causal evidence lacks authorization identity."))

    baseline = causal.get("baseline")
    if not isinstance(baseline, dict):
        errors.append(_error("VSL-047", "Causal baseline must be an object."))

    engine = causal.get("engine_evidence")
    world = causal.get("world_evidence")
    expected = causal.get("expected_transition")
    attribution = causal.get("attribution")
    confirmation = causal.get("confirmation")
    for name, value in (("engine_evidence", engine), ("world_evidence", world), ("expected_transition", expected), ("attribution", attribution), ("confirmation", confirmation)):
        if not isinstance(value, dict):
            errors.append(_error("VSL-048", f"Causal {name} must be an object."))

    if isinstance(engine, dict):
        for field in spec["required_engine_evidence"]:
            if engine.get(field) is not True:
                errors.append(_error("VSL-049", f"Required engine evidence {field!r} is not proven."))

    if isinstance(world, dict):
        for field in spec["world_evidence"]:
            if world.get(field) is not True:
                errors.append(_error("VSL-050", f"Required world evidence {field!r} is not proven."))

    if isinstance(expected, dict) and expected.get("kind") != spec["expected_transition"]:
        errors.append(_error("VSL-051", "Expected transition does not match the authoritative ACAP vertical contract."))

    if isinstance(attribution, dict):
        for predicate in spec["attribution_predicates"]:
            if attribution.get(predicate) is not True:
                errors.append(_error("VSL-052", f"Required attribution predicate {predicate!r} is not proven."))

    # A causal claim cannot be synthesized from a world delta alone.
    if state == "CONFIRMED":
        if not isinstance(attribution, dict) or not all(attribution.get(p) is True for p in spec["attribution_predicates"]):
            errors.append(_error("VSL-053", "CAUSALLY_CONFIRMED requires every authoritative attribution predicate."))

    if isinstance(confirmation, dict) and state == "CONFIRMED":
        if confirmation.get("strategic_success") is True:
            errors.append(_error("VSL-054", "Causal confirmation cannot claim strategic success."))

    if event.get("strategic_success") and state not in {"CONFIRMED"}:
        errors.append(_error("VSL-055", "Strategic success cannot be claimed without causal confirmation or an explicit direct-world confirmation mode."))

    # The causal contract is intentionally stricter than the old world-state-only validator.
    if state == "CONFIRMED" and spec.get("confirmation_predicate") == "causal_state_CONFIRMED":
        if confirmation.get("confirmed") is not True:
            errors.append(_error("VSL-056", "Causal confirmation requires confirmation.confirmed=true."))
    elif state == "CONFIRMED" and confirmation.get("confirmed") is not True:
        errors.append(_error("VSL-057", "Causal confirmation requires explicit confirmation.confirmed=true."))


def validate_vertical_slice(trace: dict[str, Any], registry: dict[str, Any] | None = None) -> dict[str, Any]:
    """Validate a trace against the authoritative vertical and ACAP causal contracts.

    Contract validity is structural. Qualification additionally requires runtime evidence
    and promotion eligibility. Causal confirmation is never inferred from a world-state
    delta alone.
    """
    registry = registry or load_registry()
    causal_contract = load_causal_contract()
    errors: list[dict[str, str]] = []

    vertical_id = trace.get("vertical_id")
    if not vertical_id:
        return {"qualified": False, "contract_valid": False, "errors": [_error("VSL-011", "Trace must identify vertical_id.")]}

    contract = registry["contracts"].get(vertical_id)
    if contract is None:
        return {"qualified": False, "contract_valid": False, "vertical_id": vertical_id, "errors": [_error("VSL-012", f"Unknown vertical_id {vertical_id!r}.")]}

    if vertical_id not in causal_contract["verticals"]:
        errors.append(_error("VSL-040", f"Vertical {vertical_id!r} is absent from ACAP causal-evidence contract."))

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
            _validate_causal_evidence(vertical_id, event, causal_contract, errors)

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
        "causal_contract_version": causal_contract["schema_version"],
        "errors": errors,
    }
