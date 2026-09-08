# AEGIS Forward Engineering Manual — 2026-09-07 Revision 2

**Project:** AEGIS-BYZ / next-generation Byzantine AI for Age of Empires II: Definitive Edition  
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Authority:** Canonical forward-engineering manual, Revision 2  
**Status:** RESEARCH FREEZE / SUBSTRATE RECONSTRUCTION  
**Runtime rule:** AEGIS owns its runtime. Promisory is forensic/reference material only and must never become a runtime dependency.

> This document supersedes the previous forward manual for forward engineering. The previous manual remains historical context. Revision 2 incorporates the target-build stock forensics, recent civilian/economic/production/control-flow QC, and external ABI cross-reference. The purpose is to stop broad archaeology and turn the evidence into an implementation and qualification program.

---

# 0. Executive decision

The project is **not restarted**. The existing AEGIS cognitive chain is retained, but the earlier assumption that a relatively thin execution layer could connect cognition directly to the game is rejected.

The stock corpus demonstrates a civilization operating substrate containing worker allocation, source selection, dropsite logistics, construction, production arbitration, escrow, threat interaction, recovery, timers, search state and executable rule control flow. AEGIS currently models much of the cognition above that substrate but not enough of the substrate itself.

The engineering decision is therefore:

```text
KEEP THE BRAIN
REBUILD THE BODY
FORMALIZE THE NERVOUS SYSTEM
HARDEN THE ABI
QUALIFY EVERYTHING IN THE TARGET INTERPRETER
```

Planning estimates for redesign:

| Area | Redesign | Decision |
|---|---:|---|
| Engine ABI | 10–20% | Harden; formal evidence ledger + runtime probes |
| World Model | 50–70% | Expand to spatial/service state |
| Civilization State | 80–95% | New first-class subsystem |
| Economic Scheduler | 90–100% | Rebuild |
| Worker Allocation | 80–95% | Rebuild as feedback allocator |
| Resource/Logistics Service | 75–90% | Rebuild |
| Civilian Operations | 75–90% | Rebuild around contracts |
| Construction OS | 75–90% | Rebuild as persistent lifecycle |
| Production Arbitration | 60–80% | Explicit scheduler |
| Information/Scouting OS | 60–75% | Replace bootstrap behavior |
| Military OS | 50–70% | Major substrate expansion |
| Technology/Age OS | 50–70% | Integrate with reservations/escrow |
| Strategic Cognition | 10–30% | Preserve; change interfaces |
| Verification | 50–70% | Expand to physical evidence |
| Recovery | 50–70% | Expand across services |
| Overall implementation | ~60–70% | Major substrate reconstruction, not restart |

These are architecture/implementation estimates, not code-diff measurements. The project is not 60–70% wasted; the strategic architecture remains valuable. The majority of the redesign is below cognition.

---

# 1. Evidence hierarchy and source discipline

Use this hierarchy for every future claim:

1. **Direct target-build runtime observation**
2. **Untouched target-build stock AI corpus**
3. **Controlled target-build runtime experiment**
4. **Existing target-build AEGIS runtime evidence**
5. **Official World's Edge / Age of Empires DE documentation**
6. **AoE2 AI Scripting Encyclopedia**
7. **UserPatch / historical scripting documentation**
8. **Open-source reverse engineering/community research**
9. **Engineering inference**

Do not average conflicting evidence. Record the conflict and rank the sources.

Every important claim must be marked:

- `OBSERVED`
- `CORRELATED`
- `INFERRED`
- `IMPLEMENTED`
- `STATIC-QUALIFIED`
- `RUNTIME-QUALIFIED`
- `STRESS-QUALIFIED`
- `REJECTED`

An `INFERRED` claim may guide an experiment but cannot silently become a runtime invariant.

## Verified external source set

### Official DE

- World's Edge, **AoE2DE Update 61321** — documents `AIDEBUGGING`, `fe-break-point`, current script position/state on breakpoint, infinite jump-loop detection, `AISCRIPTDEBUGGING`, and `LogSystems=AIScript`.  
  https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/

- World's Edge, **AoE2DE Update 177723** — current 2026 release showing continued engine/game/AI fixes; target-build qualification therefore remains mandatory.  
  https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/

### Scripting references

- **AoE2 AI Scripting Encyclopedia** — DE-oriented reference for commands, parameters, strategic numbers, facts, object data, unit lines, resources and technologies.  
  https://airef.github.io/

- **AoE2 AI Scripting Encyclopedia — Commands Index** — documents `up-jump-rule`, `up-log-data`, `up-modify-goal`, `up-modify-sn`, search/object primitives and related commands.  
  https://airef.github.io/commands/commands-index.html

- **UserPatch v1.5 Scripting Guide** — historical reference for extended commands, searches, construction, resource access, timers, jumps, logging, escrow, training, targeting and retasking.  
  https://userpatch.aiscripters.net/reference.html

- **UserPatch CPSB** — historical low-level reference for `set-goal`, `set-strategic-number`, escrow percentages and related AI scripting primitives.  
  https://userpatch.aiscripters.net/CPSB.pdf

External references accelerate semantic reconstruction. They do **not** outrank target-build runtime or untouched target-build source evidence.

---

# 2. Architectural conclusion from the completed research

The original AEGIS chain remains valid as cognition:

```text
observe
→ believe
→ situation
→ objective
→ plan
→ decision
→ commitment
```

But it is not a complete civilization architecture.

The missing middle is:

```text
STRATEGIC INTENT
      ↓
DEMAND
      ↓
ARBITRATION
      ↓
RESERVATION / ESCROW
      ↓
CIVILIZATION STATE
      ↓
SERVICE SELECTION
      ↓
WORKER / ENDPOINT ALLOCATION
      ↓
COMMAND
      ↓
ENGINE STATE
      ↓
OBSERVATION
      ↓
VERIFICATION
      ↓
RECOVERY / REPLAN
```

This is the central redesign decision.

The stock AI should be treated as a **behavioral reference operating system**, not a source tree to copy. AEGIS should recover its proven execution contracts and implement them behind cleaner ownership boundaries.

---

# 3. Canonical AEGIS architecture

```text
L0  ENGINE ABI / INTERPRETER CONTRACT
        ↓
L1  WORLD + SPATIAL OBSERVATION
        ↓
L2  CIVILIZATION STATE / RECONCILIATION
        ↓
L3  DEMAND + ARBITRATION + RESERVATION
        ↓
L4  CIVILIAN / RESOURCE OPERATIONS
        ↓
L5  CONSTRUCTION OS
        ↓
L6  PRODUCTION / QUEUE OS
        ↓
L7  INFORMATION / SCOUTING OS
        ↓
L8  MILITARY OS
        ↓
L9  TECHNOLOGY / AGE OS
        ↓
L10 STRATEGIC COGNITION
        ↓
L11 VERIFICATION / RECOVERY SUPERVISOR
        ↓
L12 TELEMETRY / QUALIFICATION / LEARNING
```

This is a state-and-service architecture, not a rigid call stack.

Ownership:

```text
Cognition              → strategic intent
Demand arbitration     → competing needs / priority
Reservation / escrow   → economic protection
Civilization State     → authoritative operational representation
Operating services     → physical task execution
ABI                    → legal interpreter interaction
Verification           → evidence of outcome
Recovery               → failure classification/disposition
Telemetry              → qualification evidence
```

No service may silently acquire another service's state ownership.

---

# 4. ABI and interpreter discipline

## 4.1 ABI foundation: keep, harden

The current Foundation/ABI work is valuable. Do not rewrite it merely because stock is larger.

Instead formalize an ABI ledger for every nontrivial primitive:

```text
primitive
fact/action class
operand class
valid range
unit vs unit-line vs class distinction
stock example
target-build source evidence
external documentation
negative example
runtime probe
qualification status
owning service
```

Known lesson:

```text
unit ID != unit-line ID != class ID
```

Likewise:

```text
goal storage range != every goal comparison range
```

and:

```text
command accepted != command confirmed
```

## 4.2 Rule control flow is part of the ABI

The scripting references document `up-jump-rule` as a forward/backward jump within the current rule set. citeturn0search1turn0search3

Stock uses jumps extensively. Therefore:

- rule ordering is executable behavior;
- jump topology is executable behavior;
- inserting a rule can alter control flow;
- backward jumps can create loops;
- a rule set cannot be reasoned about as an unordered collection of independent predicates.

Official DE instrumentation explicitly exists to diagnose jump/control-flow problems. citeturn0search0

AEGIS should therefore favor explicit state transitions over giant relative-jump networks.

## 4.3 Mutation visibility

The external references establish mutation primitives such as `set-goal`, `up-modify-goal`, `up-modify-sn`, timers and logging. citeturn0search1turn0search3

They do not establish a universal target-build rule that every mutation is immediately visible to every subsequent predicate in every control-flow context.

Therefore the architectural default remains:

```text
OBSERVE(G)
 → DERIVE(G)
 → DECIDE(G)
 → AUTHORIZE(G)
 → COMMAND(G)
 → ENGINE MUTATION
 → OBSERVE(G+1)
 → VERIFY
```

Same-pass dependencies require a dedicated target-build runtime proof.

## 4.4 Instrumentation is now mandatory engineering infrastructure

Update 61321 explicitly provides `AIDEBUGGING`, `fe-break-point`, `AISCRIPTDEBUGGING`, and `LogSystems=AIScript`. citeturn0search0

The scripting references document `up-log-data`. citeturn0search1turn0search3

Future ABI experiments should therefore use instrumentation instead of speculative interpretation whenever practical.

---

# 5. World Model redesign

Aggregate sensors remain useful:

- food;
- wood;
- gold;
- stone;
- population;
- military counts;
- age;
- focus player.

They are insufficient for civilization execution.

## Resource source

```text
source-id
source-type
object-status
task-load
position
availability evidence
serviceability
observed-at
generation
valid
failure-reason
```

## Dropsite

```text
dropsite-id
dropsite-type
status
position
operational-state
observed-at
generation
```

## Source ↔ dropsite relationship

```text
source
dropsite
delivery/service distance
reachability
task load
worker capacity
policy threshold
validity
freshness
```

Do not call `dropsite-min-distance` exact path distance without evidence. Use **delivery/service distance** until proven otherwise.

## Worker

```text
worker-id
current-role
current-action
current-order
current-target
cargo
source
dropsite
task-validity
threat-state
generation
```

## Building / production endpoint

```text
object-id
type
status
progress
pending/complete
operational
queue state
under-attack
placement state
generation
```

This is necessary to prevent “object exists” from being confused with “object can perform the required service.”

---

# 6. Civilization State — first-class subsystem

This is the largest architectural addition.

AEGIS currently has many independent goals and sensors. That is not equivalent to a reconciled civilization state.

The state layer must represent:

### Population

- total;
- cap;
- headroom;
- pending production;
- effective population state.

### Civilians

- total;
- idle;
- builders;
- workers by role;
- workers by source;
- interrupted workers;
- invalid-task workers.

### Infrastructure

- completed;
- pending;
- foundations;
- damaged;
- operational;
- failed placement;
- serviceable dropsites.

### Production

- requested;
- admitted;
- reserved;
- endpoint selected;
- authorized;
- queued;
- pending;
- confirmed;
- failed.

### Economy

- stockpiles;
- desired income;
- observed income;
- reservations;
- escrow;
- outstanding demands;
- emergency reserve.

### Technology

- age;
- pending age;
- researched technologies;
- pending research;
- reserved costs;
- completion evidence.

### Military

- counts;
- groups;
- posture;
- production demand;
- reinforcement state;
- threat/defense state.

### Information

- enemy identity;
- explored/discovered state;
- scout assignments;
- information freshness;
- threat observations.

### Failure registry

- failure class;
- owning service;
- generation;
- first observed;
- attempts;
- disposition;
- retry/replan condition.

The state layer is **representation, not strategy**.

---

# 7. Economic Scheduler — rebuild

The current Economy module is not acceptable as the final scheduler.

Stock forensics establish a worker-allocation loop:

```text
strategic demand
 → desired role counts
 → actual role counts
 → deficit
 → eligible worker candidates
 → source/dropsite qualification
 → command
 → new engine state
 → re-evaluate
```

Stock separately has an expenditure loop:

```text
production/research/build demand
 → cost registration
 → escrow/reservation
 → affordability
 → execution authorization
 → command
 → release/renew
```

These loops interact but must remain conceptually distinct.

## AEGIS economic control plane

```text
STRATEGIC DEMANDS
        ↓
DEMAND ARBITRATOR
        ↓
RESOURCE REQUIREMENTS
        ↓
RESERVATION / ESCROW
        ↓
WORKER TARGET VECTOR
        ↓
SOURCE / DROPSITE SERVICE
        ↓
TASKING
        ↓
OBSERVED INCOME
        ↓
STATE RECONCILIATION
        ↓
RE-ARBITRATE
```

## Four separate economic concepts

1. **Strategic commitment:** desired posture.
2. **Economic commitment:** expected resource requirement.
3. **Reservation/escrow:** protection against competing spending.
4. **Execution authorization:** permission to issue the specific action.

Never collapse these into one Boolean.

## Required contracts

`ECON_DEMAND`

```text
generation
resource
quantity/delta
priority
urgency
reason
expiry
reservation-policy
```

`RESOURCE_RESERVATION`

```text
reservation-id
generation
resource
amount
owner
purpose
expiry
status
```

`WORKER_TARGET`

```text
generation
role
desired-count
priority
protected-count
source constraints
```

`RESOURCE_RESULT`

```text
generation
source
worker
command-stage
confirmation-stage
observed-income
failure-class
```

Mandatory properties:

- deterministic arbitration;
- bounded reassignment;
- hysteresis;
- stale-demand expiry;
- emergency liquidity;
- generation fencing;
- explicit reservation ownership;
- no silent reservation theft;
- no self-induced starvation.

The temporary Operations `35/55/10/0` policy must eventually disappear as policy authority.

---

# 8. Worker Allocation — rebuild as feedback control

Target model:

```text
DESIRED ROLE VECTOR
        ↓
ACTUAL ROLE VECTOR
        ↓
DEFICIT
        ↓
ELIGIBLE WORKERS
        ↓
PROTECTED WORKERS REMOVED
        ↓
SOURCE CANDIDATES
        ↓
DROPSITE / DISTANCE FILTER
        ↓
TASK-LOAD FILTER
        ↓
RESOURCE-SPECIFIC QUALIFIERS
        ↓
RANK
        ↓
COMMAND
        ↓
OBSERVE
```

Stock evidence shows worker candidate filtering for incompatible cargo, entering, current targets, attack/build conflicts, task load and distance/service constraints.

AEGIS reproduces the **behavioral contract**, not the stock implementation.

Assignment lifecycle:

```text
REQUESTED
→ CANDIDATE_SELECTED
→ COMMAND_ISSUED
→ ENGINE_STATE_OBSERVED
→ PRODUCTIVE
```

Failure:

```text
COMMAND_ISSUED
→ TARGET_LOST / SOURCE_INVALID / THREAT / COMMAND_FAILURE
→ CLEANUP
→ RECLASSIFY
→ REASSIGN
```

`action-default` is a command boundary, not proof of persistent assignment.

---

# 9. Resource acquisition and logistics — rebuild

Stock does not expose one universal resource-availability Boolean.

Common operational substrate:

```text
SOURCE DISCOVERY
 → STATUS QUALIFICATION
 → RESOURCE TYPE
 → SPATIAL QUALIFICATION
 → TASK-LOAD QUALIFICATION
 → RESOURCE-SPECIFIC POLICY
 → RANK / SELECT
 → COMMAND
 → OBSERVE
 → RECOVER
```

`object-data-tasks-count` is an engine-visible workload signal, but thresholds are controller-specific. Stock paths use different thresholds for different resource classes. Therefore AEGIS must not encode a universal capacity formula.

## Failure taxonomy

- `SOURCE_NOT_PRESENT`
- `SOURCE_NOT_USABLE`
- `SOURCE_OVERLOADED`
- `SERVICE_DISTANCE_EXCEEDED`
- `DROPSITE_UNAVAILABLE`
- `INFRASTRUCTURE_PENDING`
- `INFRASTRUCTURE_FAILED`
- `WORKER_INCOMPATIBLE`
- `WORKER_TASK_INVALID`
- `THREAT_BLOCK`
- `STRATEGIC_DEMAND_CHANGED`

`TASK_INVALID` is derived; the underlying cause remains authoritative.

A source that exists but cannot be serviced is not a valid economic opportunity.

---

# 10. Food — portfolio service

Food must be treated as multiple operational source classes:

- herdables/sheep;
- forage/berries;
- boar;
- deer/hunting;
- farms;
- fishing;
- civilization/map-specific sources.

Stock demonstrates materially different controllers and failure behavior for these sources.

Examples:

- forage can fail because no bushes remain;
- fishing can fail through source absence or unacceptable service distance;
- hunting can fail through excessive hunt/drop distance;
- boar has luring, support, reset and validation behavior;
- farms/livestock have distinct worker/source relationships.

Therefore the food service selects a portfolio of source opportunities rather than merely setting a food-worker count.

The eventual optimization target may become:

```text
expected sustainable food income
 - walking cost
 - delivery cost
 - setup cost
 - infrastructure cost
 - threat/risk
 - depletion penalty
 + strategic value
```

Numerical optimization comes after lifecycle correctness.

---

# 11. Construction OS — rebuild as a persistent lifecycle

Construction is a persistent service, not an action.

Required lifecycle:

```text
BUILD_REQUEST
   ↓
RESOURCE RESERVATION
   ↓
CAN_BUILD
   ↓
SITE SELECTION
   ↓
PLACEMENT
   ↓
FOUNDATION OBSERVED
   ↓
BUILDER ASSIGNMENT
   ↓
PROGRESS
   ↓
COMPLETION
   ↓
OPERATIONAL VALIDATION
```

Failure classes:

```text
PLACEMENT_FAILED
BUILDER_INVALID
FOUNDATION_INVALID
TARGET_INVALID
THREAT_BLOCK
RESOURCE_RESERVATION_LOST
CONSTRUCTION_INTERRUPTED
```

Then:

```text
CLASSIFY
 → CLEANUP
 → RETRY / REPLACE / REPLAN / ESCALATE
```

Stock evidence includes pending-object handling, builder-count checks, placement data, foundation/target status, failed-foundation cleanup and placement reset. This justifies a dedicated Construction OS.

A completed building count is **not** sufficient evidence that the structure is operational.

---

# 12. Production and queue arbitration — explicit scheduler

Stock production is distributed rather than a single proven FIFO.

Production intent is represented by goals such as villager/unit training goals. Other rules suppress competing goals based on strategic, military, economic and population conditions. Physical production then passes through affordability/authorization and actual queue endpoints.

AEGIS pipeline:

```text
PRODUCTION_REQUEST
        ↓
ARBITRATION
        ↓
RESERVATION
        ↓
SUPPRESSION / CONFLICT RESOLUTION
        ↓
QUEUE ENDPOINT SELECTION
        ↓
AUTHORIZATION
        ↓
COMMAND
        ↓
ENGINE OBSERVATION
        ↓
VERIFICATION
```

Do not claim a universal stock FIFO or global numeric priority without direct evidence.

A production building existing is not enough. Endpoint selection must consider operational state, pending state, queue/progress, under-attack state and availability.

Contracts:

```text
PRODUCTION_REQUEST
  generation
  category
  object
  quantity
  priority
  urgency
  reason
  cost
  reservation
  endpoint constraints
```

```text
QUEUE_ENDPOINT
  object-id
  endpoint-type
  operational-status
  progress
  queue-load
  under-attack
  distance
  can-execute
  generation
```

```text
ARBITRATION_RESULT
  request-id
  generation
  disposition
  reservation
  endpoint
  suppression-reason
  authorization-state
```

---

# 13. Information / Scouting OS — rebuild

The current Operations scout rule is bootstrap only. The corrected `up-lerp-tiles` operand (`g:` rather than `c:`) fixes one ABI defect but does not qualify the subsystem.

The service must own:

- enemy-player discovery;
- target identity;
- exploration;
- resource discovery;
- military observation;
- threat observation;
- information freshness;
- scout task assignment;
- route/path safety;
- interruption recovery;
- scout replacement.

Success is useful information observed, not merely movement issued.

```text
SCOUT_REQUEST
 → TASK
 → MOVEMENT COMMAND
 → OBSERVATION
 → INFORMATION UPDATE
 → FRESHNESS
```

---

# 14. Military OS — major substrate expansion

The current Military module remains strategically useful but is not a complete military operating system.

The substrate must eventually own:

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
- military idle recovery;
- threat interaction.

The scale of stock `tsa.per` supports treating military execution as a major control plane.

---

# 15. Technology / Age OS — integrate with economy

Research must become an economic transaction:

```text
TECH_DEMAND
 → PREREQUISITE CHECK
 → COST
 → RESERVATION / ESCROW
 → AFFORDABILITY
 → AUTHORIZATION
 → RESEARCH COMMAND
 → COMPLETION OBSERVATION
```

Age-up competes for resources and timing against villagers, military, buildings and technologies.

Required state:

- age readiness;
- prerequisites;
- affordability;
- pending research;
- priority;
- reservation owner;
- completion evidence.

---

# 16. Verification and Recovery — civilization-wide supervision

Every service distinguishes:

```text
REQUESTED
≠ ADMITTED
≠ RESERVED
≠ AUTHORIZED
≠ COMMAND_ISSUED
≠ ENGINE_STATE_OBSERVED
≠ PRODUCTIVE
```

Verification classes:

- command issued;
- expected state changed;
- expected state did not change;
- evidence stale;
- evidence absent;
- partial completion;
- task interrupted;
- upstream request invalidated;
- engine/ABI failure.

Recovery must classify before retrying.

Never:

```text
failure → retry forever
```

Use:

```text
failure
 → classify
 → determine owner
 → bounded retry/reselect/rebuild/replan
 → record attempt
 → escalate if exhausted
```

---

# 17. Threat and safety model

Stock threat handling is distributed rather than one global civilian evacuation manager.

Relevant concepts include:

- under-attack;
- threat metadata;
- enemy units in town;
- source/target threat context;
- military response;
- economic suppression;
- livestock/construction changes;
- interaction/recovery.

AEGIS must preserve:

```text
THREAT_BLOCK
≠
TASK_FAILURE
```

A threat can temporarily invalidate an otherwise healthy task without invalidating the underlying strategic demand.

```text
THREAT SNAPSHOT
   ↓
REQUEST EXECUTABLE?
   ├── YES → execute
   └── NO  → THREAT_BLOCK
                 ↓
            preserve demand
                 ↓
            retry/re-route/reassign
```

Do not claim universal evacuation semantics without target-build evidence.

---

# 18. Generation, freshness and asynchronous state

Every cross-service request must carry a generation or equivalent freshness token.

Canonical lifecycle:

```text
REQUEST(G)
 → EXECUTE
 → OBSERVE(G)
 → VERIFY
```

Evidence from `G-1` must not silently satisfy `G`.

Generation is a correctness primitive for:

- military posture;
- economic demand;
- construction;
- scouting;
- production;
- research;
- recovery.

---

# 19. Timers, rule scheduling and search isolation

Timers are maintenance clocks, not the civilization state machine.

Every timer needs:

- owner;
- purpose;
- period;
- sampled state;
- maximum work;
- startup behavior;
- collision behavior;
- failure behavior.

Rule ordering and jump topology are executable control flow. Timer callbacks must therefore be treated as competing mutation sources.

Search context is mutable interpreter state. Every search service must explicitly:

```text
INITIALIZE
 → SCOPE
 → SELECT
 → FILTER
 → EXTRACT
 → COMMAND
 → RESET / CLEANUP
```

No service may assume another service left search state usable.

---

# 20. Civilization invariants

1. Villager production cannot be intentionally deadlocked without authorization.
2. Housing failure must surface before avoidable population blockage.
3. Minimum food continuity must be protected.
4. Strategic reservations cannot be silently spent by unrelated services.
5. Worker accounting must reconcile with observed civilization state within known engine exceptions.
6. Completed buildings cannot remain permanently represented as pending.
7. Failed requests cannot remain indefinitely executable.
8. Stale-generation evidence cannot satisfy current requests.
9. Every issued command must have a verification path.
10. Every nonrecoverable failure must have an owning supervisor.
11. Source existence is not source serviceability.
12. Building count is not endpoint readiness.
13. Strategic commitment is not execution authorization.
14. Threat blocking does not erase the underlying demand.
15. Recovery is bounded.

---

# 21. Existing AEGIS disposition

## Freeze / preserve

- Foundation
- Belief
- Situation
- Objectives
- Planning
- Decision
- Commitment

These become strategic-intent modules and must stop directly owning lower-level execution state.

## Refactor substantially

- Execution
- Economy
- Military
- Operations
- Verification
- Recovery

## Build as new/expanded substrate

- Civilization State
- Economic Scheduler
- Worker Allocation
- Resource/Logistics Service
- Construction OS
- Production Arbitration
- Information OS
- Technology/Age service

Do **not** rewrite every `.per` simultaneously.

---

# 22. First implementation vertical slice

The first slice must prove civilization continuity before strategic sophistication:

```text
VILLAGER DEMAND
      ↓
POPULATION / HOUSING STATE
      ↓
RESOURCE RESERVATION
      ↓
VILLAGER PRODUCTION ENDPOINT
      ↓
COMMAND
      ↓
PENDING VILLAGER
      ↓
COMPLETION OBSERVED
      ↓
CIVILIAN CENSUS
      ↓
FOOD / WOOD DEMAND
      ↓
WORKER TARGETS
      ↓
SOURCE + DROPSITE SERVICEABILITY
      ↓
WORKER ASSIGNMENT
      ↓
PRODUCTIVE STATE
      ↓
FAILURE / INTERRUPTION
      ↓
RECOVERY
```

This slice exercises ABI, state reconciliation, production arbitration, reservations, worker accounting, resource discovery, logistics, tasking, verification and recovery.

If it cannot run reliably, adding strategy is premature.

---

# 23. Qualification methodology

Every subsystem receives four passes.

## Pass 1 — Forensics

Extract exact stock:

- rules;
- dependencies;
- facts;
- goals;
- strategic numbers;
- timers;
- searches;
- predicates;
- actions;
- mutations;
- failures;
- recovery;
- neighboring subsystem interactions.

## Pass 2 — Architecture

Define:

- owner;
- state;
- input contract;
- output contract;
- generation;
- freshness;
- failure taxonomy;
- ABI operands;
- command budget;
- recovery;
- qualification test.

## Pass 3 — Implementation

Implement the smallest AEGIS-native vertical slice.

Rules:

- no Promisory runtime loads;
- no unjustified IDs;
- no duplicated strategic ownership;
- no wholesale stock copying;
- no runtime qualification claims from static success.

## Pass 4 — Adversarial qualification

Attack:

- initialization;
- empty searches;
- stale state;
- generation races;
- missing/depleted resources;
- inaccessible sources;
- blocked dropsites;
- failed construction;
- dead workers;
- threatened workers;
- population cap;
- simultaneous demands;
- queue contention;
- timer collisions;
- command conflicts;
- partial completion;
- recovery loops;
- rapid strategic changes.

---

# 24. Six-reviewer gate

Every major subsystem receives:

1. Compiler / ABI Engineer
2. Systems Architect
3. AoE2 Pro Player
4. AoE2 AI Engineer
5. Byzantine One-Trick Specialist
6. Adversarial QA Engineer

Agreement is not qualification. Evidence is qualification.

---

# 25. Qualification gates

## Static gate

- balanced parentheses;
- all AEGIS symbols defined;
- no Promisory runtime loads;
- constants in verified ranges;
- unique state ownership;
- request consumers exist;
- failure paths exist.

## ABI gate

Every nontrivial primitive/operand pair has evidence.

## Dynamic gate

Target-build execution demonstrates observable outcomes for:

- villager production;
- housing;
- worker reassignment;
- source transition;
- construction;
- scouting;
- military production;
- research;
- recovery.

## Stress gate

At minimum:

- food starvation;
- enemy rush;
- lost mining camp;
- blocked builder;
- dead scout;
- population cap;
- depleted food;
- inaccessible resource;
- simultaneous age-up/military demand;
- rapid posture changes;
- late-game saturation.

---

# 26. Runtime instrumentation plan

Official DE support provides a direct path to controlled interpreter experiments through `AIDEBUGGING`, `fe-break-point`, `AISCRIPTDEBUGGING`, and `LogSystems=AIScript`. citeturn0search0

The minimum probe suite is:

### Probe A — goal mutation

```text
set-goal / up-modify-goal
 → subsequent predicate
```

### Probe B — strategic-number mutation

```text
set-strategic-number / up-modify-sn
 → subsequent predicate
```

### Probe C — forward jump visibility

```text
mutation
 → up-jump-rule
 → read
```

### Probe D — bounded backward jump

```text
mutation
 → backward jump
 → read
```

### Probe E — command visibility

```text
engine command
 → immediate state read
 → later state read
```

### Probe F — timer boundary

```text
enable/set timer
 → predicate before trigger
 → predicate after trigger
```

### Probe G — search isolation

```text
search A
 → mutation/targeting
 → search B
 → explicit reset
```

The purpose is not to rediscover the entire interpreter. It is to eliminate the small set of unknowns capable of invalidating architecture.

---

# 27. Research freeze

Broad archaeology is now frozen.

New research is permitted only if it addresses:

1. ABI legality;
2. target-build interpreter behavior;
3. stock lifecycle semantics required by an active implementation;
4. a qualification failure;
5. a source contradiction;
6. newly discovered behavior that changes state ownership or architecture.

The objective is a qualified operating substrate, not a perfect clone of stock AI.

---

# 28. Engineering roadmap

## Phase 0 — Evidence freeze

Maintain untouched stock, ABI ledger, forensic archive, external source index and a Promisory-free runtime dependency graph.

## Phase 1 — Civilian lifecycle closure

Complete and reconcile:

1. villager production;
2. housing;
3. worker census/accounting;
4. idle/interrupted recovery;
5. food-source selection;
6. dropsites;
7. resource infrastructure;
8. worker tasking;
9. interruption/recovery;
10. escrow interaction.

## Phase 2 — Civilization State

Implement the minimum authoritative state substrate required by Phase 1.

## Phase 3 — Economic Scheduler

Implement demand, arbitration, reservation, worker targets, hysteresis and affordability.

## Phase 4 — Civilian Operations

Replace static Operations policy with request-driven services.

## Phase 5 — Construction OS

Implement persistent infrastructure requests and recovery.

## Phase 6 — Spatial model

Promote resource decisions from scalar counts to spatial service opportunities.

## Phase 7 — Production Arbitration

Unify logical request arbitration while preserving distinct physical execution paths.

## Phase 8 — Information OS

Persistent scouting, observation, freshness and recovery.

## Phase 9 — Military OS

Production, grouping, targeting, defense, retreat, reinforcement and micro.

## Phase 10 — Technology/Age OS

Integrate age-up/research with economic reservations.

## Phase 11 — Cognitive integration

Allow strategic cognition to control the qualified substrate.

## Phase 12 — Byzantine strategic intelligence

Only after civilization continuity is reliable:

- Byzantine doctrine;
- opponent modeling;
- adaptive openings;
- map adaptation;
- risk-sensitive planning;
- strategic memory;
- post-action learning;
- long-horizon optimization.

---

# 29. Stock-to-AEGIS traceability ledger

Every important stock behavior eventually receives:

| Field | Required |
|---|---|
| Stock source | exact file/rule/line region |
| Behavior | precise description |
| Preconditions | facts/goals/SNs/search state |
| Actions | engine operations |
| State mutation | goals/SNs/flags/engine state |
| Dependencies | upstream/downstream systems |
| Failure | observed/inferred modes |
| Retry | stock behavior + AEGIS policy |
| Strategic role | policy vs execution |
| AEGIS owner | canonical module/service |
| ABI | primitive/operand evidence |
| Evidence | observation level |
| Test | qualification procedure |

The ledger preserves behavior without forcing AEGIS to reproduce stock architecture.

---

# 30. Architecture-critical questions still permitted

Only these classes can reopen broad architecture:

1. Exact conversion of production authorization into physical queue commands.
2. Exact worker accounting boundary and refresh behavior.
3. Exact source/dropsite serviceability semantics required by allocation.
4. Exact construction failure and retry boundaries.
5. Exact escrow reservation/release behavior needed by the scheduler.
6. Exact command-budget constraints.
7. Exact same-pass vs next-pass mutation visibility where AEGIS would depend on it.
8. Exact endpoint readiness semantics.
9. Exact runtime recovery when workers/buildings die or become invalid.
10. Any target-build evidence contradicting the ABI ledger.

Everything else is implementation detail until evidence demonstrates otherwise.

---

# 31. Non-negotiable rules

1. **Never load Promisory at runtime.**
2. **Never treat plausible semantics as proven ABI.**
3. **Never let strategic modules directly own execution state.**
4. **Never treat percentages as the final economic representation.**
5. **Never treat a build command as construction completion.**
6. **Never treat movement as information acquisition.**
7. **Never retry blindly.**
8. **Never accept stale-generation evidence.**
9. **Never call a subsystem runtime-qualified without target-build evidence.**
10. **Never optimize strategy before civilization continuity is reliable.**
11. **Never allow silent policy ownership conflicts.**
12. **Never preserve a critical finding only on the machine; archive it in GitHub.**
13. **Never assume source existence means serviceability.**
14. **Never assume building count means endpoint readiness.**
15. **Never assume command acceptance means success.**
16. **Never let historical documentation outrank target-build evidence.**
17. **Never let external documentation silently define target-build behavior.**
18. **Never let a superseded finding remain canonical without marking it.**

---

# 32. Definition of done

The civilization substrate is complete when AEGIS can continuously:

```text
observe
 → represent state
 → identify demand
 → arbitrate competing demands
 → reserve resources
 → allocate workers
 → select viable sources
 → construct dependencies
 → select production endpoints
 → execute tasks
 → verify physical outcomes
 → recover failures
 → reconcile state
 → reconsider policy
```

Strategic cognition is complete when it can control that substrate without bypassing it.

The full bot is complete only when the architecture survives:

- different maps;
- different openings;
- resource variation;
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

# 33. Immediate next action

Do **not** implement another strategy module.

Start the first vertical slice against the untouched stock corpus in this order:

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
general.per / interaction.per / recovery
  ↓
escrow.per
  ↓
production endpoint reconciliation
  ↓
civilian lifecycle closure
```

For each subsystem:

```text
FORENSICS
 → LEDGER
 → CONTRACT
 → IMPLEMENTATION
 → STATIC GATE
 → ABI GATE
 → TARGET-BUILD RUNTIME TEST
 → ADVERSARIAL TEST
 → GITHUB ARCHIVE
```

No module advances merely because its code looks correct.

---

# 34. Canonical project documents

- `docs/AEGIS_MASTER_ENGINEERING_GUIDE.md` — master methodology/navigation.
- `docs/AEGIS_CIVILIZATION_SUBSTRATE_GUIDE.md` — substrate architecture.
- `docs/ARCHITECTURE_TRACEABILITY.md` — architecture traceability.
- `docs/KNOWLEDGE_PRESERVATION_STANDARD.md` — preservation standard.
- `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md` — project handoff.
- `docs/CANONICAL_QC_2026-09-05.md` — canonical QC state.
- `docs/AEGIS_RUNTIME_CORRECTIONS.md` — verified runtime corrections.
- `docs/forensics/` — stock forensic evidence and subsystem QC.
- `docs/forensics/P0_EXTERNAL_ABI_CROSS_REFERENCE_2026-09-07.md` — external ABI cross-reference.

Revision 2 is the forward-engineering authority until superseded by newer target-build evidence.
