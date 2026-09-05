# AEGIS World Model — Scientist Pass 3

**Date:** 2026-09-05  
**Layer:** 3A — Architecture / 4 of 5 review passes  
**Mode:** SCIENTIST  
**Status:** ENGINE-SEMANTICS QUALIFICATION — PRE-IMPLEMENTATION  
**Target build:** AoE2DE `101.103.48987.0`

## 0. Mission

Determine which surviving World Model claims are actually supported by engine and stock evidence, which are composed architectural conclusions, and which remain open until empirical qualification. This pass does not implement `.per` code, execute runtime tests, allocate ABI channels, or treat architectural intent as engine fact.

## 1. Executive verdict

**SCIENTIST RESULT: PASS WITH OPEN EMPIRICAL QUESTIONS.**

The reduced World Model is compatible with the known AoE2DE scripting surface, but several of its most important semantic guarantees are not native engine primitives. They are AEGIS rules that must eventually be implemented using qualified primitives and runtime-tested.

The engine clearly exposes a substantial observation surface: object searches, filters, selected-object reads, object-type data, object state/status, ownership, movement/target/action information, and search-state information. Official updates also demonstrate that these interfaces have historically been corrected and expanded, which is itself evidence that exact behavior is build-sensitive.

The Scientist therefore rejects two dangerous extremes:

1. **Engine absolutism:** assuming every AEGIS semantic distinction already exists as a native field.
2. **Architecture absolutism:** assuming a useful semantic distinction is implementable merely because it is conceptually clean.

The correct handoff is: **semantic contract first; empirical ABI qualification before representation; runtime tests before claiming behavior.**

## 2. Evidence classification

| World Model claim | Classification | Scientist finding |
|---|---|---|
| Engine can search/filter objects | DIRECT / DOCUMENTED | Supported |
| Engine can read selected object data | DIRECT / DOCUMENTED | Supported |
| Object ownership is observable | DIRECT / DOCUMENTED | Supported |
| Object lifecycle/progress information exists | DIRECT / DOCUMENTED | Supported |
| Type-level data can be queried separately from live-object state | DIRECT / DOCUMENTED | Supported |
| Search visibility/scope affects what can be observed | DOCUMENTED / HISTORICAL | Supported as a constraint; exact current edge behavior requires build qualification |
| Observation is not automatically a strategic interpretation | ARCHITECTURAL RULE | Correct and desirable; not an engine primitive |
| Missing search result does not prove destruction | COMPOSED / ARCHITECTURAL RULE | Required by observation scope semantics; must never be implemented as automatic destruction |
| Partial count is not total count | ARCHITECTURAL RULE | Correct; completeness must be established by the observation method |
| CURRENT vs LAST-KNOWN vs UNKNOWN vs UNRESOLVED | ARCHITECTURAL SEMANTICS | Not proven as native engine states |
| Identity continuity across observations | OPEN | Object identity exists; durable historical continuity requires qualification |
| Universal timestamp on facts | REJECTED | No need established; precise-time/timer facilities do not justify universal timestamps |
| Universal confidence | REJECTED | Not an engine requirement |
| Universal generation | OPEN / DEFERRED | Useful semantic concept; representation not established |
| Supersession | ARCHITECTURAL RULE | Can be implemented as publication policy if representation supports it |
| Contradiction | ARCHITECTURAL SEMANTICS | No dedicated contradiction primitive established |
| Object exists = capability available | REJECTED | Engine/API surface itself separates object/type/state/feasibility concepts |
| Feasibility = execution success | REJECTED | Feasibility and commands are distinct concepts |
| Command = world transition | REJECTED | Requires verification |
| Execution evidence may inform World State | COMPOSED / ARCHITECTURAL RULE | Valid design; exact implementation remains open |
| Search cost matters | DIRECT / DOCUMENTED | Supported; many search/filter operations are high-cost |
| Scheduler owns observation cadence | ARCHITECTURAL RULE | Correct separation, not engine primitive |

## 3. What the engine actually gives us

The current scripting reference exposes commands for searching and reading world objects, including `up-find-local`, `up-find-remote`, `up-filter-distance`, `up-filter-status`, `up-get-object-data`, `up-get-object-target-data`, `up-get-object-type-data`, `up-get-search-state`, and fact-oriented queries. Many of these observation operations are classified as expensive in the current scripting reference.

This supports the existence of an **Observation Workbench** as a real architectural consumer of engine primitives. It does not support turning that Workbench into a permanent object database.

Official Update 37650 records that `up-get-object-type-data` was expanded to function with unavailable units and that `object-data-ownership` was added. This establishes a useful distinction between type-level information and live-object state and demonstrates that the engine's observation surface has evolved over time. citeturn0search2

Official Update 39284 records fixes to stacked local/remote status searches, `up-find-remote` pending-object behavior, object-data idling, and focus/target fact functions. That is strong evidence that search and observation semantics contain edge cases and are not safe to infer from names alone. citeturn0search6

Official Update 50292 records additional fixes and extensions to object-data and unit-group result behavior, including corrections to `up-get-object-type-data`. Again, this supports build-scoped qualification rather than assumption. citeturn0search0

The June 2026 Update 177723 records further AI-engine corrections, including an `object-data-next-attack` fix and an exploration-command targeting fix. The project must therefore treat the exact target executable as the ABI authority for later empirical work. citeturn0search1

## 4. Observation is scoped

The Scientist accepts the following invariant:

```text
SEARCH RESULT
    ↓
WHAT DID THIS SEARCH ACTUALLY COVER?
    ↓
QUALIFY THE CLAIM
```

A search returning zero is not, by itself, proof that the world contains zero matching objects.

Likewise:

```text
OBSERVED N
```

must not silently become:

```text
TOTAL N
```

unless the observation method demonstrably establishes completeness.

Historical UserPatch documentation and official fixes reinforce that remote/local searches, pending objects, visibility, and status handling have meaningful semantics. These are reasons to preserve the architectural boundary rather than reasons to invent a stronger engine guarantee than the evidence supports.

## 5. Object identity

The engine exposes object identity and ownership information. That supports identity as an observable property.

It does **not yet prove** that AEGIS can safely maintain universal historical identity continuity across every relevant lifecycle event.

Therefore the architectural rule survives:

> Track identity only when continuity materially affects a decision, and only with evidence sufficient for the target build.

Do not create a universal identity database before an actual decision requires it.

## 6. Lifecycle and readiness

The engine exposes lifecycle/progress-oriented object data. Historical updates include corrections to `object-data-progress-type` and other object-state functions. This supports the World Model's distinction between an object existing and the object being in a particular lifecycle state. citeturn0search3

However:

```text
OBJECT EXISTS
    ≠
OBJECT READY
    ≠
CAPABILITY AVAILABLE
    ≠
CAPABILITY EFFECTIVE
```

The final two transitions are not World Model facts. They require additional capability/feasibility reasoning.

This distinction is reinforced by the engine's separate feasibility commands and by official scripting changes that independently address queueing/training/building behavior. Update 50292, for example, separately discusses object-data correctness and restrictions on queuing technologies and units. citeturn0search0

## 7. Feasibility is not execution

The architecture's execution gate survives scientific review.

Conceptually:

```text
CAN I DO THIS?
      ↓
FEASIBILITY
      ↓
ISSUE COMMAND
      ↓
DID THE WORLD CHANGE?
      ↓
VERIFY
```

The engine's existence of distinct `up-can-build`, `up-can-research`, `up-can-train`, and related readiness/feasibility primitives is evidence for keeping these concepts separate.

A successful feasibility check cannot be promoted into proof that a later command succeeded.

## 8. Command/result separation

The Scientist finds no evidence for a general transaction guarantee connecting command issuance directly to world-state completion.

This is critical.

AEGIS must not implement:

```text
COMMAND ISSUED
    ↓
ASSUME SUCCESS
```

It must instead use:

```text
COMMAND ISSUED
    ↓
OBSERVE / VERIFY
    ↓
QUALIFIED WORLD EVIDENCE
```

Official AI-engine fixes repeatedly distinguish intended commands from actual behavior—for example, corrections to targeting, pathing, object data, and queued actions. citeturn0search1turn0search0

## 9. Current / last-known / unknown / unresolved

These four states remain architecturally useful but are **not claimed as native engine fields**.

Scientist disposition:

- `CURRENT`: can be a semantic conclusion when the observation is sufficiently current for the relevant decision.
- `LAST-KNOWN`: can be represented conceptually when an earlier qualified observation remains useful after current observation is unavailable or insufficient.
- `UNKNOWN`: necessary when available evidence does not establish the fact.
- `UNRESOLVED`: necessary when materially conflicting evidence cannot yet be safely reconciled.

The exact machine representation is **OPEN**.

Do not allocate a universal validity bit or universal state code until runtime/ABI experiments establish the cheapest safe representation.

## 10. Freshness

The Scientist rejects a universal freshness subsystem.

Current documentation exposes timer and precise-time capabilities, but their existence does not prove that every World State field should carry a timestamp or that one global age threshold is strategically correct.

The correct architectural primitive remains:

```text
MATERIAL DECISION
      ↓
COULD MATERIAL STATE HAVE CHANGED?
      ↓
REVALIDATE IF YES
```

This is a decision-validity rule, not a database feature.

## 11. Supersession

Supersession is scientifically plausible as a publication rule:

```text
NEW EVIDENCE
     ↓
QUALIFY
     ↓
SUPERSEDES OLD CLAIM?
```

What remains unproven is the safest `.per` representation for arbitrary fact generations and ordering.

Therefore:

**SEMANTICS: KEEP. REPRESENTATION: OPEN.**

## 12. Contradiction

No dedicated contradiction primitive is required by the evidence.

The minimum safe behavior is simply to avoid overwriting a materially relevant claim with an incompatible claim unless the new evidence is qualified to supersede it.

If neither claim can safely win:

```text
UNRESOLVED
```

is an architectural state, not necessarily a stored engine value.

## 13. Provenance

Provenance remains conditional.

The Scientist does not find evidence requiring every World State fact to carry universal source metadata.

But source information may become materially useful when:

- two observations conflict;
- a result has unusual scope;
- execution verification is being reconciled with scouting evidence;
- identity continuity is uncertain;
- supersession depends on evidence ordering.

Therefore provenance remains a **conditional representation requirement**, not a subsystem.

## 14. Search cost is real

The current scripting reference marks many search/filter operations as expensive. That means the architectural Scheduler/Attention boundary is not theoretical decoration.

Observation cadence must be controlled because excessive observation can itself damage runtime behavior.

Therefore:

```text
SCHEDULER / ATTENTION
        ↓
WHEN TO ASK
        ↓
WORLD MODEL
        ↓
HOW TO ANSWER
```

The World Model should not decide its own polling frequency.

## 15. Stock AI evidence: use, do not inherit

The stock AI demonstrates extensive use of object facts, searches, temporary goals, strategic numbers, and stateful control. That establishes practical precedent for using the engine's observation surface.

It does **not** authorize AEGIS to inherit stock state ownership.

This remains especially important because the A1 census showed heavy multiplexing of stock goals and strategic numbers. AEGIS's Layer 2 ABI decision therefore remains unchanged: semantic architecture does not grant permission to reuse stock channels.

## 16. What requires runtime experiments

The following are now explicit Scientist gates rather than architectural assumptions:

### E1 — Search absence semantics
Determine exactly what zero-result searches establish under relevant local/remote/status/visibility conditions on build `101.103.48987.0`.

### E2 — Identity continuity
Determine whether selected object identities remain stable across relevant lifecycle transitions and replacement cases.

### E3 — Status/lifecycle transitions
Map observable values across foundation, construction, completion, queued/training, creation, destruction, and other relevant states.

### E4 — Publication representation
Determine the cheapest safe `.per` representation for current/last-known/unknown semantics where needed.

### E5 — Supersession ordering
Determine whether AEGIS can safely represent “newer evidence supersedes older evidence” without a universal generation framework.

### E6 — Verification latency
Measure how quickly world-state evidence reflects commands and consequential transitions.

### E7 — Observation cost
Measure the runtime cost of candidate Workbench queries at realistic frequencies.

### E8 — Partial-census behavior
Demonstrate which search scopes can legitimately support a complete count and which cannot.

### E9 — Capability boundary
Test the relationship between object state, feasibility, queue state, creation, and actual operational availability.

### E10 — Failure/recovery evidence
Determine which observable world changes reliably prove command failure, completion, interruption, or replacement.

## 17. Scientific falsifiers

The architecture should be revised if empirical testing demonstrates any of the following:

- F1: a required observation cannot be obtained through the available engine surface;
- F2: a supposedly stable identity is not usable for the continuity decisions we require;
- F3: required state distinctions cannot be represented within safe available channels;
- F4: observation cost makes the proposed Workbench operationally infeasible;
- F5: command verification latency makes the proposed control loops unsafe;
- F6: the engine's search semantics make the proposed scope qualification impossible;
- F7: the semantic contract requires more persistent state than the available ABI can safely support.

These are legitimate reasons to modify the architecture. Convenience is not.

## 18. Scientist disposition by component

| Component | Disposition |
|---|---|
| Observation Workbench | **PROVEN CONCEPT / IMPLEMENTABLE SURFACE** |
| Selective World State | **ARCHITECTURAL DESIGN — REPRESENTATION OPEN** |
| Current/last-known semantics | **KEEP / RUNTIME QUALIFY** |
| Unknown/unresolved semantics | **KEEP / REPRESENTATION OPEN** |
| Selective identity | **KEEP / RUNTIME QUALIFY** |
| Selective aggregates | **KEEP / SCOPE QUALIFY** |
| Lifecycle observation | **SUPPORTED / MAP EXACT VALUES** |
| Capability boundary | **KEEP / CROSS-SYSTEM QUALIFY** |
| Supersession rule | **KEEP / REPRESENTATION OPEN** |
| Provenance | **CONDITIONAL / OPEN** |
| Universal freshness | **REJECT** |
| Universal timestamp | **REJECT** |
| Universal confidence | **REJECT** |
| Universal generation | **DEFER** |
| Object database | **REJECT** |
| Contradiction manager | **REJECT** |
| Identity manager | **REJECT** |
| Observation scheduler inside World Model | **REJECT** |
| Strategic interpretation inside World State | **REJECT** |

## 19. Final scientific contract

The strongest statement we can make without runtime fiction is:

```text
REAL WORLD
    ↓
ENGINE OBSERVATION SURFACE
    ↓
OBSERVATION WORKBENCH
    ↓
QUALIFICATION
    ↓
SELECTIVE WORLD STATE
    ↓
BELIEF / SITUATION / CAPABILITY
```

And the critical scientific constraint is:

```text
ENGINE FACT
    ≠
AEGIS INTERPRETATION
    ≠
STRATEGIC DECISION
```

The engine gives us observations and operations. AEGIS supplies the semantic discipline around those observations.

## 20. Final verdict

**WORLD MODEL SCIENTIST PASS 3: PASS.**

The Carpenter-reduced architecture survives scientific scrutiny.

No new room is justified.

No universal metadata framework is justified.

No stock state channel is newly authorized.

No ABI allocation is authorized.

No runtime claim is being made.

The remaining unknowns are now concrete experimental questions rather than vague architectural uncertainty.

### Handoff to Systems Assurance

The fifth pass must now answer a different question:

> **Given the architecture, the cuts, and the scientifically established/open engine facts, can the World Model be handed to implementation without hiding an unresolved cross-system defect?**

Systems Assurance must trace the subsystem through:

```text
SCHEDULER
SCOUTING
SITUATION
CAPABILITY
ECONOMY
PRODUCTION
MILITARY
COMMITMENT
EXECUTION
VERIFICATION
RECOVERY
MEMORY
MAP
```

and produce one of:

- **PASS**
- **PASS WITH TARGETED CORRECTION**
- **HOLD FOR EVIDENCE**
- **REJECT**
- **RETURN TO SPECIFIC PASS**

Only that review can close the World Model five-pass cycle.
