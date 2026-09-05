# Pass 62 — Cross-Controller Overwrite & Priority-Inversion Archaeology

**Date:** 2026-09-04
**Layer:** Layer 2 — research / archaeology only
**Implementation authority:** NONE
**Status:** PASS — PARTIAL CLOSURE / EVIDENCE BOUNDARIES PRESERVED
**Predecessor:** Pass 61

## Mission
Determine how shared goals/strategic numbers behave when multiple controllers can write the same channel, and distinguish procedural priority from true ownership or authority.

## Executive finding
Shared state should be modeled as a **contested control surface**, not as automatic ownership.

The historical scripting model provides commands/facts for reading and writing goals and strategic numbers, while rule order and state gates determine which controller gets an opportunity to write. Public technical documentation confirms that `set-strategic-number` writes an SN and `strategic-number` tests its value; it does not assign ownership semantics.

Therefore:

```text
STATE WRITE != AUTHORITY
STATE VALUE != OWNER
RULE ORDER != GLOBAL PRIORITY
```

## 1. Cross-controller overwrite model

When controllers A and B can both write the same channel:

```text
A eligible
→ A writes X
→ later rule(s) observe X where predicate semantics permit
→ B may be blocked, enabled, or may overwrite X
```

The exact outcome depends on rule placement, conditions, control-flow actions, engine semantics, and whether another subsystem automatically writes the channel.

A shared channel must therefore be analyzed as a graph:

```text
INITIALIZER
→ WRITER A
→ READER A/B
→ WRITER B
→ RESETTER
→ ENGINE AUTO-WRITER?
```

## 2. No evidence for universal SN ownership

The technical reference describes strategic numbers as numeric engine controls/state, but does not establish a universal ownership model. Some SNs are engine-facing parameters and some are commonly used as persistent control state.

Consequently, archaeology must establish for each contested SN:

1. Who initializes it?
2. Who writes it?
3. Who reads it?
4. Does engine code automatically modify it?
5. Does another controller overwrite it?
6. Is the value semantic, numeric, or target identity?

## 3. Rule order remains a procedural arbitration mechanism

Pass 56 established direct historical author evidence that rule order matters because the first executed rule can spend resources before later rules can. This remains the strongest direct HD evidence for procedural economic arbitration.

That mechanism can combine with shared state:

```text
RULE ORDER
+
STATE WRITE
+
RESOURCE SIDE EFFECT
=
LOCAL PROCEDURAL PRIORITY
```

But this does not prove a global scheduler.

## 4. Priority inversion

Two forms must be separated.

### Economic priority inversion
A lower-value or earlier-ordered commitment consumes a resource needed by a strategically more important capability.

### Temporal priority inversion
A controller is prevented from reconsidering or acting because a timer/cooldown remains active while another capability becomes urgent.

Both are AEGIS analytical concepts. Neither is an engine-defined term.

## 5. Same-pass overwrite vs next-pass overwrite

The distinction is essential:

```text
PASS N
A writes X
B later writes Y
```

is different from:

```text
PASS N
A writes X

PASS N+1
B observes X
→ B writes Y
```

The historical scripting family supports immediate goal/SN mutations and documents cases where observations require a later pass. Therefore same-pass behavior is predicate/action-specific and must not be generalized from one example.

## 6. Resource-control interpretation

`sn-resource-control` is especially sensitive because historical controllers use it both as a numeric gate and as target-bearing commitment identity.

The correct interpretation remains:

```text
resource-control can function as an admission/commitment channel
```

not:

```text
resource-control is universally an ownership mutex
```

A candidate claiming it does not automatically prove every other controller is excluded; the surrounding reader gates must be traced.

## 7. Overwrite categories

Every shared-state overwrite should be classified as one of:

```text
A. REASSERTION
   A writes the same value again.

B. CORRECTION
   A writes a new value because state changed.

C. REPLACEMENT
   A's commitment is replaced by another target.

D. CONFLICT
   B overwrites A while A still appears eligible.

E. ENGINE OVERWRITE
   engine/system logic changes the value.
```

Only D/E establish genuine cross-owner contention; A/B/C may be normal controller lifecycle.

## 8. What the evidence closes

The research now supports:

```text
shared state can coordinate distributed controllers
rule order can create local procedural priority
state gates can suppress competing controllers
resource consumption can remove downstream affordability
commitments can be replaced or cleared
```

It does not yet close:

```text
global ownership of shared state
same-pass release → immediate successor claim
systematic priority inversion in shipped HD gameplay
universal fairness
universal controller preemption
```

## 9. Practical archaeological test

For every contested channel, build a provenance table:

| Field | Required evidence |
|---|---|
| Initial value | initializer |
| Writer | exact rule/action |
| Reader | exact predicate |
| Guard | eligibility conditions |
| Side effect | resource/world mutation |
| Timer | temporal gate, if any |
| Reset | exact rule/action |
| Replacement | exact writer/transition |
| Engine writer | local/runtime verification |
| Same-pass visibility | predicate-specific evidence |
| Next-pass visibility | replay/script evidence |

Then reconstruct:

```text
WRITER A
→ STATE X
→ RULE B ELIGIBILITY
→ WRITER B?
→ SIDE EFFECT
→ RESET
```

This is the correct way to establish cross-controller authority without inferring it from variable names.

## 10. Byzantine consequence

The Byzantine civilization has many legitimate capability claimants:

```text
camel
cataphract
monk
siege
navy
imperial transition
military upgrades
```

Therefore shared economic control channels are strategically important. But the historical corpus does not prove that Byzantine decision-making used a centralized utility score to rank these alternatives.

The stronger research conclusion is:

```text
BYZANTINE OPTION BREADTH
→ MORE POTENTIAL COMMITMENT COMPETITION
→ GREATER VALUE OF EXPLICIT ARBITRATION RESEARCH
```

This is an AEGIS strategic inference, not a historical implementation claim.

## 11. Evidence ledger

| Finding | Grade |
|---|---|
| Goals/SNs can be written and read as shared controller state | DIRECT technical/reference evidence |
| Rule order can create procedural economic priority | DIRECT HD author evidence |
| Shared state does not inherently encode ownership | DIRECT semantic constraint / analytical conclusion |
| `sn-resource-control` can function as admission/commitment state | DIRECT historical pattern |
| Same-pass visibility is predicate/action-specific | DIRECT technical caution |
| Cross-controller overwrite is possible in the scripting model | COMPOSED / requires exact writer pair |
| Systematic priority inversion occurs in shipped HD gameplay | NOT PROVEN |
| Same-pass release → successor claim | NOT PROVEN |
| Global ownership protocol | NOT PROVEN |
| Global fairness mechanism | NOT PROVEN |
| Byzantine centralized utility arbitration | NOT PROVEN |

## 12. Layer boundary

No `.per` implementation or architecture implementation is created. This pass is research-only.
