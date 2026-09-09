# AEGIS Vertical-Slice Source of Truth - 2026-09-09

**Status:** AUTHORITATIVE / DEFINITIVE CONSTRUCTION BLUEPRINT
**Authority:** This is the single governing blueprint for final AEGIS construction. It supersedes earlier informal vertical-slice lists and is the only document that should answer: *what do we know, what must be built, what remains unknown, and what must AI(HD)+Promisory still teach us?*
**Runtime:** Pure `.per`; no XS; Promisory is reference/source material, never a runtime dependency.
**Target build:** AoE2DE 101.103.48987.0 / BuildID 24094652.

## 1. Purpose: eliminate knowledge loss

The repository contains detailed forensic research, lifecycle models, ABI work, architecture guides, implementation artifacts, and qualification records. Those artifacts remain the evidence. This document is their construction-facing index and governing specification.

**Do not rely on conversational memory. Do not recreate a subsystem because its research lives in another file. Before code is written, the relevant evidence in this blueprint and its cited repository artifacts must be reconciled.**

The objective is to make three states impossible to confuse:

1. **KNOWN** — established by evidence.
2. **IMPLEMENTED/QUALIFIED** — represented by AEGIS and proven to the required gate.
3. **UNKNOWN/MISSING** — not yet established, or stock behavior exists without an AEGIS equivalent.

A capability being documented somewhere in GitHub is not the same as being implemented or runtime-qualified.

## 2. Evidence authority

Use this order when resolving conflicts:

1. Target-build runtime observation.
2. Untouched target-build stock AI source on the user's machine.
3. Direct target-build ABI qualification.
4. Existing AEGIS runtime qualification.
5. Existing AEGIS static/forensic research.
6. Official/community documentation.
7. Inference.

`DIRECT`, `COMPOSED`, `INFERRED`, `AEGIS-GENERALIZATION`, and `UNCERTAIN` remain explicit evidence classes. Confidence labels (`CONFIRMED`, `PROBABLE`, `PLAUSIBLE`, `DISPROVEN`, `OBSOLETE`, `ENGINE-SPECIFIC`, `HISTORICAL`) must never be collapsed into one status.

## 3. The complete lifecycle contract

Every vertical slice is a complete control loop:

`OBSERVE -> RECONCILE -> CLASSIFY -> BELIEVE -> DETECT TRANSITION -> OBJECTIVE -> REQUIREMENTS -> CONSTRAINTS -> CANDIDATES -> EVALUATE -> COMMIT -> AUTHORIZE -> EXECUTE -> VERIFY -> FAILURE CLASSIFICATION -> RECOVERY/REPLAN -> BELIEF UPDATE -> REASSESS`

For executable operations, retain the evidence ladder:

`INTENTION -> AUTHORIZED -> ISSUED -> ACCEPTED/QUEUED -> PENDING -> CREATED -> AVAILABLE -> DEPLOYED -> EFFECTIVE`

These are different facts. `BUILD` is not completion. `DE_QUEUE` is not a spawned unit. `RESEARCH` is not completed technology. A command record is not world-state realization. World-state realization is not operational capability. Operational capability is not strategic success.

## 4. Architecture: brain and body

The project has two inseparable halves.

### AEGIS cognition — the brain

`World -> Observe -> Classify -> Believe -> Detect Transition -> Objective -> Requirements -> Constraints -> Candidates -> Evaluate -> Commit -> Authorize`

### Civilization operating system — the body

`Authorize -> Economic/Production/Construction/Information/Military/Technology Service -> Engine ABI -> World State -> Observation -> Verification -> Recovery -> Cognition`

The strategic model is not considered executable intelligence until the body can reliably realize it.

## 5. Stock adversarial model

AI(HD)+Promisory is the adversarial reference model. Treat it as a competent RTS engineer reviewing every slice.

The stock system must be interrogated at **five levels**:

1. **Capability:** what behavior exists?
2. **Lifecycle:** how is it maintained from birth/request through completion/failure/recovery?
3. **State:** what goals/SNs/flags/timers/groups/search state carry information between rules?
4. **Topology:** which rules/services write, read, reset and override that state?
5. **Cross-system effect:** how does the behavior change economy, production, technology, military, information, map position or strategic posture?

A stock behavior is not considered captured merely because AEGIS has a similarly named rule.

## 6. What the previous blueprint was missing

The stock-adversarial review and existing GitHub research establish that the blueprint must explicitly account for the following capabilities and mechanisms, not hide them inside broad labels:

### Civilization continuity and maintenance
- civilization initialization and persistent-state startup;
- continuous villager production policy, including pending-villager accounting;
- housing lead-time management, not merely population-cap detection;
- idle-villager census, task recovery and replacement;
- worker-role accounting and discrete allocation;
- resource-site selection and serviceability;
- dropsite selection, construction and logistics dependencies;
- food-source portfolio management and source transitions;
- herdables, berries/forage, boar, deer/hunt, farms and fishing where applicable;
- hunting-specific lifecycle and recovery;
- farm creation/replacement and food fallback;
- wood/gold/stone allocation and income measurement;
- production-building existence, availability and queue maintenance;
- foundation/progress/completion reconciliation;
- construction failure, placement retry, builder recovery and rebuild/backup behavior;
- research queue continuity and age progression;
- emergency garrison/recovery behavior where supported;
- maintenance loops that keep services alive even when cognition is uncertain.

### Information and scouting
- scout production and replacement;
- exploration continuity;
- enemy-player identification;
- resource/infrastructure discovery;
- military observation;
- information freshness/staleness;
- scout target/task state;
- path analysis and alternate-path discovery;
- specialized scout micro, including avoidance and route adaptation;
- information-to-threat and information-to-target feedback.

### Military operations
- military production requests and queue arbitration;
- force composition and reinforcement;
- army/group creation and maintenance;
- task assignment and task recovery;
- target selection and target switching;
- route/movement execution;
- local advantage evaluation;
- tactical micro;
- defense, garrison and emergency response;
- retreat and retreat-state persistence;
- attack lifecycle, restart and recovery;
- siege and counter-siege;
- capture/forward operations;
- military idle recovery;
- threat-family-specific responses;
- combined-arms arbitration;
- naval military behavior;
- map-control/mobility/positioning.

### Strategic/economic integration
- economic demand vectors;
- discrete worker targets;
- escrow/resource reservation;
- competing commitment arbitration;
- opportunity cost;
- spending priority and emergency liquidity;
- allocation hysteresis/anti-oscillation;
- commitment expiration, cooldown, release, replacement and reassertion;
- same-pass arbitration/re-entry;
- economic↔military arbitration;
- technology↔military arbitration;
- map-position↔economy arbitration;
- defensive↔offensive posture arbitration;
- opponent-aware adaptation;
- timing/initiative/tempo;
- transition management;
- late-game population/resource/production changes;
- wonder/ending-state logic;
- trade and market conversion;
- ally coordination and resource requests;
- interaction/communication where behavior changes state or coordination.

### Reliability and forensic correctness
- command evidence ladder;
- world-state reconciliation;
- operational capability verification;
- strategic-effect verification;
- failure taxonomy;
- bounded retry/recovery/replan;
- generation/lifetime matching;
- stale-state detection;
- cross-service overwrite priority;
- timer semantics;
- rule ordering and control topology;
- conditional/load topology;
- engine-owned versus AEGIS-owned state;
- historical-only versus active-runtime stock behavior.

## 7. Existing repository knowledge that is now part of the blueprint

The following is already researched and must be treated as existing project knowledge, not rediscovered:

### 7.1 Civilization substrate
The Civilization Substrate Guide establishes the operating stack and explicitly identifies continuous villager production, housing, idle recovery, worker-role accounting, food selection/transition, dropsites/infrastructure, construction placement/builder management, production queues, scouting continuity, emergency recovery/garrison behavior and research continuity as civilization operating services. fileciteturn286file0

### 7.2 Stock substrate architecture
P0 established that stock is not a set of independent scripts. Its shared symbol/state ABI spans facts, objects/classes, foundations, research/timer/group/action/order constants, ObjectData fields, terrain/search/placement constants, strategic numbers, persistent goals, scratch goals and cross-module flags. It also established active cross-domain feedback among construction, research, military, threats, scouting, production and economy. fileciteturn289file0

### 7.3 Lifecycle/reconciliation research
Existing AEGIS research already covers civilian lifecycle, worker census/roles/targets/tasks/verification/productivity/recovery, resource/dropsite serviceability, demand-to-allocation, economic contention/preemption, production arbitration, multi-queue arbitration, production failure/queue saturation recovery, commitment release/replacement, competing commitments, expiration/cooldowns/reassertion, same-pass arbitration/re-entry, failure→execution feedback, recovery arbitration, object birth/lineage, production identity/command lineage, aggregate production observability, state-delta/entity lineage, controller overwrite priority, timer temporal state, strategic transitions, vertical world-state closure and cross-system control graphs.

### 7.4 R1/R2/R3/R4 state/ABI work
The effective-load, mutable-state ownership, numeric-channel allocation and existing-inventory reconciliation passes establish that:
- static inventories already exist and must be reused;
- writer ≠ owner;
- reader ≠ authority;
- resetter defines an important lifetime boundary;
- engine-owned state is not AEGIS-owned state;
- numeric equality does not establish channel identity;
- state allocation requires typing, collision, load, ownership, compiler/validator and runtime gates.

The key static join currently establishes active closure channels including `sn-cavalry-threat = 65`, `retreat-now-goal = 20`, `attack-status-goal = 24`, and `restart-attack-goal = 27`. Runtime qualification remains open.

Historical-only distinctions are also explicit: `cavarchers` is present in the broader Promisory corpus but absent from the active four-file closure; `temporary-goal2` is broadly historical but only appears as commented text in the active closure. The anomalous `up-compare-goal attack-goal >= 29876` is preserved unresolved and must not be silently normalized.

### 7.5 Replay evidence boundary
Replay reconstruction already distinguishes command/control evidence from pending lifecycle and world realization. W0/W1/W2/W3/W4 must remain separate; unsupported parser actions and missing fields remain explicit uncertainty. Replay evidence cannot be used to invent completion or strategic effect.

## 8. Definitive vertical-slice registry

There are **24 permanent slices**. Broad domains are not substitutes for the slices; each slice is a dossier boundary and must inherit the complete lifecycle contract.

### Slice 0 — ABI + initialization + state spine

**Build:** interpreter contract, operand typing, facts/actions/searches/placement, goals/SNs/flags/timers/groups/scratch, initialization, persistent state, generation/lifetime.

**Known:** ABI gates, state-typing rules, inventory/ownership framework, target-build identity and several critical ABI findings already exist.

**Must not forget:** conditional compilation/load topology, search reset semantics, rule ordering, one-command/pass behavior, engine-owned state, negative ABI tests, startup versus first-use initialization, and exact distinction among unit ID, unit-line ID and class.

**Stock must teach us:** every still-unresolved primitive/range/persistence/order semantic that affects later slices.

**Exit:** later slices can allocate/use state and issue nontrivial commands with target-build evidence.

### Slice 1 — Villager continuity

**Build:** production authorization -> queue -> pending -> creation -> accounting -> housing -> allocation -> tasking -> idle recovery -> replacement.

**Known:** civilian lifecycle and villager production/worker lifecycle research already exist; stock production is a policy network affected by food, population/civilian limits, age, strategy, military policy, research, escrow, dropsites, TC count, map mode and late-game reserves.

**Stock must teach us:** exact maintenance-rule precedence, queue interactions, special-map behavior, lead-time thresholds, failure/recovery and cross-service overrides not yet captured.

### Slice 2 — Food continuity

**Build:** source discovery -> serviceability -> portfolio selection -> tasking -> income observation -> depletion/loss -> transition/fallback -> recovery.

**Known:** Food Acquisition Controller architecture and food portfolio are already documented; stock has dedicated boar/hunting and water subsystems.

**Stock must teach us:** exact source-selection thresholds, hunting/deer behavior, farm transition policy, source risk/geometry rules and map/civ exceptions.

### Slice 3 — Worker/resource economy

**Build:** census -> role vector -> demand -> site -> assignment -> task -> productivity -> reassignment/recovery for food/wood/gold/stone.

**Known:** worker census, roles, targets, tasking, verification, productivity and source/dropsite serviceability are researched.

**Stock must teach us:** exact vector precedence, discrete rounding/transition behavior, strategy-specific overrides and maintenance ordering.

### Slice 4 — Economic arbitration

**Build:** demands -> priorities -> escrow/reservation -> contention -> authorization -> release/expiration/replacement -> reassessment.

**Known:** escrow and commitment arbitration lifecycle research is already extensive.

**Stock must teach us:** any unresolved priority/override/expiration rules and hidden cross-system resource taxes.

### Slice 5 — Construction OS

**Build:** request -> feasibility -> placement -> builder -> foundation -> progress -> completion -> failure -> retry/rebuild -> infrastructure dependency.

**Known:** construction is a state machine; placement, builders, foundation/completion tracking, failure/retry/rebuild and stock backup behavior are researched.

**Stock must teach us:** exact placement scoring/search topology, builder replacement, blocked-foundation behavior, repair/rebuild behavior and rule-order interactions.

### Slice 6 — Technology OS

**Build:** capability requirement -> prerequisites -> reservation -> affordability -> queue -> research -> completion -> capability reconciliation.

**Known:** research and escrow-based feasibility are researched; technology feeds economy/production/military.

**Stock must teach us:** exact research ordering, competing research priorities, age-up interruption/recovery and civ/map-specific technology policies.

### Slice 7 — Information OS

**Build:** scout continuity -> exploration -> discovery -> observation -> freshness -> tasking -> loss/replacement -> belief update.

**Known:** scout geometry, path analysis, enemy strength estimation, movement and retreat are researched.

**Stock must teach us:** alternate-path selection, base-access search, spear avoidance, deer pushing, scout micro and observation refresh cadence where not yet proven.

### Slice 8 — Threat model

**Build:** observation -> composition/strength interpretation -> threat classification -> persistent state -> response requirements -> belief transition.

**Known:** threat processing is distributed and includes weighted military-strength categories for cavalry, archers, skirmishers, cavalry archers, gunpowder, infantry, monks and siege. Threat state feeds production/research/economy.

**Stock must teach us:** exact weighting, thresholds, competing threat precedence, decay/reset behavior, spatial coupling and cross-system effects not yet runtime-qualified.

### Slice 9 — Cavalry Threat Containment

**Build:** cavalry observation -> `sn-cavalry-threat` -> response requirement -> counter capability -> production/technology/position -> verification -> reassessment.

**Known:** exact active writer graph and family-level threshold detector are statically established. The first threshold covers Magyar Huszar >4, Boyar >4, Knight >4, Scout Cavalry >4, Tarkan >3, War Elephant >2, Camel >4, Cataphract >4. Historical cavalry→camel production chain is established.

**Stock must teach us:** runtime threshold transitions, persistence/reset, competing writers, exact downstream effects and whether each response is actually realized/effective.

### Slice 10 — Military production/composition

**Build:** military demand -> reservation -> unit eligibility -> producer -> queue -> creation -> stock -> composition -> reinforcement.

**Known:** production arbitration, lineage and aggregate production observability research exists.

**Stock must teach us:** composition formulas, queue priority, target switching, emergency production, unit-specific micro-preparation and production-to-task handoff.

### Slice 11 — Movement/tasking

**Build:** task -> target -> route -> movement -> arrival/engagement -> interruption -> recovery.

**Known:** task/movement/path analysis and geometric selection research exist.

**Stock must teach us:** exact path-selection scoring, group movement semantics, regrouping, blocking, retreat geometry, local advantage and command precedence.

### Slice 12 — Defense/retreat/recovery

**Build:** threat -> defensive requirement -> posture -> retreat/hold/garrison -> movement -> reinforcement -> restart -> verification.

**Known:** attack-state channels 20/24/27, retreat conditions and restart lifecycle are researched.

**Stock must teach us:** exact precedence among retreat/hold/attack/reinforce, garrison rules, local advantage thresholds, recovery timing and persistent-state transitions.

### Slice 13 — Attack

**Build:** objective -> readiness -> commitment -> movement -> engagement -> target/siege decisions -> retreat/restart -> success/failure -> reassessment.

**Known:** attack lifecycle and vertical world-state closure are researched.

**Stock must teach us:** attack-group selection, target switching, local advantage, siege timing, regroup/reinforcement and attack-goal state transitions not yet runtime-qualified.

### Slice 14 — Other threat families

**Build:** archer/skirmisher, infantry, cavalry-archer, gunpowder, monk, siege and combined-arms threat-response lifecycles.

**Known:** threat categories and cross-system production/research coupling are established.

**Stock must teach us:** threat-specific counterselection, priority/weighting, mixed-composition response and transition behavior.

### Slice 15 — Map/mobility/positioning

**Build:** spatial state -> opportunity/risk -> position objective -> route -> execution -> verification -> map-state update.

**Known:** spatial model requirements, farthest-pair geometry and scout path analysis exist.

**Stock must teach us:** territorial/forward-region semantics, blocking, mobility valuation, path alternatives, settlement expansion and position/economy coupling.

### Slice 16 — Naval/water

**Build:** water opportunity -> fishing/economic demand -> docks/production -> naval force -> tasking -> recovery -> land/water arbitration.

**Known:** stock water control is a distinct subsystem and water economy is a strategic domain.

**Stock must teach us:** exact fishing-site/dock serviceability, naval production/tasking, water threat response, transport behavior and land/water priority rules.

### Slice 17 — Trade/market/conversion

**Build:** shortage/surplus -> conversion candidate -> opportunity-cost evaluation -> authorization -> transaction -> resource reconciliation.

**Known:** trade/market is a stock operating domain and interacts with economy/interaction.

**Stock must teach us:** exact trigger conditions, price/opportunity-cost policy, emergency conversion and coordination with escrow.

### Slice 18 — Interaction/ally coordination

**Build:** request/signal -> classification -> priority -> response -> resource/strategy effect -> verification.

**Known:** interaction is an operating/control subsystem; resource requests, strategy disclosure, ally coordination, market/wonder coordination and communication can alter persistent behavior.

**Stock must teach us:** exact control-signal semantics, ally-resource arbitration, communication timing and which interaction events create persistent strategic effects.

### Slice 19 — Strategic arbitration

**Build:** simultaneous situations -> objectives -> requirements -> candidate plans -> evaluation -> commitments -> cross-service authorization -> transition.

**Known:** AEGIS cognition chain is defined; stock competence emerges from distributed service feedback, timers and persistent state.

**Stock must teach us:** hidden objective priority, rule-order arbitration, posture transitions, timing/tempo logic, opponent adaptation and cross-system opportunity-cost behavior.

### Slice 20 — Late game

**Build:** saturation/exhaustion -> new demand regime -> production/economy/technology changes -> ending-state decisions.

**Known:** late-game reserves, population saturation, trade and wonder/ending domains are in the research corpus.

**Stock must teach us:** exact transition triggers, production/resource redistribution, late-game military priorities, wonder behavior and resignation/ending-state logic where applicable.

### Slice 21 — Recovery integration

**Build:** failure observation -> classification -> scope -> retry/replacement/replan/abandon -> verification -> state repair -> reassessment.

**Known:** worker, production, construction, commitment and cross-system recovery research already exists.

**Stock must teach us:** hidden failure classes, retry limits/cooldowns, priority escalation, partial-success handling and recovery ordering.

### Slice 22 — Full-system integration

**Build:** concurrent economic + military + technology + information + construction + map demands with contention, interruption, stale state and long duration.

**Known:** cross-system control graph and vertical closure establish the required feedback topology.

**Stock must teach us:** emergent interactions that do not appear in isolated slices, especially simultaneous threats, resource scarcity, actor loss, queue contention and posture changes.

### Slice 23 — Final qualification

**Build:** static QC -> ABI QC -> runtime QC -> stress QC -> regression -> stock adversarial audit -> Byzantine tuning -> freeze.

**Known:** qualification gates and evidence discipline are established.

**Stock must teach us:** only differences that remain after every lower-level capability is genuinely closed.

## 9. Mandatory dossier schema for every slice

Every slice's detailed section/work artifact must answer all of these fields before implementation is frozen:

1. Exact scope and non-scope.
2. Stock files/rules/functions relevant to the slice.
3. Existing AEGIS artifacts containing prior research.
4. Direct facts.
5. Composed facts.
6. Inferences and falsifiers.
7. Engine-owned state.
8. AEGIS-owned state.
9. Exact state channels and types.
10. Initializers and initialization conditions.
11. Writers and exact rule conditions.
12. Readers and exact rule conditions.
13. Resetters/reinitializers.
14. Lifetime/generation semantics.
15. Demand inputs.
16. Arbitration/priority/override rules.
17. Resource reservations/escrow.
18. Authorization conditions.
19. Exact engine commands/operands.
20. Command acceptance/queue evidence.
21. Pending lifecycle.
22. World-state realization.
23. Operational capability realization.
24. Strategic-effect realization.
25. Failure classes.
26. Recovery/retry/replan/abandon behavior.
27. Cross-system feedback.
28. Timer/order dependencies.
29. Stock-vs-AEGIS capability delta.
30. What is already known versus what remains unknown.
31. Static/ABI/runtime/stress qualification status.
32. Exact evidence paths and machine evidence IDs.

## 10. The stock adversarial checklist

Before accepting any slice, run AI(HD)+Promisory against it and explicitly search for:

- initialization that the slice omitted;
- maintenance loops that keep it alive;
- state channels not represented;
- hidden writers/readers/resetters;
- timers and rule-order effects;
- searches and placement algorithms;
- queue and pending-object semantics;
- actor death/loss and replacement;
- partial success;
- stale observations;
- contention with another service;
- emergency behavior;
- map/resource serviceability constraints;
- civ-specific or map-specific branches;
- special modes and late-game branches;
- target switching and priority changes;
- alternate paths and fallback actions;
- cross-system feedback;
- behaviors in the broader Promisory corpus that are absent from the active runtime closure;
- historical behavior that is understood but not yet reimplemented;
- behavior that AEGIS can improve rather than copy.

**The stock comparison is not complete until every apparent omission is dispositioned as: REIMPLEMENT, AEGIS-SUPERIOR-REPLACEMENT, ENGINE-OWNED, HISTORICAL-ONLY, IRRELEVANT-BY-DESIGN, or UNRESOLVED.**

## 11. Anti-forgetting construction law

When writing code:

1. Read this blueprint's relevant slice.
2. Read every referenced existing GitHub artifact before designing.
3. Reconcile the current implementation against that research.
4. Run the stock adversarial review.
5. Only then write code.
6. After code, update the slice's knowledge/status in this blueprint.

When research changes a conclusion, update the detailed evidence artifact and then update this blueprint. Do not create a competing master document.

No new independent symbol inventory, ABI registry, numeric census, lifecycle model or architecture guide may be created when a canonical artifact already exists.

## 12. Definition of definitive completeness

AEGIS is complete only when:

- the civilization initializes correctly;
- civilians continuously produce, gather, build, research and recover;
- resources are spatially and economically understood;
- commitments are reserved and arbitrated;
- information is acquired, aged, interpreted and reconciled;
- threats become verified capability responses;
- military forces form, move, fight, retreat, reinforce and recover;
- attacks have complete lifecycles;
- water, trade, interaction and late-game modes operate;
- cross-system conflicts are arbitrated;
- failures are classified and recovered;
- state ownership and lifetimes are controlled;
- no command/completion or historical/runtime evidence boundary is violated;
- all critical behavior is target-build qualified;
- AI(HD)+Promisory can no longer identify an unaccounted-for stock capability without a documented disposition;
- the remaining differences are deliberate AEGIS improvements, not forgotten stock behavior.

**That final condition is the standard for calling this blueprint—and the bot—definitive.**

## 13. Adversarial AI(HD)+Promisory pass — WHO / WHAT / WHEN / WHERE / WHY

This is the construction-phase adversarial gate. AI(HD)+Promisory is not being asked whether the blueprint contains the right category names. It is being asked whether a stock engineer could point to a concrete behavior, state transition, control path, or maintenance mechanism that the construction plan has failed to account for.

### 13.1 WHO — authority and actor identity

For every behavior, identify who has authority to cause the transition:
- engine-owned state or engine-generated observation;
- stock rule/service that writes or commands;
- AEGIS service that owns the corresponding state;
- cognition that authorizes the requirement;
- another service that can override, preempt, reset, or invalidate it;
- physical actor/object whose lifecycle realizes the operation.

A writer is not automatically an owner. A reader is not automatically an authority. A command issuer is not automatically the actor that realizes the command. If two services can write the same channel, precedence and ownership must be explicit.

### 13.2 WHAT — exact behavior and state transition

The unit of reconstruction is not a feature label such as “economy” or “attack.” It is the smallest behavior that changes control state or world state in a strategically meaningful way.

For each behavior, record:
- observation/input;
- classification/belief;
- state channel(s) changed;
- guard/predicate;
- candidate action(s);
- authorization;
- exact engine primitive and operands;
- queue/pending state;
- world realization;
- operational capability;
- strategic effect;
- failure and recovery;
- reset/reassessment.

Also record non-state machinery: searches, geometry, placement, ObjectData, groups, timers, queue semantics, action/order primitives, and rule-order dependencies. These are part of the behavior when the stock implementation depends on them.

### 13.3 WHEN — trigger, cadence, lifetime, and temporal precedence

“Condition exists” is insufficient. Establish when the behavior is allowed to run and how long its state remains authoritative.

Every slice must account for:
- initialization/startup;
- first-use initialization;
- recurring maintenance cadence;
- timer enable/disable/set/modify behavior;
- same-pass re-entry and arbitration;
- rule ordering and overwrite precedence;
- transition thresholds and hysteresis;
- expiration/cooldown;
- actor/object loss;
- state reset/reinitialization;
- late-game/special-mode branches;
- stale observations and refresh cadence.

A `(true)` guard does not prove a one-time initializer. Source order does not prove runtime order. A timer declaration does not prove its cadence or semantic unit. These require qualification where they affect behavior.

### 13.4 WHERE — provenance and topology

Every important claim must have a machine-addressable home:
1. target-build stock file;
2. exact rule/function/line or structural occurrence;
3. state channel/type;
4. writer/reader/resetter relationship;
5. load/conditional context;
6. existing AEGIS research artifact;
7. runtime/replay evidence ID when applicable.

The HD/Promisory source corpus is the complete `AI (HD version).per` plus the entire original `Promisory` directory. The four-file effective-load closure is a separate runtime-load question and must never be mistaken for the definition of the historical source corpus.

The broader corpus must therefore be searched even when a behavior is absent from the active four-file closure. Such behavior is classified as active, historical-only, conditional, obsolete, engine-owned, or unresolved; it is not silently discarded.

### 13.5 WHY — programmer intent and strategic function

For each stock behavior, explain the function it serves in the control system, without inventing intent from names alone:
- what problem or threat is being controlled;
- what resource, time, information, position, or capability is being protected or acquired;
- what competing objective is displaced or constrained;
- what downstream subsystem consumes the result;
- what observation causes reassessment;
- what would falsify the proposed strategic interpretation.

The strategic “why” must be derived from code topology and evidence, not from a plausible RTS story.

## 14. New adversarial findings that change construction requirements

The prior blueprint covered the major capability domains, but this pass finds several places where category-level coverage was still too permissive.

### 14.1 File-level coverage is now mandatory

The blueprint previously named relevant stock files per dossier but did not require a complete corpus-to-slice accounting. Construction must close this gap.

Every file in the complete 37-file HD/Promisory corpus must receive a disposition and at least one of:
- primary slice owner;
- cross-slice service dependency;
- historical-only evidence;
- conditional/development-only evidence;
- engine-owned dependency;
- obsolete/irrelevant-by-design with justification;
- unresolved requiring further archaeology.

Known stock domains that must remain explicitly mapped include constants/custom constants, initialization, finaling, gatherers, buildings, researches, units, scout control, threats, TSA/attack control, trade, interaction, water/boar support, resignation/ending logic, Paphos/development definitions, and merge/utility modules where present in the corpus.

### 14.2 Rule-level coverage is mandatory, not merely feature-level coverage

A slice cannot be marked “known” because one representative rule was understood. The adversarial unit is the rule family and its lifecycle: all writers, readers, resetters, guards, overrides, timers, alternate branches, maintenance rules, and failure paths that materially participate in the behavior.

The existing structural mutation parser and R2/R4 joins are the substrate for this work; do not create another symbol inventory or mutation census.

### 14.3 Load topology is part of the program

The source corpus and effective runtime closure answer different questions. The blueprint must preserve both:
- Source corpus: everything that can teach us historical architecture/behavior.
- Effective-load closure: what the target runtime actually loads.
- Conditional topology: behavior enabled only under specific preprocessing/load conditions.
- AEGIS runtime topology: what AEGIS deliberately loads and owns.

No historical behavior may be called “unused” merely because it is outside the current four-file closure.

### 14.4 The maintenance layer is a first-class requirement

AI(HD)+Promisory repeatedly demonstrates that practical competence comes from rules that keep the civilization alive between strategic decisions. Therefore every construction slice must separate:
- decision rules — choose what should happen;
- execution rules — issue/maintain commands;
- reconciliation rules — determine what actually happened;
- maintenance rules — prevent degradation while no new decision occurs;
- recovery rules — repair failed or invalid state.

A cognition loop without these maintenance loops is not an equivalent control system.

### 14.5 Negative-space behavior must be tracked

The stock corpus contains behavior that is historical, conditional, commented, or outside the active runtime closure. The absence of a behavior from the active closure is itself evidence requiring disposition.

Examples already established:
- `cavarchers`: live in the broader Promisory source corpus but absent from the active four-file closure;
- `temporary-goal2`: broadly used historically, but only commented in the active closure;
- the `attack-goal >= 29876` comparison remains an unresolved anomaly and must not be normalized.

These are not implementation instructions. They are anti-forgetting obligations.

### 14.6 State channels require complete lifecycle proof

The known active channels `sn-cavalry-threat = 65`, `retreat-now-goal = 20`, `attack-status-goal = 24`, and `restart-attack-goal = 27` demonstrate the required standard: declaration, initialization, every writer, every reader, guard context, reset/reinitializer, lifetime, authority effect, downstream consumer, runtime qualification, and disposition.

The same standard applies to every AEGIS-owned channel introduced during construction. Numeric availability alone is never sufficient for allocation.

### 14.7 Capability realization must be followed all the way to strategic effect

Construction must not stop at “the command worked.” For every important capability, qualification must distinguish:
`INTENTION -> AUTHORIZED -> ISSUED -> ACCEPTED/QUEUED -> PENDING -> CREATED -> AVAILABLE -> DEPLOYED -> EFFECTIVE -> STRATEGIC EFFECT`

A missing link is an explicit uncertainty, not an assumption.

### 14.8 The stock adversary must review transitions, not just steady states

The hardest failures will occur at transitions: age-up, food-source depletion, builder death, dropsite loss, housing pressure, queue saturation, scout loss, threat escalation, retreat, attack restart, technology completion, population saturation, water/land competition, resource exhaustion, and late-game mode changes.

Therefore each slice must include at least one transition/failure scenario in which the old state becomes invalid and the service must recover without cognition being rewritten manually.

## 15. Construction-phase 5W acceptance gate

No vertical slice is construction-complete until its dossier can answer, with evidence:

**WHO:** who observes, owns, writes, authorizes, executes, overrides, and realizes the state transition?

**WHAT:** exactly what state and world transition occurs, including operands, queues, searches, geometry, groups, timers, and failure paths?

**WHEN:** what triggers it, how often can it recur, what timer/order/priority rules govern it, and when does its state expire or reset?

**WHERE:** which exact stock source and AEGIS artifact prove it, which load/conditional path contains it, and where is its runtime evidence?

**WHY:** what strategic control problem does it solve, what does it consume/protect/displace, and what evidence would falsify that interpretation?

If any answer is “unknown,” the slice remains open. If the answer is “not applicable,” that must be justified. If the answer is inferred, the falsifier must be recorded.

## 16. Revised definition of definitive construction coverage

The blueprint is now considered construction-ready only as an inventory, not as proof of implementation. Before a slice can be frozen, it must demonstrate:
- complete stock-file provenance;
- complete relevant rule-family coverage;
- state ownership/lifetime closure;
- load/conditional topology closure;
- WHO/WHAT/WHEN/WHERE/WHY answers;
- ABI/engine-command qualification;
- pending/world/capability/strategic-effect evidence separation;
- maintenance and recovery behavior;
- cross-system contention and override handling;
- transition/failure qualification;
- explicit stock-vs-AEGIS disposition for every material difference.

Only then can implementation be called complete. The final adversarial question remains:

> **Can AI(HD)+Promisory point to a concrete stock behavior or lifecycle mechanism that AEGIS has neither reproduced, deliberately superseded, delegated to the engine, nor explicitly rejected with evidence?**

If yes, the construction is not complete.
