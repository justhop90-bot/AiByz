# AEGIS World Model — Carpenter Pass 1

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** CARPENTER  
**Status:** ADVERSARIAL SIMPLIFICATION REVIEW — NOT IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`  
**Parent:** World Model Architect Pass 1  

## 0. Mission

The Architect proposed a selective World Model with three physical layers: temporary Observation Workspace, persistent World Register, and World Aggregates. The Carpenter's job is not to admire the structure. It is to remove anything that does not earn its space.

The governing question is:

> **What is the minimum structure that preserves the useful behavioral leverage without turning `.per` into a fake database?**

No implementation, runtime execution, or ABI allocation is authorized by this document.

---

# 1. Carpenter's verdict

The Architect was directionally correct but still over-described the physical machinery.

The three layers should **not** become three literal rooms.

The simpler physical model is:

```text
OBSERVE / COMPUTE
       ↓
PUBLISH SELECTED WORLD STATE
       ↓
WORLD STATE
```

The previous `World Register` and `World Aggregates` distinction remains useful **semantically**, but should not automatically become separate storage systems.

Likewise, `WORLD_RECORD` should be treated as a contract for information, not a promise that AEGIS will maintain an object record for every relevant entity.

This removes a large amount of conceptual furniture while preserving the architecture's useful boundaries.

---

# 2. What gets demolished

## REMOVE: three physical storage layers

There is no demonstrated need for three separate persistent mechanisms.

Keep:

- temporary observation workspace;
- selected persistent world state.

Treat aggregates as a **kind of world state**, not a separate room.

## REMOVE: mandatory WORLD_RECORD

A universal record shape encourages one-record-per-object thinking.

Instead, define a semantic field contract and allow representations to vary by use case.

A military count does not need an object identity field.

A persistent strategic location may need identity and position.

A transient local count may need neither.

## REMOVE: universal provenance object

Provenance remains mandatory as an architectural concept, but does not require a heavyweight record attached to every measurement.

The minimum useful provenance is:

`WHAT WAS OBSERVED + HOW IT WAS OBSERVED + WHEN/GENERATION IF QUALIFIED`.

Exact encoding remains an empirical/representation question.

## REMOVE: universal freshness state machine

The architecture should not create `CURRENT / RECENT / STALE / UNKNOWN / CONTRADICTED` as a mandatory state machine before the engine has been qualified to support the required distinctions.

Freshness is a property of information, not necessarily a permanent field on every world fact.

## REMOVE: universal generation field

Generation is valuable where replacement or supersession matters.

It is unnecessary for every observation.

Generation therefore becomes **conditional metadata**, not a universal structural requirement.

---

# 3. What survives the saw

Four boundaries are genuinely load-bearing:

### A. OBSERVATION
What the engine/search operation directly supplied.

### B. WORLD STATE
What AEGIS has selected as sufficiently valuable and trustworthy to preserve as its current structured picture of relevant reality.

### C. BELIEF
What AEGIS thinks may be true despite incomplete or stale observation.

### D. SITUATION
What the current world state and beliefs mean strategically.

The fundamental wall remains:

```text
OBSERVATION ≠ WORLD STATE ≠ BELIEF ≠ SITUATION
```

This boundary is worth more than the three physical layers proposed previously.

---

# 4. The smallest useful World Model

The Carpenter's reduced model is:

```text
                 REAL GAME
                     ↓
             OBSERVATION WORK
          search / filter / select
                     ↓
              READ / DERIVE
                     ↓
          ┌──────────┴──────────┐
          │                     │
       TEMPORARY           PUBLISH
       MEASUREMENT        WORLD STATE
          │                     │
          └──────────┬──────────┘
                     ↓
             BELIEF / SITUATION
```

This is the preferred physical architecture until evidence demonstrates that additional machinery is necessary.

---

# 5. Persistence test — tightened

The Architect proposed five reasons to persist. The Carpenter makes them stricter.

A value may become persistent only when there is a concrete benefit from persistence:

1. **Continuity:** the same world entity/state must be recognized across observations.
2. **Fan-out:** multiple consumers need the same derived answer.
3. **Cost:** recomputation is materially expensive.
4. **Safety:** losing the information would create dangerous strategic amnesia.
5. **Transition:** a world change must survive the immediate observation cycle.

If none applies:

> **Do not store it. Recompute it.**

This is a major anti-bloat rule.

---

# 6. Aggregates are not second-class citizens

The Architect separated World Register from World Aggregates. The Carpenter rejects the implication that aggregates require a separate architectural layer.

An aggregate can simply be a World State value.

For example:

`KNOWN_ENEMY_CAVALRY = 4`

may be more useful than four individual unit records if no consumer needs individual identities.

Conversely:

`KNOWN_ENEMY_PRODUCTION_SITE = object X at location Y`

may justify continuity because location and identity have downstream value.

The architecture therefore chooses representation based on **decision value**, not on whether the information happens to describe one object or many.

---

# 7. The World Model is a cache of useful truth — not a database

A database tries to preserve everything that belongs to its domain.

The World Model should do the opposite.

It should preserve only information that earns persistence.

A useful metaphor:

> **The observation workspace is a workbench. The World Model is the few measurements written on the shop wall because everyone keeps needing them.**

The workbench can contain hundreds of temporary pieces while solving a problem.

The wall should contain only information worth keeping visible.

This is a better fit for a constrained rule engine.

---

# 8. The Carpenter attacks provenance

The Architect correctly preserved provenance, but there is a danger of making provenance bureaucratic.

The requirement should be semantic:

> A consumer must be able to distinguish a value's origin when that distinction matters to correctness.

That means provenance is required for:

- contested information;
- state whose interpretation depends on observation method;
- values whose freshness matters;
- values being promoted into consequential decisions;
- values whose source must be audited.

It does **not** mean every temporary arithmetic result needs a provenance dossier.

This preserves auditability without turning every calculation into paperwork.

---

# 9. The Carpenter attacks freshness

Freshness is indispensable, but the architecture must not confuse two questions:

### Question 1
When was this observation obtained?

### Question 2
How long is this information strategically useful?

Those are not necessarily the same.

A building location may remain strategically useful for a long time.

An army count may decay rapidly.

Therefore the eventual architecture should separate:

`OBSERVATION AGE`

from

`INFORMATION RELEVANCE / EXPIRY`.

However, neither should be given a literal representation until the target engine can support it reliably.

For now they remain contract requirements with qualification gates.

---

# 10. The Carpenter attacks identity

Object identity is demonstrably valuable in historical stock behavior, but identity should be used selectively.

Persist identity when:

- an object matters across multiple observations;
- replacement must be distinguished from continuation;
- location/production/infrastructure continuity has strategic value.

Do not persist identity merely because the engine provides an ID.

A unique number is not automatically useful information.

This is exactly the same principle as unused goals: **availability is not justification.**

---

# 11. The Carpenter attacks fan-out

Fan-out is one of the strongest design principles from the Architect, but it can become dangerous if every observation is allowed to influence everything.

Therefore:

> **Fan-out is permitted by contract, not by proximity.**

One World State value may feed multiple consumers only when each consumer has a legitimate semantic relationship to that value.

Example:

`enemy stable observed`

may legitimately feed:

- production-capacity analysis;
- cavalry-threat analysis;
- scouting priority;
- infrastructure opportunity.

But it should not directly set:

- spearman production;
- attack commitment;
- economic policy.

Those consumers must perform their own domain reasoning.

---

# 12. World Model must remain strategically neutral

The Carpenter keeps the strongest Architect boundary:

```text
WORLD STATE
    ↓
SITUATION ANALYSIS
    ↓
STRATEGIC MEANING
```

The World Model says:

> “Three enemy cavalry units are currently known.”

It does not say:

> “This is dangerous.”

Situation Analysis owns the second statement.

This allows the same world fact to support different strategic interpretations as the broader situation changes.

That is high behavioral leverage without coupling the sensor to the strategy.

---

# 13. Capability boundary survives

The Carpenter explicitly preserves:

```text
OBJECT EXISTS
      ≠
OBJECT READY
      ≠
CAPABILITY AVAILABLE
      ≠
CAPABILITY EFFECTIVE
```

This is not unnecessary complexity. It protects AEGIS from one of the most dangerous classes of false reasoning: confusing a physical object with a usable strategic capability.

The World Model may report the observed state.

Capability/Production determines what can actually be done with it.

Execution and Verification establish whether the capability subsequently became effective.

---

# 14. Minimum World State categories

The Carpenter reduces the Architect's candidate domains to six semantic categories:

### 1. ENTITY
Relevant identity/type/ownership information when continuity matters.

### 2. LOCATION
Relevant spatial information when location affects decisions.

### 3. CONDITION
Relevant lifecycle/operational state.

### 4. PRESENCE / CAPACITY
Selected counts or aggregates describing what is currently known to exist or be available as a world fact.

### 5. TRANSITION
A meaningful observed change that must survive the immediate observation.

### 6. PROVENANCE / VALIDITY
Only the metadata necessary to determine whether the world state may safely be consumed.

Everything else begins as temporary observation work.

---

# 15. The new canonical physical model

```text
                         WORLD
                           │
                           ▼
                  ┌─────────────────┐
                  │ OBSERVATION     │
                  │ WORKBENCH       │
                  │                 │
                  │ search          │
                  │ filter          │
                  │ select          │
                  │ read            │
                  │ derive          │
                  └────────┬────────┘
                           │
                  publish only if useful
                           │
                           ▼
                  ┌─────────────────┐
                  │ WORLD STATE     │
                  │                 │
                  │ entity          │
                  │ location        │
                  │ condition       │
                  │ presence/cap.   │
                  │ transition      │
                  │ validity/meta   │
                  └────────┬────────┘
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
             BELIEF              SITUATION
             MODEL                ANALYSIS
```

This replaces the previous three-room World Model architecture.

---

# 16. What this buys us

The reduction has several advantages.

### Less machinery
Fewer conceptual storage structures means fewer ownership questions.

### Better fit for `.per`
Temporary search computation is treated as a first-class mechanism rather than forcing every concept into persistent state.

### Better behavioral leverage
One world fact can be consumed by many specialized systems without duplicating the fact itself.

### Better correctness
Observation, world state, belief, and situation remain distinct.

### Better performance potential
The architecture defaults to computation-on-demand instead of permanent scanning/storage.

### Better adaptability
The representation can change by domain without changing the semantic boundary.

---

# 17. What the Carpenter refuses to simplify

Some things look like complexity but are actually structural safety features.

I will **not** remove:

- observation/world-state separation;
- world-state/belief separation;
- belief/situation separation;
- selective persistence;
- identity when continuity demonstrably matters;
- lifecycle distinction;
- capability realization distinction;
- ownership boundaries;
- evidence levels;
- empirical qualification before implementation.

These are load-bearing beams, not decoration.

---

# 18. What remains explicitly unproven

The Carpenter does not turn architecture into engine fact.

Still open:

- exact current-build freshness mechanics;
- exact timestamp availability;
- exact representation of validity/generation;
- runtime cost of observation work;
- current-build behavior of every historical object-data primitive;
- which proposed World State categories deserve actual persistent storage;
- exact AEGIS goal representation;
- exact mailbox representation;
- runtime realization semantics.

These are qualification problems, not reasons to inflate the architecture.

---

# 19. Carpenter's stress test

The reduced architecture must survive these examples.

### Case A — enemy cavalry visible

Observation workspace finds cavalry.

World State may publish known cavalry presence.

Situation Analysis determines threat significance.

**Pass.**

### Case B — cavalry disappears from observation

World State must not automatically publish zero.

Belief may reason about last-known presence.

**Pass.**

### Case C — building under construction

World State can distinguish observed construction/lifecycle state.

Capability system determines whether it counts as usable production.

**Pass.**

### Case D — same production site observed repeatedly

Identity may justify persistence.

**Pass.**

### Case E — one-time local count

Search, count, consume, discard.

**Pass.**

### Case F — one measurement used by five systems

Publish one world fact; five legitimate consumers read it.

**Pass.**

### Case G — strategic interpretation changes

World fact remains neutral while Situation Analysis changes interpretation.

**Pass.**

### Case H — engine cannot support desired freshness representation

Architecture marks the requirement open rather than inventing machinery.

**Pass.**

---

# 20. Final Carpenter verdict

The Architect built too much furniture.

Most of it was good furniture.

But the building does not need it yet.

The Carpenter therefore reduces the World Model to one physical principle:

> **Observe cheaply and selectively; preserve only valuable world state; keep world facts neutral; let higher systems create meaning.**

The resulting architecture is:

```text
OBSERVATION WORKBENCH
        ↓
   SELECT / DERIVE
        ↓
    WORLD STATE
        ↓
 BELIEF / SITUATION
```

The six semantic categories are sufficient as the current design vocabulary:

`ENTITY / LOCATION / CONDITION / PRESENCE-CAPACITY / TRANSITION / VALIDITY-PROVENANCE`

They are **not** six storage rooms.

They are six kinds of information the eventual World Model may legitimately preserve.

That is substantially smaller than the Architect's proposal while retaining its important behavioral leverage.

---

# 21. Handoff to Adversary

The Carpenter is finished cutting.

The next question is no longer:

> “Can we make this smaller?”

It is:

> **“Can this smaller architecture survive hostile conditions?”**

The next mode should therefore be **ADVERSARY**.

The Adversary should attempt to break the reduced World Model using pathological game states:

- contradictory observations;
- disappearing/reappearing armies;
- changing player focus;
- rapid unit replacement;
- construction and demolition;
- simultaneous transitions;
- stale information;
- multiple consumers racing on the same state;
- failed execution;
- misleading but technically correct observations;
- and the worst case: a perfectly valid World Model that causes a catastrophically bad strategic decision.

**The Carpenter has removed the furniture. Now the Adversary gets to try to collapse the building.**
