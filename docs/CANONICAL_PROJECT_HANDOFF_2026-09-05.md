# AiByz / AEGIS — Canonical Professional Engineering Handoff

**Effective:** 2026-09-05
**Repository:** `justhop90-bot/AiByz`
**Canonical branch:** `main`
**Status:** authoritative project handoff at conversation close

> This document supersedes the earlier handoff while preserving its history in Git. It records the project at the point where broad Layer-1 archaeology and Layer-3A architecture are complete, the external replay harness exists as real code, a real retail replay has been parsed, and machine-semantic qualification is the remaining engineering frontier.

## 1. Mission

Build AEGIS, a high-quality Byzantine AI for Age of Empires II: Definitive Edition. AEGIS is intended to be a stateful strategic controller that observes the game, maintains bounded beliefs and commitments, derives capability requirements, evaluates feasible responses, executes through verified `.per` primitives, verifies world postconditions, recovers from failure, and reassesses.

AEGIS is not a transcription of HD/Promisory and is not a static build order. The historical AI is evidence and inspiration; current target-build behavior is the runtime authority.

## 2. Current engineering position

| Layer | Status | Interpretation |
|---|---|---|
| Layer 1 — Machine/runtime | **89%, broad archaeology frozen for handoff** | Target executable and stock package are identified; remaining work is semantic qualification, not broad discovery |
| Layer 2 — Historical strategy archaeology | **Major reconstruction closed** | Targeted evidence only; no silent reopening |
| Layer 3A — AEGIS architecture | **Closed for implementation** | Five-pass subsystem architecture completed; cross-system qualification register remains active |
| Layer 3B — Machine qualification | **Active / incomplete** | Static ABI substrate qualified in important areas; runtime lifecycle semantics remain open |
| Layer 4 — Runtime `.per` implementation | **Blocked by design** | Do not promote production code until machine/ABI gates are cleared |

The immediate project point is therefore **machine truth qualification**, not another architecture rewrite.

Permanent boundaries:

- Scenario-loader automation/testing is retired.
- XS is outside AEGIS scope.
- CaptureAge/CADE is secondary validation infrastructure, not core semantic authority.
- Historical HD/Promisory source is strategic evidence, not automatic runtime authority.
- Commands are not completion proof.
- Validator acceptance is not engine semantics.
- Apparently unused numeric channels are not automatically safe.
- Embedded native test-harness capability is not assumed to be externally invocable on retail.
- Injection, executable patching, memory modification, debugger attachment, and hidden test-build facilities are outside the default AEGIS harness profile.

## 3. Target build identity

Authorized workstation evidence identifies:

- executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam BuildID: `24094652`
- current update line: `#180059`

This identity is the A1 executable target. A future engineer must re-fingerprint before treating any runtime result as target-build evidence.

## 4. Stock AI package baseline

The project owner restored:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

from Steam and designated it as the **untouched stock-runtime baseline**.

This supersedes older language implying that the installed AI tree was necessarily contaminated. Names appearing in the restored directory — including historical or shipped `Promisory`, `AiBuilder`, or test-related material — are not evidence of project modification by themselves.

The baseline is evidence and must not be modified during acquisition or qualification.

### Stock HD source closure

The actual stock HD AI source closure was established as exactly four files:

1. `AI (HD version).per`
2. `Promisory\defaultConstants.per`
3. `Promisory\finalingConstants.per`
4. `Promisory\finaling.per`

Recursive inspection found no additional loads from those three Promisory files.

Recorded sizes:

- `AI (HD version).per`: 36,141 lines / 1,167,238 bytes
- `Promisory\finaling.per`: 1,090 lines / 29,232 bytes
- `Promisory\finalingConstants.per`: 400 lines / 10,515 bytes
- `Promisory\defaultConstants.per`: 941 lines / 33,628 bytes

The stock runtime contains substantial goal, strategic-number, timer, fact, command, search, and production machinery. It is a real expert-system runtime, not a trivial ruleset.

## 5. Layer-2 / ABI conclusions that must survive handoff

The current goal namespace is 1–16,000. A complete stock-tree scan found 5,214 resolved high-goal references spanning 85 distinct high goal IDs, with resolved references reaching 8,404. No resolved stock goal-typed references were found in 10,000–15,999 under the original goal-typed scan.

A later channel-aware audit found stock `defconst` values of `10000` and `14000` (for example `heavy-wood`). This is **not** by itself a collision with a goal allocation: numeric equality across differently typed operands is not semantic identity.

The provisional AEGIS cavalry scalar candidate block remains `10000–10015`, but these values are **candidates, not cleared allocations**. They are scalar-only until every intended operation has been qualified. Do not use them in point/cost/search-state/multi-goal contexts merely because the numbers look unused.

The typed census of the stock package recorded:

- 4,893 numeric declaration rows
- 1,480 unique declared symbols
- 756 unique numeric values
- 257 numeric values shared by multiple symbols
- 87 referenced goal channels / 3,193 goal operations
- 143 referenced strategic-number channels / 1,836 operations
- 29 referenced timers / 83 operations

No stock state channel has been cleared for direct reuse as an AEGIS core control-envelope field. State-channel collision analysis is therefore an ownership boundary, not a scavenger hunt for empty variables.

## 6. AEGIS architecture status

The following Layer-3A subsystems reached five-pass architecture closure:

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

The five-person review standard is:

1. Architect
2. Carpenter
3. Adversary
4. Scientist
5. Systems Assurance & Integration Engineer

The cross-system qualification register consolidates recurring objections without creating a universal State Manager.

The central cross-system rule is:

**Use direct engine evidence → derive only what is necessary → store only what the engine cannot provide → never duplicate engine state without behavioral return.**

The mandatory semantic envelope is:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

The evidence ladder is:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

Controller time and world time must remain distinct.

## 7. First executable vertical slice

The first implementation target is **Cavalry Threat Containment**:

`ENEMY OBSERVATION → WORLD STATE → BELIEF → SITUATION → OBJECTIVE → REQUIREMENT → CAPABILITY CANDIDATES → RESOURCE/TIMING EVALUATION → DECISION → COMMITMENT → EXECUTION → VERIFICATION → RECOVERY/RE-ARBITRATION → REASSESSMENT`

The slice is deliberately chosen because it forces the project to prove observation, typed fact acquisition, state publication, capability reasoning, production feasibility, commitment, execution, and postcondition verification in one bounded chain.

Do not implement the production slice merely because its architecture is closed. Machine semantics must clear first.

## 8. Native test-harness investigation

Direct binary inspection of the actual target executable found embedded strings and symbols associated with a native test-harness system, including:

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
- `DiagnosticInformationEventController@testharness`
- `TESTHARNESS_SCRIPTS`
- `TESTHARNESS_REPORTS`
- `TESTHARNESS_REG_SAVES`
- `TESTHARNESS_XS`

The embedded FTS grammar also exposed concepts such as `WAIT TIME`, `WAIT EVENTTASK`, timeout variants, `CALL`, `REPORT`, `RANDOM`, `LABEL`, and goto/label processing.

Controlled retail launches using combinations of these discovered options did not establish a working external retail harness listener or report path. The process behaved as an ordinary game process and the expected harness report was not produced.

**Conclusion:** embedded capability ≠ enabled capability ≠ externally invocable retail capability.

Do not spend further engineering effort trying to activate hidden/test-build infrastructure unless independent evidence establishes that it is intended and supported for the target retail build.

## 9. External harness decision

The project therefore moved to an external, retail-safe evidence architecture.

Canonical implementation branch:

`aegis/external-harness-v1-2026-09-05`

Associated PR:

`https://github.com/justhop90-bot/AiByz/pull/43`

At the latest recorded point the PR is **open, unmerged, and reported non-mergeable**. Never describe it as promoted to `main` without a fresh GitHub check.

The branch contains actual Python implementation, not merely prose:

- `harness.py`
- `replay_collector.py`
- `replay_index.py`
- `schema.json`
- `test_harness.py`
- `test_replay_index.py`
- evidence and experiment manifests
- AoE2Control qualification notes

The intended pipeline is:

`EXPERIMENT MANIFEST → IMMUTABLE BUILD CAPTURE → DISPOSABLE AI PACKAGE → RETAIL LAUNCH → PROCESS/LIFECYCLE EVIDENCE → REPLAY CAPTURE → PARSER → DERIVED EVENTS → VERDICT`

The default harness forbids:

- injection
- memory writes
- executable patching
- debugger attachment
- hidden native test-harness activation
- multiplayer use for qualification

## 10. AoE2Control disposition

AoE2Control 1.0.0 was found to be unusually valuable as external live-state research material because its published release manifest targets the exact current game build:

- version `1.0.0`
- ReleasePacked x64
- source commit `3810f3b8e87ad22ea188b6a07fcdf7d793abac4b`
- gameBuildId `24094652`
- gameFileVersion `101.103.48987.0`
- published native tests `212/212`
- bounded Lua compatibility probe passed

The official distribution documentation nevertheless describes process injection/runtime attachment, and the release package uses runtime-hooking/injection machinery.

Therefore:

**AoE2Control = optional invasive instrumentation/reference adapter, not AEGIS core runtime authority.**

It can inform research into live-state observability and packed structures, but it must not silently become a dependency of the retail-safe AEGIS qualification path.

The downloaded artifact was quarantined rather than executed as part of the core qualification profile.

## 11. Replay pipeline — actual calibration evidence

A real target-build replay was acquired and parsed:

`MP Replay v101.103.48987.0 @2026.08.31 164318 (1).aoe2record`

Replay SHA-256:

`41ecadba293dfccdac6230ec7e35e4f0d0ef1fff8da13c8012760111800a041d`

Replay size:

`6,055,839` bytes

The replay was processed with `mgz-fast 1.0.0`.

Extracted artifacts:

- header: 3,922,250 bytes
- body: 5,575,340 bytes
- parsed header JSON: 91,249 lines
- parsed body JSONL: 25,428,749 bytes

Recorded artifact hashes:

- `header.bin`: `70daad999ccf4addb303f11ca14d96adac0408e83880344ea3e4d92dc100504b`
- `body.bin`: `2a5185018f2d668dae81782b6fb9d859bdcf5dce9dcd917daa1f08f44c1c29f8`
- `header.json`: `2e69a57392f95f7037b8d01090ee734a8884d7f78302bff25c1e9478563f7352`
- `body.jsonl`: `04d21b03a23a1aefd790e3f7f909e061e79b73534ad8296db1f917593ff90055`

### Body census

Total body records: `444,591`

| Operation | Count |
|---|---:|
| SYNC | 221,174 |
| VIEWLOCK | 221,174 |
| ACTION | 2,213 |
| CHAT | 29 |
| POSTGAME | 1 |

ACTION census:

| Command | Count |
|---|---:|
| MOVE | 832 |
| DE_QUEUE | 448 |
| ORDER | 383 |
| BUILD | 264 |
| GATHER_POINT | 124 |
| RESEARCH | 59 |
| UNGARRISON | 38 |
| SPECIAL | 16 |
| DE_ATTACK_MOVE | 13 |
| DELETE | 9 |
| DE_MULTI_GATHERPOINT | 6 |
| GAME | 4 |
| WALL | 4 |
| BACK_TO_WORK | 4 |
| PATROL | 4 |
| TOWN_BELL | 2 |
| DE_AUTOSCOUT | 1 |
| DE_107_B | 1 |
| FORMATION | 1 |

The replay header reports `game_version = VER 9.4`, `save_version = 68.0`, and `log_version = 5`. The parsed map is 120×120, `all_visible = false`, and the scenario metadata describes a normal Tiny Arabia two-player setup with no cheats, Dark Age start, and population limit 200.

## 12. Replay clock discovery

The body contains `221,174` SYNC records, but only `442` contained a parsed integer `current_time` field.

First observed non-null `current_time`:

`8,866`

Last observed non-null `current_time`:

`4,693,659`

The span between them is `4,684,793` parser-emitted clock units.

**Do not promote these units to milliseconds from this replay alone.** The current evidence artifact preserves the values exactly as emitted. The replay clock must be empirically aligned with known game-time anchors before any AEGIS latency or timeout calculation depends on it.

The current replay indexer also observes SYNC payload elapsed-time increments and records their aggregate progression. That implementation detail is useful for internal indexing, but the semantic unit and relationship to displayed game time still require independent qualification.

## 13. Replay lifecycle discovery

The replay contains direct lifecycle-relevant commands:

- `DE_QUEUE`: 448
- `BUILD`: 264
- `RESEARCH`: 59
- `DELETE`: 9

The indexer converts selected ACTION records into normalized `COMMAND_ISSUED` evidence. It deliberately does **not** infer:

`ACCEPTED`
`QUEUED/PENDING`
`CREATED`
`AVAILABLE`
`EFFECTIVE`

from the presence of the command alone.

This distinction is one of the most important discoveries of the project. The replay is rich enough to establish a command stream and aggregate synchronization evidence, but that does not automatically establish causal world-state completion or individual object lineage.

Some SYNC observations expose aggregate fields such as `total_res`, `dp_obj_count`, `dp_obj_ttl`, and `obj_count`. These are useful aggregate evidence, but they do not by themselves prove individual object identity continuity.

Current calibration result:

`CAL_REPLAY_001 = PASS_PIPELINE_PARSE / NOT_YET_SEMANTICALLY_QUALIFIED`

## 14. What the current replay indexer actually guarantees

`replay_index.py` is executable code and has been run against the calibration stream.

Its semantic boundary is intentionally conservative:

- ACTION → `COMMAND_ISSUED`
- SYNC → replay-clock progression / aggregate synchronization evidence
- lifecycle commands are indexed
- parser errors are explicit failures
- missing fields remain missing
- world-state completion is not invented
- effective outcome is not invented

The implementation is therefore an **evidence indexer**, not yet a causal world-state reconstruction engine.

## 15. Next engineering frontier: causal world-transition qualification

The highest-value remaining machine question is:

`COMMAND_ISSUED → ACCEPTED/REJECTED → PENDING/QUEUED → CREATED → AVAILABLE → EFFECTIVE`

The first controlled experiments should target:

1. `DE_QUEUE → individual unit creation`
2. `BUILD → building realization`
3. `RESEARCH → technology completion`
4. `DELETE → object disappearance`

Each experiment should be minimal, deterministic, disposable, and independently replayable.

The objective is not to make the replay parser “smart.” The objective is to discover exactly which observations permit each causal claim.

## 16. Required experiment methodology

For every machine-semantic experiment:

1. Capture exact executable identity.
2. Capture the AI package and every input artifact by hash.
3. Start from a disposable single-player scenario/match.
4. Issue one controlled operation where practical.
5. Capture replay and process/lifecycle evidence.
6. Parse the replay without semantic assumptions.
7. Identify all candidate observations before defining the conclusion.
8. Compare command timing against world-state observations.
9. Repeat enough times to separate deterministic behavior from coincidence.
10. Record negative evidence and ambiguity explicitly.
11. Only then upgrade the primitive's evidence grade.

A primitive cannot become `VERIFIED` merely because it worked once.

## 17. Primitive qualification standard

The Pass-90 runtime primitive registry uses evidence states:

`DOCUMENTED → ARCHAEOLOGICALLY_SUPPORTED → IMPLEMENTED → RUNTIME_VALIDATED → REPLAY_CORROBORATED → BATTLEFIELD_VALIDATED`

Before a primitive enters Layer-3 code as verified, record:

- exact signature
- typed inputs
- legal ranges
- build scope
- side effects
- search/filter interactions
- failure behavior
- validator representation
- observable postcondition
- evidence level
- repeatability

This is the bridge between architecture and `.per` implementation.

## 18. CaptureAge / CADE disposition

CaptureAge/CADE is retained as **secondary validation infrastructure**. It may be useful for observing visible game state, timelines, and human-readable corroboration, but it is not the primary source of machine semantic truth.

The strongest evidence chain remains:

`retail executable/package → controlled action → replay/live evidence → independent parser/observer → cross-correlation → qualified claim`

CaptureAge observations should be used to corroborate, not silently redefine, engine semantics.

## 19. Immediate queue for the successor engineer

### P0 — Preserve

- Do not modify the stock AI baseline.
- Start from GitHub `main`.
- Re-fingerprint the target executable.
- Verify PR #43 state before using its branch as implementation input.
- Preserve all historical handoffs and negative results.

### P1 — Complete replay causal analyzer

- Correlate ACTION sequence numbers with SYNC progression.
- Determine exact `current_time` semantics.
- Locate object-level evidence in parsed records and header structures.
- Build identity-continuity candidates.
- Determine whether individual creation can be observed directly or only inferred from aggregate deltas.
- Separate `PENDING`, `CREATED`, and `AVAILABLE` if the evidence supports those distinctions.

### P1 — Build controlled transition experiments

- Minimal `DE_QUEUE` experiment.
- Minimal `BUILD` experiment.
- Minimal `RESEARCH` experiment.
- Minimal `DELETE` experiment.
- Repeat each experiment.
- Record acceptance/failure and timing uncertainty.

### P1 — UNKNOWN / absence semantics

Prove empirically:

- no object vs hidden object
- zero count vs unavailable fact
- stale observation vs current observation
- failed search vs empty search result
- pending object vs absent object

### P1 — Identity and generation

Determine what stable identity can actually be observed across:

`issued → pending → created → available → effective`

Then define AEGIS generation semantics around real evidence instead of abstract assumptions.

### P2 — ABI freeze

Only after machine semantics are qualified:

- finalize typed goal/SN/timer allocations;
- finalize writer/reader ownership;
- freeze build-scoped ABI;
- update the collision register;
- generate machine-verifiable allocation artifacts.

### P2 — First production `.per`

Only after the ABI gate:

`Cavalry observation → requirement → camel capability → production commitment → execution → verification → recovery`

The first production slice should remain deliberately small. It is a proof of the architecture-to-machine bridge, not the whole bot.

## 20. What must not happen next

Do not:

- resume scenario-loader automation merely because it is convenient;
- activate hidden `TEST_HARNESS_*` facilities without retail-support evidence;
- treat AoE2Control injection as harmless;
- treat CaptureAge as engine truth;
- treat `ACTION` as completion;
- treat `current_time` as milliseconds without calibration;
- allocate a goal because its number looks unused;
- alias abstract unit-line identifiers to concrete unit IDs to satisfy a validator;
- build a universal State Manager;
- reopen closed architecture without falsifying evidence;
- write hundreds of `.per` lines before the machine ABI is proven.

## 21. Project-level lessons

The most important lesson is methodological rather than syntactic:

**The hard part is not teaching an AI what to do. The hard part is proving what the machine actually did.**

AoE2DE exposes several overlapping abstractions — goals, strategic numbers, timers, facts, searches, commands, queued objects, world objects, replay records, and external observations. Their names often look more precise than their semantics actually are. A professional implementation must therefore distinguish the controller's intention from the engine's acceptance and from the world's resulting state.

The project repeatedly demonstrated that a plausible interpretation can be wrong even when the code looks reasonable. The remedy is not more clever code; it is stronger evidence.

## 22. Final handoff doctrine

A future engineer/model must treat this repository as an evidence system.

Start from `main`.

Read the canonical authority documents before historical branches.

Use current target-build evidence before historical claims.

Use deterministic scripts for repeatable extraction.

Keep direct evidence, composed evidence, AEGIS design, and hypotheses visibly separate.

When new evidence contradicts an old claim, record the contradiction explicitly. Do not silently rewrite history.

The project is not finished. It has reached the more valuable point where the remaining unknowns are sharply defined.

The next breakthrough is expected from **controlled causal replay/live correlation**, not from another round of architecture prose.

**Current starting point for the successor:** prove world-transition semantics, then freeze the ABI, then implement the first bounded `.per` vertical slice.
