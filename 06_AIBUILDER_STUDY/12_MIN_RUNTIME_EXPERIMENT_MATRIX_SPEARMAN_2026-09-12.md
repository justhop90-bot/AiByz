# Minimal Runtime Experiment Matrix — `desired-number-spearmen`

**Date:** 2026-09-12  
**Status:** QUALIFICATION PLAN — no runtime result claimed  
**Scope:** `AiBuilder.per`, `AiBuilder/phaseUpdate.per`, `AiBuilder/ByzBot.per`, `AiBuilder/militaryUnits.per`  
**Purpose:** distinguish (1) same-pass Goal-write precedence, (2) persistence after the Stable disappears, and (3) phase-transition overwrites, using the smallest practical runtime matrix and no scenario-loader automation.

## 1. Measurement contract

The experiment must observe the **Goal value**, not merely whether a `train` command was accepted.

For every run record, at minimum:

```text
T0: desired-number-spearmen before stimulus
T1: desired-number-spearmen after Stable-trigger write
T2: desired-number-spearmen after Stable removal
T3: desired-number-spearmen after phase transition
```

If the available measurement mechanism cannot distinguish T1/T2/T3, the experiment is insufficient for this qualification.

Do not infer Goal value from unit count alone.

## 2. Test matrix

| Test | Stable | Phase transition | Purpose | Expected discriminator |
|---|---|---|---|---|
| **A — Control** | No | No | Establish baseline persistence with neither writer newly eligible | Goal remains at prior baseline; confirms measurement is stable |
| **B — Stable persistence** | ON → OFF | No | Isolate ByzBot write and disappearance of its condition | If Goal remains `10` after OFF, ByzBot has no automatic expiry/reset; if baseline returns without another writer, a hidden engine/Builder behavior exists |
| **C — Same-pass conflict** | ON | Yes, while ON | Both writers eligible in the same evaluation window | Immediate post-transition Goal distinguishes which write survives when both writers compete: phase baseline vs `10`; if only post-pass observation is available and ByzBot can fire again, result is marked ambiguous rather than promoted |
| **D — Phase overwrite after expiry** | ON → OFF | Yes, after OFF | Separates phase overwrite from continuing ByzBot writes | If `10` persisted in B and then changes to the new phase baseline in D, phaseUpdate is confirmed as an effective later overwrite |

**Minimum matrix: 4 runs.**

A is a control rather than strictly necessary for the logical three-question distinction, but it is retained because it detects a bad measurement harness and establishes the unperturbed Goal behavior. Removing A would make the matrix three runs but materially weakens qualification quality.

## 3. Test B — persistence

### Setup

1. Hold the AI in a stable phase; do not trigger a phase transition.
2. Establish a known baseline `B` for `desired-number-spearmen`.
3. Make the enemy Stable predicate true.
4. Observe Goal = `10` after ByzBot becomes eligible.
5. Remove the Stable condition.
6. Observe the Goal again without causing a phase transition or introducing another known writer.

### Interpretation

- `10` remains → **persistence confirmed** for the tested runtime path.
- Baseline `B` returns → there is an additional reset/overwrite mechanism not accounted for by the current source model.
- Any other value → identify every active writer before interpreting it.

This test isolates persistence because `phaseUpdate` is not supposed to write merely because the phase remains unchanged.

## 4. Test C — same-pass precedence

This is the critical test and requires care.

### Setup

1. Start from a known phase baseline `B`.
2. Make Stable true so ByzBot's intended write is `10`.
3. Cause a phase transition whose phase baseline is a **known value different from 10**. Call it `P`.
4. Arrange the transition so Stable remains true during the transition.
5. Measure the Goal at the earliest reliable point after the competing writes.

### Discriminator

```text
Observed = P  → phaseUpdate's write survived the competing pass
Observed = 10 → ByzBot's write survived the competing pass
Observed = another value → another writer or measurement ambiguity
```

### Critical caveat

A final observation of `10` is **not automatically proof that ByzBot won the same pass**, because its rule is repeatable and may have written `10` again on a subsequent evaluation before observation.

Likewise, observing `P` does not prove exact registration order; it proves only that the phase value was the effective value at the measurement point.

Therefore the strongest qualification requires either:

- an instrumentation point capable of observing the Goal between the two competing rule effects, **or**
- a minimal harness variant in which each competing writer is made one-shot for the qualification run while preserving the same predicates and `set-goal` operations.

The latter is preferable to a gameplay probe because it directly isolates scheduler semantics.

## 5. Test D — phase overwrite after Stable disappears

### Setup

1. Begin with Stable true.
2. Allow ByzBot to establish `desired-number-spearmen = 10`.
3. Turn Stable false.
4. Verify the Goal remains `10` as established by Test B.
5. Trigger a phase transition to a phase with known baseline `P != 10`.
6. Observe the Goal after the transition.

### Interpretation

```text
10 → P
```

is the cleanest source/runtime demonstration that a phase transition can overwrite a previously persistent Byzantine Goal.

If it remains `10`, investigate another writer or a phase-update qualification failure before changing architecture.

## 6. Why four tests are enough

The three required properties form a minimal causal chain:

```text
B: Does ByzBot's value survive disappearance?
             ↓
C: What happens when phaseUpdate and ByzBot compete?
             ↓
D: Can phaseUpdate replace the persistent ByzBot value afterward?
```

A provides the control condition that neither writer is newly active.

No production-world outcome is required. The target variable is the **Goal itself**.

## 7. Required stimulus values

Do not use a phase baseline equal to `10` for the precedence tests. If `P = 10`, the two competing outcomes become observationally identical.

Use:

```text
ByzBot override = 10
phase baseline = any known value != 10
```

For maximum clarity, choose a phase baseline of `0` if that is already the active configuration and does not introduce another confounder. Otherwise use a deliberately distinctive configured value such as `7`.

Do not change production executor logic merely to perform this qualification.

## 8. Confounders to exclude

The run is invalid for precedence qualification if any of these can write `desired-number-spearmen` unexpectedly:

- another Byzantine policy file
- an unrecognized customization rule
- a second copy of `ByzBot.per`
- an unrelated test rule
- a phase transition occurring earlier/later than intended
- a measurement mechanism that reports unit count rather than Goal value

The active writer set must therefore be frozen and recorded before the run.

## 9. Result classification

| Result | Classification |
|---|---|
| Goal value directly observed at each measurement point | DIRECT / CONFIRMED |
| Persistence inferred from stable value across condition removal | DIRECT runtime observation |
| Same-pass winner directly isolated by one-shot harness or intermediate observation | DIRECT runtime qualification |
| Winner inferred only from final value with repeatable ByzBot | INCONCLUSIVE / do not promote |
| Phase overwrite observed after Stable is false | DIRECT runtime qualification |
| World-state unit production inferred from Goal behavior | **NOT QUALIFIED** |

## 10. Stop condition

Do not expand into the other seven production targets until the spearman contract is classified as one of:

1. **QUALIFIED — phase wins same-pass conflict**
2. **QUALIFIED — ByzBot wins same-pass conflict**
3. **QUALIFIED — scheduler semantics require a different policy structure**
4. **UNQUALIFIED — measurement cannot isolate same-pass effects**

Only after this is resolved should the exact writer pattern be replicated for skirmishers, archers, camel riders, monks, bombard cannons, fireships, and unique units.

## 11. Architecture consequence

This experiment does **not** justify a new arbitration executor.

The purpose is narrower: establish the semantics of the existing Builder customization channel before scaling it.

The intended architecture remains:

```text
phase baseline
      ↓
Byzantine customization
      ↓
existing desired-number-spearmen Goal
      ↓
AiBuilder militaryUnits executor
      ↓
engine
```

The only currently unqualified edge is the behavior when both policy writers are eligible in the same evaluation window.
