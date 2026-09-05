# AEGIS World Model — Architect Pass 1

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** ARCHITECT  
**Status:** PROPOSED ARCHITECTURE — NOT IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`  

## 0. Mission

Turn the Scientist evidence baseline into the smallest useful World Model architecture without inventing engine capabilities.

The design rule is:

> **Represent only decision-relevant world state, preserve provenance and lifecycle, and compute temporary detail when persistence does not earn its cost.**

No `.per` implementation, runtime execution, or new ABI allocation is authorized by this document.

---

# 1. The architectural correction

AEGIS will not build a complete replica of the AoE2DE world.

That would confuse the map with the commander's understanding of the map.

Instead:

`ENGINE WORLD → OBSERVATION → WORLD MODEL → BELIEF → SITUATION`

The World Model is the **current structured picture of relevant observed reality**.

It is not:

- the raw search result;
- the entire engine state;
- a strategic conclusion;
- an opponent hypothesis;
- a command queue;
- a memory archive.

Those boundaries are load-bearing.

---

# 2. The proposed World Model has three physical layers

## Layer A — Observation Workspace

Temporary.

Purpose:
- perform search/filter/select operations;
- inspect objects;
- aggregate counts or measurements;
- answer a specific question.

This inherits the strongest stock pattern: **search is a computational workspace**.

Nothing becomes persistent merely because it was observed.

## Layer B — World Register

Persistent only where continuity or repeated strategic use justifies it.

Contains compact records describing relevant entities or aggregates.

Conceptual record:

`WORLD_RECORD`
- identity, when identity matters;
- owner;
- type/category;
- spatial reference, when strategically useful;
- lifecycle/operational state, when useful;
- observation provenance;
- freshness/lifecycle metadata;
- generation/version where replacement matters.

This is a **decision register**, not an encyclopedia.

## Layer C — World Aggregates

Persistent summaries derived from the World Register or fresh observations.

Examples of categories to investigate:
- military composition;
- production capacity;
- economic object availability;
- map-control-relevant presence;
- infrastructure state;
- capability availability.

Aggregates exist because many strategic decisions do not need individual objects.

---

# 3. The critical distinction: record vs measurement

AEGIS should not persist every measurement.

A useful rule:

> **Persist identity when continuity matters. Persist state when multiple consumers need it or when recomputation is materially expensive. Otherwise calculate it on demand.**

Example:

If a decision only needs:

`How many enemy cavalry units are currently known?`

then a fresh search-derived count may be preferable to maintaining dozens of persistent cavalry records.

But if the architecture needs to remember:

`Which enemy production site was previously observed at this location?`

identity and continuity may justify a persistent record.

This is where AEGIS seeks behavioral leverage without data-model bloat.

---

# 4. Proposed canonical World Record

This is an architectural proposal, not an engine claim.

```text
WORLD_RECORD
├── IDENTITY
│   └── engine object identity when required
├── OWNER
├── KIND
│   ├── concrete type
│   ├── line/class where semantically valid
│   └── AEGIS category only after qualification
├── SPATIAL
│   └── relevant position/distance reference
├── STATE
│   ├── existence / observed presence
│   ├── lifecycle/progress
│   └── operational state where useful
├── PROVENANCE
│   ├── observation source
│   └── observation generation
├── FRESHNESS
│   └── current / stale semantics after qualification
└── REPLACEMENT
    └── generation where identity/state supersession matters
```

Not every record needs every field.

The canonical structure describes the **semantic contract**, not a demand for a literal one-record-per-object data structure in `.per`.

That distinction is deliberate.

---

# 5. Five classes of World Model information

Every proposed field must first be classified.

### A. DIRECT WORLD FACT

Directly observed engine information.

Example category:
`object-data-player`.

### B. DERIVED WORLD FACT

A deterministic transformation of direct observations.

Example:
`known enemy cavalry count` derived from a selected set.

### C. WORLD EVENT / TRANSITION

A change inferred from before/after state or directly observable lifecycle progression.

Example category:
`producer became available`.

### D. BELIEF

Unobserved or uncertain proposition.

Not World Model truth.

### E. STRATEGIC INTERPRETATION

Meaning assigned by Situation Analysis.

Not World Model truth.

The World Model owns A and selected B/C. It does not own D/E.

---

# 6. World Model ownership rule

The World Model owns **descriptions of the world**, not decisions about the world.

Therefore it may answer:

> “What enemy military presence is currently known?”

It does not answer:

> “Should we make spearmen?”

It may expose:

> “Enemy cavalry presence increased.”

It does not own:

> “Cavalry is now the dominant strategic threat.”

That belongs to Situation Analysis.

This boundary prevents the World Model from becoming an omniscient planner disguised as a database.

---

# 7. World Model → Belief boundary

The most important semantic rule is:

> **Absence of observation is not observation of absence.**

If a cavalry unit disappears from a search because it is no longer observable, the World Model cannot automatically declare:

`enemy cavalry = 0`.

Instead, the observed state may become:

`last known presence = cavalry`  
`current observation = unavailable`

and the Belief Model may subsequently reason about what that means.

This prevents fog-of-war uncertainty from being converted into false certainty.

Exact freshness/invalidation mechanics remain subject to empirical qualification.

---

# 8. World Model → Situation boundary

Situation Analysis consumes World Model facts and Beliefs.

Conceptually:

```text
WORLD MODEL
     +
BELIEF MODEL
     +
MAP / HISTORY
     ↓
SITUATION ANALYSIS
     ↓
THREATS / OPPORTUNITIES / FORECAST
```

The same World Model fact may support multiple strategic interpretations.

For example:

`enemy stable observed`

could contribute to:
- cavalry threat;
- enemy production capacity;
- scouting priority;
- opportunity to attack infrastructure;
- technology forecast.

This is precisely the behavioral-leverage principle we want.

One reliable fact should feed several legitimate consumers rather than being duplicated into several specialized “rooms.”

---

# 9. World Model → Capability boundary

A dangerous shortcut is:

`object exists → capability exists`.

The architecture explicitly rejects that.

Instead:

```text
OBSERVED OBJECT
      ↓
LIFECYCLE / READINESS
      ↓
CAPABILITY ASSESSMENT
      ↓
AVAILABLE CAPABILITY
```

The World Model can provide the observed building/unit/lifecycle facts.

The Capability/Production system decides what those facts mean for usable capability.

This preserves the Layer 2 distinction between state representation and realization.

---

# 10. The high-leverage design pattern

The World Model should deliberately favor **fan-out** over duplication.

```text
                 ONE PROVEN OBSERVATION
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       MILITARY        ECONOMY        SCOUTING
          │              │              │
          ▼              ▼              ▼
       THREAT         CAPACITY       ATTENTION
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                      STRATEGY
```

The observation itself remains neutral.

Consumers derive their own domain meaning.

This is preferable to creating:

`CavalryObservationRoom → CavalryThreatRoom → CavalryProductionRoom → CavalryDefenseRoom`.

The latter duplicates state and creates ownership problems.

---

# 11. What should be persistent?

A proposed persistence test:

### Persist if at least one is true:

1. Multiple subsystems consume it.
2. Identity continuity matters.
3. Recomputing it is materially expensive.
4. Its absence would cause dangerous strategic amnesia.
5. It represents a meaningful world transition that must survive the immediate search.

### Do not persist merely because:

- it is easy to store;
- a goal exists;
- stock AI once stored something similar;
- the value sounds strategically interesting.

This is a deliberate anti-bloat rule.

---

# 12. Candidate persistent domains

These are candidates, not allocations.

### ENTITY CONTINUITY
Useful when the same object matters across observations.

### MILITARY PRESENCE
Compact aggregate representation of relevant known forces.

### PRODUCTION PRESENCE
Relevant enemy/own production infrastructure and readiness.

### INFRASTRUCTURE
Strategically relevant construction/completion state.

### RESOURCE OBJECTS
Only where local economic geometry or safety materially matters.

### MAP CONTROL ANCHORS
Strategically important locations/objects rather than a complete map database.

### WORLD TRANSITIONS
Only transitions whose downstream consequences persist beyond the immediate observation.

Everything else should begin as ephemeral observation workspace.

---

# 13. The World Model's interface to the rest of the apartment

```text
                 WORLD MODEL
                      │
       ┌──────────────┼───────────────┐
       │              │               │
       ▼              ▼               ▼
   BELIEF         SITUATION       CAPABILITY
    MODEL          ANALYSIS        SYSTEM
       │              │               │
       └──────────────┼───────────────┘
                      ▼
                  STRATEGIC
                   CONTROL
```

### Inputs
- direct engine observations;
- search-derived measurements;
- qualified world transitions.

### Outputs
- current world facts;
- selected derived world facts;
- relevant lifecycle state;
- provenance/freshness metadata when qualified.

### Forbidden outputs
- strategic decisions;
- commitments;
- commands;
- unsupported beliefs presented as facts.

---

# 14. The World Model should be question-driven

The most important operational design principle is:

> **Observe because a decision requires information, not because the architecture has a place to put information.**

Instead of:

`scan everything → store everything → analyze everything`,

prefer:

`decision-relevant question → targeted observation → compact derived answer → publish if valuable`.

This directly inherits the stock search/filter/select/read/derive/store/decide pattern and gives us a path toward high behavioral leverage with bounded computational cost.

---

# 15. The architecture's current canonical flow

```text
REAL WORLD
   ↓
OBSERVATION REQUEST
   ↓
SEARCH / SENSOR WORKSPACE
   ↓
FILTER / SELECT / READ
   ↓
DIRECT OBSERVATION
   ↓
DERIVE IF NECESSARY
   ↓
PERSIST ONLY IF JUSTIFIED
   ↓
WORLD MODEL
   ↓
BELIEF / SITUATION / CAPABILITY CONSUMERS
```

The World Model is therefore not primarily a storage room.

It is a **selective truth-preservation layer between the game and higher reasoning**.

---

# 16. Architect's deliberate NO list

I reject the following for the current design:

- a complete object database;
- one persistent record for every unit;
- one room per information category;
- strategic threat states inside the World Model;
- opponent hypotheses inside the World Model;
- automatic conversion of missing observation into zero;
- assuming timestamps exist merely because freshness is architecturally desirable;
- stock goal/SN reuse merely because a similar value exists;
- literal implementation of the conceptual record before representation is qualified;
- any design that requires the World Model to know what the AI should do.

---

# 17. Acceptance criteria for the Architect pass

The World Model architecture is acceptable only if:

1. Every persistent category has a demonstrated reason to persist.
2. Observation is distinct from interpretation.
3. World fact is distinct from belief.
4. World fact is distinct from strategic situation.
5. Object existence is distinct from capability availability.
6. Unknown is not silently converted into zero.
7. Search remains a temporary computational workspace where possible.
8. A single observation can serve multiple consumers without duplicated ownership.
9. Identity is preserved only where continuity provides value.
10. Freshness is represented only to the degree the engine can support.
11. No stock control channel is assumed to be AEGIS-owned.
12. No engine capability is invented to satisfy the architecture.
13. The design has a clear route to empirical qualification.
14. The model remains small enough that runtime observation cost can be bounded.
15. A hostile review can identify exactly where a false observation would propagate.

---

# 18. Handoff to Carpenter

The Architect's current conclusion is:

> **The World Model should be a selective truth-preservation layer, not a replica of the game. Its core architectural trick is to keep observations temporary by default, persist only high-value continuity/state, and let one proven observation fan out into multiple specialized consumers without duplicating ownership.**

The next mode should therefore be **CARPENTER**.

The Carpenter must now try to cut this design down.

Specifically, it should ask:

- Are three World Model layers actually necessary?
- Is `WORLD_RECORD` too elaborate for `.per`?
- Which proposed persistent domains can be eliminated?
- Can provenance/freshness/generation be represented without creating a bureaucratic state machine?
- Are any boundaries merely conceptual names for the same machinery?
- Can the entire design be reduced while preserving its leverage?

The Architect has finished adding structure.

**Now the Carpenter gets the saw.**
