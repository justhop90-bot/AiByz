# AoE2DE Practical Coding Knowledge Base — Deep QC Pass 1

**Date:** 2026-09-04  
**Status:** Deep-review audit / expansion backlog  
**Target:** `AOE2DE_PRACTICAL_CODING_KNOWLEDGE_BASE.md`  
**Source basis:** verified `AI (HD version).per` + verified Promisory source  
**Runtime boundary:** current DE execution semantics remain governed by Layer-1 evidence.

## Purpose

This is an adversarial quality-control pass over the practical coding catalogue. For **every section**, twenty independent additions/questions were generated. Each probes a different engineering dimension: syntax, state, ownership, game meaning, timing, resources, feasibility, failure, observability, performance, interaction, or AEGIS migration.

A section is not implementation-ready merely because it has a historical solution. The deeper standard is:

`GAME PROBLEM -> OBSERVATION -> STATE/BELIEF -> REQUIREMENT -> CANDIDATES -> CONSTRAINTS -> RESOURCE/TIMING TAX -> COMMITMENT -> AUTHORITY -> ACTION -> POSTCONDITION -> FAILURE DIAGNOSIS -> RECOVERY -> REASSESSMENT`

### Review labels

- **ADD** — missing practical content that should become part of the knowledge base.
- **VERIFY** — claim should be tied to exact source evidence or engine evidence before promotion.
- **DEEPEN** — existing idea is correct but underspecified.
- **SEPARATE** — concepts currently conflated should be split.
- **GENERALIZE** — historical implementation should be abstracted into an AEGIS concept.
- **GUARD** — identify an edge case, race, oscillation, stale-state, or authority hazard.
- **MEASURE** — define an observable metric or validation experiment.

---

# 1. Mandatory design questions for every subsystem

1. **DEEPEN:** Add a formal distinction between observation, classification, belief, requirement, commitment, authority, action, and postcondition.
2. **ADD:** Require an explicit state-owner field for every persistent variable.
3. **ADD:** Require the set of readers and writers for every strategic state channel.
4. **ADD:** Require entry conditions, persistence conditions, exit conditions, and cooldown conditions for state machines.
5. **ADD:** Require the resource opportunity cost of the subsystem.
6. **ADD:** Require the production/infrastructure opportunity cost.
7. **ADD:** Require the information dependency and minimum evidence quality.
8. **ADD:** Require the strategic objective in game terms, not implementation terms.
9. **ADD:** Require the expected opponent response and at least one counter-transition.
10. **ADD:** Require explicit failure signatures rather than a generic action-failed branch.
11. **ADD:** Require a measurable postcondition for side-effecting actions.
12. **ADD:** Require a stale-information policy and expiry mechanism.
13. **ADD:** Require an authority rule when multiple controllers want incompatible outcomes.
14. **ADD:** Require a performance budget for expensive searches or fact aggregation.
15. **ADD:** Require an evidence grade for historical interpretations.
16. **VERIFY:** Identify which fields are actually representable in `.per` versus AEGIS-only abstractions.
17. **ADD:** Include transition cost, not only static cost.
18. **ADD:** Include optionality preserved/lost by the decision.
19. **MEASURE:** Define what replay or runtime telemetry would falsify the strategic hypothesis.
20. **GENERALIZE:** Make this checklist a machine-readable subsystem specification template.

# 2. Constants and namespaces

1. **VERIFY:** Inventory every constant family actually used by HD/Promisory: unit, building, technology, goal, SN, age, map, timer, scratch state.
2. **ADD:** Record source file and line range for each important constant.
3. **ADD:** Record valid numeric range where engine-dependent.
4. **ADD:** Record whether a constant is engine-provided, source-defined, or compatibility-defined.
5. **GUARD:** Flag collisions between custom constants and engine identifiers.
6. **VERIFY:** Document load order and overwrite behavior using exact source evidence.
7. **ADD:** Distinguish semantic constants from scratch-register allocations.
8. **ADD:** Mark constants that are temporary, permanent, experimental, or obsolete.
9. **ADD:** Track patch sensitivity for every engine-facing constant.
10. **ADD:** Record consumers and writers of important state constants.
11. **DEEPEN:** Explain why symbolic names reduce archaeology risk but do not guarantee semantic correctness.
12. **GUARD:** Identify numeric constants that look symbolic but are actually encoded modes.
13. **ADD:** Define naming conventions for goals, SNs, timers, modes, and capabilities.
14. **ADD:** Define reserved ranges for AEGIS-owned state.
15. **VERIFY:** Cross-check suspicious identifiers against Layer-1 engine evidence.
16. **ADD:** Require a registry entry before introducing a new magic number.
17. **ADD:** Document namespace migration when historical constants are replaced.
18. **ADD:** Include serialization/debug representation for important state.
19. **MEASURE:** Add a duplicate/collision scan to CI.
20. **GENERALIZE:** Build a constant ledger that can generate validation artifacts automatically.

# 3. Initialization / bootstrap

1. **DEEPEN:** Separate immutable configuration from mutable strategic state.
2. **ADD:** Define initialization ordering dependencies.
3. **ADD:** Define what must be initialized before the first strategic evaluation.
4. **ADD:** Define the bootstrap completion signal.
5. **ADD:** Define behavior if initialization is partially interrupted.
6. **GUARD:** Prevent normal rules from firing against uninitialized state.
7. **ADD:** Record default values and why each default is strategically safe.
8. **ADD:** Distinguish engine defaults from AI-selected defaults.
9. **ADD:** Define map/player identity initialization.
10. **ADD:** Define age/population/resource baseline capture.
11. **ADD:** Define initial scouting/information state.
12. **ADD:** Define initial strategic doctrine and difficulty capability.
13. **ADD:** Define initial timers and why they start armed/disarmed.
14. **ADD:** Define initial production authorization.
15. **ADD:** Define initial reservation/escrow state.
16. **GUARD:** Ensure initialization is idempotent or explicitly one-shot.
17. **VERIFY:** Identify HD initialization sections and exact state they establish.
18. **ADD:** Add a bootstrap diagnostic snapshot.
19. **MEASURE:** Define a first-valid-decision test.
20. **GENERALIZE:** Model bootstrap as a lifecycle state machine rather than a pile of setup rules.

# 4. Strategic state

1. **DEEPEN:** Define each state channel by semantic type rather than only numeric value.
2. **ADD:** Document legal state values and illegal values.
3. **ADD:** Map every major writer and reader.
4. **ADD:** Identify competing writers and arbitration order.
5. **ADD:** Identify state that is tactical versus strategic.
6. **ADD:** Identify state that is belief versus fact.
7. **ADD:** Identify state that represents intent versus authority.
8. **ADD:** Add transition diagrams for strategy, attack, retreat, and control.
9. **GUARD:** Detect oscillation between two valid strategy states.
10. **ADD:** Define state persistence across game-time intervals.
11. **ADD:** Define when state becomes stale.
12. **ADD:** Define state reset semantics.
13. **ADD:** Define state replacement semantics.
14. **ADD:** Define priority between broad strategy and emergency override.
15. **ADD:** Track confidence in inferred enemy state.
16. **VERIFY:** Tie important state semantics to exact HD comments or writer-reader evidence.
17. **ADD:** Document which state should survive a tactical failure.
18. **ADD:** Document which state must be invalidated after major world changes.
19. **MEASURE:** Add state-transition traces to replay analysis.
20. **GENERALIZE:** Replace anonymous goals with typed strategic state in AEGIS.

# 5. Strategic numbers

1. **VERIFY:** Inventory all strategically important SNs used by the source.
2. **ADD:** Classify each SN as engine setting, policy input, state, or control interface.
3. **ADD:** Record valid range and current-build sensitivity.
4. **ADD:** Record side effects of changing each SN.
5. **ADD:** Record which modules consume each SN.
6. **ADD:** Record whether changes are immediate or sampled later.
7. **GUARD:** Identify SNs whose writers can fight each other.
8. **ADD:** Document reset/default semantics.
9. **ADD:** Document whether SN values persist across games or initialization cycles.
10. **VERIFY:** Separate historical semantics from current DE semantics.
11. **ADD:** Identify SNs used as hidden communication channels.
12. **ADD:** Identify SNs that encode enumerations versus continuous values.
13. **ADD:** Add validation for out-of-range writes.
14. **ADD:** Add observability for unexpected SN mutation.
15. **ADD:** Record temporal ownership of SNs.
16. **ADD:** Identify performance-sensitive SN changes.
17. **ADD:** Explain when an SN is a legitimate engine interface versus architectural state debt.
18. **ADD:** Define migration rules for replacing SN state with typed AEGIS state.
19. **MEASURE:** Test whether intended SN writes produce expected downstream effects.
20. **GENERALIZE:** Maintain a versioned SN semantic registry.

# 6. Enemy classification

1. **DEEPEN:** Separate observed enemy facts from inferred strategy.
2. **ADD:** Give each classification confidence.
3. **ADD:** Record evidence supporting classification.
4. **ADD:** Record evidence that would contradict it.
5. **ADD:** Define classification expiry.
6. **ADD:** Define competing enemy hypotheses.
7. **ADD:** Define minimum evidence threshold before strategic commitment.
8. **ADD:** Model enemy commitments as constraints on future spending.
9. **ADD:** Include timing as a classification feature.
10. **ADD:** Include infrastructure as a capability indicator.
11. **ADD:** Include absence of expected infrastructure as evidence.
12. **ADD:** Include map/position context.
13. **GUARD:** Prevent one stale sighting from permanently defining enemy strategy.
14. **ADD:** Define transition detection: rush -> boom, cavalry -> siege, water -> land, etc.
15. **ADD:** Record false-positive and false-negative costs.
16. **VERIFY:** Trace exact HD classification branches and self-disabling behavior.
17. **ADD:** Distinguish enemy composition from enemy intent.
18. **ADD:** Distinguish local threat from global enemy strategy.
19. **MEASURE:** Score classification accuracy against replay ground truth.
20. **GENERALIZE:** Build an opponent-belief model rather than a single enemy label.

# 7. Threat detection

1. **DEEPEN:** Define threat by source, mechanism, target, severity, and time horizon.
2. **ADD:** Distinguish detected threat from confirmed threat.
3. **ADD:** Define threat persistence.
4. **ADD:** Define threat escalation/de-escalation.
5. **ADD:** Define local versus strategic threat.
6. **ADD:** Include economic threats such as denial or raid exposure.
7. **ADD:** Include technological threats.
8. **ADD:** Include infrastructure threats.
9. **ADD:** Include information threats caused by scouting uncertainty.
10. **ADD:** Define required counter-capability for each threat class.
11. **ADD:** Define non-military responses.
12. **ADD:** Define response urgency.
13. **GUARD:** Prevent overreaction to transient sightings.
14. **GUARD:** Prevent underreaction when multiple weak signals compound.
15. **ADD:** Record threat source/target relationship.
16. **VERIFY:** Tie threat branches to exact source modules.
17. **ADD:** Define threat resolution criteria.
18. **ADD:** Define threat memory and expiry.
19. **MEASURE:** Evaluate false alarm rate and missed-threat rate.
20. **GENERALIZE:** Treat threat detection as belief generation feeding capability selection.

# 8. Resource allocation

1. **DEEPEN:** Replace static ratios with marginal strategic demand.
2. **ADD:** Separate current stock from expected income.
3. **ADD:** Track committed resources.
4. **ADD:** Track free resources.
5. **ADD:** Track resources in transit through future gathering.
6. **ADD:** Include villager travel time.
7. **ADD:** Include worker safety/exposure.
8. **ADD:** Include dropsite/infrastructure cost.
9. **ADD:** Include resource-source depletion.
10. **ADD:** Include timing deadlines.
11. **ADD:** Include production queue demand.
12. **ADD:** Include research demand.
13. **ADD:** Include reserve policy.
14. **GUARD:** Prevent allocation oscillation around thresholds.
15. **ADD:** Define reallocation hysteresis.
16. **VERIFY:** Map HD gatherer percentages to strategic conditions.
17. **ADD:** Explain temporary/sentinel goal mechanisms.
18. **MEASURE:** Compare allocation decisions to achieved capability timings.
19. **ADD:** Define starvation signatures for each resource.
20. **GENERALIZE:** Model workers as a resource-generation control surface.

# 9. Resource reservation / escrow

1. **DEEPEN:** Define reservation versus physical resource possession.
2. **ADD:** Define reservation owner.
3. **ADD:** Define reservation purpose.
4. **ADD:** Define reservation priority.
5. **ADD:** Define reservation deadline.
6. **ADD:** Define reservation release condition.
7. **ADD:** Define reservation cancellation condition.
8. **ADD:** Define conflict arbitration between reservations.
9. **ADD:** Define partial funding behavior.
10. **ADD:** Define what happens when a reservation becomes impossible.
11. **ADD:** Define emergency override rules.
12. **ADD:** Define reserved-resource visibility to production.
13. **GUARD:** Prevent dead reservations from starving the economy.
14. **GUARD:** Prevent two controllers from believing the same stock is free.
15. **VERIFY:** Trace `escrow.per` release/reset and research branches.
16. **ADD:** Explain escrow flag lifecycle.
17. **MEASURE:** Test whether reservations improve timing reliability.
18. **ADD:** Model reservation opportunity cost.
19. **ADD:** Model reserve decay as the deadline approaches or passes.
20. **GENERALIZE:** Build an explicit resource commitment ledger.

# 10. Feasibility checks

1. **DEEPEN:** Separate strategic desirability from mechanical feasibility.
2. **ADD:** Enumerate prerequisite classes: age, tech, building, resources, population, placement, target, path.
3. **ADD:** Distinguish temporarily infeasible from permanently infeasible.
4. **ADD:** Distinguish infeasible from currently unknown.
5. **ADD:** Define feasibility freshness.
6. **ADD:** Define precondition and postcondition separately.
7. **GUARD:** Never treat an earlier feasibility result as perpetual.
8. **ADD:** Define pending-action interaction.
9. **ADD:** Define race between resource arrival and another spend.
10. **ADD:** Define race between prerequisite completion and command issuance.
11. **VERIFY:** Inventory actual `can-*` patterns in HD/Promisory.
12. **ADD:** Identify actions with hidden engine preconditions.
13. **ADD:** Record failure signatures when a `can-*` test passes but execution fails.
14. **ADD:** Define fallback candidate generation.
15. **ADD:** Define authority check at side-effect boundary.
16. **MEASURE:** Build feasibility-versus-success telemetry.
17. **ADD:** Explain why command success must not be inferred from predicate success.
18. **ADD:** Define feasibility under uncertainty.
19. **ADD:** Define resource reservation as part of feasibility.
20. **GENERALIZE:** Treat feasibility as a live gate, not a planning fact.

# 11. Production authorization

1. **DEEPEN:** Separate capability demand from unit queue commands.
2. **ADD:** Define production-capability owner.
3. **ADD:** Define desired force composition.
4. **ADD:** Define replacement demand after casualties.
5. **ADD:** Define reinforcement demand during active pressure.
6. **ADD:** Define production infrastructure capacity.
7. **ADD:** Define technology prerequisites.
8. **ADD:** Define resource reservation interaction.
9. **ADD:** Define queue competition.
10. **ADD:** Define emergency production override.
11. **ADD:** Define minimum viable batch size.
12. **ADD:** Define production cancellation policy.
13. **GUARD:** Prevent production flags from oscillating every cycle.
14. **GUARD:** Prevent one controller from enabling a unit another controller disabled.
15. **VERIFY:** Trace HD unit flags and unit-goal coupling.
16. **ADD:** Define production verification: queue accepted, unit spawned, capability realized.
17. **ADD:** Define infrastructure expansion trigger.
18. **ADD:** Define production saturation and resource starvation signatures.
19. **MEASURE:** Track capability requested versus actually delivered.
20. **GENERALIZE:** Build production as a capability pipeline with explicit authority.

# 12. Technology / research

1. **DEEPEN:** Define technology as a future capability transition.
2. **ADD:** Record immediate and delayed benefits.
3. **ADD:** Record opportunity cost.
4. **ADD:** Record timing deadline.
5. **ADD:** Record prerequisites.
6. **ADD:** Record affected units/buildings/economy.
7. **ADD:** Record reservation requirements.
8. **ADD:** Record alternative technologies competing for resources.
9. **ADD:** Define emergency research overrides.
10. **ADD:** Define stale research intent.
11. **GUARD:** Prevent research from starving an urgent military transition.
12. **VERIFY:** Trace escrow flags and `can-research-with-escrow` branches.
13. **ADD:** Define pending research state.
14. **ADD:** Define completion verification.
15. **ADD:** Define post-research state update.
16. **ADD:** Define research failure/retry behavior.
17. **ADD:** Define technology substitution candidates.
18. **MEASURE:** Compare research timing against capability timing.
19. **ADD:** Include map/opponent dependency.
20. **GENERALIZE:** Evaluate technology as an investment candidate rather than a checklist item.

# 13. Buildings / infrastructure

1. **DEEPEN:** Distinguish prerequisite infrastructure from strategic infrastructure.
2. **ADD:** Define building purpose and capability gained.
3. **ADD:** Define placement objective.
4. **ADD:** Define candidate placement generation.
5. **ADD:** Define placement scoring.
6. **ADD:** Include worker travel time.
7. **ADD:** Include exposure and defensive value.
8. **ADD:** Include reinforcement/production geometry.
9. **ADD:** Include resource protection value.
10. **ADD:** Define pending construction state.
11. **ADD:** Define interruption/failure states.
12. **ADD:** Define rebuild threshold.
13. **GUARD:** Prevent duplicate buildings during pending construction.
14. **VERIFY:** Trace documented backup/rebuild behavior in `buildings.per`.
15. **ADD:** Explain `extremebuildings2.per` as a specialized/conditional path.
16. **ADD:** Define fallback placement candidates.
17. **ADD:** Define demolition/replacement logic where applicable.
18. **MEASURE:** Track placement success and strategic utility.
19. **ADD:** Define infrastructure tax on resources and builders.
20. **GENERALIZE:** Treat buildings as nodes in the capability graph, not static prerequisites.

# 14. Housing / population infrastructure

1. **DEEPEN:** Model housing as production capacity.
2. **ADD:** Forecast population demand rather than using only current cap.
3. **ADD:** Include queued units.
4. **ADD:** Include villager production.
5. **ADD:** Include military batch plans.
6. **ADD:** Include building time.
7. **ADD:** Include builder availability.
8. **ADD:** Define safe-capacity buffer.
9. **ADD:** Define emergency housing threshold.
10. **GUARD:** Prevent overbuilding housing that consumes critical wood.
11. **ADD:** Define pending-house state.
12. **ADD:** Define failed placement recovery.
13. **VERIFY:** Trace historical housing goals and thresholds.
14. **ADD:** Define housing demand under population surges.
15. **ADD:** Define interaction with trade/late game.
16. **ADD:** Define interaction with production bursts.
17. **MEASURE:** Track idle production caused by housing failure.
18. **ADD:** Define housing priority relative to military infrastructure.
19. **ADD:** Define map/position considerations for housing.
20. **GENERALIZE:** Forecast population capacity as a production constraint.

# 15. Economy / dropsites / gatherer logistics

1. **DEEPEN:** Define effective gather rate rather than nominal gather rate.
2. **ADD:** Include walking distance.
3. **ADD:** Include dropsite wait time.
4. **ADD:** Include resource contention.
5. **ADD:** Include worker safety.
6. **ADD:** Include defensive coverage.
7. **ADD:** Include infrastructure construction cost.
8. **ADD:** Include source depletion.
9. **ADD:** Include map topology.
10. **ADD:** Include raid risk.
11. **ADD:** Define dropsite candidate scoring.
12. **ADD:** Define relocation/reassignment triggers.
13. **GUARD:** Prevent oscillation between nearby dropsites.
14. **VERIFY:** Map HD dropsite distance settings to their strategic consumers.
15. **ADD:** Define economic failure signatures.
16. **ADD:** Define redundancy for threatened resource lines.
17. **MEASURE:** Track effective resources/minute rather than assignments alone.
18. **ADD:** Model infrastructure as a time-to-payback decision.
19. **ADD:** Define interaction with map control.
20. **GENERALIZE:** Treat economic logistics as part of strategic capability production.

# 16. Food acquisition / boar / hunting

1. **DEEPEN:** Define food-source value by timing, safety, and throughput.
2. **ADD:** Track source availability.
3. **ADD:** Track worker assignment.
4. **ADD:** Track travel time.
5. **ADD:** Track danger/exposure.
6. **ADD:** Define hunt-target selection.
7. **ADD:** Define worker count selection.
8. **ADD:** Define escort/safety policy.
9. **ADD:** Define source transition trigger.
10. **ADD:** Define failure signatures such as lost source or interrupted task.
11. **VERIFY:** Trace boar-hunting state transitions in `boarhunting.per`.
12. **ADD:** Define interaction with age-up timing.
13. **ADD:** Define interaction with scouting information.
14. **GUARD:** Prevent overcommitment of villagers to a transient food source.
15. **ADD:** Define fallback food sources.
16. **ADD:** Define resource tax of protecting the hunt.
17. **MEASURE:** Compare food-source choices to villager uptime and age timing.
18. **ADD:** Define map-specific source quality.
19. **ADD:** Define transition from hunted to renewable food.
20. **GENERALIZE:** Model food acquisition as a timed capability pipeline.

# 17. Farms / renewable food

1. **DEEPEN:** Model farms as wood-to-food conversion over time.
2. **ADD:** Define when a farm is strategically justified.
3. **ADD:** Include immediate wood opportunity cost.
4. **ADD:** Include expected farm lifetime.
5. **ADD:** Include worker travel/placement.
6. **ADD:** Include food demand forecast.
7. **ADD:** Include farming infrastructure.
8. **ADD:** Define farm reserve threshold.
9. **ADD:** Define emergency farm trigger.
10. **GUARD:** Prevent farm spam from starving houses/production.
11. **VERIFY:** Trace `farm-goal` and `save-wood-goal` interactions.
12. **ADD:** Define source exhaustion detection.
13. **ADD:** Define farm transition hysteresis.
14. **ADD:** Define map-specific farm feasibility.
15. **ADD:** Define defensive placement value.
16. **ADD:** Define replacement/maintenance behavior.
17. **MEASURE:** Track idle TC time caused by food shortage.
18. **ADD:** Compare farm timing to alternative food sources.
19. **ADD:** Define late-game farm economy transition.
20. **GENERALIZE:** Treat renewable food as an economic infrastructure investment.

# 18. Scouting / exploration

1. **DEEPEN:** Define information value in terms of decisions it can change.
2. **ADD:** Maintain explicit information gaps.
3. **ADD:** Score candidate scouting regions.
4. **ADD:** Include route safety.
5. **ADD:** Include travel time.
6. **ADD:** Include expected information gain.
7. **ADD:** Include expiration of old observations.
8. **ADD:** Define scouting priorities by game phase.
9. **ADD:** Define enemy-transition scouting triggers.
10. **ADD:** Define economic scouting triggers.
11. **VERIFY:** Trace `scoutcontrol.per` candidate/pivot/path logic.
12. **ADD:** Explain documented performance tradeoff in path analysis.
13. **ADD:** Define scouting group lifecycle.
14. **ADD:** Define lost/dead scout recovery.
15. **ADD:** Define information confidence.
16. **GUARD:** Prevent scouting a low-value region while a high-value uncertainty remains.
17. **ADD:** Define waypoint failure behavior.
18. **MEASURE:** Score scouting by decisions improved, not tiles covered.
19. **ADD:** Define scout-to-strategy feedback latency.
20. **GENERALIZE:** Model scouting as active information acquisition.

# 19. Candidate search / object selection

1. **DEEPEN:** Define candidate-generation versus candidate-evaluation separately.
2. **ADD:** Define candidate eligibility constraints.
3. **ADD:** Define scoring features.
4. **ADD:** Define feature normalization where needed.
5. **ADD:** Define tie-breaking.
6. **ADD:** Define uncertainty in candidate score.
7. **ADD:** Define search termination.
8. **ADD:** Define empty-candidate behavior.
9. **ADD:** Define stale-candidate invalidation.
10. **ADD:** Define search reset.
11. **VERIFY:** Trace `general.per` search state and jump loop.
12. **ADD:** Document scratch-goal usage as an implementation constraint.
13. **GUARD:** Prevent search state leakage into the next decision.
14. **ADD:** Define performance budget.
15. **ADD:** Define approximate-search fallback.
16. **ADD:** Define candidate diversity so the search does not converge on one class.
17. **MEASURE:** Compare search quality to exhaustive/reference search where possible.
18. **ADD:** Define candidate provenance for debugging.
19. **ADD:** Define how candidate scores feed commitment decisions.
20. **GENERALIZE:** Make candidate tournaments a reusable AEGIS service.

# 20. Distance / geometry

1. **DEEPEN:** Distinguish Euclidean distance from travel distance.
2. **ADD:** Include path obstruction.
3. **ADD:** Include terrain/water constraints.
4. **ADD:** Include enemy control zones where observable.
5. **ADD:** Include reinforcement time.
6. **ADD:** Include retreat route quality.
7. **ADD:** Include building placement geometry.
8. **ADD:** Include economic travel cost.
9. **ADD:** Include attack-range geometry.
10. **ADD:** Include line-of-sight implications where supported.
11. **VERIFY:** Identify exact distance mechanisms used by HD/Promisory.
12. **ADD:** Define approximation when exact path distance is expensive.
13. **GUARD:** Prevent geometric assumptions from surviving map-state changes.
14. **ADD:** Define geometry cache invalidation.
15. **ADD:** Define candidate-point generation.
16. **ADD:** Define local versus global geometry.
17. **MEASURE:** Compare predicted travel times with observed movement.
18. **ADD:** Define geometric failure signatures.
19. **ADD:** Define position as an input to strategic capability evaluation.
20. **GENERALIZE:** Treat geometry as a constraint layer between strategy and execution.

# 21. Tactical target selection

1. **DEEPEN:** Separate target eligibility from target scoring.
2. **ADD:** Include strategic objective.
3. **ADD:** Include target value.
4. **ADD:** Include target danger.
5. **ADD:** Include expected time-to-kill.
6. **ADD:** Include retaliation risk.
7. **ADD:** Include overkill/wasted damage.
8. **ADD:** Include target mobility.
9. **ADD:** Include range/position interaction.
10. **ADD:** Include siege/fortification context.
11. **VERIFY:** Trace HD target-evaluation variables and DUC/search consumers.
12. **ADD:** Define target lock duration.
13. **GUARD:** Prevent target oscillation between near-equal candidates.
14. **ADD:** Define retarget triggers.
15. **ADD:** Define target disappearance/failure handling.
16. **ADD:** Define engagement-geometry constraints where relevant.
17. **MEASURE:** Compare target selection to strategic damage and survival outcomes.
18. **ADD:** Define target candidate provenance.
19. **ADD:** Distinguish tactical target from strategic objective.
20. **GENERALIZE:** Build target selection as a candidate decision service.

# 22. Attack state machine

1. **DEEPEN:** Define explicit attack states and legal transitions.
2. **ADD:** Define preparation state.
3. **ADD:** Define authorization state.
4. **ADD:** Define movement state.
5. **ADD:** Define engagement state.
6. **ADD:** Define assessment state.
7. **ADD:** Define regroup state.
8. **ADD:** Define retreat state.
9. **ADD:** Define cooldown state.
10. **ADD:** Define restart state.
11. **VERIFY:** Trace attack-goal, attack-status-goal, retreat-now-goal, restart-attack-goal.
12. **ADD:** Define target ownership.
13. **ADD:** Define force-readiness threshold.
14. **ADD:** Define attack expiration.
15. **GUARD:** Prevent attack state from persisting after force destruction.
16. **ADD:** Define strategic cancellation versus tactical interruption.
17. **ADD:** Define post-attack verification.
18. **MEASURE:** Track attack conversion efficiency.
19. **ADD:** Define opponent-response feedback.
20. **GENERALIZE:** Implement attack as a lifecycle controller, not a boolean.

# 23. Retreat / regroup

1. **DEEPEN:** Define retreat as a capability-preservation decision.
2. **ADD:** Define local military deficit.
3. **ADD:** Define retreat route quality.
4. **ADD:** Define reinforcement time.
5. **ADD:** Define target opportunity cost.
6. **ADD:** Define regroup location.
7. **ADD:** Define minimum regroup strength.
8. **ADD:** Define pursuit risk.
9. **ADD:** Define timer/cooldown.
10. **ADD:** Define conditions for returning to attack.
11. **VERIFY:** Trace retreat and restart logic.
12. **GUARD:** Prevent retreat loops that never re-engage or transition.
13. **ADD:** Define tactical retreat versus strategic withdrawal.
14. **ADD:** Define partial retreat/group splitting.
15. **ADD:** Define damaged-unit handling.
16. **ADD:** Define information update during retreat.
17. **MEASURE:** Compare retreat decisions to preserved military value.
18. **ADD:** Define failure signatures: blocked route, destroyed regroup point, pursuit.
19. **ADD:** Define fallback target after retreat.
20. **GENERALIZE:** Model retreat as an option-preserving transition.

# 24. Fortification-aware attack

1. **DEEPEN:** Classify the defensive mechanism before selecting a response.
2. **ADD:** Distinguish walls, towers, castles, and other defensive geometries.
3. **ADD:** Estimate required capability.
4. **ADD:** Estimate current capability.
5. **ADD:** Define siege requirement.
6. **ADD:** Define alternative target/route.
7. **ADD:** Define economic denial alternative.
8. **ADD:** Define waiting/technology transition alternative.
9. **ADD:** Define timing window.
10. **ADD:** Define attack suspension criteria.
11. **VERIFY:** Trace `enemy-fortifications-goal` and related siege logic.
12. **ADD:** Define fortification memory.
13. **GUARD:** Prevent repeated futile attacks.
14. **ADD:** Define post-siege reassessment.
15. **ADD:** Define defensive structure destruction verification.
16. **ADD:** Define repair/rebuild implications if observable.
17. **MEASURE:** Track losses avoided by suspension.
18. **ADD:** Define local versus strategic fortification effect.
19. **ADD:** Define target switching policy.
20. **GENERALIZE:** Model fortifications as capability barriers, not just target objects.

# 25. Military capability / unit selection

1. **DEEPEN:** Define capability requirements before unit selection.
2. **ADD:** Include enemy composition.
3. **ADD:** Include enemy technology.
4. **ADD:** Include map geometry.
5. **ADD:** Include current technology.
6. **ADD:** Include production capacity.
7. **ADD:** Include resource commitments.
8. **ADD:** Include timing window.
9. **ADD:** Include reinforcement distance.
10. **ADD:** Include transition cost from current army.
11. **VERIFY:** Trace `unit-goal` coupling across HD modules.
12. **ADD:** Define multiple candidate responses, not a single counter.
13. **ADD:** Define composition thresholds and confidence.
14. **GUARD:** Prevent counter-switching on noisy enemy observations.
15. **ADD:** Define replacement and reinforcement policy.
16. **ADD:** Define technology substitution.
17. **MEASURE:** Evaluate capability against actual local relationship change.
18. **ADD:** Define military reserve policy.
19. **ADD:** Define interaction with strategic objective and map control.
20. **GENERALIZE:** Build a capability graph rather than a unit counter table.

# 26. Siege

1. **DEEPEN:** Define siege by strategic capability gained.
2. **ADD:** Distinguish anti-building and anti-mass capabilities.
3. **ADD:** Define prerequisite infrastructure.
4. **ADD:** Define technology requirements.
5. **ADD:** Define resource tax.
6. **ADD:** Define escort requirement.
7. **ADD:** Define target requirement.
8. **ADD:** Define timing value.
9. **ADD:** Define replacement cost.
10. **ADD:** Define mobility/position constraints.
11. **VERIFY:** Trace siege reservation and offensive checks.
12. **ADD:** Define siege vulnerability.
13. **ADD:** Define failure/recovery behavior.
14. **ADD:** Define when siege becomes obsolete.
15. **ADD:** Define alternate non-siege candidate.
16. **GUARD:** Prevent siege investment against a target that is no longer relevant.
17. **MEASURE:** Track siege investment versus strategic conversion.
18. **ADD:** Define siege reserve versus immediate siege production.
19. **ADD:** Define interaction with fortification-aware attack state.
20. **GENERALIZE:** Treat siege as a conditional transition in the capability graph.

# 27. Naval / water control

1. **DEEPEN:** Define water as a separate strategic theater.
2. **ADD:** Define naval economy.
3. **ADD:** Define naval production capacity.
4. **ADD:** Define transport capacity.
5. **ADD:** Define naval scouting.
6. **ADD:** Define naval combat capability.
7. **ADD:** Define low-HP force state.
8. **ADD:** Define retreat geometry.
9. **ADD:** Define remembered enemy strength.
10. **ADD:** Define local naval advantage.
11. **VERIFY:** Trace `watercontrol.per` action codes and group lifecycle.
12. **ADD:** Define water-map classification upstream.
13. **ADD:** Define dock/port infrastructure transitions.
14. **ADD:** Define landing/transport interaction.
15. **GUARD:** Prevent land-only assumptions from controlling naval units.
16. **ADD:** Define naval failure signatures.
17. **MEASURE:** Track naval control versus economic/transport outcomes.
18. **ADD:** Define water-to-land transition conditions.
19. **ADD:** Define enemy naval threat classification.
20. **GENERALIZE:** Build separate theater controllers sharing strategic authority.

# 28. Transport

1. **DEEPEN:** Define transport as logistics capability.
2. **ADD:** Define capacity demand.
3. **ADD:** Define route safety.
4. **ADD:** Define departure point.
5. **ADD:** Define destination.
6. **ADD:** Define escort requirement.
7. **ADD:** Define timing deadline.
8. **ADD:** Define embarkation state.
9. **ADD:** Define transit state.
10. **ADD:** Define disembarkation state.
11. **ADD:** Define transport loss failure signature.
12. **VERIFY:** Trace transport flags and naval consumers.
13. **GUARD:** Prevent repeated transport attempts after route invalidation.
14. **ADD:** Define partial-load policy.
15. **ADD:** Define return/retreat route.
16. **ADD:** Define cargo prioritization.
17. **MEASURE:** Track transport mission completion and army survival.
18. **ADD:** Define interaction with strategic attack state.
19. **ADD:** Define alternative land-route candidate.
20. **GENERALIZE:** Model transport as a committed logistics operation with postconditions.

# 29. Trade / late-game economy

1. **DEEPEN:** Define trade as a change in resource-generation topology.
2. **ADD:** Define trigger conditions.
3. **ADD:** Define infrastructure cost.
4. **ADD:** Define expected throughput.
5. **ADD:** Define map dependency.
6. **ADD:** Define safety/route dependency.
7. **ADD:** Define opportunity cost.
8. **ADD:** Define transition timing.
9. **ADD:** Define minimum viable trade scale.
10. **ADD:** Define saturation.
11. **VERIFY:** Trace `trade.per` consumers and triggers.
12. **ADD:** Define trade-versus-gather comparison.
13. **ADD:** Define trade disruption failure signatures.
14. **GUARD:** Prevent premature trade investment.
15. **ADD:** Define trade transition rollback where possible.
16. **ADD:** Define late-game reserve policy.
17. **MEASURE:** Compare trade investment to realized resource throughput.
18. **ADD:** Define interaction with team economy.
19. **ADD:** Define interaction with military composition.
20. **GENERALIZE:** Treat trade as an economic state transition, not a building toggle.

# 30. Diplomacy / allies / team context

1. **DEEPEN:** Model relationships explicitly.
2. **ADD:** Track ally capability.
3. **ADD:** Track enemy capability.
4. **ADD:** Track ally threat/need.
5. **ADD:** Track team strategic objective.
6. **ADD:** Track target coordination.
7. **ADD:** Track attack timing synchronization.
8. **ADD:** Track resource-transfer cost.
9. **ADD:** Track assistance priority.
10. **ADD:** Track team information quality.
11. **VERIFY:** Trace ally/enemy population fact-sum patterns in `tsa.per`.
12. **ADD:** Define local versus team-level authority.
13. **GUARD:** Prevent one player's tactical emergency from destroying team strategy without arbitration.
14. **ADD:** Define target ownership/coordination.
15. **ADD:** Define ally failure response.
16. **ADD:** Define communication/taunt inputs where applicable.
17. **MEASURE:** Track team conversion efficiency.
18. **ADD:** Define asymmetric roles such as flank/pocket.
19. **ADD:** Define team transition states.
20. **GENERALIZE:** Model team play as a relational capability graph.

# 31. Tribute / resource transfer

1. **DEEPEN:** Define tribute as a strategic conversion.
2. **ADD:** Define donor surplus.
3. **ADD:** Define recipient deficit.
4. **ADD:** Define recipient capability gain.
5. **ADD:** Define donor opportunity cost.
6. **ADD:** Define urgency.
7. **ADD:** Define transfer priority.
8. **ADD:** Define minimum reserve after transfer.
9. **ADD:** Define repeated-transfer cooldown.
10. **ADD:** Define transfer failure handling.
11. **VERIFY:** Trace `tribute-goal` and assistance logic.
12. **GUARD:** Prevent donation loops that permanently starve the donor.
13. **ADD:** Define strategic reason for transfer.
14. **ADD:** Define alternative self-production versus tribute.
15. **ADD:** Define team-level expected value.
16. **ADD:** Define emergency transfer authority.
17. **MEASURE:** Compare transferred resource to realized team capability.
18. **ADD:** Define information confidence in recipient need.
19. **ADD:** Define expiration of assistance requests.
20. **GENERALIZE:** Treat resource transfer as a portfolio allocation decision.

# 32. Timers / hysteresis

1. **DEEPEN:** Define timer purpose, not merely timer duration.
2. **ADD:** Classify timers as cooldown, dwell, timeout, retry, expiration, or memory.
3. **ADD:** Define timer owner.
4. **ADD:** Define timer start event.
5. **ADD:** Define timer expiration event.
6. **ADD:** Define behavior while armed.
7. **ADD:** Define behavior after expiration.
8. **ADD:** Define restart policy.
9. **ADD:** Define cancellation policy.
10. **ADD:** Define interaction with state transitions.
11. **VERIFY:** Trace representative HD timers and their lifecycle.
12. **GUARD:** Detect timers that can remain permanently armed.
13. **GUARD:** Detect timers that create stale strategic suppression.
14. **ADD:** Define threshold hysteresis separately from time hysteresis.
15. **ADD:** Define rate limiting for expensive searches.
16. **ADD:** Define temporal confidence decay.
17. **MEASURE:** Compare oscillation frequency with/without timer controls.
18. **ADD:** Define timer semantics for recovery.
19. **ADD:** Define timer semantics for opponent classification expiry.
20. **GENERALIZE:** Treat time as explicit controller memory.

# 33. Self-disabling rules

1. **DEEPEN:** Explain why self-disable is a control mechanism, not merely syntax.
2. **ADD:** Define the state transition that replaces the rule's eligibility.
3. **ADD:** Define what re-enables it.
4. **ADD:** Define whether re-enable is timer-, event-, or state-driven.
5. **GUARD:** Identify accidental permanent disablement.
6. **GUARD:** Identify multiple rules disabling each other.
7. **VERIFY:** Trace representative self-disabling patterns.
8. **ADD:** Separate one-shot initialization from recurring state transition.
9. **ADD:** Define replacement for self-disable in AEGIS.
10. **ADD:** Define authority implications.
11. **ADD:** Define observability of disable state.
12. **ADD:** Define failure recovery.
13. **ADD:** Define interaction with patch/load ordering.
14. **ADD:** Define performance rationale where relevant.
15. **ADD:** Define rule lifecycle states.
16. **MEASURE:** Detect rules that never become eligible again.
17. **ADD:** Detect rules that re-enable too aggressively.
18. **ADD:** Record whether disable encodes strategy state or merely control flow.
19. **GENERALIZE:** Replace hidden eligibility mutation with explicit state ownership where feasible.
20. **DOCUMENT:** Preserve historical self-disable as archaeology even after redesign.

# 34. Search loops / jumps

1. **DEEPEN:** Document exact control-flow semantics separately from strategic purpose.
2. **ADD:** Define loop initialization.
3. **ADD:** Define iteration state.
4. **ADD:** Define termination state.
5. **ADD:** Define jump destination.
6. **ADD:** Define state cleanup.
7. **GUARD:** Detect infinite or excessive loops.
8. **GUARD:** Detect stale search state.
9. **ADD:** Define nested-search interaction.
10. **ADD:** Define performance budget.
11. **VERIFY:** Cross-check `up-jump-rule` behavior against Layer-1 evidence.
12. **ADD:** Define candidate ordering.
13. **ADD:** Define empty-search behavior.
14. **ADD:** Define partial-search fallback.
15. **ADD:** Define search interruption semantics.
16. **MEASURE:** Count rule evaluations per search.
17. **ADD:** Define approximation threshold.
18. **ADD:** Define scratch-register allocation.
19. **GENERALIZE:** Encapsulate loops behind reusable search services in AEGIS.
20. **DOCUMENT:** Treat historical jumps as engine-shaped control flow, not normal application logic.

# 35. DUC / tactical object control

1. **DEEPEN:** Separate strategic authorization from object-level order issuance.
2. **ADD:** Define group ownership.
3. **ADD:** Define object eligibility.
4. **ADD:** Define target assignment.
5. **ADD:** Define waypoint assignment.
6. **ADD:** Define action priority.
7. **ADD:** Define command replacement semantics.
8. **GUARD:** Prevent stale orders from overriding new strategic authority.
9. **ADD:** Define command acknowledgement.
10. **ADD:** Define postcondition verification.
11. **VERIFY:** Cross-check DUC/search patterns against Layer-1 evidence.
12. **ADD:** Define tactical group lifecycle.
13. **ADD:** Define damaged/isolated object handling.
14. **ADD:** Define order conflict arbitration.
15. **ADD:** Define tactical timeout.
16. **ADD:** Define target disappearance behavior.
17. **MEASURE:** Track command-to-observed-result latency.
18. **ADD:** Define tactical failure signatures.
19. **ADD:** Define escalation back to strategic controller.
20. **GENERALIZE:** Implement DUC as an execution plane beneath strategic authority.

# 36. Pending-state management

1. **DEEPEN:** Define lifecycle `requested -> accepted/rejected -> pending -> completed/failed -> verified`.
2. **ADD:** Define operation identity.
3. **ADD:** Define operation owner.
4. **ADD:** Define expected completion condition.
5. **ADD:** Define timeout.
6. **ADD:** Define cancellation.
7. **ADD:** Define replacement.
8. **GUARD:** Prevent duplicate requests.
9. **GUARD:** Prevent stale pending state.
10. **ADD:** Define partial completion.
11. **VERIFY:** Inventory pending checks across buildings/research/production.
12. **ADD:** Define failure reason taxonomy.
13. **ADD:** Define resource reservation interaction.
14. **ADD:** Define authority during pending state.
15. **ADD:** Define what strategic changes invalidate an operation.
16. **MEASURE:** Track pending duration and failure rate.
17. **ADD:** Define retry backoff.
18. **ADD:** Define alternate candidate after failure.
19. **ADD:** Define postcondition observation source.
20. **GENERALIZE:** Treat asynchronous actions as explicit objects, not inferred facts.

# 37. Failure and fallback

1. **DEEPEN:** Replace generic failure with diagnostic classes.
2. **ADD:** Define resource failure.
3. **ADD:** Define prerequisite failure.
4. **ADD:** Define placement failure.
5. **ADD:** Define path failure.
6. **ADD:** Define target failure.
7. **ADD:** Define force insufficiency.
8. **ADD:** Define information failure.
9. **ADD:** Define authority conflict.
10. **ADD:** Define timing failure.
11. **VERIFY:** Trace backup/rebuild and attack reset patterns.
12. **ADD:** Define recovery priority.
13. **ADD:** Define retry limits.
14. **ADD:** Define alternative candidates.
15. **ADD:** Define belief update caused by failure.
16. **ADD:** Define commitment release after failure.
17. **GUARD:** Prevent endless retry loops.
18. **MEASURE:** Track failure signatures by subsystem.
19. **ADD:** Define escalation from local recovery to strategic transition.
20. **GENERALIZE:** Make failure a first-class information source.

# 38. Resignation / terminal state

1. **DEEPEN:** Define terminal game state separately from tactical defeat.
2. **ADD:** Define objective hopelessness versus temporary deficit.
3. **ADD:** Define recoverability horizon.
4. **ADD:** Define ally/team rescue possibility.
5. **ADD:** Define information confidence before terminal decision.
6. **ADD:** Define configurable leniency.
7. **VERIFY:** Trace `resign.per` terminal checks and `fastresign` behavior.
8. **GUARD:** Prevent premature resignation after recoverable setbacks.
9. **ADD:** Define terminal-state observability.
10. **ADD:** Define strategic reserve before resignation.
11. **ADD:** Define asymmetric team-game conditions.
12. **ADD:** Define map-control recovery possibility.
13. **ADD:** Define production recovery possibility.
14. **ADD:** Define technology recovery possibility.
15. **MEASURE:** Evaluate false-resignation rate.
16. **ADD:** Define explicit terminal reason codes.
17. **ADD:** Define operator override interaction.
18. **ADD:** Define post-terminal cleanup.
19. **GENERALIZE:** Model resignation as a high-level strategic policy decision.
20. **DOCUMENT:** Preserve historical resignation heuristics separately from AEGIS policy.

# 39. Difficulty / execution capability

1. **DEEPEN:** Separate strategic competence from mechanical execution.
2. **ADD:** Define reaction latency.
3. **ADD:** Define scouting precision.
4. **ADD:** Define tactical path quality.
5. **ADD:** Define micro execution quality.
6. **ADD:** Define targeting precision.
7. **ADD:** Define multitasking capacity.
8. **ADD:** Define error rate.
9. **VERIFY:** Trace HD execution-capability parameters such as missile dodging and distance maintenance.
10. **ADD:** Define whether difficulty changes information quality, strategy, or only execution.
11. **GUARD:** Prevent difficulty modifiers from corrupting strategic state.
12. **ADD:** Define skill-dependent candidate scoring.
13. **ADD:** Define execution failure signatures.
14. **ADD:** Define compensatory strategy for weak execution.
15. **ADD:** Define robust strategy under execution noise.
16. **MEASURE:** Separate strategic decision quality from mechanical outcome.
17. **ADD:** Define deterministic versus stochastic execution degradation.
18. **ADD:** Define difficulty calibration against human benchmarks.
19. **GENERALIZE:** Make competence a separate layer beneath strategic reasoning.
20. **DOCUMENT:** Do not use difficulty parameters as evidence that the historical strategy itself was weak.

# 40. Taunt / external command interface

1. **DEEPEN:** Treat taunts as an external control plane.
2. **ADD:** Define command grammar.
3. **ADD:** Define command authority.
4. **ADD:** Define command lifetime.
5. **ADD:** Define command scope.
6. **ADD:** Define command precedence over autonomous strategy.
7. **ADD:** Define cancellation semantics.
8. **ADD:** Define invalid-command behavior.
9. **ADD:** Define diagnostic versus strategic commands.
10. **VERIFY:** Inventory documented HD taunt codes and exact effects.
11. **GUARD:** Prevent external commands from bypassing resource/authority safeguards.
12. **ADD:** Define target-selection command lifetime.
13. **ADD:** Define assistance/resource-sharing command state.
14. **ADD:** Define reporting/diagnostic output.
15. **ADD:** Define operator override recovery.
16. **MEASURE:** Verify command effect through observed state rather than command acknowledgement.
17. **ADD:** Define compatibility/version handling.
18. **ADD:** Define security/accidental-input boundary in AEGIS tooling.
19. **GENERALIZE:** Expose controlled intent injection rather than raw state mutation.
20. **DOCUMENT:** Preserve taunt interface as historical evidence of the programmer's intended operator/debug surface.

---

# Cross-section QC findings

The audit exposes recurring gaps that should be corrected across the catalogue rather than only section-by-section.

## A. Universal state schema

Every subsystem should map to:

`OBSERVATION -> CLASSIFICATION/BELIEF -> REQUIREMENT -> CANDIDATES -> FEASIBILITY -> COMMITMENT -> AUTHORITY -> ACTION -> POSTCONDITION -> FAILURE -> RECOVERY -> REASSESSMENT`.

The historical source often implements only fragments because responsibility is distributed across modules. The practical catalogue should explicitly identify which fragment each module supplies.

## B. Writer-reader ownership graph

The catalogue needs a systematic:

`WHO WRITES -> WHO READS -> WHO OVERRIDES -> WHO INVALIDATES -> WHO RESTORES`.

This is critical because distributed state is one of the major strengths and weaknesses of HD/Promisory.

## C. Strategic cost model

Every subsystem should distinguish:

- immediate resource cost;
- reserved resource cost;
- villager-time cost;
- production opportunity cost;
- infrastructure cost;
- timing cost;
- map/position cost;
- military risk;
- information risk;
- optionality lost.

Nominal unit/building/technology cost is insufficient for strategic reasoning.

## D. Belief and uncertainty

Enemy and map reasoning should not be represented as certainty when observations are incomplete or stale. AEGIS should retain confidence, evidence, timestamp, expiry, and alternatives.

## E. Failure taxonomy

Recovery depends on the cause. Minimum classes:

`NO_RESOURCES | MISSING_PREREQUISITE | INVALID_PLACEMENT | PATH_BLOCKED | TARGET_GONE | FORCE_INSUFFICIENT | STALE_INFORMATION | AUTHORITY_CONFLICT | TIMING_EXPIRED | EXECUTION_ERROR`.

## F. Verification discipline

> **A command is an attempt. A postcondition is evidence.**

This must be enforced for build, research, production, movement, transport, attack, retreat, and tactical object control.

## G. Transition model

Nearly every section is stronger when represented as:

`current capability -> desired capability -> required investment -> transition window -> opponent response -> next state`.

## H. Performance economics

The historical programmer repeatedly traded analytical depth for rule-engine performance. Record:

`decision value / evaluation cost`

for expensive searches, path analysis, and aggregate sensors.

## I. Cross-subsystem dependencies

No major subsystem is isolated:

- economy feeds production;
- production creates military capability;
- technology modifies capability;
- scouting changes belief;
- belief changes military demand;
- military changes map control;
- map control changes economy;
- resources fund transitions;
- transitions change opponent behavior.

The catalogue should eventually contain a dependency graph rather than only independent chapters.

## J. Validation artifacts

Important historical claims should eventually link to:

- exact source file;
- line range;
- relevant constants;
- writer/reader graph;
- state diagram;
- replay example where available;
- engine validation where required;
- evidence grade;
- falsification test.

---

# Priority ranking from this QC pass

## P0 — required before implementation guidance is authoritative

1. State ownership and writer-reader graphs.
2. Observation/belief/requirement/commitment/action separation.
3. Postcondition verification.
4. Failure taxonomy and recovery.
5. Resource commitment/opportunity-cost model.
6. Explicit attack/retreat lifecycle.
7. Production capability pipeline.
8. Enemy belief/confidence model.
9. Timer/hysteresis semantics.
10. Current-build versus historical-source evidence boundary.

## P1 — major practical-engineering improvements

11. Candidate-generation/evaluation separation.
12. Search performance budgets.
13. Map/geometry dependency model.
14. Technology investment model.
15. Economic logistics/effective gather rate.
16. Team relational capability model.
17. Naval theater separation.
18. Difficulty/competence separation.
19. External-control authority model.
20. Versioned constant/SN registry.

## P2 — advanced optimization and observability

21. Information-value scoring.
22. Conversion-tax accounting.
23. Optionality valuation.
24. Counter-transition modeling.
25. Strategic decision telemetry.
26. Replay-grounded benchmark suite.
27. Search quality versus computational cost benchmarks.
28. Automated state-writer conflict detection.
29. Automated magic-number/constant validation.
30. Cross-subsystem causal graph generation.

---

# Final QC verdict

The practical coding knowledge base is **conceptually strong but not yet encyclopedic enough to serve as the final engineering manual**. Its central abstractions are sound, but each domain needs stronger treatment of state ownership, uncertainty, timing, opportunity cost, failure, verification, performance, and cross-system causality.

Adding twenty arbitrary syntax tips per section would be the wrong improvement. The valuable expansion is to make every section answer the same deep engineering questions while preserving the historical HD solution as evidence.

The catalogue should therefore evolve from:

`problem -> historical solution -> AEGIS lesson`

toward:

`game problem -> required observations -> strategic interpretation -> state model -> historical HD solution -> engine constraints -> candidate actions -> resource/timing tax -> authority -> execution -> postcondition -> failure signatures -> recovery -> validation -> AEGIS generalization`.

That is the standard required before any subsystem is treated as implementation-ready.
