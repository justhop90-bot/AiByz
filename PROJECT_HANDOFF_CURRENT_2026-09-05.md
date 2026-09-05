# AEGIS / AiByz — Professional Project Handoff

**Date:** 2026-09-05
**Project:** AEGIS / AiByz / ByzBot — next-generation Byzantine AI for Age of Empires II: Definitive Edition
**Canonical repository:** `justhop90-bot/AiByz`
**Authority:** GitHub `main`
**Target build:** AoE2DE `101.103.48987.0`
**Steam BuildID:** `24094652`
**Executable:** `AoE2DE_s.exe`

---

## 1. Mission

AEGIS is being engineered as a professional, evidence-driven expert system for AoE2DE rather than as a conventional `.per` script assembled by trial and error.

The project goal is a Byzantine AI whose strategic architecture is substantially more deliberate, state-aware, robust, measurable, and experimentally defensible than ordinary stock/custom AI scripts.

The central engineering constraint is that AoE2DE's rule language and engine expose a constrained machine ABI. AEGIS must therefore be designed around what the target engine actually accepts and observes, not around assumptions imported from conventional software engineering.

**Non-negotiable principles:**

- Treat `.per` as a constrained expert system / rule engine.
- Distinguish validator semantics from executable semantics.
- Distinguish unit IDs, unit-line IDs, class IDs, building IDs, goals, strategic numbers, flags, timers, and other typed operands.
- Treat build identity and executable version as part of the ABI.
- Never equate a command with successful world transition.
- Never equate a variable-like goal/SN with arbitrary memory.
- Never equate absence, zero, false, unknown, stale, or unsupported query results.
- Never allocate a numeric channel merely because it appears unused.
- Prefer direct engine evidence over derived duplicate state.
- Store only information the engine cannot safely provide natively when there is a behavioral reason to retain it.
- Keep historical experiments as evidence; `main` is the current authority.

---

## 2. Current architectural status

### Layer 2 — MACHINE / ABI

Layer 2 is closed as an architectural qualification phase.

The target build has been identified and the stock AI substrate has been inventoried. The goal namespace expansion is documented: the engine supports up to 16,000 goals, with important typed/context restrictions still requiring qualification before AEGIS allocation.

A complete stock-tree scan identified resolved high-goal references in the stock source. A later channel-aware audit found numeric constants such as `heavy-wood` using values also appearing in the candidate high-goal region; this was correctly classified as **numeric equality without semantic collision** because operands are typed/contextual. Therefore numeric reuse must remain typed and evidence-qualified.

Provisional Cavalry scalar candidates are `10000–10015`. These are candidates only, not cleared production allocations.

### Layer 3A — ARCHITECTURE

Layer 3A subsystem architecture is closed. Completed architecture reviews cover:

- World Model
- Belief Model
- Situation Analysis
- Objectives
- Planning
- Decision
- Commitment
- Execution
- Verification
- Recovery
- Resource Portfolio
- Production Capacity
- Capability Factory
- Force Composition
- Production/Economic Conversion

No P0 conceptual collapse was identified.

A cross-system objection register was created because the same machine-truth questions recur across subsystem boundaries. The solution is a shared **Machine Truth / Qualification Layer**, not a universal State Manager and not a giant manager forest.

### Layer 3B — MACHINE QUALIFICATION

Layer 3B is active. The project has moved from architecture invention to target-build evidence acquisition.

The current bottleneck is **evidence acquisition**, not architecture quality.

---

## 3. Cross-system qualification gates

The active qualification register consolidates the major integration objections, including:

1. Build identity / semantic scope
2. Typed ABI identity
3. State-channel ownership and collision
4. Identity continuity
5. Generation propagation and stale rejection
6. UNKNOWN/FALSE/ZERO semantics
7. Current versus last-known / freshness semantics
8. Publication atomicity and coherent envelopes
9. Search isolation and filter contamination
10. Zero-result / absence semantics
11. Pending → Created → Available lifecycle
12. Command → acceptance / queue semantics
13. Command → world-observable latency
14. Completion and causal attribution
15. Cancellation / supersession / stale resurrection
16. Concurrency and resource races
17. Scope propagation
18. Partiality / multi-component composition
19. Candidate identity and publication
20. Simultaneous semantic objects / channel multiplexing
21. Runtime cost and bounded search
22. Expensive evidence and caching justification
23. Native versus derived boundary
24. Target-build regression / ABI versioning
25. Verification evidence strength
26. Revalidation / hysteresis / material-change thresholds
27. Shared resource obligations and reserves
28. Production / training / research feasibility
29. Capability / force-composition contribution
30. Writer uniqueness / hidden second publisher
31. Refusal / deferral / no-selection representability
32. Cross-domain arbitration boundary
33. State lifecycle / history
34. Search multiplicity / identity continuity
35. Controller clock versus world clock
36. Error / failure / unknown distinction
37. Semantic status decomposition
38. Target-build update drift and build-scoped qualification

These gates are integration controls, not a replacement architecture.

---

## 4. Stock AoE2DE source closure

The untouched retail stock HD AI source closure is exactly four files:

1. `AI (HD version).per`
2. `Promisory\defaultConstants.per`
3. `Promisory\finalingConstants.per`
4. `Promisory\finaling.per`

Recursive load scanning found no further loads from those three Promisory files.

The stock AI remains the reference substrate and has not been modified as an AEGIS development target.

The stock runtime topology was inventoried. Important observed concentrations include:

- goal writes: 74 unique channels / 2,177 operations
- goal reads: 58 unique channels / 1,016 operations
- strategic-number writes: 143 unique channels / 1,836 operations
- fact operations: 7 unique operations / 1,867 operations
- commands: 5 unique commands / 1,806 operations

The most heavily used native state channels include `unit-goal`, `control-goal`, `strategy-goal`, `ranged-unit-type-goal`, `increase-town-size-goal`, `uu-up-goal`, and `attack-goal`; strategic numbers include the standard gatherer percentages, resource control, town size, dropsite constraints, focus-player number, and related stock controls.

AEGIS does **not** hijack these stock channels as its own universal control envelope.

---

## 5. Typed state / ABI evidence

A typed census of the stock source produced approximately:

- 4,893 numeric declaration rows
- 1,480 unique declared symbols
- 756 unique numeric values
- 257 values with multiple symbolic names
- 87 referenced goal channels / 3,193 operations
- 143 referenced strategic-number channels / 1,836 operations
- 29 referenced timers / 83 operations

The important conclusion is not the raw count. It is that numeric reuse is unsafe without operand-type and operation-context qualification.

The current ABI qualification rule is:

> A numeric value is not a semantic allocation until its type, operation legality, ownership, build scope, validator representation, and observable runtime postcondition are known.

---

## 6. Historical knight-line issue

A historical failed experiment used:

`(up-get-focus-fact unit-type-count knight-line temporary-goal)`

inside `ADByzantineIntelligence.per`.

The old validator reported `Invalid Identifier`.

The current interpretation is deliberately conservative:

- `unit-type-count` is FactId 25.
- `knight-line` is a unit-line identifier, not the concrete `knight` unit ID.
- Stock source demonstrates that typed fact operations can use unit-line identifiers in appropriate contexts.
- The historical validator result is not sufficient evidence that the target executable rejects the operation.
- Do **not** replace `knight-line` with `knight 38` merely to appease a stale validator.
- Do **not** alias `knight-line` to an unrelated line such as steppe-lancer-line.
- The exact target-build runtime semantics remain an empirical qualification target.

The historical `temporary-goal` value of 3500 is valid for appropriate store/set/up-modify-goal contexts, but must not be generalized to contexts with narrower goal restrictions such as operations historically limited to 0–511.

---

## 7. Native test-harness discovery

Direct inspection of the actual retail target executable uncovered embedded strings and symbols associated with an internal test harness, including:

- `TEST_HARNESS_COMM`
- `TEST_HARNESS_ADDRESS`
- `SCRIPT`
- `SCRIPTREPORT`
- `SESSIONID`
- `RUNNING_AUTOTEST`
- `up-testharness-test`
- `up-testharness-report`
- `fe-testharness-message`
- `fe-testharness-log-seed`
- `GameTestEventController@testharness`
- `AITestEventController@testharness`
- `TimerTestEventController@testharness`
- `UITestEventController@testharness`
- `FPSEventController@testharness`
- `DiagnosticInformationEventController@testharness`

FTS-related strings establish a native grammar containing constructs such as `WAIT TIME`, `WAIT EVENTTASK`, timeout variants, `CALL`, `REPORT`, `RANDOM`, and `LABEL`.

Controlled attempts using test-harness launch arguments and UDP probing did not establish an externally invocable retail harness. The process launched normally, the expected test listener was not observed, and no test report was produced.

Therefore:

**Embedded capability ≠ enabled capability ≠ externally invocable capability.**

AEGIS will not depend on or activate undocumented retail test-harness mechanisms.

---

## 8. External harness decision

The project therefore uses an external, retail-safe harness as the default path.

Canonical implementation branch:

`aegis/external-harness-v1-2026-09-05`

Associated PR:

`#43`

PR #43 is **open and unmerged**. GitHub has reported it as not currently mergeable. Do not represent it as promoted to `main` until that state changes.

The harness deliberately rejects invasive launch/configuration modes including:

- process injection
- executable patching
- memory modification
- undocumented internal test-harness launch arguments

The intended pipeline is:

`experiment manifest → immutable build capture → disposable AI package → retail launch → process/lifecycle evidence → replay capture → replay parser → derived events → verdict`

The target observation envelope includes:

`experiment_id, build_sha256, backend, game_time_ms, controller_time_ms, player_id, generation, observation_kind, payload, evidence_level`

Evidence bundles are structured around manifest, build, inputs, AI package, launch logs, live observations, replay artifacts, derived events, verdict, and hashes.

---

## 9. AoE2Control qualification

AoE2Control 1.0.0 was identified as the latest relevant release and its release manifest matches the target build:

- release: `1.0.0`
- configuration: `ReleasePacked|x64`
- gameBuildId: `24094652`
- gameFileVersion: `101.103.48987.0`
- source commit: `3810f3b8e87ad22ea188b6a07fcdf7d793abac4b`
- documented native tests: `212/212`
- bounded Lua compatibility probe: passed

The official distribution documentation warns that the adapter uses process injection / memory access and may trigger antivirus detections.

The quarantined ZIP has SHA-256:

`D428FA1E25D5E6F26A126E1C104BB7CD1CA73F42D6E23C28D84ECD0C684DA224`

The final engineering classification is:

**AoE2Control = statically compatible, optional experimental adapter, runtime-unqualified for AEGIS core.**

It may be useful for controlled live-state experiments, but it is not part of the default retail-safe semantic evidence path.

---

## 10. Replay subsystem — actual code and actual evidence

The replay subsystem is not merely a description. It contains executable Python tooling and has been run against a real AoE2DE `.aoe2record`.

Implemented components include:

- `harness.py`
- `replay_collector.py`
- `replay_index.py`
- `test_harness.py`
- `test_replay_index.py`
- `schema.json`

`replay_index.py` is intentionally conservative. It treats replay ACTION records as command-issued evidence and SYNC records as aggregate snapshot evidence. It does **not** silently infer acceptance, pending, created, available, or effective state without explicit evidence.

This conservative rule is foundational to AEGIS verification.

---

## 11. Latest calibration replay

Replay used for calibration:

`MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`

Recorded SHA-256:

`41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

Recorded size:

`6,055,839 bytes`

Extraction:

- header: `3,922,250 bytes`
- body: `5,575,340 bytes`

Parsed body:

- total records: `444,591`
- ACTION: `2,213`
- SYNC: `221,174`
- CHAT: `29`
- POSTGAME: `1`

Observed action categories include:

- MOVE: `832`
- DE_QUEUE: `448`
- ORDER: `383`
- BUILD: `264`
- GATHER_POINT: `124`
- RESEARCH: `59`
- UNGARRISON: `38`
- DELETE: `9`
- plus specialized commands

Non-null `current_time` snapshots:

- count: `442`
- first observed: `8,866`
- last observed: `4,693,659`

These values are **not yet declared to be milliseconds**. Time-unit semantics remain a qualification target.

The replay indexer produced approximately `780` lifecycle-command candidate events.

The current evidence interpretation is:

`ACTION` → command-issued evidence

`SYNC` → world-state/snapshot evidence

`ACTION + subsequent SYNC correlation` → candidate causal evidence

but no automatic upgrade to acceptance/creation/effectiveness is allowed without demonstrating the causal relationship.

---

## 12. mgz-fast / replay parsing infrastructure

The project has successfully used AoEInsights `mgz-fast` against real AoE2DE replays.

Relevant tools include:

- `mgz-parse-header.exe`
- `mgz-extract.exe`
- `mgz-parse-body.exe`
- `mgz-dump.exe`

A previous real replay produced a body JSONL around 70 MB, demonstrating that full replay extraction is operational.

Replay parsing remains post-run evidence. It does not automatically reconstruct arbitrary hidden runtime state, and the project explicitly refuses to infer hidden state merely because a parser exposes a convenient field.

Other replay tooling investigated:

- `happyleavesaoc/aoc-mgz`
- `aoe2ct/aoe2rec`
- `sandsmark/genieutils`

These are useful evidence/tooling sources but are not substitutes for target-build runtime qualification.

---

## 13. Build calibration

Target executable:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`

File/Product version:

`101.103.48987.0`

SHA-256:

`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

Steam BuildID:

`24094652`

The harness successfully demonstrated executable fingerprint matching and process lifecycle observation. A first harness defect was corrected: a normal game remaining alive through the observation window is an expected lifecycle state, not a harness failure.

Current calibration verdict is therefore process-level evidence only, not semantic runtime qualification.

---

## 14. Machine truth model

AEGIS uses the following evidence ladder:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

The controller has its own clock:

`goals / strategic numbers / timers / rule eligibility / searches`

The game world has another clock:

`queue / training / construction / research / object creation / movement / combat`

These clocks must not be collapsed.

Likewise, the following states must remain distinct:

- desired
- feasible
- authorized
- committed
- issued
- accepted
- queued
- pending
- created
- available
- deployed
- effective
- verified

A command appearing in a replay is not proof that the intended world transition occurred.

---

## 15. Current vertical slice

The first full-system qualification target is:

**Cavalry Threat Containment**

The vertical slice must eventually traverse:

`OBSERVATION → WORLD STATE → BELIEF → SITUATION → OBJECTIVE → PLANNING → DECISION → COMMITMENT → EXECUTION → VERIFICATION → RECOVERY`

However, implementation must wait for the minimum machine semantics needed to make those transitions honest.

The project should first prove the machine-level lifecycle:

`COMMAND_ISSUED → ACCEPTED/REJECTED → PENDING/QUEUED → CREATED → AVAILABLE → EFFECTIVE`

---

## 16. Current experiment queue

### P0 — Representation safety

1. Scalar goal write/read smoke test in candidate namespace.
2. Scalar goal compare smoke test.
3. Strategic-number read/write smoke test.
4. Typed fact test with concrete unit ID.
5. Typed fact test with unit-line ID.
6. Validator/runtime comparison.

### P1 — Semantic state safety

7. Two-generation publication test.
8. Stale-generation rejection.
9. Confirmed-zero test.
10. Search-no-result test.
11. Unsupported-query test.
12. Intentionally-unobserved test.
13. Search filter isolation.
14. Publication interruption/coherence test.

### P2 — Operational lifecycle

15. `can-*` versus command issuance.
16. issuance versus queue acceptance.
17. pending versus created.
18. created versus available.
19. cancellation versus stale reissue.
20. supersession versus old-generation execution.

### P3 — Performance

21. Representative fact-query latency.
22. Representative search latency.
23. Repeated-query cost.
24. Bounded execution cadence.
25. Minimum viable vertical-slice budget.

---

## 17. Immediate next engineering work

The next engineer should **not** restart architecture work.

The next sequence is:

### Step A — Finish replay causal analysis

Extend the existing replay indexer into a conservative causal analyzer capable of correlating:

- DE_QUEUE actions with later object-state observations;
- BUILD actions with later building-state observations;
- RESEARCH actions with technology-state observations;
- TRAIN actions with unit-state observations.

Every inference must carry an evidence grade and explicit limitations.

### Step B — Establish temporal semantics

Determine whether replay `current_time` values are game milliseconds, ticks, or another engine clock. Do this empirically from known game-duration and event-spacing anchors.

### Step C — Design disposable qualification matches

Create tiny deterministic single-player scenarios / AI packages whose only purpose is to isolate one proposition at a time.

The first useful experiment should make a single command whose world consequence is unmistakable.

### Step D — Capture command/world pairs

For example:

`TRAIN → DE_QUEUE → unit object exists`

and:

`BUILD → building object exists`

The experiment must record the command timestamp and the first defensible world-state observation.

### Step E — Test negative cases

The harness must deliberately test:

- impossible command;
- unavailable resource;
- missing production building;
- cancelled queue;
- superseded intent;
- zero-result query;
- unsupported query;
- intentionally hidden/unobserved object.

Negative cases are essential because they distinguish absence from failure and failure from unknown.

### Step F — Qualify identity/generation

Demonstrate that two observations of the same strategic proposition can be distinguished across generations and that stale information cannot overwrite newer information.

### Step G — Re-run five-person review at the evidence boundary

The team remains:

1. Architect
2. Carpenter
3. Adversary
4. Scientist
5. Systems Assurance & Integration Engineer

Systems Assurance must independently trace each qualified machine primitive into every subsystem that consumes it.

### Step H — Only then implement the first Cavalry slice

Do not build the whole Byzantine bot at once. Implement one vertical slice whose every machine dependency has a qualification record.

---

## 18. Promotion criteria

A runtime primitive is not `VERIFIED` merely because it is documented or because a script compiles.

The project uses the following progression:

`DOCUMENTED → ARCHAEOLOGICALLY_SUPPORTED → IMPLEMENTED → RUNTIME_VALIDATED → REPLAY_CORROBORATED → BATTLEFIELD_VALIDATED`

A primitive may enter production Layer-3 code only when its qualification record identifies:

- exact signature;
- legal inputs;
- output representation;
- side effects;
- build scope;
- validator representation;
- observable postcondition;
- failure/unknown behavior;
- runtime cost where material.

---

## 19. Important repository / PR state

### Architecture exit review

PR #37 remains an open historical architecture record. It must not be described as merged/promotion authority merely because its conclusion was favorable.

### Systems Assurance selection

PR #38 remains an open documentation record establishing the fifth review role.

### External harness

PR #43 remains open/unmerged and is the active implementation candidate.

The repository rule is:

> One current document. Many historical records. History is evidence; `main` is authority.

---

## 20. Critical mistakes future engineers must avoid

1. Do not use the stock AI folder as an uncontrolled scratch directory.
2. Do not modify the immutable stock baseline.
3. Do not revive ADPromisory / old `byzwarcouncil` code as production authority.
4. Do not substitute stale validator behavior for target-build engine evidence.
5. Do not infer typed semantics from numeric coincidence.
6. Do not use a universal State Manager to paper over subsystem boundaries.
7. Do not activate the embedded retail test harness merely because strings exist in the executable.
8. Do not make injection/memory modification part of the default AEGIS harness.
9. Do not call a replay ACTION an accepted command without corroboration.
10. Do not call object existence equivalent to availability/effectiveness.
11. Do not silently turn UNKNOWN into FALSE or ZERO.
12. Do not silently overwrite a newer generation with stale information.
13. Do not optimize away expensive engine queries before measuring their cost.
14. Do not allocate final ABI channels before the channel-aware collision audit and runtime qualification.
15. Do not implement the complete production bot before the first vertical slice has proven its machine contracts.

---

## 21. Current project truth

The project has crossed an important threshold.

The architecture is no longer the primary uncertainty.

The stock engine has been fingerprinted.

The stock AI closure has been mapped.

The ABI namespace has been inventoried.

The state-channel collision problem has been explicitly modeled.

The native test-harness discovery has been investigated and deliberately rejected as a production dependency.

An external retail-safe harness exists as actual code.

A real AoE2DE replay has been parsed into hundreds of thousands of records and indexed into lifecycle candidates.

The remaining challenge is to turn those observations into **machine-proven causal semantics**.

That is the bridge between a sophisticated architecture document and a genuinely trustworthy AEGIS bot.

The next lead should therefore think like an experimental systems engineer:

**Ask one machine question. Build the smallest experiment that can answer it. Capture the evidence. State exactly what was proven and what was not. Register the result. Then move one step higher.**

Do not theorize past the evidence.

Do not weaken the architecture to fit an unproven implementation.

Do not mistake complexity for progress.

The objective now is not another design.

**The objective is machine truth.**
