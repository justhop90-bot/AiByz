# AiBuilder Source Map

**Study target:** `AiBuilder.per` + `AiBuilder/`

## 1. Composition root

### `AiBuilder.per`

Role: **composition root / initialization / ABI declaration / phase configuration**.

The root is responsible for establishing the environment in which the loaded modules operate. The current study treats it as the first file to understand, not merely a launcher.

Known responsibilities:

- phase configuration constants
- `constantsUP` load
- Goal allocation and working-state allocation
- timer allocation
- Strategic Number initialization
- map/position/time/villager observations
- initialization of the building system
- module load order
- post-load customization

### Root load order

```text
AiBuilder\constantsUP
AiBuilder\phaseUpdate
AiBuilder\general
AiBuilder\market
AiBuilder\economy
AiBuilder\technologies
AiBuilder\construction
AiBuilder\militaryUnits
AiBuilder\militaryBehavior
```

This order is part of the execution environment. It must not be changed casually.

## 2. Module map

| Module | Primary role | Main relationship to root |
|---|---|---|
| `constantsUP.per` | UP/engine constants and symbolic definitions | Foundational; loaded first |
| `phaseUpdate.per` | Phase transition and phase policy projection | Major producer of `desired-*` and upgrade policy |
| `general.per` | Explorer policy and general search/group handling | Consumes root state and phase policy |
| `market.per` | Reactive market/resource exchange | Relatively autonomous; native-state driven |
| `economy.per` | Gatherer allocation and civilian production/resource behavior | Consumes phase policy |
| `technologies.per` | Research and escrow management | Consumes upgrade/age policy |
| `construction.per` | Building placement and construction | Consumes building targets and economy state |
| `militaryUnits.per` | Unit production | Consumes unit target goals and feasibility |
| `militaryBehavior.per` | Military grouping, targeting, and attack behavior | Consumes military state and attack policy |

## 3. Policy/data flow

The important architectural flow currently visible in the corpus is:

```text
phase configuration
       ↓
phaseUpdate
       ↓
`desired-*` / `upgrade-*` policy goals
       ↓
┌──────────────┬─────────────┬──────────────┬───────────────┐
│ economy      │ construction│ technologies │ militaryUnits │
└──────────────┴─────────────┴──────────────┴───────────────┘
       ↓
engine-facing requests
       ↓
AoE2 engine
```

`general`, `market`, and `militaryBehavior` provide additional behavior/control paths rather than forming a single simple producer/consumer chain.

## 4. Root Goal working-state block

The current root visibly establishes the following contiguous search-state goals:

```text
point-x             480
point-y             481
point2-x            482
point2-y            483
point3-x            484
point3-y            485
point4-x            486
point4-y            487
point5-x            488
point5-y            489
position-self-x     490
position-self-y     491
gl-game-time        492
spread-units        493
villager-count      494
local-total         495
local-last          496
remote-total        497
remote-last         498
map-size            499
temporary-goal10    501
temporary-goal9     502
temporary-goal8     503
temporary-goal7     504
temporary-goal6     505
temporary-goal5     506
temporary-goal4     507
temporary-goal3     508
temporary-goal2     509
temporary-goal      510
```

**Evidence status:** DIRECT source evidence from the root. The broader ABI semantics of every Goal operation still require systematic tracing.

## 5. Root timers

The current root visibly establishes:

```text
town-size-timer       1
unit-spread-timer      2
cheat-timer             3
land-attack-timer       4
naval-attack-timer      5
```

**Important:** this establishes these timer IDs in the current root. It does **not** establish that arbitrary new timer names are automatically assigned subsequent IDs.

## 6. Study matrix

| Area | Current status | Next action |
|---|---|---|
| Root/load order | DIRECT | Freeze as baseline; trace dependencies |
| Goal allocation | PARTIAL DIRECT | Complete all definitions and cross-module uses |
| Goal span/width | OPEN | Audit every multi-Goal operation |
| Timer allocation | PARTIAL DIRECT | Establish allocation mechanism before adding timers |
| Strategic Numbers | PARTIAL DIRECT | Build writer/reader matrix |
| Phase transitions | DIRECT + runtime unknowns | Trace every transition and repair candidate |
| Desired-count projection | DIRECT | Map each writer to all consumers |
| Feasibility gates | DIRECT | Trace each action family |
| Action completion | OPEN | Identify pending/world-change/confirmation evidence |
| Scratch state | PARTIAL | Complete temporal cross-module read/write analysis |
| Technology logic | STATICALLY QUALIFIED | Preserve existing specific-unit-count semantics unless new evidence appears |
| Enemy observation | PARTIAL | Separate infrastructure observations from army beliefs |
| Difficulty conditionals | OPEN | Resolve compile-time/runtime branch behavior |
| Byzantine extension points | NOT YET CLEARED | Do not code until execution contracts are sufficiently established |

## 7. Evidence rules for this map

A source symbol appearing in a file proves that the corpus contains that symbol in that context. It does not, by itself, prove the full engine semantics of the primitive.

Likewise:

- a Goal name is not automatically a proven free storage slot;
- a timer name is not proof of an available timer ID;
- an action command is not proof of completion;
- an observation is not automatically a belief;
- a building observation is not an army-composition observation;
- a static repair is not automatically a runtime-proven repair.

## 8. Immediate research target

The first serious study pass should build a **complete symbol/ABI matrix** for the root and all nine modules:

```text
symbol
→ definition
→ numeric allocation (if established)
→ readers
→ writers
→ operation width/span
→ module
→ load-order position
→ temporal dependency
→ evidence class
→ unresolved question
```

That matrix becomes the foundation for later vertical-slice qualification.
