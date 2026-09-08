# AEGIS-BYZ — GO-TO ENGINEERING MANUAL
## Canonical Engineering Doctrine — 2026-09-07

**Project:** AEGIS-BYZ / next-generation Byzantine AI for Age of Empires II: Definitive Edition  
**Target runtime:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Repository:** `justhop90-bot/AiByz`  
**Status:** **CANONICAL / HARD-QC PASSED WITH BINDING QUALIFICATIONS**  
**Runtime rule:** AEGIS owns its runtime. Promisory is forensic/reference material only and must never become a runtime dependency.

> This is the go-to engineering manual. Earlier forward manuals remain historical evidence. Where this document conflicts with an older planning document, this document wins unless a newer runtime-qualified finding explicitly supersedes it.

---

# 0. Mission

Build a Byzantine AI that is not merely strategically intelligent, but can reliably operate an entire civilization for long horizons inside the actual AoE2DE interpreter.

The objective is therefore not:

> produce clever `.per` rules.

It is:

> construct a verified civilization operating system whose strategic cognition can reliably command it.

The project must optimize for **correctness, persistence, recoverability, observability, and strategic competence**, in that order during substrate construction.

---

# 1. Final hard-QC verdict

The previous Revision 2 was directionally correct but was **not sufficient as the final go-to manual**. This revision fixes the remaining architectural and evidence problems.

### Binding corrections

1. **Civilization State is not authoritative over the game.** The engine/game state is authoritative. Civilization State is AEGIS's reconciled operational model of that state.
2. **The architecture is not a linear stack.** Cognition, services, state reconciliation, verification, and recovery form a feedback system. The old L0→L12 diagram is a conceptual dependency map, not an execution order.
3. **The 2026 official update corpus is not evidence of the exact target build.** Update 177723 proves the engine continues to evolve; it does not prove that a behavior exists unchanged in build 101.103.48987.0.
4. **Historical/UserPatch documentation is semantic evidence, not target-build proof.** It can establish likely meaning and syntax, but target-build stock/runtime evidence outranks it.
5. **Redesign percentages are planning estimates, not measurements.** They must never be treated as engineering completion metrics.
6. **AEGIS reservations are logical state unless directly mapped to engine escrow.** Do not claim that an AEGIS reservation is itself an engine reservation.
7. **`object-data-tasks-count` is a workload signal, not universal capacity.** Resource-specific policies must interpret it.
8. **Observed income is a measured derivative over a time window, not a primitive fact unless directly exposed by the engine.**
9. **Same-pass mutation visibility remains unqualified until experimentally proven on the target build.**
10. **Research is frozen only in breadth.** Targeted research is mandatory whenever an unresolved fact can invalidate an implementation or qualification result.
11. **Runtime instrumentation is part of the engineering system, not optional debugging.** Official DE documentation provides AI control-flow/debug facilities, including `AIDEBUGGING`, `fe-break-point`, `AISCRIPTDEBUGGING`, and `LogSystems=AIScript`. [World's Edge Update 61321](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/)
12. **No runtime claim is green merely because static analysis passes.** Static, ABI, dynamic, and stress qualification remain separate gates.

---

# 2. Evidence law

Every architectural claim must have an evidence class.

## Authority order

1. **Direct runtime observation on the exact target build**
2. **Untouched stock AI source from the exact target build**
3. **Controlled target-build runtime experiment**
4. **Existing AEGIS runtime evidence on the target build**
5. **Official World's Edge / Age of Empires DE documentation**
6. **AoE2 AI Scripting Encyclopedia**
7. **UserPatch / historical scripting references**
8. **Open-source reverse engineering and community research**
9. **Engineering inference**

When sources conflict, preserve the conflict and explain which source wins. Never average contradictory evidence.

## Claim states

- `OBSERVED` — directly observed in the target environment.
- `CORRELATED` — independently supported by multiple evidence sources.
- `INFERRED` — engineering interpretation not directly proven.
- `IMPLEMENTED` — present in AEGIS code.
- `STATIC-QUALIFIED` — source/static checks pass.
- `RUNTIME-QUALIFIED` — exercised successfully in the target interpreter.
- `STRESS-QUALIFIED` — survives adversarial/repeated conditions.
- `REJECTED` — disproven or superseded.
- `UNQUALIFIED` — evidence insufficient for a stronger state.

**Rule:** `INFERRED` and `CORRELATED` are not substitutes for `RUNTIME-QUALIFIED` when the behavior depends on interpreter execution semantics.

---

# 3. Verified external source register

## Official DE sources

- **World's Edge — AoE2DE Update 61321**  
  Documents `AIDEBUGGING`, `fe-break-point`, script-position/state diagnostics, infinite jump-loop detection, `AISCRIPTDEBUGGING`, and `LogSystems=AIScript`.  
  https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/

- **World's Edge — AoE2DE Update 177723**  
  A 2026 official update demonstrating that AI/game engine behavior continues to receive fixes and changes. It is useful for current context, but is **not** target-build proof for 101.103.48987.0.  
  https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/

- **AoE2DE Known Issues & Solutions**  
  Official support source for current issue tracking and troubleshooting context.  
  https://support.ageofempires.com/hc/en-us/articles/360049490811-Age-of-Empires-II-Definitive-Edition-Known-Issues-Solutions

## Scripting sources

- **AoE2 AI Scripting Encyclopedia** — DE-oriented command, parameter, strategic-number, fact, object-data, unit-line, resource and technology reference.  
  https://airef.github.io/

- **AI Scripting Encyclopedia — Commands Index**  
  https://airef.github.io/commands/commands-index.html

- **AI Scripting Encyclopedia — Parameters**  
  https://airef.github.io/parameters/parameters-index.html

- **AI Scripting Encyclopedia — Intro to Commands**  
  https://airef.github.io/resources/articles/intro-to-commands.html

- **AI Scripting Encyclopedia — Data Limits**  
  https://airef.github.io/resources/articles/data-limits.html

- **UserPatch v1.5 Scripting Guide** — historical reference for extended AI commands and semantics.  
  https://userpatch.aiscripters.net/reference.html

External documentation is a cross-check and semantic accelerator. It never overrides exact target-build evidence.

---

# 4. Architecture: the corrected model

Do **not** implement AEGIS as a linear stack. The real architecture is a feedback system:

```text
                         ┌─────────────────────┐
                         │ STRATEGIC COGNITION  │
                         │ belief / situation  │
                         │ objectives / plan   │
                         │ decision / commit   │
                         └──────────┬──────────┘
                                    │ strategic intent
                                    ▼
                         ┌─────────────────────┐
                         │ DEMAND + ARBITRATION│
                         │ priority / conflict │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┼────────────────┐
                    ▼               ▼                ▼
               ECONOMY        CONSTRUCTION       PRODUCTION
               RESOURCE       INFORMATION        MILITARY
               SERVICES       TECHNOLOGY         SERVICES
                    │               │                │
                    └───────────────┼────────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │ ENGINE / AI ABI     │
                         └──────────┬──────────┘
                                    ▼
                                  GAME
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ OBSERVATION / STATE │
                         │ RECONCILIATION      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ VERIFICATION        │
                         │ FAILURE / RECOVERY  │
                         └──────────┬──────────┘
                                    │
                                    └──────→ cognition
```

### Ownership law

- **Engine/game:** ultimate physical authority.
- **Civilization State:** reconciled AEGIS model of observed engine state.
- **Cognition:** strategic intent.
- **Demand arbitration:** competing needs and priorities.
- **Reservation/escrow:** economic protection; engine escrow semantics must not be conflated with AEGIS bookkeeping.
- **Operating services:** physical execution.
- **ABI layer:** interpreter legality and known semantics.
- **Verification:** outcome evidence.
- **Recovery:** failure classification and disposition.
- **Telemetry:** qualification evidence.

No module may silently become the owner of another module's state.

---

# 5. What we keep

The current cognitive chain is retained:

```text
World observation
 → Belief
 → Situation
 → Objectives
 → Planning
 → Decision
 → Commitment
```

These modules are not declared finished merely because their architecture is preserved. Their interfaces must be adapted to the new substrate.

The following are therefore **protected architecture**, not frozen code:

- Foundation/ABI
- Belief
- Situation
- Objectives
- Planning
- Decision
- Commitment

The following are **substrate reconstruction targets**:

- Execution
- Verification
- Recovery
- Economy
- Military
- Operations
- Civilization State
- Worker Allocation
- Resource/Logistics
- Construction
- Production Arbitration
- Information/Scouting
- Technology/Age integration

---

# 6. Civilization State

This is the principal new subsystem.

The engine is authoritative. Civilization State is a reconciled model with freshness and confidence metadata.

## Required state domains

### Population

- total
- cap
- headroom
- pending production
- population-affecting pending state

### Civilians

- total
- idle
- builders
- workers by current operational role
- workers by source
- interrupted workers
- invalid-task workers

### Infrastructure

- object identity
- type
- pending/foundation state
- completion
- operational usability
- damage/under-attack evidence
- service relationship
- placement state

### Production

```text
REQUESTED
→ ADMITTED
→ RESERVED
→ ENDPOINT_SELECTED
→ AUTHORIZED
→ COMMAND_ISSUED
→ ENGINE_OBSERVED
→ CONFIRMED
```

### Economy

- stockpiles
- measured income over windows
- demand vector
- logical reservations
- engine escrow state where applicable
- liquidity/emergency reserve

### Information

- source
- timestamp/generation
- confidence
- discovered state
- stale state
- enemy/focus state
- scout task state

### Failure registry

- service
- object/worker/request
- generation
- failure class
- attempts
- first observed
- disposition
- retry/replan eligibility

Every important state record must carry freshness/generation where stale information could cause an incorrect action.

---

# 7. Economy: rebuild, not tune

The current static Operations policy (`35/55/10/0`) is scaffolding, not an economy.

Stock proves a feedback allocator:

```text
DEMAND
 ↓
DESIRED ROLE VECTOR
 ↓
ACTUAL ROLE VECTOR
 ↓
DEFICIT
 ↓
ELIGIBLE WORKERS
 ↓
SOURCE / DROPSITE QUALIFICATION
 ↓
TASK COMMAND
 ↓
OBSERVE ENGINE STATE
 ↓
MEASURE RESULT
 ↓
RE-ARBITRATE
```

Stock also has a distinct expenditure path involving cost registration, escrow, affordability and execution.

## Never collapse these concepts

1. Strategic commitment — what we want strategically.
2. Economic demand — what resources the strategy requires.
3. Logical reservation — what AEGIS intends to protect.
4. Engine escrow — what the engine's economic substrate actually reserves.
5. Execution authorization — whether a specific command may be issued.
6. Queue endpoint — where the command can physically execute.
7. Confirmation — whether the engine actually entered the intended state.

## Economic contracts

### `ECON_DEMAND`

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

### `RESOURCE_RESERVATION`

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

This is AEGIS logical state unless directly coupled to a proven engine escrow mechanism.

### `WORKER_TARGET`

```text
generation
role
desired-count
priority
protected-count
source constraints
```

### `RESOURCE_RESULT`

```text
generation
source
worker
command-stage
confirmation-stage
measured-output
failure-class
```

Mandatory scheduler properties:

- deterministic arbitration;
- bounded retasking;
- hysteresis;
- stale-demand expiry;
- emergency liquidity;
- generation fencing;
- explicit reservation ownership;
- starvation prevention;
- recovery from source failure.

---

# 8. Worker allocation

A worker role is an operational state, not immutable identity.

```text
WORKER
 ├─ identity
 ├─ current role
 ├─ action
 ├─ order
 ├─ target
 ├─ cargo
 ├─ source
 ├─ dropsite relationship
 ├─ task validity
 ├─ threat state
 └─ generation/freshness
```

Allocation is:

```text
TARGET ROLE VECTOR
 → ACTUAL ROLE VECTOR
 → DEFICIT
 → ELIGIBLE WORKERS
 → PROTECTED WORKERS EXCLUDED
 → SOURCE CANDIDATES
 → SPATIAL / DROPSITE FILTER
 → TASK-LOAD FILTER
 → RESOURCE-SPECIFIC FILTERS
 → RANK
 → COMMAND
 → OBSERVE
```

`action-default` or an equivalent command is **command issuance**, not proof of persistent success.

The required lifecycle is:

```text
REQUESTED
→ CANDIDATE_SELECTED
→ COMMAND_ISSUED
→ ENGINE_STATE_OBSERVED
→ PRODUCTIVE
```

Failure:

```text
TASK INVALID
→ CLEANUP / STOP AS REQUIRED
→ CLASSIFY CAUSE
→ RESELECT
→ REASSIGN
```

---

# 9. Resource and logistics service

Stock does not support a universal `resource-good/resource-bad` model.

Resource serviceability is the conjunction of relevant dimensions:

```text
SOURCE EXISTS
+ OBJECT STATUS USABLE
+ RESOURCE TYPE QUALIFIED
+ TASK LOAD ACCEPTABLE FOR THIS CONTROLLER
+ SERVICE DISTANCE ACCEPTABLE
+ DROPSITE AVAILABLE
+ WORKER ELIGIBLE
+ STRATEGIC DEMAND STILL VALID
```

`object-data-tasks-count` is a workload signal. Different resource controllers use different thresholds. Therefore there is no universal capacity constant.

## Failure classes

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
- `COMMAND_NOT_OBSERVED`

`TASK_INVALID` is a derived state; preserve the underlying cause.

Do not assume `dropsite-min-distance` is exact path distance. Use **delivery/service distance** until independently qualified.

---

# 10. Food service

Food is a portfolio, not a scalar worker role.

Supported source classes include:

- herdables/sheep
- forage/berries
- boar
- deer/hunting
- farms
- fishing
- map/civilization-specific sources

Each source class may have its own lifecycle, failure conditions, logistics, and recovery.

The first implementation goal is not optimization. It is **correct source lifecycle and recovery**.

Only after lifecycle correctness is established should AEGIS optimize:

```text
expected sustainable income
- walking/service cost
- infrastructure cost
- risk
- depletion risk
+ strategic value
```

Any numerical model must be based on measured or documented quantities, not invented precision.

---

# 11. Construction OS

Construction is a persistent service.

```text
BUILD_REQUEST
 → RESOURCE ADMISSION
 → CAN_BUILD
 → SITE SELECTION
 → PLACEMENT
 → FOUNDATION OBSERVED
 → BUILDER ASSIGNMENT
 → PROGRESS
 → COMPLETION
 → OPERATIONAL VALIDATION
```

Failure states include:

- placement rejected;
- foundation invalid;
- builder target invalid;
- construction interrupted;
- threat blocked;
- resource reservation lost;
- target deleted/invalid;
- completion not observed.

A building count is never sufficient evidence of serviceability. A production endpoint, dropsite, defensive structure, or economic building must be represented by operational state.

Construction recovery must be able to:

```text
RETAIN
→ REASSIGN
→ REPLACE
→ DELETE/RESET
→ REPLAN
```

according to observed cause.

---

# 12. Production and technology OS

Production is arbitration plus physical endpoint selection, not a single FIFO queue.

The conceptual lifecycle is:

```text
DEMAND
 → ARBITRATION
 → RESERVATION/ESCROW
 → SUPPRESSION/CONFLICT RESOLUTION
 → ENDPOINT SELECTION
 → AUTHORIZATION
 → COMMAND
 → ENGINE OBSERVATION
 → CONFIRMATION
```

A production building existing does not prove it is an operational endpoint. Endpoint state can depend on object status, progress, attack state, queue conditions, distance, and other filters.

Research follows the same broad transactional principle:

```text
RESEARCH DEMAND
 → COST
 → RESERVATION/ESCROW
 → CAN-RESEARCH
 → COMMAND
 → COMPLETION OBSERVATION
```

No universal FIFO priority should be invented without evidence.

---

# 13. Information / scouting OS

The current Operations scout rule is only a bootstrap.

Information acquisition must become a service:

```text
SCOUT_REQUEST
 → TARGET SELECTION
 → ROUTE / SAFETY
 → COMMAND
 → MOVEMENT OBSERVATION
 → INFORMATION GAIN
 → FRESHNESS UPDATE
 → RETASK / RECOVER
```

Failure classes include:

- target unavailable;
- scout idle;
- route invalid;
- threat blocked;
- scout lost;
- information stale;
- duplicate request;
- strategic target changed.

Information is valuable only when its freshness and confidence are represented.

---

# 14. Military OS

Military cognition must remain separate from military execution.

The service must eventually cover:

- production demand;
- endpoint allocation;
- grouping;
- reinforcement;
- posture;
- defense;
- attack;
- retreat;
- threat response;
- verification;
- recovery.

The strategic module decides **why**. Military OS decides **how to maintain the physical military state**.

Do not reproduce stock `tsa.per` blindly. Recover its behavioral contracts and build explicit AEGIS state around them.

---

# 15. Threat and safety model

Threat is not equivalent to task failure.

At minimum distinguish:

```text
TASK_INVALID
THREAT_BLOCKED
WORKER_UNAVAILABLE
COMMAND_FAILED
TARGET_LOST
SOURCE_FAILED
STRATEGY_OBSOLETE
```

Stock threat behavior is distributed across economy, livestock, construction, military and interaction systems. No universal civilian evacuation manager has been proven.

Therefore AEGIS should use a typed safety service:

```text
THREAT SNAPSHOT
      ↓
┌─────┴──────────────┐
│                    │
EXECUTABLE       THREAT-BLOCKED
│                    │
└─────────┬──────────┘
          ↓
      RECOVERY
```

Threat detection timing must not be assigned a fixed cycle/latency until measured.

---

# 16. Verification is a first-class state machine

The following are distinct:

```text
REQUESTED
≠ ADMITTED
≠ RESERVED
≠ AUTHORIZED
≠ COMMAND_ISSUED
≠ ENGINE_STATE_OBSERVED
≠ PRODUCTIVE
≠ VERIFIED
```

Examples:

```text
train villager ≠ villager exists
build stable ≠ stable operational
move scout ≠ information acquired
assign miner ≠ miner is productive
research tech ≠ tech completed
```

Every important service must expose evidence for the transition it claims.

---

# 17. Recovery architecture

All services must converge on typed failure handling.

```text
SERVICE REQUEST
      ↓
COMMAND
      ↓
OBSERVE
      ↓
SUCCESS ─────────→ CONFIRM
      │
      └─ FAILURE
           ↓
       CLASSIFY
           ↓
   ┌───────┼────────┐
   ▼       ▼        ▼
 RETRY   RESELECT  ESCALATE
   │       │        │
   └───────┴────────┘
           ↓
        REPLAN
```

Recovery must be bounded. AEGIS must never create infinite command/retry loops merely because a service remains unsatisfied.

Each recovery record requires:

```text
generation
service
request/object
failure-class
attempt-count
last-observed
retry-policy
disposition
```

---

# 18. Interpreter ABI: what remains unqualified

External references substantially reduce syntax/semantic uncertainty, but the following remain target-build questions until experimentally proven:

- exact rule-pass boundary;
- universal same-pass goal visibility;
- same-pass strategic-number visibility in every context;
- command side-effect visibility within the same evaluation context;
- exact backward-jump scheduling behavior;
- exact instruction/rule budget behavior;
- exact re-entry/quiescence behavior;
- timing of object-state refresh after commands;
- exact latency of census/state refresh;
- exact interaction between timers, jumps and rule traversal.

Do not design critical correctness around any of these until qualified.

---

# 19. ABI qualification program

Use a minimal target-build probe suite.

### Probe A — goal mutation

```text
Rule A: write goal X
Rule B: immediately read goal X
Rule C: read X after a forward jump
Rule D: read X after fall-through
```

### Probe B — strategic number mutation

Same structure for SN mutation.

### Probe C — command visibility

Issue a harmless command and determine when its object/action/order state becomes observable.

### Probe D — timer behavior

Measure enable/trigger/re-enable behavior across rule passes.

### Probe E — jump behavior

Use bounded forward and backward jumps with logging and official debugging instrumentation.

### Probe F — rule re-entry

Determine whether control returns to the expected location or restarts/continues according to a different interpreter boundary.

Every result must record:

```text
target build
script hash
probe hash
expected result
observed result
log evidence
interpretation
confidence
```

---

# 20. Engineering workflow

Every subsystem is built through four mandatory passes.

## Pass 1 — Forensics

- inspect untouched stock;
- inspect existing AEGIS;
- identify behavioral contracts;
- record negative findings;
- cross-reference external documentation.

## Pass 2 — Architecture

- define ownership;
- define state;
- define request/result contracts;
- define failure taxonomy;
- define generation/freshness semantics;
- identify ABI dependencies.

## Pass 3 — Implementation

- implement the smallest vertical slice;
- keep contracts explicit;
- avoid speculative optimization;
- maintain runtime load hygiene;
- archive important changes.

## Pass 4 — Adversarial qualification

- compiler/ABI review;
- systems architecture review;
- pro-player review;
- AoE2 AI engineering review;
- Byzantine-specialist review;
- adversarial QA review.

A subsystem does not become green because Pass 3 succeeds.

---

# 21. Qualification gates

### Gate 0 — Source integrity

- exact target build recorded;
- stock corpus untouched;
- runtime load graph known;
- no accidental Promisory dependency.

### Gate 1 — Static

- syntax;
- identifiers;
- parentheses;
- definitions;
- load graph;
- ABI range checks;
- no unintended compatibility aliases.

### Gate 2 — ABI

- every nontrivial primitive used by the module has sufficient evidence;
- unresolved semantics are isolated behind safe boundaries.

### Gate 3 — Dynamic

- module loads;
- expected commands issue;
- engine state changes as intended;
- verification sees the intended state.

### Gate 4 — Stress

- source depletion;
- worker interruption;
- threat;
- construction failure;
- production contention;
- stale demand;
- reservation conflict;
- repeated long-horizon operation.

### Gate 5 — Integration

- generation alignment;
- service ownership intact;
- no starvation;
- no runaway retries;
- cognition receives trustworthy state.

### Gate 6 — Long-horizon

- civilization remains functional over extended play;
- economy does not collapse under normal perturbations;
- infrastructure recovers;
- strategic state remains synchronized with physical state.

---

# 22. First implementation vertical slice

Do not attempt the entire civilization at once.

The first complete slice is:

```text
VILLAGER DEMAND
      ↓
HOUSING
      ↓
CIVILIZATION CENSUS
      ↓
WORKER TARGETS
      ↓
FOOD / WOOD DEMAND
      ↓
SOURCE + DROPSITE SERVICEABILITY
      ↓
WORKER SELECTION
      ↓
TASK COMMAND
      ↓
ENGINE OBSERVATION
      ↓
PRODUCTIVITY MEASUREMENT
      ↓
FAILURE / RECOVERY
```

This slice deliberately exercises the deepest substrate without requiring a complete military AI.

It is the first architectural proof that AEGIS can control a living civilization rather than merely issue isolated commands.

---

# 23. Migration plan for current AEGIS

## Phase A — Freeze cognition

Preserve:

- Foundation;
- Belief;
- Situation;
- Objectives;
- Planning;
- Decision;
- Commitment.

Only change their interfaces when required by the new state/service contracts.

## Phase B — Replace Operations bootstrap

Remove strategic ownership from static Operations percentages.

Operations becomes a service layer.

## Phase C — Build Civilization State

Implement reconciliation for:

1. population;
2. villagers;
3. buildings;
4. stockpiles;
5. pending production;
6. source/service state.

## Phase D — Build economy

Implement:

1. demand;
2. arbitration;
3. logical reservation;
4. worker targets;
5. source selection;
6. tasking;
7. measurement;
8. recovery.

## Phase E — Build construction

Implement persistent construction lifecycle and recovery.

## Phase F — Production/technology

Integrate endpoint arbitration, escrow, authorization and verification.

## Phase G — Information

Replace scout bootstrap with typed information requests and freshness.

## Phase H — Military

Build physical military substrate around existing strategic cognition.

## Phase I — Long-horizon integration

Only after civilian substrate is stable should the project optimize higher-level strategy aggressively.

---

# 24. What must not be done

Never:

- copy the entire stock AI into AEGIS;
- load Promisory as a runtime dependency;
- treat external documentation as target-build proof;
- treat a building count as operational capability;
- treat command issuance as success;
- treat `object-data-tasks-count` as universal capacity;
- treat food as a homogeneous worker category;
- treat a worker role as immutable identity;
- treat threat as generic task failure;
- treat logical reservation as engine escrow without proof;
- depend on unqualified same-pass mutation visibility;
- use fixed latency assumptions without measurement;
- create giant relative-jump control structures merely because stock does;
- optimize before lifecycle correctness;
- call static qualification runtime qualification;
- archive only successes; negative findings are first-class engineering evidence;
- create machine backups as a substitute for GitHub/project history.

---

# 25. Research policy after the research freeze

Broad archaeology is paused.

Targeted research is **mandatory** when any of these conditions holds:

- an unresolved ABI fact can invalidate implementation;
- two authoritative sources conflict;
- runtime evidence contradicts stock/source expectations;
- a failure cannot be classified;
- a new subsystem requires an uncharacterized engine primitive;
- a qualification result cannot be reproduced.

Every new research pass must answer:

```text
What question?
What evidence?
What changed?
What did not change?
What architecture is affected?
What is still unqualified?
```

This prevents research from becoming an infinite project phase.

---

# 26. Documentation law

Every meaningful finding must be preserved in GitHub.

Forensics belong under:

`docs/forensics/`

Architecture belongs under:

`docs/`

Runtime corrections belong in the runtime-corrections ledger and the affected source.

Every major report should contain:

- scope;
- exact target build;
- evidence;
- source locations;
- external references;
- interpretation;
- confidence;
- negative findings;
- implementation consequence;
- unresolved questions.

No important discovery should exist only in chat history.

---

# 27. Current project truth

The current AEGIS runtime has a strong cognitive skeleton and multiple statically qualified modules. It is **not yet a fully qualified civilization operating system**.

The current state is therefore:

```text
COGNITIVE ARCHITECTURE      → STRONG
STATIC ABI DISCIPLINE       → STRONG / CONTINUING
CIVILIZATION SUBSTRATE      → INCOMPLETE
ECONOMIC SCHEDULER          → REBUILD REQUIRED
WORKER ALLOCATION            → REBUILD REQUIRED
RESOURCE LOGISTICS           → REBUILD REQUIRED
CONSTRUCTION OS              → REBUILD REQUIRED
PRODUCTION ARBITRATION       → ARCHITECTURE DEFINED / IMPLEMENTATION INCOMPLETE
INFORMATION OS               → BOOTSTRAP ONLY
MILITARY OS                  → SUBSTRATE INCOMPLETE
VERIFICATION                 → EXPANDING
RECOVERY                     → EXPANDING
TARGET-BUILD RUNTIME ABI     → PARTIALLY QUALIFIED
LONG-HORIZON QUALIFICATION   → NOT YET ACHIEVED
```

This is not failure. It is the correct engineering boundary discovered by the forensic phase.

---

# 28. Definition of success

AEGIS is not complete when it can:

- make a good strategic decision;
- train a unit;
- assign villagers;
- win a short scripted test.

AEGIS is complete when it can maintain a coherent civilization state and continuously close the loop:

```text
OBSERVE
 ↓
MODEL
 ↓
ASSESS
 ↓
DEMAND
 ↓
ARBITRATE
 ↓
RESERVE
 ↓
EXECUTE
 ↓
OBSERVE RESULT
 ↓
VERIFY
 ↓
RECOVER
 ↓
LEARN / REPLAN
 ↓
OBSERVE AGAIN
```

for the duration of a real game, including normal disruptions.

The standard is therefore **closed-loop civilization control**, not isolated tactical cleverness.

---

# 29. Immediate next work

The research phase is closed except for targeted ABI questions.

The engineering queue is:

1. qualify the target-build interpreter probes;
2. implement Civilization State for population/civilians/infrastructure;
3. implement villager production + housing lifecycle;
4. implement worker target/allocation service;
5. implement source/dropsite serviceability;
6. implement food/wood tasking;
7. implement verification and recovery for that slice;
8. adversarially qualify the vertical slice;
9. expand to construction;
10. expand to production/technology;
11. expand information/scouting;
12. expand military substrate;
13. reconnect and retune strategic cognition;
14. begin long-horizon qualification.

No new strategic cleverness should outrun the substrate.

---

# 30. Final engineering doctrine

> **AEGIS is a closed-loop civilization control system.**
>
> Strategy supplies intent.  
> Arbitration resolves competing intent.  
> Reservations protect scarce resources.  
> Services turn intent into physical work.  
> The engine is the authority on what actually happened.  
> Civilization State reconciles that reality.  
> Verification proves outcomes.  
> Recovery handles failure.  
> Cognition receives the resulting world and plans again.

That loop is the product.

Everything else is implementation detail.
