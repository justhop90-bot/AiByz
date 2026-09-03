# AEGIS Layer 1 Machine Knowledge Monograph — Final Investigation Baseline

**Status:** Public-safe operational knowledge baseline; Layer 1 investigation closed for handoff at **89%**; completion gate remains unsatisfied.  
**Purpose:** Preserve enough machine understanding that a future engineer can reconstruct the operational model without relying on conversational memory.  
**Authority:** Derived from controlled AEGIS investigations, runtime identity evidence, archived forensic passes, script evidence, qualified source-contract artifacts, and PE-structural analysis.

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

## 3. Script substrate

The AI system consumes `.ai` profile/entry configuration and `.per` rule material. The script layer is a rule-programming substrate whose declarations become runtime rule structures and whose actions mutate AI state or request engine operations.

The current operational abstraction is:

`AI profile -> script acquisition -> interpretation/compilation -> rule representation -> registration -> scheduling -> trigger evaluation -> handler/action execution -> state/world consequence -> next evaluation cycle`

The exact native boundaries remain partly unresolved. Source archaeology did not recover complete definitions for several high-value BXS symbols, so those names remain vocabulary/diagnostic evidence rather than reconstructed source implementations.

## 4. Scheduler model

Native vocabulary supports rule identity, priority, minimum/maximum intervals, enabled/disabled state, rule groups, sorted rule collections, current sorted position, rule counts, and scheduler validation/failure diagnostics.

Runtime execution order must not be modeled as simple lexical source order. Exact comparator behavior, interval mathematics, rebuild triggers, fairness, and starvation remain implementation questions.

## 5. AI fact semantic layer

The native corpus contains an explicit `Init AI Facts` boundary, comparison operators, player-scope forms, game-state/environment vocabulary, feasibility predicates, and a distinct persistent-fact evaluation phase.

The persistent-fact diagnostic sequence remains:

`Evaluating Persistent Facts -> Fact[%d] evaluated persistently to %s -> Finished Evaluating Persistent Facts`

The existence of this phase is confirmed at vocabulary level. Cache lifetime, refresh cadence, result storage, and snapshot semantics remain open.

## 6. UP observation and feasibility

Recovered UP vocabulary includes fact retrieval and aggregation, focus/player/target facts, object/type/target information, path distance, terrain/elevation/zone, timers, signals, goals, strategic numbers, resource state, pending objects, research status, and engine-feasibility predicates such as build/research/train checks.

The resulting architecture is:

`observation -> representation -> strategic decision -> feasibility -> authorized request -> execution -> result -> verification`

Feasibility is an execution gate, not a strategic objective function.

## 7. Search/filter state

UP exposes reset, filter, create, and find operations. Native AI vocabulary also exposes LOS, search radius, ownership classification, object-interest filtering, defend-target restrictions, pathability, attack range, walls, current-target retention, and better-target selection.

Search should therefore be treated as a stateful machine capability with explicit query context. ByzBot should delegate tactical search where the native capability meets the strategic requirement.

## 8. UnitAI

The native corpus exposes separate vocabulary for `CurrentOrder`, `CurrentAction`, target state, target type/position, notification processing, idle processing, order queues, notification queues, search, retryable orders, retargeting, better-target selection, completion, failure, invalidation, and search-required states.

The strongest current model is:

`durable order intent -> action execution -> target/search management -> completion/failure/invalidation -> recovery or replacement`

This remains a strong architectural inference until a verified native mutation chain is recovered.

## 9. Identity and lifecycle

Native vocabulary distinguishes unit, object, copy, class, type, owner, game, and unique identity concepts. Numeric equality is not namespace equality. Replay references are observations, not automatic proof of native identity.

Object lifecycle must distinguish observation, creation, active state, transformation, garrison, ownership change, deletion/destruction, reuse, and observation loss. Production must distinguish request, queue admission, start, completion, object birth, and deployment.

## 10. Action and failure model

The machine exposes action completion, failure, invalidation, search requirements, target changes, and pathability constraints. Therefore:

`proposal != commitment != authorization != execution != success`

A command emitted by AI code is not proof of execution, and execution is not proof of strategic success. Failure and recovery must be first-class architectural states.

## 11. Native function geometry — final major structural result

The controlled PE `.pdata` contains 166,741 physical 12-byte runtime-function slots. 166,730 contain non-zero runtime-function records and 11 are trailing zero padding. Valid starts are unique and monotonically ordered; no interval overlaps were found among valid ranges.

Function interval statistics are: minimum 1 byte, median 91 bytes, mean 275.17 bytes, maximum 106,696 bytes. Aggregate valid interval coverage is 45,879,189 bytes, approximately 88.88% of `.text` raw size.

This does not mean the binary contains 166,730 semantically meaningful source-level functions. It provides a mechanically bounded coordinate system for targeted native archaeology and an independent cross-check against fragile disassembler function inference.

## 12. CodeView/PDB

The PE debug directory contains CodeView `RSDS` data with PDB GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d` and age `1`, with an embedded build-system path ending in `AoE2DE_s.pdb`. No matching local PDB was established. A future PDB is usable only after GUID/age authentication against the controlled executable.

## 13. Native reference negative evidence

Full `.text` Capstone scanning found zero RIP-relative references to seven selected AI diagnostic/source anchors, including `UnitAIModule.cpp`, `TribeUnitAIModule.cpp`, `CurrentAction`, `currentTargetID`, `currentTargetType`, `processNotify`, and `ai::search`. Executable-wide exact 64-bit pointer scanning also found zero occurrences for those addresses.

This eliminates the tested direct representations. It does not establish absence of the underlying AI code or prove indirect/table-mediated access.

## 14. Metadata-pointer false-positive control

A correctly section-mapped metadata-area field pointed to `0x1417FF3E0`, which is a valid `.pdata` function start. Direct disassembly showed cleanup/destructor-like behavior, so the association was rejected as an XS API implementation.

The permanent rule is:

`metadata proximity + valid pointer + valid function boundary != semantic ownership`

Semantic ownership requires caller/callee, data-flow, state-effect, or equivalent independent evidence.

## 15. Ghidra boundary

Historical Pass33 remains preserved. It contains real analysis activity but substantial function-body repair noise. The separate controlled headless run imported and saved the exact executable but timed out at 1800 seconds during `Disassemble Entry Points` with a `CreateThunkFunctionCmd` / `body must contain the entry point` error.

Broad Ghidra analysis is therefore treated as index generation, not automatic semantic proof. Targeted `.pdata`-bounded verification is the preferred native method.

## 16. Programmer-intent reconstruction

For significant mechanisms, AEGIS separates observed mechanism, engineering constraint, plausible rationale, supported programmer intent, and AI architectural implication. Repeated data ownership, state lifetime, caller/callee structure, boundary placement, error handling, performance structures, and runtime consequences can strengthen intent claims. When evidence cannot distinguish alternatives, competing hypotheses remain explicit.

## 17. Predictive completion standard

Layer 1 requires critical causal paths to approach:

`PRECONDITION -> TRIGGER -> DISPATCH -> PROCESSING -> STATE TRANSITION -> POSTCONDITION`

The endpoint is predictive: given sufficiently specified state and input, the investigator should be able to predict the relevant machine transition and then test that prediction. The investigation stopped at 89% because the final implementation-level causal edge was not demonstrated.

## 18. Final architecture handed forward

The most defensible ByzBot authority model is:

`OBSERVATION -> BELIEF / MACHINE FACTS -> STRATEGIC INTENT -> TACTICAL REQUEST -> NATIVE VALIDATION / ACCEPTANCE -> EXECUTION -> OBSERVED RESULT -> RECONCILIATION -> RETAIN / RETRY / RETARGET / REPLACE / ABANDON`

This is an engineering architecture derived from convergent evidence, not a claim that the shipped engine literally implements these exact classes.

ByzBot should own strategic valuation, prioritization, Byzantine doctrine, opportunity cost, long-horizon planning, conflict arbitration, and reconciliation policy. Native machinery should be exploited for feasibility, tactical search, pathing, target management, action execution, and recovery where appropriate.

## 19. Final unresolved frontier

The remaining 11% is concentrated in:

- rule-loader/parser implementation boundary;
- rule-representation ownership and mutation;
- persistent-fact result mutation and freshness/cache semantics;
- scheduler comparator and interval transitions;
- rule/handler-to-native-action bridge;
- `CurrentOrder -> CurrentAction` mutation;
- action failure/invalidation/completion propagation;
- required object identity lifecycle edges;
- one predictive end-to-end `.per` path.

These are implementation-closure problems, not invitations to restart vocabulary collection.

## 20. Re-entry

A future engineer should read `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`, the final project status, the predictive standard, completion control, evidence matrix, native archaeology/QC documents, open questions, and atomic knowledge ledgers before changing architecture.

The final investigation position is **89%**. It remains deliberately below completion until the predictive gate is satisfied.
