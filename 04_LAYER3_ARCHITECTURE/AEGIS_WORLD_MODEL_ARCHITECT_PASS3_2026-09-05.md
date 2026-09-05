# AEGIS World Model — Architect Pass 3

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** ARCHITECT  
**Status:** CROSS-SYSTEM CONTRACT — ARCHITECTURE ONLY  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Mission

Convert Scientist Pass 3 into the minimum load-bearing contract between:

`WORLD STATE → SITUATION → CAPABILITY → COMMITMENT → EXECUTION → VERIFICATION → WORLD STATE`

The design must solve stale-decision failure without inventing a transaction engine, universal freshness database, or new room for every semantic concern.

**No `.per` implementation, runtime execution, or ABI allocation is authorized by this pass.**

---

# 1. Architectural decision

AEGIS does **not** need a transaction subsystem.

It needs a **decision-validity boundary**.

The core rule is:

> A decision is allowed to become a commitment only on the evidence available at decision time; a commitment is allowed to execute only if the assumptions that materially determine execution are still valid.

That yields the minimum control path:

```text
WORLD STATE
    ↓
SITUATION
    ↓
CAPABILITY
    ↓
DECISION
    ↓
COMMITMENT
    ↓
MATERIAL CHANGE?
   /       \
 NO         YES
 |           ↓
 |       REVALIDATE
 |           ↓
 |       STILL VALID?
 |         /      \
 |       YES       NO
 |        |         ↓
 └────→ EXECUTE   REPLAN
              ↓
          VERIFY
              ↓
          WORLD STATE
```

This is a **control rule**, not a new room.

---

# 2. The six boundaries

## Boundary A — World State → Situation

**World State answers:**

> What do we have sufficient evidence to say about the world?

**Situation answers:**

> What does that world state mean right now for the game we are playing?

World State may contain:

- observed objects;
- ownership;
- lifecycle/status;
- spatial facts;
- selected persistent facts;
- qualified aggregates;
- selected transitions.

Situation may contain:

- threat;
- opportunity;
- urgency;
- vulnerability;
- map-control implications;
- tempo implications;
- strategic significance.

**Hard boundary:** Situation may interpret World State; it may not rewrite World State merely because its interpretation is convenient.

Example:

```text
WORLD STATE: enemy stable observed
SITUATION: cavalry production risk elevated
```

The second statement must never be stored as though the first observation itself were a threat fact.

---

# 3. Boundary B — Situation → Capability

Capability answers:

> What can AEGIS actually produce, field, sustain, or execute under current conditions?

Capability is not a synonym for resources and not a synonym for object existence.

Minimum conceptual composition:

```text
WORLD STATE
+ TECHNOLOGY
+ INFRASTRUCTURE
+ PRODUCTION CAPACITY
+ RESOURCES
+ TIME
        ↓
CAPABILITY
```

Examples:

```text
stable exists
    ≠
stable can currently train cavalry
```

```text
300 food exists
    ≠
30 knights can be produced now
```

```text
10 spearmen exist
    ≠
10 spearmen are available at the threatened location
```

Capability must therefore include the distinction between:

- theoretically possible;
- currently feasible;
- operationally available;
- strategically effective.

The architecture does not require four permanent databases. These are semantic questions applied when needed.

---

# 4. Boundary C — Capability → Commitment

This is the first major control gate.

A **candidate** is not a commitment.

A **decision** is not a commitment.

A **commitment** means AEGIS has accepted responsibility for pursuing an outcome and is prepared to consume scarce resources, attention, production capacity, time, or opportunity cost.

Therefore:

```text
CAPABILITY
   ↓
CANDIDATE OPTIONS
   ↓
ARBITRATION
   ↓
DECISION
   ↓
COMMITMENT
```

The commitment must preserve the assumptions that materially justify it.

Conceptually:

```text
COMMITMENT
├── OBJECTIVE
├── REQUIRED CAPABILITY
├── MATERIAL ASSUMPTIONS
├── RESOURCE / CAPACITY COST
├── EXECUTION OWNER
├── SUCCESS CONDITION
├── FAILURE CONDITION
└── REVALIDATION CONDITION
```

This is a **semantic contract**, not a proposed literal universal record schema.

The critical field is `MATERIAL ASSUMPTIONS`.

Without it, revalidation has no target.

---

# 5. Boundary D — Commitment → Execution

Execution must not blindly trust the strategic layer.

Before execution of a materially consequential commitment:

```text
ARE MATERIAL ASSUMPTIONS STILL TRUE?
```

If no material change has occurred, execution may proceed without expensive re-analysis.

If material change has occurred, revalidation is required.

Material change examples:

- target disappeared or changed state;
- required producer is unavailable;
- required technology is no longer available/appropriate;
- required resource allocation was consumed;
- opponent composition changed materially;
- threat severity crossed a decision threshold;
- map access changed;
- a previous execution attempt altered the world;
- a higher-priority emergency invalidated the commitment.

This is intentionally threshold-based rather than continuously transactional.

---

# 6. Boundary E — Execution → Verification

Execution produces **intent and engine-directed action**.

Verification establishes whether the intended transition actually occurred.

Therefore:

```text
COMMAND
  ≠
SUCCESS
  ≠
OBJECTIVE ACHIEVED
```

Minimum verification questions:

1. Did the intended action become accepted/observable?
2. Did the relevant world state change?
3. Did the required capability become available?
4. Did the objective move toward its success condition?

Not every action requires identical verification depth.

Verification profiles remain:

- **LIGHT** — cheap, routine, low consequence;
- **NORMAL** — material state change;
- **CRITICAL** — strategic commitment or high-cost failure.

The Verification layer owns verification policy. World State owns the resulting world evidence.

---

# 7. Boundary F — Verification → World State

Verification is an **evidence producer**.

It does not become the owner of world truth.

The resulting observation returns through the normal publication path:

```text
EXECUTION
   ↓
VERIFICATION
   ↓
OBSERVATION / RESULT
   ↓
QUALIFY
   ↓
WORLD STATE
```

This prevents a common feedback-loop error:

```text
EXECUTION says it succeeded
        ↓
WORLD STATE assumes success
        ↓
SITUATION assumes success
        ↓
NEXT PLAN assumes success
```

The architecture instead requires evidence to close the loop.

---

# 8. World State currentness

The Carpenter and Adversary passes correctly rejected a universal freshness engine.

The architecture retains only the semantic distinction required to prevent false certainty:

```text
CURRENT
LAST-KNOWN
UNKNOWN
UNRESOLVED / CONTRADICTED
```

These are **qualifications**, not physical rooms or mandatory fields on every fact.

Rules:

- a current observation may replace an older fact when it is sufficiently qualified;
- lack of observation does not automatically create destruction;
- last-known information may remain useful without masquerading as current;
- unresolved information must not be silently converted into certainty;
- an estimate belongs to Belief, not World State.

---

# 9. Supersession without a transaction system

AEGIS needs the semantic concept of supersession but not a generic transaction manager.

Minimum publication rule:

```text
NEW EVIDENCE
    ↓
COMPARE WITH EXISTING PUBLISHED FACT
    ↓
IS IT QUALIFIED TO REPLACE IT?
   /             \
 YES             NO
 ↓                ↓
SUPERSEDE      RETAIN / UNRESOLVE
```

The engine representation of this rule remains an empirical qualification problem.

The architecture therefore says **what must be true**, not **which goal/SN encoding must implement it**.

Universal generation counters, atomic records, and database-style transactions remain unapproved.

---

# 10. Capability invalidation

Capability is particularly dangerous because it can become obsolete while still looking internally coherent.

Example:

```text
WORLD STATE
stable complete
        ↓
CAPABILITY
stable can produce knights
        ↓
COMMITMENT
train knights
        ↓
stable destroyed
        ↓
CAPABILITY IS OBSOLETE
```

The commitment must therefore depend on **material capability assumptions**, not merely the historical capability assessment that created it.

Architectural rule:

> A capability assessment has no permanent authority over execution.

At a consequential execution boundary, capability is re-derived or revalidated when material state may have changed.

---

# 11. Resource and capability disagreement

The architecture must tolerate temporary disagreement among:

```text
RESOURCE VIEW
CAPABILITY VIEW
WORLD STATE
EXECUTION STATE
```

These systems have different clocks and different evidence sources.

Example:

```text
RESOURCE VIEW: enough wood
CAPABILITY VIEW: barracks affordable
WORLD STATE: builder unavailable
EXECUTION: build request cannot proceed
```

The correct response is not to force one subsystem to overwrite another.

Instead:

```text
execution evidence
      ↓
world-state update
      ↓
capability recomputation
      ↓
commitment repair/replan
```

The architecture therefore treats disagreement as a signal for reconciliation, not as permission for arbitrary writer precedence.

---

# 12. Scheduler interaction

Scheduler and Attention remain cross-cutting systems.

They do not own the meaning of World State or Commitment. They determine when the system can afford to inspect, reconsider, and verify.

Minimum scheduling classes:

### Fast loop

- immediate safety;
- active combat;
- execution blockers;
- critical verification.

### Medium loop

- economy rebalance;
- production pressure;
- scouting refresh;
- opponent evidence updates.

### Slow loop

- strategic posture;
- technology direction;
- long-horizon composition;
- map-control policy.

### Event-driven loop

- age transition;
- enemy technology/composition transition;
- attack contact;
- construction completion/destruction;
- major execution failure;
- strategic commitment invalidation.

Scheduler starvation is therefore a correctness failure when it delays evidence required to invalidate a dangerous commitment.

---

# 13. Preventing feedback loops

The principal feedback loop is legitimate:

```text
WORLD → REASON → COMMIT → EXECUTE → VERIFY → WORLD
```

The pathological loop is:

```text
WORLD
 ↓
BELIEF
 ↓
SITUATION
 ↓
COMMITMENT
 ↓
EXECUTION
 ↓
SELF-GENERATED CLAIM OF SUCCESS
 ↓
WORLD
```

AEGIS must never allow intent to become evidence merely because the intent was issued.

Second pathological loop:

```text
FAILED COMMITMENT
 ↓
RETRY SAME COMMITMENT
 ↓
FAIL
 ↓
RETRY
```

Therefore failed commitments must trigger one of:

- repair;
- changed assumptions;
- changed candidate;
- abandonment;
- escalation to higher-level reassessment.

Recovery owns this policy; World State only supplies evidence.

---

# 14. Ownership rule

One semantic fact must have one authoritative publisher at the architecture level.

Consumers may derive interpretations but must not silently become competing publishers of the same world fact.

Therefore:

```text
WORLD STATE
  authoritative world fact

SITUATION
  interpretation

CAPABILITY
  feasibility interpretation

COMMITMENT
  accepted intent

EXECUTION
  engine-directed action

VERIFICATION
  evidence about result
```

This is the minimum ownership model.

It avoids the stock-style failure mode in which a heavily multiplexed goal becomes an accidental shared truth channel with unrelated writers.

It also avoids requiring a universal message-bus implementation at this architectural stage.

---

# 15. Generation: keep the concept, defer the representation

The Adversary exposed a real stale-generation problem, but the Scientist found no evidence sufficient to mandate a universal generation primitive.

Therefore AEGIS adopts:

> A commitment must be distinguishable from the evidence state that justified it.

But it does **not** yet adopt:

```text
GENERATION = one universal numeric field everywhere
```

Generation becomes a representation requirement only for a specific state channel when empirical ABI qualification demonstrates that it can be represented safely.

This preserves the semantic protection without prematurely spending ABI space.

---

# 16. Minimal cross-system contracts

## World State publishes

- qualified world facts;
- selected persistent transitions;
- current/last-known/unresolved meaning where materially necessary.

## Situation consumes

- world facts;
- map context;
- opponent evidence;
- history where relevant.

It publishes:

- threats;
- opportunities;
- urgency;
- strategic significance.

## Capability consumes

- world state;
- technology;
- infrastructure;
- production capacity;
- resources;
- time.

It publishes:

- feasible/available/effective capability assessments.

## Commitment consumes

- situation;
- capability;
- objectives;
- constraints;
- risk posture;
- strategic priorities.

It publishes:

- accepted objective pursuit;
- material assumptions;
- execution responsibility;
- verification requirements;
- revalidation conditions.

## Execution consumes

- authorized commitment;
- currently valid capability;
- execution policy.

It publishes:

- engine-directed action;
- execution outcome evidence where available.

## Verification consumes

- expected transition;
- success/failure criteria;
- world observations.

It publishes:

- qualified result evidence;
- deviation/failure signal.

## Recovery consumes

- failed/deviating commitments;
- current world state;
- situation changes.

It publishes:

- repair;
- abandonment;
- replanning trigger;
- escalation.

---

# 17. What is deliberately NOT in this contract

The following are rejected as premature architecture:

- transaction manager;
- universal world database;
- universal freshness manager;
- universal timestamp field;
- universal confidence field;
- universal generation field;
- universal event bus;
- universal contradiction database;
- one manager per unit;
- automatic destruction inference from missing search results;
- automatic success inference from command issuance;
- automatic total-force inference from partial observation;
- strategic threat/opponent hypotheses stored as World State;
- ABI allocations;
- runtime implementation.

The architecture is intentionally refusing infrastructure whose behavioral return has not yet been demonstrated.

---

# 18. The physical apartment remains small

After the full World Model review, the required physical rooms are still:

```text
                    STRATEGIC CONTROL
                           │
              ┌────────────┴────────────┐
              │                         │
         WORLD STATE                BELIEF
              │                         │
              └──────────┬──────────────┘
                         ↓
                    SITUATION
                         ↓
                    OBJECTIVES
                         ↓
                    PLANNING
                         ↓
                    DECISION
                         ↓
                   COMMITMENT
                         ↓
             ┌───────────┴───────────┐
             ↓                       ↓
       ECONOMIC EXECUTION      MILITARY EXECUTION
             │                       │
             └───────────┬───────────┘
                         ↓
                    VERIFICATION
                         ↓
                      RECOVERY
                         ↓
                    WORLD STATE
```

Cross-cutting:

```text
SCHEDULER
ATTENTION
OWNERSHIP
EVIDENCE
CURRENTNESS
SUPERSESSION
CLOCKS
RESOURCE LEDGER
MAP
DOCTRINE
RISK
STATE INTEGRITY
MEMORY
```

These remain controls, not automatically separate rooms.

---

# 19. End-to-end pathological example

Enemy cavalry is observed.

```text
WORLD STATE
enemy stable observed
```

Situation interprets it:

```text
SITUATION
cavalry-production risk elevated
```

Capability evaluates:

```text
CAPABILITY
spears feasible
```

Decision/arbitration chooses:

```text
DECISION
produce defensive spearmen
```

Commitment records the material assumptions:

```text
COMMITMENT
objective = contain cavalry
assumption = barracks available
assumption = food/wood allocation remains valid
assumption = threat remains materially relevant
```

Before execution, the scheduler detects material change:

```text
enemy cavalry count changed materially
```

Revalidation occurs.

If still valid:

```text
EXECUTE
```

If no longer valid:

```text
REPLAN
```

After execution:

```text
VERIFY
```

Then:

```text
WORLD STATE
barracks/units/queue state observed
```

This closes the loop without pretending that any stage has perfect knowledge.

---

# 20. Acceptance criteria for the cross-system contract

The architecture is accepted only if all are true:

1. World State cannot be overwritten by strategic interpretation.
2. Situation cannot masquerade as observation.
3. Capability cannot masquerade as world fact.
4. Decision cannot masquerade as commitment.
5. Commitment cannot masquerade as execution success.
6. Execution cannot self-certify strategic success.
7. Verification feeds evidence back through World State.
8. Material capability changes can invalidate execution.
9. Material assumption changes can force revalidation.
10. Non-material changes do not force continuous expensive replanning.
11. Missing observation does not imply destruction.
12. Partial observation does not imply complete census.
13. Last-known information cannot silently become current truth.
14. Contradiction can remain unresolved rather than being forced into certainty.
15. Failed commitments cannot retry forever without changed conditions.
16. Scheduler priority can surface critical invalidation work.
17. No subsystem requires a universal transaction primitive.
18. No universal timestamp/generation/confidence system is required at architecture level.
19. Each semantic fact has an authoritative publisher.
20. Implementation remains separable from semantic contract.
21. ABI allocation remains a later qualification task.
22. Runtime validation remains a later scientific task.

---

# 21. Final architectural verdict

**WORLD MODEL CROSS-SYSTEM CONTRACT: ARCHITECTURALLY ACCEPTABLE.**

The minimum useful architecture is not a database and not a transaction engine.

It is a controlled evidence loop:

```text
OBSERVE
  ↓
QUALIFY
  ↓
PUBLISH WORLD STATE
  ↓
INTERPRET
  ↓
ASSESS CAPABILITY
  ↓
DECIDE
  ↓
COMMIT
  ↓
REVALIDATE WHEN MATERIAL
  ↓
EXECUTE
  ↓
VERIFY
  ↓
PUBLISH RESULTING EVIDENCE
  ↓
RECOVER / REPLAN
  ↓
REASSESS
```

The key architectural insight is:

> **AEGIS does not need to make every state perfectly fresh. It needs to know when stale state is dangerous enough that execution must stop and the decision must be reconsidered.**

That is the highest behavioral return from the Scientist evidence with the least added machinery.

---

# 22. Evidence classification

### PROVEN / DOCUMENTED

- AoE2DE exposes search/filter/object-data surfaces.
- Object state, ownership, lifecycle/status, and type-level data are distinct engine concepts.
- Search operations have meaningful runtime cost.
- Commands and object observations are distinct primitives.
- Engine behavior has changed across builds and requires build-specific qualification.

### OBSERVED / COMPOSED

- Stock AI uses temporary search/workspace state and downstream object measurements.
- World observations can support multiple downstream strategic consumers.
- Execution outcomes require observation/verification rather than assumption.

### INFERRED

- Revalidation at materially consequential boundaries is the minimum practical stale-state defense.
- Capability should be treated as a derived assessment rather than permanent truth.

### PROPOSED

- six-boundary cross-system contract;
- material-assumption commitment model;
- selective supersession;
- verification profiles;
- one authoritative publisher per semantic fact;
- semantic currentness categories;
- scheduler-driven revalidation.

### OPEN

- exact machine representation of commitment assumptions;
- safe generation representation;
- atomicity of multi-field publication;
- exact runtime cost of proposed implementation patterns;
- build-specific ABI encoding for all future state channels.

### REJECTED

- transaction engine as a prerequisite;
- universal state metadata bureaucracy;
- command-as-success;
- absence-as-destruction;
- partial-observation-as-total;
- strategic interpretation stored as world fact.

---

# 23. Handoff to Carpenter

**NEXT MODE: 🔨 CARPENTER**

The Carpenter must now try to destroy this contract by asking:

1. Can `MATERIAL ASSUMPTIONS` be eliminated or simplified?
2. Are all six boundaries genuinely necessary?
3. Can verification profiles be reduced further?
4. Does revalidation create hidden duplicate planning?
5. Is Commitment actually a room, or merely a state transition in Decision?
6. Can Recovery remain outside this contract without creating an ownership gap?
7. Does one-authoritative-publisher work in a `.per` environment with multiplexed primitive channels?
8. Are current/last-known/unresolved semantics still earning their complexity?
9. Can the entire contract be reduced without losing the protection against stale execution?
10. What is the smallest architecture that survives all previous adversarial failures?

The next pass must simplify **without returning to unsafe ambiguity**.
