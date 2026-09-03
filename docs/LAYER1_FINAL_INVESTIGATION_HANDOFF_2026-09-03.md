# AEGIS Layer 1 — Final Investigation Handoff

**Date:** 2026-09-03  
**Layer:** Layer 1 — Machine Understanding  
**Working completion position:** **89%**  
**Investigation status:** **CLOSED / HANDOFF**  
**Completion status:** **NOT CERTIFIED COMPLETE**

## 1. Executive conclusion

The Layer 1 investigation is now closed as an investigation phase. It is not being declared 100% complete. The project has reached a stable, evidence-bounded machine model sufficient to hand the work forward without relying on conversational memory, while the remaining 11% is concentrated in a small number of implementation-level causal closures that were deliberately not fabricated.

The central achievement of the investigation is methodological as much as substantive. The project progressed from script vocabulary and replay observation, through native source/debug archaeology, PE-aware address mapping, Ghidra validation, targeted disassembly, and negative-evidence analysis, to an independent native function-coordinate layer derived from PE `.pdata`. The resulting model distinguishes machine facts from source contracts, observations, inferences, hypotheses, and historical artifacts.

The final position is therefore:

`KNOWN MACHINE SURFACE -> BOUNDED CAUSAL MODEL -> EXPLICIT OPEN IMPLEMENTATION EDGES -> NO UNACKNOWLEDGED COMPLETION CLAIM`

This is the correct stopping point for the investigation phase.

## 2. Authoritative runtime identity

All native conclusions are scoped to the controlled executable:

- File: `AoE2DE_s.exe`
- Version: `101.103.48987.0`
- Size: `71,648,568` bytes
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Image base: `0x140000000`
- Architecture: PE32+, x86:LE:64 Windows

The local installation path is intentionally redacted from public documentation. Native addresses and structures must not be generalized to another executable build without re-verification.

## 3. What is established

### 3.1 AI script substrate

The executable and installed AI material establish a `.ai/.per` rule-oriented AI substrate. Native vocabulary includes rule loading, lexical/preprocessor errors, constants, facts, actions, rule IDs, priorities, minimum/maximum intervals, sorted rules, rule groups, persistent facts, breakpoints, and execution diagnostics.

### 3.2 Rule representation and scheduler surface

The native corpus establishes the existence of rule-oriented state including current rule IDs, priority, interval state, sorted-rule structures, rule groups, and lifecycle controls. It does not yet establish the exact scheduler comparator, rebuild algorithm, interval mathematics, or all state ownership relationships.

The engineering consequence is firm: lexical order cannot be assumed to equal execution order, and scheduler state must be treated as a real machine subsystem rather than as a textual property of the `.per` file.

### 3.3 AI fact semantic layer

The native corpus contains an explicit `Init AI Facts` diagnostic boundary followed by comparison and player-scope vocabulary, including `less-than`, `less-or-equal`, `greater-than`, `greater-or-equal`, `not-equal`, `any-*`, `every-*`, and `this-*` forms. Game-mode, player, civilization, map-size, victory, starting-age, difficulty, resource-setting, and processing-mode vocabulary also appears around game-start and AI-fact initialization.

This establishes a semantic initialization surface. It does not establish that every symbol is stored in one table or initialized by one function.

### 3.4 Persistent facts

The highest-value remaining rule-engine boundary is:

`Evaluating Persistent Facts`
-> fact evaluation
-> `Fact[%d] evaluated persistently to %s`
-> `Finished Evaluating Persistent Facts`

This is native-vocabulary/diagnostic evidence for a distinct persistent-fact evaluation phase. The exact evaluator function, result storage, cache lifetime, invalidation policy, and scheduler cadence remain unresolved.

### 3.5 Feasibility versus desirability

Native vocabulary contains explicit validation and feasibility concepts, including build/research/train feasibility and invalid-object/invalid-argument diagnostics. The strongest practical architectural conclusion is:

`strategic desirability -> native feasibility -> execution -> observed result -> reconciliation`

The machine can determine whether an operation is executable under engine semantics; the strategic layer must determine whether that operation is desirable.

### 3.6 UnitAI

The native AI corpus contains separate vocabulary for `CurrentOrder`, `CurrentAction`, target state, target type, target position, notification processing, idle processing, order queues, notification queues, search, retryable orders, retargeting, better-target selection, action completion, action failure, invalidation, and search-required conditions.

This supports a strong architectural model of distinct order, action, target, notification, search, and recovery concerns. It does not yet prove their exact C++ class hierarchy or field ownership.

### 3.7 Native tactical search

Search diagnostics expose LOS, search radius, object-interest filters, ownership classification, defend-target restrictions, pathability, attack range, walls, current-target retention, and best-target selection. The practical implication is that tactical target acquisition is already a substantial native capability. ByzBot should not duplicate this machinery without a demonstrated strategic reason.

### 3.8 Object identity

Native vocabulary includes unit/object/copy/class/type/owner/game/unique identity concepts and garrison/availability/validity operations. Concrete unit IDs, unit-line IDs, and class IDs must be treated as distinct namespaces. Numeric equality is not semantic identity.

A complete creation -> lookup -> transformation -> garrison -> removal identity chain was not recovered. Replay references remain observations rather than proof of a specific native identity namespace unless independently corroborated.

## 4. The `.pdata` breakthrough

The final native archaeology method uses the executable's PE `.pdata` as an independent function-coordinate system.

The controlled build contains **166,741 physical 12-byte runtime-function slots**, of which **166,730 are non-zero valid runtime-function records** and **11 are trailing zero padding**. Valid starts are unique and monotonically ordered, and no overlaps were found among the valid runtime-function intervals.

Measured function interval statistics:

- minimum: 1 byte;
- median: 91 bytes;
- mean: 275.17 bytes;
- maximum: 106,696 bytes;
- aggregate interval coverage: 45,879,189 bytes;
- coverage: approximately 88.88% of `.text` raw size.

This does not mean the executable has 166,730 semantically meaningful source-level functions. It means that native code can be partitioned into mechanically bounded runtime-function regions without depending on guessed function boundaries.

This is now the preferred structural substrate for future native archaeology.

## 5. CodeView/PDB discovery

The PE debug directory contains CodeView type 2 data with:

- signature: `RSDS`;
- PDB GUID: `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`;
- PDB age: `1`;
- embedded path ending in `AoE2DE_s.pdb` under the build system's PhoenixBuilders path.

No matching PDB was found in the user's home directory. A full `C:\` search encountered access-denied locations and did not establish a matching local PDB.

The PDB is therefore an **authorized-future lead, not current evidence**. A matching PDB authenticated by GUID and age could substantially improve function and line attribution, but it must not be substituted casually or treated as authoritative merely because filenames match.

## 6. Direct AI-string reference tests

The corrected section-aware mapping was used for direct reference tests against seven exact AI diagnostic/source anchors, including `UnitAIModule.cpp`, `TribeUnitAIModule.cpp`, `CurrentAction`, `currentTargetID`, `currentTargetType`, `processNotify`, and `ai::search`.

The complete `.text` region was tested for RIP-relative references to those exact `.rdata` addresses. No such references were found. The complete executable image was also tested for exact 64-bit little-endian pointer occurrences of those addresses; none were found.

This is a bounded negative result for those representations. It does not establish that the corresponding AI code is absent, unused, or unreachable. It establishes that those seven strings are not straightforward direct anchors under the tested reference representations, strengthening the possibility of debug/source/metadata storage or indirect/table-mediated access.

## 7. The false-positive that must be remembered

A correctly section-mapped metadata-area field was found to contain `0x1417FF3E0`, an address recognized by `.pdata` as a real function start. Direct disassembly of the target function showed cleanup/destructor-like behavior: object-field initialization/cleanup, pointer-array iteration, release operations, and conditional freeing.

The candidate was therefore **rejected** as an XS API implementation association.

This is a critical methodological result:

`metadata proximity + valid pointer + valid function boundary != semantic API ownership`

Future archaeology must independently demonstrate caller/callee relationships, data ownership, and state effects before assigning semantic ownership.

## 8. Ghidra status

The historical Pass33 workspace remains preserved and must not be overwritten. Its logs demonstrate substantial analysis activity but also significant function-body repair noise.

The separate controlled headless analysis against the exact executable successfully imported and saved the executable into the controlled project, but the broad analysis did not terminate cleanly. The run reached the `Disassemble Entry Points` stage, emitted a `CreateThunkFunctionCmd` / `body must contain the entry point` error, and timed out at 1800 seconds. It nevertheless saved the imported program.

Therefore:

- import: established;
- project creation/save: established;
- full clean analysis completion: **not established**;
- all Ghidra auto-generated function bodies: **not automatically trusted**;
- targeted `.pdata`-bounded native work: preferred future method.

The correct interpretation is not that Ghidra failed and therefore native archaeology failed. The correct interpretation is that broad auto-analysis is an imperfect index-generation mechanism, while targeted native verification remains viable.

## 9. Why the investigation stops at 89%

The remaining 11% is not a generic request for “more research.” It is concentrated in implementation-level causal closure:

1. verified rule-loader/parser boundary;
2. verified rule representation ownership/mutation;
3. verified persistent-fact result mutation and freshness boundary;
4. verified scheduler ordering and interval transition path;
5. verified rule/handler-to-native-action bridge;
6. verified `CurrentOrder -> CurrentAction` mutation chain;
7. verified action failure/invalidation/completion propagation;
8. at least one experimentally predictive `.per` end-to-end path.

No implementation-level edge was promoted merely because the vocabulary strongly suggested it.

This is why 89% is the correct final investigation position rather than 95%, 98%, or 100%.

## 10. Predictive machine standard

The critical standard remains:

`PRECONDITION -> TRIGGER -> DISPATCH -> PROCESSING -> STATE TRANSITION -> POSTCONDITION`

A native mechanism should not be considered predictively understood until a sufficiently specified state/input can be traced through the relevant machine layers and its next meaningful state can be predicted. For critical mechanisms, the preferred evidence is a verified function boundary plus state read/write, branch/call relationship, downstream consumer, and—where practical—a runtime falsification test.

## 11. Practical architecture handed forward

The most defensible ByzBot architecture is:

`OBSERVATION`
`-> BELIEF / MACHINE FACTS`
`-> `STRATEGIC INTENT`
`-> `TACTICAL REQUEST`
`-> `NATIVE VALIDATION / ACCEPTANCE`
`-> `EXECUTION`
`-> `OBSERVED RESULT`
`-> `RECONCILIATION`
`-> `RETAIN / RETRY / RETARGET / REPLACE / ABANDON`

This is an architecture derived from convergent evidence and engineering reasoning, not a claim that the shipped engine literally implements these exact software classes.

The central design principle is division of responsibility: ByzBot should own strategic valuation, prioritization, Byzantine doctrine, opportunity cost, long-horizon planning, conflict arbitration, and reconciliation policy; the native engine should be exploited for feasibility, tactical search, pathing, target management, action execution, and recovery wherever those capabilities meet the strategic requirement.

## 12. Temporal model: hypothesis, not fact

The evidence suggests three potentially distinct state cadences:

- strategic/rule cadence: facts, goals, strategic numbers, scheduler state;
- tactical/unit cadence: orders, actions, target retention, notifications, search/recovery;
- simulation cadence: movement, combat, production, object mutation.

This is a useful hypothesis because it predicts stale observations, command latency, and asynchronous tactical recovery. It remains explicitly unproven until scheduler and state-mutation paths are recovered or a runtime experiment distinguishes competing models.

## 13. Evidence failures that are now part of institutional memory

The following approaches were explicitly downgraded or retired:

- treating strings as direct call-graph anchors;
- treating raw `VA - imagebase` as a universal file offset;
- trusting malformed or repair-heavy decompiler output without independent boundary validation;
- treating a metadata pointer's proximity to an API signature as semantic ownership;
- treating zero direct references as proof of absence;
- treating replay identifiers as automatically identical to native object identifiers;
- treating validator behavior as equivalent to runtime semantics;
- treating historical source material as automatically shipped-runtime implementation.

These are not embarrassing dead ends to hide. They are negative knowledge that prevents future engineers from repeating expensive errors.

## 14. Six-month recovery protocol

An engineer returning after six months should:

1. read `README.md`;
2. read `RESEARCH_INDEX.md`;
3. read this handoff;
4. read `docs/LAYER1_COMPLETION_CONTROL_2026-09-02.md`;
5. read `docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`;
6. read `docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md`;
7. read the native archaeology log and QC addenda;
8. read the AIExpert/UnitAI and `.pdata` passes;
9. inspect `knowledge/LAYER1_MACHINE_FACTS.jsonl` and `knowledge/MACHINE_INVESTIGATION_HISTORY.jsonl`;
10. inspect `docs/OPEN_NATIVE_QUESTIONS_LAYER1.md`;
11. treat the 89% position as authoritative until new evidence changes it;
12. resume from the explicit implementation-closure gaps rather than restarting vocabulary collection.

## 15. Final engineering disposition

Layer 1 investigation is **closed at 89%**. The machine model is mature enough to inform subsequent ByzBot engineering, but the predictive completion gate remains unsatisfied. No future implementation should silently promote the remaining hypotheses to facts.

If the project resumes native archaeology, the highest-value target is the first verified state mutation in either persistent-fact evaluation or `CurrentOrder -> CurrentAction`, followed immediately by its downstream consumer and a falsification experiment.

If the project resumes implementation work before that native closure, the implementation must explicitly label every dependency on unresolved Layer 1 behavior and isolate those assumptions behind replaceable interfaces.

**Final position: substantial machine understanding, disciplined uncertainty, strong strategic architecture, and a precisely bounded remaining native frontier.**
