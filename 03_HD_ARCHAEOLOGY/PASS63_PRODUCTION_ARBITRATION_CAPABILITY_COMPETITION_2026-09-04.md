# Pass 63 — Production Arbitration & Capability Competition

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation authority:** NONE  
**Status:** PASS / PARTIAL CLOSURE  
**Predecessors:** Passes 55–62

## Mission
Trace the historical military-production pathway from capability demand through resource control, affordability, queue authorization, training, and reassessment. Determine what can be established about competition among production demands.

## Executive finding
Historical AI evidence establishes a production control chain in which **resource commitment and affordability gates can precede the training side effect**. The historical corpus contains explicit `can-train-with-escrow` → `release-escrow` → `train` patterns and named `sn-resource-control` commitments.

This closes the existence of a production-authorization layer, but does **not** prove a single global production scheduler or utility optimizer.

## Canonical production pipeline

```text
STRATEGIC DEMAND
↓
RESOURCE COMMITMENT
↓
RESOURCE PROTECTION / ESCROW
↓
CAN-TRAIN GATE
↓
RELEASE PROTECTED RESOURCES
↓
TRAIN COMMAND
↓
WORLD / QUEUE STATE
↓
REASSESSMENT
```

The distinction remains:

```text
INTENT ≠ AUTHORIZATION ≠ ACTION ≠ EXECUTION ≠ OUTCOME
```

## Historical production evidence

The historical corpus contains selected chains of the form:

```text
sn-resource-control == <unit-or-purpose>
↓
resource saving / escrow
↓
can-train-with-escrow <unit-line>
↓
release-escrow
↓
train <unit-line>
↓
reset resource-control
```

A particularly clear historical example is the battering-ram path. The same architecture also appears in other production commitments such as monks and navy.

## What this proves

1. A military production request can have a persistent commitment identity.
2. Resources can be protected for that production purpose.
3. Affordability can be evaluated with protected resources included.
4. The actual train command occurs after authorization/release in selected paths.
5. Completion/reset can reopen the resource-control channel.
6. Competing production requests can therefore interact through shared resource state.

## What it does not prove

It does not prove that the historical AI computes:

```text
utility(unit A) > utility(unit B)
```

It does not prove a global military-production scheduler.

It does not prove that all production buildings share one arbitration controller.

It does not prove that the first eligible unit is always strategically preferred.

## Queue authorization vs queue execution

A critical boundary is:

```text
CAN-TRAIN
≠
TRAIN
≠
UNIT COMPLETED
```

`can-train` is an authorization/feasibility predicate. `train` is a side-effecting command. Actual queue completion is a later world-state event.

This is consistent with the broader AEGIS transaction model.

## Competition model

When two demands share resources:

```text
DEMAND A
→ commitment A
→ escrow / resource consumption

DEMAND B
→ later eligibility check
→ affordability may fail
```

Thus production arbitration can emerge from:

```text
RULE ORDER
+
RESOURCE CONTROL
+
ESCROW
+
AFFORDABILITY
+
TRAIN COMMAND
```

The historical evidence is procedural rather than globally score-based.

## Queue-level open question

The research still needs to establish, for specific historical production contexts, whether the competition occurs primarily:

```text
BEFORE QUEUE AUTHORIZATION
```

or whether multiple already-authorized requests can compete inside a production queue.

The current evidence strongly supports the first layer but does not establish a universal queue scheduler.

## Byzantine significance

This is strategically important because Byzantine military demands can share scarce resources:

```text
CAMEL / HEAVY CAMEL
CATAPHRACT / ELITE / LOGISTICA
MONK
SIEGE
NAVY
MILITARY UPGRADES
IMPERIAL
```

The Byzantine problem is therefore:

```text
THREAT
↓
CAPABILITY REQUIREMENT
↓
CANDIDATE UNITS
↓
RESOURCE COMPETITION
↓
PRODUCTION AUTHORIZATION
↓
QUEUE
↓
DEPLOYMENT
↓
EFFECTIVE CAPABILITY
```

A nominally correct counter that cannot obtain production authorization in time is not an effective counter.

## New research concept: production opportunity

Define analytically:

> **Production opportunity** = the interval during which a production demand is both strategically relevant and capable of obtaining an effective queue/training action.

This is not an engine term.

It connects tempo with arbitration:

```text
STRATEGIC WINDOW
∩
RESOURCE FEASIBILITY
∩
PRODUCTION ACCESS
∩
QUEUE CAPACITY
=
PRODUCTION OPPORTUNITY
```

## Evidence ledger

| Finding | Grade |
|---|---|
| Historical production uses `can-train-with-escrow` | DIRECT |
| Historical production uses named `sn-resource-control` commitments | DIRECT |
| Resource commitment can precede train authorization | DIRECT / COMPOSED |
| `train` is a distinct side-effect command | DIRECT technical evidence |
| Queue completion is distinct from issuing `train` | DIRECT semantic constraint |
| Shared resource state can suppress competing production | DIRECT / COMPOSED |
| Production arbitration is globally centralized | NOT PROVEN |
| Numeric utility score chooses all production | NOT PROVEN |
| Queue itself is a universal scheduler | NOT PROVEN |
| Historical Byzantine production uses this exact generalized policy | NOT PROVEN |

## Closure

The historical AI clearly has a **production authorization layer** built from resource control, escrow, affordability, and train commands. This is a strong bridge from economic arbitration to military composition.

The remaining high-value question is not whether production arbitration exists, but **where the arbitration boundary sits and how different production controllers interact when multiple queues and unit demands compete simultaneously**.

## Layer boundary

No `.per` implementation or architecture implementation. Research only.
