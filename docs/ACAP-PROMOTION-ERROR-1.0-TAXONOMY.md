# ACAP-PROMOTION-ERROR-1.0 Normative Error Taxonomy

**Status:** NORMATIVE

This document defines the stable error-code taxonomy used by the ACAP promotion validator. It is separate from the JSON Schema. The JSON Schema defines the structure of an error object; this document defines the normative meaning of error codes and their required validation-layer semantics.

## 1. Error namespaces

| Namespace | Validation layer | Meaning |
|---|---|---|
| `SCH-*` | `SCHEMA` | Promotion/error data violates the structural JSON contract. |
| `SEM-*` | `SEMANTIC` | Structurally valid data violates an ACAP normative semantic or promotion rule. |
| `EVD-*` | `CROSS_RECORD_EVIDENCE` | A claim cannot be supported, reconciled, or traced across its evidence records/artifacts. |

The prefix is normative. An error code whose prefix disagrees with `validation_layer` is itself an invalid validator result.

## 2. Schema errors

| Code | Normative meaning |
|---|---|
| `SCH-001` | Required field missing. |
| `SCH-002` | Unknown or disallowed field present. |
| `SCH-003` | JSON value has the wrong type. |
| `SCH-004` | Enum value is not permitted. |
| `SCH-005` | String format violation. |
| `SCH-006` | String length or pattern violation. |
| `SCH-007` | Numeric range violation. |
| `SCH-008` | Array cardinality violation. |
| `SCH-009` | Duplicate array item where uniqueness is required. |
| `SCH-010` | Invalid or unsupported schema version. |
| `SCH-011` | Goal ID is outside the normative ACAP namespace. |
| `SCH-012` | Operation is outside the normative operation set. |
| `SCH-013` | Value-range structure is invalid. |
| `SCH-014` | Date-time value is invalid. |
| `SCH-015` | Structural conditional requirement is violated. |

Schema errors are data-contract failures. They do not establish anything about AoE2DE runtime behavior.

## 3. Semantic-rule errors

| Code | Normative meaning |
|---|---|
| `SEM-001` | Value range is reversed: `minimum > maximum`. |
| `SEM-002` | Claimed `up-compare-goal` range exceeds the permitted comparison operand boundary. |
| `SEM-003` | Promotion claims direct qualification without `DIRECT` evidence. |
| `SEM-004` | Promotion claims reproduction without reproduced evidence. |
| `SEM-005` | Promotion claims qualification while one or more required gates are not `PASS`. |
| `SEM-006` | Qualified decision has an incorrect reason code. |
| `SEM-007` | `decision.qualified` contradicts `decision.status`. |
| `SEM-008` | Qualified entry does not establish exclusive ACAP ownership. |
| `SEM-009` | Qualified entry has unresolved ownership. |
| `SEM-010` | Status and reason-code combination is semantically invalid. |
| `SEM-011` | Gate combination is semantically invalid. |
| `SEM-012` | Promotion is claimed without required runtime evidence. |
| `SEM-013` | Inference is being used as independent promotion evidence. |
| `SEM-014` | Claimed boundary exceeds what the promotion rules permit. |
| `SEM-015` | A failed negative control is ignored or treated as successful qualification. |
| `SEM-016` | State-integrity gate is marked passed without the required state evidence. |
| `SEM-017` | Repeatability gate is marked passed without required reproduction. |
| `SEM-018` | Build identity is internally inconsistent. |
| `SEM-019` | Goal/operation/value claim is outside the defined ACAP test scope. |
| `SEM-020` | Promotion decision violates the normative fail-closed rule. |

## 4. Cross-record evidence errors

| Code | Normative meaning |
|---|---|
| `EVD-001` | Referenced evidence record cannot be resolved. |
| `EVD-002` | Evidence record belongs to a different qualification run. |
| `EVD-003` | Evidence goal ID does not match the promoted target. |
| `EVD-004` | Evidence operation does not match the promoted target. |
| `EVD-005` | Evidence build version does not match. |
| `EVD-006` | Evidence build fingerprint does not match. |
| `EVD-007` | Evidence environment does not match. |
| `EVD-008` | Referenced artifact cannot be resolved. |
| `EVD-009` | Required boundary observation is missing. |
| `EVD-010` | Required negative-control observation is missing. |
| `EVD-011` | Required repeat observation is missing. |
| `EVD-012` | Raw observations are contradictory. |
| `EVD-013` | Claimed range exceeds directly demonstrated evidence. |
| `EVD-014` | Evidence does not demonstrate the claimed semantic result. |
| `EVD-015` | Evidence provenance is incomplete. |
| `EVD-016` | Required evidence timestamp is unavailable or invalid. |
| `EVD-017` | Evidence originates from an incompatible target build. |
| `EVD-018` | Referenced evidence has been superseded. |
| `EVD-019` | Evidence-artifact integrity cannot be established. |
| `EVD-020` | Evidence attribution is ambiguous. |

## 5. Severity

Every validator error uses exactly one severity:

- `WARNING` — informational; cannot independently invalidate a promotion.
- `ERROR` — validation defect that makes the affected claim invalid for its current purpose.
- `BLOCKING` — a prerequisite prevents promotion or requires a fail-closed outcome.
- `CONFLICT` — independently relevant records or observations contradict one another.

A warning must never be silently converted into a passing promotion gate.

## 6. Resolution

Every validator error uses exactly one resolution:

- `REJECT_RECORD` — the promotion/error record is structurally or contractually invalid.
- `BLOCK_PROMOTION` — the record may be valid, but promotion cannot proceed.
- `MARK_UNRESOLVED` — available evidence cannot establish the result.
- `MARK_FAILED` — evidence establishes failure of the tested claim.
- `MARK_NOT_APPLICABLE` — the test has no legitimate applicability.
- `NO_ACTION` — no promotion-blocking action is required.

`MARK_FAILED` must not be used merely because evidence is absent. Absence of evidence is normally unresolved or blocked, not failure.

## 7. Evidence-reference requirements

`evidence_references` is required on every validator error object.

A pure schema error may legitimately contain an empty reference array because the error can be established from the record alone.

Semantic and cross-record evidence errors should reference the promotion record and/or the evidence records that establish the condition whenever such references exist.

A `CONFLICT` error must identify at least two evidence references in the error object. This prevents a conflict classification from being asserted without identifying the conflicting material.

## 8. Validation precedence

The normative validator pipeline is:

```text
PROMOTION RECORD
      ↓
SCHEMA VALIDATION
      ↓
SEMANTIC VALIDATION
      ↓
CROSS-RECORD EVIDENCE VALIDATION
      ↓
PROMOTION DECISION
```

A schema-invalid record must not be treated as semantically qualified. Cross-record evidence validation cannot repair structural invalidity.

## 9. Fail-closed rule

The absence of an error is not evidence of qualification.

`ACAP-QUALIFIED` requires the separate ACAP promotion gates to pass. Any blocking semantic or evidentiary defect prevents qualification.

In particular:

```text
SCH failure        → invalid record
SEM blocking error → promotion blocked/failed according to rule
EVD blocking error → promotion blocked/unresolved according to evidence state
no error           → does NOT imply qualification
all promotion gates PASS + required DIRECT/REPRODUCED evidence → qualification may be granted
```

## 10. Relationship to the normative JSON Schema

The companion schema is:

`schemas/ACAP-PROMOTION-ERROR-1.0.schema.json`

The schema defines structure, primitive types, enums, patterns, and structural conditionals. This taxonomy defines semantic meaning. Cross-record requirements such as evidence-ID resolution, build matching, range containment, and contradictory observations are validator rules and are intentionally not encoded as portable JSON Schema assertions.
