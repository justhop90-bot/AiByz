# Stock Cross-System Coupling Matrix — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Purpose:** join the stock subsystem reconstruction into a distributed control-topology model before AEGIS ownership is assigned.

This document is intentionally conservative. A relationship is recorded when source topology and/or machine-derived state topology supports it. It does not claim undocumented scheduler timing or runtime causality.

## System-level coupling

| Producer / source | State or service surface | Consumer | Relationship | Evidence status |
|---|---|---|---|---|
| `init` | operating parameters, spatial/economic doctrine | `gatherers`, `buildings`, `units`, `researches`, `trade` | establishes baseline operating constraints | LOCALLY PROVEN / STATIC-QUALIFIED |
| strategy | `strategy-goal`, policy goals/SNs | economy, production, military, construction | strategic intent changes subsystem priorities | LOCALLY PROVEN / STATIC-QUALIFIED |
| `dawn` | worker allocation percentages / reconciliation | `gatherers` | converts strategic allocation into worker-role state | LOCALLY PROVEN / HISTORICALLY CORROBORATED |
| `gatherers` | worker task state, resource/search state | economy, construction | maintains civilian task lifecycle and infrastructure-linked gathering | LOCALLY PROVEN / STATIC-QUALIFIED |
| `boarhunting` | food acquisition state | `gatherers`, economy | supplies specialized early food demand and fallback/recovery | LOCALLY PROVEN / STATIC-QUALIFIED |
| `buildings` | pending construction, placement, builder state | economy, military, threat | turns structural demand into placement/builder execution | LOCALLY PROVEN / STATIC-QUALIFIED |
| `researches` | age/research goals and pending state | strategy, economy, military | changes capability and resource priorities | LOCALLY PROVEN / STATIC-QUALIFIED |
| `units` | unit production goals / composition state | military, economy | converts strategic/military demand into production | LOCALLY PROVEN / STATIC-QUALIFIED |
| `tsa` | tactical military state | attack, retreat, units, scouting | manages military posture and tactical execution | LOCALLY PROVEN / STATIC-QUALIFIED |
| `scoutcontrol` | exploration, enemy information, waypoints | threats, strategy, military | provides information and tactical discovery | LOCALLY PROVEN / STATIC-QUALIFIED |
| `threats` | threat goals/SNs/facts | buildings, military, economy | converts enemy pressure into distributed response signals | LOCALLY PROVEN / STATIC-QUALIFIED |
| `trade` | trade state | economy, strategy | supplements resource acquisition and strategic decisions | LOCALLY PROVEN / STATIC-QUALIFIED |
| `watercontrol` | naval object state | navy, economy | supports water-specific operating policy | LOCALLY PROVEN / STATIC-QUALIFIED |
| `escrow` | reservation/authorization resource state | production, research, economy | protects competing resource commitments | LOCALLY PROVEN / STATIC-QUALIFIED |
| `general` / `orb` | search/object-management services | most operating systems | provides shared query/filter/object control primitives | LOCALLY PROVEN / STATIC-QUALIFIED |
| `interaction` | communication/cooperation state | strategy, military | cross-player coordination and communication | LOCALLY PROVEN / STATIC-QUALIFIED |

## High-value state channels

The target-build machine topology identifies these as major shared channels. Their numeric identifiers are deliberately not repeated here; numeric assignment must remain in the machine evidence registry until owner and lifecycle are established.

| Channel | Approx. writes | Approx. reads | Dominant role | Coupling significance |
|---|---:|---:|---|---|
| `unit-goal` | 432 | 122 | unit production/composition | Major strategy → production → military bridge |
| `control-goal` | 335 | 142 | control arbitration | Major shared control surface; collision-sensitive |
| `strategy-goal` | 328 | 120 | strategic policy | Primary cognition/policy bridge |
| `ranged-unit-type-goal` | 229 | 21 | ranged composition | Production/military specialization |
| `increase-town-size-goal` | 171 | 10 | infrastructure growth | Economy ↔ construction ↔ strategic capacity |
| `uu-up-goal` | 146 | 4 | unique-unit/civ capability | Civilization policy → production |
| `attack-goal` | 81 | 22 | attack state | Strategy ↔ tactical military |
| `train-civ-goal` | 43 | 0 in top census | civilization production policy | Civ policy → production |
| `farm-goal` | 36 | 6 | food infrastructure | Economy ↔ construction |
| `escrow-purpose-goal` | 24 | 1 | reservation purpose | Economy ↔ production/research |
| `attack-status-goal` | 19 | 0 in top read census | tactical status | Military state transition |
| `under-attack-goal` | 7 | 7 | threat state | Threat ↔ military/economy/construction |

These counts come from the A1 normalized runtime topology. They are operation counts, not semantic weights or priorities.

## Strategic-number coupling

The highest-write stock strategic numbers are particularly important because they form persistent control surfaces across multiple services:

| Strategic number | Writes in A1 topology | Interpretation for reconstruction |
|---|---:|---|
| `sn-wood-gatherer-percentage` | 224 | Worker allocation policy |
| `sn-gold-gatherer-percentage` | 224 | Worker allocation policy |
| `sn-food-gatherer-percentage` | 223 | Worker allocation policy |
| `sn-stone-gatherer-percentage` | 223 | Worker allocation policy |
| `sn-resource-control` | 91 | Resource/economic arbitration |
| `sn-maximum-town-size` | 61 | Infrastructure/town-size policy |
| `sn-allow-adjacent-dropsites` | 38 | Dropsite placement policy |
| `sn-maximum-wood-drop-distance` | 35 | Economic service-distance constraint |
| `sn-focus-player-number` | 35 | Information/threat target identity |
| `sn-camp-max-distance` | 28 | Economic infrastructure constraint |
| `sn-maximum-gold-drop-distance` | 27 | Economic service-distance constraint |
| `sn-maximum-food-drop-distance` | 26 | Economic service-distance constraint |
| `sn-target-player-number` | 26 | Military/information identity |
| `sn-number-explore-groups` | 24 | Scouting allocation |
| `sn-current-age` | 21 | Global progression state |
| `sn-military-level` | 13 | Military posture/quality policy |

The extreme concentration of worker-percentage writes is evidence that economic allocation is a persistent control loop, not a one-time setup operation.

## Cross-system causal chains established statically

### Economy → construction → workers

```text
resource demand
    ↓
worker/economic policy
    ↓
dropsite / infrastructure demand
    ↓
construction placement
    ↓
builder assignment
    ↓
completed infrastructure
    ↓
worker task eligibility / service distance
```

This chain is supported by the separate `gatherers`, `buildings`, `init`, and `dawn` source systems and their shared state surfaces. Exact temporal ordering remains a runtime question.

### Threat → construction

```text
enemy pressure / threat state
    ↓
strategic construction demand
    ↓
placement eligibility
    ↓
build-line / placement action
    ↓
builder assignment
```

The stock tower logic is a direct source-level example: threat/cavalry state changes builder allocation for defensive construction.

### Strategy → production

```text
strategy-goal
    ↓
unit/composition goals
    ↓
production authorization
    ↓
train / up-train
    ↓
pending / completion state
```

The A1 topology records `strategy-goal` as one of the highest-write/read shared goals and `research`/`up-research` plus `train`/`can-train` as dominant engine-facing command families.

### Information → threat → military

```text
scouting / enemy facts
    ↓
threat state
    ↓
attack / retreat / composition decisions
    ↓
unit production and tactical control
```

The source topology supports this distributed relationship, but does not prove a universal fixed latency from observation to tactical action.

### Reservation → authorization

```text
strategic demand
    ↓
escrow purpose
    ↓
resource reservation
    ↓
can-build / can-train / can-research
    ↓
physical command
```

This is why AEGIS must model demand, reservation, authorization, command issuance, and confirmation as separate states.

## Architectural consequence for AEGIS

The historical stock architecture is best understood as a **distributed operating system**, not as a flat list of scripts.

AEGIS therefore should not reproduce stock module boundaries mechanically. Instead, it should recover the invariant service contracts:

```text
Cognition
  ↓
Demand
  ↓
Arbitration / reservation
  ↓
Service selection
  ↓
Authorization
  ↓
Engine command
  ↓
Observation
  ↓
Verification
  ↓
Recovery
```

The stock modules become evidence for the implementation of those contracts.

## Unknowns intentionally preserved

The matrix does **not** claim:

- exact same-pass visibility of state mutations;
- exact rule scheduler ordering beyond source/jump topology;
- universal command completion latency;
- universal pending-object transition timing;
- universal worker reassignment latency;
- exact causality where multiple distributed rules can independently write the same channel;
- that a high write count implies priority;
- that historical module names map one-to-one to final AEGIS services.

Those remain separate qualification claims.

## Next deconstruction join

The next static artifact should move from module-level coupling to **symbol-level ownership**:

```text
symbol
 → declaring source
 → writer modules
 → reader modules
 → resetter modules
 → activation predicates
 → object/search state
 → lifecycle transitions
 → collision set
 → AEGIS owner candidate
 → evidence status
```

That is the final static join required before beginning the formal AEGIS ABI ownership allocation.
