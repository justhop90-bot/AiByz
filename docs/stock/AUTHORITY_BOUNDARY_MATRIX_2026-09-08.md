# AEGIS-BYZ — Static Authority Boundary Matrix — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Primary corpus:** restored target-build `AI (HD version).per` plus Promisory source corpus
**Status:** STATIC DECONSTRUCTION / ARCHITECTURAL EVIDENCE
**Runtime qualification:** NOT COMPLETE

## 1. Purpose

This document is the next layer after the exact cross-subsystem rule-path extraction. Its purpose is to separate three things that are historically conflated:

1. who produces a state value;
2. who consumes a state value;
3. who should own the semantic state in AEGIS.

A historical producer is not automatically the AEGIS owner. Shared stock goals are evidence of coupling, not instructions to recreate a global register.

## 2. Authority rule

AEGIS ownership follows semantic responsibility and lifecycle authority, not writer count.

For each state channel, distinguish:

```text
OBSERVATION AUTHORITY
    ↓
INTERPRETATION AUTHORITY
    ↓
POLICY AUTHORITY
    ↓
EXECUTION AUTHORITY
    ↓
VERIFICATION AUTHORITY
```

A subsystem may read a state without owning it. A service may execute a request without owning the policy that generated it.

## 3. Static authority matrix

| Domain | AEGIS owner | Primary owned state | Historical stock intermediaries | Main inputs | Main outputs | Evidence status |
|---|---|---|---|---|---|---|
| World / Observation | World Model / Sensor layer | observed entities, resources, geometry, freshness | raw facts, object searches, player/unit counts | engine state | typed observations | STATIC-QUALIFIED topology |
| Scouting | Scouting OS | scout mission, coverage, contact observations, scouting confidence | position-goal, enemy-goal, scout groups, waypoints | observations, path/threat signals | EnemyObservation / ContactUpdate | STATIC-QUALIFIED topology |
| Threat | Threat OS | threat assessments, strength estimates, urgency | enemy-goal, threat strategic numbers, focus/target channels | scouting + engine observations | ThreatAssessment | STATIC-QUALIFIED topology |
| Strategy | Strategy OS | strategic intent, mode, priorities, posture decisions | strategy-goal, control-goal, position-goal | situation, economy, threat, tech, map | typed demands / policy decisions | STATIC-QUALIFIED topology |
| Economy | Economy OS | resource state, economic demand, worker allocation policy, liquidity | farm-goal, gatherer percentages, escrow interactions | resources, population, strategy, tech, infrastructure | EconomyDemand / AllocationRequest | STATIC-QUALIFIED topology |
| Construction | Construction OS | infrastructure demand admission, placement, builders, pending/completion state | farm-goal, position-goal, placement state, pending objects | economy, strategy, threat, tech | ConstructionRequest / ExecutionState | STATIC-QUALIFIED topology; runtime ABI separately qualified |
| Production | Production OS | train/build/research admission and endpoint selection | unit-goal, production goals, escrow state | strategy, economy, military demand, tech | ProductionRequest / authorization | STATIC-QUALIFIED topology |
| Military | Military OS | composition demand, tactical posture, attack/retreat state, unit control | unit-goal, attack-goal, control-goal, enemy-goal | threat, scouting, strategy, production | MilitaryRequest / execution state | STATIC-QUALIFIED topology |
| Research | Research OS | age/technology demand, affordability, pending research, authorization | research goals, escrow interactions | strategy, economy, military | ResearchRequest / tech state | STATIC-QUALIFIED topology |
| Interaction | Interaction OS | external coordination/input, ally requests, communication-derived intent | control-goal, enemy-goal, interaction flags | player/ally interaction | typed coordination events | STATIC-QUALIFIED topology |
| Logistics / Trade | Logistics OS | dropsite/serviceability, trade demand, transport constraints | resource service state, trade goals | economy + map + water | logistics requests | STATIC-QUALIFIED topology |
| Recovery / Verification | Verification & Recovery | command observation, validity, failure class, retry/reconciliation state | pending-object checks, resets, temporary goals | engine observations + service state | verified completion / recovery | ARCHITECTURE TARGET |

## 4. Historical channel disposition

### `strategy-goal`

**AEGIS disposition:** semantic strategy state, not a universal cross-service register.

Strategy may own strategic intent and transitions. Downstream services consume typed consequences. AEGIS must not let economy, military, or construction directly mutate strategic intent merely because stock rules sometimes co-locate those operations.

### `control-goal`

**AEGIS disposition:** split into typed control/coordination states.

The stock channel is distributed across the flattened controller, `init.per`, and `interaction.per`, with 480 behavioral sites. The existing static graph therefore supports treating it as a historical multiplexed coordination channel rather than one AEGIS integer.

Candidate semantic splits:

```text
StrategicMode
CoordinationMode
InteractionDisposition
ExecutionDisposition
Validity / Generation
```

These remain reconstruction candidates until every writer lifecycle is classified.

### `position-goal`

**AEGIS disposition:** `SpatialPosture` / spatial context.

The static producer surface is concentrated in initialization/topology classification and controller setup, with downstream use by economy, buildings, military, and spatial/search operations. The historical `flank` / `pocket` values strongly support topology/posture semantics rather than a coordinate variable.

### `enemy-goal`

**AEGIS disposition:** split `EnemyIdentity`, `ThreatAssessment`, and `TargetSelection`.

The static graph contains 232 behavioral sites across eight files and 36 writer sites. Because interaction, general, initialization, units, buildings, tactical/military, and threat paths all participate, no single global integer is an acceptable AEGIS semantic owner.

### `farm-goal`

**AEGIS disposition:** split `FoodDemand`, `FarmInfrastructureDemand`, `ConstructionRequest`, and `FarmExecutionState`.

The static graph contains 99 behavioral sites across four files, with a strong producer surface in the flattened controller and a major execution surface in `buildings.per`. This is a feedback interface, not construction-owned state.

## 5. Ownership versus authority

The following distinctions are mandatory:

```text
Strategy owns:       WHY / WHAT SHOULD HAPPEN
Economy owns:        RESOURCE CAPACITY / ECONOMIC DEMAND
Construction owns:   HOW STRUCTURES ARE EXECUTED
Production owns:     HOW TRAIN/BUILD/RESEARCH REQUESTS ARE ADMITTED
Military owns:       TACTICAL EXECUTION / FORCE STATE
Scouting owns:       WHAT HAS BEEN OBSERVED BY SCOUTING
Threat owns:         WHAT THE OBSERVATION MEANS AS RISK
Research owns:       WHAT TECHNOLOGY STATE EXISTS / IS AUTHORIZED
Interaction owns:    EXTERNAL COORDINATION INPUT
Verification owns:  WHETHER REQUESTED STATE ACTUALLY OCCURRED
```

This prevents the historical rule system's multiplexed goals from becoming AEGIS architectural coupling.

## 6. Concrete static evidence edges

The exact cross-subsystem pass establishes several high-value edges:

```text
enemy context + position + food state
        ↓
strategy-goal
        ↓
unit-goal / military demand
```

```text
enemy unit observation
        ↓
archer-threat strategic signal
        ↓
military policy consumers
```

```text
food/resource/logistics state + farm-goal
        ↓
build eligibility
        ↓
build farm
```

```text
strategy / technology / resources
        ↓
infrastructure demand
        ↓
build-forward
```

These prove static coupling. They do not prove interpreter scheduling, same-pass visibility, command completion timing, or persistence.

## 7. State-flow rule for AEGIS

Every cross-service mutation must eventually become one of these forms:

```text
OBSERVATION
    ↓
CONTEXT
    ↓
POLICY / INTENT
    ↓
DEMAND
    ↓
RESERVATION / ARBITRATION
    ↓
SERVICE REQUEST
    ↓
ENGINE COMMAND
    ↓
OBSERVED RESULT
    ↓
VERIFICATION
    ↓
RECOVERY / RECONCILIATION
```

A raw engine command must not silently become a strategic state mutation. Conversely, an observation must not silently become an execution command without an explicit policy/service boundary.

## 8. Generation and freshness

Any state derived from observation or asynchronous execution must carry enough provenance to prevent stale data from winning over newer state.

The architectural minimum is conceptually:

```text
value
source
created/observed generation
evidence/freshness
validity
owner
```

This is especially important for `enemy-goal`, `position-goal`, pending construction state, and military/threat signals.

## 9. Shared-state collision rule

Historical shared goals are not safe allocation targets.

Do not allocate an AEGIS field because a numeric slot appears unused. Before using a goal, strategic number, timer, or scratch register, the state ABI must establish:

```text
symbol
channel type
range/context
owner
readers
writers
lifecycle
collision status
provenance
```

Scratch registers such as `temporary-goal2` and `temporary-goal7` should remain implementation-local temporaries rather than becoming public AEGIS state.

## 10. What this closes

This pass closes the first authority-boundary layer for the major distributed interfaces:

```text
position-goal → spatial context
enemy-goal    → enemy/target coordination
farm-goal     → economic/infrastructure feedback
control-goal  → distributed control/interaction coordination
```

It also establishes a provisional owner for the major operating services without claiming that every historical rule has been semantically classified.

## 11. What remains unresolved

Static evidence does not yet establish:

- exact interpreter scheduling;
- same-pass mutation visibility;
- exact persistence epochs;
- command completion latency;
- whether all conditional branches are active in every target runtime mode;
- the complete semantic partition of `control-goal`;
- the final semantic partition of every shared stock strategic number;
- runtime behavior of AEGIS service contracts.

These remain explicit qualification items.

## 12. Next investigation

The next static layer should join authority boundaries into a **complete state/service dependency matrix**.

For each major state transition, extract:

```text
producer
owner
input evidence
preconditions
state mutation
consumer
service boundary
engine action
verification signal
failure mode
recovery owner
generation/freshness
```

Priority order:

1. Strategy → Economy → Production
2. Scouting → Threat → Military
3. Economy → Construction → Economic reconciliation
4. Research → Economy / Production / Military
5. Military → Economy / Construction
6. Interaction → Strategy / Military
7. Recovery / Verification across all services

Only after this matrix is complete should the AEGIS ownership ABI be frozen for implementation.

## Evidence discipline

**STATIC-QUALIFIED:** source locations, source distributions, visible reads/writes, cross-system coupling, and architectural ownership hypotheses derived from those observations.

**UNQUALIFIED:** interpreter timing, same-pass visibility, exact runtime state persistence, physical command completion, and any behavior not directly established by target-build runtime evidence.
