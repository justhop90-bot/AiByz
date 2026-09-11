# ACAP-PROMOTION-1.0 Cross-Record Semantic Validator Rules

**Status:** NORMATIVE
**Validator target:** ACAP-PROMOTION-1.0
**Error object:** ACAP-PROMOTION-ERROR-1.0

## 1. Purpose

These rules define the cross-record checks required before an ACAP promotion claim can be accepted. They operate after structural JSON Schema validation and are intentionally expressed as validator logic rather than portable JSON Schema assertions.

The validator MUST fail closed: inability to establish a required relationship is not evidence that the relationship is valid.

## 2. Required identity tuple

Every promotion target is identified by:

```text
(goal_id, operation, build_fingerprint)
```

The qualification run and environment provide additional provenance, but they do not replace this target identity tuple.

For each supporting evidence record, the validator MUST compare:

```text
promotion.target.goal_id          == evidence.goal_id
promotion.target.operation        == evidence.operation
promotion.build.build_fingerprint == evidence.build_fingerprint
```

A mismatch MUST NOT be silently normalized, coerced, or interpolated.

### EVD mappings

- `EVD-003`: goal ID mismatch.
- `EVD-004`: operation mismatch.
- `EVD-006`: build fingerprint mismatch.
- `EVD-002`: qualification-run mismatch when run identity is required by the evidence claim.
- `EVD-007`: environment mismatch where environment identity is part of the qualification record.

## 3. Demonstrated-range containment

A promotion MAY claim only behavior directly demonstrated by the qualifying evidence.

Let:

```text
C = claimed range = [Cmin, Cmax]
D = demonstrated range = [Dmin, Dmax]
```

The containment requirement is:

```text
Dmin <= Cmin
AND
Cmax <= Dmax
```

Equivalent set relation:

```text
C ⊆ D
```

If either condition fails, the promotion MUST NOT be marked `ACAP-QUALIFIED`.

The validator MUST emit `EVD-013` when the claimed range exceeds directly demonstrated evidence.

### Important boundary rule

The validator MUST NOT infer an untested interior or exterior range merely because two endpoints were observed. Range qualification requires the evidence model to explicitly define the demonstrated range and the observations supporting it.

For operation-specific qualification, the demonstrated range MUST respect primitive-specific limits. In particular, `up-compare-goal` comparison operands are subject to the narrower operation limit; the global goal storage range does not override that limit.

## 4. Evidence identity matching

For every evidence reference used to support a promotion gate, the validator MUST resolve the referenced record and verify:

1. record exists;
2. record belongs to the expected qualification run when applicable;
3. `goal_id` exactly matches the promotion target;
4. `operation` exactly matches the promotion target;
5. `build_fingerprint` exactly matches the promotion build;
6. environment identity matches when the qualification protocol requires it;
7. evidence type is appropriate for the gate being supported;
8. the observation is temporally and causally relevant to the claim;
9. artifact integrity/provenance is available where an artifact is required.

Failure of item 1 is `EVD-001`.
Failure of item 2 is `EVD-002`.
Failure of item 3 is `EVD-003`.
Failure of item 4 is `EVD-004`.
Failure of item 5 is `EVD-006`.
Failure of item 6 is `EVD-007`.
Failure of item 7 is `EVD-014`.
Failure of item 8 is `EVD-014`.
Failure of item 9 is `EVD-019`.

## 5. Build identity is exact

`build_fingerprint` is an exact identity field, not a descriptive label.

The validator MUST compare it as an opaque string. It MUST NOT:

- compare only a build-version prefix;
- accept a missing fingerprint because the version matches;
- substitute a later or earlier build;
- assume compatibility between fingerprints;
- infer equivalence from identical observed behavior.

If fingerprints differ, the evidence does not support the target promotion unless the promotion record explicitly targets the evidence build instead.

## 6. Operation identity is exact

The validator MUST treat these operations as distinct:

- `set-goal`
- `goal`
- `up-modify-goal`
- `up-compare-goal`

Evidence for one operation MUST NOT qualify another operation merely because both access the same goal ID.

Example:

```text
(goal_id=740, operation=set-goal)
```

does not establish:

```text
(goal_id=740, operation=up-compare-goal)
```

without direct qualifying evidence for the comparison operation.

## 7. Goal identity is exact

Evidence for goal `740` MUST NOT be credited to goal `741`, even when:

- both goals are in the ACAP namespace;
- both have identical observed values;
- both use the same operation;
- both occur in the same run.

The namespace establishes ownership and admissibility, not interchangeability.

## 8. Run and build coherence

A promotion's evidence set MUST form a coherent qualification context.

At minimum, all evidence supporting one promoted target MUST resolve to the same:

```text
qualification_run_id
build_fingerprint
goal_id
operation
```

where those fields are required by the evidence record schema.

Mixed-build evidence MUST be rejected for qualification rather than merged into a synthetic result.

Mixed-run evidence MUST be rejected unless the promotion protocol explicitly defines a multi-run aggregation rule. ACAP-PROMOTION-1.0 does not silently provide such aggregation.

## 9. Gate-specific evidence requirements

### 9.1 Namespace/ownership

The evidence MUST establish that the goal ID is within `740–759` and that the ACAP namespace has exclusive ownership.

### 9.2 Static legality

Static evidence MUST support the exact operation and argument form being promoted. Static legality cannot substitute for runtime execution evidence.

### 9.3 Runtime execution

At least one qualifying runtime observation MUST directly establish that the exact `(goal_id, operation, build_fingerprint)` executed on the target build.

### 9.4 Semantic result

The evidence MUST demonstrate the expected semantic effect, not merely successful parsing or absence of an error.

### 9.5 Boundary

Every boundary included in the claimed range MUST be represented by qualifying evidence. The validator MUST NOT silently extend the range between unobserved values.

### 9.6 Negative controls

Required negative controls MUST be present and must retain their intended interpretation. A failed or contaminated negative control prevents the corresponding integrity gate from passing.

### 9.7 Repeatability

Repeatability evidence MUST use the same target identity tuple and compatible qualification context. A different build fingerprint is not an independent reproduction of the same target.

## 10. Contradictory evidence

If two otherwise relevant records with the same target identity contain contradictory runtime results, the validator MUST NOT choose the favorable observation.

The validator MUST emit `EVD-012` and classify the promotion as unresolved or blocked according to the promotion decision rules.

A conflict MUST retain references to at least two conflicting evidence records and SHOULD include their observed values/results in `details`.

## 11. Provenance chain

A promoted result MUST be traceable:

```text
promotion decision
    ↓
validator result
    ↓
raw evidence record(s)
    ↓
runtime observation / artifact
    ↓
target build fingerprint
```

Breaking this chain prevents qualification. The validator MUST emit `EVD-015` when required provenance cannot be established.

## 12. No silent interpolation

The validator MUST NOT manufacture evidence for:

- untested goal IDs;
- untested operations;
- untested values;
- untested comparison operands;
- other builds;
- other environments;
- other qualification runs.

A demonstrated range is an evidence claim, not a mathematical assumption that every value inside a nominal interval behaved identically.

## 13. Normative validation algorithm

```text
INPUT: promotion_record P

1. Resolve every evidence reference used by P.
2. For each evidence record E:
   a. verify E exists;
   b. verify run identity where required;
   c. compare E.goal_id with P.target.goal_id;
   d. compare E.operation with P.target.operation;
   e. compare E.build_fingerprint with P.build.build_fingerprint;
   f. verify environment identity where required;
   g. verify evidence type and provenance;
   h. verify temporal/semantic relevance.
3. Derive demonstrated range D only from qualifying raw observations.
4. Read claimed range C from P.
5. Require C ⊆ D.
6. Verify operation-specific primitive limits.
7. Verify required boundary observations.
8. Verify required negative controls.
9. Verify repeatability using the same target identity tuple.
10. Detect contradictions among relevant evidence.
11. Emit normative error objects for every failed rule.
12. If any required promotion gate is BLOCKING or UNRESOLVED, do not qualify.
13. Grant ACAP-QUALIFIED only when all required gates pass and the required evidence is DIRECT and reproduced.
```

## 14. Error precedence

When multiple errors arise, the validator SHOULD report all independently established errors, but promotion status MUST remain fail-closed.

Structural errors precede semantic evaluation. Unresolvable evidence precedes claims that depend on that evidence. A missing evidence record must not be transformed into a semantic pass merely because the promotion record asserts the expected result.

## 15. Required tests for the validator itself

The validator implementation MUST include cases covering at least:

| Case | Expected result |
|---|---|
| exact goal/operation/build match | PASS identity check |
| goal ID mismatch | `EVD-003` |
| operation mismatch | `EVD-004` |
| build fingerprint mismatch | `EVD-006` |
| missing evidence record | `EVD-001` |
| claimed range equal to demonstrated range | PASS containment |
| claimed range strictly inside demonstrated range | PASS containment |
| claimed minimum below demonstrated minimum | `EVD-013` |
| claimed maximum above demonstrated maximum | `EVD-013` |
| reversed demonstrated range | semantic validation failure |
| required boundary absent | `EVD-009` |
| required negative control absent | `EVD-010` |
| contradictory observations | `EVD-012` |
| evidence from another build | `EVD-006` / `EVD-017` as applicable |
| static-only evidence used for runtime promotion | `SEM-012` |
| inferred evidence used as independent promotion evidence | `SEM-013` |
| one successful observation with no reproduction | `SEM-004` / repeatability gate failure |

## 16. Relationship to the error schema and taxonomy

The structural error object is defined by:

`schemas/ACAP-PROMOTION-ERROR-1.0.schema.json`

The normative error-code meanings are defined by:

`docs/ACAP-PROMOTION-ERROR-1.0-TAXONOMY.md`

This document supplies the cross-record semantic rules those artifacts intentionally do not encode as portable JSON Schema assertions.
