# HD/2013 Implicit Strategic Principles — Pass 2

**Date:** 2026-09-02  
**Status:** RECONSTRUCTION / HYPOTHESIS — no runtime implementation authority  
**Source identity:** `AI (HD version).per`  
**Source SHA-256:** `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`

## 1. Purpose

Pass 1 established what the historical program explicitly represented and did.
Pass 2 asks the harder question:

> **What competitive principles are most plausibly encoded by the repeated control patterns?**

This is not a claim that the original authors consciously wrote these principles
in this terminology. The reconstruction generalizes repeated executable behavior
into strategy concepts while preserving an evidence trail and a falsification path.

## 2. Epistemic rule

A principle is promoted only when multiple observations converge on the same
strategic interpretation. Names alone are not evidence. A single threshold is not
a law. Repetition, coupling, temporal behavior, action consequence, and negative
evidence all matter.

Status vocabulary:

- **CONFIRMED:** the source explicitly states the underlying semantic contract.
- **PROBABLE:** repeated behavior strongly supports the generalized principle.
- **PLAUSIBLE:** interpretation is coherent but needs independent validation.
- **UNCERTAIN:** insufficient evidence.
- **ENGINE-SPECIFIC:** principle may be an implementation consequence rather than a general RTS law.

## 3. Principle P2-01 — Strategy is a coupled capability portfolio

**Status:** PROBABLE  
**Evidence:** 328 `strategy-goal` writes; 432 `unit-goal` writes; 306 rules co-write both.

The historical controller does not treat strategy as a single categorical label.
Strategy selection is repeatedly coupled to the military capability intended to
execute it, and frequently to control/resource state as well.

### Reconstructed principle

A strategic plan is incomplete until the program identifies the capability portfolio
that can actually realize it.

### Generalization

`strategy -> capability -> production -> resource demand`

Therefore a strategy engine should not select “rush,” “boom,” or “defend” without
also estimating what production, technology, and resource profile makes that mode
operational.

### Falsifier

If strategy and unit selection are independent throughout all high-impact branches,
the portfolio interpretation would be weakened.

## 4. Principle P2-02 — Strategic information should be compressed into reusable state

**Status:** PROBABLE / ENGINE-SPECIFIC implementation  
**Evidence:** `enemy-goal`, `position-goal`, and other classification goals are
written by observation rules and consumed downstream.

### Reconstructed principle

Do expensive interpretation once, persist the conclusion, and allow multiple
controllers to consume it.

### Why this matters

The rule substrate makes repeated high-dimensional predicates costly and fragile.
Classification state acts as a cache of strategic meaning.

### Generalization

`raw observation -> belief/classification -> reusable strategic state`

AEGIS should retain this principle while replacing the historical register-based
implementation with typed belief objects and explicit confidence.

## 5. Principle P2-03 — Resources have opportunity cost before they are spent

**Status:** PROBABLE  
**Evidence:** 91 active writes to `sn-resource-control`; repeated escrow/release
patterns; reservation states around technology, siege, units, and infrastructure.

### Reconstructed principle

The value of a resource is conditional on what future action it must remain capable
of funding.

A resource is therefore not simply “available” or “unavailable.” It can be:

- free;
- committed;
- protected;
- escrowed;
- required for a near-term capability;
- released when the requirement disappears.

### Strategic generalization

The correct question is not:

`Can I afford X?`

but:

`What capability would I lose by spending these resources on X now?`

This is the historical seed of **resource taxation / opportunity-cost reasoning**.

## 6. Principle P2-04 — Capability timing matters more than nominal unit count

**Status:** PROBABLE  
**Evidence:** military level, population pressure, siege availability, age, target
fortifications, and timers repeatedly appear together in attack/retreat decisions.

### Reconstructed principle

A military force has strategic value only relative to what it can accomplish during
the current timing window.

Ten units before the enemy's counter-capability can be strategically stronger than
fifteen units after the window closes.

### Generalization

`capability value = combat power × timing relevance × objective relevance`

## 7. Principle P2-05 — Preserve optionality when commitment is premature

**Status:** PLAUSIBLE -> PROBABLE pending cross-validation  
**Evidence:** attack interruption, reset/restart state, resource reservations, and
conditional production choices.

The source frequently avoids irreversible commitment until feasibility, target,
position, or resource conditions support it.

### Reconstructed principle

When uncertainty is high, preserve the ability to change composition, target, or
production direction.

### Strategic interpretation

Optionality has economic value. Spending resources too early can create a
conversion tax against oneself by narrowing future responses.

## 8. Principle P2-06 — Tactical interruption need not equal strategic abandonment

**Status:** PROBABLE  
**Evidence:** retreat modifies attack lifecycle state while separate restart/reset
state exists; timers create recovery windows.

### Reconstructed principle

A tactical retreat can be an internal transition inside the same strategic plan.

This separates:

`stop this action`

from:

`abandon the strategic objective`.

That distinction is essential to robust RTS reasoning.

## 9. Principle P2-07 — Hysteresis is required for stable strategic control

**Status:** CONFIRMED at implementation level; PROBABLE as strategic rationale  
**Evidence:** 233 active timer-enable actions and multiple attack/retreat/scouting/
reset timers.

### Reconstructed principle

A controller must not immediately reverse a decision merely because the triggering
measurement fluctuates around a threshold.

Timers create a minimum dwell time or cooldown. This reduces oscillation, action
spam, and destructive indecision.

### Generalization

Strategic state should have **entry conditions, persistence conditions, exit
conditions, and cooldown/recovery conditions**.

## 10. Principle P2-08 — Threats are typed, not merely scalar

**Status:** PROBABLE  
**Evidence:** threat-source, threat-target, threat classes, defensive structures,
unit families, and distinct retreat responses.

### Reconstructed principle

“Enemy pressure” is not one variable. The response depends on the mechanism of
pressure: tower, castle fire, cavalry, ranged mass, siege, raid, forward position,
or other threat classes.

### Generalization

`threat = source × mechanism × target × timing × severity`

This implies that a general counter system should be a transition model rather than
a single counter-unit lookup.

## 11. Principle P2-09 — Map position is an economic and military variable

**Status:** PROBABLE  
**Evidence:** position classification changes strategy/unit state; water-map logic
changes docks, exploration, transport, and production.

### Reconstructed principle

Position changes the feasible strategy set.

A pocket, flank, island, mixed-water map, or defended location changes the cost,
capacity, and timing of strategic options.

### Generalization

Map control is not merely combat territory. It changes:

- worker safety;
- travel time;
- reinforcement time;
- resource access;
- production exposure;
- scouting quality;
- attack routes;
- retreat routes.

Therefore map position belongs inside the strategic value function.

## 12. Principle P2-10 — Production is a capability pipeline, not a queue

**Status:** PROBABLE  
**Evidence:** building thresholds, pending-object tests, feasibility predicates,
age conditions, unit goals, and resource control interact.

### Reconstructed principle

The real strategic production problem is:

`objective -> required capability -> infrastructure -> technology -> resource demand -> queue -> reinforcement -> replacement`

A production queue without this upstream capability model is strategically blind.

## 13. Principle P2-11 — Failure of a planned action is information

**Status:** PROBABLE  
**Evidence:** `can-build`/pending checks, alternative construction branches, timers,
reset state, and state changes following blocked actions.

### Reconstructed principle

When an intended action cannot execute, the controller should not treat the event
as a null result. It is evidence about the current state and may justify a branch.

Example pattern:

`cannot build preferred infrastructure -> alternative infrastructure -> altered exploration/production posture`

This is the seed of explicit **failure signatures and recovery policies**.

## 14. Principle P2-12 — Information acquisition has capacity and timing costs

**Status:** PLAUSIBLE / PROBABLE  
**Evidence:** exploration-group strategic numbers, scouting timers, map-specific
exploration behavior, and production decisions coupled to exploration capacity.

### Reconstructed principle

Information is an economic resource. More scouting capacity costs production,
attention, and sometimes military opportunity; insufficient information increases
strategic uncertainty.

The correct decision therefore balances:

`information gain vs. resource/attention cost vs. decision value`.

This is the historical precursor of a Value-of-Information model.

## 15. Principle P2-13 — Strategic decisions should be stateful rather than purely reactive

**Status:** PROBABLE  
**Evidence:** persistent goals, timers, reset latches, reservations, and reusable
classifications.

### Reconstructed principle

The historical AI stores enough memory to distinguish the present observation from
what the controller previously decided.

A purely reactive controller would repeatedly rediscover the same facts and could
oscillate. Stateful control permits commitment, cooldown, recovery, and staged
transitions.

## 16. Principle P2-14 — Counterplay should target the opponent's transition, not just current composition

**Status:** PLAUSIBLE  
**Evidence:** enemy strategy classifications, technology conditions, building
counts, military infrastructure observations, and strategic response branches.

The source repeatedly observes more than the enemy's current army. It observes
buildings, age, technology, military population, and timing because those variables
constrain what the opponent can do next.

### Reconstructed principle

The most valuable counter is often the one that taxes or denies the opponent's next
transition rather than the one that trades most efficiently against the current
army.

This is a direct bridge to the AEGIS thesis of **conversion tax**.

## 17. Principle P2-15 — Strategic tempo is a controllable resource

**Status:** PLAUSIBLE  
**Evidence:** timers, attack windows, resource reservations, production timing,
position-dependent transitions, and reset/restart logic.

### Reconstructed principle

The controller is not merely optimizing resources and units; it is controlling
when the opponent is allowed to act and when our own capability becomes available.

Tempo can be created by:

- forcing inefficient enemy responses;
- threatening multiple transitions;
- denying infrastructure;
- preserving a reserve;
- moving the opponent into defensive production;
- exploiting a temporary capability window.

## 18. Principle P2-16 — Resource allocation should follow strategic demand, not static ratios

**Status:** PROBABLE  
**Evidence:** 223–224 active writes across gatherer percentage channels and repeated
contextual changes tied to strategy and technology/unit conditions.

### Reconstructed principle

Worker allocation is a control output derived from expected demand.

Static 40/40/20-style allocations are therefore only valid when the future demand
profile remains stable. When strategy changes, the allocation should change before
or during the transition.

## 19. Principle P2-17 — The controller separates detection from execution because the world is asynchronous

**Status:** CONFIRMED / ENGINE-SPECIFIC  
**Evidence:** pending-object checks, research-status checks, feasibility predicates,
and delayed timers.

### Reconstructed principle

The world after a command is not assumed to equal the world before a command plus
the requested change. Construction, research, production, movement, and combat
have latency and failure states.

### Generalization

Every command should have:

`intent -> request -> accepted/rejected -> pending -> completed/failed -> observed result`

## 20. Cross-principle synthesis

The principles above form a coherent strategic model:

`OBSERVE`
→ `CLASSIFY`
→ `ESTIMATE CAPABILITY`
→ `IDENTIFY OBJECTIVE`
→ `RESERVE OPTIONS/RESOURCES`
→ `CHOOSE TIMING WINDOW`
→ `COMMIT CAPABILITY`
→ `ACT`
→ `OBSERVE CONSEQUENCE`
→ `UPDATE BELIEF`
→ `REASSESS`

The historical implementation distributes this cycle across many rules. The
strategic meaning is nevertheless coherent enough to recover.

## 21. The first appearance of the AEGIS conversion-tax concept

The source does not use the term “conversion tax” as a general doctrine. That term
is an AEGIS abstraction.

However, the historical patterns strongly support its ingredients:

1. resources can be reserved for future capability;
2. enemy commitments are classified before response;
3. map/position changes the feasible response set;
4. tactical pressure can force defensive production;
5. timing changes capability value;
6. the opponent's transition can be observed before completion;
7. a response can deliberately alter the opponent's economic/production state.

The AEGIS generalization is therefore:

> **A strong strategic action is one whose consequence forces the opponent to spend
> more resources, time, production capacity, map control, or strategic optionality
> than the action itself cost us.**

This remains a hypothesis until validated against independent AoE2 evidence.

## 22. What was probably human reasoning versus machine workaround

### Likely human strategic reasoning

- position affects strategy;
- current enemy state constrains future transitions;
- resources have opportunity cost;
- military strength is contextual;
- timing matters;
- retreat can preserve future capability;
- different threats demand different responses;
- information changes the value of decisions.

### Likely machine-substrate compensation

- overloaded goal registers;
- numeric strategic-number conventions;
- distributed writers;
- self-disabling rules;
- timer-based hysteresis;
- scratch goals;
- duplicated or obsolete branches;
- engine-specific feasibility predicates.

The central research task is to separate these two categories without deleting the
historical evidence of how the designers bridged them.

## 23. What Pass 2 still does not establish

Pass 2 does not establish that the original authors consciously intended every
modern abstraction above. It also does not establish optimality.

Independent validation must come from:

- repeated source patterns;
- the Promisory substrate where relevant;
- V3 behavioral intent;
- replay evidence;
- competitive AoE2 strategy knowledge;
- controlled experiments;
- machine constraints established in Layer 1.

## 24. Practical AEGIS consequence

The eventual strategic engine should not copy the historical rule structure.
Instead it should implement a typed state model with explicit:

`belief + confidence + objective + capability + reservation + timing + action + expected consequence + failure signature + recovery`

The historical AI provides the archaeological evidence that these dimensions were
already being approximated inside the old substrate.

## 25. Next pass

Pass 3 will reconstruct **meta-knowledge**: why a skilled programmer would choose
this distributed control architecture, why timers/self-disabling/reset mechanisms
were necessary, how the authors managed complexity, what they appear to have
optimized for, and which engineering tradeoffs were imposed by the rule machine.

Only after Pass 3 should the recovered principles be generalized into the formal
Layer-2 AoE2 strategic ontology and tested against independent evidence.
