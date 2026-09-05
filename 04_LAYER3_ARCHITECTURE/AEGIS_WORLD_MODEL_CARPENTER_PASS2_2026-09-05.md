# AEGIS World Model — Carpenter Pass 2

**Date:** 2026-09-05  
**Layer:** 3A — Architecture  
**Mode:** CARPENTER  
**Status:** Simplification review — not implementation  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Mission

Attack Architect Pass 2 with one rule:

> If a concept does not earn its existence through a concrete failure it prevents or a concrete behavioral return it creates, remove it.

No `.per` implementation, runtime execution, or ABI allocation is authorized by this pass.

---

# 1. Carpenter verdict

The World Model can be simplified again.

The previous architecture is correct, but several semantic concepts were in danger of becoming implementation furniture.

The final physical shape should remain only:

```text
OBSERVE
  ↓
QUALIFY
  ↓
PUBLISH USEFUL WORLD FACT
```

Everything else is a rule governing that pipeline, not another subsystem.

The Carpenter therefore rejects adding:

- a dedicated publication service;
- a dedicated supersession service;
- a dedicated provenance subsystem;
- a dedicated freshness subsystem;
- a dedicated identity subsystem;
- a dedicated aggregate subsystem.

Those concerns remain local rules of World State publication.

---

# 2. First cut — remove semantic furniture

The Architect described:

```text
VALUE
KIND
STATUS
SOURCE / PROVENANCE
```

This is useful as a review vocabulary, but it should not automatically become a four-field universal data structure.

The machine representation should be determined by the actual information being stored.

For example:

```text
CURRENT AGE = CASTLE
```

does not need the same representation as:

```text
ENEMY CAVALRY = 4 OBSERVED UNITS
```

The first is a simple scalar world fact.

The second has observation scope and completeness semantics that materially affect interpretation.

### Carpenter rule

> **Semantic richness belongs at the boundary; representation stays as small as the question allows.**

---

# 3. Second cut — status does not need four permanent buckets

The proposed status vocabulary was:

```text
CURRENT
LAST-KNOWN
UNKNOWN
UNRESOLVED / CONTRADICTED
```

The Carpenter asks whether all four must exist as stored states.

Answer: **No.**

The essential invariant is simply:

```text
CURRENTLY QUALIFIED
        vs
NOT CURRENTLY QUALIFIED
```

`LAST-KNOWN` can often be represented by retaining the previous qualified value while marking it no longer current.

`UNKNOWN` can often be represented by absence of a qualified value.

`CONTRADICTED` can be represented only when contradiction materially affects a decision.

Therefore the physical model does not require four status values everywhere.

### Reduced rule

```text
VALUE + CURRENT/NOT-CURRENT
```

with additional qualification only where the decision requires it.

This is substantially cheaper.

---

# 4. Third cut — provenance is conditional

Provenance is valuable when multiple evidence paths can disagree.

It is not valuable merely because we can store it.

Examples where provenance earns its cost:

- two observation methods report different states;
- execution evidence competes with observation;
- identity continuity is uncertain;
- a transition is inferred rather than directly observed.

Examples where it may not earn its cost:

- a single deterministic scalar read used immediately by one consumer;
- transient search measurements with no persistence;
- facts whose source is structurally unambiguous.

### Carpenter rule

> **Provenance is a conflict-resolution tool, not a mandatory badge on every number.**

---

# 5. Fourth cut — supersession is a publication rule

The previous architecture described supersession as a semantic requirement.

That is correct.

But it does not deserve its own room or subsystem.

The rule is simply:

```text
NEW OBSERVATION
      ↓
COMPARE QUALIFICATION
      ↓
SUPERSEDES? ──NO──→ RETAIN
      │
     YES
      ↓
   PUBLISH
```

The actual mechanism may eventually use a goal, generation, phase, event, or another engine-supported representation.

That representation is deliberately not chosen here.

### Carpenter verdict

**Keep the rule. Remove the furniture.**

---

# 6. Fifth cut — identity is a conditional capability

Identity tracking is seductive because it looks sophisticated.

It is also one of the easiest ways to build a useless object database.

The Carpenter therefore imposes:

```text
IF decision depends on continuity
    THEN seek identity evidence
ELSE
    DO NOT TRACK INDIVIDUAL IDENTITY
```

Aggregate questions should remain aggregate questions.

If the only question is:

```text
How much enemy cavalry have we observed?
```

do not build:

```text
Knight_001
Knight_002
Knight_003
...
```

This is a major complexity saving.

---

# 7. Sixth cut — aggregate qualification belongs to the value

The architecture does not need a separate Aggregate subsystem.

Instead, the semantic contract simply prevents ambiguous aggregates.

Bad:

```text
ENEMY_CAVALRY = 2
```

Better:

```text
ENEMY_CAVALRY_OBSERVED = 2
```

or, where completeness is genuinely established:

```text
ENEMY_CAVALRY_CONFIRMED_TOTAL = 2
```

The distinction can be represented through different fields or contextual meaning where that is cheaper than a universal metadata structure.

### Carpenter rule

> **Name/represent the question precisely rather than building a generic metadata machine to rescue ambiguous names.**

---

# 8. Seventh cut — World State should be selective, not comprehensive

The strongest simplification remains:

```text
TRANSIENT OBSERVATION
        ↓
DOES IT EARN PERSISTENCE?
        ↓
NO → discard
YES → publish
```

Persistence earns its cost when information:

- serves multiple consumers;
- preserves material continuity;
- prevents dangerous amnesia;
- is expensive to recompute;
- represents a meaningful transition.

Nothing else belongs in persistent World State merely because it was observed.

---

# 9. Eighth cut — no generic freshness engine

Freshness is real.

A universal freshness framework is not yet earned.

The architecture only requires that consumers cannot mistake known-old information for current information when that distinction materially changes the decision.

Until the engine representation is known, use the smallest semantic distinction required by the consumer.

For example:

```text
CURRENT ENEMY ARMY POSITION
```

may require stronger recency handling than:

```text
LAST KNOWN ENEMY BASE LOCATION
```

There is no reason to impose one freshness mechanism on both.

---

# 10. Ninth cut — no universal contradiction store

Contradiction is important but rare enough that it does not justify a global contradiction database.

Use the simplest safe behavior:

```text
CONFLICTING EVIDENCE
        ↓
DO NOT OVERWRITE VALID STATE WITH WEAKER EVIDENCE
        ↓
REQUEST / WAIT FOR BETTER EVIDENCE IF MATERIAL
```

Only persist explicit unresolved state if a downstream decision actually depends on resolving the conflict.

Again:

**rule, not room.**

---

# 11. The truly minimal World Model

After the cuts, the World Model is conceptually only three things:

### 1. Observation Workbench

Answers questions about the current observable world.

### 2. World State

Retains a small set of useful qualified facts.

### 3. Publication Rules

Prevent obvious semantic corruption.

The third is not a physical room.

Therefore:

```text
                  REAL WORLD
                      ↓
             OBSERVATION WORKBENCH
                      ↓
                 QUALIFY
                      ↓
                 WORLD STATE
                      ↓
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
    BELIEF        SITUATION       CAPABILITY
```

Cross-cutting rules:

```text
OWNERSHIP
CURRENTNESS
SUPERSESSION
EVIDENCE
COST
```

That is enough.

---

# 12. The carpenter's load test

Every remaining concept must carry a load.

| Concept | Load carried | Keep? |
|---|---|---|
| Observation Workbench | Obtains world information | YES |
| World State | Preserves useful world information | YES |
| Qualification | Prevents semantic corruption | YES |
| Ownership | Prevents competing writers | YES |
| Currentness | Prevents stale-as-current errors | YES |
| Supersession | Prevents old evidence overwriting newer evidence | YES |
| Evidence | Prevents commands/inferences becoming facts | YES |
| Cost | Prevents observation/storage explosion | YES |
| Provenance | Resolves meaningful evidence conflicts | CONDITIONAL |
| Identity | Preserves continuity where materially needed | CONDITIONAL |
| Aggregate completeness | Prevents subset/total confusion | CONDITIONAL |
| Universal timestamps | Generic recency mechanism | NO — not yet earned |
| Universal confidence | Generic uncertainty mechanism | NO |
| Object database | Complete world replica | NO |
| Contradiction database | Global conflict storage | NO |
| Freshness subsystem | Generic expiry machinery | NO |
| Supersession subsystem | Dedicated service | NO |

This is the architecture earning its beams.

---

# 13. The deeper simplification

The World Model does not actually need to own “truth.”

It needs to own **qualified published observations**.

That wording is more precise.

Why?

Because the game world is true regardless of what AEGIS knows.

The engine's observation surface provides evidence about that world.

AEGIS then publishes only what the evidence justifies.

Therefore:

```text
REALITY
  ↓
OBSERVATION
  ↓
QUALIFICATION
  ↓
PUBLISHED WORLD KNOWLEDGE
```

This avoids pretending that the AI has omniscient world state.

---

# 14. World State is not a truth database

This distinction is important enough to make explicit.

Bad architecture:

```text
WORLD DATABASE
= everything we think is true
```

Better architecture:

```text
WORLD STATE
= information we have sufficient evidence to publish
```

Belief then handles uncertainty and prediction.

Situation Analysis handles meaning.

Capability handles what can actually be done.

This gives us a clean epistemic boundary without building an epistemology engine.

---

# 15. The behavioral-return test

The World Model earns its existence only if its facts create downstream leverage.

For every persistent fact we eventually implement, we should be able to draw:

```text
FACT
 ↓
CONSUMER 1
CONSUMER 2
CONSUMER 3
...
```

If the graph ends immediately:

```text
FACT → nobody
```

then the fact probably should not exist.

If the graph is:

```text
FACT
 ↓
THREAT
 ↓
OBJECTIVE
 ↓
REQUIREMENT
 ↓
PRODUCTION
 ↓
MILITARY
```

then the observation has high behavioral leverage.

This becomes the primary architectural metric for World State.

---

# 16. Failure cases after simplification

The Carpenter confirms that the reduced architecture still handles the major failures.

### Fog of war

```text
No observation
≠
Destroyed
```

### Partial observation

```text
Observed subset
≠
Confirmed total
```

### Unit replacement

```text
Same type
≠
Same identity
```

### Building foundation

```text
Exists
≠
Ready
```

### Command

```text
Issued
≠
Completed
```

### Stale observation

```text
Last-known
≠
Current
```

### Contradiction

```text
Conflict
≠
Permission to guess
```

### Strategic interpretation

```text
World fact
≠
Threat rating
```

Nothing in the simplification breaks these invariants.

---

# 17. What the Carpenter refuses to add

The following are explicitly blocked unless a later adversarial failure proves necessity:

- universal `WORLD_RECORD` schema;
- universal `VALID` bit on every fact;
- universal `GENERATION` field;
- universal timestamp;
- universal confidence score;
- universal expiry timer;
- object registry;
- identity manager;
- aggregate manager;
- provenance manager;
- contradiction manager;
- world-event bus;
- dedicated world-state scheduler;
- world-state recovery engine.

These may eventually emerge as implementation mechanisms for specific proven needs.

They are not architecture yet.

---

# 18. Final carpenter design

The smallest architecture that survives the review is:

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
                          QUALIFY
                             │
                             ▼
                 ┌───────────────────────┐
                 │      WORLD STATE      │
                 │                       │
                 │ useful current facts │
                 │ useful last-known    │
                 │ unresolved only when │
                 │ materially necessary │
                 └───────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
           BELIEF        SITUATION       CAPABILITY
           MODEL          ANALYSIS         SYSTEM
```

The World Model itself therefore contains only:

```text
OBSERVE
QUALIFY
PUBLISH
RETAIN
```

Everything beyond those verbs belongs elsewhere or is a local semantic rule.

---

# 19. Carpenter verdict

**PASS.**

The architecture has reached a useful stopping point for simplification.

Further reduction would begin to erase distinctions that prevent real failure modes:

- current vs last-known;
- observed vs total;
- identity vs guess;
- fact vs interpretation;
- command vs outcome.

Those distinctions have earned their beams.

Everything else remains conditional.

The next attack should therefore not be another broad complexity review.

It should be an adversarial **cross-system failure review**:

> What happens when World Model, Belief, Situation, Capability, Commitment, Execution, and Scheduler all receive slightly different versions of reality at the same time?

That is where a clean World Model can still be destroyed by a bad building around it.

---

# 20. Handoff

**NEXT MODE: ⚔️ ADVERSARY**

Attack target:

```text
WORLD STATE
      ↕
BELIEF
      ↕
SITUATION
      ↕
CAPABILITY
      ↕
COMMITMENT
      ↕
EXECUTION
      ↕
WORLD STATE
```

The adversary should specifically attack:

1. stale information crossing subsystem boundaries;
2. conflicting writers;
3. feedback loops;
4. commitment made against obsolete capability;
5. execution evidence arriving before observation;
6. observation arriving before execution acknowledgment;
7. multiple generations of the same strategic decision;
8. scheduler starvation;
9. contradictory beliefs;
10. strategic oscillation caused by rapidly changing observations;
11. resource/capability/world-state disagreement;
12. recovery loops that repeatedly recreate failed commitments.

The next question is no longer whether the World Model is simple enough.

It is whether the **building around it can safely consume reality without corrupting it.**
