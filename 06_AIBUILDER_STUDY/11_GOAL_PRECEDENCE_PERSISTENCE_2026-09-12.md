# AiBuilder Goal Precedence & Persistence Qualification — 2026-09-12

**Status:** STATICALLY QUALIFIED; RUNTIME PRECEDENCE REMAINS UNQUALIFIED  
**Scope:** `AiBuilder.per`, `AiBuilder/phaseUpdate.per`, `AiBuilder/ByzBot.per`, `AiBuilder/militaryUnits.per`  
**Primary slice:** `desired-number-spearmen`  
**Purpose:** determine what can be proven from source about competing Goal writers, persistence, and the native production reader before changing architecture.

## 1. Executive result

The spearman Goal has **two active writers** in the current AiBuilder architecture:

1. `AiBuilder/phaseUpdate.per` writes `desired-number-spearmen` when a phase transition is detected.
2. `AiBuilder/ByzBot.per` writes `desired-number-spearmen 10` whenever the enemy Stable predicate is true.

The production executor is a separate reader/action path in `AiBuilder/militaryUnits.per` and does not compete for ownership of the Goal.

Static source analysis establishes the following:

- **Phase policy is event/transition-driven.** `phaseUpdate.per` uses `up-compare-goal current-phase g:!= previous-phase` before projecting the phase's unit caps.
- **ByzBot is condition-driven and repeatable.** Its Stable rule has no `disable-self`, so nothing in the source makes it a one-shot rule.
- **ByzBot does not contain a reset path.** When the Stable condition becomes false, the rule simply stops firing; there is no compensating `set-goal desired-number-spearmen <phase baseline>` rule in `ByzBot.per`.
- Therefore, **static rule semantics imply that a ByzBot-written value can persist after the triggering condition disappears until another writer changes the Goal**. This is a Goal-state inference from the source, not proof of a particular engine scheduling implementation.
- The root load order places `phaseUpdate` before `ByzBot`, and both before the production executor. However, **textual/load order is not sufficient evidence to assert same-pass final-write precedence**. The AoE2DE rule scheduler's exact ordering/visibility semantics remain unqualified here.

**Decision:** do not invent an arbitration layer yet. The correct unresolved question is the Builder/engine behavior of competing `set-goal` writes in the same evaluation cycle.

## 2. Writer ledger: `desired-number-spearmen`

| Writer | Condition | Write | Reset/expiry in same file | Static status |
|---|---|---:|---|---|
| `phaseUpdate.per` | `current-phase != previous-phase` AND phase = 1..5 AND active difficulty branch | phase-specific `phaseX-spearman-cap-{easy/moderate/hard}` | No explicit reset rule; next phase transition writes the new baseline | **CONFIRMED** |
| `ByzBot.per` | `players-building-type-count any-enemy stable > 0` | `10` | None | **CONFIRMED** |
| `militaryUnits.per` | `unit-type-count-total spearman-line < desired-number-spearmen` AND `can-train spearman-line` | **reads Goal; does not write it** | N/A | **CONFIRMED** |

The root allocates `desired-number-spearmen` as a Goal channel. `phaseUpdate.per` projects phase constants into that channel, while `ByzBot.per` uses the same channel for Byzantine policy.

## 3. Exact phase writer behavior

`phaseUpdate.per` detects a phase transition with:

```text
(up-compare-goal current-phase g:!= previous-phase)
```

and then, inside the difficulty-specific phase rule, executes a write such as:

```text
(set-goal desired-number-spearmen phase1-spearman-cap-easy)
```

Equivalent rules exist for the other phases and difficulty branches.

This means the phase writer is **not continuously rewriting the spearman Goal merely because the AI remains in the same phase**. Its write is tied to the detected phase change.

**Evidence:** DIRECT / CONFIRMED.

## 4. Exact Byzantine writer behavior

`AiBuilder/ByzBot.per` contains:

```text
(defrule
    (players-building-type-count any-enemy stable > 0)
=>
    (set-goal desired-number-spearmen 10))
```

There is no `disable-self` action, no timer condition, and no explicit phase condition.

Therefore, at the rule level:

```text
Stable condition true
        ↓
write Goal = 10
        ↓
condition remains true
        ↓
rule remains eligible
        ↓
write Goal = 10 again
```

This is **repeatable policy**, not a one-time event.

**Evidence:** DIRECT / CONFIRMED.

## 5. Persistence after threat/capability disappearance

The important asymmetry is:

```text
Phase writer:
    transition → write baseline

ByzBot:
    condition true → write 10
    condition false → no write
```

There is no rule in the current `ByzBot.per` that says:

```text
condition false → restore phase baseline
```

Consequently, once ByzBot writes `10`, that value is not statically scheduled to revert merely because the enemy Stable disappears.

The next identifiable source-level writer capable of replacing it is a later/next eligible phase projection from `phaseUpdate.per` (or any future/current third-party writer discovered by a complete Goal-writer search).

**Classification:** COMPOSED from DIRECT rule structure, with engine-state persistence treated as **PROBABLE/UNQUALIFIED** rather than runtime-proven.

## 6. Load order

The current root loads the Builder libraries in this order around the relevant files:

```text
AiBuilder\\phaseUpdate
AiBuilder\\general
AiBuilder\\market
AiBuilder\\economy
AiBuilder\\technologies
AiBuilder\\construction
AiBuilder\\ByzBot
AiBuilder\\militaryUnits
AiBuilder\\militaryBehavior
```

The root then provides a separate explicit:

```text
; - CUSTOMIZATION -
; You can add more lines to customize your AI here --->
```

section after the library loads.

Thus, structurally:

```text
phaseUpdate → ... → ByzBot → militaryUnits → militaryBehavior → CUSTOMIZATION
```

This is useful architectural evidence, but **must not be promoted to a same-pass precedence rule** without engine evidence.

### Why load order is insufficient

Several distinct questions must be separated:

1. In what order are files parsed/loaded?
2. In what order are rules registered?
3. In what order are eligible rules evaluated?
4. When does a `set-goal` mutation become visible to another rule?
5. If two eligible rules write the same Goal during one evaluation cycle, which value survives?
6. Does the next cycle see the final value from the prior cycle?

The repository currently proves #1. It does not prove #2–#6 for the target AoE2DE runtime.

## 7. Production reader boundary

`AiBuilder/militaryUnits.per` contains the native spearman executor:

```text
(unit-type-count-total spearman-line g:< desired-number-spearmen)
(can-train spearman-line)
=>
(train spearman-line)
```

This confirms that the executor consumes the Goal and performs the native training request. It does not establish that the request immediately creates a completed spearman in world state.

Therefore the authority boundary remains:

```text
Goal writers
    ↓
existing Builder Goal
    ↓
production deficit test
    ↓
can-train feasibility
    ↓
train request
    ↓
engine/queue/world transition
    ↓
count observation
```

No modification to `militaryUnits.per` is justified by the precedence finding.

## 8. Conflict matrix

### Case A — no Stable, no phase transition

```text
phaseUpdate: no write
ByzBot: no write
```

The current Goal remains whatever value the previous eligible writer left in it.

**Static consequence:** no source rule in these two files guarantees automatic baseline restoration.

### Case B — Stable appears during an established phase

```text
phaseUpdate: normally no phase-transition write
ByzBot: writes 10
```

The Goal becomes subject to the ByzBot policy.

**Runtime caveat:** exact mutation timing remains unqualified.

### Case C — Stable remains present across multiple passes

```text
ByzBot remains eligible and repeatedly writes 10.
```

There is no source-level expiry.

### Case D — phase transition while Stable is present

Both writers may become relevant:

```text
phaseUpdate → phase baseline
ByzBot → 10
```

This is the critical **same-cycle precedence case**.

The source does not prove which write is final if both are evaluated in the same cycle.

### Case E — phase transition after Stable disappears

`phaseUpdate` can replace the old Byzantine value with the new phase baseline.

This is the clearest source-level reset mechanism currently visible.

## 9. Architecture finding

The current architecture is not fundamentally broken because two policies write one Goal. The actual missing primitive is **well-defined ownership semantics** for shared Builder Goals.

The Builder-native hierarchy should remain:

```text
phase baseline
      ↓
Byzantine reactive customization
      ↓
existing desired-number-* Goal
      ↓
AiBuilder executor
```

But the exact composition rule must be known before scaling this pattern to all eight production targets.

Do **not** introduce a new `production-arbitration.per` yet.

## 10. What can be qualified without runtime probing

### CONFIRMED / DIRECT

- `phaseUpdate.per` writes `desired-number-spearmen` on phase transitions.
- `ByzBot.per` writes `desired-number-spearmen 10` while the Stable predicate is true.
- `ByzBot.per` has no `disable-self` on the Stable rule.
- `ByzBot.per` has no explicit reset/expiry rule for the spearman Goal.
- The root loads `phaseUpdate` before `ByzBot` and `militaryUnits`.
- The root has a dedicated post-load customization section.
- `militaryUnits.per` reads the Goal and uses `can-train` plus `train`.

### COMPOSED / PROBABLE

- A ByzBot override can persist after the Stable condition disappears until another writer changes the Goal.
- Phase transitions provide a natural Builder-native re-baselining point.
- The current production issue is Goal ownership/precedence, not executor capability.

### UNQUALIFIED / ENGINE-SPECIFIC

- Exact same-pass rule evaluation order.
- Whether file load order equals rule firing order.
- Whether a `set-goal` made by one eligible rule is visible to another rule in the same pass.
- Which competing writer wins if both phaseUpdate and ByzBot write the same Goal in one pass.
- Whether moving ByzBot into the explicit post-load CUSTOMIZATION section changes that precedence.

## 11. Minimum future runtime qualification

The smallest useful qualification is **not** a full gameplay test suite and does not require scenario-loader automation.

The single question to qualify is:

> When `phaseUpdate.per` and `ByzBot.per` are both eligible to write `desired-number-spearmen` in the same logical evaluation window, what Goal value is observed by `militaryUnits.per` afterward?

A future minimal ABI measurement should distinguish at least:

```text
baseline Goal
→ phase transition
→ Byzantine Stable condition
→ competing writes
→ resulting Goal
→ production reader
```

Until that measurement exists, the repository must label precedence as **ENGINE-SPECIFIC / UNQUALIFIED**.

## 12. Immediate implementation decision

**No production code change is required from this audit.**

The correct action is to preserve the native Builder executor and document the shared-Goal semantics explicitly.

The next implementation step is to qualify one Builder-native precedence contract for the spearman slice. Once that contract is known, the same writer analysis can be mechanically applied to skirmishers, archers, camel riders, monks, bombard cannons, fireships, and unique units.

This avoids prematurely designing an arbitration system that may contradict the Builder's native customization model.

## 13. Repository decision record

This document supersedes any earlier implication that textual load order alone establishes final Goal-writer precedence.

**Canonical statement:**

> File/load order is DIRECT evidence of structural ordering. It is not, by itself, DIRECT evidence of same-pass rule precedence or final Goal ownership.

That distinction is now part of the AEGIS/AiBuilder evidence standard for production policy.
