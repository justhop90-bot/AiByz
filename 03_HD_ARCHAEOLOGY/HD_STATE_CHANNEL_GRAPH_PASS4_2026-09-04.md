# Layer 2 — HD State-Channel / Writer-Reader Graph Pass 4

**Date:** 2026-09-04  
**Status:** RECONSTRUCTION / WORKING KNOWLEDGE  
**Source authority:** verified `AI (HD version).per` + verified Promisory source supplied for Layer 2  
**Runtime boundary:** current DE execution semantics remain governed by Layer 1; Layer 1 remains frozen at 89%.

## 1. Purpose

Pass 3 reconstructed the historical program as a stateful, transition-oriented strategy controller. Pass 4 makes that model more concrete by asking a harder architectural question:

> **Which state channels exist, who appears to write them, who reads them, what game decision do they mediate, and where can conflicting writers create strategic instability?**

This is not a claim that the historical program had a clean object-oriented architecture. The opposite is the important finding: its architecture is distributed across goals, strategic numbers, timers, escrow, production flags, search state, DUC state, and specialized modules.

The graph therefore describes the *logical architecture* recovered from the source, not a claim about internal engine objects.

## 2. State-channel model

Use this normalized representation for archaeology:

`CHANNEL = {name, semantic_type, apparent_owner, writers, readers, inputs, outputs, temporal_policy, side_effects, failure_modes, evidence_grade}`

The critical distinction is:

`FACT / OBSERVATION -> BELIEF / CLASSIFICATION -> REQUIREMENT -> COMMITMENT -> AUTHORITY -> ACTION -> POSTCONDITION`

A goal or strategic number may physically carry more than one of these semantic roles in the historical source. That is precisely what AEGIS must avoid reproducing without an explicit type boundary.

## 3. Channel A — strategy selection

**Primary state:** `strategy-goal` and related strategy-selection values.  
**Apparent writers:** HD strategy-selection branches and initialization/configuration logic.  
**Readers:** economy, production, technology, military, building, map and attack branches.  
**Inputs:** age, map classification, resource state, enemy classification, game mode, position, timing, existing commitments.  
**Outputs:** downstream unit, economy, building and attack behavior.

### Game meaning

The program does not merely select a build order. It selects a strategic posture that changes the interpretation of later facts.

### Reconstructed control loop

`GAME CONTEXT -> STRATEGY CLASSIFICATION -> strategy-goal -> downstream subsystem policies -> changed world -> reclassification`

### Architectural risk

If many modules write the strategy channel opportunistically, the program can oscillate between plans. Historical timers and conditional branches appear to mitigate this, but ownership is not centralized.

**Evidence:** PROBABLE for distributed strategic state; CONFIRMED that `strategy-goal` exists and is consumed across strategic logic.

## 4. Channel B — unit / capability requirement

**Primary state:** `unit-goal`, `ranged-unit-type-goal`, `uu-up-goal`, anti-threat goals and related production flags.  
**Apparent writers:** strategy, threat, military and production branches.  
**Readers:** `units.per`, production/building logic, technology logic, attack composition logic.  
**Inputs:** enemy capability, current army, technology, resources, infrastructure, strategic mode.  
**Outputs:** production authorization and army composition.

### Game meaning

This is the bridge between strategic intent and executable force generation.

`enemy / objective -> required capability -> unit-goal -> production authorization -> units`

### Important inference

The historical `unit-goal` should not be interpreted as a simple queue instruction. Its location in a wider network makes it closer to a *capability requirement*.

**Evidence:** PROBABLE.

## 5. Channel C — control / authority

**Primary state:** `control-goal`, plus attack/control flags and related strategic-number settings.  
**Apparent writers:** strategy and control branches.  
**Readers:** resource, castle/stone, production and tactical branches.

The source comments explicitly associate `control-goal` with control behavior such as shooting/stone decisions around castle strategy.

### Game meaning

This channel represents permission or mode constraints that change what the rest of the controller is allowed or expected to do.

### AEGIS distinction

AEGIS should separate:

`strategic intent` from `execution authority`.

Historical code often places the two close together because the rule engine has few native architectural boundaries.

**Evidence:** CONFIRMED existence and documented use; PROBABLE interpretation as an authority-like channel.

## 6. Channel D — enemy identity / focus

**Primary state:** `enemy-goal`, focus-player context, target identity and related player-selection state.  
**Apparent writers:** enemy selection, taunt targeting, strategic targeting, team/military logic.  
**Readers:** threat, attack, target selection, intelligence and assistance logic.

### Game meaning

The AI needs to answer "which opponent matters right now?" before many observations have strategic meaning.

The historical taunt interface can force target selection for a time window, demonstrating that target identity is itself persistent strategic state rather than a transient fact.

### AEGIS representation

`target_belief = {player, reason, confidence, expiry, override_source}`

**Evidence:** CONFIRMED for persistent target/focus mechanisms; PROBABLE for the generalized belief model.

## 7. Channel E — threat state

**Primary state:** threat source/target/type/time data and anti-cavalry, monk, forward, fortification and related threat goals.  
**Apparent writers:** `threats.per`, intelligence/threat classification branches.  
**Readers:** military production, attack state, defense, target selection, resource allocation.

### Game meaning

A threat is not simply an enemy unit count. It is a relationship:

`source -> mechanism -> target -> time -> severity -> required response`.

### Strategic consequence

Threat state is a compressed cache of expensive interpretation. Downstream systems should consume the classification instead of repeatedly reconstructing the raw evidence.

**Evidence:** CONFIRMED for dedicated threat channels and specialized threat branches; PROBABLE for cache interpretation.

## 8. Channel F — resource commitment / escrow

**Primary state:** escrow amounts, escrow percentages, escrow purpose, `escrow-flag`, resource-control settings.  
**Apparent writers:** `escrow.per`, resource-control and strategy branches.  
**Readers:** research, production, buildings, economy and strategic transition logic.

### Canonical lifecycle recovered

`REQUIREMENT -> RESERVE -> PROTECT -> FEASIBILITY -> EXECUTE -> RELEASE / RESET`

The opening release/reset behavior in `escrow.per` is especially important: stale reservations are explicitly cleared rather than allowed to remain indefinitely.

### Game meaning

The stockpile is treated as a set of competing future claims.

### AEGIS consequence

Reservations need explicit owner, priority, expiry and cancellation semantics. The historical mechanism provides the conceptual seed but not a clean ownership model.

**Evidence:** CONFIRMED for escrow lifecycle; PROBABLE for opportunity-cost interpretation.

## 9. Channel G — economy allocation

**Primary state:** gatherer percentages, resource-control settings, `save-wood-goal`, food/farm/hunting state.  
**Apparent writers:** `gatherers.per`, economy/strategy rules.  
**Readers:** worker task allocation, production, research, buildings and strategic transition rules.

### Reconstructed loop

`STRATEGIC DEMAND -> RESOURCE PRIORITY -> GATHERER ALLOCATION -> STOCKPILE CHANGE -> COMMITMENT FEASIBILITY -> REASSESS`

The source's contextual changes in food/wood/gold/stone allocation show that economic distribution is dynamic state, not a fixed opening ratio.

**Evidence:** CONFIRMED for contextual allocation; PROBABLE for the higher-order demand-control interpretation.

## 10. Channel H — attack authorization and lifecycle

**Primary state:** `attack-goal`, `attack-status-goal`, `restart-attack-goal`, `retreat-now-goal`, target identity, attack timers.  
**Apparent writers:** `tsa.per` and related attack/control logic.  
**Readers:** target selection, unit control, regroup, retreat, production and strategic reassessment.

### State model

`IDLE -> PREPARE -> COMMIT -> MOVE -> ENGAGE -> ASSESS -> CONTINUE | REGROUP | RETREAT -> COOLDOWN -> RESTART | ABANDON`

### Key observation

The presence of distinct attack state, retreat state, restart state and timers strongly argues against a boolean interpretation of "attack." The program models an attack as a temporal process.

**Evidence:** CONFIRMED for separate channels; PROBABLE for normalized state-machine interpretation.

## 11. Channel I — position / map posture

**Primary state:** `position-goal`, `forward-goal`, `forward-threat-goal`, `nr-map-goal`, point-goal pairs and geometry/search state.  
**Apparent writers:** map classification, scouting, attack, building and tactical controllers.  
**Readers:** economy, attack, construction, scouting and movement.

### Game meaning

Position changes the feasible strategy set. The same force can be valuable or useless depending on distance, reinforcement path, terrain, defensive coverage and resource access.

### Source evidence

Scouting and water-control code performs explicit geometric candidate generation, path analysis and local-advantage evaluation. Building code likewise uses placement context.

**Evidence:** PROBABLE as a cross-system strategic abstraction; CONFIRMED for explicit geometry/candidate mechanisms.

## 12. Channel J — production authorization

**Primary state:** training flags and production goals in `units.per`, plus building/infrastructure state.  
**Apparent writers:** strategic requirement, threat, technology and military branches.  
**Readers:** production actions and queue state.

The historical pattern of initializing many train flags to `no` and selectively enabling them is architecturally significant.

### Reconstructed semantics

`CAPABILITY REQUIRED? -> PRODUCTION AUTHORIZED? -> INFRASTRUCTURE READY? -> CAN-TRAIN? -> TRAIN -> VERIFY`

### AEGIS consequence

Production should be modeled as a controlled capability pipeline with an explicit owner of each authorization, rather than as independent unit-spam rules.

**Evidence:** CONFIRMED for the initialization/enable pattern; PROBABLE for capability-pipeline abstraction.

## 13. Channel K — technology transition

**Primary state:** research/escrow flags, current-age state, technology-specific commitments.  
**Apparent writers:** `escrow.per`, research rules, strategy/economy branches.  
**Readers:** economy, production, military, age transition and strategic mode.

### Canonical chain

`TECH REQUIREMENT -> RESOURCE RESERVATION -> CAN-RESEARCH -> RESEARCH -> AGE/TECH STATE CHANGE -> RELEASE / REALLOCATION`

### Game meaning

Technology is a strategic transition, not merely a purchase. Its value depends on what capability it unlocks and what competing resources it displaces.

**Evidence:** CONFIRMED for escrow-gated research and age state updates; PROBABLE for investment framing.

## 14. Channel L — pending / asynchronous state

**Primary mechanisms:** `can-build`, `can-research`, pending object checks, pending placement, training-site readiness.  
**Writers:** engine-side execution and construction/research/production activity.  
**Readers:** virtually every subsystem that must avoid duplicate commitments.

### Critical semantic boundary

`REQUESTED != STARTED != PENDING != COMPLETED`

The source repeatedly guards actions with availability and pending-state tests. This is evidence that the programmer understood the asynchronous nature of game actions and the danger of issuing duplicate work.

**Evidence:** CONFIRMED at the coding-pattern level; current runtime details remain Layer-1 territory.

## 15. Channel M — tactical search state

**Primary mechanisms:** search reset/state, temporary goals, candidate object selection, target points, DUC state, jumps.  
**Apparent writers:** `general.per`, `scoutcontrol.per`, `watercontrol.per`, military/targeting systems.  
**Readers:** tactical action rules.

### Reconstructed search machine

`RESET -> ENUMERATE -> FILTER -> SCORE -> PRESERVE BEST -> TERMINATE -> TARGET -> ACT`

The historical implementation is a manually encoded optimizer. It uses scratch goals as registers and rule jumps as control flow.

### Performance meaning

Search is not free. The scout source explicitly documents path-analysis performance cost, and the source uses compressed loops and jumps to keep execution manageable.

**Evidence:** CONFIRMED for explicit search machinery; PROBABLE for optimizer interpretation.

## 16. Channel N — tactical target / selected object

**Primary mechanisms:** target object, target point, DUC group, target-evaluation values.  
**Writers:** candidate search and targeting systems.  
**Readers:** attack, movement, micro, siege and tactical action rules.

### Strategic interpretation

A target is the result of a constrained selection process, not merely the last visible enemy.

The target should therefore carry:

`identity + location + capability interaction + distance + objective relevance + confidence + expiry`.

**Evidence:** PROBABLE.

## 17. Channel O — timer / hysteresis memory

**Primary mechanisms:** attack timers, threat timers, scout/tactical timers, cooldowns, restart intervals and related time state.  
**Writers:** state-transition rules.  
**Readers:** re-entry guards and downstream action rules.

### Control interpretation

A timer stores temporal context that would otherwise be lost between rule evaluations.

`EVENT -> STATE ENTRY -> TIMER -> PERSISTENCE WINDOW -> EXIT / COOLDOWN -> REASSESS`

### Architectural consequence

Timers should be attached to transitions and purposes, not scattered as unexplained numeric delays.

**Evidence:** CONFIRMED for timer use; PROBABLE for hysteresis interpretation.

## 18. Channel P — external operator / taunt control

**Primary mechanisms:** documented taunt interface: stop/start slinging, resign suppression, resource cheats, assistance, monk rush, temporary enemy targeting, strategy reporting.  
**Writers:** external player/taunt input.  
**Readers:** strategic and control state.

### Important architecture lesson

External requests should enter through an authority boundary:

`INPUT -> VALIDATE -> SET CONTROL STATE -> APPLY LIFETIME/EXPIRY -> STRATEGIC EFFECT`

A taunt should not directly mutate arbitrary internal state without ownership and expiration semantics.

**Evidence:** CONFIRMED for the documented input interface; AEGIS authority model is DESIGN.

## 19. Channel Q — difficulty / execution capability

**Primary mechanisms:** difficulty parameters including execution-oriented abilities such as missile dodging and maintaining distance.  
**Writers:** initialization/configuration.  
**Readers:** tactical execution.

### Key architectural discovery

The source distinguishes strategic knowledge from execution capability. A player can conceptually know what should happen while having a deliberately constrained ability to execute it.

This is an important separation for AEGIS:

`STRATEGIC COMPETENCE != EXECUTION FIDELITY`

**Evidence:** CONFIRMED for execution-related difficulty parameters; PROBABLE for generalized architecture.

## 20. Channel R — failure / fallback state

**Primary mechanisms:** backup building/rebuild paths, reset placement, attack reset/restart, regroup, alternative search candidates, release/reset escrow.  
**Writers:** failure detection or timeout paths.  
**Readers:** recovery controllers.

### Game meaning

The historical programmer did not treat failed commands as terminal. The system frequently attempts an alternate route.

### Failure taxonomy for AEGIS

1. **Capability failure** — required capability does not exist.
2. **Feasibility failure** — capability exists but prerequisites/resources are unavailable.
3. **Execution failure** — request was made but did not produce the intended effect.
4. **Position failure** — action is technically possible but tactically unsound.
5. **Information failure** — decision was based on stale/incorrect belief.
6. **Timing failure** — opportunity window expired.
7. **Competition failure** — another commitment consumed the needed resource/capacity.
8. **Strategic-obsolescence failure** — the action succeeded technically but is no longer valuable.

The historical source supports the existence of multiple recovery mechanisms; this taxonomy is an AEGIS generalization.

## 21. Cross-channel causal spine

The recovered architecture can now be expressed as a set of coupled channels rather than isolated modules:

`MAP / INFO`
`    -> ENEMY BELIEF`
`    -> THREAT / OBJECTIVE`
`    -> REQUIRED CAPABILITY`
`    -> RESOURCE COMMITMENT`
`    -> PRODUCTION AUTHORITY`
`    -> INFRASTRUCTURE / TECHNOLOGY`
`    -> MILITARY CAPABILITY`
`    -> POSITION / ATTACK AUTHORITY`
`    -> TACTICAL EXECUTION`
`    -> WORLD CHANGE`
`    -> OBSERVATION`
`    -> BELIEF UPDATE`

Economy is coupled across the entire chain:

`STRATEGIC OBJECTIVE -> RESOURCE DEMAND -> GATHERER ALLOCATION -> STOCKPILE -> ESCROW -> EXECUTION -> NEW CAPABILITY`

The key architectural insight is that no major subsystem is actually independent.

## 22. Writer-reader conflict classes

### Conflict A — competing strategic writers

Two strategy rules can select incompatible postures in the same evaluation horizon.

**Historical mitigation:** conditions, timers, state flags, and self-disabling behavior.  
**AEGIS treatment:** explicit strategy owner + transition arbitration.

### Conflict B — resource reservation collision

Research, production, construction and tribute can all require the same resource stock.

**Historical mitigation:** escrow/resource-control.  
**AEGIS treatment:** explicit reservation ledger with priority and opportunity cost.

### Conflict C — stale enemy classification

An enemy classification remains active after new information changes the likely strategy.

**Historical mitigation:** reclassification rules and timers.  
**AEGIS treatment:** confidence, evidence age, expiry and contradiction handling.

### Conflict D — tactical target staleness

A target selected during one search becomes invalid or strategically inferior before action.

**Historical mitigation:** repeated search/update behavior and target resets.  
**AEGIS treatment:** target validity predicate immediately before action.

### Conflict E — asynchronous duplication

A command is issued again because the first request has not completed.

**Historical mitigation:** pending/can-* guards.  
**AEGIS treatment:** explicit operation identity and postcondition state.

### Conflict F — execution versus strategic intent

A low-level command remains active after the strategic reason for it disappears.

**Historical mitigation:** reset/retreat/restart controls.  
**AEGIS treatment:** authority leases tied to the commitment that created them.

## 23. What the graph says about the programmer

The strongest reconstruction is not that the programmer had a collection of clever rules. It is that they repeatedly encountered the same systems problem:

> **AoE2 decisions persist long enough to interfere with one another.**

A resource choice affects production. Production affects military capability. Military capability affects attack timing. Attack timing affects enemy response. Enemy response invalidates the earlier resource allocation. Therefore the AI needs memory, arbitration, timing, and recovery.

This explains the recurring architectural fossils:

- goals as persistent state;
- strategic numbers as mutable control surfaces;
- escrow as commitment protection;
- timers as temporal memory;
- pending checks as asynchronous-state guards;
- search loops as bounded local optimization;
- threat state as compressed interpretation;
- attack/retreat/restart as lifecycle control;
- fallback branches as recovery;
- map classifications as upstream context;
- execution parameters as a separation between knowledge and ability.

**Evidence grade:** PROBABLE as a synthesis, with individual mechanisms ranging from CONFIRMED to PROBABLE.

## 24. AEGIS architecture extracted from the graph

The historical graph should be normalized into these explicit planes:

### Plane 1 — Observation

Facts about the current world, with source and freshness.

### Plane 2 — Belief

Interpretations of observations, with confidence, evidence and expiry.

### Plane 3 — Objective / Requirement

What strategic relationship or capability should change.

### Plane 4 — Candidate generation

Possible unit, composition, technology, building, route, target, economic allocation, timing or posture.

### Plane 5 — Evaluation

Capability gain, resource tax, opportunity cost, timing, position, information requirements, risk, optionality and expected conversion.

### Plane 6 — Commitment

A selected candidate with owner, priority, reserved resources, validity conditions and expiry.

### Plane 7 — Authority

Permission for execution while the commitment remains valid.

### Plane 8 — Execution

Engine-facing actions and tactical control.

### Plane 9 — Verification

World-state postconditions.

### Plane 10 — Recovery / Reassessment

Failure classification, rollback/release, alternate candidate and updated belief.

## 25. The fundamental AEGIS rule

The historical source should not be copied as a module tree.

It should be translated as a causal architecture:

`GAME RELATIONSHIP -> OBSERVATION -> BELIEF -> STRATEGIC REQUIREMENT -> CANDIDATES -> COST/TIMING EVALUATION -> COMMITMENT -> AUTHORITY -> ACTION -> POSTCONDITION -> FAILURE CLASSIFICATION -> RECOVERY -> REASSESSMENT`

That is the architecture the historical programmer was approximating through the available `.per` substrate.

## 26. Promotion criteria for implementation

No historical channel should become an AEGIS implementation variable until the repository records:

1. semantic type;
2. owner;
3. writers;
4. readers;
5. legal transitions;
6. input evidence;
7. output consequences;
8. temporal policy;
9. resource interactions;
10. failure modes;
11. verification signal;
12. independent validation path.

If ownership cannot be identified, the channel remains archaeological evidence rather than an implementation contract.

## 27. Immediate next pass

The writer/reader graph exposes the next high-value research target:

> **Trace complete causal chains end-to-end rather than channel-by-channel.**

Priority chains:

1. enemy cavalry observation -> threat belief -> anti-cavalry requirement -> production -> attack posture;
2. Castle Age objective -> gatherer allocation -> escrow -> research -> age transition -> production reallocation;
3. enemy fortification -> attack suppression -> siege requirement -> resource reservation -> siege production -> attack restart;
4. map classification -> economy posture -> infrastructure -> military posture;
5. scouting observation -> belief update -> target selection -> tactical action -> postcondition -> reassessment.

These chains are where the programmer's implicit strategy is most likely to become fully visible.

## 28. Boundary

This pass reconstructs the logical state architecture of the verified historical source. It does not assert that every inferred ownership relationship was explicitly designed by the original authors, and it does not replace Layer-1 evidence for current DE engine semantics.

The historical source remains the evidence base; the normalized planes are the AEGIS architectural interpretation.
