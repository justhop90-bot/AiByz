# ACAP-PROMOTION-1.0 Validator Implementation Contract

**Status:** NORMATIVE DESIGN CONTRACT — implementation not yet claimed

## Objective

Implement a fail-closed validator for ACAP-PROMOTION-1.0 that validates structural schema, semantic promotion rules, and cross-record evidence relationships before any promotion can be granted.

## Core identity comparison

For every supporting evidence record:

```text
assert_equal(P.target.goal_id, E.goal_id, EVD-003)
assert_equal(P.target.operation, E.operation, EVD-004)
assert_equal(P.build.build_fingerprint, E.build.build_fingerprint, EVD-006)
```

The comparison is exact and case-sensitive for string fingerprints.

## Demonstrated-range algorithm

Given qualifying direct runtime observations for one exact target identity:

```text
Dmin = minimum directly demonstrated qualifying value
Dmax = maximum directly demonstrated qualifying value
Cmin = promotion.claimed_range.minimum
Cmax = promotion.claimed_range.maximum

require Dmin <= Cmin
require Cmax <= Dmax
```

If either requirement fails, emit `EVD-013` and prevent qualification.

The validator MUST also verify that every claimed boundary has an appropriate raw observation under the qualification protocol. `Dmin`/`Dmax` MUST NOT be synthesized from unsupported assumptions.

## Evidence selection

Only evidence records satisfying all identity/provenance requirements may enter the demonstrated-range calculation. Records from another goal, operation, build, run, or incompatible environment are excluded from qualifying evidence and produce the corresponding evidence error.

Exclusion does not make a promotion pass. If exclusion leaves insufficient evidence, the affected gate is unresolved or blocked.

## Error emission

Every failed rule produces an ACAP-PROMOTION-ERROR-1.0 object. The validator SHOULD emit the most specific applicable code and MAY emit additional independently established codes.

At minimum:

```text
EVD-001 unresolved reference
EVD-002 run mismatch
EVD-003 goal mismatch
EVD-004 operation mismatch
EVD-006 build fingerprint mismatch
EVD-009 missing boundary evidence
EVD-010 missing negative control
EVD-012 contradictory evidence
EVD-013 claimed range exceeds demonstrated range
EVD-014 evidence does not establish semantic result
EVD-015 incomplete provenance
EVD-017 incompatible build evidence
EVD-019 artifact integrity failure
```

## Promotion gate behavior

```text
schema failure
    → reject record

identity/provenance failure
    → block or unresolved

range containment failure
    → block promotion

runtime evidence absent
    → block promotion

semantic result absent
    → unresolved/block

contradictory evidence
    → unresolved/block

all required gates PASS
+ DIRECT evidence
+ reproduced evidence
+ coherent target identity
+ demonstrated range contains claimed range
    → eligible for ACAP-QUALIFIED
```

## Prohibited validator behavior

The implementation MUST NOT:

- coerce goal IDs or operations into matches;
- compare build versions while ignoring fingerprints;
- merge evidence from different builds;
- use static evidence as runtime evidence;
- use inferred evidence as direct evidence;
- expand a demonstrated range without raw observations;
- select favorable observations when records conflict;
- treat absence of an error as qualification;
- silently repair malformed evidence;
- invent completion or runtime observations.

## Test fixtures required before implementation qualification

The validator test suite MUST include exact-match, goal-mismatch, operation-mismatch, build-mismatch, run-mismatch, missing-reference, exact-containment, interior-containment, lower-bound failure, upper-bound failure, missing-boundary, negative-control, contradiction, static-only, inferred-only, and non-reproduced cases.

Passing validator unit tests does not qualify the AoE2DE goal namespace itself. It qualifies only the validator implementation against the normative records and rules.
