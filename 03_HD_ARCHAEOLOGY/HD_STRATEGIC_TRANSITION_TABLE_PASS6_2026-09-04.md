# Layer 2 — Evidence-Backed Strategic Transition Table — Pass 6

**Date:** 2026-09-04  
**Status:** Source-derived reconstruction / evidence-grade working model  
**Primary evidence:** verified `AI (HD version).per` + verified Promisory modules  
**Runtime authority:** Layer 1 machine evidence for current AoE2DE execution semantics  
**Purpose:** convert the Pass-5 causal chains into auditable transition records without pretending that inferred strategy is explicit source doctrine.

---

## 0. Why this table exists

Pass 5 established causal chains. Pass-5 QC established that those chains were too permissive unless every edge was classified and every transition contained constraints, commitment-break conditions, postconditions, invalidation, opponent response, and recovery.

This pass therefore uses the canonical transition contract:

`GAME PROBLEM → TRIGGER → EVIDENCE → PRECONDITIONS → BELIEF → OBJECTIVE → CONSTRAINTS → CANDIDATES → EVALUATION → COMMITMENT → ACTIONS → POSTCONDITIONS → OPPONENT RESPONSE → INVALIDATION → EXIT → FAILURE → RECOVERY → REASSESSMENT`

### Evidence grades

- **DIRECT:** executable source behavior or explicit source comment supports the edge.
- **COMPOSED:** multiple DIRECT relationships form the edge; no single rule necessarily states the whole relationship.
- **INFERRED:** strategic interpretation reconstructed from repeated behavior.
- **AEGIS-GENERALIZATION:** design abstraction derived from the historical pattern, not a claim about author terminology or intent.

The distinction is mandatory. A coherent strategic interpretation is not automatically a source fact.

---

# 1. ST-01 — Dark → Feudal transition

## Game problem

Convert early-game economy into Feudal capability at the required time without starving the economic base or exposing the player to an unrecoverable military deficit.

## Trigger / evidence

**Trigger:** age-up objective becomes active through the economic/research control system.  
**Source evidence:** `escrow.per` uses escrow state and `can-research-with-escrow` to authorize Castle/Imperial research; the same architecture establishes the historical pattern for age-transition control. `gatherers.per` changes resource allocation by age/resource state.  
**Evidence grade:** COMPOSED.

## Preconditions

- required age-up research is available;
- required resources can be accumulated within the intended window;
- prerequisite infrastructure is satisfied;
- no higher-priority emergency invalidates the transition;
- resource reservations do not conflict with survival requirements.

## Programmer's belief model

The programmer treats age advancement as a **resource conversion problem**, not simply a button that becomes available when a resource threshold is reached.

The implicit state is approximately:

`current economy + protected resources + prerequisite state + military risk + target timing → age-transition readiness`.

**Belief grade:** INFERRED from composed resource-control, research, gatherer, and timing behavior.

## Strategic objective

Purchase a new capability regime whose future value exceeds the opportunity cost of delaying other investments.

## Constraints

- food is simultaneously required for villagers and age-up;
- wood may be required for houses, camps, production, farms, or infrastructure;
- gold/stone may have competing strategic uses;
- military pressure can change the acceptable transition timing;
- delayed infrastructure can make nominal age completion strategically useless.

## Candidate transitions

1. accelerate age-up;
2. delay age-up for military/economic stabilization;
3. alter gatherer allocation;
4. preserve resources through escrow/resource control;
5. spend on emergency capability first.

## Evaluation

Historical code clearly evaluates feasibility and resource state. It does **not** expose a universal utility function proving how an optimal age-up was chosen.

AEGIS evaluation should therefore consider:

`age-up capability gain + timing value - economic starvation - military exposure - displaced alternatives`.

**AEGIS status:** GENERALIZATION, not historical formula.

## Commitment

Reserve the required resources and worker/economic flow sufficiently to make the transition executable.

## Actions

- change gatherer allocation;
- protect required resources;
- execute research when feasible;
- update strategic age state;
- release/reset reservations after conversion.

## Postconditions

**Tactical:** research request accepted.  
**Operational:** age transition is pending/completed and resource reservation state changes.  
**Strategic:** new production/research/economic capability becomes available.

## Opponent response

Opponent may exploit the temporary military weakness created by the investment or accelerate its own transition.

## Invalidation

- required resources cease to be attainable in the window;
- prerequisite cannot be completed;
- immediate threat changes survival priority;
- expected post-age capability is no longer relevant.

## Failure signature / recovery

**Failure:** transition stalls or completes too late to deliver intended value.  
**Recovery:** revise resource allocation, release obsolete reservation, stabilize military state, reassess transition timing.

## Key lesson

**Age is a capability transition funded by a changing economic portfolio.**

---

# 2. ST-02 — Feudal pressure → Castle transition

## Game problem

Decide when to stop converting resources into immediate Feudal pressure and instead buy the larger capability jump of Castle Age.

## Trigger / evidence

**Trigger:** Feudal military/economic state reaches a point where additional Feudal investment competes with Castle timing.  
**Source evidence:** `gatherers.per` contains contextual percentage changes by age, units, buildings, research, and resource state; `escrow.per` contains explicit research escrow and age-transition control; HD strategy/unit/control state is repeatedly coupled.  
**Evidence grade:** COMPOSED.

## Programmer's belief model

A Feudal force is valuable only while its current capability is relevant. The code's repeated coupling of military state, resources, age, technology, and attack state implies that the programmer did not model “keep producing Feudal units” as an unconditional objective.

**Belief grade:** PROBABLE.

## Strategic objective

Convert current pressure into either:

- continued denial while preserving the Castle transition;
- or a deliberate Castle timing attack/capability jump.

## Constraints

- pressure can force emergency production;
- Castle investment consumes resources that could sustain Feudal armies;
- stopping production too early can surrender map control;
- continuing production too long can delay superior technology and production options.

## Candidate transitions

1. continue Feudal pressure;
2. stabilize/defend and age;
3. maintain a minimum pressure force while aging;
4. exploit a temporary opponent vulnerability before aging;
5. disengage from a low-value fight to protect the transition.

## Evaluation

The historical source provides the ingredients but not a single explicit “Castle timing score.” AEGIS should evaluate:

`marginal Feudal conversion value vs. Castle capability delta + timing window + preserved optionality`.

## Commitment / actions

Resource control and gatherer allocation protect the age-up path; attack state may be allowed to continue, reset, or retreat depending on military conditions.

## Postconditions

The important strategic postcondition is not merely “Castle researched.” It is:

`new capability set available before the opponent's counter-transition closes the window`.

## Invalidation / recovery

If the opponent's pressure makes aging unsafe, the Castle commitment must be revisited rather than blindly preserved.

## Key lesson

**A transition competes against the opportunity cost of maintaining the current regime.**

---

# 3. ST-03 — Castle → Imperial transition

## Game problem

Convert Castle infrastructure, economy, and military state into Imperial capability without entering the transition too early or too late.

## Trigger / evidence

`escrow.per` explicitly contains Imperial research state and updates strategic age state. `gatherers.per` changes allocation as strategic demand evolves. Military/attack systems continue operating around age and capability state.

**Evidence grade:** DIRECT for the existence of the controlled Imperial transition; COMPOSED for the strategic interpretation.

## Preconditions

- Imperial research is feasible;
- resource reservation can be satisfied;
- required prerequisites exist;
- current military state can survive the investment;
- post-Imperial capability is relevant enough to justify the opportunity cost.

## Strategic interpretation

The programmer treats Imperial as a **planned state conversion** with protected resources and post-transition state changes, not merely an automatic age threshold.

## Candidate policies

- fast Imperial;
- maintain Castle military until safer;
- pressure before aging;
- defensive stabilization before aging;
- preserve specific technology/unit commitments through the transition.

## Evaluation

AEGIS must include:

`Imperial timing + capability unlock + technology interaction + production readiness + opponent timing + resource opportunity cost`.

## Failure / recovery

A completed age-up can still be strategically unsuccessful if the economy, infrastructure, production, or military cannot exploit the new capability. This is a critical distinction between **conversion completion** and **conversion success**.

## Key lesson

**Technology completion is an intermediate postcondition; usable strategic capability is the real postcondition.**

---

# 4. ST-04 — Enemy composition change → counter-composition

## Game problem

Translate incomplete observations of an opponent's units, infrastructure, technology, age, and timing into a response that changes the capability relationship rather than merely matching the visible army.

## Trigger / evidence

**Source evidence:** `threats.per` branches by threat class; HD maintains `enemy-goal`, threat state, unit/strategy goals, military population, buildings, age, and timing; the source observes knight-line/cavalry, ranged, gunpowder, infantry, siege, fortification and related states.  
**Evidence grade:** DIRECT for typed detection/response machinery; INFERRED for transition-denial doctrine.

## Preconditions

- enough evidence exists to distinguish a meaningful capability change from noise;
- the response is feasible;
- the response does not create a larger vulnerability;
- production capacity can support the selected capability.

## Belief

`observed composition + infrastructure + timing → hypothesis about enemy capability/transition`.

The correct epistemic representation is a belief, not certainty.

## Objective

Restore or improve the capability relationship while protecting the player's own strategic transition options.

## Constraints

- hidden enemy state;
- production latency;
- resource scarcity;
- counter-vulnerability;
- map geometry;
- existing production commitments;
- timing of the enemy's next reinforcement wave.

## Candidate responses

1. direct counter-unit;
2. siege;
3. mobility/raid;
4. fortification;
5. target/route change;
6. retreat/delay;
7. technology;
8. attack the enemy's enabling infrastructure.

## Evaluation

The historical code supports context-sensitive response. AEGIS extends this into:

`current capability + expected transition + cost + readiness + sustainability + position + opponent response`.

## Commitment break

Break or replace the response commitment if:

- the belief is contradicted;
- the counter is no longer required;
- the opponent transitions into a different threat;
- the counter's opportunity cost exceeds its remaining value.

## Key lesson

**The opponent's army is evidence about a capability transition, not merely a list of targets.**

---

# 5. ST-05 — Attack → retreat → regroup → restart

## Game problem

Preserve military capital when the current engagement becomes unfavorable without abandoning a still-valid strategic objective.

## Trigger / evidence

Source casebook exhibit: approx. HD lines 32578–32595 changes `retreat-now-goal`, `attack-status-goal`, clears `attack-goal`, enables `attack-timer`, and sets reset state. Separate restart logic exists around `restart-attack-goal`.

**Evidence grade:** DIRECT.

## Preconditions

- an active attack exists;
- local engagement conditions are unfavorable or objective conditions changed;
- a recoverable strategic objective remains.

## Belief

Current engagement is not equivalent to overall strategic failure.

## Objective

Trade short-term loss of position/contact for preservation of future military capability and a better future engagement state.

## Constraints

- retreat route safety;
- reinforcement distance;
- enemy mobility;
- remaining force;
- target opportunity;
- attack cooldown;
- map control loss.

## Candidate actions

- continue engagement;
- temporary retreat;
- full retreat;
- regroup;
- change target;
- wait for reinforcement;
- restart attack when conditions improve.

## Evaluation

AEGIS should explicitly compare:

`expected remaining force after continuation` vs `preserved force + future opportunity after retreat`.

## Commitment

A retreat is a **commitment-state change**, not necessarily cancellation of the strategic objective.

## Postconditions

**Tactical:** units disengage / regroup.  
**Operational:** attack state enters cooldown/reset/restart lifecycle.  
**Strategic:** offensive objective remains eligible if its prerequisites survive.

## Opponent response

Opponent may pursue, reinforce, fortify, counterattack, or interpret the retreat as an opening.

## Invalidation

Restart becomes invalid if target disappears, defenses change, force falls below requirement, or another transition becomes higher value.

## Key lesson

**A robust controller needs tactical abort without forced strategic abandonment.**

---

# 6. ST-06 — Fortification → siege transition

## Game problem

Avoid paying military and resource costs to attack a defensive mechanism with an incompatible capability.

## Trigger / evidence

HD explicitly maintains `enemy-fortifications-goal`; comments describe delaying attacks against castles/walls and interaction with siege/attack state. Attack, military-level, population-pressure, timers, retreat, and restart state interact.

**Evidence grade:** DIRECT for fortification-aware attack suppression; COMPOSED for the full “change capability” transition.

## Preconditions

- fortification is relevant to the intended objective;
- direct assault is insufficient or too costly;
- siege or another bypass capability is feasible;
- alternative target/route has been evaluated.

## Belief

`defensive structure → current force cannot efficiently convert contact into objective progress`.

## Candidate transitions

1. siege production;
2. alternate route;
3. alternate target;
4. containment/denial;
5. retreat and rebuild capability;
6. direct assault if the capability differential is actually favorable.

## Evaluation

The central metric is not damage dealt to the building. It is:

`objective progress / total strategic commitment cost`.

## Failure signature

Repeated attacks produce losses without changing the defensive relationship.

That outcome should increase confidence that the current capability is mismatched and trigger transition reconsideration.

## Recovery

Change capability, target, route, or timing; do not merely repeat the same attack faster.

## Key lesson

**When the relationship is structurally unfavorable, change the capability before increasing commitment.**

---

# 7. ST-07 — Map / role classification → economic and military posture

## Game problem

Use spatial role and map structure to change the feasible strategic set before committing to an inappropriate generic plan.

## Trigger / evidence

HD casebook exhibit approx. lines 5252–5262: changing `position-goal` to `pocket` also writes `strategy-goal`, `unit-goal`, and `control-goal`. Water logic similarly changes exploration, docks, transport, and naval control. `customConstants.per` contains standard-map and map-related settings.

**Evidence grade:** DIRECT.

## Preconditions

- position/map classification has enough evidence;
- classification is stable enough to affect strategic planning;
- classification is not merely transient tactical location.

## Belief

Position is a relational strategic state, not an `(x,y)` coordinate.

## Objective

Select an economic/military posture appropriate to map role, reinforcement geometry, exposure, and strategic responsibility.

## Candidate postures

- pocket/boom-support;
- flank pressure;
- defensive walling;
- forward pressure;
- water/naval investment;
- alternate exploration strategy;
- resource-protection posture.

## Evaluation

Map role affects:

`worker safety + resource access + reinforcement time + attack routes + retreat routes + scouting cost + infrastructure exposure`.

## Invalidation

A role classification should be revised if map evidence, ally position, enemy pressure, or strategic geography changes materially.

## Key lesson

**Where the player sits in the game changes what strategy is feasible before any unit is trained.**

---

# 8. ST-08 — Food-source exhaustion → renewable food

## Game problem

Replace finite or timing-sensitive food with renewable throughput without destabilizing military, housing, or technology commitments.

## Trigger / evidence

`boarhunting.per` contains dedicated hunting logic; `farm-goal`, save-wood logic, gatherer allocation, and food/wood state connect the transition from active food sources toward farms/renewable food. The source's food strategy is contextual rather than a single static gather ratio.

**Evidence grade:** COMPOSED.

## Preconditions

- current food source is declining/unavailable;
- renewable food infrastructure is feasible;
- wood opportunity cost is acceptable;
- projected food demand persists long enough to justify the conversion.

## Belief

Food availability is a **trajectory**, not just current stock.

The controller needs to anticipate:

`current source → depletion rate → next source → infrastructure lead time → expected food demand`.

## Candidate transitions

1. continue current source;
2. add farms gradually;
3. accelerate farm infrastructure;
4. shift to another renewable source;
5. temporarily reduce food demand;
6. alter military/technology plan to fit food throughput.

## Evaluation

The strategic cost of farms includes:

`wood cost + infrastructure + worker opportunity + timing + displaced military/eco investment`.

Their benefit is reliable future food throughput.

## Failure signature

Farm investment arrives too early and starves another critical wood conversion, or arrives too late and causes production/research starvation.

## Recovery

Adjust farm commitment and gatherer allocation according to the revised food-demand trajectory.

## Key lesson

**Economic transitions must be scheduled against future throughput, not current inventory.**

---

# 9. Cross-transition findings

The eight transitions expose a deeper common structure.

## 9.1 Transitions are capability conversions

Every major transition can be represented as:

`current capability → commitment → resource/time expenditure → new capability → changed feasible strategy set`.

The age-up, counter-composition, siege, retreat, map posture, and food transitions all fit this model.

## 9.2 The programmer repeatedly reasons about prerequisites

The code rarely treats an action as sufficient by itself. It checks prerequisites, pending state, resources, infrastructure, timing, and strategic state.

This supports a general rule:

> **A desired action is only a candidate transition until its dependency graph is satisfied.**

## 9.3 The strongest historical pattern is not “reaction”; it is controlled transition

The source does not merely:

`see X → do Y`.

It more often approximates:

`see X → classify X → alter state → preserve/protect required resources → wait for feasibility → commit → act → hold/retreat/reset/restart → reassess`.

That is materially closer to a stateful controller than to a build-order script.

## 9.4 Constraints propagate backward

A strategic objective creates requirements; requirements create resource/production constraints; constraints restrict candidates.

Therefore the AEGIS direction should be:

`OBJECTIVE → REQUIRED CAPABILITY → PREREQUISITES → RESOURCE/PRODUCTION CONSTRAINTS → FEASIBLE CANDIDATES`.

Not:

`RESOURCE SURPLUS → RANDOMLY BUY SOMETHING USEFUL`.

## 9.5 Postconditions exist at three levels

A command can succeed tactically while failing operationally or strategically.

Example:

`build forward castle`

- Tactical: building placed.
- Operational: defensive/production geometry established.
- Strategic: intended territory denial or timing conversion actually improved.

AEGIS must never collapse these into one boolean success flag.

## 9.6 Every commitment needs an invalidation set

The historical source approximates this with timers, reset state, changed goals, threat changes, feasibility checks, and alternative branches.

AEGIS should make it explicit:

`commitment + invalidation conditions + exit path`.

This prevents sunk-cost persistence.

## 9.7 Opponent response is part of the transition

A transition changes the game state and therefore changes the opponent's feasible actions. The transition is not complete when our action finishes; it is complete when the resulting relationship is evaluated.

This is the foundation of the AEGIS **conversion-tax** concept, but conversion tax remains an AEGIS abstraction rather than historical terminology.

## 9.8 Failure should update beliefs

If a planned transition fails, the correct question is not merely “what command failed?”

It is:

`Which assumption about resources, capability, timing, position, opponent, or feasibility was falsified?`

That makes failure diagnostic rather than merely negative.

---

# 10. Historical source → AEGIS translation matrix

| Historical pattern | Source status | AEGIS abstraction | Do not overclaim |
|---|---|---|---|
| Escrow / resource-control | DIRECT | Explicit reservation ledger | Original authors did not use AEGIS terminology |
| Enemy goals / threat classes | DIRECT | Belief + typed threat model | Confidence/probability is an AEGIS extension |
| Unit/strategy coupling | DIRECT / COMPOSED | Capability portfolio | No historical universal utility function |
| Attack / retreat / restart | DIRECT | Commitment lifecycle | “Preserve optionality” is an interpretation |
| Fortification-aware attack | DIRECT | Capability-transition decision | Conversion tax is generalized |
| Position changes strategy | DIRECT | Relational map state | Full map-value function is AEGIS design |
| Gatherer regime changes | DIRECT | Demand-driven economic controller | Shadow prices are AEGIS design |
| Timers / reset | DIRECT | Hysteresis / commitment dwell time | Control-theory terminology is retrospective |
| Pending / can-* checks | DIRECT | Side-effect feasibility gate | Current engine semantics remain Layer-1 authority |
| Search loops / candidate evaluation | DIRECT | Candidate generator/evaluator | Historical implementation is not an optimizer in the modern sense |

---

# 11. The deeper game-theoretic reconstruction

The eight transitions reveal that the historical programmer appears to understand AoE2 as a sequence of **changing capability relationships**.

A useful reconstruction is:

```text
ECONOMIC STATE
      ↓
TECHNOLOGY / INFRASTRUCTURE
      ↓
AVAILABLE CAPABILITY
      ↓
POSITION + INFORMATION
      ↓
PRESSURE / OBJECTIVE
      ↓
OPPONENT RESPONSE
      ↓
NEW RESOURCE / PRODUCTION DEMAND
      ↓
NEW CAPABILITY
      ↓
NEW TRANSITION
```

The strategic object is therefore not a static army, economy, or build order. It is the **trajectory of feasible transitions** through game state.

That is the strongest conceptual bridge from the HD source to AEGIS.

## What the programmer seems to understand about winning

The evidence supports the following reconstruction, with the grades shown:

1. **Capability must be funded before it can be used.** — PROBABLE  
2. **Timing changes the value of capability.** — PROBABLE  
3. **Opponent commitments reveal future constraints.** — PROBABLE  
4. **Resources have opportunity cost before expenditure.** — PROBABLE  
5. **Position changes the feasible strategy set.** — PROBABLE / DIRECT for specific position effects  
6. **A tactical setback does not necessarily invalidate the strategic objective.** — PROBABLE  
7. **A defensive mechanism can require a capability transition rather than more commitment to the same attack.** — PROBABLE  
8. **Economic throughput must be managed as a trajectory.** — PROBABLE  
9. **Information is valuable because it changes future decisions.** — PLAUSIBLE / PROBABLE  
10. **Stable strategy requires memory, timers, and controlled re-entry.** — PROBABLE; implementation-level timer use is DIRECT.

These are not claims that the original programmers articulated these principles in these exact terms.

---

# 12. AEGIS implementation consequence

The strategic engine should eventually represent a transition as:

```text
TRANSITION
├── trigger
├── evidence
├── belief
├── objective
├── required_capability
├── constraints
├── candidate_set
├── evaluation
├── commitment
├── entry_state
├── actions
├── tactical_postcondition
├── operational_postcondition
├── strategic_postcondition
├── opponent_response_model
├── invalidation_set
├── exit_condition
├── failure_signature
├── recovery_policy
├── reassessment_trigger
└── evidence_grade
```

The runtime decision pipeline should then be:

`OBSERVE → CLASSIFY → BELIEVE → DETECT TRANSITION → DEFINE OBJECTIVE → DERIVE REQUIREMENTS → PROPAGATE CONSTRAINTS → GENERATE CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → UPDATE → RELEASE/MODIFY/REINFORCE → REASSESS`.

This is an AEGIS design target, not a claim that the historical source implemented this object model explicitly.

---

# 13. Research gaps exposed by Pass 6

The table is strong enough to define the next evidence requirements.

### G1 — Exact age-transition writer graph

Need a complete writer/reader graph for age-related goals, escrow flags, gatherer regimes, and production consequences.

### G2 — Exact production-capacity transition graph

Need to trace how enemy classification becomes unit-goal changes and how unit-goal changes become actual production authorization.

### G3 — Attack failure taxonomy

Need to distinguish source branches for force disadvantage, target invalidation, fortification, retreat, timeout, and infrastructure interruption.

### G4 — Food trajectory

Need a fuller writer/reader chain linking hunting, farm-goal, save-wood, gatherer allocation, and production demand.

### G5 — Map classification consequences

Need to enumerate every strategic write caused by position/map classification and separate true strategic role from local tactical position.

### G6 — Opponent-transition prediction

Need to determine exactly which enemy observations are used as evidence of future capability rather than current composition.

### G7 — Decision alternatives

Historical source often encodes branches but does not expose an explicit set of simultaneously scored alternatives. AEGIS must not retroactively claim a candidate tournament where the source only used priority rules.

---

# 14. Pass-6 determination

**Status: PROMOTED AS EVIDENCE-BACKED STRATEGIC TRANSITION MODEL — NOT FINAL POLICY.**

The eight transitions now have enough structure to support disciplined implementation planning, but several quantitative concepts remain hypotheses requiring replay calibration and controlled intervention.

The strongest surviving thesis is:

> **The historical AI's strategic sophistication comes less from any single rule than from repeatedly managing transitions between economic, technological, military, positional, informational, and temporal states.**

The most important AEGIS inheritance is therefore not a list of old rules. It is the idea that **strategy is the controlled management of changing capability relationships under uncertainty and opportunity cost**.

That is the principle subsequent AEGIS policy should attempt to prove, falsify, refine, and eventually operationalize.
