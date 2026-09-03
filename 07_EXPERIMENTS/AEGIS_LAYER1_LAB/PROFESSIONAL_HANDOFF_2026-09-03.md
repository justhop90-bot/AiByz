# AEGIS Layer 1 — Professional Engineering Handoff

Date: 2026-09-03
Status: active investigation; no Layer 1 causal promotion
Formal Layer 1 status: **89%**
Canonical build: `101.103.48987.0`
Executable: `AoE2DE_s.exe`
Executable SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
Repository branch: `lab/aoe2de-adapter-2026-09-03`

## 1. Mission

AEGIS is reconstructing the native Age of Empires II: Definitive Edition AI machine before designing the Byzantine bot around it. The architectural constraint is hard: the final ByzBot is a pure `.per` AI. XS is archaeological/reference material only and is not part of the ByzBot runtime architecture.

Layer 1 is not a percentage of source files understood. It is a maturity assessment of the causal machine model. The project must not promote a mechanism from vocabulary, historical source, replay observation, static correlation, or validator behavior into native truth without discriminating evidence.

## 2. Epistemic contract

Required investigation record:

`question → prior evidence → competing hypotheses → discriminating test → exact setup/build → raw observation → interpretation → confidence → promotion/rejection decision → repository artifact → next test`

Rules:
- Exact build identity is mandatory for native claims.
- Historical source is comparative evidence, never current-runtime proof.
- Replay is observation, not native-state truth.
- Validator behavior is not runtime evidence.
- Strings are semantic anchors, not executable call edges.
- RVA/VA proximity is not a function or object relationship.
- `.pdata` function intervals establish executable structure, not semantics.
- Infrastructure success is not causal success.
- Negative evidence is retained and dated.
- Superseded claims are not silently rewritten.
- No causal promotion occurs merely because several weak signals agree.

## 3. Current Layer 1 QC

```text
Breadth: HIGH
Semantic map: HIGH
Evidence rigor: HIGH
Native geometry: HIGH
Causal closure: INCOMPLETE
Temporal model: INCOMPLETE
Mutation model: INCOMPLETE
Failure model: INCOMPLETE
Identity model: INCOMPLETE
Predictiveness: INCOMPLETE
```

The 89% figure remains unchanged. The current work has increased evidence quality and narrowed the remaining unknowns; it has not closed the causal propositions required to move the percentage.

## 4. What is now established

### Native AI subsystem
The exact executable contains native AIExpert/AIExpertEngine evidence, including:
- AIExpert system construction during game loading.
- Native `.per` / `.per2` parsing and rule-loading diagnostics.
- Native rule/list representation and debug state.
- Player AI identity fields such as AI script base name, civilization/name identity, and custom-AI state.
- Scenario AI filename resolution and both embedded-AI and loose-file failure paths.
- A named native phase `Evaluating Persistent Facts` / `Finished Evaluating Persistent Facts`.
- A native regression path `GamePC::RunTestScenario(PathSpec const&)`.

These establish the existence and boundaries of native subsystems. They do **not** yet establish their exact instruction-level call graph or causal scheduling semantics.

### Native binary geometry
The controlled executable's `.pdata` contains approximately 166,730 valid nonzero runtime-function records with unique monotonic starts and no overlaps. This is now the preferred executable-structure index. It must not be interpreted as 166,730 semantic functions.

A corrected instruction-level RIP-relative scan of `.text` produced zero direct references to the selected AIExpertEngine diagnostic-string addresses. This corrected the earlier assumption that diagnostic strings should yield simple direct xrefs.

### Native runtime operation
The exact build launches and runs under the isolated runtime controller. Background random-game execution was observed with a valid native process/window and normal termination. MainLog showed `Running Game`, `AIScript is being logged`, and `Constant Logging is ON`. This is infrastructure/runtime evidence only; no causal AI-state observation was obtained.

### Parser/scenario adapter
The qualified AoE2ScenarioParser source tree and isolated Python 3.13 environment passed the bundled parser suite and deterministic scenario parse/reconstruct/write/reparse checks. The lab fixture is XS-free. Automated Scenario Editor interaction was attempted but proved unreliable; it has therefore been shelved as a primary causal route.

### Harness archaeology
The executable contains internal test-harness infrastructure, including event controllers, FTS script grammar, storage points, regression-test names, UDP communication strings, and automation flags. The project has deliberately **not** activated undocumented internal harness functionality. Presence in the executable is not treated as authorization. Supported Scenario Editor / ordinary game routes remain preferred.

## 5. Critical corrections made during this pass

### Correction A — historical RunList signature
A public historical project, `FLWL/aoe2-ai-module`, contains a DE RunList byte signature and models `AIExpert::RunList` as `(AIExpert*, int listId, void* statsOutput)`. Its code dynamically resolves the DE RunList function and calls the original function before processing its own queue.

That signature was tested against the exact current executable and returned **0 matches**. Therefore the historical signature is retained as an architectural lead only. No current-build RunList address has been inferred from it.

### Correction B — string-xref methodology
The first instinct was to locate AI functions through direct references to diagnostic strings. The corrected scan found zero direct RIP-relative code references for the selected AI diagnostic strings. This does not mean the strings are unused; it means direct string xrefs are not a reliable current-build recovery path here.

### Correction C — whole-.text disassembly
A whole-section Capstone pass can stop or desynchronize when mixed/data regions are encountered. The correct procedure is to use `.pdata` to partition executable ranges and disassemble function intervals individually.

### Correction D — generic RCX-field matches
Raw patterns resembling offsets `0x18`, `0x20`, `0x38`, and `0x40` were not promoted as AIExpert members. Candidate functions also accessed unrelated offsets such as `0x50`, `0x68`, and `0x70`, so the matches are not object identity proof.

### Correction E — Scenario Editor automation
Scenario Editor automation was shelved as a primary route after repeated foreground/input/loading failures. This is a tooling-route rejection, not a rejection of Scenario Editor itself or of scenario-based AI testing as a supported feature.

### Correction F — build identity
The controlled executable `101.103.48987.0` is treated as the exact current experimental build captured in this lab. Future claims must re-verify the SHA-256 before using native evidence. Official June 2026 update material and subsequent minor-update notes were checked during this handoff; the project must treat any later local executable hash as a new evidence boundary.

## 6. New comparative evidence worth retaining

The historical `aoe2-ai-module` source is useful because it independently exposes concepts that match native AI vocabulary:
- RunList has an `AIExpert*`, list identifier, and stats output boundary.
- DE AIExpert state includes string, fact, and action tables with counts/names.
- AIFact includes `type`, `touched`, `lastResult`, `argc`, a native function pointer, and argument-type metadata.
- A historical loader maps fact names to native fact function pointers and argument counts.

This is **comparative architecture**, not proof that the 2021 structure is byte-for-byte identical to the 2026 executable. The source is historical and its current-build signature failed to match.

## 7. Remaining P0 causal frontiers

### P0-A — Persistent facts
Required chain:
`fact source → evaluation → storage → invalidation/refresh → consumer`

The native executable proves a persistent-fact evaluation phase exists. It does not yet prove whether values are live, cached, scheduler-refreshed, invalidated, or explicitly reevaluated after mutation.

### P0-B — Scheduler / RunList
Required chain:
`loaded rule → rule representation → eligibility → ordering/comparator → selected rule → interval/timing transition`

This is the current highest-priority static recovery target. Start from executable structure, not from the historical address signature.

### P0-C — Rule to action
Required chain:
`selected rule → action handler/order request → native acceptance`

### P0-D — UnitAI mutation
Required chain:
`accepted order → CurrentOrder → CurrentAction → execution`

### P0-E — Failure/recovery
Required chain:
`failure/invalidation → notification → recovery/search → replacement`

## 8. P1 causal frontiers

- Temporal causality: simulation ↔ facts ↔ scheduler ↔ UnitAI.
- Identity lifecycle: create → lookup → transform → garrison → ownership → destroy → reuse → replay correlation.
- Determinism/resource semantics: repeated identical state and controlled input should be tested for scheduler/search/resource/action repeatability.
- End-to-end prediction: native state should permit prediction of the next AI transition before observing it.

## 9. Automation strategy

The project will not depend on a human manually launching hundreds of games.

Use three levels:
1. Static computational experiments for source/corpus/binary analysis.
2. Automated native runtime experiments with strict launch/timeout/artifact controls.
3. Adaptive causal discovery where the knowledge graph selects the next experiment by discrimination value, P0 priority, low confounding, cost, and falsification potential.

Generated/dry-run cases are not counted as valid runtime causal experiments merely because they execute successfully.

## 10. Current repository artifacts that matter first

Start with:
- `README.md`
- `RESEARCH_INDEX.md`
- `PROJECT_MATERIALS.md`
- `03_HD_ARCHAEOLOGY/`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/LAB_MANIFEST.json`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/MACHINE_EXPERIMENT_SCHEMA.json`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/SECURITY_GATE_STANDARD_2026-09-03.md`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/NATIVE_PER_LOADER_QC_DEEP_DIVE_2026-09-03.md`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/NATIVE_SCENARIO_AI_EMBEDDING_GATE_2026-09-03.md`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/NATIVE_SCHEDULER_RECOVERY_PASS_2026-09-03.md`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/NATIVE_FUNCTION_RECOVERY_*`
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/BACKGROUND_RUNTIME_OPERATION_GATE_2026-09-03.md`
- this handoff.

## 11. Exact next engineering pass

**P0-B Native Scheduler Recovery.**

Do not resume Scenario Editor automation unless a new reason makes it materially more discriminating.

Procedure:
1. Re-verify executable SHA-256.
2. Build/update the `.pdata` RVA→function interval index.
3. Build a reverse index of function-pointer-like references from `.rdata/.data` to genuine `.pdata` starts.
4. Recover candidate AIExpert object access patterns using independently supported field-layout evidence, not generic offsets alone.
5. Identify constructor/loadRules callers and their call neighborhoods.
6. Trace candidate list execution routines outward to rule iteration, eligibility, and ordering operations.
7. Record every candidate with confidence and rejection reason.
8. Only after structural convergence, design the smallest native runtime calibration capable of distinguishing scheduler hypotheses.
9. Promote no scheduler claim until a competing-hypothesis test closes the causal edge.

## 12. Six-month recovery guarantee

The repository is intended to be the institutional memory of AEGIS. A future engineer should be able to reconstruct the current state without relying on this chat.

To return to the present state after a long absence, recover:
- repository branch and commit recorded by this handoff;
- exact executable hash/build;
- experiment schemas and security gate;
- latest dated reports, especially the scheduler recovery pass;
- current QC and remaining P0/P1 frontier;
- all negative findings and rejected routes;
- exact next-pass procedure above.

What cannot be guaranteed is that the external environment will remain unchanged. A future Steam/AoE2DE update, missing local executable, changed paths, unavailable device, dependency drift, or lost uncommitted artifacts can create a new evidence boundary. Those conditions must be treated as environment changes, not silently merged into old evidence.

The engineering standard is therefore: **the project must be resumable from Git, but native claims remain build-scoped.**

## 13. Handoff conclusion

The project is not lost at the conversation boundary. The important knowledge has been converted into dated repository artifacts, including the current build identity, methodology, negative evidence, tooling decisions, causal frontiers, and next action.

The project is currently at **Layer 1: 89%**. The correct next move is not more broad collection. It is causal recovery of the native scheduler, beginning with current-build executable structure and the AIExpert/loadRules boundary.
