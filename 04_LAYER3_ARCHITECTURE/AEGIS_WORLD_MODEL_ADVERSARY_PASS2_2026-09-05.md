# AEGIS World Model — Adversary Pass 2

**Date:** 2026-09-05  
**Layer:** 3A — Subsystem five-pass review  
**Mode:** ADVERSARY  
**Pass:** 3 of 5  
**Target build:** AoE2DE `101.103.48987.0`  
**Status:** ADVERSARIAL INTEGRATION REVIEW — NO IMPLEMENTATION  

## 0. Mission

Attack the Carpenter-reduced World Model under full-system conditions. The question is not whether the World Model is elegant in isolation. The question is whether it remains truthful when Economy, Production, Scouting, Situation, Capability, Decision, Scheduler, Commitment, Execution, Verification, Recovery, Memory, and Map systems simultaneously consume and influence information about the same changing world.

No `.per` implementation, runtime execution, or ABI allocation is authorized by this pass.

## 1. Starting architecture

The Carpenter reduced the subsystem to two physical responsibilities:

```text
REAL WORLD
    ↓
OBSERVE / QUALIFY
    ↓
WORLD STATE
    ↓
INTERPRET
    ↓
CAPABILITY
    ↓
DECIDE / COMMIT
    ↓
EXECUTE
    ↓
VERIFY
    ↓
WORLD STATE
```

The following remain semantic rules rather than dedicated infrastructure:

- current vs last-known information;
- unknown and unresolved state;
- selective persistence;
- selective identity continuity;
- supersession;
- conditional provenance;
- partial-observation scope;
- material revalidation.

## 2. Adversarial verdict

**PASS WITH TARGETED CORRECTION.**

The reduced architecture survives the cross-system attack. I found no justification for restoring the rejected database, manager, event-bus, transaction, or universal-metadata machinery.

One rule must be made more explicit:

> **A retained World State fact must carry enough semantic qualification for every consequential consumer to know what claim the evidence actually supports.**

This is not a universal metadata schema. It is an ownership and publication rule. A value that is ambiguous between `observed`, `last-known`, `partial`, and `confirmed` is unsafe at the boundary.

## 3. Attack: simultaneous objectives

Suppose the AI simultaneously wants to:

- defend villagers;
- establish Castle Age timing;
- maintain production;
- scout the opponent;
- expand map control.

Several systems ask the Workbench overlapping questions.

Failure mode:

```text
SYSTEM A observes X
SYSTEM B observes X differently
SYSTEM C stores X independently
```

This creates competing truths.

Required rule:

```text
ONE WORLD FACT
      ↓
ONE AUTHORITATIVE WORLD-STATE PUBLICATION
      ↓
MANY CONSUMERS
```

Consumers may derive different interpretations. They may not silently create competing versions of the underlying fact.

**Result: survives. No new subsystem required.**

## 4. Attack: fog of war

Enemy army is observed at position A.

Later the army cannot be found.

Bad system:

```text
NOT FOUND → ZERO
```

Correct system:

```text
NOT CURRENTLY OBSERVED
        ↓
LAST-KNOWN / UNKNOWN
```

The World Model must never manufacture destruction, retreat, or disappearance from absence alone.

**Result: survives. Currentness semantics remain load-bearing.**

## 5. Attack: partial census

A search sees three enemy cavalry units.

The opponent may have additional cavalry outside the observation scope.

Failure:

```text
OBSERVED = 3
        ↓
TOTAL = 3
```

Required distinction:

```text
OBSERVED COUNT
≠
CONFIRMED TOTAL
≠
STRATEGIC ESTIMATE
```

The first belongs to World State when retained. The latter interpretations belong elsewhere unless independently established.

**Result: survives. No aggregate manager required.**

## 6. Attack: false identity continuity

An object disappears and another object of the same type appears later.

Failure:

```text
SAME TYPE → SAME OBJECT
```

Required rule:

> Identity continuity is accepted only when supported by evidence sufficient for the decision using it.

If continuity cannot be established, the World Model must tolerate a new identity or unresolved relationship.

**Result: survives. No identity manager required.**

## 7. Attack: lifecycle race

A production building is observed.

A commitment assumes it is usable.

Before execution, the building is destroyed or is not actually ready.

Failure:

```text
EXISTS → AVAILABLE
```

Correct chain:

```text
EXISTS
  ↓
LIFECYCLE / STATUS
  ↓
READY
  ↓
CAPABILITY
```

Capability must be revalidated when the relevant assumption may have changed.

**Result: survives. Revalidation remains an execution gate, not a manager.**

## 8. Attack: command becomes fake evidence

AEGIS issues a train/build/research command.

A naive World Model records the intended result immediately.

That creates:

```text
INTENT → WORLD FACT
```

This is forbidden.

The correct direction is:

```text
COMMAND
   ↓
EXECUTION
   ↓
OBSERVABLE RESULT
   ↓
QUALIFY
   ↓
WORLD STATE
```

Command issuance may be useful evidence that an attempt occurred, but it is not proof that the world transitioned successfully.

**Result: survives. This is a hard invariant.**

## 9. Attack: execution succeeds but objective fails

A unit is successfully trained.

That does not prove:

```text
OBJECTIVE ACHIEVED
```

The World Model may publish:

```text
UNIT EXISTS
```

Situation/Decision/Verification determine whether the strategic purpose was achieved.

**Result: survives. World State remains deliberately narrower than strategy.**

## 10. Attack: stale commitment

Sequence:

```text
OBSERVE cavalry = 2
↓
PLAN spearmen
↓
COMMIT
↓
Enemy produces 8 cavalry
↓
EXECUTE old plan
```

The architecture must not demand globally fresh state at all times. It must instead identify consequential boundaries where material assumptions require revalidation.

```text
COMMIT
  ↓
MATERIAL CHANGE?
 /          \
NO          YES
 |            ↓
 |        REVALIDATE
 |            ↓
 └────── EXECUTE / REPLAN
```

**Result: survives. No global freshness engine justified.**

## 11. Attack: feedback contamination

Execution observes an intended result.

The execution layer is tempted to write that result directly as world truth.

This would let intent certify itself.

Hard rule:

```text
INTENT ≠ EVIDENCE

COMMAND ≠ OUTCOME

OUTCOME CLAIM ≠ VERIFIED WORLD FACT
```

Only qualified observation/verification may publish the resulting world fact.

**Result: survives and is strengthened as a constitutional rule.**

## 12. Attack: two writers disagree

Example:

```text
Scouting says enemy stable exists.
Military says stable destroyed.
```

Neither downstream interpretation gets to overwrite the underlying world fact merely because its conclusion depends on it.

The publisher must evaluate evidence and produce:

```text
CURRENT
LAST-KNOWN
RETAIN
or
UNRESOLVED
```

If evidence is insufficient, uncertainty is preferable to arbitrary winner selection.

**Result: survives. No conflict manager justified.**

## 13. Attack: scheduler starvation

A cheap economy observation repeatedly consumes attention while a high-consequence enemy-transition question is delayed.

This is not fundamentally a World Model storage problem.

It is Scheduler/Attention failure.

World Model therefore must expose observations in a form that permits priority-sensitive consumers, while Scheduler owns cadence and prioritization.

**Result: survives. Ownership boundary remains correct.**

## 14. Attack: observation cost explosion

A naive implementation continuously searches every enemy object, every resource, every production site, and every unit.

This destroys runtime budget.

The Workbench must remain question-driven and Scheduler-controlled.

The World Model does not earn authority to poll merely because information is interesting.

**Result: survives. No World Model scheduler required.**

## 15. Attack: resource/capability/world disagreement

Suppose:

```text
WORLD STATE: barracks exists
RESOURCE STATE: enough food/wood
CAPABILITY: spearman production feasible
```

Then another event invalidates one assumption.

The correct response is not to decide which subsystem is “more true.” Each owns a different semantic question.

```text
WORLD STATE → what exists / what is observed
CAPABILITY → what can be done
DECISION → what should be done
EXECUTION → what was attempted
VERIFICATION → what actually happened
```

If evidence conflicts, the system re-observes and reconciles at the appropriate boundary.

**Result: survives.**

## 16. Attack: strategic interpretation overwrites fact

Example:

```text
WORLD:
enemy stable observed

SITUATION:
cavalry threat elevated

STRATEGY:
defensive posture
```

If cavalry threat later falls, Situation may change without rewriting the historical fact that a stable was observed.

Conversely, if the stable is destroyed, World State changes and downstream interpretation must respond.

This directional dependency is essential:

```text
WORLD FACT → INTERPRETATION
```

not:

```text
INTERPRETATION → WORLD FACT
```

**Result: survives.**

## 17. Attack: contradiction during rapid change

A building is observed complete.

A subsequent observation says it is no longer available.

The architecture must not force immediate certainty about the causal explanation.

The safe sequence is:

```text
NEW EVIDENCE
   ↓
QUALIFY
   ↓
CURRENT / LAST-KNOWN / UNRESOLVED
```

Downstream systems can decide whether to investigate further.

**Result: survives. No contradiction database needed.**

## 18. Attack: capability becomes obsolete

Capability was valid when the decision was made.

The world changes.

The capability assessment is now obsolete.

Failure mode:

```text
OLD CAPABILITY
    ↓
PERMANENT AUTHORITY
```

Correct model:

```text
CAPABILITY IS CONDITIONAL ON CURRENTLY RELEVANT WORLD STATE
```

At consequential execution boundaries, revalidate material assumptions.

**Result: survives.**

## 19. Attack: recovery loop

A failed execution returns evidence that the desired state was not reached.

Bad recovery:

```text
FAIL
↓
RETRY SAME THING
↓
FAIL
↓
RETRY
```

World Model must publish the failure evidence. Recovery owns the response.

Required policy:

```text
FAILED COMMITMENT
→ REPAIR
→ CHANGE ASSUMPTION
→ CHANGE CANDIDATE
→ ABANDON
→ ESCALATE / REASSESS
```

At least one material condition must change before indefinite retry.

**Result: survives. Recovery remains outside World State.**

## 20. Attack: belief contaminates world state

Opponent Model infers:

```text
"Opponent is preparing cavalry." 
```

That hypothesis must not become:

```text
WORLD FACT:
Opponent has cavalry.
```

The direction must remain:

```text
WORLD EVIDENCE
    ↓
BELIEF / HYPOTHESIS
    ↓
SITUATION
```

Belief may be wrong. World State must not be rewritten to make belief look correct.

**Result: survives.**

## 21. Attack: correct World State, bad strategy

This is important because the World Model can be completely correct and AEGIS can still lose.

Example:

```text
WORLD:
enemy stable exists

SITUATION:
cavalry risk elevated

CAPABILITY:
spearmen feasible

DECISION:
produce spearmen

RESULT:
strategically bad because enemy is transitioning to ranged units
```

This is **not a World Model failure**.

The subsystem must not expand merely because downstream reasoning is imperfect.

**Result: boundary preserved.**

## 22. Attack: map-control distortion

The same military force has different practical value depending on location, access, reinforcement distance, and map control.

World Model should expose spatial facts.

It should not calculate strategic map value.

That belongs to Situation/Map Control/Capability.

**Result: survives.**

## 23. Attack: memory pollution

If every transient observation is retained, World State becomes historical sludge.

Failure:

```text
OBSERVE EVERYTHING
→ STORE EVERYTHING
→ REASON THROUGH EVERYTHING
```

Persistence must remain selective.

A fact that nobody materially consumes and whose recomputation is cheap should normally die in the Workbench.

**Result: survives. Persistence test is load-bearing.**

## 24. Attack: World State becomes hidden planner

A dangerous implementation shortcut is to add fields such as:

```text
recommended-response
priority
threat-score
next-action
preferred-unit
```

to World State.

That would collapse:

```text
FACT → INTERPRETATION → DECISION
```

into one contaminated state store.

**Hard rejection:** strategic recommendation does not belong in World State.

## 25. Attack: universal metadata creep

Implementation pressure will eventually suggest adding:

```text
VALID
OWNER
GENERATION
TIMESTAMP
CONFIDENCE
EXPIRY
SOURCE
PRIORITY
```

to everything.

The adversary rejects this unless an actual field demonstrates a need.

The architecture already permits these concepts where materially required, but refuses universal representation.

**Result: survives Carpenter cut.**

## 26. Attack: stock ABI contamination

Stock strategic numbers/goals and stock semantic channels have heavy multiplexing and established ownership. AEGIS must not infer that a similar stock field is available merely because it looks useful.

The World Model architecture therefore remains representation-neutral until the Scientist/ABI phase qualifies concrete fields.

**Result: survives. No stock channel hijacking permitted.**

## 27. Attack: implementation convenience changes ownership

A programmer may discover that it is easier to have Military write an enemy-count field directly than route it through World State.

That is rejected.

Convenience is not authority.

If the semantic fact is a World State fact, World State owns publication of it.

## 28. Attack: oscillation

Rapid observations could cause:

```text
enemy cavalry detected
→ cavalry threat high
→ produce spears
→ cavalry disappears
→ cancel spears
→ cavalry reappears
→ produce spears
```

This is primarily a Situation/Decision/Commitment policy problem, not a World Model problem.

World Model's job is to preserve evidence faithfully. Hysteresis, commitment duration, and strategic inertia belong downstream.

**Result: boundary preserved.**

## 29. Attack: execution evidence arrives out of order

Suppose an earlier command's verification result is observed after a later world change.

The architecture cannot assume that every evidence item is globally ordered merely because it was observed later.

Therefore:

> **Observation order is not automatically world-event order.**

The eventual representation of ordering/generation remains an empirical question. The semantic rule is simply that evidence must not supersede newer qualified state without justification.

**Result: survives; representation deferred to Scientist.**

## 30. Attack: World Model becomes a second memory system

Strategic Memory already exists conceptually.

World Model should not absorb long-term strategic lessons such as:

```text
Opponent likes cavalry openings.
Opponent historically booms on Arena.
```

Those are historical/strategic memory.

World Model should retain world facts and selected transitions; Memory stores reusable strategic/history information.

**Result: boundary preserved.**

## 31. Load-bearing invariants after attack

The adversary identifies the following invariants as non-negotiable:

1. World facts have one authoritative publisher.
2. Observation is not automatically complete knowledge.
3. Non-observation is not destruction.
4. Observed count is not automatically total count.
5. Identity continuity requires evidence.
6. Object existence is not capability.
7. Capability is not decision.
8. Decision is not command.
9. Command is not success.
10. Verification evidence must return through the evidence boundary.
11. Intent may never self-certify as world truth.
12. Last-known information may not silently become current.
13. Contradiction may remain unresolved.
14. Materially stale assumptions require revalidation before consequential execution.
15. Failed commitments cannot retry forever unchanged.
16. Observation cost is controlled by Scheduler/Attention.
17. Strategic interpretation cannot rewrite world facts.
18. World State remains selective.
19. Stock state channels are not implicitly AEGIS-owned.
20. Unknown engine representation is tested rather than assumed.

## 32. What the adversary tried to force—and refused to add

The attack produced no justification for:

- object database;
- identity manager;
- aggregate manager;
- contradiction manager;
- freshness manager;
- provenance manager;
- supersession manager;
- universal timestamp system;
- universal generation system;
- universal confidence system;
- world-event bus;
- transaction engine;
- World Model scheduler;
- hidden strategic planner inside World State;
- one record per unit;
- stock ABI channel reuse without qualification.

These remain rejected unless later evidence demonstrates a concrete failure that cannot be solved locally.

## 33. Targeted correction

One correction is promoted from implicit to explicit:

> **Every consequential consumer must be able to distinguish the strength and scope of a retained World State claim sufficiently to avoid treating partial, last-known, or unresolved information as confirmed current fact.**

This does not prescribe fields, goals, strategic numbers, timestamps, or implementation machinery.

It is a semantic acceptance condition for the future ABI qualification.

## 34. Adversary verdict

**WORLD MODEL PASS 3 RESULT: PASS WITH TARGETED CORRECTION.**

The Carpenter's two-part physical architecture survives full-system attack.

The correction is semantic, not structural:

```text
OBSERVE
   ↓
QUALIFY
   ↓
PUBLISH CLAIM WITH SUFFICIENT SCOPE/STATUS
   ↓
WORLD STATE
```

No additional World Model room is justified.

## 35. Handoff to Scientist

The next pass must determine which of these invariants the actual AoE2DE engine can represent directly, which are derivable from multiple engine observations, and which require empirical runtime qualification.

Scientist must specifically test or qualify:

- observation scope and completeness;
- current vs last-known representation;
- lifecycle transitions;
- identity continuity;
- object ownership and status;
- ordering/supersession;
- command/result separation;
- search-state semantics;
- feasibility versus actual execution;
- representation cost;
- whether selected retained facts can be published without destructive aliasing of stock channels.

No implementation is authorized by this pass.

**NEXT MODE: 🔬 SCIENTIST — World Model, Pass 4 of 5**
