# AEGIS World Model — Adversary Pass 1

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** ADVERSARY  
**Status:** ADVERSARIAL REVIEW — NOT IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Mission

Try to break the Carpenter's simplified World Model before implementation.

The current physical design is intentionally small:

```text
REAL WORLD
    ↓
OBSERVATION WORKBENCH
    ↓
WORLD STATE
    ↓
BELIEF / SITUATION / CAPABILITY CONSUMERS
```

The adversary does not reward elegant diagrams. It searches for conditions under which accurate observations produce false state, stale state is treated as current, uncertainty becomes certainty, or correct world state still produces dangerous strategic behavior.

No `.per` implementation, runtime execution, or ABI allocation is authorized by this pass.

---

# 1. Adversarial verdict

**The Carpenter's simplification survives, but only after one important correction:**

> **WORLD STATE must not be treated as a single undifferentiated bucket. It needs a minimal distinction between CURRENTLY OBSERVED and LAST-KNOWN / UNCONFIRMED state.**

This does **not** justify restoring the Architect's full `WORLD_RECORD` machinery.

It means the simplified model needs one semantic safety rail:

```text
OBSERVATION WORKBENCH
        ↓
  PUBLISH / DISCARD
        ↓
WORLD STATE
├── CURRENT FACTS
└── QUALIFIED LAST-KNOWN FACTS
        ↓
BELIEF / SITUATION / CAPABILITY
```

The second category is not a database layer. It is a validity distinction.

Without it, the architecture is vulnerable to the most dangerous fog-of-war failure: treating an observation's disappearance as proof of disappearance in the world.

---

# 2. Attack #1 — Enemy army disappears

### Setup

AEGIS observes six enemy cavalry units.

Later, a search returns zero observable cavalry.

### Naive failure

```text
search result = 0
        ↓
enemy cavalry = 0
```

This is false under fog of war.

### Required behavior

```text
CURRENT OBSERVATION = no cavalry observed
LAST KNOWN = six cavalry
WORLD CERTAINTY = unresolved
```

Situation Analysis may then decide whether the old observation remains strategically relevant.

### Result

**FAILURE FOUND.**

The Carpenter design needs an explicit semantic distinction between “currently observed absent” and “known absent.”

### Correction

The World State must support at least:

- **PRESENTLY OBSERVED**
- **NOT CURRENTLY OBSERVED / LAST KNOWN**

It does not need a universal freshness timer yet.

---

# 3. Attack #2 — Enemy army moves

### Setup

A cavalry group is observed at location A.

Later the group is observed at location B.

### Failure mode

If A remains published as current simply because it was once true, downstream systems may defend an empty location.

### Required semantic rule

A newer qualified observation supersedes an older current observation for the same continuity identity **when identity continuity has actually been established**.

If identity continuity cannot be established, A and B may represent two separate observations and must not be silently merged.

### Result

**SURVIVES with qualification.**

The architecture does not need universal identity tracking. It needs identity only when continuity changes a decision.

---

# 4. Attack #3 — Unit replacement

### Setup

Enemy knight X dies.

Enemy knight Y appears nearby.

Both are the same unit type.

### Failure

A naive record keyed only by type or location may conclude:

`X survived.`

### Correction

Identity is optional but becomes mandatory when the decision depends on continuity of a specific object.

If the strategic question is merely:

`How much cavalry is present?`

then aggregate observation is sufficient and individual identity is unnecessary.

### Result

**SURVIVES.**

This validates the Carpenter's anti-database rule.

---

# 5. Attack #4 — Building lifecycle

### Setup

A production building is observed as a foundation.

Later it completes.

### Failure

`building exists` is mistaken for `building can produce`.

### Required distinction

```text
OBJECT OBSERVED
      ↓
LIFECYCLE STATE
      ↓
READINESS / CAPABILITY
```

World State owns the observed lifecycle fact.

Capability/Production determines whether it represents usable production.

### Result

**SURVIVES.**

This remains one of the architecture's most important boundaries.

---

# 6. Attack #5 — Building destroyed while capability is committed

### Setup

Production planning believes two stables are available.

One is destroyed.

A production commitment still assumes two-stable throughput.

### Failure

World State may be correct while Commitment/Execution is stale.

### Lesson

This is **not a World Model problem alone**.

It exposes a cross-system requirement:

> Capability consumers must be able to detect that a world-state prerequisite for a commitment has changed.

Therefore World State must publish materially relevant transitions, but Commitment/Execution owns the response.

### Result

**BOUNDARY FAILURE, NOT WORLD-MODEL FAILURE.**

This is important. Do not stuff recovery logic into World State.

---

# 7. Attack #6 — Correct observation, wrong strategy

### Setup

World State correctly reports:

`enemy has 12 knights.`

Situation Analysis decides this requires an enormous anti-cavalry investment.

But the knights are trapped, damaged, and unable to threaten anything important.

### Result

**WORLD MODEL CAN BE CORRECT WHILE STRATEGY IS WRONG.**

This is healthy architecture.

The World Model should report facts. Situation Analysis must account for geometry, accessibility, damage, trajectory, objectives, and risk.

Do not contaminate World State with strategic weighting merely to prevent bad decisions downstream.

---

# 8. Attack #7 — Observation is accurate but stale

### Setup

At time T0, an enemy army is accurately observed.

At T1, the army changes composition.

At T2, an old consumer reads the T0 state as if it were current.

### Failure

Truth becomes dangerous because its age is hidden.

### Required minimum

A published state that can materially become stale needs some qualified notion of recency or supersession.

But the architecture must not invent engine timestamps.

Therefore:

```text
CURRENT
LAST-KNOWN
UNKNOWN
```

is currently sufficient as an architectural semantic model.

Exact implementation of recency remains an empirical question.

### Result

**SURVIVES after minimal validity distinction.**

---

# 9. Attack #8 — Contradictory observations

### Setup

One observation says an enemy building exists.

Another says no such building is currently observable.

### Bad response

Pick one arbitrarily.

### Better response

Preserve the contradiction as uncertainty until evidence resolves it.

Conceptually:

```text
OBS A: building observed
OBS B: building not currently observed
        ↓
DO NOT ASSERT DESTRUCTION
```

A later direct observation of destruction, absence under a sufficiently qualified search, or another reliable transition may resolve it.

### Result

**SURVIVES if contradiction is allowed to remain unresolved.**

The World Model must not force binary truth when the observation system cannot justify it.

---

# 10. Attack #9 — Same observation, conflicting consumers

### Setup

Enemy stable observed.

Military wants it interpreted as cavalry capacity.

Scouting wants it interpreted as an exploration target.

Opportunity analysis wants it interpreted as a vulnerable infrastructure target.

### Failure risk

Each room creates its own copy of “enemy stable.”

### Correct architecture

One world fact, many interpretations:

```text
ENEMY STABLE OBSERVED
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
THREAT MAP  OPPORTUNITY
```

### Result

**STRONGLY SURVIVES.**

This is one of the highest-leverage properties of the design.

---

# 11. Attack #10 — Partial observation

### Setup

A scout sees two cavalry units.

The enemy actually has ten.

### Failure

World State stores:

`enemy cavalry = 2`

and downstream treats it as total force.

### Correction

The semantic label must distinguish:

`OBSERVED COUNT = 2`

from:

`TOTAL ENEMY COUNT = 2`.

The former is a world observation.

The latter is a belief or inference unless the observation surface provides completeness.

### Result

**FAILURE FOUND unless aggregate semantics are explicit.**

This is another reason not to let the World Model expose ambiguous quantities.

Every aggregate needs a semantic qualifier such as:

- observed;
- confirmed total;
- estimated;
- last known.

This does not require a giant confidence framework.

---

# 12. Attack #11 — False continuity

### Setup

Two units of the same type occupy nearly identical positions at different times.

### Failure

AEGIS assumes they are the same object.

### Result

Identity continuity must never be inferred solely from similarity unless the engine evidence supports it.

Therefore:

> **Identity is evidence, not a guess.**

When continuity cannot be established, treat observations as separate facts/measurements rather than forcing a persistent identity.

---

# 13. Attack #12 — World State becomes a hidden planner

### Setup

The World Model stores:

`enemy cavalry threat = high`

### Failure

That is no longer world description. It is strategic interpretation.

### Result

**REJECTED.**

World State may store:

`observed enemy cavalry presence`.

Situation Analysis may derive:

`cavalry threat = high`.

This remains a hard ownership boundary.

---

# 14. Attack #13 — Execution succeeds but World State lags

### Setup

A unit completes training.

Execution knows the command completed.

World State still reflects the previous production state.

### Failure

Planning sees stale capability and issues unnecessary production.

### Lesson

World Model cannot be the sole source of truth for every execution transition.

The architecture needs a controlled path for **qualified execution/world-transition evidence** to update World State.

But this does not make Execution the owner of World State. It makes execution evidence one possible input.

### Result

**SURVIVES with explicit evidence boundary.**

---

# 15. Attack #14 — Observation itself is expensive

### Setup

AEGIS scans large portions of the map every rule cycle.

### Failure

The World Model is conceptually correct but computationally ruinous.

### Result

The question-driven observation rule survives and becomes mandatory:

> **No observation without a consumer or explicit strategic reason.**

Observation frequency belongs under Scheduler/Attention, not World State.

This reinforces the separation:

```text
WHAT DO WE NEED TO KNOW?
        ↓
ATTENTION / SCHEDULER
        ↓
HOW DO WE OBSERVE IT?
        ↓
OBSERVATION WORKBENCH
```

---

# 16. Attack #15 — Information is technically current but strategically irrelevant

### Setup

World State accurately tracks an enemy farm or isolated house.

No current strategic decision depends on it.

### Failure

Storage and update cost grows without behavioral return.

### Result

The Carpenter's persistence rule survives:

> **If information does not preserve useful continuity, reduce dangerous amnesia, serve multiple consumers, or avoid material recomputation, do not persist it.**

---

# 17. Attack #16 — World State corruption

### Setup

A stale writer overwrites newer state.

### Failure

Old truth becomes current truth.

### Required architectural guard

Published state must have an ordering/supersession concept where multiple writers can update the same semantic field.

But this should be local, not universal.

Conceptually:

```text
NEW OBSERVATION
      ↓
IS THIS NEWER / BETTER QUALIFIED?
      ↓
YES → PUBLISH
NO  → DISCARD / RETAIN LAST VALID
```

Exact generation implementation is deferred until representation is qualified.

### Result

**SURVIVES with local supersession rule.**

---

# 18. Attack #17 — World State and Belief collapse

### Setup

The enemy's stable was last observed two minutes ago.

Belief predicts it still exists.

A consumer reads that prediction as direct fact.

### Result

The boundary must be explicit:

```text
WORLD FACT
   ↓
BELIEF
   ↓
STRATEGIC INTERPRETATION
```

Belief can inherit world evidence.

World State cannot inherit belief merely because the belief is plausible.

---

# 19. The adversary's central discovery

The most dangerous architectural ambiguity is not storage.

It is **semantic qualification of observations**.

A number such as:

`2 cavalry`

is uselessly ambiguous.

It must answer:

> **Two what, observed how, at what semantic status?**

At architecture level the minimum useful vocabulary is:

```text
VALUE
KIND
STATUS
SOURCE / PROVENANCE WHEN MATERIAL
```

Where `STATUS` can remain intentionally small:

```text
CURRENT
LAST-KNOWN
UNKNOWN
CONTRADICTED
```

Not every value needs every status.

The architecture should not implement this as a universal record schema. It is a semantic contract for published information.

---

# 20. Adversarial correction to the Carpenter design

The Carpenter successfully removed unnecessary physical structure.

The Adversary adds one correction:

### Before

```text
OBSERVATION WORKBENCH → WORLD STATE
```

### After

```text
OBSERVATION WORKBENCH
          ↓
   QUALIFIED PUBLISH
          ↓
      WORLD STATE
      ├── CURRENT
      ├── LAST-KNOWN
      ├── UNKNOWN
      └── CONTRADICTED
```

This is not four databases.

It is one semantic state surface.

Likewise, provenance and ordering are not mandatory bureaucracy. They become mandatory only when multiple observations could otherwise corrupt meaning.

---

# 21. Final adversarial acceptance test

The simplified World Model passes only if it can answer these questions without ambiguity:

1. What was actually observed?
2. Is this a current observation or merely last-known information?
3. Is this quantity an observed subset or a confirmed total?
4. Is object identity proven or merely guessed?
5. Has a newer observation superseded this one?
6. Could this state be contradicted without implying destruction?
7. Is this a world fact or a belief?
8. Is this a world fact or a strategic interpretation?
9. Does object readiness differ from capability availability?
10. Which subsystem owns the next decision?
11. Who is allowed to replace this state?
12. What happens if the observation is wrong?
13. What happens if it is stale?
14. What happens if it disappears because of fog of war?
15. What happens if execution changes the world before observation catches up?
16. Why does this information deserve persistence?

If the architecture cannot answer these, implementation is premature.

---

# 22. Carpenter + Adversary combined design

The current recommended World Model is now:

```text
                         REAL WORLD
                             │
                             ▼
                 ┌───────────────────────┐
                 │ OBSERVATION WORKBENCH │
                 │ search/filter/select  │
                 │ read / measure / derive│
                 └───────────┬───────────┘
                             │
                     QUALIFY / PUBLISH
                             │
                             ▼
                 ┌───────────────────────┐
                 │      WORLD STATE      │
                 │                       │
                 │ current facts        │
                 │ last-known facts     │
                 │ unresolved state      │
                 │ selected transitions │
                 └───────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
           BELIEF        SITUATION       CAPABILITY
           MODEL          ANALYSIS        SYSTEM
```

Underneath the entire surface:

```text
OWNERSHIP
SUPERSESSION
EVIDENCE
SCHEDULING
COST
```

These are cross-cutting controls, not additional rooms.

---

# 23. What the Adversary explicitly rejects

The attack does **not** justify:

- a complete object database;
- universal timestamps before engine support is proven;
- one persistent record per unit;
- a universal confidence engine;
- strategic threat values inside World State;
- opponent hypotheses inside World State;
- automatic destruction inference from non-observation;
- automatic total-force inference from partial observations;
- guessed identity continuity;
- World State owning recovery;
- World State owning commands;
- World State becoming a hidden planner;
- a separate room for every semantic status;
- implementation before empirical qualification.

---

# 24. Verdict

**ADVERSARY RESULT: PASS WITH CORRECTION.**

The Carpenter's simplification was the right move.

The Architect's three physical layers were unnecessary.

But the simplified design was too permissive about the meaning of published state.

The smallest robust correction is:

> **World State is one selective state surface whose published facts carry only the semantic qualification necessary to prevent stale, partial, contradictory, or fog-of-war observations from masquerading as current complete truth.**

This preserves the original objective:

**maximum behavioral leverage per primitive, minimum machinery necessary to make that leverage trustworthy.**

The next mode should be **SCIENTIST**.

The Scientist must now determine which pieces of this adversarial correction are actually supportable by the AoE2DE engine and stock evidence, rather than allowing the architecture to turn sensible semantics into assumed ABI capabilities.

That means the next pass should ask:

- Which state qualifiers can the engine represent directly?
- Which must be derived?
- Can ordering/supersession be represented safely?
- What stock primitives expose lifecycle transitions?
- What exactly can search results prove about absence?
- What can `object-data-*` prove about identity and ownership?
- Which parts of the proposed semantic contract require runtime experiments?

**No implementation. No runtime. No ABI allocation.**

The building survived the fire. Now we test whether the fireproofing is actually made of steel.