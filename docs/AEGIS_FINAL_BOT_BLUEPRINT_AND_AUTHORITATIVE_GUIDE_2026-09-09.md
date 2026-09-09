# AEGIS / ByzBot — Final Bot Blueprint & Authoritative Engineering Guide

**Date:** 2026-09-09  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652  
**Status:** Authoritative project blueprint for final-bot design; implementation remains gated by machine/ABI qualification  
**Authority:** `CANONICAL_AUTHORITY.md`  
**Primary historical source:** verified stock `AI (HD version).per` + verified Promisory closure  
**Runtime authority:** current target-build machine evidence  
**Scope:** independent AEGIS Byzantine AI; pure `.per`; no XS

---

## 0. Purpose

This document is the controlling blueprint for what the finished AEGIS Byzantine bot must know, decide, authorize, execute, verify, recover from, and continuously reassess.

It is deliberately **not** a claim that every listed subsystem has already been implemented or runtime-qualified. It is the design and coverage target against which implementation is measured.

The governing rule is:

> **Cross-reference the historical AI before designing the AEGIS equivalent, then cross-reference the current target-build ABI before writing runtime code. Never convert an inference into an engine fact.**

The blueprint therefore separates:

1. **Historical evidence** — what HD/Promisory actually does.
2. **Machine evidence** — what the target DE build actually accepts and means.
3. **AEGIS design** — what the independent bot should do.
4. **Qualification state** — what has or has not been proven at runtime.

No `.per` implementation is authorized merely because the architecture is plausible.

---

# 1. Non-negotiable architecture

AEGIS is independent of stock AI.

```text
                         AoE2DE ENGINE
                              |
                +-------------+-------------+
                |                           |
           STOCK AI / HD                AEGIS-BYZ
            archaeology                  TARGET
                |                           |
        historical evidence          independent design
                |                           |
                +-------- ENGINE ABI -------+
```

Stock HD/Promisory is **reference material**, not:

- an intelligence parent;
- a runtime dependency;
- a state authority;
- a hidden planner;
- a source of live AEGIS state.

AEGIS must remain capable of standing alone with a minimal independent `.ai` root and its own reachable `.per` closure.

Permanent constraints:

- Pure `.per`; XS is outside scope.
- Scenario-loader automation is retired and must not be reopened.
- CADE is secondary validation infrastructure.
- Hidden/native test-harness activation is not assumed to be available on retail.
- Invasive runtime instrumentation is not part of the core qualification path.
- Prototypes are evidence, not production authority.
- No production stub, placeholder, invented primitive, or unqualified numeric channel.

---

# 2. Evidence law

## 2.1 Two independent evidence axes

### Machine/runtime authority

`A1 exact installed target package/build`  
`>` `A2 verified immutable package snapshot`  
`>` `A3 byte/content-equivalent repository snapshot`  
`>` `A4 historical/source material`  
`>` `A5 inference`

Only A1–A3 can clear numeric ABI allocation.

### Strategic archaeology

Use the repository evidence taxonomy:

- **DIRECT** — source visibly establishes the relationship.
- **COMPOSED** — multiple direct relationships form the chain.
- **INFERRED** — strategic meaning reconstructed from behavior/context.
- **AEGIS-GENERALIZATION** — project-owned design derived from evidence.
- **UNCERTAIN** — evidence is insufficient.

Never promote UNCERTAIN or INFERRED evidence to engine fact.

## 2.2 Completion ladder

Every important operation must preserve the distinction:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

A command is not completion proof. Validator acceptance is not engine-semantic proof. Aggregate replay change is not automatically object lineage.

## 2.3 State envelope

Any cross-module state publication must carry:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Controller time and world time are separate dimensions.

---

# 3. Final strategic control loop

The final bot is a closed-loop strategic controller:

```text
WORLD
 ↓
OBSERVE
 ↓
CLASSIFY / BELIEVE
 ↓
DETECT TRANSITION
 ↓
DEFINE OBJECTIVE
 ↓
DERIVE REQUIREMENTS
 ↓
GENERATE CAPABILITY CANDIDATES
 ↓
EVALUATE COST / TIMING / POSITION / INFORMATION / RISK
 ↓
COMMIT
 ↓
AUTHORIZE
 ↓
EXECUTE
 ↓
OBSERVE RESULT
 ↓
VERIFY POSTCONDITION
 ↓
CLASSIFY SUCCESS / PARTIAL / FAILURE / UNKNOWN
 ↓
RECOVER / RE-ARBITRATE
 ↓
UPDATE BELIEFS
 ↓
REASSESS
```

This is the architectural spine. Every vertical slice must demonstrate the same lifecycle at the appropriate scale.

---

# 4. What the final bot must model

The strategic state space is not a single score. It is a bounded portfolio of interacting state domains:

- Economy
- Production
- Military
- Technology
- Map
- Position
- Information
- Timing
- Infrastructure
- Logistics
- Reserves
- Threats
- Commitments
- Opportunities
- Confidence
- Initiative
- Tempo
- Population / housing
- Civilian lifecycle
- Resource-source lifecycle
- Production capacity
- Force readiness
- Recovery state
- Transition state

The final bot must distinguish **world state** from **belief state**, and both from **decision state**.

---

# 5. Historical lessons that constrain the design

The verified HD/Promisory archaeology establishes a recurring programmer pattern:

`OBSERVE → MEASURE → COMPRESS INTO STATE → GUARD → ACT → RESET/TRANSITION → RE-ENTER CONTROLLER`

Concrete recovered mechanisms include:

- escrowed age research and protected resource commitments;
- contextual gatherer allocation;
- production authorization and feasibility gating;
- threat classification;
- search/candidate evaluation through persistent scratch state;
- geometric scout/path/waypoint logic;
- attack → retreat → restart lifecycle;
- fortification-aware attack suppression/defer behavior;
- building placement/rebuild fallback;
- timers and persistent state used for temporal hysteresis;
- pending-state checks to avoid duplicate asynchronous actions;
- ally/enemy population and cooperation/tribute state;
- trade and late-game economic transitions;
- resignation/terminal policy;
- difficulty/execution scaling separate from strategic intent.

These are historical findings, not a claim that the final AEGIS implementation should copy the same rule layout.

The historical strategic problem matrix is the controlling checklist for this section and must remain linked to direct source evidence before implementation.

---

# 6. Final capability blueprint — 20 major vertical slices

The previous 14-slice plan was too compressed. It omitted or buried important RTS capability domains, most notably monk operations and several basic economic/logistics/defensive functions.

The current blueprint therefore uses **20 major vertical slices**, plus cross-cutting qualification/hardening.

These are a **coverage target**, not a claim that the number 20 is mathematically final. The HD capability-coverage audit must be kept open until every meaningful historical capability is mapped or explicitly classified as not applicable/unsupported.

## Slice 1 — Foundation / Game-State Control Loop

Must establish:

- one coherent observation generation;
- state ownership and publication;
- controller/world time separation;
- validity and generation handling;
- bounded update cadence;
- stale-state detection;
- deterministic module contracts;
- minimal independent `.ai` closure.

Historical cross-reference: distributed measurement, state, timers, guards, and re-entry.  
AEGIS requirement: one coherent world-model publication rather than duplicated speculative state.

## Slice 2 — Opening Economy / Age Advancement

Must cover:

- initial worker production;
- housing continuity;
- early food acquisition;
- wood/gold/stone setup;
- resource-source transitions;
- age-up prerequisites;
- escrow/commitment protection;
- transition timing;
- post-transition reallocation.

Historical cross-reference: age research, escrow, gatherer allocation, villager production, housing, early food and source transitions.

## Slice 3 — Civilian Lifecycle

Must cover the complete civilian lifecycle:

`CREATE → AVAILABLE → ASSIGN → WORK → REASSIGN → IDLE → RECOVER/REPAIR → DEATH → REPLACEMENT`

Capabilities include:

- worker census;
- role classification;
- assignment;
- task selection;
- task command;
- productivity observation;
- idle recovery;
- death/replacement accounting;
- builder lifecycle;
- support for military/economic transitions.

Historical cross-reference: villager production, gatherer allocation, building, repair, work-state handling, and production continuity.

## Slice 4 — Resource Economy

Must model:

- food;
- wood;
- gold;
- stone;
- stock;
- inflow;
- committed stock;
- near-term demand;
- source availability;
- source depletion/transition;
- resource opportunity cost.

Economic control is an output of strategic demand, not a static villager ratio.

## Slice 5 — Economic Logistics

Must cover the physical/logistical side of gathering:

- dropsites;
- source serviceability;
- travel distance;
- source safety;
- worker saturation;
- farm/fishing/hunting transitions;
- effective gather rate;
- infrastructure required to maintain income.

Historical cross-reference: dropsite/building rules, gatherer allocation, source transitions, water/fishing behavior.

## Slice 6 — Market / Resource Conversion / Trade

Must cover:

- market access;
- buying/selling feasibility;
- resource conversion;
- trade;
- trade-route economics where applicable;
- opportunity cost;
- late-game economic regime changes.

Historical cross-reference: trade and conversion subsystems. Exact primitive semantics remain machine-qualified separately.

## Slice 7 — Construction & Infrastructure

Must cover:

- building prerequisites;
- builder selection;
- placement candidate generation;
- placement feasibility;
- infrastructure purpose;
- rebuild/repair;
- defensive placement;
- production infrastructure;
- alternate placement/recovery.

This slice remains behind the explicit construction ABI qualification boundary. Do not pretend construction is runtime-qualified merely because static architecture exists.

## Slice 8 — Production Director

Must be the central production authority.

```text
CAPABILITY DEMAND
 → DEFICIT
 → PRODUCER CANDIDATES
 → RESOURCE LOAD
 → QUEUE / CAPACITY ANALYSIS
 → ARBITRATION
 → AUTHORIZED PRODUCTION REQUEST
 → EXECUTION BRIDGE
 → EVIDENCE
```

No strategic module should directly bypass this plane to train military units.

Must cover:

- civilian production;
- military production;
- siege production;
- monk production;
- unique units;
- queue pressure;
- production capacity;
- prerequisites;
- resource reservations;
- switch cost;
- pending transactions;
- replacement production.

## Slice 9 — Cavalry Threat Containment

First intended executable vertical slice.

```text
ENEMY OBSERVATION
 → CAVALRY BELIEF
 → CONTAINMENT OBJECTIVE
 → CAPABILITY DEMAND
 → DEFICIT
 → PRODUCTION LOAD
 → ARBITRATION
 → EXECUTION
 → WORLD EVIDENCE
 → VERIFICATION
 → RECOVERY / RE-ARBITRATION
```

The required capability is not necessarily “build camels.” Candidate response classes may include:

`COUNTER_UNIT | FORTIFICATION | MOBILITY | POSITIONAL_DENIAL | ECONOMIC_RELOCATION | RETREAT | COUNTER_ATTACK | TECHNOLOGY | DELAY`

The candidate set is AEGIS design; historical evidence establishes threat-driven response and production coupling, not this exact taxonomy.

## Slice 10 — Infantry / Ranged Warfare

Must cover capability response to:

- infantry pressure;
- archer/ranged pressure;
- mixed compositions;
- mobility interactions;
- counters and counter-counters;
- production transition;
- tactical positioning;
- ranged/melee engagement constraints.

Do not hard-code a single unit-to-unit lookup as the complete military model.

## Slice 11 — Siege Warfare

Must cover:

- siege capability acquisition;
- anti-siege response;
- defensive structure pressure;
- siege escort/support;
- target priority;
- siege vulnerability;
- fortification transitions;
- timing windows.

Historical cross-reference: fortification detection, siege/rams/trebuchets production, attack suppression/defer logic.

## Slice 12 — Monastic / Monk Operations

This is a dedicated capability domain, not a technology footnote.

Must cover:

- monastery prerequisites;
- monk production;
- healing;
- relic detection;
- relic collection;
- relic transport;
- relic return/deposit;
- conversion;
- conversion target selection;
- monk positioning;
- monk survival/retreat;
- support of armies;
- reserve monks;
- monastery technology interactions;
- technology-dependent capability changes.

Technology interactions must include, where supported by current game data and qualified engine semantics, the relevant monastery technologies such as Redemption, Atonement, Heresy, Sanctity, Fervor, Illumination, Faith, and Theocracy.

The blueprint does **not** claim that all of these exact behaviors were reconstructed from one historical HD code block. Their inclusion is required by the actual AoE2 capability surface; historical source archaeology must be used to determine what the HD AI did with them.

## Slice 13 — Scouting / Exploration / Map Knowledge

Must cover:

- scout production/assignment;
- exploration;
- waypoint generation;
- route safety;
- target-region selection;
- resource discovery;
- enemy-base discovery;
- military-information acquisition;
- scout survival;
- information-return value.

Historical cross-reference: scout groups, path analysis, quartersteps, pivot/candidate points, waypoint selection, performance constraints.

## Slice 14 — Information / Belief / Fog-of-War

Must separate:

- observed facts;
- stale facts;
- inferred facts;
- hypotheses;
- confidence;
- alternative explanations;
- invalidation conditions.

Must model information value:

`INFORMATION GAP → VALUE OF INFORMATION → OBSERVATION ACTION → NEW EVIDENCE → BELIEF UPDATE`

Never treat predicted enemy behavior as observed behavior.

## Slice 15 — Battlefield Force Composition

Must cover:

- desired force composition;
- current effective force;
- damaged/ineffective force;
- deployed force;
- reserve force;
- pending force;
- committed force;
- capability deficit/surplus;
- composition transition;
- replacement demand.

Core invariant:

`effective capability + deficit >= required capability`

with nonnegative quantities and explicit generation/evidence.

## Slice 16 — Battlefield Command

Must cover:

- movement;
- attack;
- attack-move;
- target selection;
- formation;
- patrol;
- regroup;
- retreat;
- pursuit;
- positional control;
- tactical objective transitions.

Attack is a lifecycle, not a Boolean:

`PREPARE → AUTHORIZE → MOVE → ENGAGE → ASSESS → CONTINUE / CHANGE / REGROUP / RETREAT → RESET → REASSESS`

Historical cross-reference: attack-goal, attack-status, retreat-now, restart-attack, timers, fortification suppression/defer behavior.

## Slice 17 — Garrison / Defense / Emergency Response

Must cover:

- defensive garrison;
- civilian protection;
- emergency response;
- town-bell-like responses where appropriate;
- exposed-resource response;
- defensive structures;
- emergency retreat;
- evacuation/redeployment;
- defensive reinforcement.

Historical evidence must be used to distinguish actual stock behavior from AEGIS extensions.

## Slice 18 — Naval / Water Operations

Must cover the separate water theater:

- docks;
- fishing;
- naval production;
- transport;
- military naval groups;
- naval positioning;
- retreat;
- naval attack;
- transport logistics;
- water-map economy;
- water-map transitions.

Historical cross-reference: watercontrol, fishing/transport/naval group state, map-dependent production and behavior.

## Slice 19 — Technology / Research / Strategic Transitions

Must cover:

- research prerequisites;
- resource feasibility;
- escrow;
- technology priority;
- age transition;
- military/economic technology investment;
- technology-dependent capability changes;
- completion verification;
- post-transition reallocation.

Technology is a capability investment, not a shopping list.

## Slice 20 — Strategic Director / Full Byzantine Integration

This is the highest-level controller.

It must arbitrate among:

- economic growth;
- military pressure;
- defense;
- technology;
- scouting/information;
- monks/relics;
- water theater;
- construction;
- trade;
- recovery;
- timing;
- reserves;
- opponent transitions;
- initiative and tempo.

Every candidate decision must be expressible as:

`STATE + UNCERTAINTY + OBJECTIVE + AVAILABLE ACTIONS`

→

`SELECTED ACTION + EXPECTED CONSEQUENCE + RISK + FAILURE SIGNATURE + RECOVERY PATH`

The Strategic Director does not execute engine commands. It establishes priorities and authorizations consumed by subordinate capability directors.

---

# 7. Cross-cutting capabilities — mandatory in every relevant slice

The following are not optional “extra features.” They recur across the entire bot:

### Population / housing

Prevent housed production, forecast housing demand, build housing before critical production stalls, and verify actual capacity changes.

### Idle-time management

Idle civilians are lost economic throughput. Idle state must be observed, classified, corrected, and measured.

### Repair / maintenance

Repair is a capability-preservation action. It competes for worker time and may be less valuable than replacement or retreat depending on context.

### Death / replacement

Every persistent worker/army requirement must account for attrition and replacement demand.

### Timing / tempo

A resource-efficient action can be strategically wrong if it misses a timing window.

### Reserves

Do not commit all available capability to the immediate objective if reserve capacity materially changes failure risk.

### Failure / recovery

Every action class requires explicit failure signatures and recovery paths.

### Hysteresis

Recent decisions, timers, commitments, and transition state must prevent pathological rule oscillation.

### Search discipline

Candidate searches must bound scope, cost, iteration count, state lifetime, reset behavior, and early exit.

### Performance budget

A correct decision that starves the rule engine of time needed for higher-value control is not acceptable.

---

# 8. Capability-demand architecture

The final bot must distinguish **what capability is required** from **how to obtain it**.

Required flow:

```text
OBJECTIVE
   ↓
CAPABILITY DEMAND
   ↓
REQUIRED STRENGTH
   ↓
CURRENT EFFECTIVE STRENGTH
   ↓
QUALIFYING PENDING / COMMITTED STRENGTH
   ↓
DEFICIT / SURPLUS
   ↓
PRODUCTION / TECHNOLOGY / POSITION / OTHER CANDIDATES
```

A capability-demand record should contain, at minimum:

- capability identity;
- owner;
- generation;
- valid/stale state;
- stage;
- required strength;
- minimum/target/maximum where appropriate;
- current effective strength;
- available strength;
- deployed strength;
- damaged/ineffective strength;
- qualifying pending strength;
- committed strength;
- resulting deficit/surplus;
- urgency;
- confidence;
- evidence provenance;
- observation timestamp/generation.

This is an AEGIS design contract, not a claim that HD used this exact object.

---

# 9. Production authority

The final production plane is:

```text
FORCE / CIVILIAN REQUIREMENT
          ↓
   PRODUCTION DIRECTOR
          ↓
   DEFICIT / LOAD MODEL
          ↓
      ARBITRATION
          ↓
 PRODUCER / QUEUE SELECTION
          ↓
 AUTHORIZED PRODUCTION REQUEST
          ↓
   EXECUTION BRIDGE ONLY
          ↓
       ENGINE
          ↓
 OBSERVATION / EVIDENCE / VERIFY
```

No module outside the Execution Bridge may perform the final engine-facing production side effect.

This corrects the current prototype defect where final-named execution rules can reach directly into `can-train` / `train`.

---

# 10. Verification and recovery contract

Verification must never be reduced to “the command ran.”

For each operation define:

1. issuance evidence;
2. acceptance/queue evidence if observable;
3. pending evidence;
4. world-state creation evidence;
5. availability evidence;
6. deployment evidence;
7. effectiveness evidence;
8. strategic postcondition.

If evidence is unavailable, retain **UNKNOWN** rather than fabricating a successful transition.

Recovery must classify:

- transient failure;
- invalidated objective;
- resource conflict;
- producer unavailable;
- target invalidated;
- timing window lost;
- world-state mismatch;
- stale decision;
- repeated failure.

Retry must carry explicit transaction/generation identity. Sentinel resets are prototype mechanisms and cannot become production semantics without qualification.

---

# 11. First implementation sequence

The final bot is not built by implementing the 20 slices in arbitrary order.

The dependency order is:

1. **Freeze symbolic contracts.**
2. **Acquire immutable current stock/runtime package evidence.**
3. **Complete typed ABI inventory and collision audit.**
4. **Clear numeric allocation.**
5. **Build independent observation/world-state surface.**
6. **Build coherent generation publication.**
7. **Build belief/situation/objective contracts.**
8. **Build capability-demand/deficit contract.**
9. **Build Production Director.**
10. **Build Execution Bridge.**
11. **Build conservative evidence-backed verification.**
12. **Build bounded recovery/re-arbitration.**
13. **Implement Slice 9 — Cavalry Threat Containment.**
14. **Qualify it end-to-end.**
15. **Expand capability families one slice at a time.**
16. **Integrate Strategic Director only after subordinate capability planes are reliable.**
17. **Run whole-bot closure/QC.**

Do not write a byte of production `.per` merely to make the architecture look complete.

---

# 12. HD capability coverage audit requirement

The 20-slice list is not considered complete until the verified HD/Promisory corpus has been enumerated by **capability**, not merely by file name or strategy label.

For every meaningful historical capability, record:

| Field | Required content |
|---|---|
| Historical source | exact file/module |
| Source mechanism | rule/search/state/command family |
| Game problem | what problem it solves |
| Observation | what it measures |
| State | what it persists |
| Guard | what blocks action |
| Action | what it commands |
| Postcondition | what outcome is checked |
| Recovery | what happens on failure |
| Vertical slice | exactly one primary slice |
| Evidence level | DIRECT / COMPOSED / INFERRED / etc. |
| Machine qualification | status on current target build |
| AEGIS treatment | copy concept / generalize / reject / TBD |

**No historical capability may be silently dropped because it does not fit the current architecture.** If a capability cannot be mapped, either the blueprint must gain another slice or the capability must be explicitly classified as non-applicable/unsupported with evidence.

This audit is the authoritative closure mechanism for the question “does the final bot cover everything worth learning from AI (HD)?”

The answer is **not yet declared complete** until this audit closes.

---

# 13. Current known gaps / explicit non-claims

The following remain open and must not be represented as solved:

- complete A1 stock-package immutable manifest;
- final numeric ABI clearance;
- exact target-build semantics for every proposed primitive;
- construction runtime qualification;
- complete world-observation implementation;
- individual lifecycle evidence beyond currently proven replay evidence;
- producer identity / queue transaction identity;
- complete HD capability inventory;
- runtime certification of the first vertical slice;
- final monk implementation semantics;
- complete water/naval runtime qualification;
- complete tactical target-selection qualification;
- full-bot performance budget qualification.

Open does not mean impossible. It means **not yet proven**.

---

# 14. Prototype salvage policy

Prototype modules may contribute:

- algorithmic ideas;
- state-field candidates;
- control-flow patterns;
- failure/recovery concepts;
- architectural experiments;
- known negative results.

They may not contribute automatically:

- numeric ABI allocations;
- assumed engine semantics;
- direct production authority;
- completion claims;
- stock-state ownership;
- unqualified construction behavior;
- hidden runtime dependencies.

The current vertical-slice gap analysis already identifies the major prototype defects that must not be carried forward.

---

# 15. Final acceptance standard

AEGIS is “final” only when all of the following are true:

### Architecture

- every major capability has an owner;
- every cross-module contract has generation/validity/evidence;
- strategic intent is separated from execution;
- recovery is explicit;
- no universal speculative state manager has emerged.

### Historical coverage

- every meaningful HD capability is mapped;
- source evidence is traceable;
- historical fact and AEGIS generalization remain distinct;
- no important capability is omitted without an explicit disposition.

### Machine qualification

- target build is fingerprinted;
- stock package is immutable and hashed;
- import closure is known;
- ABI inventory is complete;
- collision audit is complete;
- numeric channels are cleared;
- required primitives are target-build qualified.

### Runtime

- independent `.ai` closure is valid;
- observation works;
- decisions use current evidence;
- commands pass through authorized bridges;
- postconditions are observed;
- unknown remains unknown;
- failures recover without state corruption;
- no duplicate asynchronous transactions are created.

### Strategic behavior

- economy adapts to capability demand;
- military responds to capability, not just unit identity;
- monks are operationally integrated;
- scouting produces information value;
- technology changes capability models;
- naval operations are a real theater;
- defense and emergency response exist;
- attacks have lifecycle and retreat/restart behavior;
- construction has fallback;
- trade/resource conversion is strategic;
- timing, reserves, initiative, and tempo affect decisions;
- the bot continuously reassesses instead of executing a static build order.

---

# 16. Immediate project directive

The correct next engineering artifact is **not another `.per` module**.

It is the **HD Capability Coverage Audit**: a source-backed inventory that walks the complete verified `AI (HD version).per` + Promisory closure and maps every meaningful capability into this blueprint.

Only after that audit is materially closed should the project declare the 20-slice architecture complete.

Then the machine gate remains:

`STOCK SNAPSHOT → IMPORT CLOSURE → ABI INVENTORY → COLLISION AUDIT → ABI FREEZE → .per IMPLEMENTATION`

And the implementation gate remains:

`OBSERVE → BELIEVE → OBJECTIVE → DEMAND → DEFICIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER → REASSESS`

**This document is the design target. The evidence ledgers decide what is proven.**
