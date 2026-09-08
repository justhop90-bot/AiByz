# AEGIS Stock Subsystem Reconstruction Map — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Machine:** Weebo  
**Authoritative source:** untouched stock installation under `resources\\_common\\ai`  
**Purpose:** Convert the accumulated stock AI/Promisory archaeology into an ownership and reconstruction map for the final AEGIS civilization operating system.

## 1. Executive result

This pass establishes the current reconstruction boundary for the complete stock AI system.

The key correction is that the stock system has **three different layers of provenance** that must not be conflated:

1. **AI (HD version).per** is the large flattened behavioral controller. It contains the operational civilization logic that actually forms the bulk of the stock AI program.
2. **Promisory source modules** are the decomposed source corpus from which many mechanisms are organized and maintained. They are invaluable reconstruction material, but most are not independently loaded by the flattened AI at runtime.
3. **Promisory runtime substrate** is the small set of files explicitly loaded by the stock entry point, chiefly `defaultConstants`, `finalingConstants`, and conditionally `finaling`, plus nested imports when individual Promisory modules are directly loaded.

Therefore the final AEGIS reconstruction must recover behavior from the **flattened controller and the source substrate together**, while preserving only the necessary engine-facing semantics under AEGIS ownership.

This is not a choice between AI(HD) and Promisory. Both are required evidence layers.

---

## 2. Stock runtime import closure

Direct inspection of the target-build `AI (HD version).per` shows:

```per
(load "Promisory\\defaultConstants")
(load "Promisory\\finalingConstants")
...
(load "Promisory\\finaling")
```

The finaling load is conditional within the source preprocessor structure; it is not safe to model the entire file as an unconditional import without preserving the surrounding conditional compilation context.

Important nested imports found in the Promisory corpus include:

```text
Promisory/buildings.per
    -> Promisory/extremebuildings2

Promisory/gatherers.per
    -> Promisory/ugp
```

The visible imports in `init.per` and `merge.per` are commented out in the current target corpus. They are provenance evidence, not active dependencies.

The Promisory directory also contains experimental, test, compatibility, and placeholder files that are not automatically part of the active flattened runtime graph.

### Runtime-closure rule

A file is not considered a runtime dependency merely because it exists under `Promisory` or is referenced by historical source comments. Active dependency requires an active load path under the target source/preprocessor conditions.

---

## 3. Complete Promisory corpus partition

The target Promisory directory contains the following source families.

### Core operational source modules

| File | Primary responsibility | Reconstruction status |
|---|---|---|
| `units.per` | unit production policy and execution | major forensic coverage; reconstruction required |
| `buildings.per` | construction, placement, builders, foundations | undercovered; P0 reconstruction target |
| `gatherers.per` | worker allocation, source selection, tasking | strong P0 forensic coverage |
| `dawn.per` | percentage-to-integer worker allocation | strong structural evidence |
| `escrow.per` | resource escrow and purchase arbitration | strong P0 forensic coverage |
| `researches.per` | age and technology scheduling | partially inspected; P0/P1 reconstruction target |
| `tsa.per` | military task/scheduling/targeting/execution | undercovered; major reconstruction target |
| `scoutcontrol.per` | scouting, discovery, targeting and scout micro | undercovered; major reconstruction target |
| `threats.per` | threat detection/state/response | forensic coverage exists; full ownership map needed |
| `trade.per` | market/trade economy and commodity conversion | undercovered |
| `watercontrol.per` | fishing/water economy | undercovered |
| `boarhunting.per` | boar lifecycle and food acquisition | identified; full ownership map needed |
| `interaction.per` | taunts, interaction, commands, special hooks | undercovered |
| `general.per` | broad maintenance and support logic | undercovered |
| `init.per` | bootstrap, strategic numbers, operating defaults | partially inspected; major dependency source |
| `orb.per` | operational/support behavior | undercovered |
| `finaling.per` | final runtime setup, reset/maintenance, resignation/support | directly inspected; important runtime substrate |

### Constant/ABI source modules

| File | Responsibility | Reconstruction status |
|---|---|---|
| `defaultConstants.per` | FactId, classes, foundations, research/timer states | strong ABI evidence |
| `finalingConstants.per` | finaling goals, difficulty values, object-data constants and special IDs | strong ABI evidence |
| `const.per` | stock constant namespace | strong source reference |
| `customConstants.per` | game/civ/custom constants | strong source reference; ownership partition required |

### Specialized / compatibility / experimental modules

| File | Observed purpose | Runtime interpretation |
|---|---|---|
| `extremebuildings2.per` | alternate/specialized building behavior | loaded by `buildings.per`; retain behavior only after qualification |
| `ugp.per` | supporting gatherer behavior | loaded by `gatherers.per`; reconstruct with worker service |
| `resign.per` | resignation/failure/late-game exit behavior | source behavior; likely flattened/conditionally represented in AI(HD) |
| `event.per` | one-shot disabled rule | no strategic runtime role demonstrated |
| `events.per` | special chat/event hook | auxiliary/event behavior |
| `merge.per` | historical merge loader | currently commented; provenance only |
| `merge1b.per` | experimental civ/Chronicles constants | not active unless conditional path proves otherwise |
| `merge2.per` | empty placeholder | no behavior |
| `merge2b.per` | placeholder | no behavior |
| `merge3.per` | empty placeholder | no behavior |
| `merge3b.per` | empty placeholder | no behavior |
| `merge4.per` | player-count/taunt cooperative targeting | compatibility/support source; ownership required |
| `paphosConstants.per` | experimental/new civ constants and large custom ABI namespace | not established as active stock runtime dependency |

The existence of specialized files is therefore not equivalent to their inclusion in the normal Byzantine runtime.

---

## 4. Flattened AI(HD) reconstruction map

The flattened `AI (HD version).per` remains the primary behavioral body. Its major regions should be reconstructed into AEGIS services rather than copied as one monolithic artifact.

| Flattened region | Stock responsibility | AEGIS owner |
|---|---|---|
| constants / loads | namespace/bootstrap | AEGIS ABI + bootstrap |
| initialization/setup | initial state and policy defaults | Civilization State + Bootstrap |
| navy initialization | initial naval state | Water OS + Military OS |
| superiority | military/strategic comparison | Situation + Military OS |
| scouts | discovery/targeting | Information OS |
| strategy | strategic policy selection | AEGIS Cognition |
| civ-specific policy | Byzantine and generic civ policy branches | Byzantine Policy layer |
| boar hunting | dedicated food lifecycle | Food Controller |
| resource management / age-up | economic control and age transitions | Economic Scheduler + Technology OS |
| research | technology execution | Technology OS |
| siege | siege production/use | Military OS |
| trade | market/trade | Trade OS |
| villagers | civilian production and worker lifecycle | Civilian OS |
| buildings | construction and placement | Construction OS |
| units | unit production | Production/Military OS |
| navy | naval production/control | Water OS + Military OS |
| gatherers | worker tasking | Worker Tasking Service |
| attack | attack planning/execution | Military OS |
| retreat | defensive/recovery movement | Military OS + Recovery |
| navy management | naval task control | Water/Military OS |
| cooperation/taunts | external interaction | Interaction/Cooperation OS |
| town-size | expansion/base scale policy | Construction + Cognition |
| miscellaneous/late game | resignation, maintenance, support | Verification/Recovery + Late Game OS |

These are behavioral ownership assignments, not claims that each flattened region maps one-to-one to one source file. Many behaviors cross region boundaries.

---

## 5. Critical cross-layer relationships

### 5.1 Civilization production

The verified civilian production chain is:

```text
strategy / economy
    ↓
trainvillager authorization
    ↓
can-train with escrow state
    ↓
up-train
    ↓
pending production
    ↓
population/civilian accounting
    ↓
worker allocation
```

AEGIS must preserve these distinctions.

### 5.2 Economy

The verified economic chain is:

```text
strategic demand
    ↓
resource commitment
    ↓
escrow / competing claims
    ↓
integer worker targets
    ↓
source + infrastructure selection
    ↓
worker tasking
    ↓
measured income
    ↓
state reconciliation
```

### 5.3 Construction

Stock construction couples placement and worker state:

```text
build need
    ↓
can-build
    ↓
placement/search
    ↓
foundation
    ↓
builder assignment
    ↓
progress
    ↓
completion/failure
    ↓
resource/infrastructure state
```

`buildings.per` must therefore be reconstructed as an operating system, not reduced to a build queue.

### 5.4 Information

Scouting is persistent state, not merely an initial move:

```text
player targeting
    ↓
scout task
    ↓
waypoint / point selection
    ↓
movement
    ↓
observation
    ↓
enemy/resource information
    ↓
retarget / recovery
```

### 5.5 Military

The TSA evidence demonstrates multiple interacting state machines:

```text
military demand
    ↓
production
    ↓
army population
    ↓
attack/defense group state
    ↓
target evaluation
    ↓
attack / micro / retreat
    ↓
reinforcement
```

Attack-system selection itself can switch between old/new micro systems based on map, population, unit composition, turn-time, walls, siege and naval conditions. This proves that “military strategy” is not one scalar policy.

### 5.6 Technology

Research is integrated with civilian/economic state. The inspected age-up rules consider food, villager count, pending production, strategy, enemy age and other conditions. Technology must therefore consume the same reservation/authorization plane as economy and military production.

### 5.7 Water

`watercontrol.per` demonstrates specialized spatial logistics: fishing ships are compared against shore/deep fish by distance and carrying state, and random exploration can be used when suitable deep fish are not known. This is a separate operating discipline, not a trivial gatherer variant.

### 5.8 Trade

`trade.per` can release escrow, sell excess resources, and buy resources conditionally. This means market conversion is itself part of resource arbitration and must not be bolted on after the economic scheduler.

### 5.9 Interaction/cooperation

`interaction.per`, `merge4.per`, and parts of `finaling.per` contain taunt-driven control, cooperative targeting, chat/event hooks and other external interaction. These should be isolated from core strategic cognition so interaction commands cannot accidentally become hidden strategic authority.

### 5.10 Resignation/recovery

`resign.per` and the tail of the flattened AI show that “game termination” is itself a state machine with timers, population/military thresholds, ally/enemy conditions, victory conditions and cleanup behavior. It belongs under a late-game/verification/recovery service, not as an arbitrary final rule.

---

## 6. Important ABI discovery from the constant corpus

`defaultConstants.per` directly defines the base FactId namespace:

```text
0  game-time
1  population-cap
2  population-headroom
3  housing-headroom
4  idle-farm-count
5  food-amount
6  wood-amount
7  stone-amount
8  gold-amount
9  escrow-amount
10 commodity-buying-price
11 commodity-selling-price
12 dropsite-min-distance
13 soldier-count
14 attack-soldier-count
15 defend-soldier-count
16 warboat-count
17 attack-warboat-count
18 defend-warboat-count
19 current-age
20 current-score
21 civilization
22 player-number
23 player-in-game
24 unit-count
25 unit-type-count
26 unit-type-count-total
27 building-count
28 building-type-count
29 building-type-count-total
30 population
31 military-population
32 civilian-population
33 random-number
34 resource-amount
35 player-distance
36 allied-goal
37 allied-sn
38 resource-percent
39 enemy-buildings-in-town
40 enemy-units-in-town
41 enemy-villagers-in-town
42 players-in-game
43 defender-count
44 building-type-in-town
45 unit-type-in-town
46 villager-type-in-town
47 gaia-type-count
48 gaia-type-count-total
49 cc-gaia-type-count
50 current-age-time
51 timer-status
52 players-tribute
53 players-tribute-memory
54 treaty-time
55 battle-royale-time
```

This is a genuine ABI namespace and should remain in the AEGIS ABI ledger. It is not merely “constants copied from Promisory.”

The same file defines the stock class namespace, foundation IDs, research-state IDs and timer-state IDs. These are engine-facing semantic contracts and should be rehosted under AEGIS with provenance retained.

---

## 7. Object-data ABI

`finalingConstants.per` exposes an extensive object-data namespace, including:

```text
object-data-id
object-data-type
object-data-class
object-data-action
object-data-order
object-data-target
object-data-point-x/y
object-data-hitpoints/maxhp
object-data-range/speed
object-data-dropsite/resource/carry
object-data-garrisoned/garrison-count
object-data-status
object-data-player
object-data-attack-stance
object-data-action-time
object-data-target-id
object-data-formation-id
object-data-patrolling
object-data-locked
object-data-garrison-id
object-data-train-count
object-data-tasks-count
object-data-attacker-count/id
object-data-under-attack
object-data-attack-timer
object-data-point-z
object-data-precise-x/y/z
object-data-researching
object-data-tile-position/inverse
object-data-distance
object-data-precise-distance
object-data-full-distance
object-data-map-zone-id
object-data-on-mainland
object-data-idling
object-data-move-x/y
object-data-precise-move-x/y
object-data-reload-time
object-data-next-attack
object-data-train-site/time
object-data-blast-radius/level
object-data-progress-type/value
object-data-min-range
object-data-target-time
object-data-heresy/faith/redemption/atonement/theocracy/spies
object-data-ballistics
object-data-gather-type
object-data-language-id
object-data-group-flag
object-data-hero-flags/hero
object-data-auto-heal
object-data-no-convert
object-data-frame-delay
object-data-attack-count
object-data-to-precise
object-data-base-type
object-data-upgrade-type
object-data-ownership
object-data-capture-flag
```

This namespace materially expands the AEGIS world model available for worker, construction, scouting and military reconstruction. It should be treated as an ABI capability inventory, not as an implementation suggestion that every field must be sampled continuously.

---

## 8. Finaling is not cosmetic cleanup

Direct inspection of `finaling.per` shows that finaling performs real runtime work:

- initializes exploration-group count;
- configures idle-unit limits;
- sets enemy-sighted response parameters;
- initializes wall targeting;
- sets escrow percentages;
- retrieves population cap;
- clears transient attack/capture state;
- initializes naval filtering;
- performs direct production rules;
- uses jump control;
- runs reset/maintenance timers;
- maintains rule-pass timing state;
- computes AI turn-time estimates;
- controls resignation and post-resignation behavior;
- resets selected units and strategic modifiers.

Therefore finaling belongs in the reconstruction map as a **runtime supervisor/finalization service**, not merely as a constants file.

AEGIS should reproduce required finaling semantics through explicit services and verification rather than blindly importing `finaling.per`.

---

## 9. Experimental source must be separated from production source

The Promisory directory contains files such as `merge1b.per` and `paphosConstants.per` containing constants for additional civilizations/Chronicles-era content. They introduce IDs and namespaces outside the ordinary Byzantine stock problem.

These files are useful because they reveal how the authors handled extensibility, conditional constants and large ABI namespaces. They must not automatically be incorporated into the Byzantine runtime.

Likewise, empty/placeholder merge files should not consume implementation effort merely because they exist.

This distinction prevents a common reconstruction error: mistaking **source-corpus completeness** for **runtime dependency completeness**.

---

## 10. Stock-to-AEGIS disposition matrix

| Stock subsystem | Disposition | Reason |
|---|---|---|
| Fact/class/foundation ABI | REIMPLEMENT/REHOST | required engine contract |
| Object-data ABI | REIMPLEMENT/REHOST | required state observation capability |
| Timer-state ABI | REIMPLEMENT/REHOST | required scheduling semantics |
| Villager production | REIMPLEMENT | AEGIS must own production lifecycle |
| Worker allocation | REIMPLEMENT | AEGIS scheduler must own policy-to-count conversion |
| Worker tasking | REIMPLEMENT | AEGIS needs explicit service state and recovery |
| Resource/source selection | REIMPLEMENT | preserve spatial/operational behavior with AEGIS ownership |
| Escrow | REIMPLEMENT/ADAPT | engine escrow semantics are execution-relevant |
| Construction | REIMPLEMENT | persistent queue/state machine required |
| Scouting | REIMPLEMENT | persistent information service required |
| Threat response | REIMPLEMENT/ADAPT | preserve distributed threat semantics |
| Military/TSA | REIMPLEMENT | cognition must not inherit opaque monolithic military authority |
| Research/age | REIMPLEMENT | shared economic authorization required |
| Trade | REIMPLEMENT | must participate in resource arbitration |
| Water | REIMPLEMENT | specialized spatial economy |
| Boar/hunt | ADAPT/REIMPLEMENT | source-specific lifecycle should survive under food controller |
| Interaction/taunts | ADAPT | preserve supported external controls, isolate ownership |
| Resignation | REIMPLEMENT | recovery/late-game state machine |
| Finaling | REIMPLEMENT | final supervisor semantics should be explicit |
| Historical merge files | PRESERVE AS REFERENCE | not active without proof |
| Experimental civ constants | PRESERVE AS REFERENCE | not Byzantine runtime requirements |
| Placeholder files | IGNORE unless dependency discovered | no behavior established |

---

## 11. AEGIS service graph generated by this pass

```text
AEGIS Cognition
   │
   ├── Objective / Commitment
   │
   └── typed service requests
           │
           ▼
   Demand + Arbitration
      │    │    │
      │    │    └── Technology OS
      │    ├─────── Military OS
      │    └─────── Construction OS
      ▼
   Economic Scheduler / Escrow
      │
      ├── Worker Allocation
      ├── Resource Opportunity
      ├── Trade Conversion
      └── Food Portfolio
      │
      ▼
   Civilization Operations
      ├── Villager Production
      ├── Housing
      ├── Worker Tasking
      ├── Hunting/Farms/Fishing
      └── Recovery
      │
      ├────────────── Information OS
      │                  └── Scouts / Discovery / Targeting
      │
      ├────────────── Military OS
      │                  └── Production / Groups / Targeting / Retreat / Micro
      │
      └────────────── Construction OS
                         └── Placement / Builders / Foundations / Retry
      │
      ▼
   AEGIS ABI
      │
      ▼
   AoE2DE Engine
      │
      ▼
   Observation / Reconciliation
      │
      └────────────── Verification / Recovery ────► Cognition
```

---

## 12. Reconstruction order

The evidence supports the following order for the actual final bot:

### Stage 1 — ABI and state foundation

- FactId/class/foundation namespace
- object-data namespace
- timer/research states
- search semantics
- generation/validity envelope
- civilization state

### Stage 2 — Civilization survival

- villager production
- housing
- worker census/accounting
- worker allocation
- worker tasking
- food portfolio
- source/infrastructure serviceability
- interruption/recovery

### Stage 3 — Construction

- build requests
- placement
- builder allocation
- foundations
- progress
- completion/failure
- retry/replan

### Stage 4 — Information

- scout lifecycle
- exploration
- enemy identification
- information freshness
- target updates
- scout recovery

### Stage 5 — Military

- unit production
- military state
- army formation
- tasking
- target evaluation
- attack/defend/retreat
- reinforcement
- micro policy

### Stage 6 — Technology and market

- age-up
- research queue
- technology reservation
- trade conversion
- water economy

### Stage 7 — Byzantine cognition integration

Only after the substrate can reliably maintain civilization state should Byzantine strategy become the broad policy authority.

---

## 13. Evidence boundary

This pass establishes the **static reconstruction boundary**.

### Established

- The flattened AI is the primary behavioral body.
- Promisory is simultaneously source corpus and runtime substrate.
- The active runtime import graph is much smaller than the complete Promisory source directory.
- `defaultConstants` and `finalingConstants` are real ABI namespaces.
- `finaling` contains real runtime supervisor/maintenance behavior.
- `buildings -> extremebuildings2` and `gatherers -> ugp` are nested source dependencies when those modules are loaded.
- Merge/experimental modules cannot be promoted to active dependencies solely from existence or comments.
- Worker/economic, construction, scouting, military, research, trade, water and interaction systems all require explicit AEGIS ownership.
- The final architecture must incorporate the complete stock behavioral contract, not simply copy the 36k-line flattened file.

### Not established by this pass

- Exact one-to-one source correspondence for every flattened AI region.
- Complete goal writer/reader closure across all 36k lines.
- Complete strategic-number writer/reader closure.
- Complete action/order lifecycle graph.
- Exact conditional-preprocessor expansion for every possible difficulty/game/civ combination.
- Exact target-build runtime semantics for every ABI primitive.
- Runtime equivalence of any AEGIS replacement.

Those require targeted forensic passes or controlled runtime experiments.

---

## 14. Engineering decision

The project is now past the point where another generic “study the AI” pass is useful.

The correct next step is to take each remaining high-risk operating system and perform a **source-level reconstruction pass with explicit state/goal/SN/action ownership**.

Priority:

1. Construction OS
2. Military/TSA OS
3. Information/Scouting OS
4. Technology/Age OS
5. Interaction/Cooperation OS
6. Trade/Water/Late-game OS

Civilian/economic archaeology remains active only where one of these systems exposes a cross-layer dependency.

**Status: STATIC STOCK RECONSTRUCTION MAP COMPLETE FOR CURRENT EVIDENCE.**
**Runtime qualification remains open.**
