# AiBuilder Existing-Channel Trace — `desired-number-skirmishers`

**Status:** STATIC AUDIT — NOT RUNTIME QUALIFIED  
**Purpose:** Establish the complete existing Goal → reader → action path before any Byzantine write authority is considered.  
**Scope:** `desired-number-skirmishers` only. No source modification or new Goal allocation is authorized by this document.

---

## 1. Executive finding

The existing AiBuilder substrate provides a complete **static** production path for `desired-number-skirmishers`:

```text
phaseUpdate policy constant
        ↓
set-goal desired-number-skirmishers
        ↓
Goal 57
        ↓
militaryUnits reads Goal 57
        ↓
unit-type-count-total skirmisher-line < Goal 57
        ↓
can-train skirmisher-line
        ↓
train skirmisher-line
```

This proves the **source-level data path**. It does **not** prove runtime write precedence, rule firing order, command acceptance, unit creation, or strategic effect.

The critical additional finding is that `phaseUpdate` guards its phase-policy writes with:

```text
(up-compare-goal current-phase g:!= previous-phase)
```

while the inspected `phaseUpdate.per` corpus contains **no writer for `previous-phase`**. Therefore the intended one-time phase-transition latch is not statically closed. Whether the predicate remains continuously true at runtime depends on the initial/default value and rule-engine scheduling semantics. This is a separate substrate finding and must not be silently converted into an assumed runtime behavior.

---

## 2. ABI identity

`AiBuilder.per` explicitly binds:

```text
(defconst desired-number-skirmishers 57)
```

This is DIRECT source evidence that the channel is Goal 57 in the current composition root.

Source: `AiBuilder.per` (current main, blob `3028f852d06e98cefde9a71054b5dd7522026fc6`).

**Classification:**

- Goal symbol: `desired-number-skirmishers`
- Numeric slot: `57`
- Width: 1 Goal
- Current extension status: existing channel; Byzantine write authority NOT AUTHORIZED

---

## 3. Writer path — `phaseUpdate`

`phaseUpdate.per` contains phase-policy rules that write:

```text
(set-goal desired-number-skirmishers phase1-skirmisher-cap-easy)
(set-goal desired-number-skirmishers phase1-skirmisher-cap-moderate)
(set-goal desired-number-skirmishers phase1-skirmisher-cap-hard)
```

and corresponding phase 2–5 variants.

The writes are guarded by the same transition predicate:

```text
(up-compare-goal current-phase g:!= previous-phase)
(goal current-phase N)
```

for the applicable phase and difficulty block.

Source: `AiBuilder/phaseUpdate.per` (current main, blob `77da34106abe91ef67fb725e9710ee03df02588d`).

**Classification:** DIRECT.

### Writer ownership

Current source writer: **`phaseUpdate`**.

Current policy authority: **AiBuilder phase policy**.

Byzantine policy is **not authorized to write Goal 57** merely because the channel is an existing desired-state interface.

---

## 4. Reader path — `militaryUnits`

`militaryUnits.per` contains the direct execution rule:

```text
(unit-type-count-total skirmisher-line g:< desired-number-skirmishers)
(can-train skirmisher-line)
=>
(train skirmisher-line)
```

Therefore the Goal is not merely stored policy metadata. It is directly consumed by a production rule whose action is `train skirmisher-line`.

Source: `AiBuilder/militaryUnits.per` (current main, blob `92695f6d448d4f30c31ac9590c6387bc9ab8542c`).

**Classification:** DIRECT.

### Reader semantics established statically

The rule requires both:

1. current total skirmisher-line count is below Goal 57's value; and
2. `can-train skirmisher-line` is true.

The consequent issues `train skirmisher-line`.

This establishes a **desired-count → train-request** path, not a guarantee of production completion.

---

## 5. Load-order fact vs. execution-order claim

The current ABI matrix records the composed module order as:

```text
AiBuilder.per
constantsUP
phaseUpdate
...
militaryUnits
...
militaryBehavior
```

`phaseUpdate` therefore precedes `militaryUnits` in the composition/load corpus.

**Important:** source/load order is NOT sufficient evidence that `phaseUpdate` writes Goal 57 immediately before `militaryUnits` reads it, nor that one module's rule fires before another module's rule. No runtime scheduling guarantee is claimed here.

Therefore:

```text
LOAD ORDER ≠ RULE FIRING ORDER ≠ LAST-WRITE AUTHORITY
```

This is the central unresolved question for B1.

---

## 6. `previous-phase` ownership defect / unresolved transition latch

The root declares:

```text
(defconst previous-phase 2)
```

The inspected `phaseUpdate.per` corpus reads `previous-phase` in the phase-policy predicates, but a source search found **no `set-goal previous-phase ...` writer**.

This is a DIRECT static ownership finding.

It does **not** yet prove that `previous-phase` is a bug. Possible interpretations include:

- incomplete phase-transition state tracking;
- intentionally constant/vestigial state;
- a missing writer in the current composition;
- a semantic mechanism outside the inspected source.

The repository currently establishes only:

```text
previous-phase: declared
previous-phase: read
previous-phase: no local writer found
intended transition-latch semantics: NOT ESTABLISHED
```

D-01 remains independent of B1 and is not authorized for repair merely to facilitate Byzantine policy.

---

## 7. Current channel contract

| Property | Current status | Evidence |
|---|---|---|
| Goal symbol exists | CONFIRMED | DIRECT |
| Goal number = 57 | CONFIRMED | DIRECT |
| Phase policy writes Goal 57 | CONFIRMED | DIRECT |
| Military execution reads Goal 57 | CONFIRMED | DIRECT |
| Reader produces `train skirmisher-line` request | CONFIRMED | DIRECT |
| `can-train` gates request | CONFIRMED | DIRECT |
| Unit creation follows request | NOT ESTABLISHED | Runtime evidence required |
| Goal write precedence | NOT ESTABLISHED | Runtime scheduling required |
| `phaseUpdate` always wins | NOT ESTABLISHED | Cannot infer from load order |
| Byzantine write authority | NOT AUTHORIZED | Governance decision pending |
| Phase-transition latch via `previous-phase` | NOT ESTABLISHED | No local writer found |
| Strategic effect | NOT ESTABLISHED | W2–W4 evidence required |

---

## 8. B1 qualification consequence

The original B1 question can now be narrowed precisely:

> **If an additive policy rule writes a different value to existing Goal 57, can the existing `militaryUnits` rule observe that value at its decision point and issue the corresponding train request?**

The static corpus already proves the reader/action side. Therefore B1 should **not** retest whether `militaryUnits` reads Goal 57. That is already DIRECT source evidence.

The runtime qualification only needs to resolve the unresolved boundary:

```text
additive writer
      ↓
Goal 57
      ↓
existing militaryUnits reader
      ↓
train request
```

The qualification must capture the **train-request boundary** before using eventual unit count as corroboration.

---

## 9. Minimum runtime qualification — tester-facing definition

No broad probe campaign is authorized or required.

### A1 — Same-pass authority

Use a controlled condition in which the existing phase policy establishes baseline `B`, then the additive test rule attempts override `O`.

Observe whether the existing `militaryUnits` rule behaves as if Goal 57 = `O`.

**Primary observation:** train request behavior.  
**Secondary observation:** resulting unit production, where observable.

### A2 — Repeated recomputation

Have the additive rule produce `O1`, then a later evaluation produce `O2`.

Determine whether the existing reader responds to the latest effective Goal value rather than a one-time initialization value.

### A3 — Phase transition

Only after A1/A2 are interpretable, test whether a phase-policy rewrite and additive rewrite can establish a deterministic effective value after a phase transition.

A3 must not be interpreted as proof of D-01. It is a separate observation of the interface under phase-policy activity.

---

## 10. Failure classification

| Observation | Interpretation |
|---|---|
| `militaryUnits` behaves according to override | Existing-channel write path is viable for the tested scheduling condition |
| `militaryUnits` behaves according to baseline | Additive writer does not control the effective Goal at the reader's decision point |
| Goal appears changed but no train request follows | Goal is not the only production authority; inspect other preconditions before assigning fault |
| Train request occurs but no unit appears | Request-to-world transition remains unproven; do not call this a Goal-interface failure |
| Behavior changes inconsistently between equivalent passes | Rule scheduling/authority is nondeterministic or incompletely controlled; B1 fails closure |
| Phase transition changes outcome | Interface is phase-coupled; A3 requires explicit ownership/lifecycle treatment |

---

## 11. What this audit does NOT establish

This document does not establish:

- legality of new Goal declarations in 122–479;
- legality of Goal 500;
- timer allocation;
- enemy observation primitives;
- Byzantine strategic policy;
- engine acceptance of `train`;
- unit creation;
- strategic success;
- any runtime rule-firing order not directly observed.

Those remain separate proof questions.

---

## 12. Evidence disposition

**Static substrate trace:** CLOSED for this channel.  
**Existing-channel authority:** OPEN — requires targeted runtime qualification.  
**D-01 (`previous-phase`):** OPEN — independent architectural ownership question.  
**New Goal allocation:** OPEN — UC-04'.  
**Byzantine implementation:** BLOCKED.

### Canonical principle

> **The existing AiBuilder substrate already exposes a complete desired-count → execution-request path. The remaining question is not whether the path exists; it is whether an additive policy layer can become the effective writer without violating existing ownership or relying on unproven rule-order semantics.**

---

**Next audit target:** finish the existing-channel ownership/liveness pass for the remaining desired military Goals, then finalize the smallest B1 runtime qualification package. No new Goal or timer should be allocated before UC-04' is independently resolved.
