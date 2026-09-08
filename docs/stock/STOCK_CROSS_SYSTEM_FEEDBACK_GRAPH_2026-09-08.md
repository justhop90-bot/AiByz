# Stock Cross-System Feedback Graph — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Corpus:** restored target-build `AI (HD version).per` + Promisory source corpus
**Status:** STATIC DECONSTRUCTION — NOT runtime qualified

## Executive result

The four distributed interfaces are not independent. Their static relationships form a feedback network connecting strategic selection, control state, spatial posture, enemy context, infrastructure demand, production, and military execution.

The key result is that the historical controller is better modeled as a **distributed feedback control system** than as a linear priority list.

## Consolidated graph

```text
                         STRATEGY
                            │
                            ▼
                       strategy-goal
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
             control-goal        unit-goal
                  │                   │
          ┌───────┴──────┐            ▼
          ▼              ▼       production policy
     position-goal    enemy-goal        │
          │              │              ▼
          │        threat/target     units/state
          │              │              │
          └──────┬───────┘              ▼
                 ▼                  attack-goal
           spatial + threat              │
                 │                      ▼
                 │                  military
                 │                      │
                 └──────────┬───────────┘
                            ▼
                       engine state
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
          economy      construction    observation
             │              │              │
             ▼              ▼              ▼
         farm-goal ◄──── infrastructure ──┘
             │
             ▼
       economic capacity
             │
             └──────────────► strategy
```

The arrows are static dependency hypotheses derived from source coupling. They do not assert same-pass execution.

## Feedback cycle 1 — strategic posture

```text
strategy-goal
   ↓
control-goal
   ↓
position-goal
   ↓
spatial / execution posture
   ↓
observed game state
   ↓
strategy-goal
```

**Architectural meaning:** strategic posture is not just a label. It changes the control and spatial context used by downstream services, which then changes the observed state available to future strategic decisions.

## Feedback cycle 2 — enemy response

```text
enemy observation
   ↓
enemy-goal
   ↓
threat / target interpretation
   ↓
unit-goal / attack-goal / construction response
   ↓
engine state
   ↓
new enemy observation
```

**Architectural meaning:** enemy context should be treated as a continuously reconciled observation product, not a permanent target identifier.

## Feedback cycle 3 — economic infrastructure

```text
resource / population pressure
   ↓
farm-goal
   ↓
construction service
   ↓
farm infrastructure
   ↓
economic capacity
   ↓
resource / population pressure
```

This is a genuine demand-capacity feedback loop in the source architecture.

## Feedback cycle 4 — military composition

```text
strategy-goal
   ↓
unit-goal
   ↓
ranged-unit-type-goal / composition policy
   ↓
production
   ↓
military state
   ↓
enemy/threat observation
   ↓
strategy / unit-goal
```

This is why production cannot be modeled independently of strategic cognition and enemy observation.

## Multiplexed-state hazards

The historical controller repeatedly uses compact numeric channels as intermediaries between different concerns. The most important architectural hazards are:

1. `control-goal` multiplexing control/coordination concepts;
2. `position-goal` carrying topology/spatial posture;
3. `enemy-goal` carrying enemy/target context;
4. `farm-goal` carrying infrastructure demand;
5. `temporary-goal*` acting as shared scratch state.

AEGIS must split these into typed, owned state rather than reproduce their historical multiplexing.

## Authority boundaries

The reconstruction implies five distinct authorities:

```text
Cognition
  → decides intent

Arbitration
  → resolves competing intent

Service
  → selects executable operation

ABI / Engine
  → determines legal physical effect

Verification / Recovery
  → determines whether the effect actually occurred
```

A state variable crossing those boundaries is an interface, not automatically the property of whichever module happens to write it most often.

## Critical non-conclusions

Static coupling does not prove:

- execution order;
- rule-pass boundaries;
- same-pass mutation visibility;
- exact jump scheduling;
- command completion latency;
- pending-object timing;
- engine-side rollback behavior.

Those remain target-build runtime qualification items.

## AEGIS architecture consequence

The final AEGIS control plane should therefore be organized around typed service contracts:

```text
StrategicIntent
Demand
Reservation
SpatialContext
EnemyContext
ExecutionRequest
ObservedResult
FailureDisposition
```

rather than direct reuse of stock goal names.

## Deconstruction milestone

The project has now completed the first distributed-interface set:

```text
position-goal → reconstructed
enemy-goal    → reconstructed
farm-goal     → reconstructed
control-goal  → reconstructed
```

The next static layer is **subsystem-to-subsystem edge enumeration**. Instead of starting with another goal, extract the concrete service transitions connecting:

- strategy ↔ economy;
- strategy ↔ military;
- economy ↔ construction;
- scouting ↔ military;
- threat ↔ construction;
- research ↔ economy/military;
- production ↔ military;
- execution ↔ observation/recovery.

This is the boundary immediately before freezing AEGIS subsystem ownership.

No runtime qualification is implied by this document.
