# AEGIS / ByzBot — Master Plan

**Last reconciled:** 2026-09-09  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652  
**Scope:** independent Byzantine AI, pure `.per`, no XS  
**Authority:** `CANONICAL_AUTHORITY.md`  
**Role:** **single current planning/design authority for the final AEGIS bot**

> This is the one active plan. Historical forensic documents, machine evidence, external sources, experiments, and prototypes are evidence records—not competing plans.

---

# 1. Governing rule

**Cross-reference stock `AI (HD version).per` and the Promisory closure before designing the AEGIS equivalent. Cross-reference the current target-build machine evidence before writing runtime code. Never generalize `.per` from Lisp-like syntax, and never infer undocumented side effects from vocabulary alone.**

The project separates four kinds of truth:

1. **Historical evidence** — what HD/Promisory source actually does.
2. **Machine evidence** — what the target DE build accepts and means.
3. **AEGIS design** — what the independent Byzantine controller should do.
4. **Qualification status** — what is proven, open, blocked, or merely proposed.

---

# 2. Non-negotiable boundaries

- AEGIS is independent of stock AI.
- Stock HD/Promisory is archaeology/reference material, not a runtime parent, intelligence dependency, or live state authority.
- Pure `.per`; XS is outside scope.
- Scenario-loader automation is retired and must not be reopened.
- CADE/CaptureAge is secondary validation infrastructure, not primary authority.
- Construction remains a runtime ABI qualification boundary until directly proven.
- Prototypes/experiments are evidence, not production authority.
- No production stubs, placeholders, invented primitives, invented numeric channels, or copied `final` prototypes without qualification.
- No PR is merged without explicit authorization.
- Do not reopen broad Layer-1 archaeology merely because an interesting unknown remains; pursue targeted evidence only when it changes implementation correctness.

---

# 3. Current status

| Area | Status | Meaning |
|---|---|---|
| Layer 1 — machine/runtime archaeology | **89% / frozen** | Broad archaeology is closed for handoff; targeted ABI questions remain only where implementation requires them. |
| Layer 2 — HD/Promisory archaeology | **Major reconstruction; targeted source closure OPEN** | Strategic/programmer model is strong, but meaningful capability closure is not yet fully line-anchored. |
| Layer 3 — AEGIS architecture | **Established / active qualification** | This master plan is the current design authority. |
| Layer 4 — production `.per` | **BLOCKED** | Requires applicable machine/ABI clearance and frozen symbolic contracts. |
| First executable vertical slice | **Cavalry Threat Containment** | Architecture target only; implementation remains gated. |

**Hard-QC verdict:** the 20-slice architecture survives. The missing material is not another collection of top-level domains; it is explicit cross-cutting control machinery and source-anchored operational coverage.

---

# 4. External-source QC baseline

Current online corroboration confirms several important constraints:

- The current AoE2DE depot exposes `AI (HD version).per` plus a substantial Promisory/AiBuilder module family. The depot inventory is useful corroboration, but filename presence is **not** semantic proof. citeturn0search0
- Community AI scripting sources confirm that advanced `.per` files can be substantially more complicated than AI-builder abstractions and that existing scripts are normally inspected directly rather than mechanically converted. This supports our decision to treat source archaeology as primary. citeturn1search0
- Public scripting examples demonstrate persistent goals, timers, random state, strategic numbers, and explicit reset/re-entry patterns. They are corroboration only; stock source remains the authority for historical behavior. citeturn1search2turn1search6
- Official patch notes demonstrate that the AI scripting surface itself changes over time—for example new facts/commands and AI fixes—so target-build qualification must remain separate from historical HD archaeology. citeturn0search9
- Public community reports show that small changes in AI script state/logic can materially change attack, resignation, and competitiveness behavior. These are anecdotal, not strategic authority. citeturn0search8turn1search3

**QC conclusion:** online sources strengthen the methodology and identify additional areas to audit, but none supersedes the verified installed stock package or project evidence.

---

# 5. Final architecture

## 5.1 System boundary

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

## 5.2 Strategic loop

```text
WORLD
→ OBSERVE
→ CLASSIFY / BELIEVE
→ DETECT TRANSITION
→ SELECT REGIME
→ DEFINE OBJECTIVE
→ DERIVE CAPABILITY REQUIREMENTS
→ GENERATE CANDIDATES
→ SEARCH / EVALUATE COST + TIMING + POSITION + INFORMATION + RISK
→ COMMIT
→ AUTHORIZE
→ EXECUTE
→ OBSERVE RESULT
→ VERIFY POSTCONDITION
→ SUCCESS / PARTIAL / FAILURE / UNKNOWN
→ RECOVER / RE-ARBITRATE
→ UPDATE BELIEFS
→ REASSESS
```

No module may turn intention directly into assumed world state.

## 5.3 Cross-cutting control plane

```text
                    STRATEGIC DIRECTOR
                           |
                  REGIME / TRANSITION
                           |
       +-------------------+-------------------+
       |                   |                   |
 RESOURCE CONTROL      SEARCH SERVICE      EXECUTION POLICY
       |                   |                   |
       +-------------------+-------------------+
                           |
                  20 CAPABILITY SLICES
                           |
        OBSERVE → AUTHORIZE → COMMAND → VERIFY
                           |
                 RESET / RECOVER / REASSESS
```

### Regime

A `REGIME` carries identity, generation, entry/exit conditions, protected commitments, enabled/suppressed capability families, resource posture, timing posture, transition state, and recovery path.

`OPENING`, `TRANSITION`, `ECONOMIC_BUILD`, `MILITARY_PRESSURE`, `DEFENSE`, `RECOVERY`, `WATER`, `LATE_GAME`, and `TERMINAL` are AEGIS design categories, not claims that HD uses those exact names.

### Transition

`PRE → COMMIT → IN_PROGRESS → COMPLETE_DETECTED → REALLOCATE → STABILIZE`, with timeout/failure/recovery.

### Resource control

`RAW STOCK → CONTROLLED STOCK → COMMITTED / PROTECTED STOCK → AVAILABLE SPEND`.

Represent reserves, anticipated demand, strategic commitments, emergency conversion authority, expenditure restrictions, release conditions, and stale-commitment invalidation. This is an AEGIS model derived from historical escrow/resource-control behavior, not a claim that HD stored this exact object.

### Search service

`RESET → INITIALIZE → ENUMERATE → MEASURE → HARD-GUARD → SCORE → PRESERVE-BEST → ADVANCE → TERMINATE → RETURN`.

Search state must carry generation/scope/cursor/constraints/measurements/score/uncertainty/budget/invalidation.

### Execution policy

Separate strategic intent from execution cadence, search depth, candidate count, reaction latency, aggressiveness, retry budget, communication frequency, and rule-budget consumption. Difficulty must not silently alter strategic-state semantics.

---

# 6. Evidence law

## Machine authority

`A1 exact installed target package/build > A2 immutable verified package snapshot > A3 byte/content-equivalent repository snapshot > A4 historical/source material > A5 inference`.

Only A1–A3 can clear numeric ABI allocation.

## Strategic evidence

- **DIRECT** — source visibly establishes the relationship.
- **COMPOSED** — multiple direct facts establish a chain.
- **INFERRED** — strategic meaning reconstructed from behavior/context.
- **AEGIS-GENERALIZATION** — project-owned design derived from evidence.
- **UNCERTAIN** — insufficient evidence.

Never promote inference to engine fact.

## Completion ladder

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`.

A command is not completion proof. Validator acceptance is not automatically engine-semantic proof. Replay aggregate change is not automatically object lineage.

## State envelope

Every cross-module publication carries:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`.

Controller time and world time remain separate.

---

# 7. HD/Promisory findings that are now architectural requirements

The verified historical corpus repeatedly shows:

`OBSERVE → MEASURE → COMPRESS INTO STATE → GUARD → ACT → RESET / TRANSITION → RE-ENTER CONTROLLER`.

Confirmed/recovered mechanism families include:

- escrowed age research and protected expenditure;
- contextual gatherer allocation;
- production authorization and feasibility gating;
- threat classification;
- persistent scratch-state candidate search;
- scout/path/waypoint geometry and safety search;
- attack → retreat → restart;
- fortification-aware attack suppression/defer;
- building placement/rebuild fallback;
- timers and persistent state for temporal hysteresis;
- pending-state checks against duplicate asynchronous work;
- ally/enemy population, cooperation, tribute, and communication state;
- trade and late-game economic transitions;
- resignation/terminal policy;
- difficulty/execution scaling;
- initialization and state setup;
- specialized food/hunting control;
- research/technology/upgrades;
- water/fishing/naval behavior.

The verified HD root closure is:

`Promisory/defaultConstants → Promisory/finalingConstants → Promisory/finaling`.

The public depot inventory corroborates a broader module family including `boarhunting`, `buildings`, `escrow`, `gatherers`, `general`, `interaction`, `researches`, `resign`, `scoutcontrol`, `threats`, `trade`, and water-related modules. Again: inventory is corroboration, not semantics. citeturn0search0

### Hard-QC additions to the historical model

The HD audit must not stop at strategic labels. It must explicitly trace the mundane machinery underneath them:

1. civilian creation, queue, housing, idle, death, replacement;
2. builder selection/release and repair-capable workers;
3. food-source lifecycle: herdables, boar, huntables, farms, fishing, depletion, dropsite transitions;
4. infrastructure creation, serviceability, destruction and replacement;
5. unit/technology queue continuity and upgrades;
6. target invalidation and command deduplication;
7. garrison/ungarrison and emergency response;
8. monks: production, healing, relics, conversion, retreat and technology dependencies;
9. siege production, escort, anti-siege and recovery;
10. water economy, naval operations and transport/amphibious logistics;
11. market/trade/conversion and late-game resource regimes;
12. ally cooperation, tribute, requests/taunts/operator interfaces;
13. terminal/resignation/hopeless-state behavior;
14. difficulty as execution policy rather than strategic-state corruption;
15. timer, reset, scratch-state, stale-state, fallback, and performance hygiene.

These are **coverage requirements**, not claims that every behavior is already reconstructed.

---

# 8. Final capability blueprint — 20 slices

## 1 — Foundation / Game-State Control Loop

World observation generation, ownership, publication, controller/world time, validity, generations, stale-state handling, bounded cadence, deterministic contracts, independent `.ai` closure.

## 2 — Opening Economy / Age Advancement

Villager production, housing, early food, wood/gold/stone setup, source transitions, age prerequisites, escrow, transition timing, post-transition reallocation.

## 3 — Civilian Lifecycle

`CREATE → QUEUE → AVAILABLE → ASSIGN → WORK → REASSIGN → IDLE → RECOVER/REPAIR → DEATH → REPLACEMENT`.

Worker census, roles, task command, productivity observation, idle recovery, builder lifecycle, repair-capable workers, emergency reassignment, replacement accounting.

## 4 — Resource Economy

Food/wood/gold/stone, stock, inflow, controlled/protected stock, commitments, near-term demand, source availability/depletion, opportunity cost, resource-control posture.

## 5 — Economic Logistics

Dropsites, camps/mills/docks, serviceability, travel, safety, saturation, source transitions, effective gather rate, infrastructure continuity and replacement.

## 6 — Market / Resource Conversion / Trade

Market access, buy/sell feasibility, emergency conversion, trade routes/units where applicable, route safety, opportunity cost, late-game resource regimes.

## 7 — Construction & Infrastructure

Prerequisites, builder selection, placement search, feasibility, authorization, completion, defensive construction, walling/containment, economic/production/technology infrastructure, rebuild, alternate placement, repair/recovery.

**Construction remains runtime/ABI-unqualified until proven.**

## 8 — Production Director

`CAPABILITY DEMAND → DEFICIT → PRODUCER CANDIDATES → RESOURCE LOAD → QUEUE/CAPACITY → ARBITRATION → AUTHORIZED PRODUCTION → EXECUTION BRIDGE → EVIDENCE`.

Civilians, military, siege, monks, unique units, queues, capacity, prerequisites, reservations, switching, pending transactions, upgrades, replacement.

No strategic module trains units directly.

## 9 — Cavalry Threat Containment

First intended executable slice:

`ENEMY OBSERVATION → CAVALRY BELIEF → OBJECTIVE → CAPABILITY DEMAND → DEFICIT → RESPONSE CANDIDATES → ARBITRATION → EXECUTION → WORLD EVIDENCE → VERIFY → RECOVER`.

Candidate response classes may include counter-unit, fortification, mobility, positional denial, economic relocation, retreat, counterattack, siege, technology, or delay. This is AEGIS design, not a historical claim.

## 10 — Infantry / Ranged Warfare

Infantry/ranged pressure, mixed compositions, mobility interactions, counters/counter-counters, production transitions, positioning, engagement constraints, replacement/recovery.

## 11 — Siege Warfare

Siege production/prerequisites, escort, target selection, vulnerability, anti-siege, fortification pressure, timing, retreat/recovery, replacement.

## 12 — Monastic / Monk Operations

Monastery prerequisites/construction, monk production/queues, healing targets/positioning, relic discovery/assignment/pickup/transport/deposit, conversion targeting/timing, survival/retreat, escort, reserves, monastery technologies.

Game capability surface must remain distinct from what HD actually did; source anchors determine historical behavior.

## 13 — Scouting / Exploration / Map Knowledge

Scout production/assignment, exploration, route safety, waypoints, target regions, resource/enemy discovery, military information, survival, information value, geometric search.

## 14 — Information / Belief / Fog-of-War

Observed facts, stale facts, inferred facts, hypotheses, confidence, alternatives, invalidation, information gaps, value-of-information, observation actions, belief updates.

`Predicted enemy behavior ≠ observed enemy behavior.`

## 15 — Battlefield Force Composition

Desired/current effective force, damaged/ineffective, deployed, reserve, pending, committed, deficit/surplus, transitions, replacement.

Invariant: `effective capability + deficit >= required capability`.

## 16 — Battlefield Command

Movement, attack, attack-move, target selection, formation, patrol, regroup, pursuit, retreat, positional control, tactical transitions.

`PREPARE → AUTHORIZE → MOVE → ENGAGE → ASSESS → CONTINUE / CHANGE / REGROUP / RETREAT → RESET → REASSESS`.

## 17 — Garrison / Defense / Emergency Response

Garrison/ungarrison, civilian protection, exposed-resource response, defensive structures, emergency retreat/evacuation/redeployment, reinforcement, economic defense, appropriate emergency response.

## 18 — Naval / Water Operations

Fishing economy, docks, naval production, transports, naval groups, movement, attack, retreat, unloading/army delivery, water-map economy, land/water transitions, amphibious logistics.

## 19 — Technology / Research / Strategic Transitions

Age advancement, economic/military/unit-line/civilization/monastery technologies, prerequisites, escrow, queue conflicts, opportunity cost, completion verification, capability changes, post-transition reallocation.

## 20 — Strategic Director / Full Byzantine Integration

Arbitrates economic growth, military pressure, defense, technology, information, monks/relics, water, construction, trade, recovery, timing, reserves, opponent transitions, initiative and tempo.

Strategic Director decides/authorizes; it does not directly execute engine-facing commands.

---

# 9. Universal lifecycle and control-plane requirements

Every slice must explicitly account for:

1. idle-time management;
2. death/replacement;
3. repair/maintenance;
4. housing/population continuity;
5. queue continuity;
6. upgrade continuity;
7. target invalidation;
8. command deduplication;
9. timers/cooldowns/temporal hysteresis;
10. generation/stale-state handling;
11. search reset/scratch-state isolation;
12. performance/rule-budget management;
13. emergency mode;
14. recovery mode;
15. terminal-state handling;
16. communication/operator-control isolation;
17. transition reallocation;
18. asynchronous completion verification;
19. explicit unknown state where evidence is insufficient.

Universal operational contract:

`OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → CAPABILITY STATE → AUTHORIZE → COMMAND → PENDING → WORLD EVIDENCE → VERIFY → RECOVER/RECOMMIT`.

---

# 10. Historical coverage closure ledger

Historical coverage remains **OPEN** until every meaningful HD/Promisory capability relevant to the target is source-anchored.

Required trace:

`FILE → LINE/RULE/FUNCTION → OBSERVATION → STATE WRITE → STATE READER → GUARD → ACTION → POSTCONDITION → FAILURE → RECOVERY → STRATEGIC PURPOSE → AEGIS OWNER`.

Priority order:

| Priority | Family | Owner | Status |
|---:|---|---|---|
| P0 | regime/transition selection | 1 / 19 / 20 | OPEN |
| P0 | resource control/protected expenditure | 4 / 6 / 19 | OPEN |
| P0 | civilian production/housing/idle/death/replacement | 2 / 3 / 8 | OPEN |
| P0 | food-source lifecycle | 2 / 4 / 5 | OPEN |
| P0 | infrastructure/dropsite replacement | 5 / 7 | OPEN |
| P0 | production authorization/queue continuity | 8 | OPEN |
| P0 | target/search/invalidation | 10 / 13 / 16 | OPEN |
| P0 | attack/retreat/restart | 16 | OPEN |
| P1 | monks/relic/conversion/healing | 12 | OPEN |
| P1 | siege/fortification | 11 / 16 / 17 | OPEN |
| P1 | water/fishing/transport/naval | 18 | OPEN |
| P1 | market/trade/conversion | 6 | OPEN |
| P1 | ally/tribute/cooperation/communication | 20 | OPEN |
| P1 | technology/research/age transitions | 19 | OPEN |
| P1 | difficulty/execution scaling | execution policy | OPEN |
| P1 | resignation/terminal behavior | terminal controller | OPEN |

A row becomes **CLOSED** only when exact source anchors, executable mechanism, separated interpretation, AEGIS owner, current-build requirements, unresolved semantics, and behavior preservation are all recorded.

If something does not fit a slice:

`MISSING SLICE → CAPABILITY → SOURCE EVIDENCE → ARCHITECTURAL FAILURE`.

---

# 11. Machine / ABI gate

Historical closure does not authorize code.

Required sequence:

`IMMUTABLE STOCK SNAPSHOT → IMPORT CLOSURE → COMPLETE SYMBOL/REFERENCE INVENTORY → CHANNEL OCCUPANCY → WRITER/READER MATRIX → ENGINE/VALIDATOR JOIN → ABI DECISIONS → ABI FREEZE`.

Current machine evidence includes thousands of declaration/operation records, hundreds of shared numeric values, and many goal/SN/timer channels. Numeric emptiness is not sufficient ABI clearance.

Binding principles:

- exact token/identifier semantics matter;
- `.per` is not generalized Lisp;
- goal channels and strategic-number channels have distinct semantics;
- parser acceptance does not prove engine reservation/meaning;
- pending-object/research-status evidence is stronger when directly stock-proven;
- construction remains qualification-gated;
- compatibility shims require evidence before production use.

---

# 12. Symbolic/state contracts and authority

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

Production authority:

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

No strategic module bypasses this path for direct military production.

---

# 13. First executable vertical slice

## Cavalry Threat Containment

Required chain:

`ENEMY OBSERVATION → THREAT BELIEF → CONTAINMENT OBJECTIVE → CAPABILITY DEMAND → CURRENT EFFECTIVE CAPABILITY → DEFICIT → RESOURCE/QUEUE/PRODUCER FEASIBILITY → ARBITRATION → AUTHORIZED REQUEST → EXECUTION BRIDGE → WORLD EVIDENCE → VERIFY → RECOVER/RE-ARBITRATE`.

Invariant:

`effective capability + deficit >= required capability`.

Do not implement until exact existing AEGIS/world-state fields for current, pending, deployed and effective force are identified and the applicable machine ABI is clear. The old direct `can-train camel-line` shortcut is not the final architecture.

---

# 14. Prototype salvage policy

Prototype material is mined for concepts, not promoted wholesale. Candidate salvage includes civilian/economic demand, arbitration, civilization-state reconciliation, worker census/productivity, recovery lifecycle, and execution/verification separation.

Machine `*-final` names do not make artifacts final. Machine/repository byte differences require reconciliation. Construction prototypes remain qualification boundaries.

---

# 15. Definition of done

The final bot is done only when:

- every required capability has a primary owner;
- every relevant historical capability is traced or explicitly classified;
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
- independent `.ai`/`.per` closure is clean;
- the bot operates without stock AI intelligence as a dependency.

Final invariant:

`WORLD → BELIEF → REGIME → OBJECTIVE → CAPABILITY → RESOURCE/SEARCH EVALUATION → COMMITMENT → AUTHORIZATION → EXECUTION → WORLD EVIDENCE → VERIFICATION → RECOVERY → REASSESSMENT`.

---

# 16. Current next actions — no new plan documents

### Phase A — Historical source closure

Perform the exact HD/Promisory source-anchor pass in this order:

1. regime/transition selection;
2. resource-control/protected expenditure;
3. civilian production/housing/idle/death/replacement;
4. food-source lifecycle;
5. infrastructure/dropsite replacement;
6. production authorization/queues/upgrades;
7. target search/invalidation;
8. attack/retreat/restart;
9. monks/relics/healing/conversion;
10. siege/fortification;
11. water/fishing/transport/naval;
12. market/trade/conversion;
13. ally/tribute/cooperation/communication;
14. research/technology/age transitions;
15. difficulty/execution scaling;
16. resignation/terminal behavior.

### Phase B — First-slice machine gate

Clear only the symbols/channels needed by Slice 9 and its supporting substrate from the immutable target package.

### Phase C — Contract freeze

Freeze ownership, generation, lifecycle, evidence, command authority, verification, recovery, and numeric allocations.

### Phase D — First production `.per`

Only after A–C clear. Minimal, fully qualified, directly traceable to evidence.

### Phase E — Vertical qualification

Validate:

`OBSERVE → BELIEVE → OBJECTIVE → DEMAND → DEFICIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER → REASSESS`.

No scenario-loader automation.

### Phase F — Expansion

Add slices while preserving the same control plane and evidence law.

### Phase G — Byzantine optimization

Only after the capability substrate is reliable, optimize Byzantine-specific priorities, initiative, tempo, reserves, timing, and multi-domain tradeoffs.

---

# 17. Document governance

**There is exactly one current AEGIS plan: this file.**

Do not create another blueprint, addendum, reconciliation, revised plan, or competing roadmap.

When new evidence changes the design:

1. update this master plan;
2. preserve underlying forensic evidence in the appropriate evidence layer when necessary;
3. update the relevant status/ledger here;
4. do not create a second planning authority.

Historical dated documents may remain as provenance records. They do not become current design authority.
