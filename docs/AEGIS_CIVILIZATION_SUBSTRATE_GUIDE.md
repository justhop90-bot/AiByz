# AEGIS Civilization Substrate — Engineering Guide

**Status:** Architecture / implementation master guide  
**Target:** AoE2: Definitive Edition 101.103.48987.0 / BuildID 24094652  
**Runtime principle:** AEGIS-native runtime; stock Promisory is reference material only and must not be loaded.

## 1. Executive finding

The central architectural risk in the current AEGIS design is not an absence of strategic intelligence. It is an incomplete **civilization operating substrate** underneath that intelligence.

The stock AI demonstrates that successful RTS control is a persistent, distributed operating system: resource policy becomes discrete worker assignments; construction policy becomes placement, builder, foundation, retry and recovery state; scouting becomes information acquisition and target management; military strategy becomes production, grouping, tasking, targeting, retreat and reinforcement; research becomes an affordability and opportunity-cost scheduler. These are not incidental implementation details. They are the physical mechanisms by which strategy becomes game state.

AEGIS currently has a strong cognitive chain:

`World Model -> Belief -> Situation -> Objectives -> Planning -> Decision -> Commitment -> Execution -> Verification -> Recovery`

That chain must remain, but it needs a disciplined substrate below it:

`Engine ABI -> World/Spatial State -> Civilization State -> Economic Scheduler -> Civilian Operations -> Construction OS -> Information OS -> Military OS -> Technology OS -> AEGIS cognition`

The objective is **not** to clone Promisory. The objective is to extract the generic, proven RTS operating primitives and reimplement them behind AEGIS-owned interfaces.

## 2. Evidence and why it matters

The authoritative local reference is the untouched stock AI installation at:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

The inspected stock source contains large dedicated subsystems including `units.per`, `buildings.per`, `gatherers.per`, `scoutcontrol.per`, `boarhunting.per`, `researches.per`, `escrow.per`, `tsa.per`, `threats.per`, `interaction.per`, `trade.per`, and others. The flattened `AI (HD version).per` is also substantial. The exact local file contents and counts should be treated as the machine ABI laboratory, not as an assumption that future game builds are identical.

Official AoE2 DE update notes reinforce the same architectural conclusion. The game has repeatedly changed AI behavior around resource allocation, defensive building, scouting, garrisoning, mining-camp ordering, attack-group targeting, micro, research and map-specific behavior. This demonstrates that robust AI behavior depends on many interacting operational systems rather than a single strategic rule set. See the official update references collected during the research pass.

## 3. The missing abstraction: Civilization Operating System

### 3.1 Strategy is not execution

A high-level decision such as `add four gold miners` is not an engine action. It is a resource-management request that must pass through several stateful layers:

`Strategic intent -> economic demand -> resource reservation -> worker-role allocation -> resource-site selection -> worker tasking -> engine command -> verification -> World Model update`

The same pattern applies to construction, military production, scouting and research.

### 3.2 The substrate must own mundane continuity

The substrate must keep the civilization alive even when the strategic layer is temporarily uncertain. Minimum continuity services include:

- continuous villager production when economically authorized;
- housing before population blockage;
- idle-villager recovery;
- resource-role accounting;
- food-source selection and transition;
- dropsite and infrastructure dependencies;
- construction placement and builder management;
- production-queue maintenance;
- basic scouting continuity;
- emergency recovery and garrison behavior;
- research queue continuity.

The strategic layer should change policy, not repeatedly reimplement these mechanisms.

## 4. Proposed AEGIS architecture

### Layer 0 — Engine ABI

Own exact facts, actions, operand classes, goal ranges, strategic-number semantics, searches, placement primitives, rule-order constraints and version-specific quirks.

Deliverable: a machine-verified ABI ledger with examples and negative tests.

### Layer 1 — World / Spatial Model

Expand the current World Model from aggregate resource counts into spatially meaningful state:

- entities and classes;
- resource nodes;
- positions and path distances;
- dropsites;
- infrastructure;
- explored/visible state;
- threat zones;
- worker accessibility;
- settlement/base regions.

A resource should ultimately be represented as `type + quantity + location + accessibility + distance + dropsite relationship + risk`, not merely a scalar quantity.

### Layer 2 — Civilization State

Maintain:

- population and cap;
- villager count;
- idle/pending villagers;
- worker-role counts;
- buildings and foundations;
- production queues;
- stockpiles;
- resource income estimates;
- age;
- technology state;
- military counts;
- active service requests.

### Layer 3 — Economic Scheduler

This is the missing bridge between strategy and gatherers.

It must support:

- resource demand;
- discrete worker targets;
- resource reservations;
- affordability;
- competing claims;
- spending priority;
- emergency liquidity;
- allocation hysteresis to avoid oscillation;
- conversion of strategic goals into worker distributions.

### Layer 4 — Civilian Operations

Own execution of economic policy:

- villager production;
- housing;
- idle recovery;
- food acquisition;
- wood/gold/stone gathering;
- dropsites;
- farms;
- hunting;
- worker reassignment.

Operations must **not** continuously overwrite economic policy with hard-coded percentages.

### Layer 5 — Construction OS

Own:

`request -> can-build -> choose site -> placement -> foundation -> builder assignment -> progress -> completion/failure -> retry/replan`

Construction is a state machine, not a single `build` command.

### Layer 6 — Information OS

Own:

- scout discovery;
- enemy-player identification;
- exploration;
- resource discovery;
- military observation;
- threat observation;
- information freshness;
- scout-task assignment and recovery.

### Layer 7 — Military OS

Own:

- production requests;
- army formation;
- task assignment;
- target evaluation;
- attack/defend/retreat;
- reinforcement;
- local advantage evaluation;
- micro execution;
- military idle recovery.

The stock AI's military subsystem demonstrates that this is a separate operating discipline, not merely a strategic decision rule.

### Layer 8 — Technology OS

Own:

- age-up readiness;
- research affordability;
- prerequisite satisfaction;
- research queue;
- economic technology policy;
- military technology policy;
- civilization-specific technologies;
- opportunity cost.

### Layer 9 — AEGIS Cognition

Retain and strengthen the existing:

`Belief -> Situation -> Objectives -> Planning -> Decision -> Commitment`

The cognition layer issues **typed service requests**, not arbitrary engine commands.

### Layer 10 — Verification / Recovery Supervisor

Verification must validate both strategic decisions and substrate operations. Recovery must classify failures as transient, local, upstream, stale, impossible or ABI-related rather than blindly retrying.

## 5. Critical newly identified subsystem: Economic Escrow

Strategic Commitment and economic reservation are different concepts.

AEGIS must distinguish:

- **Strategic commitment:** what strategic posture is being pursued.
- **Economic commitment:** what resource requirements are expected.
- **Resource escrow:** which resources are reserved against competing spending.
- **Execution authorization:** which concrete action may currently be issued.

Example:

`Commit to cavalry pressure -> reserve gold -> maintain minimum food income -> approve stable production -> issue knight training -> verify -> release/adjust reservation.`

Without this separation, high-level plans will fight the economy for the same resources.

## 6. Economic control loop

The desired loop is:

`Strategic demand -> resource demand vector -> reservation/escrow -> target worker distribution -> discrete allocation -> task/site selection -> execution -> measured income -> model update`

Do not use raw percentages as the final control representation. Percentages can remain a policy input, but the substrate must convert them into explicit integer worker targets and site assignments.

### Required safeguards

- minimum food income for villager continuity;
- housing lead time;
- age-up reservation;
- military-production reservation;
- technology reservation;
- construction reservation;
- emergency liquidity threshold;
- allocation hysteresis;
- maximum reassignment rate per cycle;
- stale-demand expiration;
- generation matching.

## 7. Food Acquisition Controller

Food must be modeled as a portfolio of sources:

- herdables;
- forage/berries;
- boar;
- deer/hunt;
- farms;
- fishing where applicable;
- civilization/map-specific sources.

The controller should select sources using:

`effective food rate = gather rate adjusted for walking, drop distance, setup cost, risk, depletion and infrastructure requirements`

It must support transitions and fallbacks. A food shortage should not simply trigger more generic food workers; it should identify the best available food source and establish the required infrastructure.

## 8. Construction Controller

Every build request should carry at least:

- structure type;
- requester/module;
- priority;
- purpose;
- placement policy;
- deadline/urgency;
- builder budget;
- resource reservation ID;
- retry count;
- generation;
- failure disposition.

The controller must understand that `foundation exists` is not equivalent to `construction complete`, and that a placement can fail without invalidating the strategic objective.

## 9. Spatial Economy

The World Model needs to evolve from `resource count` toward `resource opportunity`.

A useful abstract record is:

`ResourceOpportunity = { type, amount, position, nearestDropsite, pathDistance, expectedRate, setupCost, risk, accessibility, expiry }`

This permits decisions such as:

- whether to build a mining camp;
- whether a distant gold source is economically viable;
- whether to establish a new Town Center;
- whether farms are preferable to distant hunt;
- whether a forward resource is worth the military risk.

## 10. Event-driven substrate

The architecture should not rely entirely on periodic polling. Events should be normalized into state transitions where possible:

- enemy sighted;
- worker attacked;
- resource source depleted;
- building foundation failed;
- production queue blocked;
- housing threshold crossed;
- age-up became affordable;
- military group reached threshold;
- scout discovered target;
- technology completed.

Timers remain appropriate for maintenance and sampling, but events should provide urgency and causality.

## 11. AEGIS service-contract model

The cognition layer should communicate through typed, versioned service requests.

Examples:

### Economy request

`ECON_DEMAND(resource=gold, delta=+4, priority=high, reason=military, generation=G)`

### Construction request

`BUILD_REQUEST(type=stable, priority=high, placement=base-safe, builders=2, generation=G)`

### Military request

`MIL_REQUEST(unit=knight, count=3, priority=high, generation=G)`

### Information request

`SCOUT_REQUEST(target=enemy_base, urgency=high, generation=G)`

The `.per` ABI will encode these through AEGIS-owned goals/strategic numbers, but the conceptual contracts should remain explicit in documentation.

## 12. Implementation strategy

### Phase A — Freeze and document

1. Preserve untouched stock AI as the reference laboratory.
2. Freeze current AEGIS cognitive modules.
3. Maintain a machine ABI ledger.
4. Record every extracted stock primitive as `observed`, `inferred`, `implemented`, or `runtime-qualified`.
5. Keep Promisory absent from the AEGIS runtime load graph.

### Phase B — Build Civilization State

Implement a dedicated AEGIS state layer for population, workers, buildings, queues, stockpiles, age and technology state.

Do not yet optimize strategy. First make state trustworthy.

### Phase C — Build Economic Scheduler

Implement integer worker targets, demand vectors, escrow/reservation, affordability and allocation hysteresis.

Replace the temporary Operations `35/55/10/0` policy with scheduler-driven policy.

### Phase D — Build Civilian Operations

Implement in this order:

1. villager production service;
2. housing service;
3. idle recovery;
4. dropsites;
5. food acquisition;
6. wood;
7. gold;
8. stone;
9. worker reassignment;
10. farm transition;
11. hunting transitions.

Each service receives requests and reports evidence. It does not invent strategic policy.

### Phase E — Construction OS

Implement construction as a persistent queue with placement, builder assignment, foundation monitoring, retry and failure classification.

### Phase F — Spatial Model

Add position/distance/pathability to resource and infrastructure state. Prioritize high-value early-game queries first.

### Phase G — Information OS

Replace the current one-shot scout rule with a persistent scout-task service.

### Phase H — Military OS

Implement production, group formation, tasking, targeting, retreat, reinforcement and micro as separate services.

### Phase I — Technology OS

Implement age-up and research scheduling using the same demand/escrow infrastructure.

### Phase J — Cognitive integration

Only after the substrate is stable should Belief/Situation/Objectives/Planning/Decision begin issuing broad civilization requests.

## 13. Four-pass engineering workflow for every subsystem

Every new subsystem must pass four reviews:

### Pass 1 — Forensics

Extract exact stock behavior from the authoritative machine copy. Record preconditions, actions, state variables, timers, searches, failure behavior and rule-order dependencies. No implementation yet.

### Pass 2 — Architecture

Define AEGIS ownership, state contract, inputs, outputs, generation semantics, validity semantics, failure classes and ABI operands.

### Pass 3 — Implementation

Write the smallest AEGIS-native production implementation. No Promisory loads. No unexplained magic IDs. No strategic-policy duplication.

### Pass 4 — Adversarial qualification

Attack:

- initialization order;
- stale generations;
- rule-order races;
- impossible searches;
- missing resources;
- blocked placement;
- population cap;
- resource starvation;
- duplicate requests;
- partial completion;
- failed commands;
- timer collisions;
- interaction with other services;
- recovery loops.

Then runtime-test before calling the subsystem qualified.

## 14. Six-reviewer model

Use the established six perspectives for every major module:

1. Compiler / ABI Engineer
2. Systems Architect
3. AoE2 Pro Player
4. AoE2 AI Engineer
5. Byzantine One-Trick Specialist
6. Adversarial QA Engineer

A subsystem is not complete because five reviewers like the design. It is complete only when the engine accepts it, the state transitions are observable, and adversarial tests do not expose a critical failure.

## 15. Qualification gates

### Static gate

- balanced parentheses;
- all AEGIS symbols defined;
- no Promisory runtime loads;
- constants within verified ranges;
- no duplicate state ownership;
- all service requests have consumers;
- all consumers have failure handling.

### ABI gate

Every command/operand pair must be traced to an authoritative engine example or runtime qualification.

### Dynamic gate

Verify observable game outcomes:

- villager production continues;
- housing succeeds before cap;
- idle villagers are recovered;
- worker distribution converges;
- resources are gathered from viable sites;
- construction completes;
- failed construction recovers;
- scouts acquire information;
- military production responds to requests;
- technology requests execute;
- strategic changes propagate without corrupting civilization state.

### Stress gate

Test:

- resource starvation;
- enemy rush;
- lost mining camp;
- blocked builder;
- dead scout;
- population cap;
- depleted food source;
- inaccessible resource;
- simultaneous military and age-up demand;
- rapid strategic posture changes;
- late-game population saturation.

## 16. What not to do

Do not:

- load Promisory at runtime;
- copy the stock AI wholesale;
- let Operations continuously overwrite Economy;
- represent the economy only with percentages;
- treat construction as a single command;
- treat food as one homogeneous resource source;
- treat resource counts without spatial context as sufficient;
- allow every strategic module to issue raw engine commands;
- use timers as a substitute for state;
- call a subsystem qualified without runtime evidence;
- optimize strategic sophistication before civilization survival is reliable.

## 17. Immediate implementation backlog

### P0

- qualify the corrected Operations scout ABI;
- extract complete villager production contract;
- extract housing contract;
- extract idle-villager recovery;
- extract worker allocation;
- extract food-source selection;
- identify exact stock goal/strategic-number ownership for these services;
- define AEGIS Civilization State interface.

### P1

- economic demand vector;
- resource escrow;
- worker target allocator;
- food acquisition service;
- dropsite service;
- farm fallback.

### P2

- construction queue;
- placement service;
- builder allocator;
- foundation monitor;
- construction recovery.

### P3

- spatial/resource opportunity model;
- scout-task service;
- information freshness.

### P4

- military production/tasking;
- army grouping;
- target selection;
- retreat/reinforcement;
- military recovery.

### P5

- age/research scheduler;
- technology escrow;
- civilization-specific policy.

### P6

- reconnect the AEGIS cognition stack to the complete substrate;
- remove temporary Operations policies;
- run full-system qualification.

## 18. Definition of success

The AEGIS strategic layer should eventually be able to say, in effect:

> `I believe cavalry pressure is likely. I therefore want a defensive spearman posture, sufficient gold denial, continuous villager production, and a safe transition to the next economic state.`

It should **not** need to know how to:

- find a woodline;
- place a lumber camp;
- select a builder;
- recover a blocked foundation;
- redistribute a villager;
- prevent housing blockage;
- queue a villager;
- select the nearest viable food source;
- calculate the operational consequences of a distant mining camp.

Those are substrate responsibilities.

The strategic brain should command the civilization. The substrate should make the civilization physically operable.

## 19. Research discipline

Every stock behavior we extract should be recorded with:

`SOURCE -> OBSERVED RULE -> ENGINE PRIMITIVES -> STATE DEPENDENCIES -> FAILURE MODES -> AEGIS OWNER -> AEGIS CONTRACT -> TEST -> QUALIFICATION STATUS`

This creates a traceable bridge between the untouched stock AI and the new architecture without creating a runtime dependency.

## 20. Final architectural thesis

The next generation of ByzBot should not be conceived as a larger rule script. It should be conceived as a **hierarchical control system**.

The stock AI provides a mature catalogue of low-level RTS operating mechanisms. AEGIS should retain the mechanisms' proven interaction with the AoE2 engine while replacing their strategic policy with an explicit model-based reasoning system.

The desired end state is:

`Engine ABI`
`  -> Civilization Substrate`
`      -> Economic / Construction / Information / Military / Technology Services`
`          -> AEGIS World Model`
`              -> Belief`
`                  -> Situation`
`                      -> Objectives`
`                          -> Planning`
`                              -> Decision`
`                                  -> Commitment`
`                                      -> Service Requests`
`                                          -> Execution`
`                                              -> Verification`
`                                                  -> Recovery`
`                                                      -> World Model update`

That architecture preserves the hard-won engine knowledge while giving AEGIS a fundamentally stronger control model than a conventional Promisory-style strategy script.
