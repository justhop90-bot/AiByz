# AoE2DE Practical Engineering Masterclass — Pass 8

**Date:** 2026-09-04  
**Layer:** 2 — HD / Promisory strategic-code archaeology  
**Status:** Working practical field manual  
**Primary source:** verified `AI (HD version).per` and verified Promisory modules  
**Runtime authority:** Layer-1 machine evidence for current DE semantics  
**Relationship to the practical knowledge base:** teaching expansion; does not replace the source-derived catalogue  

---

## 0. What this chapter is supposed to teach

The purpose of this document is not to teach somebody how to memorize `.per` syntax. It is to teach them how to **turn an AoE2 strategy problem into a functioning rule-based control system**.

The reader should leave able to look at a strategic problem and decompose it into:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION → STATE → REQUIREMENT → CONSTRAINTS → CANDIDATES → EVALUATION → COMMITMENT → AUTHORIZATION → ACTION → VERIFICATION → FAILURE → RECOVERY → REASSESSMENT`

That sequence is the practical core of the HD/Promisory codebase and the principal engineering lesson AEGIS should inherit.

The historical source demonstrates many pieces of this pattern directly. It does **not** prove that the original programmers possessed one unified modern optimizer or belief engine. Where this document reconstructs such a unification, the claim is explicitly marked as an AEGIS generalization or strategic inference.

### The test for mastery

A reader understands this material when they can answer all of these questions for a new subsystem before writing it:

1. **WHO** owns the state and whose capability is being changed?
2. **WHAT** game fact or capability matters?
3. **WHEN** does the relationship become relevant?
4. **WHERE** does geography/object identity change the answer?
5. **WHY** is the action strategically valuable?
6. **HOW** will the rule system represent and execute it?
7. **WHAT CAN BLOCK IT?**
8. **WHAT PROVES IT WORKED?**
9. **WHAT PROVES THE ASSUMPTION WAS WRONG?**
10. **WHO MAY CHANGE THE STATE AFTERWARD?**

If those questions cannot be answered, the subsystem is not designed yet.

---

# Part I — The fundamental translation

## 1. Start with the game, not the rule

Bad AI engineering begins with:

> “What rule can I write?”

Good AoE2 AI engineering begins with:

> “What relationship in the game am I trying to change?”

Example:

> Enemy cavalry is becoming dangerous.

That sentence is not yet a rule. It is a strategic situation.

Break it down:

- **Observation:** cavalry-line units are observed.
- **Classification:** enemy has a cavalry capability.
- **Belief:** cavalry pressure is sufficiently likely/relevant.
- **Requirement:** acquire a capability that changes the cavalry relationship.
- **Constraints:** resources, age, technology, production buildings, map, distance, timing.
- **Candidates:** counter-unit, mixed composition, siege, fortification, mobility, avoidance, attack elsewhere, technology, or economic transition.
- **Evaluation:** compare capability, timing, cost, risk, and opportunity cost.
- **Commitment:** reserve resources and/or production capacity.
- **Authorization:** permit the selected response.
- **Action:** build/train/research/move/attack.
- **Verification:** inspect the world rather than assuming command success.
- **Reassessment:** determine whether the enemy relationship actually changed.

This is the difference between **coding a response** and **engineering a controller**.

---

## 2. The five meanings hidden inside a fact

A raw engine observation should not automatically become a strategic conclusion.

Consider:

`enemy has 8 knights`

That can mean several different things depending on context.

### Observation

There are eight observed knight-line units.

### Classification

The opponent has meaningful mobile cavalry capability.

### Belief

The opponent may be committing to cavalry pressure.

### Requirement

Our current military/economic state may need an anti-cavalry response.

### Commitment

We are willing to sacrifice another use of resources to obtain that response.

These are different state types. The historical source often encodes them in separate goals, strategic numbers, threat state, timers, and production state. AEGIS should make the distinction explicit rather than collapsing everything into one boolean.

**Engineering rule:** never let a raw observation silently become an irreversible strategic commitment.

---

# Part II — The `.per` toolbox as an engineering vocabulary

## 3. Facts: what the machine says

Facts answer questions about the current game or engine state.

Typical categories include:

- unit counts
- building counts
- age
- resources
- distances
- object properties
- pending actions
- target identity
- map state
- player relationships
- feasibility
- tactical conditions

A fact is evidence. It is not automatically a strategy.

The practical mistake is writing:

`fact → action`

when the problem really requires:

`fact → interpretation → requirement → authorization → action`.

The historical HD/Promisory architecture contains many intermediate state channels precisely because complex strategy cannot be represented safely as direct fact-to-action mappings.

---

## 4. Goals: persistent strategic memory

Goals are useful when a controller needs to remember a decision or state across evaluations.

Examples from the verified HD source include channels for:

- strategy
- unit selection
- attack state
- retreat
- enemy state
- threat state
- farm state
- housing
- technology purpose
- map role
- military distribution
- fortifications
- scouting and tactical state

The important lesson is not the names. It is the **persistence**.

A goal allows the AI to say:

> “This is what I currently believe/intend/control.”

rather than recomputing everything from scratch every time.

### But persistence creates danger

A persistent value can become stale.

Therefore every important strategic state should have some concept of:

- writer
- readers
- lifetime
- reset condition
- invalidation condition
- replacement condition
- confidence where appropriate

AEGIS should not allow five unrelated subsystems to silently compete for ownership of one strategic channel.

---

## 5. Strategic numbers: engine controls, not a free-form database

HD uses strategic numbers extensively for operating parameters and dynamic control.

The practical distinction is:

**Goal:** strategic/internal state.  
**Strategic number:** an engine-facing control interface or persistent configurable value.

A strategic number can alter actual engine behavior. Therefore it should be treated more like an API than like a miscellaneous variable.

For every AEGIS SN, document:

`name | purpose | owner | readers | writer | valid range | side effects | lifecycle | version sensitivity`

A programmer should know whether changing a value merely records state or changes the engine's behavior.

---

## 6. Timers: time is part of state

A strategy without time is usually incomplete.

The same observation can demand different actions:

- immediately,
- after a cooldown,
- only during a transition window,
- until an objective completes,
- until the belief expires,
- or only once.

The historical source repeatedly uses timers around attack, retreat, scouting, micro, and reset behavior.

Therefore a state should not merely say:

`attack = yes`

It may need:

`attack = authorized; expires = T; cooldown = C; invalidated by = X`.

AEGIS should explicitly distinguish:

`IMMEDIATE | DELAYED | COOLDOWN | PERSISTENT | ONE-SHOT | UNTIL-CLEARED | UNKNOWN`.

---

## 7. Temporary goals: scratch registers

High-numbered or explicitly temporary goals are useful as intermediate registers.

They are appropriate for:

- arithmetic
- counts
- candidate values
- search state
- intermediate fact results
- temporary comparisons
- transport of a value between rules

They should not silently become architectural state.

The engineering question is:

> “If this value disappeared after this control operation, would the strategy still be defined?”

If yes, it is probably scratch state.

If no, it needs a named architectural owner.

---

## 8. `can-*` and pending state: the last gate before side effects

A plan can be correct while execution is impossible.

Examples:

- wrong age
- missing prerequisite
- insufficient resources
- missing building
- population limit
- placement impossible
- technology unavailable
- action already pending

Historical code repeatedly uses feasibility and pending checks.

The practical rule is:

`DESIRE ≠ FEASIBILITY ≠ EXECUTION ≠ SUCCESS`

A `can-*` fact answers whether an action is currently feasible. It does not prove that the action has succeeded.

A pending state answers whether an attempted conversion is already underway.

This distinction prevents duplicate actions and false assumptions.

---

# Part III — Building a real subsystem

## 9. The canonical control event

For AEGIS, every major subsystem should be explainable as:

```text
OBSERVE
  ↓
CLASSIFY
  ↓
WRITE STATE
  ↓
DERIVE REQUIREMENT
  ↓
CHECK CONSTRAINTS
  ↓
GENERATE CANDIDATES
  ↓
EVALUATE
  ↓
COMMIT
  ↓
AUTHORIZE
  ↓
EXECUTE
  ↓
VERIFY
  ↓
CLASSIFY RESULT
  ↓
UPDATE STATE
  ↓
REASSESS
```

The historical source does not necessarily implement this as one literal pipeline. Instead, the pieces are distributed across modules and rule networks.

The pipeline is therefore a **composed architectural reconstruction**, not a claim that the original source contains a single centralized controller.

That distinction matters.

---

## 10. Worked example: enemy cavalry

### Situation

The enemy has begun producing cavalry.

### Step 1 — Observe

Collect relevant evidence:

- enemy cavalry count
- enemy age
- supporting units
- cavalry production infrastructure
- observed location
- our current anti-cavalry capability
- our production capacity
- resource state
- technology state

Do not immediately produce a counter.

### Step 2 — Classify

Ask whether the observation represents:

- incidental cavalry,
- defensive cavalry,
- raiding capability,
- mass cavalry transition,
- or uncertain information.

Historical threat logic demonstrates the importance of classification rather than one generic enemy-danger flag.

### Step 3 — Derive requirement

The requirement is not necessarily:

> “Build spearmen.”

It is:

> “Acquire enough capability to prevent cavalry from producing unacceptable strategic damage.”

That capability might be:

- counter units,
- a mixed composition,
- fortification,
- ranged support,
- siege support,
- mobility,
- denial,
- target avoidance,
- or an economic/military transition.

The broader candidate space is an AEGIS generalization; the historical source demonstrates distributed threat-to-response machinery but not a single universal candidate tournament.

### Step 4 — Constraints

A theoretically ideal counter may be impossible because:

- technology is missing,
- production buildings do not exist,
- gold is committed elsewhere,
- the enemy is already attacking,
- the map makes the response too slow,
- or the response arrives after the critical timing window.

### Step 5 — Commit

If the response is strategically justified, reserve resources and/or production capacity.

This is where the historical escrow/resource-control pattern becomes strategically important.

### Step 6 — Authorize

Turn the selected capability into actual production authorization.

This is where the historical unit-goal/production machinery matters.

### Step 7 — Verify

Do not infer success because the production command was issued.

Verify:

- units exist,
- capability is available,
- the local threat changed,
- losses are acceptable,
- and the opponent has not transitioned again.

### Step 8 — Reassess

The enemy may now have:

- more cavalry,
- ranged support,
- siege,
- a new target,
- or a new strategic objective.

Therefore the counter is not a permanent answer. It is a response to a changing relationship.

---

# Part IV — Resources as strategy

## 11. Why resource count is not enough

Suppose the AI has 600 wood.

That number says almost nothing strategically.

The 600 wood may be:

- uncommitted,
- reserved for Castle Age infrastructure,
- required for farms,
- required for houses,
- required for production buildings,
- reserved for siege support,
- or needed to recover from an attack.

The historical escrow/resource-control system is important because it demonstrates the underlying concept:

> **resources can represent claims on future capability.**

Therefore AEGIS should reason about:

`stock | committed | accessible | reserved | expected income | expected demand | opportunity cost`

A resource is strategically available only after accounting for its commitments.

---

## 12. Resource taxation

Every strategic commitment imposes a tax on the rest of the economy.

Example:

> Build three military production buildings.

The cost is not only their wood price.

It may also include:

- delayed farms,
- delayed housing,
- delayed technology,
- builder opportunity cost,
- reduced military production during construction,
- altered gatherer allocation,
- and a smaller emergency reserve.

AEGIS should therefore evaluate:

`direct cost + infrastructure cost + opportunity cost + timing cost + risk cost`.

This formula is an AEGIS design proposal, not a recovered historical equation.

---

## 13. Why gatherer allocation is strategic control

The historical `gatherers.per` system changes resource allocation according to contextual state.

This reveals a fundamental principle:

> worker distribution is downstream of strategic demand.

A permanent ratio is inadequate because demand changes.

If the objective changes from:

`Castle Age`

to:

`mass cavalry`

to:

`farms + siege`

the required resource flow changes.

Therefore the correct architecture is:

`objective → demand forecast → resource allocation → resource arrival → capability`.

---

# Part V — Production and technology

## 14. Production is a capability pipeline

A weak production controller asks:

> “What unit should I queue?”

A stronger one asks:

> “What capability must exist at time T, in what quantity, from which production capacity, using which resources?”

The historical `units.per` architecture initializes many training permissions to `no` and enables production through strategic conditions.

This is significant because production is being treated as **authorization**, not simply as an unconditional queue.

AEGIS should preserve that idea but make ownership explicit.

### Production state should conceptually contain

- desired capability
- desired composition
- production priority
- available production capacity
- resource commitment
- replacement demand
- reinforcement demand
- transition condition
- cancellation condition

---

## 15. Technology is a transition purchase

Technology consumes resources now to alter the future capability space.

Therefore:

`technology choice = immediate cost + timing effect + future capability + opportunity cost + survival effect`.

Historical escrow and research logic demonstrates the first half of this control problem: protect resources, test feasibility, execute research, update age/strategy state, and release/reset the reservation.

AEGIS should add explicit candidate evaluation rather than assuming every available upgrade is strategically correct.

---

## 16. Age-up as a capability transition

An age transition is not merely a research command.

It changes:

- available units,
- buildings,
- technologies,
- economy,
- production possibilities,
- military options,
- and strategic timing.

Therefore the controller should reason about:

`current capability → transition cost → transition timing → resulting capability space`.

The historical source gives strong direct evidence for Castle and Imperial research authorization through escrow and age-state updates. The exact complete doctrine for every age transition must remain evidence-graded rather than assumed.

---

# Part VI — Search and optimization

## 17. How to build an optimizer without a conventional optimizer

The historical code demonstrates that `.per` can construct iterative search machinery.

The pattern found in `general.per` includes concepts such as:

1. reset search state,
2. find candidates,
3. retrieve search state,
4. store candidate information,
5. evaluate candidate properties,
6. calculate distance/score,
7. preserve the best candidate,
8. decrement/advance state,
9. jump through the search loop,
10. terminate and act.

This is a miniature algorithm expressed through rule-engine state.

### The lesson

Do not confuse a rule engine with a language incapable of algorithms.

The algorithm exists in the **state transitions between rules**.

---

## 18. Candidate evaluation

The reusable abstraction is:

`CANDIDATE → FEATURES → CONSTRAINTS → SCORE → UNCERTAINTY → DECISION`

A target, building location, scouting waypoint, military composition, or technology can all become candidates.

This is where AEGIS can unify several historically separate mechanisms.

But the unification is an AEGIS architecture decision, not proof that HD had one general candidate evaluator.

---

## 19. Performance is part of correctness

A search that finds the right answer but consumes too much rule budget is not a successful implementation.

Historical comments explicitly discuss performance costs in scouting and optimization logic.

Therefore candidate search must record:

- search scope,
- candidate count,
- iterations,
- reset behavior,
- early exit,
- rule-budget cost,
- state persistence,
- and worst-case behavior.

The practical engineer asks:

> “What is the computational price of knowing this?”

That is an AoE2-specific engineering constraint, not an optional optimization.

---

# Part VII — Geometry and tactical control

## 20. Distance is strategic information

Distance affects:

- travel time,
- reinforcement timing,
- retreat feasibility,
- exposure,
- target value,
- building placement,
- scouting risk,
- economic throughput.

Therefore distance should not be treated as merely a movement calculation.

It belongs in candidate evaluation whenever geometry changes the strategic relationship.

---

## 21. Scouting is information acquisition

The historical `scoutcontrol.per` system is especially instructive because it does more than issue move commands.

It contains logic for:

- group creation,
- path analysis,
- obstacle/threat analysis,
- candidate pivot points,
- geometric transformations,
- waypoint selection,
- action selection,
- and documented performance compromises.

The strategic interpretation is:

> scouting is a resource-constrained information-acquisition problem.

The value of a scout is not measured only by explored area. It is measured by whether its information changes a decision.

AEGIS should therefore prefer:

`information need → expected decision value → safe acquisition plan → observation`

over:

`explore everything possible`.

---

## 22. Tactical targets are strategic candidates

Historical target evaluation uses factors such as:

- hit points,
- distance,
- range,
- damage,
- rate of fire,
- siege properties,
- time-to-kill,
- attack attempts.

These are tactical features.

AEGIS should add the strategic layer:

- Does killing this target change the objective?
- Does it expose our force?
- Does it open a route?
- Does it protect an economic area?
- Does it provoke an unfavorable counter-transition?

Thus:

`combat value ≠ strategic value`.

---

# Part VIII — Attack, retreat, and failure

## 23. An attack is a state machine

Historical HD state includes distinct attack, attack-status, retreat, restart, target, timer, and reset channels.

That means an attack should not be modeled as:

`attack = true`.

It is better represented as:

```text
PREPARE
  ↓
AUTHORIZE
  ↓
MOVE
  ↓
ENGAGE
  ↓
ASSESS
  ├── CONTINUE
  ├── REGROUP
  ├── RETREAT
  └── CHANGE OBJECTIVE
        ↓
     COOLDOWN / RESET
        ↓
     RESTART / TRANSITION
```

This is one of the strongest practical lessons in the historical architecture.

---

## 24. Retreat is not defeat

A retreat can be a control action that preserves future capability.

But that interpretation is strategic inference, not a literal statement that every historical retreat was intended as military-capital preservation.

AEGIS should evaluate:

- current force value,
- expected losses,
- replacement speed,
- route safety,
- target value,
- reinforcement time,
- initiative cost,
- and recovery window.

A retreat should therefore produce a new strategic state, not simply clear an attack flag.

---

## 25. Fortifications change the problem

A castle or wall is not merely another enemy object.

It changes what actions are feasible.

The historical source explicitly represents enemy fortifications and modifies attack behavior around them. Siege capability and attack state are separate but interacting mechanisms.

The practical rule is:

> First identify the defensive mechanism. Then ask whether the current force can change the relationship.

If not, change:

- capability,
- target,
- route,
- timing,
- or objective.

This is the general pattern of **capability substitution**.

---

## 26. Failure must have a taxonomy

Do not use one state called `failed`.

At minimum distinguish:

### Execution failure

The command could not execute.

### Feasibility failure

The action became impossible.

### Tactical failure

The action executed but produced a bad immediate result.

### Operational failure

The immediate action worked, but the broader operation failed.

### Strategic failure

The action and operation may have succeeded locally while worsening the overall game.

### Information failure

The decision was reasonable under the belief but the belief was wrong or stale.

### Timing failure

The capability arrived too late.

### Resource failure

The commitment consumed resources needed elsewhere.

These categories are an AEGIS strengthening of the historical architecture.

---

# Part IX — Verification

## 27. Command success is not world-state success

This distinction should become instinctive.

Suppose the AI issues:

> build production building.

Possible realities:

1. command rejected,
2. command accepted,
3. villager begins construction,
4. construction is interrupted,
5. building completes,
6. building completes too late,
7. building completes but is strategically useless,
8. building completes and enables the intended capability.

Only the later world-state observations establish what actually happened.

Therefore every consequential action needs an expected postcondition.

---

## 28. Three levels of postcondition

### Command/control postcondition

Did the controller issue the intended command/state change?

### World-state postcondition

Did the game world actually change?

### Strategic postcondition

Did the change improve or protect the strategic objective?

These must never be silently conflated.

---

# Part X — State ownership and architecture

## 29. Every state variable needs an owner

A distributed rule system becomes dangerous when multiple modules can write the same strategic state without an explicit contract.

For every major channel define:

`OWNER | WRITERS | READERS | RESETTER | AUTHORITY EFFECT | LIFETIME | INVALIDATION`

Example:

```text
attack-goal
Owner: offensive controller
Readers: tactical attack, retreat, timer logic
Resetter: attack lifecycle controller
Authority effect: permits offensive execution
Lifetime: until completion / retreat / invalidation
```

The exact ownership assignment above is an AEGIS architecture example; historical source ownership must be established by source tracing.

---

## 30. Authority is different from intention

A subsystem may want to perform an action without being authorized to do it.

This distinction becomes critical when several strategic objectives compete.

Conceptually:

`INTENT → COMMITMENT → AUTHORITY → ACTION`

An emergency controller may revoke authority from a lower-priority plan.

A replacement commitment may supersede an obsolete commitment.

This separation is central to the Porphyra-derived AEGIS architecture and is the principal improvement over loosely distributed historical control.

---

# Part XI — Hysteresis, invalidation, and transitions

## 31. Why simple thresholds oscillate

Suppose a controller attacks whenever:

`force_ratio >= 1.0`.

If the ratio moves:

`0.99 → 1.01 → 0.99 → 1.01`

the controller may repeatedly attack and retreat.

A more stable controller uses different entry and exit thresholds:

`T_enter ≠ T_exit`.

This is **asymmetric hysteresis**.

It is an AEGIS design principle, not a claim that every historical threshold used explicit hysteresis.

---

## 32. Commitments need break conditions

Once the AI commits to Castle Age, siege, a military composition, or a forward operation, it should not blindly continue after the world changes.

Every major commitment should have:

`owner | objective | cost | deadline | break condition | replacement condition | release action`

Example:

```text
Commitment: siege transition
Objective: overcome enemy fortification
Break if: fortification removed / target abandoned / resource emergency
Replace if: enemy exits defensive posture and new military objective dominates
Release: cancel reservation and restore resource availability
```

This is the practical meaning of treating strategy as transition management.

---

## 33. Strategy is management of changing relationships

AoE2 strategy is not a sequence of isolated commands.

It is a changing relationship:

`ECONOMIC STATE`
→ `TECHNOLOGY TRANSITION`
→ `MILITARY CAPABILITY`
→ `PRESSURE`
→ `OPPONENT RESPONSE`
→ `COUNTER-TRANSITION`
→ `NEW EQUILIBRIUM`
→ `NEXT OPPORTUNITY`

Timers, retreat states, escrow, pending state, production authorization, scouting, and search loops all make more sense when viewed as mechanisms for controlling these transitions.

This is one of the strongest strategic abstractions recovered from the combined source archaeology.

---

# Part XII — The engineer's complete workflow

## 34. Before coding

Write a one-page design contract.

```text
GAME PROBLEM:

WHO:

WHAT:

WHEN:

WHERE:

WHY:

OBSERVATIONS:

CLASSIFICATIONS:

BELIEFS:

REQUIREMENTS:

CONSTRAINTS:

CANDIDATES:

EVALUATION:

COMMITMENT:

AUTHORITY:

ACTION:

TACTICAL POSTCONDITION:

OPERATIONAL POSTCONDITION:

STRATEGIC POSTCONDITION:

FAILURE SIGNATURES:

RECOVERY:

INVALIDATION:

REASSESSMENT TRIGGER:

STATE OWNER:

PERFORMANCE BUDGET:

EVIDENCE GRADE:
```

If the design cannot fill this out, more archaeology is required.

---

## 35. While coding

Build the smallest independently understandable relations.

Prefer:

`one observation`
→ `one classification`
→ `one state write`
→ `one authorization condition`
→ `one action`
→ `one verification path`

rather than a giant rule containing the entire strategy.

The historical source demonstrates the power of composition but also contains complexity and distributed ownership that AEGIS should improve.

---

## 36. After coding

Audit the subsystem in this order:

### State audit

Who writes every variable?

### Feasibility audit

Can every side effect become impossible between planning and execution?

### Lifecycle audit

What initializes, updates, resets, expires, and replaces the state?

### Postcondition audit

What proves success?

### Failure audit

What distinguishes execution, tactical, operational, strategic, information, timing, and resource failure?

### Performance audit

What is the worst-case rule/search cost?

### Evidence audit

Which behavior is directly supported by source, which is composed, which is inferred, and which is new AEGIS design?

---

# Part XIII — Ten problems every AEGIS engineer should be able to solve

## Problem 1 — “Enemy has cavalry.”

Do not write a spear rule.

Build:

`observe → classify → determine required capability → constrain → choose response → commit → produce → verify → reassess`.

## Problem 2 — “We need Castle Age.”

Do not write a food/gold ratio.

Build:

`transition objective → resource demand → reservation → feasibility → research → age-state verification → release/reallocate`.

## Problem 3 — “Our attack cannot break the castle.”

Do not repeatedly attack.

Build:

`fortification detection → capability comparison → suppress/defer → siege transition → production → reassessment → restart or change objective`.

## Problem 4 — “The scout needs to find the enemy.”

Do not maximize wandering.

Build:

`information requirement → candidate region → path risk → waypoint → observation → belief update`.

## Problem 5 — “We need a building.”

Do not issue a build command.

Build:

`requirement → placement candidates → constraints → feasibility → build → pending → completion → failure/fallback`.

## Problem 6 — “The resource exists.”

Do not spend it automatically.

Ask:

`is it committed? reserved? needed for a higher-priority transition?`

## Problem 7 — “The attack command succeeded.”

Do not declare success.

Verify the world state and strategic effect.

## Problem 8 — “The threshold keeps oscillating.”

Do not add random delays.

Investigate state ownership, hysteresis, stale beliefs, cooldowns, and commitment lifecycle.

## Problem 9 — “The search finds the correct target but the AI becomes unstable.”

Investigate:

- search reset,
- candidate persistence,
- jump flow,
- early termination,
- state ownership,
- and rule-budget cost.

## Problem 10 — “The code works, but the strategy is bad.”

This is not necessarily a coding failure.

Ask whether the candidate evaluation optimized the wrong objective.

The controller may have achieved the local postcondition while failing the operational or strategic postcondition.

---

# Part XIV — What the historical programmer was really doing

The deepest practical lesson is that the original programmer was repeatedly solving the same meta-problem:

> **How do I represent a changing strategy-game relationship using a rule language with limited state, search, timing, and control primitives?**

That explains why the source contains apparently strange machinery:

- temporary goals,
- state flags,
- search counters,
- geometric calculations,
- timers,
- attack resets,
- escrow,
- feasibility checks,
- pending checks,
- production permissions,
- threat classifications,
- map classifications,
- fallback rules,
- and rule jumps.

These are not random implementation details.

They are the accumulated solutions to recurring strategic-control problems.

The historical code therefore teaches two things simultaneously:

1. **what competent AoE2 AI needs to reason about**, and
2. **how a programmer can construct algorithms inside a constrained rule engine.**

The second lesson is especially important for AEGIS.

---

# Part XV — What AEGIS should inherit, and what it should reject

## Inherit

- explicit strategic state
- contextual resource allocation
- resource reservation
- feasibility gates
- production authorization
- threat classification
- map-aware strategy
- tactical candidate search
- geometry
- attack lifecycle
- retreat/reset/restart
- timers
- fallback paths
- pending-state awareness
- performance consciousness
- modular composition

## Improve

- explicit state ownership
- typed observations vs beliefs
- explicit commitments
- authority separate from intent
- postcondition verification
- failure taxonomy
- invalidation sets
- opportunity-cost accounting
- uncertainty/confidence
- transition ownership
- measurable strategic objectives
- explicit performance budgets
- historical-vs-AEGIS candidate separation

## Reject as architecture

- unexplained shared state
- giant multi-purpose rules
- assuming command issuance equals success
- permanent thresholds without lifecycle control
- treating all enemy danger as one class
- treating resources as uncommitted merely because they are in stock
- treating every historical workaround as an ideal design
- claiming inferred strategy as direct historical fact

---

# Final practical doctrine

A competent AoE2 `.per` engineer does not ask only:

> “What command do I want the AI to execute?”

They ask:

> **“What game relationship am I trying to change, what evidence tells me it needs changing, what capability can change it, what does that capability cost, what prevents me from obtaining it, what am I committing, how do I authorize it, what proves it happened, what proves it worked, what happens if it fails, and when must I change my mind?”**

That is the practical bridge from **game strategy → AI architecture → `.per` implementation**.

And that bridge is the purpose of Layer 2.

---

## Evidence discipline

This document deliberately uses four levels of statement:

- **DIRECT:** executable historical source or explicit source text demonstrates the relationship.
- **COMPOSED:** multiple directly supported relationships form the chain.
- **INFERRED:** strategic meaning reconstructed from repeated source behavior.
- **AEGIS-GENERALIZATION:** a proposed architecture or improvement derived from the historical evidence.

The verified historical source remains the authority for what HD/Promisory actually did. Layer 1 remains the authority for current machine semantics. This document must never be used to turn a plausible architectural interpretation into a false historical claim.
