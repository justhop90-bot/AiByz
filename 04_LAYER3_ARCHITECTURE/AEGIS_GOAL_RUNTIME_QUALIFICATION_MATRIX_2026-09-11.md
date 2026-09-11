# AEGIS — Goal Runtime Qualification Matrix

**Date:** 2026-09-11  
**Status:** DISPOSABLE RUNTIME QUALIFICATION PLAN — NOT IMPLEMENTATION  
**Target:** AoE2DE target build used by AEGIS; record exact executable/build fingerprint at execution time  
**Scope:** ACAP candidate goal IDs 740–759; operations `set-goal`, `goal`, `up-modify-goal`, `up-compare-goal`

## 1. Purpose

Directly establish which candidate scalar goals and operations are accepted and observable by the target AoE2DE build before any ACAP production code uses them.

Static range validity is not runtime qualification. Every promoted operation must have direct runtime evidence on the exact target build.

## 2. Safety rules

- Qualification is disposable and isolated from production AEGIS logic.
- Do not load or modify the production ACAP implementation.
- Do not redefine, repurpose, or overwrite existing stock AEGIS goals.
- Do not use stock architectural goals as test storage.
- Use a dedicated disposable probe file and a fresh test context.
- Record build fingerprint, probe version/hash, exact rule text, primitive arguments, expected value, observed value, validator result, runtime result, and timing.
- A crash, parser rejection, silent non-mutation, or ambiguous observation is a FAIL/UNRESOLVED result, not a pass.
- Do not infer legality of one primitive from another primitive's success.

## 3. Candidate goal IDs

| ID | Candidate role |
|---:|---|
| 740 | generation |
| 741 | valid |
| 742 | FSM state |
| 743 | required capability |
| 744 | verified capability |
| 745 | deficit |
| 746 | candidate |
| 747 | quantity |
| 748 | feasibility |
| 749 | authorization |
| 750 | production requested |
| 751 | production pending |
| 752 | production baseline |
| 753 | observed capability |
| 754 | reassessment/expiry |
| 755 | failure |
| 756 | evidence strength |
| 757 | consumed threat generation |
| 758 | attempts |
| 759 | physical-production permit |

## 4. Required operations

Each goal ID is tested independently with:

1. `set-goal`
2. `goal`
3. `up-modify-goal`
4. `up-compare-goal`

No operation is promoted merely because another operation succeeds.

## 5. Value matrix

Use the following scalar values where the primitive permits them:

### V0 — initialization

`0`

Purpose: establish deterministic baseline and prove that the goal can be written/read at zero.

### V1 — ordinary positive value

`1`

Purpose: prove ordinary nonzero storage/comparison.

### V2 — representative ACAP value

`10`

Purpose: exercise a realistic small capability/count value.

### V3 — comparison upper-bound probe

`511`

Purpose: test the known strict comparison-domain boundary without assuming that the storage domain has the same limit.

### V4 — first out-of-comparison-domain probe

`512`

Purpose: negative control for `up-compare-goal` value handling. Do not interpret failure here as evidence that the goal itself cannot store 512.

### V5 — high storage probe

`3500`

Purpose: test the known high end of the ordinary AEGIS goal-value range where applicable. This is specifically a storage-value probe, not an assertion that `up-compare-goal` accepts 3500.

### V6 — high negative-control value

`3501`

Purpose: probe rejection above the known scalar-goal value ceiling where the parser/validator permits the test to reach runtime.

## 6. Per-ID operation matrix

For each ID 740–759 execute the following independent cases.

| Case | Primitive | Expected value/operand | Required observation |
|---|---|---:|---|
| S0 | `set-goal` | 0 | write accepted; later `goal` returns 0 |
| S1 | `set-goal` | 1 | write accepted; later `goal` returns 1 |
| S2 | `set-goal` | 10 | write accepted; later `goal` returns 10 |
| S3 | `set-goal` | 511 | determine storage acceptance |
| S4 | `set-goal` | 512 | determine storage acceptance independently of compare legality |
| S5 | `set-goal` | 3500 | determine high-value storage acceptance |
| S6 | `set-goal` | 3501 | expected negative control if validator exposes the ceiling |
| G0 | `goal` | after S0 | returns 0 |
| G1 | `goal` | after S1 | returns 1 |
| G2 | `goal` | after S2 | returns 10 |
| G3 | `goal` | after S3 | returns the successfully stored value, if S3 passes |
| M0 | `up-modify-goal` | controlled increment from 0 | exact expected mutation observed |
| M1 | `up-modify-goal` | controlled decrement/inverse if legal | exact expected mutation or explicit rejection |
| M2 | `up-modify-goal` | boundary-adjacent value | determine behavior without contaminating later cases |
| C0 | `up-compare-goal` | compare against 0 | true/false matches known stored value |
| C1 | `up-compare-goal` | compare against 1 | true/false matches known stored value |
| C2 | `up-compare-goal` | compare against 10 | true/false matches known stored value |
| C3 | `up-compare-goal` | compare against 511 | direct boundary result |
| C4 | `up-compare-goal` | compare against 512 | negative-control result |
| C5 | `up-compare-goal` | compare against 3500 | negative-control result; do not classify as storage failure |

## 7. Operation-specific tests

### 7.1 `set-goal`

For each ID:

1. Set 0.
2. Read it with `goal`.
3. Set 1.
4. Read it.
5. Set 10.
6. Read it.
7. Set 511.
8. Read it.
9. Set 512.
10. Read it.
11. Set 3500.
12. Read it.
13. Attempt 3501 only if the probe harness can safely record validator rejection without terminating qualification.

Promotion condition: exact write/read agreement for every value claimed legal.

### 7.2 `goal`

`goal` is qualified only against values previously written by `set-goal` in the same isolated probe.

Promotion condition: returned value exactly equals the last accepted write; no stale value may be treated as success.

### 7.3 `up-modify-goal`

Use fresh disposable state for every case.

Baseline:

`set-goal <ID> 0`

Then apply the smallest legal positive modification and observe with `goal`.

Repeat from a known baseline using a boundary-adjacent modification. Record the exact resulting value.

If a decrement/inverse form is supported by the target primitive syntax, qualify it independently; otherwise record it as unsupported rather than inventing syntax.

Promotion condition: exact observed arithmetic mutation with no cross-test state contamination.

### 7.4 `up-compare-goal`

Do not test this by assuming that a goal ID's storage domain equals its comparison operand domain.

For each ID:

1. Store 0; compare against 0 and 1.
2. Store 1; compare against 0 and 1.
3. Store 10; compare against 10 and 11.
4. Store 511; compare against 511 and 510.
5. If storage of 512 succeeds, compare against 512 as a negative control.
6. If storage of 3500 succeeds, compare against 3500 as a negative control.

Promotion condition: the exact comparison expression used by ACAP is directly demonstrated, including its operand range.

## 8. Negative controls

Negative controls are mandatory because a successful low-value test does not establish boundary behavior.

### NC-1 — high goal value

Attempt storage of `3501` where safe. Expected outcome: rejection if the target validator enforces the known 3500 ceiling.

### NC-2 — comparison operand 512

Use a valid candidate goal but attempt an `up-compare-goal` comparison involving `512`. Expected outcome: rejection/invalidity if the target's comparison domain is 0–511. The exact observed behavior must be recorded.

### NC-3 — comparison operand 3500

Use a goal that successfully stores 3500, then attempt comparison against 3500. This separates storage legality from comparison legality.

### NC-4 — adjacent stock-range goal

Select a documented stock goal immediately outside the candidate namespace only as a read-only negative control. Never write it. Record its identity and provenance. The test must establish that the probe did not accidentally overwrite stock state.

### NC-5 — uninitialized candidate read

In a fresh probe context, read a candidate ID before any explicit `set-goal`. Record the observed value. This establishes initialization behavior and must not be interpreted as proof of legal persistent initialization.

## 9. Isolation protocol

Each case must start from a clean disposable state whenever mutation history could affect interpretation.

Recommended execution order per ID:

```text
fresh probe
  ↓
NC-5 uninitialized read
  ↓
S0 → G0
  ↓
S1 → G1
  ↓
S2 → G2
  ↓
S3 → G3
  ↓
S4 → G4
  ↓
S5 → G5
  ↓
S6 if safe
  ↓
M0/M1/M2 on fresh state
  ↓
C0/C1/C2/C3
  ↓
C4/C5 negative controls
```

Do not reuse a mutated goal for a later test unless the expected starting state is explicitly recorded.

## 10. Required evidence record

Every test row must produce:

```text
build_fingerprint
executable_version
probe_file_hash
probe_case_id
goal_id
primitive
argument_types
initial_goal_value
requested_value_or_operand
expected_result
validator_result
runtime_result
observed_goal_value
observed_compare_result
first_observation_time
completion_observation_time
error_or_rejection_text
pass_fail_unresolved
notes
```

## 11. Qualification rules

A goal/operation pair is:

- **RUNTIME QUALIFIED** only when the exact operation and argument form are directly demonstrated on the target build.
- **RUNTIME REJECTED** when the target validator/runtime directly rejects the exact operation.
- **UNRESOLVED** when evidence is incomplete, ambiguous, or dependent on an unproven behavior.
- **NOT TESTED** when the case was not executed.

A goal ID becomes **ACAP IMPLEMENTATION-QUALIFIED** only for the specific operations required by its assigned role. It is not enough for the ID to be globally writable.

## 12. ACAP promotion mapping

| ACAP role | Minimum required runtime operations |
|---|---|
| generation | `set-goal`, `goal`, comparison if used for generation gating |
| valid | `set-goal`, `goal`, comparison |
| FSM state | `set-goal`, `goal`, comparison |
| required capability | `set-goal`, `goal`, arithmetic mutation if used |
| verified capability | `set-goal`, `goal`, arithmetic mutation if used |
| deficit | `set-goal`, `goal`, arithmetic mutation and comparison |
| candidate | `set-goal`, `goal`, comparison |
| quantity | `set-goal`, `goal`, comparison |
| feasibility | `set-goal`, `goal`, comparison |
| authorization | `set-goal`, `goal`, comparison |
| production requested | `set-goal`, `goal`, comparison |
| production pending | `set-goal`, `goal`, comparison |
| production baseline | `set-goal`, `goal` |
| observed capability | `set-goal`, `goal`, arithmetic mutation if used |
| reassessment/expiry | `set-goal`, `goal`, comparison |
| failure | `set-goal`, `goal`, comparison |
| evidence strength | `set-goal`, `goal`, comparison |
| consumed threat generation | `set-goal`, `goal`, comparison |
| attempts | `set-goal`, `goal`, arithmetic mutation if used |
| production permit | `set-goal`, `goal`, comparison |

## 13. Promotion gate

The runtime matrix does not authorize implementation by itself.

The ACAP middle layer may use a goal ID only after:

1. the exact goal ID is shown writable/readable on the target build;
2. every required mutation operation is shown legal;
3. every required comparison operation is shown legal with its actual operand domain;
4. boundary behavior is recorded;
5. negative controls behave as expected or are explicitly explained;
6. no stock goal was modified;
7. the evidence is archived with build fingerprint and probe hash;
8. the resulting qualified namespace is frozen before production implementation.

Until then, 740–759 remain **candidate IDs**, not production ABI.
