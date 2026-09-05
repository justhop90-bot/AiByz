# AEGIS World Model — Carpenter Pass 3

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** CARPENTER  
**Status:** SIMPLIFICATION / CONTRACT REVIEW — NO IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Mission

Attack Architect Pass 3 and remove anything that does not earn its complexity.

The target is the smallest architecture that still survives the previously demonstrated failures:

- stale information reaching execution;
- capability becoming obsolete;
- command being mistaken for success;
- partial observation being mistaken for complete knowledge;
- missing search being mistaken for destruction;
- strategic interpretation contaminating world truth;
- failed commitments retrying forever;
- competing writers corrupting semantic ownership;
- scheduler starvation delaying critical invalidation.

**No `.per` implementation, runtime execution, or ABI allocation is authorized.**

---

# 1. Carpenter verdict

**PASS — with substantial compression.**

Architect Pass 3 is sound, but it contains several concepts that are useful as rules and do not deserve to become additional machinery.

The final physical model should be:

```text
OBSERVE / QUALIFY
        ↓
WORLD STATE
        ↓
SITUATION
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

There is no need for a separate physical room for:

- Commitment;
- Revalidation;
- Supersession;
- Currentness;
- Provenance;
- Contradiction;
- Recovery;
- Verification profiles.

These are **rules governing the rooms**, not rooms themselves.

---

# 2. First cut: Commitment is not a room

Architect Pass 3 treated Commitment as a distinct conceptual stage. That distinction is semantically useful but physically unnecessary.

The smaller model is:

```text
DECISION
  ↓
COMMIT
  ↓
EXECUTION
```

Commitment is simply the point at which a selected decision becomes an accepted obligation with consequences.

The distinction must remain in the contract because:

```text
candidate ≠ decision ≠ commitment ≠ command
```

But it does not require a standalone subsystem.

### Keep

A committed decision must identify, where material:

- objective;
- required capability;
- assumptions that could invalidate it;
- owner/executor;
- success/failure condition.

### Remove

Do not build a universal commitment database or commitment manager merely to represent these semantics.

**Carpenter decision: COMMITMENT REMAINS A STATE TRANSITION INSIDE DECISION, NOT A ROOM.**

---

# 3. Second cut: Revalidation is a gate, not a subsystem

The strongest result from the adversarial passes was the stale-decision problem.

The tempting overreaction is a global transaction/freshness system.

Reject it.

Use one rule:

```text
BEFORE CONSEQUENTIAL EXECUTION
        ↓
DID A MATERIAL ASSUMPTION CHANGE?
      /       \
    NO         YES
    ↓           ↓
 EXECUTE    REVALIDATE
                ↓
           STILL VALID?
             /    \
           YES     NO
            ↓       ↓
         EXECUTE  REPLAN
```

This rule is enough to defend the architecture without creating another control plane.

Revalidation can occur at the execution boundary or earlier when the Scheduler detects a material event.

**Carpenter decision: REVALIDATION IS A GATE.**

---

# 4. Third cut: Supersession is publication logic

There is no need for a Supersession Manager.

World State simply obeys:

```text
NEW EVIDENCE
    ↓
QUALIFY
    ↓
REPLACE / RETAIN / UNRESOLVE
```

The representation used later may require generation, sequence, timer, or another mechanism, but that is an ABI question.

Architectural semantics are enough now.

**Carpenter decision: SUPERSESSION IS A WORLD-STATE PUBLICATION RULE.**

---

# 5. Fourth cut: Provenance is conditional

Provenance is useful when two pieces of evidence compete or when a consumer must know why a fact exists.

It is not useful as mandatory bureaucracy on every scalar.

Therefore:

```text
PROVENANCE REQUIRED
when evidence source materially affects interpretation,
supersession, conflict resolution, or verification.
```

Otherwise, do not spend representation on it.

This preserves the Scientist's evidence discipline without creating a metadata system.

**Carpenter decision: PROVENANCE IS ON-DEMAND SEMANTICS.**

---

# 6. Fifth cut: Current / Last-Known / Unknown / Contradicted

These distinctions survived the Adversary for good reason, but their representation can be compressed.

Do not create four stores.

The minimum rule is:

```text
VALUE
+ QUALIFICATION WHEN MATERIAL
```

The qualification answers:

```text
CURRENT?
LAST-KNOWN?
UNRESOLVED?
```

`UNKNOWN` can normally be represented by the absence of a sufficiently qualified value rather than by a dedicated global state object.

`CONTRADICTED` should only exist when two materially relevant pieces of evidence cannot safely be reconciled.

Thus the practical hierarchy becomes:

```text
QUALIFIED VALUE
      ↓
current when supported
last-known when no longer current
unresolved when conflicting
absent when unknown
```

This preserves the semantic protection while eliminating a universal state machine.

**Carpenter decision: KEEP THE SEMANTICS; REMOVE THE MACHINERY.**

---

# 7. Sixth cut: Verification profiles

The Architect retained LIGHT / NORMAL / CRITICAL verification profiles.

Keep the concept, but do not make it a formal framework yet.

The real rule is simply:

> Verification depth should scale with consequence and cost of failure.

Examples:

```text
routine low-cost action → cheap verification
material production/build → normal verification
strategic/high-cost commitment → strong verification
```

No profile registry is needed in architecture.

**Carpenter decision: VERIFICATION DEPTH IS POLICY, NOT INFRASTRUCTURE.**

---

# 8. Seventh cut: Recovery

Recovery is important but does not need to sit inside the World Model contract.

Its minimum obligation is:

```text
FAILED / DEVIATING COMMITMENT
        ↓
CHANGE SOMETHING
```

That means one of:

- repair;
- alter assumptions;
- select another candidate;
- abandon;
- escalate/reassess.

The World Model supplies evidence. Recovery owns the response.

A failed commitment must never simply re-enter execution unchanged forever.

**Carpenter decision: RECOVERY REMAINS A CROSS-CUTTING CONTROL, NOT WORLD-STATE MACHINERY.**

---

# 9. The real load-bearing boundary

After all cuts, one boundary remains absolutely non-negotiable:

```text
WORLD FACT
      ↓
INTERPRETATION
      ↓
DECISION
      ↓
ACTION
      ↓
EVIDENCE
```

The system fails if these categories collapse.

Specifically:

```text
OBSERVATION ≠ BELIEF
BELIEF ≠ SITUATION
SITUATION ≠ CAPABILITY
CAPABILITY ≠ DECISION
DECISION ≠ COMMAND
COMMAND ≠ SUCCESS
SUCCESS CLAIM ≠ VERIFIED WORLD FACT
```

This is more important than any particular data structure.

---

# 10. The minimum World Model contract

The World Model needs only two physical responsibilities:

### A. Observation Workbench

```text
SEARCH
FILTER
SELECT
READ
MEASURE
DERIVE
QUALIFY
```

### B. World State

Persist only information that earns persistence.

A fact earns persistence when at least one is true:

1. multiple important consumers need it;
2. identity continuity matters;
3. recomputation is materially expensive;
4. forgetting it creates dangerous strategic amnesia;
5. it represents a meaningful transition that must survive the immediate observation cycle.

Everything else can remain transient.

---

# 11. The minimum Decision contract

Decision does four things:

```text
OBJECTIVE
   ↓
OPTIONS
   ↓
ARBITRATION
   ↓
SELECT
```

If selected, it becomes a commitment.

The decision retains only the assumptions necessary to know whether execution remains justified.

This means the old separate:

- Objective Room;
- Requirement Room;
- Constraint Room;
- Capability Room;
- Candidate Room;
- Arbitration Room;
- Commitment Room;

can remain useful as **logical stages**, but they should not automatically become seven physical rooms.

The apartment should have one **Planning / Decision** area with internal stages.

This is the same conceptual decompression principle applied correctly: explicit reasoning without unnecessary physical fragmentation.

---

# 12. Capability should remain separate

Capability cannot be collapsed into Decision because it answers a different question:

> Can we actually do this?

Decision asks:

> Should we do this?

That separation earns its cost because the same capability assessment can serve multiple decisions.

Minimum capability inputs:

```text
WORLD STATE
TECHNOLOGY
INFRASTRUCTURE
PRODUCTION CAPACITY
RESOURCES
TIME
```

Minimum outputs:

```text
FEASIBLE
AVAILABLE
EFFECTIVE
```

These remain semantic categories, not mandatory database fields.

---

# 13. Situation should remain separate

Situation earns its room because it converts facts into strategic significance.

World State:

```text
enemy stable observed
```

Situation:

```text
cavalry-production risk elevated
```

That separation prevents strategic interpretation from contaminating world truth.

Threat, opportunity, urgency, vulnerability, map control, and tempo remain **outputs of Situation Analysis**, not World State records.

---

# 14. World State should not know about decisions

This is a critical carpenter cut.

World State should never contain:

```text
enemy stable = therefore build spearmen
```

Nor:

```text
stable observed = cavalry threat = priority 90
```

Those are downstream interpretations.

World State may contain the observed stable and other supporting facts.

Situation determines significance.

Decision determines response.

This one-way semantic flow prevents circular contamination.

---

# 15. One publisher, many consumers

The ownership rule survives.

But it can be expressed simply:

> **One semantic fact has one authoritative publisher; many systems may consume it.**

This is stronger and simpler than a general message-bus architecture.

Example:

```text
WORLD STATE
enemy stable observed
       │
       ├── Situation
       ├── Scouting
       ├── Attention
       ├── Opponent Model
       └── Capability
```

Each consumer can derive its own interpretation without claiming ownership of the underlying world fact.

---

# 16. Scheduler remains load-bearing

The Carpenter does **not** cut Scheduler.

This is one of the few structures whose behavioral return is already obvious from the engine evidence.

Search/filter operations can be expensive. Critical state can change while the bot is executing another plan.

Therefore Scheduler decides:

```text
WHAT TO OBSERVE
WHEN TO OBSERVE IT
WHEN TO REASSESS
WHEN TO VERIFY
```

The Scheduler does not decide what observations mean.

It controls computational attention and timing.

This is a clean separation:

```text
SCHEDULER → WHEN
WORLD MODEL → WHAT IS OBSERVED
SITUATION → WHAT IT MEANS
DECISION → WHAT TO DO
```

---

# 17. The smallest safe feedback loop

After compression:

```text
┌───────────────┐
│    WORLD      │
│    STATE      │
└───────┬───────┘
        ↓
┌───────────────┐
│   SITUATION   │
└───────┬───────┘
        ↓
┌───────────────┐
│  CAPABILITY   │
└───────┬───────┘
        ↓
┌───────────────┐
│ DECISION/COMMIT│
└───────┬───────┘
        ↓
┌───────────────┐
│   EXECUTION   │
└───────┬───────┘
        ↓
┌───────────────┐
│ VERIFICATION  │
└───────┬───────┘
        ↓
┌───────────────┐
│    WORLD      │
│    STATE      │
└───────────────┘
```

Cross-cutting:

```text
SCHEDULER
ATTENTION
OWNERSHIP
EVIDENCE
REVALIDATION
RECOVERY
RESOURCE LEDGER
MAP
DOCTRINE
RISK
MEMORY
STATE INTEGRITY
```

No transaction engine.

No universal freshness engine.

No universal event bus.

No universal object database.

---

# 18. Adversarial retest after compression

## Failure: enemy disappears

World State retains last-known/unknown semantics. No destruction inference.

**SURVIVES.**

## Failure: enemy changes composition before execution

Scheduler or execution boundary triggers material revalidation.

**SURVIVES.**

## Failure: producer is destroyed

Capability becomes invalid; commitment revalidates.

**SURVIVES.**

## Failure: command fails

Verification observes the resulting state rather than trusting issuance.

**SURVIVES.**

## Failure: partial census

World State preserves observation scope; Situation cannot silently promote subset to total.

**SURVIVES.**

## Failure: two systems disagree

One owns the underlying world fact; consumers own their interpretations.

**SURVIVES.**

## Failure: stale retry

Recovery must alter, abandon, or escalate failed commitments.

**SURVIVES.**

## Failure: expensive polling

Scheduler controls observation cadence.

**SURVIVES.**

## Failure: architecture becomes bureaucracy

No universal metadata or transaction subsystem exists.

**SURVIVES.**

---

# 19. What the Carpenter removed

The following are explicitly **not physical architecture**:

- Commitment Room;
- Revalidation Manager;
- Supersession Manager;
- Freshness Manager;
- Provenance Manager;
- Contradiction Manager;
- Verification Profile Registry;
- Recovery Engine inside World State;
- universal generation subsystem;
- universal timestamp subsystem;
- universal confidence subsystem;
- world-event bus;
- object database;
- one record per unit;
- one manager per semantic qualifier.

They may return only if later empirical evidence demonstrates that a concrete failure cannot be solved without them.

---

# 20. Final physical floor plan

```text
                         STRATEGIC CONTROL
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
       WORLD / OBSERVATION                    BELIEF / HISTORY
              │                                   │
              └────────────────┬──────────────────┘
                               ↓
                         SITUATION ANALYSIS
                               ↓
                          PLANNING / DECISION
                               ↓
                         CAPABILITY CHECK
                               ↓
                          DECIDE / COMMIT
                               ↓
                  ┌────────────┴────────────┐
                  ↓                         ↓
          ECONOMIC EXECUTION        MILITARY EXECUTION
                  │                         │
                  └────────────┬────────────┘
                               ↓
                           VERIFICATION
                               ↓
                            RECOVERY
                               ↓
                           WORLD STATE
```

Cross-cutting controls:

```text
SCHEDULER
ATTENTION
OWNERSHIP
EVIDENCE
REVALIDATION
RESOURCE LEDGER
MAP
DOCTRINE
RISK
MEMORY
STATE INTEGRITY
```

The exact physical split between Belief/History, Situation, Planning, Economy, Military, and other operational rooms remains subject to the broader apartment review. This pass only establishes what the World Model contract requires.

---

# 21. Behavioral return test

Every surviving concept must answer:

```text
WHAT FAILURE DOES IT PREVENT?
OR
WHAT IMPORTANT BEHAVIOR DOES IT ENABLE?
```

| Concept | Return | Decision |
|---|---|---|
| Observation Workbench | enables engine observation | KEEP |
| World State | prevents strategic amnesia | KEEP |
| Situation | converts facts into significance | KEEP |
| Capability | prevents impossible plans | KEEP |
| Decision | selects among competing actions | KEEP |
| Commitment semantics | prevents silent plan drift | KEEP AS STATE |
| Revalidation | prevents stale execution | KEEP AS GATE |
| Verification | prevents command=success | KEEP |
| Scheduler | controls expensive observation/reassessment | KEEP |
| Provenance | conflict/evidence support when needed | CONDITIONAL |
| Supersession | prevents stale overwrite | KEEP AS RULE |
| Universal freshness | not yet justified | CUT |
| Universal generation | not yet justified | CUT |
| Universal confidence | not yet justified | CUT |
| Transaction engine | unnecessary at architecture stage | CUT |
| Universal event bus | unnecessary | CUT |
| Object database | excessive | CUT |

---

# 22. Carpenter acceptance criteria

The compressed architecture passes only if:

1. It still distinguishes world facts from interpretations.
2. It still distinguishes capability from decision.
3. It still distinguishes decision from commitment.
4. It still distinguishes command from verified result.
5. It can invalidate materially stale execution.
6. It does not require universal freshness machinery.
7. It does not require universal generation machinery.
8. It does not infer destruction from missing search.
9. It does not infer totals from partial observations.
10. It prevents strategic consumers from becoming world-fact publishers.
11. It prevents failed commitments from infinite unchanged retries.
12. It gives Scheduler authority over computational attention.
13. It keeps World State selective rather than encyclopedic.
14. It allows provenance where materially useful without making it universal.
15. It preserves supersession semantics without a transaction system.
16. It remains implementable in the constrained `.per` environment in principle.
17. It leaves actual representation and ABI qualification to later Scientist work.
18. It adds no runtime implementation during architecture.

**Result: PASS.**

---

# 23. Final Carpenter conclusion

The previous Architect design was not wrong. It was simply beginning to turn useful semantic distinctions into infrastructure.

The carpenter's job is to stop that before the building becomes larger than the problem.

The final principle is:

> **Keep distinctions that prevent failure. Remove machinery that merely records those distinctions.**

For the World Model, the minimum safe design is therefore:

```text
OBSERVE
  ↓
QUALIFY
  ↓
WORLD STATE
  ↓
INTERPRET
  ↓
ASSESS CAPABILITY
  ↓
DECIDE / COMMIT
  ↓
REVALIDATE WHEN MATERIAL
  ↓
EXECUTE
  ↓
VERIFY
  ↓
UPDATE WORLD STATE
```

This is the smallest design that has survived the Scientist, Architect, and Adversary passes without giving the Carpenter an excuse to rebuild it as a database.

**CARPENTER VERDICT: PASS.**

## Next mode

**⚔️ ADVERSARY**

The next pass should attack the compressed floor plan under full-system conditions rather than another World-Model-only review.

Specifically:

- Dark Age opening;
- economic allocation;
- first scouting divergence;
- enemy cavalry transition;
- production bottleneck;
- military commitment;
- failed attack;
- recovery;
- Castle transition;
- opponent reversal;
- map-control conflict;
- late-game resource exhaustion.

The question is no longer merely whether World Model survives.

The question becomes:

> **Can the entire apartment remain coherent when multiple rooms simultaneously believe they need different things?**
