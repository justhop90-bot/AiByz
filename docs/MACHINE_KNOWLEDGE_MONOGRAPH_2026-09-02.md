# AEGIS Layer 1 Machine Knowledge Monograph

**Status:** Public-safe operational knowledge baseline; native evidence remains subject to the Layer 1 evidence and publication gates.
**Purpose:** Preserve enough machine understanding that a future engineer can reconstruct the operational model without relying on conversational memory.
**Authority:** Derived from controlled AEGIS investigations, runtime identity evidence, archived forensic passes, script evidence, and qualified source-contract artifacts.

## 1. Epistemic rule

This document is not a claim of total reverse engineering. A symbol string establishes vocabulary, not semantics. A source declaration establishes a contract surface. A method body establishes implementation. A call site establishes a relationship. An assignment establishes a state transition. A controlled runtime experiment establishes behavior. Independent convergence upgrades confidence. Where evidence stops, the claim remains an inference or hypothesis.

Evidence classes:

1. **RUNTIME-IDENTITY** — verified executable identity.
2. **SCRIPT-CONSUMED** — behavior demonstrably consumable by the AI script layer.
3. **NATIVE-VOCABULARY** — embedded names, diagnostics, or signatures.
4. **SOURCE-CONTRACT** — independent source/archive material describing an interface or contract.
5. **NATIVE-IMPLEMENTATION** — verified native function body, call relationship, field access, or state transition.
6. **RUNTIME-EXPERIMENT** — controlled execution demonstrating a proposition.
7. **INFERENCE** — constrained interpretation from convergent evidence.
8. **HYPOTHESIS** — plausible but insufficiently demonstrated explanation.
9. **HISTORICAL** — contextual evidence whose relationship to the current runtime is not established.

Evidence strength and publication permission are independent. An accurate native observation can remain restricted.

## 2. Runtime identity

The controlled native runtime is identified by:

- executable: `AoE2DE_s.exe`;
- version: `101.103.48987.0`;
- size: `71,648,568` bytes;
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`;
- PE machine: `0x8664`;
- PE format: PE32+ / 64-bit;
- observed section count: 8.

The exact local installation path is intentionally excluded from the public record. Build identity is fixed by version, size, and cryptographic hash.

Evidence from another executable, another build, a development archive, or a historical source package must not silently inherit this identity.

## 3. Script substrate

The AI system consumes `.ai` profile/entry configuration and `.per` rule material. The script layer is a rule-programming substrate whose declarations become runtime rule structures and whose actions mutate AI state or request engine operations.

The current operational abstraction is:

`AI profile -> script acquisition -> interpretation/compilation -> rule representation -> registration -> scheduling -> trigger evaluation -> handler/action execution -> state/world consequence -> next evaluation cycle`

The exact native boundaries remain partly unresolved. Source archaeology did not recover complete definitions for several high-value BXS symbols, so those names remain vocabulary/diagnostic evidence rather than reconstructed source implementations.

## 4. Scheduler model

Native vocabulary supports a rule system containing concepts corresponding to:

- rule identity and validity;
- priority;
- minimum and maximum intervals;
- enabled/disabled state;
- rule groups;
- sorted rule collections;
- current sorted position;
- rule counts;
- scheduler validation and failure diagnostics.

The safest conclusion is that runtime execution order is not safely modeled as simple lexical source order. Priority, interval, grouping, and sorting are machine-level scheduling concepts.

Exact comparator behavior, interval mathematics, and rebuild triggers remain implementation questions until directly demonstrated.

## 5. Dynamic rule control

Native vocabulary exposes rule and rule-group lifecycle controls and dynamic priority/interval operations. These observations support a machine model in which rule lifecycle and scheduling metadata are script-addressable concepts.

They do not alone establish legal ranges, ordering direction, timing units, or behavior in every rule state. Those propositions require implementation or controlled experimental evidence.

## 6. Scheduler failure model

Native diagnostics expose multiple validation boundaries, including invalid rule IDs, duplicate scheduling metadata, rule-group construction failures, sorted-rule insertion failures, interpretation failures, and compilation/sorting failures.

Engineering consequence:

> malformed scheduler state and execution failure are machine fault classes, not impossible conditions.

AEGIS must therefore model fault detection, containment, recovery, and verification rather than assuming every accepted command succeeds.

## 7. State substrate

The machine exposes a distributed AI state substrate involving facts, goals, strategic numbers, timers, search/filter state, object/group state, player/enemy information, and engine-mediated actions.

Goals, strategic numbers, timers, and facts are not interchangeable merely because they are represented numerically. Their architectural meaning must be inferred from reads, writes, lifecycle, and downstream consequences.

## 8. UP observation and actuation

Recovered UP vocabulary includes fact retrieval and aggregation, focus/player/target facts, object/type/target information, path distance, terrain/elevation/zone, timers, signals, shared and indirect goals, resource amounts/percentages, pending objects, research status, and engine-feasibility predicates such as build, research, and train checks.

The resulting architecture is richer than static threshold logic:

`observation -> representation -> decision -> feasibility -> authorized action -> postcondition verification`

Engine feasibility should be treated as an explicit gate rather than inferred from resource totals alone.

## 9. Search/filter state

UP exposes reset, filter, create, and find operations. This supports an engine-side query workflow in which search/filter context is mutable state.

Architectural consequence:

> search procedures must establish their query context explicitly.

A rule that assumes search state is stateless can create nonlocal failures through stale filters or stale query context.

## 10. Identifier discipline

Native vocabulary distinguishes unit, object, copy, class, type, game, and unique identity concepts. The existence of names such as unit/object lookup operations and identity fields establishes a rich identity surface, but does not establish equality between the namespaces.

The governing rule is:

`unit ID != unit-line ID != class ID != object ID != copy ID != game ID != unique ID`

unless a specific relationship has been demonstrated.

The same rule applies to replay references: a numeric replay value is not automatically a native object ID.

## 11. Object lifecycle

The identity investigation models object lifecycle as:

`unknown -> observed -> created/inferred -> active -> state transitions -> terminal/non-observed state`

Relevant transitions include movement, gathering, combat, production, garrison, transformation, ownership change, deletion/destruction, and observation loss.

Absence from an observation is never sufficient to prove destruction. A missing object may be garrisoned, transformed, outside the observation boundary, filtered by a query, deleted, ownership-changed, or absent from parser output.

Production must likewise be distinguished into intent, queue admission, queued/started state, completion, object birth, availability, and deployment. A queue command is not a completion event.

## 12. Action execution

The machine distinguishes order/action/target state from result and postcondition. Native vocabulary exposes action completion, failure, invalidation, search requirements, target changes, pathability, and retargeting.

Therefore:

`PROPOSAL != COMMITMENT != AUTHORIZATION != EXECUTION != SUCCESS`

Command issuance is evidence that a request was made. It is not evidence that the machine accepted, completed, or achieved the intended strategic consequence.

## 13. Movement and targeting

Native action vocabulary demonstrates that geometry and pathability can invalidate an otherwise reasonable intent. Target selection is dynamic and may preserve, invalidate, or replace targets based on machine conditions.

AEGIS should therefore separate strategic target intent from native tactical target execution and should treat pathability/feasibility as execution-boundary evidence.

## 14. Production and research

Production is best represented as a capability pipeline:

`objective -> capability requirement -> composition -> capacity -> prerequisites -> resource demand -> feasibility -> action -> completion -> reinforcement/replacement`

Research is likewise a capability transition with feasibility, cost, status, expected return, and postcondition verification.

This architecture is materially safer than treating train/research statements as independent unconditional writes.

## 15. Economy as machine state

The machine exposes resource amounts, percentages, cost information, technology/research state, market operations, tribute, and gatherer-related state. The implication is that economic reasoning can be modeled as a state/deficit/opportunity-cost problem rather than a fixed worker-percentage table.

The strategic layer must still distinguish machine-observable facts from derived beliefs and policy judgments.

## 16. Error taxonomy

A useful cross-layer fault taxonomy is:

`parse/lexical -> rule construction -> registration/scheduling -> interpretation -> feasibility -> execution -> result -> postcondition verification`

A failure at one layer does not imply failure at another. In particular, successful command emission does not establish successful execution, and successful execution does not establish strategic success.

## 17. Replay boundary

Replay parsing is an observation instrument. It establishes what the recording encoded and what the parser decoded; it does not automatically expose complete internal simulation state.

For the reference recording, the forensic parser produced 6,858 ACTION records and 27,369 object-reference candidates spanning 4,411 distinct numeric values, with zero malformed JSON records after normalization. Some numeric values are implausibly large, so object identity remains explicitly unresolved.

The promotion rule is:

`replay observation -> cross-layer correlation -> native/runtime evidence -> identity claim`

not:

`numeric equality -> assumed identity`.

## 18. Ghidra boundary

Broad Ghidra analysis is treated as index generation, not semantic proof. Decompiler output, strings, addresses, symbols, and reference results require evidence classification and, for critical claims, targeted verification.

A previous disassembly-reference experiment was explicitly downgraded after its instruction substrate proved incomplete. Its zero-result reference count is therefore not executable-wide negative evidence.

Native archaeology proceeds by increasing representation fidelity:

`symbol -> defined data -> raw region -> instruction reference -> consumer -> implementation -> runtime corroboration`

## 19. Programmer-intent reconstruction

For significant mechanisms, AEGIS separates:

1. observed mechanism;
2. engineering constraint;
3. plausible design rationale;
4. supported programmer intent;
5. AI architectural implication.

Repeated patterns, data ownership, state lifetime, caller/callee structure, error handling, performance structures, source remnants, and runtime consequences may strengthen an intent hypothesis. When evidence cannot distinguish alternatives, competing hypotheses remain explicit.

## 20. Predictive completion criterion

Layer 1 is not complete because a vocabulary catalog is large. It is complete only when material AI-facing causal paths have no unacknowledged black boxes that could change implementation decisions.

For critical mechanisms the target trace is:

**PRECONDITION -> TRIGGER -> DISPATCH -> PROCESSING -> STATE TRANSITION -> POSTCONDITION**

The endpoint is predictive: given sufficiently specified state and input, the investigator should be able to predict the relevant machine transition and then test that prediction.

## 21. Public-safety boundary

This public document intentionally omits exact local installation paths and does not redistribute proprietary executables, DLLs, assets, bulk binary dumps, substantial decompiler output, private symbols, or copied source.

Native findings remain subject to the project's independent evidence and publication gates. A fact being technically accurate does not make every representation of that fact appropriate for public release.

The preferred public transformation is:

`source identity -> original observation -> evidence classification -> interpretation -> general principle -> AEGIS abstraction -> independent implementation -> validation`

## 22. Re-entry standard

A future engineer should be able to recover from this repository:

- authoritative runtime identity;
- evidence definitions;
- scheduler/state/action model;
- identity and lifecycle boundaries;
- replay limitations;
- Ghidra methodological limitations;
- programmer-intent reasoning boundaries;
- architectural consequences;
- unresolved questions and their promotion tests;
- publication/safety constraints.

If a claim cannot be traced to evidence, provenance, and an explicit confidence boundary, it is not a completed Layer 1 fact.
