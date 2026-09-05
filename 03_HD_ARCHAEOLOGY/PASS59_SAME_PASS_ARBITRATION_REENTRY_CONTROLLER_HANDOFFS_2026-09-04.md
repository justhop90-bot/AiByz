# Pass 59 — Same-Pass Arbitration, Re-entry & Controller Handoffs

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Status:** PASS / PARTIAL CLOSURE

## Mission
Determine how controller state mutations interact with later rules in the same script pass, and whether released commitments can immediately transfer execution opportunity to another controller.

## Executive finding
The historical scripting model supports a **two-clock interpretation**:

```text
CONTROLLER CLOCK
same-pass goal/SN/flag mutations

WORLD-OBSERVATION CLOCK
command → engine processing → world change → observable fact
```

These clocks must not be conflated.

## Same-pass state model

Where immediate state mutation is established:

```text
STATE₀
↓
RULE A
↓
STATE₁
↓
RULE B sees STATE₁
↓
STATE₂
```

This makes rule order a potential same-pass state machine.

However, not every observation updates at the same time. Some world-derived predicates can require the next script pass.

## Transaction lifecycle evidence

`research-pending` is better treated as an intermediate transaction-lifecycle observation than merely a boolean guard. `up-pending-objects` similarly exposes pending construction state in selected paths.

This supports:

```text
REQUEST
→ PENDING
→ WORLD PROCESSING
→ COMPLETED / INVALIDATED
```

rather than assuming command issuance equals completion.

## Controller handoff model

A useful archaeological reconstruction is:

```text
CONTROLLER A
↓
owns/claims economic commitment
↓
condition changes
↓
release / reset
↓
CONTROLLER B becomes eligible
```

But **same-pass handoff is not closed**.

The following remains an explicit open question:

```text
PASS N
A releases
→ B claims in PASS N?
```

versus:

```text
PASS N
A releases
PASS N+1
B claims
```

## Shared resource-control

`sn-resource-control` can act as an admission channel in selected historical controllers, but it is not proven to be a formal mutex. Its behavior depends on the gates that read it.

## Re-entry

After a transition, historical controllers can reset state and allow later rules to become eligible again. This produces a recurrent control loop:

```text
DECIDE
→ ACT
→ RESET
→ REASSESS
→ RE-ENTER
```

## Strongest closure

```text
COMPETING CAPABILITY DEMANDS
↓
CANDIDATE RULES BECOME ELIGIBLE
↓
RULE ORDER SELECTS FIRST EFFECTIVE PATH
↓
STATE / RESOURCE SIDE EFFECT
↓
OTHER CANDIDATES MAY LOSE ELIGIBILITY
↓
COMMITMENT PERSISTS
↓
NEXT PASS REASSESSES
```

## Evidence ledger

| Finding | Grade |
|---|---|
| Rule-side state mutations can affect later rule eligibility | DIRECT / COMPOSED |
| Goals/SNs can participate in same-pass control | DIRECT technical evidence |
| Some world observations update later | DIRECT technical evidence |
| Pending lifecycle states exist | DIRECT |
| Controllers can release/reset state and re-enter | COMPOSED / DIRECT patterns |
| Same-pass release → successor claim | NOT PROVEN |
| Global handoff protocol | NOT PROVEN |
| Global fairness | NOT PROVEN |

## Byzantine implication

The eventual Byzantine control model must distinguish internal controller-state latency from actual game-world latency. A counter commitment may be released internally before the resulting world state is observable.

## Layer boundary

No `.per` implementation. Research only.
