# AoE2DE `.per` Practical Coding Knowledge Base

**Date:** 2026-09-04  
**Status:** Layer-2 working reference / historical-source-derived  
**Primary source:** verified `AI (HD version).per` and verified Promisory modules  
**Runtime authority:** Layer-1 machine evidence for current DE semantics  

## Purpose

This is the practical catalogue an AEGIS engineer should consult before inventing a new `.per` subsystem.

It answers:

> **What problem must an AoE2 AI solve, what does the old HD/Promisory code do about it, what coding pattern does that imply, and what should AEGIS do differently?**

This is deliberately broader than a syntax reference. AoE2 AI engineering is a strategy-game control problem implemented through a constrained rule language. The same game problem often requires a combination of facts, goals, strategic numbers, timers, search state, feasibility checks, actions, and recovery rules.

---

## 1. Mandatory design questions for every subsystem

Before writing code, answer:

| Question | Required answer |
|---|---|
| WHO | Whose state, whose capability, whose target, whose authority? |
| WHAT | What game variable or capability is changing? |
| WHEN | What age, time, timer, event, transition, or pending state gates it? |
| WHERE | What map area, object, route, base, resource site, or tactical neighborhood? |
| WHY | What strategic objective or conversion does it serve? |
| HOW | Which facts, goals, SNs, searches, actions, and guards implement it? |
| FAILURE | What happens if the action cannot execute or the assumption becomes false? |
| FEEDBACK | What observable state proves success, failure, or changed conditions? |
| OWNERSHIP | Which controller owns the state and which controllers may modify it? |
| EVIDENCE | What is confirmed, inferred, engine-specific, historical, or unknown? |

The minimum control-event shape is:

`OBSERVE -> CLASSIFY -> WRITE STATE -> CHECK AUTHORITY/FEASIBILITY -> ACT -> VERIFY -> UPDATE -> REASSESS`

---

## 2. Constants and namespaces

### Problem

AoE2 AI needs stable identifiers for units, buildings, technologies, goals, strategic numbers, ages, map types, and internal state.

### Historical solution

HD and Promisory use extensive `defconst` declarations and dedicated constant modules. `customConstants.per` also documents version/patch maintenance and load-order concerns.

### Practical pattern

```lisp
(defconst my-goal 123)
(defconst my-mode 2)
```

Use dedicated constant namespaces/blocks for semantic state. Avoid unexplained literals in decision rules.

### AEGIS rule

**PRESERVE:** symbolic constants.  
**IMPROVE:** typed registry + ownership + valid range + semantic description + evidence source.

---

## 3. Initialization / bootstrap

### Problem

A controller needs a known initial state and configuration before strategic rules become active.

### Historical solution

HD initialization establishes ages, exploration parameters, gathering behavior, tactical capabilities, attack-group configuration, target evaluation variables, and other operating doctrine.

### Coding pattern

Initialize configuration once, then transition into normal control. Do not make normal decision rules depend on implicit zero/uninitialized state.

### AEGIS rule

Bootstrap must establish:

`identity + configuration + state defaults + controller ownership + heartbeat readiness`.

---

## 4. Strategic state

### Problem

The AI must remember strategic mode across evaluation cycles.

### Historical solution

`strategy-goal`, `unit-goal`, `control-goal`, `position-goal`, `enemy-goal`, `attack-goal`, `attack-status-goal`, `retreat-now-goal`, `under-attack-goal`, `save-wood-goal`, `escrow-purpose-goal`, and related channels.

### Pattern

```lisp
(if strategic-condition
    (set-goal strategy-goal desired-strategy))
```

The historical source distributes writes across many rules.

### AEGIS rule

**Preserve the conceptual separation. Reject distributed ownership.** One strategic state object should have an explicit owner and controlled transitions.

---

## 5. Strategic numbers

### Problem

Some engine-level settings and persistent control values need to be changed dynamically.

### Historical solution

HD uses strategic numbers extensively for economy, control, exploration, gathering, resources, and engine settings.

### Pattern

```lisp
(set-strategic-number sn-resource-control value)
```

### AEGIS rule

Treat SNs as an interface to the engine, not as an unrestricted strategic database. Maintain a registry describing purpose, writer, consumers, valid range, side effects, and version sensitivity.

---

## 6. Enemy classification

### Problem

Raw enemy observations are expensive to reconstruct repeatedly.

### Historical solution

Observe age, unit families, buildings, military population, defensive structures, and timing; compress them into enemy strategy/threat state.

### Pattern

`raw observations -> enemy-goal/threat state -> downstream strategy/unit rules`.

### Why

The game problem is not "how many units exist?" It is "what capability and transition is the opponent committing to?"

### AEGIS rule

Use typed beliefs:

`belief(class, confidence, evidence, last_observed, expiry)`.

---

## 7. Threat detection

### Problem

Enemy pressure can come from different mechanisms requiring different responses.

### Historical solution

Threats are represented through source/target/type and dedicated threat branches for cavalry, ranged, gunpowder, infantry, fortifications, monks, forward pressure, etc.

### Pattern

`detect threat -> classify mechanism -> choose response transition -> control attack/production/economy`.

### AEGIS rule

Never implement a universal `enemy-is-dangerous` switch when the response depends on mechanism, target, location, timing, and severity.

---

## 8. Resource allocation

### Problem

Food, wood, gold, and stone must support competing future objectives.

### Historical solution

`gatherers.per` changes allocation contextually by age, strategy, technology, units, buildings, and resource state.

### Pattern

`strategic demand -> gatherer allocation -> resource arrival -> production/research capability`.

### AEGIS rule

Worker allocation is an output of strategic demand, not a permanent ratio.

---

## 9. Resource reservation / escrow

### Problem

A resource currently available may be required for a more important near-term conversion.

### Historical solution

`escrow.per` and resource-control logic protect resources for research, technology, units, siege, naval operations, and other purposes, then release them when the commitment executes or becomes obsolete.

### Pattern

`need -> reserve -> protect -> feasibility -> execute -> release`.

### AEGIS rule

Represent reservations explicitly:

`reservation(owner, purpose, resources, deadline, priority, cancel_condition)`.

A resource is not strategically free merely because it is physically in stock.

---

## 10. Feasibility checks

### Problem

A desired action may be impossible because age, technology, building, resource, population, placement, or other conditions are missing.

### Historical solution

`can-build`, `can-research`, pending-object tests, existing-building counts, age conditions, villager thresholds, and time gates.

### Pattern

`intent -> can-* / pending -> action`.

### AEGIS rule

Feasibility is checked immediately before side effects. Earlier planning feasibility must not be treated as proof that execution is currently possible.

---

## 11. Production authorization

### Problem

The AI must decide what to train while resources and production capacity are shared among competing capabilities.

### Historical solution

`units.per` initializes many training flags to `no` and enables specific production goals based on strategic conditions. Unit goals are coupled to strategy, resources, enemy state, technology, and infrastructure.

### Pattern

`strategic requirement -> capability -> production authorization -> queue -> reinforcement/replacement`.

### AEGIS rule

Production is a capability pipeline, not merely a list of units to queue.

---

## 12. Technology / research

### Problem

Technology changes future capability but consumes resources and time.

### Historical solution

Escrow flags, `can-research-with-escrow`, age transitions, economic upgrades, unique upgrades, and release/reset behavior coordinate research.

### Pattern

`technology requirement -> reservation -> feasibility -> research -> verify -> release/reallocate`.

### AEGIS rule

Technology candidates must be scored against immediate survival, timing, future capability, opportunity cost, and transition value.

---

## 13. Buildings / infrastructure

### Problem

Buildings are both prerequisites and strategic capabilities, and placement can fail.

### Historical solution

`buildings.per` contains production/defensive placement logic and explicit backup/rebuild paths. `extremebuildings2.per` contains additional placement strategies and documented performance compromises.

### Pattern

`need -> placement candidate -> feasibility -> build -> pending -> completion/failure -> fallback`.

### AEGIS rule

A building plan is incomplete without placement criteria, postcondition, failure signature, and fallback.

---

## 14. Housing / population infrastructure

### Problem

Production stalls when population capacity is exhausted.

### Historical solution

Dedicated housing state and building rules, with thresholds and pending checks.

### Pattern

`projected demand -> housing requirement -> build authorization -> completion verification`.

### AEGIS rule

Housing is production infrastructure and should be modeled against expected future demand, not only current population.

---

## 15. Economy / dropsites / gatherer logistics

### Problem

Workers need safe and efficient access to resources, and dropsites influence travel time and exposure.

### Historical solution

Gatherer allocation, dropsite distance settings, camp construction, farms/fishing, and map-dependent infrastructure.

### Pattern

`resource demand -> worker assignment -> access point -> travel/safety -> throughput`.

### AEGIS rule

Economic efficiency includes travel, safety, infrastructure, and opportunity cost—not just nominal gather rate.

---

## 16. Food acquisition / boar / hunting

### Problem

Early food has unusually high timing value and requires active management.

### Historical solution

`boarhunting.per` contains dedicated hunting logic and state transitions.

### Pattern

`food requirement -> hunt target -> worker task -> safety/position -> transition to next food source`.

### AEGIS rule

Treat food-source transitions as capability/timing events, not isolated gather commands.

---

## 17. Farms / renewable food

### Problem

The AI must replace exhausted food sources and manage wood expenditure.

### Historical solution

Farm strategy is coupled to `farm-goal`, save-wood logic, gatherer allocation, and resource state.

### AEGIS rule

Farm investment is a conversion of wood into reliable future food throughput; evaluate it against other wood demands and timing.

---

## 18. Scouting / exploration

### Problem

Information is incomplete and must be acquired with limited units, time, and attention.

### Historical solution

`scoutcontrol.per` creates groups, evaluates paths, analyzes obstacles/threats, generates candidate pivot points, calculates waypoints, selects actions, and documents performance limits.

### Pattern

`information need -> target region -> path candidate -> safety evaluation -> waypoint -> action -> observation`.

### AEGIS rule

Scouting should optimize decision value, not maximum explored area.

---

## 19. Candidate search / object selection

### Problem

The rule engine lacks a conventional general-purpose optimizer, but tactical decisions require comparing objects/locations.

### Historical solution

`general.per` builds explicit iterative search state: reset search, find objects, store candidates, evaluate points/distance, preserve best candidate, decrement state, and jump through the rule loop.

### Pattern

`initialize search -> enumerate -> score -> keep best -> terminate -> act`.

### AEGIS rule

Candidate evaluation should be a first-class abstraction with explicit:

`candidate -> features -> constraints -> score -> uncertainty -> selected candidate`.

---

## 20. Distance / geometry

### Problem

Position changes combat, scouting, construction, retreat, and economic value.

### Historical solution

Distance calculations appear in target selection, scouting, placement, and tactical movement.

### AEGIS rule

Geometry must be upstream of strategy when it changes feasibility, timing, exposure, or reinforcement.

---

## 21. Tactical target selection

### Problem

The nearest or weakest target is not always strategically best.

### Historical solution

Target-evaluation variables include HP, distance, range, damage, ROF, siege, time-to-kill, and attack attempts; DUC/search machinery supports object selection.

### Pattern

`eligible targets -> evaluate capability interaction -> score -> select -> act -> verify`.

### AEGIS rule

Target score must include strategic objective and post-engagement consequences, not merely combat efficiency.

---

## 22. Attack state machine

### Problem

An attack has preparation, movement, engagement, regroup, retreat, reset, restart, and reassessment phases.

### Historical solution

Separate `attack-goal`, `attack-status-goal`, `retreat-now-goal`, `restart-attack-goal`, target identity, military level, timers, and reset state.

### Pattern

`prepare -> authorize -> move -> engage -> assess -> continue / regroup / retreat -> cooldown -> restart or transition`.

### AEGIS rule

Attack permission, attack execution, and strategic objective must be separate state dimensions.

---

## 23. Retreat / regroup

### Problem

Continuing a fight can destroy future military capability; retreating can also surrender initiative.

### Historical solution

Retreat changes attack state, arms timers, resets/restarts the attack lifecycle, and later permits reassessment.

### AEGIS rule

A retreat decision must evaluate preservation of military capital, target opportunity, replacement capacity, route safety, and expected recovery window.

---

## 24. Fortification-aware attack

### Problem

Attacking castles, walls, towers, or other defensive structures without the necessary capability can be catastrophically inefficient.

### Historical solution

`enemy-fortifications-goal`, siege availability, military level, population pressure, timers, retreat, and reset branches interact.

### AEGIS rule

Detect the defensive mechanism first. Then ask whether the current force can change the relationship. If not, change capability, target, route, or timing.

---

## 25. Military capability / unit selection

### Problem

The correct unit depends on enemy composition, technology, map, position, resources, and timing.

### Historical solution

`unit-goal` is heavily coupled to strategy and threat state. Production is enabled/disabled contextually.

### AEGIS rule

Select capability, not a memorized counter. Candidate responses include unit, composition, siege, mobility, fortification, denial, technology, retreat, economic transition, or attack elsewhere.

---

## 26. Siege

### Problem

Siege changes the feasible relationship against buildings and massed units but has high opportunity cost.

### Historical solution

Siege availability is checked in offensive and resource-reservation logic; attack behavior changes around fortifications and siege state.

### AEGIS rule

Treat siege as a strategic capability transition, not merely another production item.

---

## 27. Naval / water control

### Problem

Water maps change exploration, economy, transport, production, military control, and retreat geometry.

### Historical solution

`watercontrol.per` has group creation, melee groups, low-HP handling, retreat-position calculation, enemy-strength estimation, target/local-advantage evaluation, and action codes. Map classification changes infrastructure posture.

### AEGIS rule

Water is a separate strategic theater with its own capability graph; do not bolt naval behavior onto land-only logic.

---

## 28. Transport

### Problem

Units must cross water or move through constrained geography while transport capacity and safety are uncertain.

### Historical solution

Transport flags, naval groups, path/position analysis, and tactical control.

### AEGIS rule

Transport is a logistics commitment with route, capacity, escort, timing, and failure states.

---

## 29. Trade / late-game economy

### Problem

Resource acquisition can shift from local gathering toward trade or other scalable economies.

### Historical solution

`trade.per` contains dedicated trade logic and interacts with map/economic conditions.

### AEGIS rule

Treat trade as a transition in the resource-generation model, not simply a building/unit action.

---

## 30. Diplomacy / allies / team context

### Problem

Team games change target selection, resource sharing, attack timing, and military distribution.

### Historical solution

Ally/enemy population context, assistance/tribute state, target selection, and team attack coordination.

### AEGIS rule

Model each player's capability and relationship separately. Team strategy is not merely four independent 1v1 controllers.

---

## 31. Tribute / resource transfer

### Problem

Giving resources can create immediate team capability but reduces self capability.

### Historical solution

Tribute goals and cooperation logic coordinate sharing.

### AEGIS rule

Treat tribute as a resource conversion with team-level expected value and donor survival constraints.

---

## 32. Timers / hysteresis

### Problem

Rules can oscillate when state fluctuates around thresholds.

### Historical solution

Hundreds of timer-enable actions appear around attacks, scouting, micro, defense, tribute, regrouping, and resets.

### Pattern

`enter state -> enable timer -> suppress/restrict re-entry -> expire -> reassess`.

### AEGIS rule

Every unstable state should define entry, persistence, exit, and cooldown semantics.

---

## 33. Self-disabling rules

### Problem

A one-shot transition must not fire every evaluation cycle.

### Historical solution

Many rules disable themselves after writing state.

### AEGIS rule

The concept is valid; the mechanism should be replaced by explicit state ownership and transition guards where architecture permits.

---

## 34. Search loops / jumps

### Problem

The rule substrate lacks conventional loops/collections.

### Historical solution

Stateful search counters plus `up-jump-rule` create iterative behavior.

### Risks

- hidden control flow;
- stale search state;
- difficult termination reasoning;
- performance cost;
- interactions with rule ordering.

### AEGIS rule

Encapsulate search semantics and make reset/termination explicit.

---

## 35. DUC / tactical object control

### Problem

Strategic intent must become unit/object orders.

### Historical solution

DUC/search-oriented systems select objects, targets, groups, waypoints and actions.

### AEGIS rule

Separate strategic command authorization from tactical execution. A strategic controller should not directly micromanage every object unless tactical authority is explicitly delegated.

---

## 36. Pending-state management

### Problem

Buildings, research, production, movement, and other actions take time.

### Historical solution

Pending-object checks and research/production status tests prevent duplicate or premature commands.

### AEGIS rule

Every asynchronous operation has:

`requested -> accepted/rejected -> pending -> completed/failed -> verified`.

---

## 37. Failure and fallback

### Problem

Real game state invalidates plans.

### Historical solution

Backup/rebuild building paths, alternate placement, reset/restart attack states, timers, and alternative strategic branches.

### AEGIS rule

Every high-impact commitment requires:

`failure signature + diagnosis class + recovery policy`.

Failure should update belief rather than disappear as an error.

---

## 38. Resignation / terminal state

### Problem

A controller needs explicit terminal policies rather than continuing meaningless actions.

### Historical solution

`resign.per` contains leniency configuration and multiple terminal-game checks.

### AEGIS rule

Terminal decisions should be explicit, configurable, and strategically justified. Never conflate tactical defeat with global game terminality.

---

## 39. Difficulty / execution capability

### Problem

Strategic knowledge and mechanical execution ability are different axes.

### Historical solution

HD initialization includes parameters such as missile-dodging and distance-maintenance ability, indicating that execution capability can vary independently of strategic logic.

### AEGIS rule

Keep:

`strategy quality != execution skill`.

A future competence model can degrade reaction speed, micro quality, scouting precision, or tactical execution without deleting strategic knowledge.

---

## 40. Taunt / external command interface

### Problem

The AI can expose operator controls or diagnostics without rewriting strategy code.

### Historical solution

The HD source documents taunt codes for changing resource sharing, resignation behavior, resource cheats on hardest, assistance, monk rush, target selection, and current-strategy reporting.

### AEGIS rule

External commands must enter through a controlled interface that validates authority, scope, and lifetime. Do not let diagnostic/operator inputs silently mutate strategic state.

---

## 41. Performance management

### Problem

The rule engine has finite evaluation capacity; sophisticated search can become too expensive.

### Historical solution

Comments in scouting/building/search systems explicitly discuss performance costs, jumps, and reducing analysis granularity.

### AEGIS rule

Every expensive reasoning mechanism needs a cost budget:

`expected decision value / evaluation cost`.

Prefer cached classifications and staged candidate evaluation over repeating high-dimensional predicates.

---

## 42. Version / patch resilience

### Problem

AoE2DE patches can change constants, interfaces, or engine semantics.

### Historical solution

Promisory `customConstants.per` explicitly warns advanced users about refilling settings after patches and documents load-order/overwrite behavior.

### AEGIS rule

Maintain a versioned compatibility layer:

`engine build -> semantic registry -> validated capability set -> runtime profile`.

No strategic rule should silently depend on an unrecorded engine assumption.

---

## 43. Debugging / observability

### Problem

A rule firing is difficult to understand without state visibility.

### Historical solution

Debug/taunt interfaces, strategic-number state, and source comments expose selected internal state.

### AEGIS rule

Expose a structured trace:

`observation -> belief -> requirement -> candidate set -> selected action -> authorization -> execution -> postcondition -> state transition`.

---

## 44. Common anti-patterns identified by the historical code

| Anti-pattern | Why it is dangerous | AEGIS replacement |
|---|---|---|
| Magic numeric state | Semantic ambiguity | Typed state registry |
| Many writers to one state variable | Oscillation / hidden authority | Explicit ownership + arbitration |
| Giant predicates | Cost and fragility | Cached classifications |
| Immediate reaction to threshold | Oscillation | Hysteresis / dwell / cooldown |
| Command = success | False state | Postcondition verification |
| Static resource ratios | Missed transitions | Demand-driven allocation |
| Unit-count-only military logic | Ignores context | Capability/candidate evaluation |
| Static counter table | Fails against transitions | Counter-transition model |
| No fallback | One failure collapses plan | Failure signature + recovery |
| Hidden search state | Stale/incorrect candidate selection | Encapsulated search object |
| Treating map as decoration | Wrong feasible strategy set | Position as strategic state |
| Treating retreat as defeat | Destroys optionality | Tactical interruption state |

---

## 45. Minimum implementation checklist by subsystem

### Economy

- resource observations
- gatherer allocation
- dropsite/logistics state
- reservation/escrow
- housing forecast
- food-source transition
- production demand
- research demand
- failure/recovery

### Production

- capability requirement
- infrastructure requirement
- technology requirement
- resource reservation
- queue authorization
- pending state
- reinforcement/replacement demand
- completion verification

### Military

- enemy belief
- threat classification
- friendly capability
- target candidates
- position/geometry
- timing window
- attack authority
- tactical execution
- post-engagement assessment
- retreat/recovery

### Technology

- prerequisite state
- candidate value
- resource tax
- timing value
- reservation
- feasibility
- pending state
- completion verification
- downstream capability update

### Map / scouting

- map classification
- information gaps
- candidate regions
- route safety
- scouting value
- timing
- observation update

### Infrastructure

- strategic requirement
- candidate placement
- resource tax
- construction authority
- pending state
- placement failure
- fallback
- completion verification

### Team / diplomacy

- ally capability
- enemy capability
- relationship state
- assistance demand
- tribute value
- target coordination
- team timing
- donor/recipient opportunity cost

---

## 46. The AEGIS control contract

Every high-impact decision should eventually fit:

`STATE + BELIEF + UNCERTAINTY + OBJECTIVE + AVAILABLE ACTIONS`

`-> candidate generation`

`-> feasibility filtering`

`-> capability / timing / resource-tax evaluation`

`-> commitment`

`-> authorized action`

`-> observed postcondition`

`-> belief/state update`

`-> continue / modify / abort / recover`.

This is the practical generalization of the historical HD controller without reproducing its distributed implementation.

---

## 47. Evidence discipline

When adding an entry to this catalogue, classify each claim:

- **CONFIRMED:** source syntax/comment or independently verified engine behavior.
- **PROBABLE:** repeated executable pattern with strong consistency.
- **PLAUSIBLE:** strategic interpretation awaiting validation.
- **ENGINE-SPECIFIC:** implementation-dependent.
- **HISTORICAL:** development/compatibility evidence.
- **OBSOLETE:** source marks it unused.
- **DISPROVEN:** stronger evidence contradicts it.

Do not turn an observed coding pattern into a universal AoE2 law without independent validation.

## 48. The practical rule

Before writing a new rule, ask:

> **What game problem am I solving? What state proves that the problem exists? What capability actually changes the relationship? What resources and opportunity costs does that capability consume? What timing window makes it valuable? What if the opponent changes? What if the command fails? What state proves the action succeeded? What state owns the decision? And what does the historical HD/Promisory code teach us about solving the same problem?**

If those questions cannot be answered, the implementation is not yet strategically specified.
