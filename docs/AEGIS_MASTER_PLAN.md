# AEGIS / ByzBot — Master Plan

**Last reconciled:** 2026-09-09  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652  
**Scope:** independent Byzantine AI, pure `.per`, no XS  
**Authority:** `CANONICAL_AUTHORITY.md`  
**Role:** **single current planning/design authority for the final AEGIS bot**

> This file replaces the previous chain of dated blueprint, capability-audit, red-team, and reconciliation documents as the project's **one active plan**. Historical forensic documents remain evidence records; they are not competing plans.

---

## 1. What this plan is

This is the controlling answer to:

- What are we building?
- What must the final bot be capable of?
- What architecture governs it?
- What did the historical HD/Promisory AI teach us?
- What remains unproven?
- What must happen next?
- What gates must clear before production `.per` is written?

The plan is deliberately separated into four kinds of truth:

1. **Historical evidence** — what the stock HD/Promisory source actually does.
2. **Machine evidence** — what the target DE build actually accepts and means.
3. **AEGIS design** — what the independent bot should do.
4. **Qualification status** — what is currently proven, open, or blocked.

No architectural idea becomes engine fact merely because it is elegant. No production `.per` is written until its required primitives, symbols, channels, and side effects have been qualified.

### Governing rule

**Cross-reference stock `AI (HD version).per` before designing the AEGIS equivalent. Cross-reference the current target-build machine evidence before writing runtime code. Never generalize `.per` from Lisp-like syntax or assume undocumented side effects.**

---

# 2. Non-negotiable project boundaries

- AEGIS is independent of stock AI.
- Stock HD/Promisory is archaeology/reference material, not a runtime parent, intelligence dependency, or live state authority.
- Pure `.per`; XS is outside scope.
- Scenario-loader automation is retired and must not be reopened.
- CADE/CaptureAge is secondary validation infrastructure, not the primary authority.
- Retail hidden/native test-harness capabilities are not assumed.
- Construction remains a runtime ABI qualification boundary until directly proven.
- Prototypes and experiments are evidence only; they are not production authority.
- No production stubs, placeholders, invented primitives, invented numeric channels, or copied `final` prototypes without qualification.
- No PR is merged without explicit authorization.
- Do not reopen broad Layer-1 archaeology merely because an interesting unknown remains; pursue targeted evidence only when it changes implementation correctness.

---

# 3. Current project state

| Area | Status | Meaning |
|---|---|---|
| Layer 1 — machine/runtime archaeology | **89% / frozen** | Broad archaeology is closed for handoff; targeted ABI questions remain only where implementation requires them. |
| Layer 2 — HD/Promisory archaeology | **Major reconstruction closed; targeted source closure OPEN** | The strategic/programmer model is strong, but every meaningful capability is not yet line-anchored. |
| Layer 3 — AEGIS architecture | **Established / active qualification** | This master plan is the current design authority. |
| Layer 4 — production `.per` | **BLOCKED** | Requires applicable machine/ABI clearance and frozen symbolic contracts. |
| First executable vertical slice | **Cavalry Threat Containment** | Architecture target only; implementation is still gated. |

### Current architectural conclusion

The **20-slice decomposition remains valid**. The red-team pass did not justify adding arbitrary top-level slices. Instead, it exposed a cross-cutting control plane that must exist across all slices:

`REGIME / TRANSITION + RESOURCE CONTROL + SEARCH SERVICE + EXECUTION POLICY + CONTROL-PLANE HYGIENE`

This is now part of the master architecture, not a separate addendum.

---

# 4. Final architecture

## 4.1 System boundary

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

Stock AI answers historical questions such as **how programmers used the machine**. AEGIS independently answers **what a Byzantine strategic controller should decide**.

## 4.2 Strategic control loop

```text
WORLD
  ↓
OBSERVE
  ↓
CLASSIFY / BELIEVE
  ↓
DETECT TRANSITION
  ↓
SELECT REGIME
  ↓
DEFINE OBJECTIVE
  ↓
DERIVE CAPABILITY REQUIREMENTS
  ↓
GENERATE CANDIDATES
  ↓
SEARCH / EVALUATE COST + TIMING + POSITION + INFORMATION + RISK
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
SUCCESS / PARTIAL / FAILURE / UNKNOWN
  ↓
RECOVER / RE-ARBITRATE
  ↓
UPDATE BELIEFS
  ↓
REASSESS
```

No module is allowed to turn an intention directly into an assumed world-state change.

## 4.3 Cross-cutting control plane

```text
                    STRATEGIC DIRECTOR
                           |
                  REGIME / TRANSITION
                           |
        +------------------+------------------+
        |                  |                  |
  RESOURCE CONTROL     SEARCH SERVICE     EXECUTION POLICY
        |                  |                  |
        +------------------+------------------+
                           |
                  20 CAPABILITY SLICES
                           |
        OBSERVE → AUTHORIZE → COMMAND → VERIFY
                           |
                 RESET / RECOVER / REASSESS
```

### Regime model

A `REGIME` is the current strategic operating mode. It must carry identity, generation, entry/exit conditions, protected commitments, enabled/suppressed capability families, resource posture, timing posture, transition state, and recovery path.

Architectural categories such as `OPENING`, `TRANSITION`, `ECONOMIC_BUILD`, `MILITARY_PRESSURE`, `DEFENSE`, `RECOVERY`, `WATER`, `LATE_GAME`, and `TERMINAL` are AEGIS design categories, **not claims that HD uses those exact names**.

### Transition model

Major transitions use:

`PRE → COMMIT → IN_PROGRESS → COMPLETE_DETECTED → REALLOCATE → STABILIZE`

with timeout/failure/recovery semantics.

This applies to age transitions, economic source transitions, military composition changes, emergency-to-normal recovery, water/land operating changes, and attack/retreat/re-engagement transitions where applicable.

### Resource-control model

Never collapse resources into one number. Distinguish:

`RAW STOCK → CONTROLLED STOCK → COMMITTED / PROTECTED STOCK → AVAILABLE SPEND`

The model must represent protected reserves, anticipated demands, strategic commitments, emergency conversion authority, expenditure restrictions, release conditions, and stale-commitment invalidation.

### Search service

Search is a reusable bounded engine service, not a scouting-only trick:

`RESET → INITIALIZE → ENUMERATE → MEASURE → HARD-GUARD → SCORE → PRESERVE-BEST → ADVANCE → TERMINATE → RETURN`

Search state must carry generation/scope/cursor/constraints/measurements/score/uncertainty/budget/invalidation semantics.

### Execution policy

Separate **strategic intent** from execution behavior. Execution policy may constrain observation cadence, search depth, candidate count, reaction latency, aggressiveness, retry budget, communication frequency, and rule-budget consumption. Difficulty must not silently change strategic-state semantics.

---

# 5. Evidence law

## 5.1 Machine/runtime authority

`A1 exact installed target package/build > A2 immutable verified package snapshot > A3 byte/content-equivalent repository snapshot > A4 historical/source material > A5 inference`

Only A1–A3 can clear numeric ABI allocation.

## 5.2 Strategic evidence

- **DIRECT** — source visibly establishes the relationship.
- **COMPOSED** — multiple direct facts establish a chain.
- **INFERRED** — strategic meaning reconstructed from behavior/context.
- **AEGIS-GENERALIZATION** — project-owned design derived from evidence.
- **UNCERTAIN** — insufficient evidence.

Never promote inference to engine fact.

## 5.3 Execution completion ladder

Every asynchronous operation must preserve:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

A command is not completion proof. Validator acceptance is not automatically engine-semantic proof. Replay aggregate change is not automatically object lineage.

## 5.4 State envelope

Cross-module state publication requires:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Controller time and world time remain separate.

---

# 6. What HD/Promisory has taught us so far

The verified historical corpus shows a recurring engineering pattern:

`OBSERVE → MEASURE → COMPRESS INTO STATE → GUARD → ACT → RESET / TRANSITION → RE-ENTER CONTROLLER`

Recovered historical mechanisms include:

- escrowed age research and protected resource commitments;
- contextual gatherer allocation;
- production authorization and feasibility gating;
- threat classification;
- persistent scratch-state candidate search;
- geometric scout/path/waypoint selection;
- attack → retreat → restart lifecycle;
- fortification-aware attack suppression/defer behavior;
- building placement/rebuild fallback;
- timers and persistent state for temporal hysteresis;
- pending-state checks against duplicate asynchronous work;
- ally/enemy population and cooperation/tribute state;
- trade and late-game economic transitions;
- resignation/terminal policy;
- difficulty/execution scaling.

The stock root's verified closure includes:

- `Promisory/defaultConstants`
- `Promisory/finalingConstants`
- `Promisory/finaling`

The shipped source family also exposes dedicated operational areas including initialization, boar hunting, buildings, escrow, gatherers, general search/state machinery, interaction, research, resignation, scouting, threats, trade, upgrades/technology, and water behavior. **Filename presence is corroboration only; exact semantics require source anchors.**

### Historical lessons that are now architectural requirements

1. State is a compressed control surface, not merely a log.
2. Guards precede side effects.
3. Search occurs before commitment when candidate choice matters.
4. Transitions reset or invalidate old state.
5. Controllers re-enter after asynchronous operations.
6. Resource control protects future capability, not merely current spending.
7. Performance/search cost is part of correctness in a bounded rule engine.
8. Communication is a control interface, not world-state evidence.
9. Terminal/resignation behavior is part of the controller.
10. Difficulty/execution scaling belongs below strategic intent.

---

# 7. Final capability blueprint — 20 vertical slices

The following are the **coverage and implementation targets**. They are not claims that each slice is already implemented or historically closed.

## 1 — Foundation / Game-State Control Loop

World observation generation, ownership, publication, controller/world time, validity, generations, stale-state handling, bounded cadence, deterministic contracts, independent `.ai` closure.

## 2 — Opening Economy / Age Advancement

Villager production, housing continuity, early food, wood/gold/stone setup, source transitions, age prerequisites, escrow, transition timing, post-transition reallocation.

## 3 — Civilian Lifecycle

`CREATE → QUEUE → AVAILABLE → ASSIGN → WORK → REASSIGN → IDLE → RECOVER/REPAIR → DEATH → REPLACEMENT`.

Includes worker census, role classification, task command, productivity observation, idle recovery, builder lifecycle, repair-capable workers, emergency reassignment, and replacement accounting.

## 4 — Resource Economy

Food/wood/gold/stone, stock, inflow, controlled/protected stock, commitments, near-term demand, source availability/depletion, opportunity cost, resource-control posture.

## 5 — Economic Logistics

Dropsites, camps/mills/docks, serviceability, travel, safety, saturation, source transitions, effective gather rate, infrastructure continuity, replacement after loss.

## 6 — Market / Resource Conversion / Trade

Market access, buy/sell feasibility, emergency conversion, trade routes/units where applicable, route safety, opportunity cost, late-game resource regimes.

## 7 — Construction & Infrastructure

What/when, prerequisites, builder selection, placement search, feasibility, authorization, completion, defensive construction, walling/containment, economic/production/technology infrastructure, rebuild, alternate placement, repair and recovery.

**Construction remains explicitly ABI/runtime-unqualified until proven.**

## 8 — Production Director

Central production authority:

`CAPABILITY DEMAND → DEFICIT → PRODUCER CANDIDATES → RESOURCE LOAD → QUEUE/CAPACITY → ARBITRATION → AUTHORIZED PRODUCTION → EXECUTION BRIDGE → EVIDENCE`

Covers civilians, military, siege, monks, unique units, queues, capacity, prerequisites, reservations, switching, pending transactions, upgrades, and replacement.

No strategic module bypasses this authority for direct military production.

## 9 — Cavalry Threat Containment

First intended executable slice:

`ENEMY OBSERVATION → CAVALRY BELIEF → OBJECTIVE → CAPABILITY DEMAND → DEFICIT → PRODUCTION/ALTERNATIVE RESPONSE → ARBITRATION → EXECUTION → WORLD EVIDENCE → VERIFY → RECOVER`

Potential response classes include counter-unit, fortification, mobility, positional denial, economic relocation, retreat, counterattack, technology, or delay. This taxonomy is AEGIS design, not a historical claim.

## 10 — Infantry / Ranged Warfare

Infantry/ranged pressure, mixed compositions, mobility interactions, counters/counter-counters, production transitions, positioning, engagement constraints, replacement and recovery.

## 11 — Siege Warfare

Siege production/prerequisites, escort, target selection, vulnerability, anti-siege, fortification pressure, timing, retreat/recovery, replacement.

## 12 — Monastic / Monk Operations

Monastery prerequisites/construction, monk production/queues, healing targets and positioning, relic discovery/assignment/pickup/transport/deposit, conversion targeting/timing, survival/retreat, escort, reserve monks, monastery technologies and capability changes.

The game capability surface must be distinguished from what HD actually did; historical source anchors determine the latter.

## 13 — Scouting / Exploration / Map Knowledge

Scout production/assignment, exploration, route safety, waypoints, target regions, resource/enemy discovery, military information acquisition, survival, information value, geometric search.

## 14 — Information / Belief / Fog-of-War

Observed facts, stale facts, inferred facts, hypotheses, confidence, alternatives, invalidation, information gaps, value-of-information, observation actions, belief updates.

`Predicted enemy behavior ≠ observed enemy behavior.`

## 15 — Battlefield Force Composition

Desired/current effective force, damaged/ineffective, deployed, reserve, pending, committed, deficit/surplus, transitions, replacement.

Invariant:

`effective capability + deficit >= required capability`

with nonnegative quantities and explicit generation/evidence.

## 16 — Battlefield Command

Movement, attack, attack-move, target selection, formation, patrol, regroup, pursuit, retreat, positional control, tactical transitions.

Attack lifecycle:

`PREPARE → AUTHORIZE → MOVE → ENGAGE → ASSESS → CONTINUE / CHANGE / REGROUP / RETREAT → RESET → REASSESS`

## 17 — Garrison / Defense / Emergency Response

Garrison/ungarrison, civilian protection, exposed-resource response, defensive structures, emergency retreat/evacuation/redeployment, reinforcement, economic defense, and appropriate town-bell-like responses.

Historical source must distinguish stock behavior from AEGIS extension.

## 18 — Naval / Water Operations

Fishing economy, docks, naval production, transports, naval groups, movement, attack, retreat, unloading/army delivery, water-map economy, land/water transitions, amphibious logistics.

## 19 — Technology / Research / Strategic Transitions

Age advancement, economic/military/unit-line/civilization/monastery technologies, prerequisites, escrow, queue conflicts, opportunity cost, completion verification, capability changes, post-transition reallocation.

Technology is a capability investment, not a shopping list.

## 20 — Strategic Director / Full Byzantine Integration

Arbitrates economic growth, military pressure, defense, technology, information, monks/relics, water, construction, trade, recovery, timing, reserves, opponent transitions, initiative and tempo.

The Strategic Director decides and authorizes; it does not directly perform engine-facing commands.

---

# 8. Universal lifecycle requirements

Every slice must explicitly account for the mundane machinery that is easy to hide behind strategic labels.

### Universal requirements

1. Idle-time management.
2. Death/replacement management.
3. Repair/maintenance.
4. Housing/population continuity.
5. Queue continuity.
6. Upgrade continuity.
7. Target invalidation.
8. Command deduplication.
9. Timers/cooldowns/temporal hysteresis.
10. Generation and stale-state handling.
11. Search reset and scratch-state isolation.
12. Performance/rule-budget management.
13. Emergency mode.
14. Recovery mode.
15. Terminal-state handling.
16. Communication/operator-control isolation.

### Universal operational contract

`OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → CAPABILITY STATE → AUTHORIZE → COMMAND → PENDING → WORLD EVIDENCE → VERIFY → RECOVER/RECOMMIT`

A capability is not complete merely because its strategic objective exists.

---

# 9. Historical capability-closure ledger

Historical coverage is **OPEN** until each meaningful HD/Promisory capability has direct source anchors.

For every source family, the required trace is:

`FILE → LINE/RULE/FUNCTION → OBSERVATION → STATE WRITE → STATE READER → GUARD → ACTION → POSTCONDITION → FAILURE → RECOVERY → STRATEGIC PURPOSE → AEGIS OWNER`

### Priority closure order

| Priority | Family | Primary owner | Status |
|---:|---|---|---|
| P0 | strategy/regime selection and transitions | 1 / 19 / 20 | OPEN |
| P0 | resource-control / expenditure protection | 4 / 6 / 19 | OPEN |
| P0 | civilian production, housing, idle, death, replacement | 2 / 3 / 8 | OPEN |
| P0 | food-source lifecycle | 2 / 4 / 5 | OPEN |
| P0 | infrastructure/dropsite replacement | 5 / 7 | OPEN |
| P0 | production authorization / queue continuity | 8 | OPEN |
| P0 | target/search/invalidation | 10 / 13 / 16 | OPEN |
| P0 | attack/retreat/restart | 16 | OPEN |
| P1 | monks/relic/conversion/healing | 12 | OPEN |
| P1 | siege/fortification response | 11 / 16 / 17 | OPEN |
| P1 | water/fishing/transport/naval | 18 | OPEN |
| P1 | market/trade/conversion | 6 | OPEN |
| P1 | ally/tribute/cooperation/communication | 20 | OPEN |
| P1 | technology/research/age transitions | 19 | OPEN |
| P1 | difficulty/execution scaling | 20 / execution policy | OPEN |
| P1 | resignation/terminal behavior | 20 / terminal controller | OPEN |

### Closure rule

A row becomes **CLOSED** only when:

1. exact source anchors are identified;
2. executable mechanism is traced;
3. strategic interpretation is separated from source fact;
4. one primary AEGIS owner is assigned;
5. current-build machine requirements are identified;
6. unresolved semantics are recorded;
7. no important behavior is lost during abstraction.

If a capability cannot fit one of the 20 slices, record:

`MISSING SLICE → CAPABILITY → SOURCE EVIDENCE → ARCHITECTURAL FAILURE`

and revise this master plan before implementation.

---

# 10. Machine/ABI gate

Historical closure does not authorize code.

Required machine sequence:

`IMMUTABLE STOCK SNAPSHOT`
→ `IMPORT CLOSURE`
→ `COMPLETE SYMBOL / REFERENCE INVENTORY`
→ `CHANNEL OCCUPANCY`
→ `WRITER / READER MATRIX`
→ `ENGINE / VALIDATOR JOIN`
→ `ABI DECISIONS`
→ `ABI FREEZE`

Current known inventory scale includes thousands of numeric declaration/operation records and hundreds of shared numeric values; therefore **numeric emptiness is not sufficient evidence of safety**.

Known machine principles that remain binding include:

- exact token/identifier semantics matter;
- `.per` is not generalized Lisp;
- goal channels and strategic-number channels have distinct semantics;
- parser acceptance does not prove engine reservation/meaning;
- pending-object and research-status evidence are stronger when directly observed in stock source;
- construction remains qualification-gated;
- no invented compatibility shim is production authority without evidence.

---

# 11. Symbolic and state-contract rules

Before production implementation, freeze:

- state registry;
- owner of every mutable state field;
- generation semantics;
- lifecycle stages;
- evidence levels;
- cross-module publication contracts;
- numeric channel allocation;
- search-state allocation;
- timer allocation;
- command authority;
- verification authority;
- recovery authority.

### Ownership rule

Every mutable state field has exactly one authoritative writer/owner. Readers consume published state; they do not silently recreate competing versions.

### Production authority rule

```text
Force Planner
     ↓ capability demand
Production Director
     ↓ deficit/resource/queue arbitration
Execution Bridge
     ↓ engine-facing command
Engine
     ↓ world evidence
Observation / Verification
```

No strategic module trains units directly.

---

# 12. First executable vertical slice

## Cavalry Threat Containment

This remains the first intended production slice because it exercises the full architecture without requiring the entire final bot first.

### Required evidence chain

`ENEMY OBSERVATION`
→ `THREAT BELIEF`
→ `CONTAINMENT OBJECTIVE`
→ `CAPABILITY DEMAND`
→ `CURRENT EFFECTIVE CAPABILITY`
→ `DEFICIT`
→ `RESOURCE / QUEUE / PRODUCER FEASIBILITY`
→ `ARBITRATION`
→ `AUTHORIZED REQUEST`
→ `EXECUTION BRIDGE`
→ `WORLD EVIDENCE`
→ `VERIFY`
→ `RECOVER / RE-ARBITRATE`

### Capability-demand invariant

`effective capability + deficit >= required capability`

All quantities must be nonnegative and carry generation/evidence.

### Important restriction

Do **not** implement this slice until exact existing AEGIS/world-state fields for current, pending, deployed, and effective force are identified and the applicable machine ABI is clear.

The old direct `can-train camel-line` shortcut is not the final architecture.

---

# 13. Prototype salvage policy

Existing prototype material is mined for concepts, not promoted wholesale.

Potential salvage includes:

- civilian demand policy;
- economic demand;
- demand arbitration;
- civilization-state reconciliation;
- worker census/productivity concepts;
- recovery lifecycle;
- execution/verification separation.

Machine prototypes with names such as `*-final` are not automatically final. Byte differences between machine and repository versions mean they must be reconciled before reuse.

Construction prototypes remain qualification boundaries.

---

# 14. Repository organization

The repository now has one active plan. Everything else is evidence, procedure, implementation candidate, experiment, or institutional memory.

```text
CANONICAL_AUTHORITY.md       Governance authority

docs/AEGIS_MASTER_PLAN.md    ← ONE CURRENT FINAL-BOT PLAN

docs/MACHINE_EVIDENCE/       Machine/package/ABI evidence
03_HD_ARCHAEOLOGY/            Historical HD/Promisory evidence
04_LAYER3_ARCHITECTURE/       Architecture/ABI research and procedures
05_RUNTIME_CANDIDATE/         Replay/runtime research instruments
07_EXPERIMENTS/               Experimental material
12_RESEARCH/                  External/comparative research
knowledge/                    Durable atomic institutional memory
```

### Document rule

**Do not create another blueprint, addendum, reconciliation, or revised plan.**

If new evidence changes the design:

1. update this master plan;
2. record the underlying forensic evidence in the appropriate evidence directory if necessary;
3. update the status/ledger here;
4. do not create a competing planning document.

Historical dated documents may remain when they are genuine provenance records, but they are never current planning authority.

---

# 15. What happens next

The project is no longer waiting for another architecture brainstorm.

## Phase A — Close historical coverage

Perform the exact HD source-anchor pass in this order:

1. regime/transition selection;
2. resource-control and protected expenditure;
3. civilian production/housing/idle/death/replacement;
4. food-source lifecycle;
5. infrastructure and dropsite replacement;
6. production authorization/queues/upgrades;
7. target search/invalidation;
8. attack/retreat/restart;
9. monks/relics/healing/conversion;
10. siege/fortification response;
11. water/fishing/transport/naval;
12. market/trade/conversion;
13. ally/tribute/cooperation/communication;
14. research/technology/age transitions;
15. difficulty/execution scaling;
16. resignation/terminal behavior.

For each, produce source anchors and close or explicitly classify every meaningful capability.

## Phase B — Close the machine gate for the first slice

Use the immutable target package to clear only the symbols/channels actually needed by Slice 9 and its supporting substrate.

## Phase C — Freeze contracts

Freeze state ownership, generation, lifecycle stages, evidence levels, command authority, verification, recovery, and numeric allocations.

## Phase D — Write the first production `.per`

Only after A–C clear. Production code must be minimal, fully qualified, and directly traceable to evidence.

## Phase E — Qualify the vertical slice

Validate:

`OBSERVE → BELIEVE → OBJECTIVE → DEMAND → DEFICIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER → REASSESS`

No scenario-loader automation.

## Phase F — Expand slice by slice

Add the remaining capabilities while preserving the same control-plane and evidence laws.

## Phase G — Integration / Byzantine strategic optimization

Only after the underlying capability substrate is reliable should the Strategic Director optimize Byzantine-specific priorities, initiative, tempo, reserves, timing, and multi-domain tradeoffs.

---

# 16. Definition of done

The final AEGIS bot is not done because it has 20 modules or because it can issue commands.

It is done when:

- every required capability has a primary owner;
- every historical capability relevant to the target has been traced or explicitly classified;
- every production primitive is machine-qualified;
- every numeric channel is ABI-cleared;
- every mutable state field has one owner;
- asynchronous operations preserve lifecycle state;
- commands are verified against world evidence;
- failures have explicit recovery/re-arbitration;
- search is bounded and reset-safe;
- resource control protects future commitments;
- transitions invalidate/reallocate state correctly;
- communication is not mistaken for world state;
- terminal behavior is explicit;
- execution policy is separated from strategic intent;
- the independent `.ai`/`.per` closure is clean;
- the bot operates without stock AI intelligence as a dependency.

### Final invariant

**AEGIS is a closed-loop strategic controller, not a collection of rules.**

`WORLD → BELIEF → REGIME → OBJECTIVE → CAPABILITY → RESOURCE/SEARCH EVALUATION → COMMITMENT → AUTHORIZATION → EXECUTION → WORLD EVIDENCE → VERIFICATION → RECOVERY → REASSESSMENT`

That is the single plan.