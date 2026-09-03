# AEGIS Layer 1 — Native .per Loader Deep-Dive QC

Date: 2026-09-03
Build: 101.103.48987.0 / game build #180059 / Steam Build ID 24094652
Executable SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4
Status: evidence audit; no causal promotion

## Question
Re-audit the latest native .per-loader findings for missed signals, overclaims,
namespace confusion, and new discriminating targets.

## Method
The exact controlled executable was rescanned by literal ASCII extraction around
native AI, scenario, and loader vocabulary. Findings were separated into native
AIExpert evidence, scenario AI identity/resolution evidence, FTS/test-harness
evidence, and regression evidence. String presence is treated as structural
provenance only; no call edge is promoted without code-level evidence.
## Corrected interpretation
The earlier association of `Parsing script '%s'` with .per loading was too broad.
The nearby FTS tokens (`WAIT`, `EXECUTE`, `SET`, `GET`, `GOTOIF`, `REPORT`,
`EVENTTASK`, `FPS_CHECK`, `MEMORY_LEAK_CHECK`) identify a test-harness/FTS
parser surface. That evidence is retained but must not be used as proof of
AIExpert .per parsing.

## Strong native AIExpert evidence
A separate cluster at executable offset ~52210144 contains `AIExpertEngine::`,
source provenance `Game\\ai\\AIExpertEngine.cpp`, rule-element expressions,
`list->ruleElements[list->ruleElementsPtr]`, `list->ruleDebugInfo[j].cString()`,
`Evaluating Persistent Facts`, `Finished Evaluating Persistent Facts`, rule
navigation diagnostics, and `AIExpertEngine::ResolveBreakPoint`.

The same native AIExpert cluster contains:
- `Defining BoolOp[%d]`
- `Defining LocalSymbol[%d]`
- `Defining LocalConst[%d]`
- `Defining Symbol[%d]`
- `Defining Fact[%d]`
- `Defining Action[%d]`
- `loadRules for listId=%d, file=%s`
- `%s AI file must have at least one rule`
- `.ai`, `.ai2`, `.per`, `.per2`
- parse directive errors and command parse errors
- `No Rule`, `defRule(`, `End of file`, `Next Rule:`

This is strong structural evidence for a native rule-based AIExpert subsystem,
not merely generic scripting vocabulary.

## Scenario-to-AI identity evidence
The executable contains the native member names `mAiScriptBaseName` and
`mIsCustomAI`, plus `mAiRulesFileData`, `aiRulesFileSize`, and
`aiRulesFileDataSize`. It also contains the native symbol
`BaseScenario::getOrExtractPlayerAiRulesFileName(...)` and messages describing
embedded AI data versus loose AI files:
`Scenario doesn't contain embedded AI data, and loose file cannot be found: %s`
and `No AI was found when reading scenario.`

These findings establish the existence of scenario/player AI identity and
AI-rule resolution concepts. They do NOT yet prove the call chain from
`mAiScriptBaseName` to filename extraction to `AIExpertEngine::loadRules`.
## New P0-A relevance
`Evaluating Persistent Facts` / `Finished Evaluating Persistent Facts` gives
P0-A a concrete native subsystem target. It does not establish freshness,
cache lifetime, invalidation, cadence, or replication. The next test must
separate evaluation from consumption and mutation.

## Native rule representation
The cluster exposes rule-element and rule-debug-info references, a rule cursor,
and out-of-bounds jump diagnostics. This supports a native rule-list
representation and explicit rule navigation. It does not establish scheduler
ordering or comparator semantics.

## Native scenario execution evidence
A separately recovered native symbol is `GamePC::RunTestScenario(PathSpec const&)`.
Together with the previously documented `RUN_REGRESSION_TEST*`, SaveFiles/temp,
and scenario-server strings, this strengthens the existence of a native
regression scenario path. It does not establish a safe user-facing invocation
or its relationship to the AIExpert loader.

## Evidence table
AIExpertEngine existence: CONFIRMED structurally.
Native .per/.per2 rule-loading vocabulary: CONFIRMED structurally.
`loadRules(listId,file)` existence: CONFIRMED structurally.
Persistent-fact evaluation phase vocabulary: CONFIRMED structurally.
AI script base-name field: CONFIRMED structurally.
Scenario AI filename-resolution symbol: CONFIRMED structurally.
Embedded/loose AI-rule handling: CONFIRMED structurally.
User .per reaches loader: NOT ESTABLISHED.
Successful user .per parse: NOT ESTABLISHED.
Meaning of listId: OPEN.
AI file root/path contract: OPEN.
Filename-resolution -> loadRules call edge: OPEN.
Rule scheduling: OPEN.

## Competing hypotheses
H1 scenario/player AI identity resolves a loose or embedded rule file and passes
it to AIExpertEngine.
H2 embedded and loose AI resolution converge elsewhere before AIExpertEngine.
H3 `loadRules` can service multiple rule-list consumers and listId is not a
player index.
H4 some observed parser messages belong to adjacent tooling despite shared
terminology.

## Next discriminating pass
Use PE-aware disassembly to resolve the containing function and callers for
`loadRules`, then separately resolve `BaseScenario::getOrExtractPlayerAiRulesFileName`.
Recover argument boundaries and any registration/vtable/factory relationships.
Do not infer edges from string proximity. Do not invoke guessed regression or
UDP protocols. If and only if a legitimate AI-selection contract is recovered,
run one minimal pure-.per positive/negative calibration.

## Security / provenance
No binary modification, DLL injection, hooks, debugger attachment, memory
patching, arbitrary UDP, XS, or installed-AI-file modification was used.
Executable hash was treated as a mandatory provenance boundary.
No causal Layer 1 claim is promoted by this report.
