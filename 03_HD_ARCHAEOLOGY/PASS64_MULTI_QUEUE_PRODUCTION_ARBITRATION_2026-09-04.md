# Pass 64 — Multi-Queue Production Arbitration Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Status:** PASS / EVIDENCE-BOUNDARY PRESERVED  
**Predecessors:** Passes 56–63

## Mission

Determine how historical AI production decisions interact with multiple production locations and whether resource arbitration, queue eligibility, and actual queue execution should be modeled as separate stages.

## Executive finding

The historical evidence supports a layered production-control model rather than a single atomic `train-unit` decision:

```text
CAPABILITY DEMAND
↓
RESOURCE / COMMITMENT GATE
↓
AFFORDABILITY / CAN-TRAIN
↓
PRODUCTION-LOCATION ELIGIBILITY
↓
TRAIN COMMAND
↓
QUEUE / PENDING STATE
↓
WORLD COMPLETION
↓
REASSESSMENT
```

A resource commitment can authorize a production action without proving that the resulting unit has already entered the world. Queueing, pending state, and completion must remain separate evidence states.

## Key closure from prior passes

The prior economic-arbitration work establishes that rule order and resource side effects can determine which eligible spending path obtains execution opportunity first. This does not imply a centralized global production scheduler.

The correct distinction is:

```text
ELIGIBLE DEMAND
≠
AUTHORIZED DEMAND
≠
QUEUE REQUEST
≠
QUEUED OBJECT
≠
COMPLETED UNIT
```

## Multi-location problem

A military demand may have multiple possible producers. Therefore production archaeology must distinguish:

1. unit eligibility;
2. producer eligibility;
3. resource affordability;
4. queue capacity/state;
5. actual train command;
6. resulting pending lifecycle;
7. completion.

A `can-train` result alone cannot establish which production building ultimately executed the request unless producer identity is independently established.

## Arbitration model

The strongest historical reconstruction is:

```text
DEMAND A ─┐
          ├→ RULE / STATE GATES → RESOURCE STATE → FIRST EFFECTIVE ACTION
DEMAND B ─┘

FIRST EFFECTIVE ACTION
↓
RESOURCE / STATE SIDE EFFECT
↓
OTHER DEMANDS MAY LOSE ELIGIBILITY
```

This is **procedural arbitration**, not proven numeric utility optimization.

## Byzantine relevance

For Byzantines, multiple legitimate military demands can simultaneously target the same production economy:

```text
CAMEL
CATAPHRACT
SIEGE
MONK
NAVY
UPGRADES
IMPERIAL TRANSITION
```

The eventual Byzantine policy therefore needs to reason about the distinction between:

```text
COUNTER SELECTED
→ RESOURCES PROTECTED
→ PRODUCTION AUTHORIZED
→ PRODUCTION ACTUALLY OCCURS
→ CAPABILITY BECOMES AVAILABLE
```

A counter decision cannot be considered successful merely because a production rule fired.

## Replay methodology consequence

The replay interpreter must preserve uncertainty around queue and completion transitions. A queue action should not automatically be promoted to a spawned unit. Strong evidence requires object identity or an equivalent producer/type/temporal linkage.

This preserves the established invariant:

> When evidence cannot prove transition, preserve uncertainty instead of inventing it.

## Important negative findings

This pass does **not** prove:

- a global production optimizer;
- a universal production priority score;
- that rule order alone controls every queue;
- that all production buildings are arbitrated through one shared controller;
- that historical Byzantine production follows one universal policy;
- that queue insertion guarantees eventual completion;
- that production authorization immediately changes world capability.

## Evidence ledger

| Finding | Grade |
|---|---|
| Historical AI separates feasibility/authorization from train side effects | DIRECT / COMPOSED |
| Resource commitment can gate production | DIRECT historical pattern |
| Rule order can affect resource-spending execution opportunity | DIRECT historical evidence |
| Queue/pending/completion should be distinct states | DIRECT technical + replay evidence |
| Multiple production locations create a producer-selection problem | COMPOSED / MECHANICAL |
| Global production scheduler | NOT PROVEN |
| Numeric production utility optimizer | NOT PROVEN |
| Universal queue arbitration policy | NOT PROVEN |
| Queue request = completed unit | REJECTED |

## Layer boundary

No `.per` implementation, architecture implementation, runtime deployment, or modification of the canonical bot was performed. This artifact is research only.
