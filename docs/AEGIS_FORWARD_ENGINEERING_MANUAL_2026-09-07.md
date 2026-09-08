# AEGIS Forward Engineering Manual — 2026-09-07

**Project:** AEGIS-BYZ / next-generation Byzantine AI for Age of Empires II: Definitive Edition  
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Status:** Canonical forward plan after P0 stock forensics and external ABI cross-reference  
**Runtime principle:** AEGIS owns its runtime. Promisory is laboratory/reference material only and must never become a runtime dependency.

---

# 0. Executive decision

The project should **not be restarted** and the existing AEGIS cognitive stack should **not be thrown away**.

However, the new stock evidence changes the engineering balance substantially.

The current AEGIS design is cognitively ahead of its civilization substrate. The strategic chain is useful and should be frozen as a strategic-control layer, while the lower half of the system is redesigned around the operating-system behavior proven in the untouched stock corpus.

The correct conclusion is:

> **AEGIS does not need a new brain. It needs a much more complete body, nervous system, scheduler, and ABI discipline.**

The largest redesign is therefore below cognition, not inside cognition.

A practical redesign estimate is:

| Area | Redesign required | Decision |
|---|---:|---|
| Engine ABI layer | 10–20% | Harden, do not rewrite |
| World Model | 40–60% | Expand from aggregate sensors to spatial/service state |
| Civilization State | 70–90% | Build as a first-class subsystem |
| Economic Scheduler | 80–100% | Major redesign; current version is only a placeholder |
| Civilian Operations | 70–90% | Major redesign around service contracts |
| Construction OS | 70–90% | Build as persistent state machine |
| Information/Scouting OS | 50–70% | Replace bootstrap rule with persistent service |
| Military OS | 50–70% | Existing policy is not enough; execution substrate required |
| Technology/Age OS | 50–70% | Integrate with demand/reservation/escrow |
| Strategic Cognition | 10–30% | Preserve architecture; change interfaces |
| Verification/Recovery | 40–60% | Expand to supervise substrate, not just cognition |
| Overall AEGIS runtime | ~60–70% | Preserve the architecture; rebuild much of the substrate |

These are engineering planning estimates, not measured code percentages. They describe how much of each subsystem's **responsibility and implementation** must change.

The key point is that the project is not 60–70% wasted. The existing cognitive architecture remains valuable. The lower-level implementation is where most of the redesign belongs.

---

# 1. What the research changed

The original AEGIS direction was:

```text
observe
→ believe
→ assess situation
→ choose objective
→ plan
→ decide
→ commit
→ execute
→ verify
→ recover
```

That remains valid.

The stock investigation demonstrated that this chain is insufficient as the complete architecture because a strategic decision does not directly become game state.

The missing middle is:

```text
STRATEGY
   ↓
DEMAND
   ↓
RESERVATION / ESCROW
   ↓
CIVILIZATION STATE
   ↓
RESOURCE / QUEUE / BUILDING SERVICE
   ↓
WORKER / ENDPOINT ALLOCATION
   ↓
ENGINE COMMAND
   ↓
ENGINE STATE
   ↓
OBSERVATION
```

This is the central architectural correction.

The stock AI is not merely a giant strategy script. It behaves as a distributed civilization operating system whose strategic policy is interleaved with execution machinery.

AEGIS should not copy that monolith. It should extract its operating primitives and place them behind cleaner AEGIS-owned contracts.

---

# 2. What we learned from the external ABI research

External documentation materially reduces the amount of ABI rediscovery required.

The AoE2 AI Scripting Encyclopedia describes itself as an exhaustive reference covering commands, parameters, strategic numbers, facts, object data, unit lines, resource types and related scripting structures, with DE applicability. The UserPatch reference independently documents extended commands such as `up-jump-rule`, `up-log-data`, `up-modify-goal`, `up-modify-sn`, search/object operations and other primitives.

Official DE update documentation establishes an additional fact: current DE has explicit AI debugging support for control-flow investigation. Update 61321 added `AIDEBUGGING` and `AISCRIPTDEBUGGING`; the former can expose current script position and state when breakpoints or infinite jump loops occur, while the latter can emit AI debugging information into logs. This makes targeted runtime ABI experiments substantially more practical.

The research therefore changes methodology from:

```text
infer → implement → hope → debug
```

to:

```text
external documentation
      ↓
historical/reference semantics
      ↓
target-build stock confirmation
      ↓
target-build runtime experiment where needed
      ↓
ABI ledger
      ↓
implementation
```

External documentation is not allowed to outrank target-build evidence. It is a semantic accelerator and cross-check, not a substitute for qualification.

---

# 3. Revised evidence hierarchy

Use this hierarchy for all future engineering decisions:

1. **Direct target-build runtime observation**
2. **Untouched target-build stock AI source**
3. **Controlled target-build ABI experiment**
4. **Existing AEGIS target-build runtime evidence**
5. **Official World's Edge DE documentation/patch notes**
6. **AoE2 AI Scripting Encyclopedia / UserPatch reference**
7. **Open-source reverse engineering / community research**
8. **Engineering inference**

When two sources disagree, record the disagreement instead of averaging them.

Every important claim must carry a status:

- `OBSERVED`
- `CORRELATED`
- `INFERRED`
- `IMPLEMENTED`
- `STATIC-QUALIFIED`
- `RUNTIME-QUALIFIED`
- `STRESS-QUALIFIED`
- `REJECTED`

No `INFERRED` claim may silently become an architecture dependency.

---

# 4. The new canonical architecture

The target system is now:

```text
L0  ENGINE ABI / INTERPRETER
        ↓
L1  WORLD + SPATIAL MODEL
        ↓
L2  CIVILIZATION STATE
        ↓
L3  ECONOMIC SCHEDULER / ESCROW
        ↓
L4  CIVILIAN OPERATIONS
        ↓
L5  CONSTRUCTION OS
        ↓
L6  INFORMATION / SCOUTING OS
        ↓
L7  MILITARY OS
        ↓
L8  TECHNOLOGY / AGE OS
        ↓
L9  AEGIS STRATEGIC COGNITION
        ↓
L10 VERIFICATION / RECOVERY SUPERVISOR
        ↓
L11 TELEMETRY / QUALIFICATION / LONG-HORIZON ADAPTATION
```

This is not a rigid call stack. It is a state-and-service architecture.

The crucial ownership rule is:

```text
Cognition owns strategic intent.
Scheduler owns resource arbitration.
Civilization State owns authoritative state representation.
Operating systems own physical task execution.
ABI owns legality and interpreter assumptions.
Verification owns evidence.
Recovery owns failure disposition.
```

No layer may silently take ownership of another layer's state.

---

# 5. Redesign decision by module

## 5.1 Foundation / ABI — KEEP, HARDEN

The foundation ABI work is valuable. The major change is methodological rather than architectural.

Add an explicit ABI ledger containing:

- primitive;
- operand class;
- valid range;
- target-build evidence;
- stock example;
- external documentation;
- negative example;
- runtime probe;
- qualification status.

Known lesson from the Byzantine intelligence identifier issue:

```text
unit ID != unit-line ID != class ID
```

The ABI layer must make those distinctions explicit.

Likewise:

```text
goal storage range != goal comparison range
```

and:

```text
command issued != command confirmed
```

The foundation should not be rewritten; it should become the contract boundary that prevents future modules from repeating these mistakes.

---

## 5.2 World Model — EXPAND

The existing aggregate World Model is insufficient for the substrate.

Current useful state such as:

- food;
- wood;
- gold;
- population;
- military counts;
- focus player;

should remain.

But it must expand toward:

```text
RESOURCE SOURCE
  identity
  type
  status
  task load
  position
  availability evidence

DROPSITE
  identity
  type
  status
  position

SERVICE RELATIONSHIP
  source
  dropsite
  delivery/service distance
  reachability
  worker load
  validity
  observed-at

WORKER
  identity
  current order
  current target
  current action
  cargo
  role
  task validity
  threat state

BUILDING
  identity
  type
  status
  progress
  operational state
  queue state
  under-attack state

INFORMATION
  source
  observation time
  generation
  confidence
```

Do not prematurely invent exact quantities where the engine does not expose them. Preserve uncertainty explicitly.

---

# 6. Civilization State — MAJOR NEW SUBSYSTEM

This is the single largest missing architectural component.

AEGIS currently has many independent sensors and goals. That is not equivalent to a coherent civilization state.

Build a state layer that reconciles:

```text
POPULATION
  total
  cap
  headroom
  pending

CIVILIANS
  total
  idle
  builders
  workers by role
  workers by source
  interrupted workers

INFRASTRUCTURE
  completed
  pending
  foundations
  damaged
  operational

PRODUCTION
  requested
  authorized
  endpoint selected
  queued
  pending
  confirmed
  failed

ECONOMY
  stockpiles
  desired income
  observed income
  reservations
  escrow
  outstanding demands

TECHNOLOGY
  age
  pending age
  researched
  queued research
  reserved cost

MILITARY
  counts
  groups
  posture
  pending production

INFORMATION
  enemy identities
  discovered regions
  scout state
  threat state
  freshness

FAILURES
  active failures
  retry count
  owning service
  generation
  disposition
```

The Civilization State is authoritative representation, not strategy.

---

# 7. Economic Scheduler — REDESIGN FROM THE GROUND UP

The current economy module is not the final economic scheduler.

Stock forensics proved several separate mechanisms:

```text
strategic percentages
        ↓
integer desired worker counts
        ↓
actual role counts
        ↓
deficit
        ↓
eligible worker set
        ↓
source/dropsite selection
        ↓
command
        ↓
engine state
        ↓
re-evaluation
```

Separately, stock has an expenditure loop:

```text
production/research/build demand
        ↓
cost registration
        ↓
escrow
        ↓
affordability
        ↓
execution authorization
        ↓
command
        ↓
release/rebuild escrow
```

These loops interact but must not be collapsed.

### AEGIS economic architecture

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
WORKER TASKING
       ↓
OBSERVED INCOME
       ↓
STATE UPDATE
       ↓
RE-ARBITRATE
```

### Required economic objects

`ECON_DEMAND`

```text
generation
resource
quantity/delta
priority
urgency
reason
expiry
reservation policy
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
command stage
confirmation stage
observed income
failure class
```

### Mandatory properties

- deterministic arbitration;
- bounded reassignment;
- hysteresis;
- stale-demand expiry;
- emergency reserve;
- generation fencing;
- explicit resource ownership;
- no silent reservation theft.

The temporary Operations `35/55/10/0` allocation must eventually disappear as policy authority.

---

# 8. Worker Allocation — REDESIGN

The correct model is not:

```text
set wood percentage
```

It is:

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
TASK LOAD FILTER
        ↓
RANK
        ↓
COMMAND
        ↓
VERIFY
```

The stock evidence specifically shows filters for workers who are:

- carrying incompatible resources;
- already entering;
- already targeting the relevant source;
- attacking;
- building;
- otherwise unsuitable;
- too distant from the required service relationship.

AEGIS must reproduce the *behavioral contract*, not the stock implementation.

Worker assignment must become a service with explicit result states:

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

---

# 9. Resource Service — REDESIGN

Stock does not have one universal resource-availability boolean.

It combines:

```text
source existence
+ object status
+ resource type
+ task load
+ spatial serviceability
+ dropsite relationship
+ worker eligibility
+ resource-specific policy
```

The important discovery is that `object-data-tasks-count` is not a universal capacity value. Different controllers use different thresholds.

Therefore AEGIS must not encode:

```text
tasks-count < universal-capacity
```

Instead:

```text
source controller
  → resource-specific serviceability policy
```

Failure classes should include:

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

`TASK_INVALID` is a derived condition; the underlying cause must be retained.

---

# 10. Food — REDESIGN AS A PORTFOLIO

Food must not be represented as one homogeneous source.

The service must know about:

- sheep/herdables;
- berries/forage;
- boar;
- deer;
- farms;
- fishing;
- civilization/map-specific sources.

Stock proves that these sources have different operational controllers and different failure conditions.

Examples:

- forage can fail because no bushes remain;
- fishing can fail because fish are absent or service distance is unacceptable;
- hunting can fail because hunt distance is excessive;
- boar has a dedicated luring/support lifecycle;
- farms have their own worker/source relationship.

Therefore the food service must select among source classes rather than merely increase `food-villagers`.

The eventual optimization target is:

```text
food value
= expected sustainable income
- walking cost
- drop cost
- setup cost
- infrastructure cost
- risk
- depletion risk
+ strategic value
```

But numerical optimization comes after the lifecycle is correct.

---

# 11. Construction OS — MAJOR REDESIGN

Construction is a persistent subsystem, not an action.

Stock evidence includes:

- pending-object searches;
- builder-count logic;
- placement data;
- foundation state;
- target-status validation;
- failed foundation cleanup;
- placement reset;
- adaptive dropsite/camp logic;
- infrastructure migration.

AEGIS construction must implement:

```text
BUILD_REQUEST
   ↓
RESOURCE RESERVATION
   ↓
CAN-BUILD
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

Failure paths:

```text
PLACEMENT_FAILED
FOUNDATION_INVALID
BUILDER_INVALID
TARGET_LOST
THREAT_BLOCK
RESOURCE_RESERVATION_LOST
CONSTRUCTION_STALLED
```

A failed build must preserve the upstream demand when appropriate.

For example:

```text
GOLD DEMAND
  ↓
MINING CAMP REQUEST
  ↓
PLACEMENT FAILURE
  ↓
BUILD FAILURE
  ↓
GOLD SERVICE INVALID
  ↓
ALTERNATIVE CAMP / SOURCE / STRATEGIC RESPONSE
```

This is how infrastructure becomes part of economic reasoning instead of a disconnected helper.

---

# 12. Production Queue Arbitration — REDESIGN

The production investigation proved that stock has no single universal FIFO queue.

It has distributed arbitration using:

- persistent production goals;
- suppression rules;
- rule topology;
- strategic numbers;
- military population limits;
- escrow;
- endpoint search;
- `can-*` authorization;
- final train/research/build commands.

AEGIS should improve the architecture rather than reproduce the distributed complexity.

Use:

```text
PRODUCTION DEMAND
      ↓
LOGICAL ARBITRATION
      ↓
RESERVATION
      ↓
SUPPRESSION / CONFLICT RESOLUTION
      ↓
ENDPOINT DISCOVERY
      ↓
AUTHORIZATION
      ↓
COMMAND
      ↓
ENGINE OBSERVATION
      ↓
VERIFICATION
```

A production building is an operational endpoint, not merely a building count.

The endpoint state should include:

- object identity;
- type;
- operational status;
- progress;
- under-attack state;
- queue load where observable;
- distance;
- `can-execute` state;
- generation.

---

# 13. Escrow — PRESERVE AND STRENGTHEN

Stock escrow evidence is one of the strongest discoveries in the project.

Stock releases and rebuilds escrowed values rather than maintaining a permanently static ledger.

This suggests a transactional cycle:

```text
DEMAND
→ COST REGISTRATION
→ RESERVATION
→ AUTHORIZATION
→ COMMAND
→ OBSERVE
→ RELEASE / RENEW / REBUILD
```

AEGIS should preserve the conceptual distinction:

```text
strategic commitment
≠ economic commitment
≠ resource escrow
≠ execution authorization
```

This separation is foundational and should not be redesigned away.

---

# 14. Information / Scouting OS — REDESIGN

The current Operations scout rule is a bootstrap mechanism, not an information system.

Stock scouting demonstrates persistent state involving:

- enemy discovery;
- target selection;
- waypoints;
- path safety;
- threat awareness;
- reinforcement;
- retreat;
- information acquisition.

AEGIS should implement:

```text
SCOUT_REQUEST
   ↓
TARGET SELECTION
   ↓
ROUTE / SAFETY
   ↓
SCOUT ASSIGNMENT
   ↓
MOVEMENT
   ↓
OBSERVATION
   ↓
INFORMATION UPDATE
   ↓
TASK COMPLETE / RETASK / RECOVER
```

Information itself must have freshness.

An enemy-base observation from generation `G-20` cannot be treated as equivalent to a current observation.

The corrected Operations `up-lerp-tiles` ABI is a useful foundation fix, but it does not qualify the service.

---

# 15. Military OS — REFRAME

The existing Military cognitive module should remain, but it cannot be treated as a complete military system.

Stock `tsa.per` demonstrates the scale of the execution substrate required for:

- group formation;
- target evaluation;
- attack;
- defense;
- retreat;
- reinforcement;
- task scheduling;
- micro.

AEGIS military architecture should therefore split:

```text
MILITARY OBJECTIVE
→ MILITARY DEMAND
→ PRODUCTION / GROUP REQUEST
→ GROUP STATE
→ TASK ASSIGNMENT
→ TARGETING
→ COMMAND
→ COMBAT OBSERVATION
→ RETREAT / REINFORCE / RECOVER
```

Strategic cognition should not directly command individual units as the normal architecture.

---

# 16. Technology / Age OS — REFRAME

Age-up and research belong inside the same economic transaction architecture.

The research evidence establishes:

```text
research demand
→ cost registration
→ escrow flag
→ can-research-with-escrow
→ research command
```

Therefore age-up should become:

```text
AGE OBJECTIVE
→ RESOURCE REQUIREMENT
→ RESERVATION
→ READINESS CHECK
→ AUTHORIZATION
→ COMMAND
→ COMPLETION EVIDENCE
```

Economic technologies should compete through the same reservation/arbitration layer.

This prevents military strategy, age-up and economic technology from independently believing they own the same resources.

---

# 17. Verification — EXPAND FROM COGNITION TO PHYSICAL STATE

Current AEGIS verification is conceptually correct but must become substrate-wide.

Every request must distinguish:

```text
REQUESTED
AUTHORIZED
COMMAND_ISSUED
ENGINE_STATE_OBSERVED
PRODUCTIVE / COMPLETE
```

These are not synonyms.

Example:

```text
BUILD_REQUEST
→ build command issued
≠ foundation exists
≠ builder assigned
≠ building complete
≠ building operational
```

Likewise:

```text
TRAIN_REQUEST
→ train command issued
≠ unit queued
≠ unit created
```

Verification must consume engine evidence rather than trust the command layer.

---

# 18. Recovery — EXPAND INTO A SUPERVISOR

Recovery is currently too heavily associated with strategic failure.

It must supervise the whole substrate.

The recovery model should be:

```text
FAILURE OBSERVED
      ↓
CLASSIFY CAUSE
      ↓
CHECK GENERATION
      ↓
CHECK RETRY BUDGET
      ↓
CHECK WHETHER DEMAND STILL EXISTS
      ↓
LOCAL RECOVERY OR UPSTREAM ESCALATION
```

Recovery dispositions:

- retry locally;
- reselect source;
- reselect worker;
- rebuild infrastructure;
- invalidate request;
- escalate upstream;
- hold;
- abandon as impossible;
- mark ABI fault.

A recovery loop must never be allowed to silently run forever.

---

# 19. Interpreter semantics — ARCHITECTURE HARDENING

The external documentation confirms more than our earlier source-only model, but not everything.

We now know with high confidence that:

- `up-jump-rule` is genuine interpreter control flow;
- it can move forward or backward within a rule set;
- `up-log-data` exists as an AI logging primitive;
- DE provides explicit control-flow debugging;
- infinite jump loops are an engine-recognized failure mode;
- the interpreter exposes a mutable script position during debugging.

The historical rule documentation also describes rules as being evaluated while enabled, with `disable-self` controlling continued evaluation. This is useful historical semantics, but exact current DE pass scheduling still requires target-build qualification.

Therefore AEGIS must assume:

```text
rule execution is stateful
control flow matters
mutation can matter to later execution
pass boundaries are not yet fully characterized
```

Do not build a correctness-critical subsystem around an assumed “snapshot all predicates, commit all actions at end of tick” model.

Use generation fencing instead:

```text
OBSERVE(G)
→ DERIVE(G)
→ DECIDE(G)
→ AUTHORIZE(G)
→ COMMAND(G)
→ ENGINE MUTATION
→ OBSERVE(G+1 or later)
→ VERIFY
```

This architecture remains correct under several plausible interpreter visibility models.

---

# 20. Timers — DEMOTE FROM ARCHITECTURE TO MAINTENANCE

Timers are useful but dangerous.

The current Operations timer repeatedly overwrites strategic-number allocation. That is precisely what must stop.

Timers should own:

- periodic census;
- reconciliation;
- stale-state cleanup;
- source refresh;
- bounded maintenance;
- retry delays.

Timers should not become the hidden owners of strategic policy.

Every timer must declare:

```text
owner
period
purpose
state read
state written
maximum work
startup behavior
collision risk
failure behavior
```

---

# 21. Search state — TREAT AS MUTABLE SHARED CONTEXT

Stock makes extensive use of local and remote searches.

AEGIS must treat search state as mutable interpreter context, not as a pure functional query.

Every search service must explicitly define:

```text
RESET
→ INITIALIZE
→ FILTER
→ RANK / CLEAN
→ SELECT
→ EXTRACT
→ COMMAND
→ RESET
```

No module may assume another module left a search in a known state.

This is especially important if several AEGIS services are executed in one interpreter invocation.

---

# 22. The vertical slice we should actually build

Do not attempt to rebuild the entire civilization at once.

The first production slice should be:

```text
VILLAGER PRODUCTION
        ↓
HOUSING
        ↓
CIVILIZATION CENSUS
        ↓
WORKER TARGETS
        ↓
WOOD + FOOD
        ↓
DROPSITE CHECK
        ↓
WORKER TASKING
        ↓
VERIFICATION
        ↓
RECOVERY
```

Why this slice?

Because it crosses almost every important substrate boundary while remaining small enough to qualify:

- production;
- population accounting;
- construction dependency;
- resource demand;
- worker allocation;
- source selection;
- dropsite logistics;
- command issuance;
- verification;
- recovery.

Once this slice is reliable, gold, stone, military, research and scouting can reuse the same substrate.

---

# 23. P0 forensic program

Before implementing that vertical slice, complete the stock lifecycle in this exact order:

## P0-1 — Villager production

Trace:

```text
trainvillager goal
→ all writers
→ all readers
→ food conditions
→ pending checks
→ TC endpoint search
→ can-train
→ train
→ pending/completed evidence
```

Deliverable: `VILLAGER_PRODUCTION_CONTRACT.md`

## P0-2 — Housing

Trace:

```text
population forecast
→ housing headroom
→ pending houses
→ reservation
→ placement
→ builder
→ completion
```

Deliverable: `HOUSING_CONTRACT.md`

## P0-3 — Worker accounting

Trace `dawn.per` and `gatherers.per` end-to-end.

Deliverable: `WORKER_ACCOUNTING_CONTRACT.md`

## P0-4 — Worker tasking

Trace the exact candidate filters and command boundary.

Deliverable: `WORKER_TASKING_CONTRACT.md`

## P0-5 — Food source selection

Reconcile herdables, forage, hunting, boar, farms and fishing.

Deliverable: `FOOD_ACQUISITION_CONTRACT.md`

## P0-6 — Dropsites/logistics

Trace source-to-dropsite serviceability and infrastructure migration.

Deliverable: `RESOURCE_LOGISTICS_CONTRACT.md`

## P0-7 — Interruption/recovery

Reconcile source failure, worker interruption, threat, builder and death/accounting behavior.

Deliverable: `CIVILIAN_RECOVERY_CONTRACT.md`

## P0-8 — Escrow

Reconcile resource reservation with villager production, construction, research and military production.

Deliverable: `ECONOMIC_TRANSACTION_CONTRACT.md`

## P0-9 — Lifecycle reconciliation

Build the complete state transition graph.

Deliverable: `CIVILIAN_LIFECYCLE_STATE_MACHINE.md`

Only then implement the vertical slice.

---

# 24. Runtime ABI qualification program

External research has reduced the unknown ABI to a manageable set.

Build minimal isolated probes for:

### Probe A — goal visibility

Rule 1 writes a goal. Rule 2 reads it.

### Probe B — strategic-number visibility

Rule 1 mutates an SN. Rule 2 reads it.

### Probe C — jump visibility

Write state, jump forward over a reader, then test what executes.

### Probe D — bounded backward jump

Use a counter to characterize loop behavior without creating an infinite loop.

### Probe E — command observation

Issue a harmless physical command and determine whether its resulting object state is visible immediately or only later.

### Probe F — disable-self

Determine exact persistence/reevaluation behavior in target DE.

### Probe G — timer boundary

Characterize timer-triggered rule execution relative to ordinary rules.

Use `up-log-data` where supported and the official DE AI debugging/logging mechanisms where useful. The goal is not to create a giant test framework. The goal is to close the handful of ABI questions that could invalidate the architecture.

Every probe must record:

```text
build
script hash
initial state
expected result
observed result
log evidence
interpretation
confidence
```

---

# 25. Four engineering passes — mandatory for every subsystem

## Pass 1 — Forensics

No implementation.

Extract exact stock behavior and external semantics.

Record:

- predicates;
- actions;
- state;
- timers;
- searches;
- dependencies;
- failures;
- rule-order effects;
- command boundaries.

## Pass 2 — Architecture

Define:

- owner;
- inputs;
- outputs;
- state machine;
- generation model;
- validity model;
- failure taxonomy;
- ABI operands;
- command budget;
- recovery.

## Pass 3 — Implementation

Implement only the minimum AEGIS-native behavior required by the contract.

No Promisory runtime loads.
No unexplained magic identifiers.
No duplicate ownership.
No strategic policy hidden in execution services.

## Pass 4 — Adversarial qualification

Attack:

- startup;
- empty searches;
- stale generation;
- source depletion;
- dropsite failure;
- blocked construction;
- threat interruption;
- worker death;
- queue saturation;
- competing reservations;
- simultaneous commands;
- timer collision;
- rapid strategic changes;
- partial completion;
- recovery loops.

---

# 26. Six-reviewer gate

Every major subsystem must be reviewed as if by:

1. Compiler / ABI Engineer
2. Systems Architect
3. AoE2 Pro Player
4. AoE2 AI Engineer
5. Byzantine One-Trick Specialist
6. Adversarial QA Engineer

Each reviewer must answer:

```text
What is correct?
What is unsupported?
What is dangerous?
What is missing?
What should be tested next?
```

The reviewer gate is not ceremonial. A subsystem remains open if a critical reviewer identifies an unqualified assumption.

---

# 27. Qualification gates

## Static

- balanced parentheses;
- all symbols defined;
- constants within verified ranges;
- no Promisory runtime dependency;
- unique state ownership;
- all requests have consumers;
- all commands have verification paths;
- all failures have dispositions.

## ABI

- every nontrivial primitive has evidence;
- operand class is known;
- version relevance is known;
- negative cases are documented.

## Dynamic

The target interpreter demonstrates:

- expected state transitions;
- command effects;
- recovery;
- no persistent deadlock.

## Stress

At minimum:

- food starvation;
- population pressure;
- depleted food;
- lost dropsite;
- failed placement;
- worker interruption;
- enemy pressure;
- simultaneous age/military demands;
- production endpoint saturation;
- rapid strategic changes.

---

# 28. What gets preserved from current AEGIS

Do not rewrite these without evidence:

### Preserve

- Foundation ABI structure;
- World Model concept;
- Belief;
- Situation;
- Objectives;
- Planning;
- Decision;
- Commitment;
- Verification concept;
- Recovery concept;
- explicit generation IDs;
- AEGIS-owned runtime load graph;
- Byzantine-specific strategic cognition.

### Refactor interfaces

- Execution;
- Economy;
- Military;
- Operations.

These modules should stop acting as isolated mini-systems and become clients/supervisors of the new substrate.

### Major rebuild

- Civilization State;
- Economic Scheduler;
- Worker Allocation;
- Resource Service;
- Construction OS;
- Production arbitration;
- persistent Information OS.

The distinction is important: **we are not deleting AEGIS; we are changing what its lower layers mean.**

---

# 29. What must NOT happen

Do not:

1. Copy Promisory wholesale.
2. Load Promisory at runtime.
3. Keep hard-coded `35/55/10/0` allocation as permanent authority.
4. Let multiple modules write the same strategic numbers without an ownership contract.
5. Treat building counts as operational endpoint counts.
6. Treat source existence as source serviceability.
7. Treat command issuance as confirmation.
8. Treat worker role as immutable identity.
9. Treat `object-data-tasks-count` as universal capacity.
10. Treat all food sources as equivalent.
11. Treat threat-blocked as identical to ordinary task failure.
12. Treat stale information as current information.
13. Depend on undocumented same-pass mutation behavior.
14. Use timers as hidden strategic schedulers.
15. Claim runtime qualification from static checks.
16. Optimize Byzantine strategy before civilian continuity works.

---

# 30. Immediate execution sequence

The project should proceed in this order.

### Stage 1 — Freeze cognition

Freeze the current cognitive modules except for ABI corrections required by evidence.

Do not add new strategic sophistication.

### Stage 2 — Finish ABI probes

Close the small set of interpreter questions that can affect service contracts.

### Stage 3 — Complete P0 civilian forensics

Finish the lifecycle contracts listed above.

### Stage 4 — Build Civilization State

Implement authoritative state representation before optimizing allocation.

### Stage 5 — Build economic transaction layer

Implement demand → reservation/escrow → authorization.

### Stage 6 — Build worker/resource services

Implement target vectors, candidate selection, source/dropsite qualification and recovery.

### Stage 7 — Build construction

Make infrastructure persistent and serviceable.

### Stage 8 — Build vertical slice

Prove villager + housing + food/wood + worker allocation + construction dependency + verification + recovery.

### Stage 9 — Replace Operations bootstrap policy

Remove the static economic override and make Operations consume scheduler requests.

### Stage 10 — Expand substrate

Gold → stone → farms → hunting → fishing → scouting → military → technology.

### Stage 11 — Reintegrate cognition

Let strategic cognition issue broad typed requests through the now-reliable substrate.

### Stage 12 — Byzantine optimization

Only now optimize:

- Byzantine timing;
- counter-unit selection;
- monastery/relic policy;
- cavalry/infantry transitions;
- defensive architecture;
- map-specific adaptation;
- opponent modeling;
- strategic deception and tempo.

---

# 31. Definition of architectural success

The architecture is successful when a strategic statement such as:

> “We need sustained cavalry pressure.”

can become a verified chain:

```text
BELIEF
 ↓
SITUATION
 ↓
OBJECTIVE
 ↓
PLAN
 ↓
COMMITMENT
 ↓
MILITARY DEMAND
 ↓
GOLD / FOOD DEMAND
 ↓
RESERVATION
 ↓
WORKER TARGETS
 ↓
SOURCE / DROPSITE SERVICE
 ↓
STABLE REQUEST
 ↓
STABLE PLACEMENT
 ↓
BUILDER ASSIGNMENT
 ↓
STABLE OPERATIONAL
 ↓
KNIGHT PRODUCTION AUTHORIZATION
 ↓
QUEUE ENDPOINT
 ↓
TRAIN COMMAND
 ↓
UNIT CREATION
 ↓
MILITARY GROUP
 ↓
TASK
 ↓
COMBAT
 ↓
OBSERVED RESULT
 ↓
UPDATED BELIEF
```

If any link is missing, cognition is making promises the substrate cannot keep.

That is the central test of AEGIS.

---

# 32. Final engineering position

The research does not tell us that AEGIS was a mistake.

It tells us that we built the strategic nervous system before fully reconstructing the civilization machinery that nervous system must control.

That is a fixable engineering problem.

The current architecture should therefore be treated as:

```text
                AEGIS COGNITION
        ┌──────────────────────────┐
        │ Belief                   │
        │ Situation                │
        │ Objectives               │
        │ Planning                 │
        │ Decision                 │
        │ Commitment               │
        └────────────┬─────────────┘
                     │ typed intent
                     ↓
        ┌──────────────────────────┐
        │ ECONOMIC / STRATEGIC     │
        │ ARBITRATION              │
        │ demand / reservation     │
        └────────────┬─────────────┘
                     ↓
        ┌──────────────────────────┐
        │ CIVILIZATION STATE       │
        │ workers / buildings      │
        │ queues / resources       │
        │ information / failures   │
        └────────────┬─────────────┘
                     ↓
        ┌──────────────────────────┐
        │ OPERATING SYSTEMS        │
        │ economy / construction   │
        │ information / military   │
        │ technology               │
        └────────────┬─────────────┘
                     ↓
        ┌──────────────────────────┐
        │ ENGINE ABI               │
        │ searches / actions       │
        │ goals / SNs / commands   │
        └────────────┬─────────────┘
                     ↓
                  GAME STATE
                     ↓
               OBSERVATION
                     ↓
                  AEGIS
```

The strategic architecture stays.

The substrate becomes the main engineering project.

That is the direction going forward.
