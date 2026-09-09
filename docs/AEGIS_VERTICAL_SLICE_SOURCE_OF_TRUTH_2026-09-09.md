# AEGIS Vertical-Slice Source of Truth — 2026-09-09

**Status:** AUTHORITATIVE CONSOLIDATION / CONSTRUCTION CONTROL DOCUMENT
**Purpose:** Prevent loss, fragmentation, and accidental re-invention of research already completed across the AEGIS repository. This document is the governing index and blueprint for construction of every permanent vertical slice.
**Runtime:** Pure `.per`; no XS; Promisory is reference/source material only and must never be a runtime dependency.
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652.

## 0. Authority and precedence

This document does **not** replace the detailed forensic reports. It consolidates them into one construction-facing source of truth so that implementation and review begin from what AEGIS already knows.

Precedence:

1. Target-build runtime evidence.
2. Untouched target-build stock AI on the user's machine.
3. Direct ABI qualification.
4. Existing AEGIS static/runtime qualification.
5. Existing repository forensic research.
6. Official/community documentation.
7. Inference.

When this document conflicts with a detailed forensic artifact, the detailed artifact must be rechecked and this document corrected. Nothing is promoted merely because it appears here.

## 1. The central rule

**A vertical slice is complete only when its complete lifecycle is understood and implemented, not when its visible feature exists.**

Every slice uses this canonical lifecycle:

`OBSERVE/RECONCILE -> CLASSIFY/BELIEVE -> OBJECTIVE -> REQUIREMENTS -> CONSTRAINTS -> CANDIDATES -> EVALUATE -> COMMIT -> AUTHORIZE -> EXECUTE -> VERIFY -> FAILURE CLASSIFICATION -> RECOVERY/REPLAN -> BELIEF UPDATE -> REASSESS`

For executable operations, preserve the evidence ladder:

`INTENTION -> AUTHORIZED -> ISSUED -> ACCEPTED/QUEUED -> PENDING -> CREATED -> AVAILABLE -> DEPLOYED -> EFFECTIVE`

The distinction is mandatory. A command is not completion. A queue entry is not a created object. A created object is not an available capability. An available capability is not strategic success.

## 2. What the repository already knows

The existing repository already contains substantial lifecycle research. It must be reused rather than recreated. The authoritative architecture documents establish the following:

- Engine ABI and interpreter semantics are a separate qualification layer.
- World state must include spatial/entity relationships, not only scalar counts.
- Civilization state must reconcile population, workers, buildings, queues, stockpiles, age, technology, military state, and active requests.
- Economic control is a demand/reservation/arbitration problem, not a fixed-percentage problem.
- Economic Escrow separates strategic commitment, economic requirement, resource reservation, and execution authorization.
- Civilian lifecycle is already modeled as existence -> production authorization -> queue -> creation -> accounting -> allocation -> tasking -> interruption -> recovery -> replacement.
- Worker lifecycle research already covers census, role vectors, target selection, task command, task verification, productivity observation, interruption and recovery.
- Resource/dropsite serviceability, economic demand -> worker allocation, economic contention/preemption, and production arbitration are already documented.
- Production research already covers queue arbitration, multi-queue arbitration, queue saturation/failure recovery, commitment release/replacement, competing commitments, expiration/cooldowns/reassertion, same-pass arbitration/re-entry, and execution feedback.
- Construction is a state machine: request -> can-build -> placement -> foundation -> builder assignment -> progress -> completion/failure -> retry/replan.
- Information is an operating subsystem: scouting, exploration, enemy identification, resource/infrastructure discovery, military observation, freshness, threat interpretation and belief updates.
- Military is an operating system: production, composition, grouping, reinforcement, tasking, targeting, movement, local advantage, micro, defense, retreat, attack lifecycle, recovery and threat-specific responses.
- Threat processing includes interpreted military-strength models and cross-system consequences.
- Historical stock architecture contains timers, persistent state, searches, rule ordering, maintenance loops and distributed control effects that cannot be reconstructed from names alone.
- Cross-system lifecycle research already exists for object birth/lineage, production identity/command lineage, aggregate production observability, state deltas/entity lineage, controller overwrite priority, timer temporal state, strategic transitions, vertical world-state closure and cross-system control graphs.
- The repository already contains a complete civilization-substrate architecture guide and a master engineering guide. This document indexes them instead of competing with them.

## 3. Coverage states

Every capability in every slice receives exactly one current disposition:

- `MISSING` — not yet represented adequately.
- `DOCUMENTED` — architecture/research exists, implementation not established.
- `STATIC-ANALYZED` — source/ABI analysis complete enough to implement.
- `IMPLEMENTED` — AEGIS code exists.
- `STATIC-QUALIFIED` — implementation passes static/ABI checks.
- `RUNTIME-QUALIFIED` — demonstrated on the target build.
- `STRESS-QUALIFIED` — survives adversarial qualification.
- `HISTORICAL-ONLY` — found in broader stock source but not established as active in the relevant runtime closure.
- `ENGINE-OWNED` — state/semantics belong to the engine and are not AEGIS-owned.
- `UNRESOLVED` — evidence is insufficient or conflicting.

No higher status may be claimed without the evidence required by the lower status.

## 4. Existing evidence that must not be forgotten

### 4.1 Civilization substrate

The Civilization Substrate Guide establishes the operating stack:

`Engine ABI -> World/Spatial State -> Civilization State -> Economic Scheduler -> Civilian Operations -> Construction OS -> Information OS -> Military OS -> Technology OS -> AEGIS cognition`

It explicitly identifies continuous villager production, housing continuity, idle-villager recovery, resource-role accounting, food-source selection/transition, dropsite dependencies, construction placement/builder management, production queues, scouting continuity, emergency recovery/garrison behavior and research continuity as mundane services that keep strategy executable.

### 4.2 Economic control

Known model:

`Strategic demand -> resource demand vector -> reservation/escrow -> worker targets -> discrete allocation -> site/task selection -> execution -> measured income -> model update`

Known safeguards include food continuity, housing lead time, age-up reservation, military-production reservation, technology reservation, construction reservation, emergency liquidity, allocation hysteresis, reassignment limits, stale-demand expiration and generation matching.

Food is a portfolio: herdables, forage/berries, boar, deer/hunt, farms, fishing where applicable, and civilization/map-specific sources. Effective food value must account for walking, drop distance, setup cost, risk, depletion and infrastructure.

### 4.3 Construction

Construction must retain purpose, requester, priority, placement policy, urgency/deadline, builder budget, reservation identity, retry count, generation and failure disposition. Foundation existence is not completion.

### 4.4 Production and lifecycle

Production must distinguish request, eligibility, site, feasibility, queue/command, pending state, completion, stock/capability realization and later deployment. Queue arbitration and commitment arbitration are separate but interacting control loops.

### 4.5 Historical stock state networks

The current active four-file closure contains important active state channels such as:

- `sn-cavalry-threat = 65`
- `retreat-now-goal = 20`
- `attack-status-goal = 24`
- `restart-attack-goal = 27`

The static lifecycle join established writers/readers and rule scope for these channels. Runtime qualification is still required.

The broader Promisory corpus also contains historical state such as `cavarchers` and extensive `temporary-goal2` usage. These must not be promoted into active AEGIS state merely because they exist historically.

The `sn-cavalry-threat` threshold family is a family-level detector: Magyar Huszar, Boyar, Knight, Scout Cavalry, Tarkan, War Elephant, Camel and Cataphract lines participate at different thresholds. It is not a simple knight detector.

The literal `up-compare-goal attack-goal >= 29876` is preserved as an unresolved anomaly. It must be qualified rather than silently corrected.

## 5. Vertical slice registry

The following 24 slices are the authoritative construction order. Each slice below is a **dossier boundary**: all existing research relevant to that slice must be mapped into it before implementation begins.

### Slice 0 — ABI, initialization and state spine

**Purpose:** Establish the legal machine vocabulary and trustworthy startup/state foundation.

**Must include:** engine facts/actions/operands; goal/SN/flag/timer/group/scratch typing; searches; placement; build/train/research primitives; pending semantics; rule order; state initialization; persistent state; generation/lifetime discipline; civilization startup.

**Already known:** ABI qualification gates and the numeric-channel allocation rules exist. The distinction between unit IDs, unit-line IDs and classes is established. No numeric channel may be allocated because a number merely appears unused.

**Primary existing sources:** `AEGIS_MASTER_ENGINEERING_GUIDE.md`, `ABI_PROBE_PLAN_2026-09-08.md`, R1/R2/R3/R4 forensic artifacts, state ABI registries.

**Stock challenge:** prove what is actually legal and persistent on the target interpreter; do not infer engine semantics from vocabulary.

**Exit:** ABI/state startup is runtime-qualified enough that later slices can safely allocate and mutate AEGIS-owned state.

### Slice 1 — Villager continuity

**Purpose:** Keep civilian population continuously alive and usable.

**Must include:** villager-production authorization, food feasibility, production-site selection, queue maintenance, pending-villager accounting, creation reconciliation, housing lead time, idle detection, idle recovery, replacement and failure handling.

**Already known:** the repository contains civilian lifecycle, villager production actuator, civilization-state implementation, worker census/role vectors, worker targeting/tasking/verification/productivity/recovery research.

**Stock challenge:** continuous production is a policy network coupled to age, food reserves, civilian limits, military policy, research, escrow, dropsites, TC count, special maps and late-game reserves.

**Exit:** no ordinary idle/cap/production failure breaks civilization continuity under tested conditions.

### Slice 2 — Food continuity

**Purpose:** Make food acquisition a persistent source-selection and transition system.

**Must include:** source discovery, serviceability, portfolio selection, herdables, berries, boar, deer/hunt, farms, fishing where applicable, walking/drop cost, source depletion, transitions, fallback and recovery.

**Already known:** Food Acquisition Controller architecture and food-source portfolio are documented; dedicated stock hunting/water subsystems are known.

**Stock challenge:** stock does not treat food as homogeneous. Source choice depends on map, infrastructure, distance, risk, depletion and timing.

**Exit:** food continuity survives source depletion, loss and transition without collapsing villager production.

### Slice 3 — Worker/resource economy

**Purpose:** Convert economic policy into discrete worker/resource operations.

**Must include:** worker roles, resource-site selection, dropsites, wood/gold/stone, income measurement, accessibility, target allocation, reassignment, task verification and recovery.

**Already known:** gatherer policy, worker lifecycle, source/dropsite serviceability and demand-to-allocation research are already present.

**Stock challenge:** worker allocation is strategy- and state-dependent, not a static percentage table.

**Exit:** observed worker distributions and measured income converge toward authorized demand without destructive oscillation.

### Slice 4 — Economic arbitration

**Purpose:** Prevent strategic objectives from fighting over the same resources.

**Must include:** demand vectors, reservations, escrow, affordability, opportunity cost, competing claims, preemption, commitment lifecycle, expiration, cooldowns, reassertion, same-pass arbitration, hysteresis and emergency liquidity.

**Already known:** escrow QC and extensive commitment/production arbitration research already exist.

**Stock challenge:** research, production, construction, military posture and economy all consume shared resources and can change priority dynamically.

**Exit:** resource commitments are explainable, non-duplicated, released correctly and resilient to competing objectives.

### Slice 5 — Construction OS

**Purpose:** Turn build intent into reliable structures and infrastructure.

**Must include:** build request, feasibility, placement search, builder allocation, foundation state, progress/completion observation, queueing, failure classification, retry/rebuild, infrastructure dependency and recovery.

**Already known:** construction controller architecture and stock `buildings.per` evidence establish placement, builder, foundation and backup/rebuild concepts.

**Stock challenge:** placement/serviceability and failure/retry are part of construction semantics, not optional polish.

**Exit:** structures are created, tracked and recovered from failed or blocked construction without losing strategic intent.

### Slice 6 — Technology OS

**Purpose:** Treat age advancement and research as capability acquisition with resource arbitration.

**Must include:** readiness, prerequisites, affordability, reservation, queue, command, completion, capability reconciliation, economic/military/civ-specific technology policy and opportunity cost.

**Already known:** `researches.per` and escrow-based research feasibility are established historical sources.

**Stock challenge:** research competes with production, age-up, construction and economy and feeds back into those systems.

**Exit:** every claimed technology capability is reconciled from authorization through completion and usable state.

### Slice 7 — Information OS

**Purpose:** Turn scouts and observations into persistent information state.

**Must include:** scout production/continuity, exploration, enemy identification, resource/infrastructure discovery, military observation, pathing, target tasks, freshness/staleness, interruption and recovery.

**Already known:** `scoutcontrol.per` research establishes quarterstep/pivot geometry, path analysis, enemy strength estimation, movement and retreat behavior. Scouting is information processing, not just movement.

**Stock challenge:** scout behavior includes path alternatives, base access, spear avoidance, deer pushing and target discovery/refresh behavior.

**Exit:** information remains fresh enough to drive threat and strategic decisions, including scout loss/replacement.

### Slice 8 — Threat model

**Purpose:** Convert observations into threat state and capability implications.

**Must include:** focus player, target player, attacking enemy, enemy pocket, military-superiority state, composition estimates, weighted military-strength interpretation, spatial threat/path analysis, threat classification and belief updates.

**Already known:** stock military strength is an interpreted weighted model covering cavalry, archers, skirmishers, cavalry archers, gunpowder, infantry, monks and siege.

**Stock challenge:** threat state feeds economy, research and production; it is not only a military display.

**Exit:** threat transitions are observable, persistent and linked to downstream authorized responses.

### Slice 9 — Cavalry Threat Containment

**Purpose:** First complete strategic/military vertical slice built on the substrate.

**Must include:** cavalry observation -> classification -> state -> capability response -> production/technology/position response -> verification -> reassessment.

**Already known:** historical threat-to-capability chain includes cavalry observations, `sn-cavalry-threat`, camel production (`traincamel`) and feasibility; the exact active-closure status of historical `cavarchers` is separated from broader Promisory evidence.

**Stock challenge:** cavalry threat is family-level and thresholded; multiple cavalry families trigger different levels.

**Exit:** a controlled cavalry threat produces an evidenced, verified and recoverable response rather than a merely issued command.

### Slice 10 — Military production and composition

**Purpose:** Turn military requirements into actual force composition.

**Must include:** production requests, unit eligibility, resource reservations, queue arbitration, composition, reinforcement, production identity/lineage and capability reconciliation.

**Already known:** production arbitration, multi-queue arbitration, lineage and aggregate production observability research exists.

**Stock challenge:** military production adapts to opponent composition and shared economic constraints.

**Exit:** requested military capability becomes available stock with known lineage and no false completion claims.

### Slice 11 — Movement and tasking

**Purpose:** Execute military and operational movement reliably.

**Must include:** target selection, route/path choice, movement commands, group/task state, spatial positioning, local advantage, task interruption and recovery.

**Already known:** stock `tsa.per` and `scoutcontrol.per` demonstrate task/movement/path analysis; `general.per` contains geometric selection algorithms.

**Stock challenge:** movement is a stateful control loop, not a single move command.

**Exit:** groups reach authorized operational states and stale/failed tasks recover.

### Slice 12 — Defense, retreat and recovery

**Purpose:** Prevent bad engagements from becoming civilization failure.

**Must include:** defense posture, threat response, retreat authorization, retreat movement, group state, reinforcement, restart logic, garrison/emergency behavior and failure classification.

**Already known:** attack lifecycle goals 20/24/27 and historical retreat/restart chains are documented; vertical world-state closure and recovery research exists.

**Stock challenge:** retreat is conditional on castles, towers, TC, monks, insufficient siege and other tactical/operational contexts; restart is a separate lifecycle.

**Exit:** defense/retreat/restart transitions are observable and do not corrupt strategic state.

### Slice 13 — Attack

**Purpose:** Make offensive action a complete lifecycle rather than an attack command.

**Must include:** target evaluation, army readiness, objective, commitment, movement, engagement, siege integration, attack state, retreat/restart, reinforcement, success/failure and strategic reassessment.

**Already known:** attack-status, retreat-now and restart-attack state networks, attack lifecycle research and strategic transition tables exist.

**Stock challenge:** attack is a persistent state machine with failure and recovery, not a one-shot order.

**Exit:** an attack can be authorized, executed, verified, abandoned/recovered and restarted without losing the strategic objective unnecessarily.

### Slice 14 — Other threat families

**Purpose:** Generalize the proven threat-response architecture without assuming identical counters.

**Must include:** archer/skirmisher, infantry, cavalry-archer, gunpowder, monk, siege and combined-arms threat responses.

**Already known:** stock threat strength categories and production/research cross-links are documented.

**Stock challenge:** each threat family may alter economy, technology, production, positioning and timing differently.

**Exit:** each threat family has an evidenced response chain and combined-arms arbitration rather than isolated counter-unit rules.

### Slice 15 — Map, mobility and positioning

**Purpose:** Make geography part of strategy and operations.

**Must include:** map regions, base/forward areas, pathability, distance, threat zones, resource opportunity, mobility, forward operations, capture and positioning.

**Already known:** spatial model requirements, farthest-villager geometry, scout path analysis and map-control research are present.

**Stock challenge:** map information changes economic viability and military advantage.

**Exit:** strategic decisions can consume and update spatial state rather than treating map position as decorative metadata.

### Slice 16 — Naval and water

**Purpose:** Operate economies and militaries on water maps and mixed land/water maps.

**Must include:** fishing, docks, water economy, naval production, naval military operations, transport/interaction where applicable and land/water arbitration.

**Already known:** stock `watercontrol.per`, `trade.per` and water-related source evidence exist in the repository's stock corpus inventory.

**Stock challenge:** water is an alternative economy and military theater, not a late add-on.

**Exit:** water behavior can sustain, produce and fight under qualification scenarios without breaking land systems.

### Slice 17 — Trade, market and conversion

**Purpose:** Provide resource conversion and fallback when direct resource acquisition is constrained.

**Must include:** market decisions, trade, conversion, opportunity cost, emergency liquidity and interaction with economic reservations.

**Already known:** stock `trade.per` and interaction/economic arbitration research identify trade as an operating domain.

**Stock challenge:** conversion is a strategic resource decision and competes with other uses of resources.

**Exit:** conversion is authorized by demand/arbitration and reconciled to actual resource state.

### Slice 18 — Interaction and ally coordination

**Purpose:** Treat communication, resource requests and ally coordination as control signals.

**Must include:** resource requests, ally coordination, taunts/communication where behaviorally relevant, market/wonder coordination and persistent state effects of interaction.

**Already known:** `interaction.per` is established as part of the stock OS/control system; interaction can alter persistent strategy/state.

**Stock challenge:** communication is not merely cosmetic when it changes coordination or resource behavior.

**Exit:** interaction actions have explicit authority, lifecycle and verification where the engine permits observation.

### Slice 19 — Strategic arbitration

**Purpose:** Connect the AEGIS cognitive model to all operating systems without allowing uncontrolled command issuance.

**Must include:** situation classification, objectives, requirements, candidates, evaluation, decision, commitment, timing, initiative/tempo, transitions, opponent adaptation, economic/military arbitration, technology/military arbitration, map/economy arbitration and defensive/offensive posture.

**Already known:** AEGIS cognition is already organized around World -> Observe -> Classify -> Believe -> Transition -> Objective -> Requirements -> Constraints -> Candidates -> Evaluate -> Commit -> Authorize -> Execute -> Verify -> Failure/Success -> Update -> Reassess.

**Stock challenge:** the stock bot's strategic intelligence is distributed through operating services, timers, state writes and cross-system feedback rather than one planner.

**Exit:** cognition issues typed service requests and commitments; operating services own execution; verification feeds cognition.

### Slice 20 — Late game

**Purpose:** Prevent early-game architecture from collapsing under late-game conditions.

**Must include:** population saturation, resource exhaustion, alternate economies, technology completion, military scaling, wonder/ending states, production/economic transitions and strategic commitment changes.

**Already known:** late-game reserves, wonder/ending behavior, trade and population-saturation domains are in the stock-derived architecture inventory.

**Stock challenge:** late game changes the meaning of scarcity, production priority and resource conversion.

**Exit:** the civilization remains coherent through saturation, exhaustion and ending-state decisions.

### Slice 21 — Recovery integration

**Purpose:** Make failure handling a system-wide supervisor rather than local retry code.

**Must include:** failure taxonomy, stale state, partial completion, conflicting commitments, blocked queues, failed searches/placements, lost actors, generation/lifetime checks, retry/recovery/replan and cross-service arbitration.

**Already known:** repository research covers failure -> execution feedback, recovery arbitration, production failure, construction recovery, worker interruption/recovery, commitment expiration/replacement and vertical world-state closure.

**Stock challenge:** recovery must preserve strategic intent while changing execution plans.

**Exit:** representative failures cause diagnosis and bounded recovery rather than silent divergence or infinite loops.

### Slice 22 — Full-system integration

**Purpose:** Prove that all operating systems and cognition form one stable civilization.

**Must include:** simultaneous economic, military, technology, information, construction and map demands; competing commitments; resource contention; threat transitions; recovery; stale state; long-duration operation.

**Already known:** cross-system control graph and vertical closure research define the required observation -> state -> authority -> consequence -> timer -> reassessment pattern.

**Stock challenge:** stock competence comes from interaction between systems, not isolated features.

**Exit:** the bot survives sustained adversarial operation without subsystem ownership collisions or strategic deadlocks.

### Slice 23 — Final qualification

**Purpose:** Freeze the final bot only after evidence closes every required gate.

**Must include:** static QC, ABI qualification, runtime qualification, stress qualification, regression, evidence-boundary audit, Byzantine strategic tuning and final stock adversarial comparison.

**Exit:** every capability has an evidence status; every unresolved item has a documented disposition; no hidden Promisory dependency remains; target-build behavior is demonstrated.

## 6. Mandatory dossier fields for every slice

Each slice must maintain these fields in its final detailed dossier:

| Field | Required content |
|---|---|
| Scope | Exact capability boundary |
| Stock corpus | Exact source files/rules relevant to the slice |
| Existing AEGIS research | Existing repository artifacts that already establish knowledge |
| Known facts | Directly established behavior |
| Composed facts | Multiple evidence sources joined without semantic overreach |
| Inferences | Explicitly marked and falsifiable |
| Engine-owned state | State AEGIS must observe rather than own |
| AEGIS-owned state | State AEGIS is authorized to maintain |
| State channels | GOAL/SN/FLAG/TIMER/GROUP/scratch with exact typing |
| Writers | Exact writer rules and conditions |
| Readers | Exact reader rules and conditions |
| Resetters | Lifetime/reset behavior |
| Demands | What cognition/other services can request |
| Arbitration | How competing requests are resolved |
| Reservation | Resource/commitment reservation semantics |
| Authorization | Conditions under which commands may issue |
| Execution | Exact engine operation |
| Observation | What can actually be observed afterward |
| Reconciliation | How world state is updated |
| Verification | What proves each lifecycle stage |
| Failure classes | Transient/local/upstream/stale/impossible/ABI/etc. |
| Recovery | Retry, replacement, replan, abandon conditions |
| Generation | Identity/lifetime semantics |
| Stock comparison | What AI(HD)+Promisory does that AEGIS does not |
| Missing knowledge | What stock still needs to teach us |
| Qualification | Static/ABI/runtime/stress status |
| Evidence links | Exact repository artifact paths and machine evidence |

## 7. The adversarial stock review

Before any slice is implemented or accepted, AI(HD)+Promisory must be treated as the adversarial reviewer and asked:

1. What does stock maintain continuously that AEGIS does not?
2. What does stock retry, rebuild, release, expire or restart?
3. What state does stock write and who reads it?
4. What timers and rule-order dependencies matter?
5. What mundane maintenance loop prevents civilization failure?
6. What map/resource/serviceability condition changes the behavior?
7. What cross-system feedback path is absent?
8. What happens when the preferred action fails?
9. What happens when two valid objectives compete?
10. What does stock do after partial success?
11. What does stock do when an actor dies or becomes unavailable?
12. What behavior exists in the broader Promisory corpus but not in the active runtime closure?
13. What historical behavior has already been proven but is currently missing from AEGIS implementation?

The purpose is not to clone stock. It is to ensure that every stock capability is either reimplemented, intentionally replaced by a demonstrably superior AEGIS mechanism, or explicitly dispositioned as irrelevant/engine-owned/historical-only.

## 8. Anti-forgetting rule

When implementing any slice, **do not rely on conversational memory**. Start from this document, follow its existing-research references, then inspect the detailed repository artifacts before writing code.

A new discovery must be written back into the slice dossier before it is considered project knowledge. A corrected finding must update both the detailed forensic artifact and this source of truth. A rejected design must remain archived with its reason for rejection.

No new independent inventory, ABI registry, numeric census or lifecycle model may be created when an existing canonical artifact already serves that purpose.

## 9. Construction gate

No production implementation begins merely because a slice is next in order. The slice must first have:

1. repository evidence consolidated;
2. stock adversarial review completed;
3. state ownership mapped;
4. ABI operands justified;
5. lifecycle contract complete;
6. failure/recovery paths defined;
7. qualification plan defined.

Only then:

`FORENSICS -> CONSOLIDATION -> ADVERSARIAL REVIEW -> ARCHITECTURE -> IMPLEMENTATION -> STATIC QC -> ABI QC -> RUNTIME QC -> STRESS QC -> FREEZE`

## 10. Current strategic interpretation

The major project risk is no longer that AEGIS lacks a high-level cognitive model. The major risk is forgetting or underbuilding the operating machinery that makes competent RTS behavior possible.

The repository already contains much of that knowledge. The job of this source of truth is to make it impossible to mistake **"documented somewhere"** for **"known, mapped, implemented, and qualified."**

The next research question after consolidation is therefore precise:

> **For each slice, what do we already know, what have we already implemented, what remains unqualified, and what does AI(HD)+Promisory still demonstrate that is absent?**

That question—not another generic feature list—controls the next engineering pass.
