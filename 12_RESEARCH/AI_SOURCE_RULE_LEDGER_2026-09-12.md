# AEGIS Source-Rule Ledger — HD → Promisory → AIBuilder → AEGIS

**Date:** 2026-09-12  
**Status:** Deep static source ledger; production code unchanged  
**Scope:** Stock `AI (HD version).per`, installed Promisory corpus, AIBuilder corpus/current AIByzBuild fork, and documented native `.per` capabilities.  
**Implementation constraint:** pure `.per`; XS is historical evidence only and is not an AEGIS dependency.

## 0. Reading rules

This ledger is deliberately stricter than a feature checklist. A capability is not promoted merely because a command appears in historical source. Each entry separates:

- **Observation:** what the historical program actually reads.
- **State:** what it stores or derives.
- **Authority:** what component owns the state/writer.
- **Authorization:** what must be true before action.
- **Execution:** the command/channel that performs the action.
- **Verification:** what distinguishes accepted command from changed world state.
- **Failure:** what invalidates the attempted transition.
- **Expiry:** what makes stale state unsafe.
- **Reassessment:** what causes the decision to be recomputed.
- **AEGIS insertion:** the smallest safe insertion point in the preserved AIBuilder substrate.

Evidence labels:

`DIRECT` = exact source behavior.  
`COMPOSED` = multiple direct rules form one lifecycle.  
`INFERRED` = functional interpretation not explicitly stated by source.  
`AEGIS-GENERALIZATION` = AEGIS architectural abstraction.  
`UNCERTAIN` = semantics require engine/runtime qualification.

---

# 1. Phase-driven policy projection

## Historical chain

**HD:** The stock monolith uses phase/age/strategy state to continuously rewrite economic, military, construction, research, and exploration policy.  
**Promisory:** `init.per`, `gatherers.per`, `units.per`, `buildings.per`, and `general.per` expand this into specialized state machines.  
**AIBuilder:** `phaseUpdate.per` is the principal policy projection layer. It writes desired explorers, house policy, town-center targets, resource percentages, building targets, and military targets.  
**AEGIS:** preserve this control plane as authoritative; additions must consume its outputs rather than replace them.

## Key symbols

**Readers:** `sn-current-age`, strategy goals, resource totals, building counts, population/civilian population, military population.  
**Writers:** `desired-military-explorers`, `desired-civilian-explorers`, `desired-naval-explorers`, `allow-houses`, desired building/unit goals, gatherer percentages.  
**Consumers:** `general.per`, `construction.per`, `economy.per`, `militaryUnits.per`, `militaryBehavior.per`.

## Contract

**Preconditions:** phase/strategy state is initialized; the downstream module is loaded after the policy writer.  
**Authorization:** phase transition and current strategic policy authorize desired-state changes.  
**Execution:** downstream modules execute desired goals.  
**Postcondition:** downstream policy has a coherent desired state for the current phase.  
**Failure:** missing writer, duplicate writer, stale phase state, or competing module overwrites a desired value.  
**Expiry:** every phase transition supersedes prior phase-specific assignments.  
**Reassessment:** phase changes, strategic goal changes, resource state, population, building state.

## AEGIS insertion

**DO NOT replace `phaseUpdate.per`.** New AEGIS policy should read phase outputs and add narrowly scoped state/authorization rules downstream. This is **DIRECT + COMPOSED** evidence.

---

# 2. Continuous economic control / gatherer continuity

## Promisory source rules

Primary source: `gatherers.per` (5,325 lines). The corpus contains repeated phase/strategy/resource-state projections and native gatherer-control mechanisms.

Representative direct symbols/rules:

- `sn-wood-gatherer-percentage`
- `sn-food-gatherer-percentage`
- `sn-gold-gatherer-percentage`
- `sn-stone-gatherer-percentage`
- `up-retask-gatherers`
- `up-drop-resources`
- `up-idle-unit-count`
- `object-data-carry`
- `object-data-target`
- `dropsite-min-distance`
- `up-path-distance`

Promisory also computes many phase/strategy-specific percentage transitions instead of relying on one static ratio.

## HD → Promisory evolution

**HD:** resource allocation is primarily strategic-number driven.  
**Promisory:** adds continuity and tactical worker state: cargo, task, source, distance, dropsite state, idle units, and explicit retasking/recovery.  
**AIBuilder:** percentage-based economy is preserved and stable, but does not expose the same demonstrated gatherer-state control surface.  
**AEGIS:** add continuity as an overlay, not a replacement for percentage policy.

## Contract

**Observation:** resource totals, worker counts, current gather target/task, dropsite distance, idle state.  
**Classification:** resource deficit/surplus; unsafe/inefficient gather assignment.  
**State:** desired resource channel plus optional AEGIS resource-control state.  
**Authorization:** retask only when the destination is valid and the worker can safely release its current task/cargo.  
**Execution:** native gatherer retasking / drop-resource channel.  
**Verification:** target/task changes; cargo state changes; subsequent resource production confirms effect.  
**Failure:** invalid target, worker unavailable, pending construction consuming workers, stale target.  
**Expiry:** resource requirement satisfied or target becomes invalid.  
**Reassessment:** after meaningful resource-state change or failed assignment.

**AEGIS insertion:** economy policy/worker-control boundary; do not write the same percentage SNs from a second owner.

**Priority:** P1.

---

# 3. Scouting / information acquisition

## Promisory source rules

Primary source: `scoutcontrol.per` (1,342 lines), plus `general.per`.

Direct mechanisms include:

- `up-send-scout`
- `up-find-player`
- `up-find-remote`
- `up-get-search-state`
- `up-get-point-distance`
- `up-path-distance`
- `up-point-explored`
- `up-reset-scouts`
- `sn-number-explore-groups`
- `sn-total-number-explorers`
- `sn-home-exploration-time`
- scout group goals/state

Promisory builds scout groups, calculates waypoints, searches for enemy military classes, scores relative scout/enemy strength, retreats from dangerous positions, and changes radius over time.

Representative `scoutcontrol.per` rule families:

1. enemy target acquisition using `up-find-player`;  
2. enemy TC acquisition using remote search;  
3. scout group creation with `up-create-group`;  
4. quarter-step path safety searches;  
5. scout strength versus enemy strength classification;  
6. retreat when scout superiority becomes sufficiently negative;  
7. projectile/TC proximity retreat;  
8. waypoint/radius reassessment.

## HD → Promisory → AIBuilder

**HD:** native explorer behavior plus explicit enemy/player search.  
**Promisory:** tactical scout micro and information scoring.  
**AIBuilder:** explorer demand is controlled through phase policy and `general.per`; it does not need a competing scout controller to function.  
**AEGIS:** information layer must preserve AIBuilder's explorer ownership.

## Contract

**Preconditions:** explorer group exists or native explorer demand is positive; enemy/player target is valid.  
**Observation:** player identity, TC location, military objects, path distance, danger indicators.  
**State:** target player, target point, exploration phase, threat/strength estimates.  
**Authorization:** dispatch/retask only when explorer policy permits it.  
**Execution:** native explorer dispatch or narrowly scoped scout action.  
**Verification:** exploration/action state changes and newly acquired observations.  
**Failure:** enemy not located; target invalid; group absent; scout threatened; competing explorer owner.  
**Expiry:** target location/strength observation becomes stale; scout group destroyed/repurposed.  
**Reassessment:** timed pulse, new enemy location, danger, strength change.

**AEGIS insertion:** observation/classification layer around `general.per`; no duplicate writes to explorer SNs.

**Priority:** P1.

---

# 4. Threat telemetry → contextual response

## Direct source

Primary Promisory sources: `init.per` and `threats.per`.

Initialization directly calls:

```text
up-get-threat-data gl-threat-time gl-threat-player gl-threat-source gl-threat-target
```

`threats.per` then uses threat state together with player identity, military population, enemy structures, target selection, and temporary goals.

Relevant symbols:

- `gl-threat-time`
- `gl-threat-player`
- `gl-threat-source`
- `gl-threat-target`
- `attacking-enemy`
- `sn-focus-player-number`
- `sn-target-player-number`
- `cavalry`, `archers`, `infantry`, `spears`, `skirms`, `cavarchers`, `siege`
- `enemy-pocket`, `ep-mpop`, `ep-cpop`, `ep-pop`

## Historical functional chain

```text
threat observation
→ identify threat player/source/target
→ validate enemy focus
→ classify enemy military population
→ classify unit families
→ derive response weights
→ feed production/attack logic
```

Promisory's `threats.per` literally reads enemy unit families into weighted strategic-number counters. It also performs enemy-pocket searches for buildings and military state.

## Contract

**Preconditions:** threat telemetry available; focus/target player valid.  
**Observation:** elapsed threat time, player, source, target.  
**Classification:** immediate threat versus strategic enemy capability.  
**State:** AEGIS threat state plus contextual target.  
**Authorization:** threat observation alone does not authorize production; capability classification and feasibility are required.  
**Execution:** existing military/economy production channels.  
**Verification:** state/production consequences must be observed independently.  
**Failure:** stale threat, invalid player, missing target, false structure inference.  
**Expiry:** threat timestamp ages out.  
**Reassessment:** new threat event, changed enemy military population, age transition, destroyed target.

**AEGIS insertion:** `OBSERVATION → CLASSIFICATION → BELIEF/STATE`, immediately upstream of the existing military policy.

**Priority:** P1 / central Layer-2 slice.

---

# 5. Boar lifecycle / support-hunter management

## Primary source: `boarhunting.per`

This file is 1,236 lines and implements a stateful lifecycle rather than a single lure command.

Important symbols:

- `minBoar`
- `myboars`, `totalboars`
- `current-boar`
- `found-boar`
- `boar-lurer`
- `found-lurer`
- `boar-distance`
- `lure-distance`
- `lure-support`
- `boar-captured`
- `search-action`
- `search-action-boar-hunting`
- `search-action-hunt-support`
- `boar-reset-timer`
- `sn-enable-boar-hunting`
- `sn-minimum-boar-hunt-group-size`
- `sn-minimum-number-hunters`
- `sn-minimum-boar-lure-group-size`

Direct rule families:

1. determine whether hunting restrictions should be enabled;
2. find a valid live boar near the TC;
3. validate boar health/carry/status;
4. select the nearest valid boar;
5. select a lurer;
6. reserve a lure distance/timer;
7. detect a failed/unsafe lure;
8. request support hunters;
9. execute the lure/capture transition;
10. reset stale boar state and recover.

The source also uses `up-get-point-distance`, `up-get-path-distance`, search filters, pending objects, object status/action/cargo, and resource distance.

## Contract

**Preconditions:** valid boar; sufficient villagers; safe hunting state; appropriate age/technology/resource context.  
**Observation:** boar distance, HP/status, lurer state, hunter count.  
**Classification:** valid lure / unsafe lure / lost target / recovery.  
**Authorization:** only when minimum hunter/lure conditions and resource constraints are satisfied.  
**Execution:** target/gather operations and support reassignment.  
**Verification:** active lure state, hunter support, boar capture/death, food flow.  
**Failure:** lurer dies, target lost, boar leaves valid state, insufficient hunters, stale timer.  
**Expiry:** boar reset timer and invalid target state.  
**Reassessment:** timer, target status, distance, hunter availability.

**AEGIS insertion:** economic/worker control boundary, with state isolated from phase policy.

**Priority:** P1; candidate for a controlled vertical slice.

---

# 6. Escrow / resource reservation / feasibility

## Promisory source: `escrow.per`

The source contains thousands of lines of explicit escrow state management.

Key symbols:

- `escrow-flag`
- `escrow-flag2`
- `escrow-flag3`
- `escrow-state`
- `escrowing`
- `up-modify-escrow`
- `up-release-escrow`
- `set-escrow-percentage`
- `can-research-with-escrow`
- `can-train-with-escrow`
- `can-build-with-escrow`
- `up-add-research-cost`

Representative source pattern:

```text
condition
→ up-add-research-cost
→ set escrow flag
→ can-research-with-escrow
→ research
→ release/reset escrow state
```

Promisory also uses escrow-aware construction placement and production.

AIBuilder independently contains substantial `can-research-with-escrow` use. Its builder-upgrades library demonstrates the same fundamental contract: establish escrow, verify feasibility, release the appropriate resources, then execute research.

## Contract

**Preconditions:** desired operation identified; resource reservation possible.  
**State:** reserved amounts and purpose.  
**Authorization:** `can-* -with-escrow` is the feasibility gate.  
**Execution:** research/train/build.  
**Postcondition:** action command accepted and escrow consumed/released as appropriate.  
**Verification:** separate completion observation.  
**Failure:** insufficient resource after reservation, prerequisite unavailable, building/unit unavailable, competing escrow purpose.  
**Expiry:** operation becomes invalid or reservation is no longer required.  
**Reassessment:** failed feasibility, completion, strategic cancellation.

**AEGIS insertion:** authorization/resource layer. Do not invent a second resource-reservation mechanism that conflicts with native escrow.

**Priority:** P1.

---

# 7. Pending-state / construction lifecycle

## Promisory source: `buildings.per`

This is one of the strongest direct architectural signals in the corpus.

The file contains hundreds of `up-pending-objects` references and numerous `up-pending-placement` references.

Representative direct families include:

- lumber camp pending checks;
- mining camp pending checks;
- TC pending checks;
- house pending checks;
- market/monastery/siege workshop pending placement;
- defensive building pending placement;
- failed/recovery construction paths.

The source explicitly contains the comment:

> “Secondary backup for rebuilds - regular system occasionally fails”

followed by a TC fallback using `build town-center` after a timer and pending-object test.

## AIBuilder / current AEGIS

The current AIBuilder-derived `construction.per` already uses pending-object checks for housing. This is a preserved capability and must not be overwritten.

## Contract

```text
DESIRED COUNT
→ FEASIBILITY
→ PLACEMENT
→ BUILD REQUEST
→ PENDING
→ COMPLETED
→ VERIFY
→ REASSESS
```

**Preconditions:** desired building count and build feasibility.  
**Authorization:** construction policy permits the build.  
**Execution:** `build`, `up-build`, placement subsystem.  
**Pending evidence:** `up-pending-objects` / `up-pending-placement`.  
**Completion evidence:** building count/type/state.  
**Failure:** placement failure, builder loss, hostile interruption, stale request.  
**Expiry:** pending request disappears without completion or policy no longer requires it.  
**Reassessment:** pending timeout, completion, resource change, threat change.

**AEGIS insertion:** formalize this existing AIBuilder construction lifecycle; do not create another builder queue.

**Priority:** P0/P1.

---

# 8. Geometry/search as candidate-generation infrastructure

## Promisory sources

`scoutcontrol.per`, `buildings.per`, `boarhunting.per`, `general.per`, `threats.per`.

Native primitives repeatedly used:

- `up-full-reset-search`
- `up-reset-search`
- `up-reset-filters`
- `up-filter-distance`
- `up-find-local`
- `up-find-remote`
- `up-find-resource`
- `up-get-search-state`
- `up-get-point`
- `up-get-point-distance`
- `up-get-path-distance`
- `up-set-target-point`
- `up-set-target-object`
- `up-clean-search`
- `up-remove-objects`
- `up-bound-point`
- `up-lerp-tiles`
- `up-lerp-percent`

## Functional meaning

Promisory uses search/geometry not merely for movement but to generate and filter candidate locations/targets before execution.

Examples:

- boar candidate selection;
- scout waypoint safety;
- TC/settlement placement;
- dock/port placement;
- defensive foundation safety;
- enemy military classification;
- building proximity checks.

## Contract

**Observation:** map/object/search state.  
**Candidate generation:** find objects/points satisfying coarse constraints.  
**Filtering:** distance, terrain, status, object-data filters.  
**Evaluation:** path distance, danger, proximity, resource value.  
**Selection:** target point/object.  
**Execution:** existing placement/movement/build command.  
**Verification:** selected object/point exists and resulting state changes.  
**Failure:** empty search, stale object index, inaccessible point, invalid path.  
**Expiry:** search state must be reset before reuse; candidate can become stale.  
**Reassessment:** repeat search after meaningful world-state changes.

**AEGIS insertion:** candidate/evaluation layer, not a replacement for construction/military executors.

**Priority:** P1.

---

# 9. Dynamic army control / attack-defense-retreat lifecycle

## Promisory sources

`init.per`, `general.per`, `units.per`, `threats.per`, `scoutcontrol.per`.

Initialization explicitly establishes attack/defense strategic numbers including:

- `sn-number-defend-groups`
- `sn-number-attack-groups`
- `sn-minimum-defend-group-size`
- `sn-maximum-defend-group-size`
- `sn-minimum-attack-group-size`
- `sn-maximum-attack-group-size`
- `sn-percent-attack-soldiers`
- `sn-percent-enemy-sighted-response`
- `sn-group-form-distance`
- `sn-group-commander-selection-method`
- `sn-group-leader-defense-distance`
- `sn-scaling-frequency`

Promisory also uses `up-retreat-now`, projectile detection/target primitives, attack/defense priorities, target evaluation, and unit-state resets.

Historical HD additionally exposes the strategic attack-state constants:

```text
retreat-now-goal = 20
attack-status-goal = 24
restart-attack-goal = 27
```

These constants are historical evidence of explicit attack-state bookkeeping; their exact engine semantics remain source-specific unless independently qualified.

## Contract

**Preconditions:** army exists; target valid; strategic attack policy permits action.  
**Observation:** army size/composition, target state, threat/projectiles, distance, military superiority.  
**Classification:** attack / defend / retreat / regroup.  
**Authorization:** attack requires sufficient group/strategic conditions; retreat may override attack.  
**Execution:** group targeting, attack, defense, retreat.  
**Verification:** unit orders/state and subsequent target/world change.  
**Failure:** target invalid, army too small, threat too high, group destroyed, path invalid.  
**Expiry:** attack commitment becomes stale after target/threat transition.  
**Reassessment:** timer, target change, military superiority change, projectile/threat event.

**AEGIS insertion:** military decision layer feeding existing `militaryBehavior.per`; do not duplicate its operational writers.

**Priority:** P1.

---

# 10. Proactive infrastructure / defensive state

## Promisory sources

`buildings.per`, `init.per`, `threats.per`, `general.per`.

Direct mechanisms include:

- `up-set-defense-priority`
- `up-set-offense-priority`
- `sn-town-defend-priority`
- `sn-gold-defend-priority`
- `sn-stone-defend-priority`
- `sn-forage-defend-priority`
- `sn-relic-defend-priority`
- `sn-livestock-defend-priority`
- `sn-defense-distance`
- `sn-defend-overlap-distance`
- `sn-wall-targeting-mode`
- `sn-enable-offensive-priority`
- `up-pending-placement`
- defensive-object searches

Promisory also searches for nearby enemy defensive structures and can delete dangerous/failed foundations before they become destroyed or strategically harmful.

## Contract

**Observation:** threat, infrastructure, map geometry, pending foundations.  
**Classification:** exposed economic site / defensive requirement / unsafe construction.  
**State:** defense requirement and placement priority.  
**Authorization:** threat/position policy plus build feasibility.  
**Execution:** construction/target-priority channels.  
**Verification:** completed defensive object or changed target priority.  
**Failure:** no placement, insufficient resources, threat changes, builder loss.  
**Expiry:** defensive requirement disappears or location becomes obsolete.  
**Reassessment:** threat event, construction completion/failure, enemy movement.

**AEGIS insertion:** defensive policy above the existing construction executor.

**Priority:** P1/P2.

---

# 11. Cross-generation symbol map

| Functional state | HD evidence | Promisory | AIBuilder | AEGIS disposition |
|---|---|---|---|---|
| Current phase | phase/age goals | init + specialized modules | `phaseUpdate` | **preserve** |
| Resource allocation | gatherer SNs | `gatherers.per` | economy/phase | **extend, don't replace** |
| Threat timestamp/source | threat primitive | `gl-threat-*` | absent | **add observation layer** |
| Enemy capability | unit-count/facts | weighted family SNs | partial | **add classification** |
| Explorer demand | explorer SNs | general/scoutcontrol | general/phase | **preserve owner** |
| Scout tactical state | native scout actions | scoutcontrol | basic | **overlay carefully** |
| Boar state | hunting logic | boarhunting | limited | **vertical slice** |
| Escrow | native escrow | escrow state machine | strong research support | **reuse native ABI** |
| Pending construction | build state | buildings | construction | **formalize** |
| Search/geometry | native search | pervasive | partial | **candidate layer** |
| Attack state | attack goals/SNs | general/units | militaryBehavior | **decision overlay** |
| Defense priorities | priorities | init/buildings | construction | **policy overlay** |

---

# 12. Writer/reader ownership rules for AEGIS

The audit establishes the following ownership constraints before any new `.per` implementation:

1. `phaseUpdate.per` remains the owner of phase-derived policy outputs.
2. `general.per` remains the owner of the AIBuilder explorer translation path.
3. `construction.per` remains the owner of normal building execution.
4. `economy.per` remains the owner of baseline economic allocation/execution.
5. `militaryUnits.per` remains the owner of unit-production execution.
6. `militaryBehavior.per` remains the owner of operational military behavior.
7. AEGIS observation modules may write **AEGIS-private state**, not native executor state, unless an explicit authority transfer is documented.
8. Native escrow remains the resource reservation mechanism.
9. Pending objects are evidence of an outstanding world-state transition, not proof of completion.
10. Every new AEGIS writer requires a corresponding reader/consumer and expiry/reassessment rule.

---

# 13. Ten insertion points, ranked

| Rank | Slice | Insertion point | Risk |
|---:|---|---|---|
| 1 | Threat telemetry | new AEGIS observation/classification layer before military policy | Low–medium |
| 2 | Pending construction contract | construction observation boundary | Low |
| 3 | Escrow authorization | existing economy/technology feasibility boundary | Medium |
| 4 | Scout information state | general/scout observation boundary | Medium |
| 5 | Boar support | gatherer/hunting boundary | Medium |
| 6 | Geometry candidate service | reusable AEGIS search state, consumer-specific | Medium |
| 7 | Gatherer continuity | economy worker-control boundary | Medium–high |
| 8 | Defensive infrastructure | construction policy boundary | Medium |
| 9 | Attack/retreat decision | military policy boundary | High |
| 10 | Full adaptive composition | multi-subsystem arbitration | Highest; defer |

---

# 14. What is NOT yet promoted

The following remain historical/analytical only:

- Promisory's full scout micro system.
- Promisory's full gatherer system.
- Promisory's complete boar state machine.
- Promisory's target-evaluation/scaling system.
- Promisory's full defensive search system.
- Any XS geometry implementation.
- Any wholesale Promisory load order.
- Any duplicate ownership of AIBuilder phase/explorer/construction/military writers.

---

# 15. Evidence gaps requiring later qualification

Static source analysis cannot prove several engine-time facts:

1. exact semantics of every `up-*` primitive under current AoE2DE build;
2. exact persistence/overwrite timing for some strategic-number writes;
3. whether a command accepted by the interpreter creates the intended world transition;
4. precise expiration semantics of every pending/search state;
5. undocumented interactions between native AIBuilder systems and new AEGIS writers.

These are **runtime ABI questions**, not reasons to weaken the static ledger.

---

# 16. Promotion gate

No mechanic from this ledger should be promoted directly from historical source into production.

Required promotion sequence:

```text
DIRECT SOURCE RULE
→ FUNCTIONAL CONTRACT
→ SYMBOL/WRITER/READER GRAPH
→ AIBuilder CHANNEL MATCH
→ AEGIS PRIVATE STATE
→ AUTHORIZATION
→ EXISTING EXECUTOR
→ PENDING EVIDENCE
→ COMPLETION EVIDENCE
→ FAILURE/EXPIRY
→ REASSESSMENT
→ STATIC QUALIFICATION
→ BOUNDED RUNTIME QUALIFICATION
→ PROMOTION
```

This is the canonical source-rule discipline for the ten capabilities.

## 17. Immediate implementation recommendation

The first implementation should be **Threat Telemetry → Threat Classification**, not counter-unit production.

Reason: Promisory directly demonstrates the observation and classification machinery, while AEGIS already has a strategic `THREAT → CAPABILITY` research objective. This lets AEGIS establish a trustworthy state layer without immediately taking ownership of `militaryUnits.per`.

The second should be **Pending Construction Lifecycle**, because AIBuilder already possesses the executor and pending-object mechanism. It offers the cleanest demonstration of:

```text
intent → authorization → execution → pending → completion → reassessment
```

Only after those two contracts are stable should AEGIS begin modifying tactical production decisions.
