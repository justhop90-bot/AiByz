# AEGIS Master Engineering Guide

**Project:** AEGIS-BYZ / next-generation Byzantine AI for Age of Empires II: Definitive Edition  
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Date established:** 2026-09-07  
**Status:** Canonical master plan; forensic extraction is active  
**Runtime rule:** AEGIS runtime is self-owned. Stock Promisory is laboratory/reference material only and must never be a runtime dependency.

---

## 0. Mission

AEGIS is not a larger `.per` strategy script. It is intended to become a hierarchical control system capable of turning uncertain game observations into reliable civilization behavior.

The central engineering question is not:

> What strategy should the bot use?

It is:

> What complete set of state, control, execution, feedback, recovery, and engine-ABI mechanisms are required for a strategic decision to reliably become game state?

Every layer must therefore be investigated before it is designed, and designed before it is implemented.

The project rule is deliberately adversarial:

**Assume that a fundamental subsystem is still missing until the stock corpus, engine ABI, runtime behavior, and cross-layer interactions provide evidence that it is not.**

---

## 1. Canonical architecture

AEGIS is organized as a vertical stack:

```text
L0  Engine ABI / Interpreter Contract
L1  World + Spatial Model
L2  Civilization State
L3  Economic Scheduler + Escrow
L4  Civilian Operations
L5  Construction Operating System
L6  Information / Scouting Operating System
L7  Military Operating System
L8  Technology / Age Operating System
L9  Strategic Cognition
L10 Verification / Recovery Supervisor
L11 Cross-layer adaptation, learning, telemetry, and qualification
```

The stack is hierarchical but not isolated. Every layer must publish explicit state and consume explicit contracts.

The fundamental separation is:

```text
Cognition decides WHAT should happen.
Scheduler decides WHAT resources/state are required.
Operating systems decide HOW to make it happen.
Engine ABI determines WHICH commands are legal.
Verification determines WHETHER it actually happened.
Recovery determines WHAT to do when it did not.
```

---

## 2. Evidence hierarchy

Evidence is ranked as follows:

1. **Target-build runtime behavior** — strongest evidence.
2. **Target-build stock AI source on the user's machine** — authoritative implementation reference.
3. **Direct engine ABI qualification** using controlled experiments.
4. **Existing AEGIS runtime behavior and static qualification.**
5. **Official AoE2DE update documentation.**
6. **Community documentation/reverse engineering.**
7. **Inference from naming or apparent design intent.**

Inference must never be promoted to fact merely because it is plausible.

Every important discovery receives one of these states:

- `OBSERVED` — directly present in authoritative source/runtime evidence.
- `CORRELATED` — supported by multiple observations.
- `INFERRED` — technically plausible but not directly established.
- `IMPLEMENTED` — represented in AEGIS code.
- `STATIC-QUALIFIED` — passes source/ABI/static checks.
- `RUNTIME-QUALIFIED` — demonstrated in the target interpreter.
- `STRESS-QUALIFIED` — survives adversarial scenarios.

---

## 3. Authoritative local corpus

The untouched stock AI reference is:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

The major stock subsystems already identified include:

| File | Approx. local size | Role under investigation |
|---|---:|---|
| `units.per` | 13,786 lines | unit production and production policy |
| `buildings.per` | 13,117 | construction, placement, builders, foundations |
| `tsa.per` | 12,769 | military task/scheduling/targeting/execution substrate |
| `init.per` | 10,725 | initialization and persistent operating state |
| `customConstants.per` | 8,064 | engine/game constants |
| `general.per` | 7,605 | broad operational state and maintenance |
| `researches.per` | 7,023 | technology and age scheduling |
| `const.per` | 5,965 | stock constants |
| `gatherers.per` | 5,325 | economic policy and gatherer allocation |
| `orb.per` | 4,515 | operational/resource behavior |
| `interaction.per` | 4,501 | interaction state and commands |
| `escrow.per` | 3,386 | resource reservation/competing claims |
| `threats.per` | 1,822 | threat state and response |
| `scoutcontrol.per` | 1,342 | scouting, target/path/task control |
| `trade.per` | 1,306 | trade economy |
| `boarhunting.per` | 1,236 | dedicated hunting lifecycle |
| `watercontrol.per` | 1,055 | fishing/water economy |
| `AI (HD version).per` | 36,141 | flattened stock controller/reference |

These counts are a snapshot of the target installation and are evidence of subsystem scale, not a specification of behavior by themselves.

---

# PART I — THE LAYERS WE MUST PROVE

## L0 — Engine ABI and interpreter semantics

### Objective

Establish exactly what the target interpreter accepts, what operands mean, what ranges are legal, how searches behave, how state persists, and how rule ordering affects commands.

### Required forensic domains

- fact identifiers;
- unit IDs, unit-line IDs, classes and their distinct semantics;
- goal IDs and legal ranges by primitive;
- strategic-number IDs and writable/readable semantics;
- `up-*` facts and actions;
- search initialization/reset semantics;
- local versus remote searches;
- point/object transfer semantics;
- placement primitives;
- build/train commands;
- pending-object semantics;
- research-status semantics;
- timers;
- rule firing/order constraints;
- one-command-per-pass constraints;
- goal mutation timing;
- engine version-specific quirks.

### Known critical ABI lesson

`up-get-focus-fact` with `unit-type-count` can operate on concrete unit IDs and supported unit-line IDs. A unit class is not interchangeable with a unit-line. This distinction previously produced an `Invalid Identifier` investigation and must remain explicit in the ABI ledger.

### Exit gate

No subsystem may claim ABI correctness from syntax alone. Every nontrivial command/operand combination requires an authoritative example or target-build runtime evidence.

---

## L1 — World and spatial model

### Objective

Turn raw observations into a world model that contains not merely quantities but opportunities, locations, accessibility, relationships, and uncertainty.

### Required state

- entities and identity;
- unit/building classes;
- positions;
- terrain;
- explored/visible state;
- resource nodes;
- resource quantity;
- dropsites;
- path distance;
- accessibility/pathability;
- base/settlement regions;
- enemy regions;
- threat zones;
- military groups;
- construction sites;
- information freshness.

### Target abstraction

```text
ResourceOpportunity = {
  type,
  amount,
  position,
  nearestDropsite,
  pathDistance,
  expectedRate,
  setupCost,
  risk,
  accessibility,
  expiry
}
```

### Missing question

The existing aggregate resource sensors are insufficient for high-quality economic control. We must determine exactly which spatial facts the engine exposes and which must be approximated through searches and persistent state.

---

## L2 — Civilization state

### Objective

Maintain a trustworthy internal representation of the civilization before asking cognition to optimize it.

### Required state domains

- total population;
- population cap;
- population headroom;
- villager count;
- pending villagers;
- idle villagers;
- worker-role counts;
- buildings;
- foundations;
- production queues;
- stockpiles;
- income estimates;
- age;
- technology state;
- military counts;
- resource infrastructure;
- active service requests;
- reservations/escrow;
- failures and outstanding recovery work.

### Core principle

A civilization state variable needs ownership. Two modules must never independently believe they own the same state.

---

# PART II — P0 FORENSIC EXTRACTION: COMPLETE CIVILIAN LIFECYCLE

## 4. Why civilian lifecycle is first

The civilian system is the minimum substrate that keeps the civilization alive while higher-level cognition changes its policy.

A villager is not simply a unit that gets trained. The lifecycle is:

```text
existence
  -> production authorization
  -> queue admission
  -> creation
  -> housing/cap accounting
  -> idle/unassigned state
  -> role allocation
  -> source selection
  -> movement/tasking
  -> productive state
  -> interruption
  -> recovery/reassignment
  -> death/replacement
  -> accounting update
```

The first implementation target is therefore not “build an economy.” It is to reconstruct this lifecycle exactly enough to define its interfaces.

---

## 5. P0-A — Villager production

### Stock evidence already established

`units.per` does not simply issue unconditional villager training. It repeatedly evaluates conditions and sets the `trainvillager` goal. The inspected stock logic varies villager-production authorization with food stockpile, villager count, age, strategy, military state, build state, fast-Imperial state, and other conditions.

Examples observed in the target file include:

- villager-count thresholds;
- food thresholds;
- `feudal-food` / `feudal-f2` style food targets;
- pending-villager checks;
- strategy-specific production;
- fast-Imperial thresholds;
- military-state conditions;
- civ-specific branches.

### Forensic questions

1. Which subsystem consumes `trainvillager` and issues the actual train command?
2. Which food reservations/escrow rules gate it?
3. How is pending production distinguished from completed population?
4. What happens when the TC is unavailable, blocked, or under attack?
5. Which civ-specific production rules alter the lifecycle?
6. How is villager production coordinated with age-up and military production?
7. What is the exact failure behavior?

### AEGIS target contract

```text
VILLAGER_DEMAND
 -> affordability check
 -> resource reservation
 -> production authorization
 -> TC queue service
 -> pending state
 -> creation evidence
 -> civilization-state update
```

No direct training rule should become the permanent strategic controller.

---

## 6. P0-B — Housing lifecycle

Housing is not an occasional construction action. It is a production dependency.

Required state machine:

```text
population forecast
 -> housing requirement
 -> lead-time threshold
 -> resource reservation
 -> build request
 -> site selection
 -> builder assignment
 -> foundation
 -> completion
 -> capacity update
```

Forensics must determine stock thresholds, pending-house accounting, multiple-house behavior, emergency behavior, and interaction with population production.

AEGIS must schedule housing from **forecasted blockage**, not wait for population cap failure.

---

## 7. P0-C — Worker accounting

The stock `dawn.per` evidence is especially important. It maintains explicit goals including:

- `sum-villagers`;
- `wood-villagers`;
- `food-villagers`;
- `gold-villagers`;
- `stone-villagers`.

The observed rule structure repeatedly increments/decrements these values until they represent an integer allocation consistent with the current villager population and economic policy.

Therefore the control loop is more accurately represented as:

```text
policy percentages / strategic demand
        ↓
integer target counts
        ↓
role accounting
        ↓
actual worker allocation
```

This is a stronger model than treating the four gatherer percentages as the economy itself.

### Required extraction

- exact source percentages;
- normalization rules;
- minimum food constraints;
- age-specific constraints;
- worker-count rounding;
- role stealing/reallocation;
- stone activation;
- gold activation;
- military/technology dependencies;
- water/fishing effects;
- farm/hunt/forage interactions.

---

## 8. P0-D — Idle worker lifecycle

The civilian substrate must detect and recover workers whose intended task has disappeared.

Required states:

```text
productive
 -> task invalidated
 -> idle/interrupted
 -> cause classification
 -> replacement task search
 -> reassignment
 -> productive
```

Failure classes must distinguish at least:

- source depleted;
- source inaccessible;
- dropsite invalid;
- construction interrupted;
- worker displaced;
- enemy threat;
- command failure;
- strategic reassignment;
- unknown.

An idle-villager system that merely sends workers to an arbitrary resource is not sufficient.

---

## 9. P0-E — Food acquisition

Food is a portfolio, not one resource node.

Required sources:

- herdables;
- forage/berries;
- boar;
- deer/hunt;
- farms;
- fishing;
- civilization/map-specific sources.

`boarhunting.per` demonstrates that hunting itself is a dedicated operational subsystem with state, luring, support, fallback and threat considerations.

The AEGIS food controller must therefore select food by effective value:

```text
expected food income
- walking cost
- drop cost
- setup cost
- infrastructure cost
- risk
- depletion penalty
+ strategic value
```

The exact numerical model comes later. The first task is to identify every stock state transition and dependency.

---

## 10. P0-F — Dropsites and resource infrastructure

A worker assignment is invalid if the required infrastructure is absent.

The civilian lifecycle therefore includes:

```text
resource demand
 -> viable source
 -> nearest/acceptable dropsite
 -> infrastructure check
 -> construction request if absent
 -> worker assignment
 -> gathering
```

Stock initialization evidence already shows explicit spatial parameters for food, wood, gold, stone, hunting, fishing, dropsites, camps, mills, and town/defense regions.

This establishes that distance and infrastructure are first-class economic concerns.

---

## 11. P0-G — Construction dependency

The civilian lifecycle cannot be separated cleanly from construction.

Construction must be modeled as:

```text
request
 -> affordability
 -> placement
 -> foundation
 -> builder assignment
 -> progress
 -> completion
 -> validation
```

Failures must not erase the upstream need. A failed mining camp should produce a recoverable infrastructure failure, not silently strand gold demand.

---

## 12. P0-H — Worker interruption and recovery

The recovery supervisor must eventually distinguish:

- local execution failure;
- temporary resource failure;
- infrastructure failure;
- threat-driven interruption;
- stale strategic request;
- impossible request;
- ABI/command failure.

Retries must be bounded and generation-aware.

---

# PART III — THE ECONOMIC CONTROL SYSTEM

## 13. L3 — Economic scheduler

The economic scheduler is the bridge between cognition and worker operations.

It must transform:

```text
strategic objective
 -> resource demand vector
 -> reservations/escrow
 -> worker targets
 -> task/source requests
```

### Resource escrow is mandatory

Four concepts must remain separate:

1. Strategic commitment — what posture is desired.
2. Economic commitment — what resource requirement is expected.
3. Resource escrow — what is reserved against competing spending.
4. Execution authorization — what may be issued now.

Without this separation, age-up, military, construction and economy will race for the same stockpile.

### Required safeguards

- minimum food continuity;
- housing lead time;
- age-up reservation;
- military reservation;
- technology reservation;
- construction reservation;
- emergency liquidity;
- allocation hysteresis;
- maximum reassignment rate;
- stale-demand expiry;
- generation matching.

---

## 14. Economic scheduler qualification

It is not enough to show that percentages change.

The scheduler must demonstrate:

- integer worker targets converge;
- targets do not oscillate every cycle;
- reserved resources remain protected;
- competing requests have deterministic priority;
- starvation cannot occur through self-reinforcing reassignment;
- source failures cause targeted reallocation;
- strategic changes propagate without corrupting worker accounting.

The current Operations `35/55/10/0` rule is explicitly temporary life support and must be removed as strategic authority once the scheduler is operational.

---

# PART IV — CIVILIAN OPERATING SYSTEMS

## 15. L4 — Civilian Operations

Operations is the hands of AEGIS, not its brain.

It owns execution services such as:

- villager production;
- housing;
- idle recovery;
- food acquisition;
- wood;
- gold;
- stone;
- farms;
- hunting;
- worker reassignment.

Operations must consume service contracts and report evidence. It must not continuously overwrite strategic policy.

---

## 16. L5 — Construction OS

Construction is a persistent queue/state machine.

Each request should carry:

```text
structure
requester
priority
purpose
placement policy
deadline/urgency
builder budget
resource reservation
generation
retry count
failure disposition
```

The OS must support placement zones, builder assignment, foundations, completion detection, failed placement, blocked builders, bad foundations, rebuilds and cancellation.

The stock `buildings.per` corpus is large enough that construction should be treated as a major operating system rather than a helper function.

---

## 17. L6 — Information OS

Information acquisition must become persistent rather than a one-shot scout command.

Required capabilities:

- enemy-player discovery;
- target identity;
- exploration;
- resource discovery;
- military observation;
- threat observation;
- information freshness;
- scout task assignment;
- route/path safety;
- scout recovery;
- replacement scouting.

The current AEGIS Operations scout rule is a bootstrap implementation only. The corrected `up-lerp-tiles` operand is now `g:` rather than `c:`; this fix is important but does not constitute runtime qualification of the entire subsystem.

---

## 18. L7 — Military OS

Military strategy is only the policy layer. The operating substrate must own:

- production;
- army formation;
- grouping;
- task scheduling;
- target evaluation;
- attack;
- defense;
- retreat;
- reinforcement;
- local advantage;
- micro;
- military idle recovery.

The size of `tsa.per` demonstrates that military execution is a substantial control plane in the stock architecture.

---

## 19. L8 — Technology OS

Research must be scheduled against opportunity cost.

Required state:

- age readiness;
- prerequisite state;
- affordability;
- pending research;
- technology priority;
- military/economic competition;
- civ-specific technology;
- reservation ownership;
- completion evidence.

Age-up is an economic transaction with a timing objective, not merely a research command.

---

# PART V — AEGIS COGNITION

## 20. L9 — Strategic cognition

The existing cognitive chain remains valuable:

```text
World Model
 -> Belief
 -> Situation
 -> Objectives
 -> Planning
 -> Decision
 -> Commitment
```

Its responsibility changes subtly: cognition should issue typed requests rather than arbitrary engine commands.

Examples:

```text
ECON_DEMAND(resource=gold, delta=+4, priority=high, reason=military, generation=G)
BUILD_REQUEST(type=stable, priority=high, placement=base-safe, builders=2, generation=G)
MIL_REQUEST(unit=knight, count=3, priority=high, generation=G)
SCOUT_REQUEST(target=enemy_base, urgency=high, generation=G)
```

The `.per` representation may use goals and strategic numbers, but the conceptual contract must remain explicit.

---

## 21. L10 — Verification and recovery

Verification must validate both cognition and substrate.

A successful strategic decision with failed execution is not success.

Required verification classes:

- action issued;
- expected state changed;
- expected state failed to change;
- evidence stale;
- evidence absent;
- action partially completed;
- upstream request invalidated;
- engine/ABI failure.

Recovery should classify before retrying.

---

# PART VI — CROSS-LAYER SYSTEMS WE MUST NOT FORGET

## 22. Persistent state and generation control

Every asynchronous request should carry a generation or equivalent freshness token.

The canonical pattern is:

```text
request generation G
 -> execution
 -> evidence generation G
 -> verification
```

Evidence from generation `G-1` must not satisfy generation `G`.

This prevents stale military, economic, scout, construction and research requests from resurrecting obsolete plans.

---

## 23. Timer architecture

Timers are maintenance clocks, not the state machine itself.

Each timer must have:

- clear owner;
- period;
- purpose;
- state it samples;
- maximum work per pass;
- collision analysis;
- startup behavior;
- failure behavior.

The target architecture should prefer event/state transitions where the engine makes them practical and use timers for maintenance, polling and bounded reconciliation.

---

## 24. Rule-order and command-budget hazards

The engine's rule execution model is part of the ABI.

Known concern: construction/up-build behavior can be sensitive to multiple build commands in one rule pass. Therefore a service must be designed around explicit command budgets rather than assuming every RHS action succeeds independently.

Every module review must inspect:

- ordering;
- conflicting writes;
- same-pass dependencies;
- multiple action commands;
- search-state contamination;
- goal mutation visibility;
- timer collisions.

---

## 25. Search isolation

Search context is effectively shared mutable interpreter state.

Any service using searches must define:

```text
search initialization
 -> scope
 -> target selection
 -> extraction
 -> action
 -> reset/cleanup
```

A module must not assume that a previous module left the search in a known state.

---

## 26. Resource economy as a control problem

The final economy should not be represented solely as four percentages.

The real control vector is closer to:

```text
food demand
wood demand
gold demand
stone demand
construction demand
technology demand
military demand
trade demand
emergency reserve
```

The allocator then decides how many workers and which sources can satisfy those demands under spatial and risk constraints.

---

## 27. Civilization continuity invariants

AEGIS should maintain explicit invariants such as:

- civilization must not intentionally deadlock villager production without authorization;
- population cannot exceed effective capacity through preventable housing failure;
- minimum food continuity must be protected;
- strategic reservations cannot be spent by unrelated services;
- worker counts must reconcile with civilization state within known exceptions;
- completed buildings must not remain permanently represented as pending;
- failed requests must not remain indefinitely executable;
- stale generations must not issue current actions;
- every issued action must have a verification path;
- every nonrecoverable failure must surface to an owning supervisor.

---

# PART VII — LAYER-BY-LAYER RESEARCH METHOD

## 28. Four passes per subsystem

### Pass 1 — Forensics

No implementation.

Extract:

- exact source rules;
- dependencies;
- facts;
- goals;
- strategic numbers;
- timers;
- searches;
- preconditions;
- actions;
- side effects;
- failure behavior;
- rule-order constraints;
- interactions with neighboring systems.

### Pass 2 — Architecture

Define:

- owner;
- state;
- input contract;
- output contract;
- generation semantics;
- validity semantics;
- failure taxonomy;
- ABI operands;
- command budget;
- recovery semantics.

### Pass 3 — Implementation

Implement the smallest production AEGIS-native version.

Rules:

- no Promisory runtime loads;
- no unjustified magic IDs;
- no duplicated strategic ownership;
- no copying stock wholesale;
- no claiming runtime qualification from static success.

### Pass 4 — Adversarial qualification

Attack:

- initialization;
- stale state;
- generation races;
- empty searches;
- blocked placement;
- missing resources;
- population cap;
- starvation;
- simultaneous demands;
- dead units;
- depleted sources;
- inaccessible sources;
- timer collisions;
- command conflicts;
- partial completion;
- recovery loops.

---

## 29. Six-reviewer gate

Every major module receives six independent perspectives:

1. Compiler / ABI Engineer
2. Systems Architect
3. AoE2 Pro Player
4. AoE2 AI Engineer
5. Byzantine One-Trick Specialist
6. Adversarial QA Engineer

Agreement is not qualification. Evidence is qualification.

---

# PART VIII — QUALIFICATION MATRIX

## 30. Static gate

Required:

- balanced parentheses;
- all AEGIS symbols defined;
- no Promisory runtime loads;
- constants in verified ranges;
- unique state ownership;
- request consumers exist;
- failure handling exists.

## 31. ABI gate

Every nontrivial command/operand pair is traced to evidence.

## 32. Dynamic gate

The actual interpreter must demonstrate observable outcomes.

Examples:

- villager production;
- housing;
- worker reassignment;
- food transition;
- construction;
- scouting;
- military production;
- research;
- recovery.

## 33. Stress gate

At minimum:

- food starvation;
- enemy rush;
- lost mining camp;
- blocked builder;
- dead scout;
- population cap;
- depleted food;
- inaccessible resource;
- simultaneous military/age-up demand;
- rapid strategic posture changes;
- late-game population saturation.

---

# PART IX — IMPLEMENTATION ROADMAP

## 34. Phase 0 — Evidence and architecture freeze

- maintain untouched stock reference;
- maintain machine ABI ledger;
- maintain canonical evidence states;
- keep runtime dependency graph clean;
- archive important corrections to GitHub;
- do not create backup clutter in the live runtime tree.

## 35. Phase 1 — Civilian lifecycle forensics

Order:

1. villager production;
2. housing;
3. worker accounting;
4. idle recovery;
5. food-source selection;
6. dropsites;
7. resource infrastructure dependencies;
8. interruption/recovery;
9. escrow interaction;
10. complete lifecycle reconciliation.

**This is the current P0.**

## 36. Phase 2 — Civilization State

Build the smallest trustworthy state substrate that can represent the extracted lifecycle.

## 37. Phase 3 — Economic Scheduler

Introduce demand vectors, escrow, worker targets, hysteresis and affordability.

## 38. Phase 4 — Civilian Operations

Replace temporary static resource policy with request-driven execution.

## 39. Phase 5 — Construction OS

Make infrastructure persistent, observable and recoverable.

## 40. Phase 6 — Spatial Model

Promote resource and infrastructure decisions from scalar counts to spatial opportunities.

## 41. Phase 7 — Information OS

Replace bootstrap scouting with persistent information acquisition.

## 42. Phase 8 — Military OS

Build production, grouping, tasking, targeting, retreat, reinforcement and micro services.

## 43. Phase 9 — Technology OS

Integrate age-up and research with economic escrow.

## 44. Phase 10 — Cognitive integration

Only now should strategic cognition exercise broad civilization control.

## 45. Phase 11 — Adaptation and long-horizon intelligence

After the substrate is reliable, add:

- opponent modeling;
- Byzantine-specific strategic doctrine;
- build-order adaptation;
- map adaptation;
- risk-sensitive planning;
- strategic memory;
- post-action learning;
- long-horizon optimization.

Intelligence is the final multiplier, not the foundation.

---

# PART X — CURRENT AEGIS STATUS

## 46. Existing cognition/substrate modules

The current runtime contains the established AEGIS stack including foundation, Carpenter, Belief, Situation, Objectives, Planning, Decision, Commitment, Execution, Verification, Recovery, Economy, Military and Operations.

Most existing modules have passed static/ABI review at various stages. Operations recently received a confirmed ABI correction to its scout `up-lerp-tiles` call (`c:` -> `g:`), but **Operations as a whole remains runtime-unqualified**.

The current root load graph intentionally excludes Promisory.

## 47. Important existing architectural lessons

- The cognitive chain is not the missing core.
- Civilization continuity is the missing core.
- Static percentage allocation is not an economy.
- Construction is an OS, not a command.
- Scouting is an information service, not a move order.
- Military strategy is not military execution.
- Research is an economic transaction.
- Escrow is distinct from strategic commitment.
- Verification must include physical game-state evidence.
- Recovery must classify failures before retrying.
- Runtime qualification remains mandatory.

---

# PART XI — STOCK-TO-AEGIS TRACEABILITY STANDARD

## 48. Required ledger row

Every extracted stock behavior must eventually have a row containing:

| Field | Required content |
|---|---|
| Stock source | exact file/rule/line region |
| Behavior | precise description |
| Preconditions | facts/goals/SNs/search state |
| Actions | engine operations |
| State | mutated goals/SNs/requests |
| Dependencies | upstream/downstream systems |
| Failure | observed/inferred failure modes |
| Retry | stock behavior and AEGIS policy |
| Strategic role | policy versus execution |
| AEGIS owner | canonical module |
| ABI contract | exact primitive/operand evidence |
| Evidence state | observed/correlated/etc. |
| Test | qualification procedure |

The ledger is more important than copying code. It preserves behavior while allowing AEGIS to use cleaner architecture.

---

# PART XII — P0 QUESTIONS THAT CAN CHANGE THE ARCHITECTURE

These questions are intentionally unresolved until evidence answers them:

1. Where exactly does stock turn `trainvillager` authorization into TC training?
2. What is the complete chain from gatherer percentages to individual villager tasking?
3. Which goals are policy state versus execution state?
4. Which stock state is persistent across rule cycles and which is recomputed?
5. How are idle villagers discovered and reassigned?
6. How are resource sources selected among multiple candidates?
7. How are dropsite distances and infrastructure dependencies enforced?
8. How does stock reserve food for villagers while simultaneously reserving food for age-up/military/research?
9. What exactly does `escrow.per` reserve and release?
10. How are construction failures represented and retried?
11. Which food-source transitions are event-driven versus timer-driven?
12. How does the engine expose pending production versus completed population?
13. What hidden interaction exists between economy, research and military production?
14. Which spatial facts are directly queryable and which require persistent state?
15. What command-budget/rule-order assumptions are embedded in stock operational code?
16. Which stock behavior is essential engine plumbing and which is merely strategic preference?
17. Which mechanisms are civilization-generic and which must remain Byzantine-specific?
18. What happens when two high-priority service requests compete for the same worker/resource/building?
19. What is the minimum substrate required to keep the civilization alive when cognition is temporarily invalid?
20. Which assumptions in the current AEGIS modules become false once the full substrate exists?

These are not optional research questions. Any answer that changes ownership, state representation, or ABI semantics must feed back into the architecture.

---

# PART XIII — ENGINEERING PRINCIPLES

## 49. Non-negotiable rules

1. **Never load Promisory at runtime.**
2. **Never treat plausible semantics as proven ABI.**
3. **Never let strategic modules directly own execution state.**
4. **Never use percentages as the final economic representation.**
5. **Never treat a build command as construction completion.**
6. **Never treat a move command as information acquisition.**
7. **Never retry blindly.**
8. **Never accept stale-generation evidence.**
9. **Never call a subsystem runtime-qualified without target-build evidence.**
10. **Never optimize strategy before civilization continuity is reliable.**
11. **Never let one module silently overwrite another module's policy state.**
12. **Never archive important runtime corrections only on the machine; preserve them in GitHub history.**
13. **Never assume the current architecture is complete.**

---

# PART XIV — DEFINITION OF DONE

AEGIS is not “finished” when the bot wins a scripted opening.

The civilization substrate is complete when the system can continuously:

```text
observe
 -> represent state
 -> identify demand
 -> reserve resources
 -> allocate workers
 -> select viable sources
 -> construct dependencies
 -> execute tasks
 -> verify physical outcomes
 -> recover failures
 -> update state
 -> reconsider policy
```

The strategic layer is complete when it can operate this substrate without bypassing it.

The full bot is complete only when the same architecture survives:

- different maps;
- different openings;
- different resource distributions;
- Byzantine-specific constraints;
- opponent pressure;
- economic disruption;
- military disruption;
- technology races;
- late-game saturation;
- partial subsystem failure;
- target-build interpreter quirks.

The final product should behave less like a giant decision tree and more like a **civilization operating system with strategic cognition above it**.

---

# PART XV — CURRENT NEXT ACTION

**Do not implement another strategy module yet.**

Begin P0 forensic extraction from the untouched target-build stock corpus in this exact order:

```text
units.per
  ↓
gatherers.per
  ↓
dawn.per
  ↓
buildings.per
  ↓
boarhunting.per + food transitions
  ↓
general.per / interaction.per / idle recovery
  ↓
escrow.per
  ↓
complete civilian lifecycle reconciliation
```

Produce the stock-to-AEGIS ledger before implementation.

Then run the six-reviewer architecture gate.

Then implement only the minimum AEGIS-native vertical slice necessary to prove the lifecycle.

Then qualify it in the target interpreter.

Only after that should the next layer be opened.

---

## Related canonical documents

- `docs/AEGIS_CIVILIZATION_SUBSTRATE_GUIDE.md` — detailed substrate architecture.
- `docs/ARCHITECTURE_TRACEABILITY.md` — architecture traceability.
- `docs/KNOWLEDGE_PRESERVATION_STANDARD.md` — preservation standard.
- `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md` — project handoff.
- `docs/CANONICAL_QC_2026-09-05.md` — canonical QC state.

This document is the **master navigation and methodology document**. Detailed forensic ledgers and subsystem specifications should link back to it and may supersede individual sections when new target-build evidence changes the model.
