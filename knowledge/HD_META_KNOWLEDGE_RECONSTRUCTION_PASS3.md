# HD/2013 Meta-Knowledge Reconstruction — Layer 2 Pass 3

## Scope and evidence boundary

Pass 1 asks **what the historical AI explicitly encoded**. Pass 2 asks **what strategic principles recur in that behavior**. Pass 3 asks **what engineering and design knowledge can be reconstructed from the shape of the system itself**.

This is designer-model reconstruction, not mind-reading. The source contains no programmer diary, so conclusions below are inferences from repeated structures, state interactions, timing mechanisms, and control patterns.

### Evidence boundary

The primary strategic evidence is the recovered HD/2013 source and the derived archaeology records:

- `03_HD_ARCHAEOLOGY/HD_DESIGNER_LOGIC_RECONSTRUCTION.md`
- `03_HD_ARCHAEOLOGY/HD_EXPLICIT_STATE_LEDGER_PASS1.json`
- `03_HD_ARCHAEOLOGY/HD_IMPLICIT_STRATEGIC_PRINCIPLES_PASS2.md`
- `03_HD_ARCHAEOLOGY/HD_CONTROL_EVENT_SCHEMA.json`

**ADPromisory, ByzantineWarCouncil, and AiBuilder are excluded from this knowledge reconstruction.** They are failed/derived experimental material and are not evidence for AEGIS strategy, architecture, or designer intent.

## M1 — The programmers were solving a feedback-control problem

The strongest architectural interpretation is a feedback controller rather than a static build-order engine.

The recurring pattern is:

`observe -> classify -> write state -> act -> wait/reassess -> observe again`

The HD designer reconstruction identifies the same structure: strategy, enemy state, resource control, position, attack/retreat state, and timers form a continuously changing control surface. See `03_HD_ARCHAEOLOGY/HD_DESIGNER_LOGIC_RECONSTRUCTION.md`.

### Meta-knowledge

The programmer's problem was not simply selecting an action. It was maintaining useful behavior while the world changed underneath the controller.

### AEGIS lesson

Make feedback control an explicit architectural primitive. A strategic decision is provisional until its expected world-state change is observed.

## M2 — State compression was a deliberate complexity-management technique

The source repeatedly converts expensive observations into compact reusable variables: strategy, unit, control, enemy, position, attack state, military level, resource-control state, and related classifications.

These variables are more than storage. They form a **symbolic vocabulary** for downstream reasoning.

### Meta-knowledge

A constrained rule engine cannot repeatedly carry every raw observation through every decision. The programmer therefore manufactures intermediate concepts that later rules can consume cheaply.

This is analogous to feature extraction in a statistical system, except the features are human-designed symbolic state variables.

### AEGIS lesson

Separate:

`raw observation -> derived fact -> belief/classification -> strategic state`.

Every derived state variable should have a semantic definition, provenance, update policy, confidence, and failure mode.

## M3 — Timers are behavioral memory

Timers recur around strategic transitions, reassessment, attack/retreat behavior, and recurring control cycles.

### Likely functions

A timer can provide:

1. persistence of a recent decision;
2. hysteresis against rapid reversal;
3. debounce against repeated rule firing;
4. rate limiting of expensive evaluation;
5. delayed re-entry into a strategic state;
6. a temporal window in which an expected consequence should appear.

The exact function must be established per control event. The general meta-principle is strong because temporal mechanisms recur across otherwise different subsystems.

### AEGIS lesson

Temporal state is part of strategy. It should not be hidden as arbitrary cooldown constants scattered through implementation.

## M4 — Self-disable is a one-shot transaction primitive

Many initialization and transition rules write state and then disable themselves.

A representative conceptual form is:

```lisp
(condition)
=>
(set-goal state value)
(disable-self)
```

The exhibit is intentionally tiny: its value is the control pattern, not the historical source itself.

### Meta-knowledge

The programmer needed to distinguish a condition that remains true from an event that should happen once. In a repeatedly evaluated rule substrate, self-disable is a practical transaction boundary.

### AEGIS lesson

Represent event lifecycle explicitly: pending -> authorized -> executed -> acknowledged. Do not depend on a permanent predicate to imply one-shot semantics.

## M5 — Distributed state is an engineering strategy with a verification cost

The HD implementation distributes strategic state across many rule families. That creates composability: many rules can consume the same compact state. It also creates ambiguous authority when several families can write related variables.

### Meta-knowledge

The distribution appears to be a response to the substrate. A centralized strategic object with typed fields, methods, and explicit ownership is difficult to express in a weak declarative rule environment.

The programmer therefore appears to have optimized for **expressible local control**, accepting a larger verification burden.

### AEGIS lesson

Preserve semantic decomposition. Replace ambiguous authority with:

`owner -> readers -> writers -> legal transitions -> priority -> verification`.

## M6 — Goals and strategic numbers represent different layers of control

The source uses goals and strategic numbers extensively rather than collapsing everything into one state mechanism.

### Meta-knowledge

The distinction is useful because not every value has the same semantic role. Some values behave like internal state; others configure or communicate with engine-level policy machinery.

The exact semantics must be proven against machine evidence before assigning universal rules, but the architectural distinction itself is valuable.

### AEGIS lesson

Maintain separate concepts for:

- observation;
- engine fact;
- strategic parameter;
- belief/state;
- command intent;
- authorization;
- execution acknowledgement.

## M7 — Resource control is reservation and opportunity-cost logic

The extensive resource-control behavior is best understood as protecting resources for strategically important future conversions.

A resource is therefore not merely:

`current amount`.

It is closer to:

`current amount + committed purpose + future opportunity cost`.

### Meta-knowledge

The programmer understood an important RTS truth: spending a resource can be strategically wrong even when the immediate purchase is affordable.

### AEGIS lesson

Resource allocation must begin with desired future capability and competing commitments, then determine what spending is legal now.

## M8 — Enemy classification is predictive compression

The source observes enemy units, buildings, age, military conditions, and other signals and converts them into enemy-strategy classifications consumed by downstream strategy rules.

### Meta-knowledge

The purpose of scouting is not merely to know what exists. It is to reduce uncertainty about what the opponent can and probably will do next.

### AEGIS lesson

Opponent modeling should contain:

`observation + hypothesis + confidence + alternatives + expected transition + required resources + vulnerability`.

A single deterministic label is often insufficient.

## M9 — Strategy is a coupled portfolio

The source's strategy changes can interact with unit choice, worker allocation, military spreading, resource control, production, and timing.

### Meta-knowledge

The programmer appears to understand that a strategic label such as “rush” is shorthand for a collection of mutually supporting capability decisions.

### AEGIS lesson

Represent strategic intent as a capability portfolio and resource-demand vector rather than merely as a named build.

## M10 — Position is upstream causal state

Position/map classifications are consumed by strategic and military rules.

### Meta-knowledge

Geography changes the feasible strategy set. It changes defensive cost, attack routes, economic access, exposure, reinforcement distance, and the value of particular compositions.

### AEGIS lesson

Map geometry belongs in strategic evaluation, not solely in movement/micro code.

## M11 — Attack is a state machine, not a boolean

The historical attack controller incorporates military mass, age, siege, target conditions, technology, resource control, attack status, retreat state, resets, and timing.

### Meta-knowledge

The programmer was modeling an attack as a **conditional state transition** with entry conditions, persistence, interruption, and re-entry—not simply deciding whether an army exists.

### AEGIS lesson

An attack intent should specify:

`objective -> entry conditions -> force requirement -> expected payoff -> risk -> persistence -> exit -> failure signature -> recovery`.

## M12 — Retreat preserves option value

Retreat state is separated from broader strategy and can interact with timers and later offensive behavior.

### Meta-knowledge

This strongly suggests a distinction between local tactical unfavorable conditions and global strategic failure. Preserving surviving units preserves future capability, initiative, and information.

### AEGIS lesson

Treat retreat as a strategic action when it preserves future option value. Do not equate loss of contact with loss of plan.

## M13 — Reset, restart, and abandonment are different scopes

The historical architecture contains distinct mechanisms for clearing tactical state and later restarting behavior.

### Meta-knowledge

A controller needs multiple failure scopes:

- tactical interruption;
- local reset;
- strategic replan;
- full recovery.

Collapsing them into one “failed” state destroys useful information.

### AEGIS lesson

Failure state should preserve as much valid prior state as possible while invalidating only what the failure actually disproves.

## M14 — Reassessment exists because plans are hypotheses

The source repeatedly revisits strategic conditions instead of assuming that an earlier decision remains correct indefinitely.

### Meta-knowledge

A plan is an expectation about a future world state. The world can invalidate that expectation. Reassessment is therefore epistemic as well as tactical.

### AEGIS lesson

Every major commitment should have an expected result and a recognizable failure signature.

## M15 — The programmers optimized for operational survivability inside the substrate

The source contains duplication, historical layering, defensive checks, special cases, experiments, and uneven abstractions.

### Meta-knowledge

The correct comparison is not “is this elegant modern software?” but “does this structure solve the problem imposed by this particular machine?”

The source appears to optimize for reliable useful behavior under severe representational constraints.

### AEGIS lesson

Do not reproduce implementation ugliness when the new architecture removes the original constraint. Preserve the successful strategic idea, not its accidental encoding.

## M16 — What the source could not express cleanly is evidence

Rich probability distributions, explicit causal graphs, centralized utility comparison, multi-step lookahead, and typed command authorization are difficult to represent directly in the historical substrate.

The programmers often approximate richer concepts using goals, strategic numbers, timers, and rule chains.

### Meta-knowledge

The approximation reveals two things simultaneously:

1. the concept the programmer was trying to represent;
2. the expressive boundary of the machine.

### AEGIS lesson

Recover the concept first. Choose the representation second.

## M17 — Complexity is not intelligence

Historical AI source mixes genuine strategic mechanisms with obsolete code, debug controls, experiments, compatibility behavior, and accumulated exceptions.

### Archaeological rule

Never infer quality from size or complexity.

Use:

`preserve -> classify -> corroborate -> test -> promote/reject`.

### AEGIS lesson

Every imported idea must receive an epistemic class and evidence strength before entering the strategic architecture.

## M18 — The real research object is the control event

A line is too small to explain strategy. A whole file is too large to preserve causality cleanly. The useful unit is the control event:

`observation -> classification -> state transition -> authority effect -> action/resource consequence -> temporal guard -> reassessment`.

### AEGIS lesson

The knowledge ledger should preserve control events, not merely code excerpts.

## M19 — The source contains implicit commitment economics

Strategy changes, technology investment, production choices, resource reservation, and retreat behavior all interact with what future choices remain available.

### Meta-knowledge

The historical controller contains an implicit model of **option value** even when it cannot name it mathematically.

A commitment is valuable not only because of its direct payoff but because of what it enables or prevents later.

### AEGIS lesson

Strategic evaluation should include:

`benefit + initiative + future capability - opportunity cost - transition cost - replacement cost - exposure`.

## M20 — Strategic tempo is an emergent control resource

Timers, commitment persistence, attack windows, reassessment intervals, and resource-control mechanisms collectively affect who is forced to react next.

### Meta-knowledge

Tempo is not simply game time. It is control over the sequence of decisions.

### AEGIS lesson

Track initiative explicitly: who is forcing the next decision, who is responding, and what happens if the response is delayed.

## M21 — The designer model is closer to constrained control theory than to build-order scripting

Putting the findings together gives a coherent reconstruction:

> A changing environment produces observations. The controller compresses those observations into symbolic state, uses that state to select a capability portfolio, protects resources for valuable conversions, commits to actions only when conditions justify them, uses temporal mechanisms to stabilize behavior, preserves optionality after local failure, and repeatedly compares the observed world with the expected world.

That is a control system operating through a declarative symbolic substrate.

## AEGIS preserve / generalize / replace map

| Historical insight | AEGIS treatment |
|---|---|
| State decomposition | **Preserve + formalize** |
| Symbolic classifications | **Preserve + type** |
| Enemy strategy inference | **Preserve + add confidence/alternatives** |
| Resource control | **Preserve + explicit reservation model** |
| Timers/hysteresis | **Preserve + make semantic** |
| Attack state machine | **Preserve + centralize authority** |
| Retreat as preservation | **Preserve** |
| Reset/restart separation | **Preserve + formal failure scopes** |
| Distributed writers | **Replace with ownership contracts** |
| Magic thresholds without rationale | **Reject unless evidence supports them** |
| Historical experiments | **Preserve as archaeology; do not promote automatically** |
| Debug/compatibility machinery | **Classify as engine/history unless strategically justified** |
| Implicit option value | **Generalize into strategic evaluation** |
| Implicit tempo | **Generalize into initiative/tempo state** |
| Rule syntax as architecture | **Replace with explicit AEGIS architecture** |

## What this pass establishes

Pass 3 establishes a coherent meta-model of the historical programmer's engineering problem:

1. The AI was built as a feedback controller.
2. Symbolic state was the practical memory architecture.
3. Timers supplied temporal stabilization and memory.
4. Self-disabling rules supplied event semantics.
5. Distributed state traded verification clarity for expressibility.
6. Resources were treated as competing strategic commitments.
7. Enemy observations were compressed into predictive strategic state.
8. Attack and retreat were state transitions with different scopes.
9. Plans were provisional hypotheses requiring reassessment.
10. Historical complexity contains both genuine intelligence and substrate-driven debris.
11. The most durable contribution is the decomposition of strategic causality, not the syntax of the implementation.

## What remains unproven

The following require control-event-level corroboration before promotion to high-confidence universal principles:

- exact purpose of individual timers;
- authority of every major state variable;
- whether particular thresholds were strategic laws or empirical tuning;
- whether some apparent opportunity-cost behavior was incidental to implementation;
- which historical experiments materially improved final behavior;
- how much of the strategic model was authored versus inherited or later modified.

## Next pass — Layer 2 Pass 4

The next task is **Generalization**.

We will take the recovered historical knowledge and derive implementation-independent AoE2 strategic laws. Each law must be expressed without requiring the historical source to exist, then mapped to an AEGIS abstraction and eventually to measurable runtime signals.

Target transformation:

`HD control event -> implicit principle -> general AoE2 law -> formal strategic concept -> measurable state -> candidate decision policy -> validation experiment`.

The goal is to stop thinking in terms of “what this old bot did” and begin answering “what is actually true about strong AoE2 play, and how can a machine know it?”
