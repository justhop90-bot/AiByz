# AEGIS — Cross-System Objection & Qualification Register

**Date:** 2026-09-05  
**Layer:** 3A — Architecture → Qualification  
**Status:** ACTIVE QUALIFICATION REGISTER — ARCHITECTURE CLOSURES PRESERVED  
**Target build:** AoE2DE `101.103.48987.0`  
**Canonical repository:** `justhop90-bot/AiByz` / `main`

## 1. Purpose

This register consolidates the unresolved machine-level questions repeated across the completed AEGIS subsystem reviews into one shared qualification program.

It is deliberately **not** a runtime subsystem, manager, database, universal state manager, or second architecture. It is the engineering control document that prevents the same machine question from being independently reinvented, inconsistently answered, or silently converted from hypothesis into implementation truth.

The governing rule is:

> Prove shared machine semantics once where they are genuinely shared; specialize only where a subsystem's behavior is materially different.

The register therefore separates three things:

1. **Architecture closure** — the subsystem's conceptual boundary survives the five-pass review.
2. **Machine qualification** — the target build proves that an intended representation or primitive actually behaves as required.
3. **Runtime validation** — the implemented system demonstrates the qualified architecture under controlled execution.

An open qualification gate does not by itself reopen a closed architecture. A gate reopens architecture only when target-build evidence falsifies a load-bearing architectural statement.

## 2. Executive disposition

The cross-system audit found no demonstrated P0 collapse of the completed Layer-3A architecture.

The dominant remaining risk is concentrated in a relatively small set of shared machine truths:

- typed identity and ABI meaning;
- identity and generation continuity;
- scope continuity;
- UNKNOWN versus FALSE versus ZERO;
- current versus last-known state;
- coherent publication;
- search/filter isolation;
- pending versus created versus available lifecycle;
- command issuance versus acceptance;
- cancellation and supersession;
- concurrency and resource/commitment races;
- runtime cost and build-scoped behavior.

These questions recur because the AoE2DE engine supplies useful primitives but does not natively provide the complete AEGIS semantic model. The correct response is consolidation, not architectural inflation.

## 3. Architectural rule set

### 3.1 Native evidence precedence

Use direct engine evidence first. Derive only what the engine cannot provide. Store only derived state with a behavioral return. Never duplicate engine state merely to make the architecture look complete.

### 3.2 Semantic identity precedes numeric identity

A number is not a meaning. Every proposed channel must be qualified by primitive, parameter type, semantic owner, legal range, writer, reader, lifecycle, and build/profile scope.

### 3.3 One semantic state, one authoritative publisher

Multiple consumers may read a state. Multiple observations may contribute evidence. There must not be two independent authoritative publishers for the same semantic state.

### 3.4 UNKNOWN is a real result

Failure to observe, zero results, stale evidence, unsupported representation, and confirmed absence are not interchangeable.

### 3.5 Controller time and world time are different clocks

Rule eligibility, timers, generations, and publication cycles describe controller state. Queueing, construction, training, research, movement, combat, and object creation describe world transitions. One must not be substituted for the other.

### 3.6 Command is not completion

The mandatory realization ladder remains:

`DESIRE → CAN-FACT → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

A later state must be established by appropriate evidence rather than inferred from an earlier state.

## 4. Shared qualification gates

The following twelve gates are the primary consolidated program. Subsystem-specific gates remain subordinate to these shared gates unless a subsystem proves a materially different semantic requirement.

### Q-01 — Build Identity & Semantic Scope

**Question:** Are all qualified claims tied to the exact AoE2DE executable/build/profile for which they are intended?

**Why it matters:** Documentation and historical behavior can diverge from the installed executable. A valid primitive on one build is not unconditional proof on another.

**Consumes:** executable fingerprint, installed AI closure, validator/profile identity, source/version evidence.

**Evidence required:** exact executable version/hash; relevant stock AI snapshot; explicit target-build identifier on every qualification artifact.

**Closure criterion:** every admitted primitive and representation has an unambiguous build scope and regression identity.

**Severity:** P1.

**Owner:** Machine Qualification / ABI authority.

**Dependencies:** all other gates.

**Architecture reopen:** No, unless evidence shows the architecture depends on a behavior unavailable on the target build.

### Q-02 — Typed ABI Identity & Legal Range

**Question:** Does each proposed AEGIS channel/primitive use the correct semantic parameter type, identifier namespace, legal range, and operation-specific constraints?

**Why it matters:** unit, unit-line, class, building, technology, goal, strategic number, point, object data, and output-goal parameters are not interchangeable. Numeric coincidence is not type compatibility.

**Evidence required:** exact engine signature; target-build behavior; validator behavior; stock symbol/value/type census; operation-specific range tests.

**Closure criterion:** a channel can be identified as `(primitive, parameter type, semantic symbol, numeric identity, legal range, context)` rather than by number alone.

**Severity:** P1.

**Owner:** ABI authority.

**Dependencies:** Q-01, Q-03.

**Architecture reopen:** Only if a required semantic cannot be represented without violating the subsystem boundary.

### Q-03 — State-Channel Ownership & Collision

**Question:** Can every AEGIS semantic state be assigned an unambiguous owner without hijacking stock channels?

**Why it matters:** stock goals/SNs/timers/facts are heavily multiplexed. Reusing an existing channel can create invisible coupling and corrupt unrelated AI behavior.

**Current disposition:** No stock channel is cleared merely because its numeric value appears convenient. The previously established collision map remains authoritative input to qualification.

**Evidence required:** symbol/value/context census; writer/reader map; lifecycle analysis; cross-subsystem ownership review.

**Closure criterion:** each core semantic channel has one publisher, known readers, known collision status, and target-build ABI qualification.

**Severity:** P1.

**Owner:** Systems Assurance + ABI authority.

**Dependencies:** Q-02, Q-08, Q-30.

**Architecture reopen:** Yes only if no non-colliding representation can satisfy a load-bearing contract without changing architecture.

### Q-04 — Identity & Generation Continuity

**Question:** Can an objective, candidate, decision, commitment, execution attempt, and verification result be correlated without confusing successive versions of the same semantic object?

**Why it matters:** asynchronous world changes make stale commands and stale results dangerous. Identity alone is insufficient when the same semantic object is revised.

**Evidence required:** target-build representation of identity/generation; propagation tests; stale-generation rejection; wrap/initial-value policy; concurrent-generation tests.

**Closure criterion:** a downstream consumer can reject evidence or action belonging to a superseded generation without deleting valid history.

**Severity:** P1.

**Owner:** Commitment / Execution / Verification contract authority, coordinated by Systems Assurance.

**Dependencies:** Q-02, Q-05, Q-08, Q-15.

**Architecture reopen:** Only if generation protection proves impossible and the architecture's stale-state invariants cannot otherwise be preserved.

### Q-05 — Scope, Freshness & Current-vs-Last-Known Semantics

**Question:** Does retained information preserve the scope and temporal qualification necessary for its meaning?

**Why it matters:** a current enemy count, a last-known count, an observation of one location, and a global claim are different propositions.

**Required distinctions:** current, last-known, stale, unresolved, unknown; plus geographic/player/object scope where consequential.

**Evidence required:** repeated observation tests; delayed observation tests; material-change/revalidation tests; scope propagation tests.

**Closure criterion:** no subsystem can silently widen a local/stale observation into a current/global fact.

**Severity:** P1.

**Owner:** World Model for observation truth; Belief/Situation for inference scope; Systems Assurance for interface integrity.

**Dependencies:** Q-01, Q-04, Q-06, Q-26.

**Architecture reopen:** Yes if a load-bearing architecture statement requires a distinction the machine cannot represent or qualify.

### Q-06 — UNKNOWN / FALSE / ZERO / Absence Semantics

**Question:** Can the implementation preserve the difference between confirmed zero, confirmed absence, unknown, unobserved, stale, and search failure?

**Why it matters:** collapsing these states creates false certainty and can trigger incorrect planning, decisions, commands, or recovery.

**Evidence required:** fact failure tests; zero-result search tests; unavailable-object tests; stale-data tests; explicit unknown encoding tests.

**Closure criterion:** consequential unknowns remain distinguishable from false/zero and are prevented from silently becoming strategic facts.

**Severity:** P1.

**Owner:** World Model / Belief / Verification semantic contract; ABI authority for representation.

**Dependencies:** Q-05, Q-09, Q-10, Q-25.

**Architecture reopen:** Yes if the architecture requires UNKNOWN but the target machine cannot represent it without semantic corruption.

### Q-07 — Search Isolation, Filter State & Multiplicity

**Question:** Do searches, filters, object queries, and repeated fact operations produce isolated and correctly attributable results?

**Why it matters:** AoE2DE search operations have historical quirks and some alter state used by subsequent searches. Search results may be expensive, empty, provisional, or affected by pending-object behavior.

**Evidence required:** stacked-search tests; filter reset tests; zero-result tests; repeated-search identity tests; multiple-result handling; concurrent search-state tests where applicable; cost measurements.

**Closure criterion:** every search-dependent semantic has proven filter setup, isolation behavior, result multiplicity, identity continuity, and zero-result interpretation.

**Severity:** P1.

**Owner:** Machine Qualification / Scientist.

**Dependencies:** Q-01, Q-02, Q-06, Q-21, Q-22.

**Architecture reopen:** Only if required evidence cannot be obtained without changing a subsystem's load-bearing boundary.

### Q-08 — Publication Coherence & Atomic Semantic Envelope

**Question:** Can a multi-field semantic result be published without consumers observing a mixed-generation or partially written state?

**Why it matters:** AEGIS contracts often require `VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`. If fields are observed from different publication cycles, the consumer can act on a state that never existed coherently.

**Required behavior:** invalidate → populate → establish identity/owner/scope/payload → validate/publicize. The word “atomic” must not be used unless the engine actually provides atomicity.

**Evidence required:** interrupted publication tests; repeated read-during-write tests; validity protocol tests; generation coherence tests.

**Closure criterion:** consumers either see a coherent published record or a deliberately invalid/unknown record.

**Severity:** P1.

**Owner:** Semantic publisher + Systems Assurance.

**Dependencies:** Q-03, Q-04, Q-05, Q-08 itself, Q-30.

**Architecture reopen:** Yes if coherent publication is impossible and the architecture relies on coherent multi-field state.

### Q-09 — Command Acceptance & Pending Lifecycle

**Question:** What exactly happens between an issued engine action and the resulting world object/state?

**Lifecycle under test:** issued → accepted/queued → pending → created → available → deployed → effective.

**Why it matters:** `train`, `build`, `research`, and related commands are not transaction receipts. Pending-object semantics and queue coverage have changed historically.

**Evidence required:** controlled action tests; `can-*` versus action tests; pending-object observation; creation observation; availability observation; queue interruption/cancellation tests.

**Closure criterion:** each action used by AEGIS has an empirically established acceptance/postcondition path on the target build.

**Severity:** P1.

**Owner:** Execution + Verification, with Scientist qualification.

**Dependencies:** Q-01, Q-02, Q-04, Q-10, Q-15.

**Architecture reopen:** Only if the architecture assumes a transition the engine demonstrably cannot expose or qualify.

### Q-10 — Cancellation, Supersession & Stale-Action Safety

**Question:** Can AEGIS cancel or supersede an obligation without accidentally resurrecting stale authority or rewriting historical world evidence?

**Why it matters:** cancellation changes current authority; it does not erase already-created objects or historical facts. Supersession must prevent old generations from acting again.

**Evidence required:** cancellation tests; post-cancellation observation; supersession races; stale-generation command attempts; partial execution; repeated retry attempts.

**Closure criterion:** stale actions are rejected, current authority remains unique, and historical effects remain attributable.

**Severity:** P1.

**Owner:** Commitment / Execution / Verification.

**Dependencies:** Q-04, Q-08, Q-09, Q-16.

**Architecture reopen:** Yes if safe cancellation/supersession cannot be represented while preserving the existing authority boundary.

### Q-11 — Concurrency, Shared Obligations & Resource Races

**Question:** What happens when multiple objectives, candidates, commitments, or production demands simultaneously depend on the same resources, producers, queues, or world objects?

**Why it matters:** feasibility observed by one subsystem can become false before execution; two valid-looking decisions can conflict without either subsystem being individually wrong.

**Required distinctions:** observation of availability versus reservation/obligation; resource state versus obligation; capacity versus allocation; commitment versus resource ownership.

**Evidence required:** simultaneous-demand tests; resource depletion races; producer contention; duplicate commitment tests; shared-contributor capability tests.

**Closure criterion:** contention is visible to the correct owner, no subsystem gains hidden reservation authority, and race outcomes remain attributable.

**Severity:** P1.

**Owner:** Resource Portfolio / Production Capacity / Commitment interfaces; Systems Assurance for cross-system integrity.

**Dependencies:** Q-03, Q-04, Q-09, Q-16, Q-27.

**Architecture reopen:** Only if safe cross-system behavior requires a new load-bearing authority not present in the architecture.

### Q-12 — Runtime Cost, Bounded Work & Qualification Budget

**Question:** Can the required evidence and control logic execute within a bounded cost without starving the AI or turning expensive search into a permanent control loop?

**Why it matters:** runtime latency is correctness. A logically correct subsystem that prevents timely decisions or execution is operationally incorrect.

**Required controls:** bounded candidate counts, bounded searches, cheap gates before expensive evidence, justified caching, controlled observation frequency, measured latency, and separation of fast/slow work.

**Evidence required:** per-primitive timing; repeated-cycle measurements; search-cost measurements; worst-case candidate counts; contention scenarios; slow-loop/fast-loop interference tests.

**Closure criterion:** each implementation path has an explicit runtime budget and evidence that its worst-case work is bounded enough for the target build.

**Severity:** P2 initially, P1 when a control loop depends on it.

**Owner:** Scheduler + Scientist + Systems Assurance.

**Dependencies:** Q-07, Q-09, Q-11.

**Architecture reopen:** Only if measured cost invalidates a load-bearing architectural topology rather than merely requiring optimization.

## 5. Cross-system gate ownership matrix

| Gate | WM | Belief | Situation | Obj | Planning | Decision | Commitment | Execution | Verification | Recovery | Resource | Production | Capability | Force Comp | Conversion |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q-01 Build | I | I | I | I | I | I | I | P | V | I | I | I | I | I | I |
| Q-02 ABI | I | I | I | I | I | I | I | P | V | I | I | I | I | I | I |
| Q-03 Ownership | P | I | I | P | I | P | P | P | V | I | I | I | I | I | I |
| Q-04 Identity/gen | I | I | I | I | I | I | P | P | V | I | I | I | I | I | I |
| Q-05 Scope/freshness | P | P | P | P | I | I | I | I | V | I | I | I | I | I | I |
| Q-06 Unknown/zero | P | P | P | I | I | I | I | I | V | I | I | I | I | I | I |
| Q-07 Search | P | I | I | I | I | I | I | P | V | I | I | I | I | I | I |
| Q-08 Publication | P | P | P | P | P | P | P | P | V | P | P | P | P | P | P |
| Q-09 Lifecycle | P | I | I | I | I | I | P | P | V | I | I | P | P | I | P |
| Q-10 Cancel/supersede | I | I | I | I | I | I | P | P | P | P | I | I | I | I | I |
| Q-11 Concurrency | I | I | I | I | I | I | P | P | V | P | P | P | P | P | P |
| Q-12 Runtime | I | I | I | I | I | I | I | P | V | P | I | P | I | I | P |

Legend: **P** = primary publisher/owner; **V** = verification authority; **I** = material input/consumer.

## 6. Subsystem mapping

The fifteen completed architecture closures are retained as independent contracts:

1. World Model
2. Belief Model
3. Situation Analysis
4. Objectives
5. Planning
6. Decision
7. Commitment
8. Execution
9. Verification
10. Recovery
11. Resource Portfolio
12. Production Capacity
13. Capability Factory
14. Force Composition
15. Production / Economic Conversion

Their recurring empirical questions now map primarily to Q-01 through Q-12. This prevents duplicated qualification programs while preserving subsystem-specific behavior where necessary.

### Primary concentrations

- **World Model / Belief / Situation:** Q-05, Q-06, Q-07, Q-08.
- **Objectives / Planning / Decision:** Q-02, Q-03, Q-04, Q-05, Q-06, Q-08, Q-12.
- **Commitment / Execution / Verification / Recovery:** Q-04, Q-08, Q-09, Q-10, Q-11, Q-12.
- **Resource Portfolio / Production Capacity:** Q-06, Q-07, Q-09, Q-11, Q-12.
- **Capability Factory / Force Composition / Conversion:** Q-02, Q-04, Q-05, Q-06, Q-08, Q-11, Q-12.

## 7. Cross-system objections resolved by consolidation

### Objection A — “Every subsystem has its own identity/generation problem.”

**Resolution:** No. Identity and generation are shared machine semantics. Q-04 qualifies the common mechanism; subsystem contracts specify only what identity they need.

### Objection B — “Every subsystem needs its own database/state manager.”

**Resolution:** Rejected. The repeated question is representation and publication, not justification for a universal state manager.

### Objection C — “UNKNOWN needs a universal manager.”

**Resolution:** Rejected. UNKNOWN is a semantic state whose representation must be qualified where consequential. Q-06 governs the machine distinction.

### Objection D — “Search behavior should be hidden behind a permanent abstraction.”

**Resolution:** Rejected. Search is an engine primitive with cost and quirks. Q-07 qualifies the exact search contracts used by each consumer.

### Objection E — “Resource races require a reservation subsystem.”

**Resolution:** Not established. Q-11 first determines whether engine/Aegis obligations can safely expose the needed behavior. Reservation authority is not granted merely because contention exists.

### Objection F — “Atomic publication requires an atomic engine primitive.”

**Resolution:** Not assumed. Q-08 qualifies a semantic publication protocol. The register prohibits claiming hardware/engine atomicity without evidence.

### Objection G — “A command is successful because the engine accepted the command syntax.”

**Resolution:** Rejected. Q-09 explicitly separates issuance, acceptance, pending, creation, availability, deployment, and effectiveness.

### Objection H — “A failed search proves absence.”

**Resolution:** Rejected unless the exact search semantics and completeness are qualified. Q-06 and Q-07 jointly govern this distinction.

### Objection I — “Runtime optimization can come later.”

**Resolution:** Partly rejected. Optimization can wait; bounded cost cannot. Q-12 treats runtime budget as an engineering correctness constraint.

## 8. Relationship to the existing ABI work

Layer 2 remains closed as the static ABI closure. This register does not alter the Layer-2 namespace decision and does not allocate runtime channels.

The established candidate scalar-goal namespace of `10000–15999` remains a qualification candidate, not a blanket license to use every slot. Operation-specific legal ranges and typed semantics remain governed by Q-02.

Stock goals, strategic numbers, timers, facts, and other channels remain stock territory unless independently cleared by the ABI process. The collision map is an input, not a waiver.

## 9. Qualification sequencing

### Phase 0 — Baseline fingerprint

Q-01: executable/build/profile/source closure.

### Phase 1 — Scalar ABI and channel safety

Q-02 + Q-03: typed identity, ranges, ownership, collision, writer/reader map.

### Phase 2 — Observation/search semantics

Q-05 + Q-06 + Q-07: scope, freshness, unknown/zero, search isolation, result multiplicity.

### Phase 3 — World-transition semantics

Q-09 + Q-10: command acceptance, pending/created/available, cancellation, supersession.

### Phase 4 — Cross-system publication

Q-04 + Q-08: identity/generation propagation and coherent publication.

### Phase 5 — Concurrency

Q-11: shared resources, producer contention, concurrent commitments, shared contributors.

### Phase 6 — Performance

Q-12: bounded searches, timing, fast/slow loop separation, evidence cost.

### Phase 7 — Controlled vertical slice

Only after the prerequisite gates for the slice are qualified. The first intended vertical slice remains **Cavalry Threat Containment**, because it crosses observation, belief/situation, objectives, planning, decision, commitment, production/capability, execution, verification, and recovery without requiring the entire bot to exist.

## 10. Qualification evidence states

Every gate should advance through explicit evidence states rather than a binary “done” flag:

`HYPOTHESIS → DOCUMENTED → ARCHAEOLOGICALLY SUPPORTED → TARGET-BUILD QUALIFIED → IMPLEMENTATION QUALIFIED → RUNTIME VALIDATED → REPLAY CORROBORATED → BATTLEFIELD VALIDATED`

A lower state must never be presented as a higher state.

## 11. Closure-integrity rules

1. A subsystem marked CLOSED — ARCHITECTURE remains closed unless evidence falsifies a load-bearing architectural claim.
2. An unproven machine representation is not automatically an architecture defect.
3. A machine test that contradicts a load-bearing contract reopens the smallest owning subsystem/pass necessary.
4. Later knowledge may challenge earlier closure but must not silently rewrite history.
5. Direct engine evidence outranks duplicated AEGIS state.
6. Historical documentation is evidence, not target-build proof.
7. Validator behavior is evidence about the validator, not automatically proof about runtime.
8. Runtime behavior is evidence about the build/configuration under test, not automatically universal semantics.
9. Numeric identity never substitutes for semantic identity.
10. One semantic state has one authoritative publisher.
11. Unknown remains unknown until qualified evidence resolves it.
12. Search failure is not automatically absence.
13. Command issue is not acceptance; acceptance is not completion; completion is not effectiveness.
14. Cancellation does not erase history.
15. Supersession does not rewrite prior world evidence.
16. Resource obligation is not resource state.
17. Capability is not unit count.
18. Force composition is not a universal counter matrix.
19. Feasibility is not desirability.
20. Decision is not Commitment.
21. Commitment is not Execution.
22. Execution is not Verification.
23. Verification is not strategic success.
24. Runtime cost is part of correctness.
25. No new universal manager is justified merely because a shared question exists.

## 12. Exit criteria for this register

The register itself is complete enough to govern engineering when:

- every recurring cross-system machine question has a single Q-ID;
- each Q-ID has an owner;
- each Q-ID has an evidence requirement;
- each Q-ID has a closure criterion;
- each Q-ID has a severity;
- each Q-ID has explicit architecture-reopen conditions;
- all fifteen closed subsystem contracts can map their deferred questions into the shared gates;
- no shared gate silently grants ABI allocation or runtime authority.

This document therefore does **not** require every gate to be experimentally closed before the register is considered structurally complete. It requires the engineering obligation to be unambiguous.

## 13. Immediate engineering decision

The completed subsystem architectures should not be reopened merely to repeat the same empirical questions under fifteen different names.

The next engineering work should use this register as the shared qualification backbone, beginning with build identity and typed ABI qualification, then search/fact semantics, then lifecycle/acceptance semantics, then identity/publication, concurrency, and performance.

Execution should receive a fresh five-pass review under the current five-person standard, but its Scientist and Assurance work should consume this shared qualification register rather than recreating a separate universe of machine questions.

## 14. Final status

**CROSS-SYSTEM OBJECTION & QUALIFICATION REGISTER — ACTIVE / GOVERNING**

Architecture closures preserved.  
Shared machine questions consolidated.  
No universal state manager introduced.  
No ABI channels allocated by this register.  
No runtime implementation authorized by this register.
