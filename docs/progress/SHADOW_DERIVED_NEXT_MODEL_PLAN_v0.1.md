# Shadow-Derived Next Model Plan v0.1

**Project:** AiByz / Byzantine next-generation AI
**Target runtime:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Reference controller:** Shadow DC7, canonical source preserved by `TheByzantineShadow/SourceShaRef`
**Status:** FORWARD DESIGN / PRE-IMPLEMENTATION

## 0. Executive correction

The next bot is **not an AEGIS architecture implemented from scratch**.

The next bot is a **Shadow-derived controller** whose behavioral architecture, control idioms, and proven `.per` mechanisms are retained wherever forensic evidence shows they work. AEGIS principles are applied as targeted repairs to Shadow's weaknesses, not as a replacement architecture.

The design target is:

```text
SHADOW DC7
    ↓
forensic extraction of proven control mechanisms
    ↓
pattern classification
    ↓
failure/ambiguity inventory
    ↓
minimal corrective modifications
    ↓
SHADOW-DERIVED NEXT MODEL
```

The governing rule is:

> Preserve demonstrated control competence; modify only the mechanisms whose ambiguity, coupling, stale-state behavior, ownership, or verification weakness creates demonstrable engineering risk.

## 1. What is retained

The next model retains Shadow's fundamental programming model:

- centralized constants and state vocabulary;
- explicit state machines;
- timers as hysteresis, debounce, dwell, and retry mechanisms;
- search/filter/aggregate/select loops;
- scratch goals for local computation;
- negative-jump iteration where it is proven and bounded;
- geometric reasoning and point calculations;
- group formation and group-state control;
- target history and anti-thrashing memory;
- resource/source selection;
- construction progression;
- production progression;
- research progression;
- escrow and resource protection;
- market conversion;
- direct engine commands at execution boundaries;
- economic/military interaction;
- explicit recovery and re-entry behavior.

These are not to be replaced merely because they are stylistically old or monolithic.

## 2. What is modified

### 2.1 State ownership

Every consequential state variable receives a declared owner, readers, lifetime, reset condition, and semantic type.

### 2.2 Scratch-state discipline

Shadow's scratch-state technique is retained. Generic scratch channels are not abolished. Their use is bounded by declared owner/lifetime contracts so that one subsystem cannot silently inherit another subsystem's live state.

### 2.3 Consequential generation fencing

Long-lived strategic, economic, construction, production, and military commitments receive a generation identifier. Transient arithmetic/search scratch does not receive unnecessary lifecycle machinery.

### 2.4 Explicit expiry

Requirements, reservations, target decisions, progression states, and pending operations that can become obsolete receive explicit expiry or invalidation conditions.

### 2.5 Command/result separation

A command is an attempted world mutation. It is not completion evidence. Where an action matters to progression or capability, the next model records pending state and verifies the resulting world state.

### 2.6 Reconciliation

When expected progression and observed world state disagree, the system reconciles from observation rather than blindly advancing the old progression state.

### 2.7 Duplicate/dead-code control

Shadow's historical residue is evidence, not automatically executable design. Duplicate definitions, aliases, obsolete experiments, and conflicting generations must be identified before transplant.

### 2.8 Control-flow hardening

Shadow's jump-based loops are retained where useful, but every transplanted loop receives a boundedness and reachability audit. New behavior must not depend on fragile rule insertion positions without explicit documentation.

## 3. What is deliberately NOT done

The next model will not:

- become a service-oriented rewrite disconnected from Shadow's `.per` idioms;
- replace every goal with a formal record object;
- hide engine primitives behind unnecessary abstraction;
- separate economy and military so aggressively that cross-domain feedback disappears;
- treat all scratch state as requiring heavyweight lifecycle metadata;
- copy Shadow's duplicate definitions or accidental aliases without qualification;
- copy commands merely because they exist in Shadow;
- infer target-build semantics from historical behavior without qualification;
- declare an action successful merely because a command was issued.

## 4. Development sequence

### Phase 0 — Canonical Shadow freeze

`SourceShaRef` is the canonical source reference. Conversational pasted copies are subordinate to it when disagreement exists.

### Phase 1 — Control-pattern extraction

Inventory Shadow by mechanism, not only by file section:

1. search loops;
2. state machines;
3. timer/hysteresis loops;
4. geometry/candidate selection;
5. source/dropsite selection;
6. worker allocation;
7. escrow/reservation;
8. construction lifecycle;
9. production lifecycle;
10. technology progression;
11. scouting/information control;
12. military group control;
13. target/raid control;
14. recovery/re-entry;
15. end-state and safety behavior.

### Phase 2 — Failure inventory

Each pattern is checked for:

- ambiguous ownership;
- state collision;
- stale state;
- implicit completion;
- missing timeout;
- missing recovery;
- hidden dependency;
- duplicated definition;
- alias/collision;
- jump fragility;
- direct cross-domain mutation;
- unqualified engine assumption.

### Phase 3 — Minimal Shadow-derived kernel

Implement only reusable protections needed by the extracted patterns:

```text
OWNER
STATE
LIFETIME
GENERATION where consequential
EXPIRY
PENDING
VERIFICATION
RECOVERY
```

The kernel is subordinate to the Shadow-derived control model. It is not a new architecture imposed on it.

### Phase 4 — Economic/resource control transplant

First substantial subsystem: Resource Logistics / Worker Allocation.

Reason: this subsystem exercises Shadow's strongest reusable mechanisms while touching the greatest number of civilization-state dependencies without requiring the entire military controller.

### Phase 5 — Production control transplant

Demand → candidate unit → affordability/escrow → production endpoint → train → pending → census verification → composition update.

### Phase 6 — Information/scouting transplant

Retain Shadow's exploration/search/geometry/timer control while adding freshness and target-generation fencing where necessary.

### Phase 7 — Military control transplant

Retain Shadow's group states, target selection, geometry, retreat vectors, reinforcement, raid state machine, and tactical search loops. Add verification/reconciliation only around consequential state transitions.

### Phase 8 — Technology/progression integration

Integrate research, age progression, escrow, construction, production, and recovery using Shadow's proven progression-controller pattern with explicit stale-state protection.

### Phase 9 — Whole-civilization integration

Qualify cross-domain feedback:

```text
THREAT
→ CAPABILITY GAP
→ ECONOMIC RESPONSE
→ PRODUCTION / CONSTRUCTION
→ VERIFIED WORLD STATE
→ MILITARY CAPABILITY
→ REASSESSMENT
```

## 5. Success criterion

The next model is successful when it demonstrates that Shadow's behavioral mechanisms survive transplantation while the known Shadow failure modes are materially reduced.

The primary metric is not lines of `.per`.

The metric is closed-loop competence:

```text
OBSERVE
→ DECIDE
→ ACT
→ WORLD CHANGES
→ VERIFY
→ RECOVER IF NECESSARY
→ REASSESS
```

The final controller should still be recognizably a Shadow-descended `.per` AI, but with substantially stronger state integrity and evidence discipline.
