# AEGIS World Model — Architect Pass 2

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** ARCHITECT  
**Status:** Architecture contract candidate — not implementation  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Purpose

This pass compresses the Scientist findings into the smallest World Model contract that still survives the Carpenter and Adversary reviews.

The objective is not to design a database. It is to define the minimum semantic boundary between the observed game world and the systems that reason about it.

No `.per` implementation, runtime execution, or ABI allocation is authorized by this pass.

---

# 1. Architectural verdict

The World Model should be one conceptual subsystem with two physical responsibilities:

```text
OBSERVATION WORKBENCH
        ↓
 QUALIFY / PUBLISH
        ↓
     WORLD STATE
```

There is **no separate observation database, object database, belief database, or world-history database** in the architecture.

The World Model owns only information that earns persistence or publication.

Its core contract is:

> **Preserve useful world facts without pretending that observations are complete, permanent, or strategic interpretations.**

---

# 2. The minimum semantic state model

Published world information has a small semantic status vocabulary:

```text
CURRENT
LAST-KNOWN
UNKNOWN
UNRESOLVED / CONTRADICTED
```

These are not four storage rooms.

They are qualifications attached to information when required by its semantics.

The critical distinction is:

```text
NOT OBSERVED NOW
        ≠
PROVEN ABSENT
```

Therefore the World Model must never silently convert loss of observation into destruction or zero quantity.

---

# 3. The World Model contract

Every published fact must answer four questions when materially necessary:

```text
WHAT?
KIND?
STATUS?
EVIDENCE / PROVENANCE?
```

Conceptually:

```text
WORLD FACT
├── VALUE
├── KIND
├── STATUS
└── SOURCE / PROVENANCE when material
```

This is a semantic contract, not a universal runtime record schema.

A simple scalar may require only value + kind + status.

An identity-sensitive or conflicting observation may additionally require provenance or continuity evidence.

The architecture deliberately refuses to require metadata merely because metadata is fashionable.

---

# 4. World Model ownership

## World Model owns

- directly observed world facts;
- qualified observations derived directly from engine observation primitives;
- selected persistent facts whose continuity has practical value;
- world lifecycle/readiness observations where directly observable;
- selected world transitions when evidence is strong enough;
- semantic publication status.

## World Model does not own

- threat ratings;
- strategic priorities;
- opponent hypotheses;
- build orders;
- resource policy;
- military composition decisions;
- attack decisions;
- commitments;
- commands;
- recovery policy.

This boundary is load-bearing.

---

# 5. Observation Workbench

The Observation Workbench is the computational front end of the World Model.

Its job is to answer questions cheaply and transiently:

```text
SEARCH
FILTER
SELECT
READ
MEASURE
DERIVE
QUALIFY
```

It is a workspace, not permanent storage.

The architecture should prefer:

```text
QUESTION
  ↓
OBSERVE
  ↓
PUBLISH IF WORTH KEEPING
```

over:

```text
SCAN EVERYTHING
  ↓
STORE EVERYTHING
  ↓
HOPE SOMEONE USES IT
```

This directly supports the behavioral-return principle.

---

# 6. Persistence rule

A world fact earns persistence if at least one of these is materially true:

1. multiple consumers need it;
2. identity continuity matters;
3. recomputing it is materially expensive;
4. losing it creates dangerous strategic amnesia;
5. it represents a meaningful persistent world transition.

Otherwise, keep it transient.

This is the primary defense against building an unnecessary object database.

---

# 7. Aggregate semantics

Aggregates require special care.

The World Model must distinguish:

```text
OBSERVED COUNT
```

from:

```text
CONFIRMED TOTAL
```

and from:

```text
ESTIMATE / BELIEF
```

For example:

```text
2 enemy cavalry observed
```

must not silently become:

```text
enemy owns exactly 2 cavalry
```

unless the observation mechanism actually establishes completeness.

This is one of the most important anti-hallucination rules in the architecture.

---

# 8. Identity policy

Identity is evidence, not inference.

The architecture supports identity-sensitive world state only where continuity materially changes a decision.

If the engine provides sufficiently strong identity evidence:

```text
OBJECT A @ T0
        ↓
OBJECT A @ T1
```

may be treated as continuity.

If evidence is insufficient:

```text
same type + nearby position
```

is not enough to declare continuity.

For aggregate questions, individual identity should normally be unnecessary.

This prevents the World Model from becoming a one-record-per-unit simulation database.

---

# 9. Lifecycle and capability boundary

The architecture explicitly separates:

```text
OBJECT EXISTS
      ↓
OBJECT LIFECYCLE STATE
      ↓
OBJECT READY
      ↓
CAPABILITY AVAILABLE
      ↓
CAPABILITY EFFECTIVE
```

World Model may establish the observed object and lifecycle state.

Capability/Production determines what that state means operationally.

Example:

```text
stable foundation observed
        ↓
production building exists
        ↓
completion observed
        ↓
stable can contribute production capability
```

The World Model must not jump directly from existence to strategic capability.

---

# 10. Current versus last-known

The minimum safe publication model is:

```text
CURRENT
```

for a presently qualified observation, and:

```text
LAST-KNOWN
```

when a previous observation remains useful but is no longer current evidence.

`UNKNOWN` means the architecture has insufficient evidence to assert the proposition.

`UNRESOLVED / CONTRADICTED` means available evidence does not support choosing one interpretation safely.

These categories do not require universal timestamps.

Exact recency representation remains an implementation/ABI qualification question.

---

# 11. Supersession policy

When multiple observations can affect the same semantic fact, the World Model needs a local publication rule:

```text
NEW EVIDENCE
    ↓
IS IT QUALIFIED TO SUPERSEDE?
    ↓
 YES → publish / replace
 NO  → retain existing qualified state
```

The architecture does **not** require a universal generation counter yet.

A generation mechanism becomes necessary only where the implementation demonstrates that multiple writers or asynchronous transitions can otherwise corrupt state.

Thus:

> **Supersession is a semantic requirement; its machine representation remains open.**

---

# 12. Contradiction policy

Contradiction must be representable without forcing a false binary answer.

Example:

```text
T0: enemy building observed
T1: building not currently observable
```

The system must not automatically conclude:

```text
building destroyed
```

Instead:

```text
LAST-KNOWN: building present
CURRENT OBSERVATION: not observed
STATUS: unresolved
```

A later direct observation or qualified transition can resolve the contradiction.

---

# 13. Execution is an evidence source, not World Model ownership

Execution can produce evidence of a world transition.

For example:

```text
TRAIN COMMAND
     ↓
ACCEPTED / QUEUED
     ↓
COMPLETION EVIDENCE
     ↓
WORLD STATE UPDATE
```

The crucial rule is:

> A command is not automatically a world fact.

Likewise, Execution does not become the owner of World State merely because it can provide evidence about a transition.

This preserves the evidence ladder:

```text
INTENTION
AUTHORIZED
ISSUED
ACCEPTED / QUEUED
PENDING
CREATED
AVAILABLE
DEPLOYED
EFFECTIVE
```

The World Model consumes only the level justified by evidence.

---

# 14. World Model → Belief boundary

```text
WORLD FACT
    ↓
BELIEF
    ↓
STRATEGIC INTERPRETATION
```

The direction matters.

Belief may use world facts.

World State must not silently absorb beliefs merely because they are plausible.

Examples:

```text
WORLD FACT:
enemy stable observed

BELIEF:
enemy may be preparing cavalry

STRATEGIC INTERPRETATION:
raise cavalry containment priority
```

Only the first belongs in World State.

---

# 15. World Model → Situation boundary

Situation Analysis consumes world facts and combines them with:

- geometry;
- accessibility;
- damage/readiness;
- trajectories;
- objectives;
- risk posture;
- opponent evidence;
- economic constraints;
- time/tempo.

Therefore:

```text
WORLD STATE
    ↓
SITUATION ANALYSIS
    ↓
THREAT / OPPORTUNITY / FORECAST
```

The World Model should never become a disguised threat engine.

---

# 16. World Model → Capability boundary

Capability is not a raw object count.

Conceptually:

```text
WORLD FACTS
    +
TECHNOLOGY
    +
INFRASTRUCTURE
    +
PRODUCTION CAPACITY
    +
RESOURCE STATE
    +
TIME
        ↓
CAPABILITY
```

The World Model supplies the world facts.

The Capability system determines what can actually be produced, fielded, supported, or made effective.

This prevents the common architectural mistake of equating “the building exists” with “the capability exists.”

---

# 17. Attention and Scheduler relationship

The World Model must not decide how often it observes itself.

That responsibility belongs to the cross-cutting control layer:

```text
ATTENTION / SCHEDULER
        ↓
WHAT INFORMATION MATTERS NOW?
        ↓
OBSERVATION WORKBENCH
```

Observation cadence should be driven by decision value and urgency.

Examples:

- army safety: fast;
- production blockers: fast/periodic;
- economy rebalance: periodic;
- scouting questions: periodic/event-driven;
- strategic posture: slow/event-driven.

This protects runtime budget while increasing behavioral leverage.

---

# 18. The World Model's actual physical shape

The final conceptual floor plan is now intentionally small:

```text
                         REAL WORLD
                             │
                             ▼
                 ┌───────────────────────┐
                 │ OBSERVATION WORKBENCH │
                 │                       │
                 │ search / filter       │
                 │ select / read         │
                 │ measure / derive      │
                 └───────────┬───────────┘
                             │
                       QUALIFY / PUBLISH
                             │
                             ▼
                 ┌───────────────────────┐
                 │      WORLD STATE      │
                 │                       │
                 │ current              │
                 │ last-known           │
                 │ unresolved           │
                 │ selected transitions │
                 └───────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
           BELIEF        SITUATION       CAPABILITY
           MODEL          ANALYSIS         SYSTEM
```

Cross-cutting:

```text
OWNERSHIP
SUPERSESSION
EVIDENCE
ATTENTION
SCHEDULING
COST
```

No additional World Model rooms are currently justified.

---

# 19. What we deliberately removed

The Architect Pass 1 proposed a richer three-part conceptual structure.

This pass rejects the following as physical structures:

- separate World Register room;
- separate World Aggregate room;
- universal object records;
- universal provenance records;
- universal timestamp system;
- universal confidence engine;
- one manager per object;
- persistent copy of every search result;
- strategic threat storage inside World State;
- opponent hypotheses inside World State;
- recovery logic inside World State.

Those concepts may exist semantically where necessary, but they do not earn independent physical architecture.

---

# 20. High-leverage World Model pattern

The World Model becomes valuable when one observation produces many useful downstream consequences.

Example:

```text
ENEMY STABLE OBSERVED
        │
        ├── Opponent Model
        ├── Threat Analysis
        ├── Opportunity Analysis
        ├── Scouting Priority
        ├── Military Composition
        ├── Production Planning
        └── Attention Scheduling
```

One world fact.

Many consumers.

No duplicated ownership.

This is the architecture's implementation of the stock AI lesson:

> **maximize behavioral return per primitive.**

---

# 21. World Model acceptance criteria

The architecture is ready for empirical qualification only when the implementation can be tested against these questions:

1. Can the observation surface retrieve the required world fact?
2. Can it distinguish an observed subset from a complete total?
3. Can object identity be established reliably enough for continuity-sensitive decisions?
4. Can lifecycle state be observed distinctly from existence?
5. Can a current observation replace an older observation without stale overwrite?
6. Can disappearance from observation remain unresolved rather than becoming destruction?
7. Can contradiction remain representable?
8. Can execution evidence feed world transition without collapsing command and outcome?
9. Can World State remain separate from Belief?
10. Can World State remain separate from strategic interpretation?
11. Can observation frequency be controlled externally by Attention/Scheduler?
12. Can the representation stay small enough to justify its runtime cost?
13. Can multiple consumers use the same fact without duplicating ownership?
14. Can stale information be prevented from silently masquerading as current?
15. Can the implementation survive fog-of-war and partial observation?

Failure of any item blocks implementation of that semantic path until resolved.

---

# 22. Evidence classification

This architecture now distinguishes:

### PROVEN / DOCUMENTED

- AoE2DE exposes a substantial object/search/status observation surface.
- Stock AI uses search/filter/read and object-data concepts.
- Lifecycle/progress information exists in the scripting vocabulary.
- Execution commands and world observations are distinct conceptual surfaces.
- Search cost and scripting performance are real engineering constraints.

### OBSERVED / COMPOSED

- Stock behavior uses temporary observation workspaces and downstream state.
- Stock code demonstrates practical reuse of measurements across multiple decisions.

### INFERRED

- A selective persistent World State is preferable to a full object database for AEGIS.
- Local supersession is likely necessary wherever multiple evidence paths converge.

### PROPOSED

- `CURRENT / LAST-KNOWN / UNKNOWN / UNRESOLVED` semantic vocabulary.
- Question-driven observation scheduling.
- Persistence earning rules.
- Explicit aggregate qualification.
- Identity-only-when-material policy.

### OPEN

- Exact machine representation of semantic status.
- Exact current-build freshness mechanisms.
- Exact identity continuity guarantees.
- Exact absence/completeness guarantees for searches.
- Exact supersession/generation representation.
- Runtime cost of candidate observation schedules.

### REJECTED

- Treating non-observation as destruction.
- Treating observed subset as total force.
- Treating type similarity as identity continuity.
- Treating commands as completed world transitions.
- Storing strategic interpretation as world fact.
- Building a complete world database before proving the need.

---

# 23. Final architectural decision

The World Model is now reduced to its essential purpose:

> **Observe selectively, preserve only useful world truth, qualify what that truth actually means, and hand it to reasoning systems without contaminating it with their conclusions.**

Its physical architecture is:

```text
OBSERVATION WORKBENCH
        ↓
QUALIFIED WORLD STATE
        ↓
BELIEF / SITUATION / CAPABILITY
```

Its semantic safety rails are:

```text
CURRENT vs LAST-KNOWN
OBSERVED vs TOTAL
IDENTITY vs GUESS
EXISTENCE vs READINESS vs CAPABILITY
FACT vs BELIEF vs INTERPRETATION
COMMAND vs WORLD TRANSITION
NEWER vs STALE / SUPERSEDED
```

Its cross-cutting controls are:

```text
OWNERSHIP
EVIDENCE
SUPERSESSION
ATTENTION
SCHEDULING
COST
```

Nothing else gets added until a concrete failure demonstrates that it earns its place.

---

# 24. Handoff to the next mode

**NEXT MODE: 🔨 CARPENTER**

The Carpenter should now attack the compressed contract itself.

The key questions are no longer “what room are we missing?” They are:

1. Can any remaining semantic distinction be eliminated?
2. Are `CURRENT / LAST-KNOWN / UNKNOWN / UNRESOLVED` genuinely the minimum, or can one be derived?
3. Is `KIND` necessary everywhere, or only at interfaces?
4. Is provenance truly needed for the first implementation slice?
5. Is supersession a World Model responsibility or a cross-cutting publication service?
6. Can the World Model be expressed as fewer concepts without losing safety?
7. Which parts are architecture and which are merely documentation?
8. Does the design create enough behavioral leverage to justify itself?

The Carpenter's job is to remove anything that does not earn its existence.

Only after that should the Adversary attack the reduced form again.
