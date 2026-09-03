# AEGIS Layer 1 — Native `.per` Loader Deep QC — 2026-09-03

## Scope
This report is a strict quality-control review of the native `.per` loader finding. It re-examines the exact executable evidence, separates `.per` AI parsing from the native FTS (`.fts`) test-harness parser, and identifies additional native source/provenance signals that were overlooked in the first-pass interpretation.

## Controlled build
- Executable: `AoE2DE_s.exe`
- Executable version: `101.103.48987.0`
- Game build: `#180059`
- Steam build ID: `24094652`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

## Method
1. Re-read the existing native loader gate and adapter evidence.
2. Re-scanned the immutable executable for parser diagnostics, source-path strings, AI state fields, rule-debug fields, and nearby symbols.
3. Distinguished the `.per/.per2` AIExpert parser surface from the `.fts` test-harness parser surface.
4. Searched for native C++ source/provenance and RTTI-like mangled names near relevant regions.
5. Cross-checked public AoE2DE scripting documentation for claims that can be externally corroborated.
6. No executable modification, injection, hooks, debugger attachment, memory modification, arbitrary UDP, unknown script execution, or XS was used.

## Major correction to the previous interpretation
The string `Parsing script '%s'` is not by itself a `.per` parser marker. The surrounding error cluster at approximately offsets `52,940,807+` contains `.fts`-specific syntax and errors including `FRAME`, `TIME`, `EVENTTASK`, `EVENTPROPERTY`, `TIMEOUTCONTINUE`, `TIMEOUTFAIL`, `EVENTTASKTIMEOUTGOTO`, `TKN_WAIT`, `TKN_EXECUTE`, `TKN_SET`, and `TKN_GET`.

Therefore the earlier report's wording that treated the repeated `Parsing script` cluster as part of the `.per` loader was too broad. It is evidence of a native script parser, but that cluster is specifically associated with the FTS/test-harness scripting language unless further code tracing proves otherwise.

The `.per` loader evidence is instead the distinct `AIExpertEngine` cluster around offsets `52,207,008–52,211,xxx`.

## Stronger `.per` / AIExpert evidence
The exact executable contains the following coherent cluster:

- `AI file Error: '%s' Line %d`
- `Creating AIExpert system`
- `Creating AIExpert system via load game`
- `Destroying AIExpert system`
- source path: `...\\Source\\Game\\ai\\aiexpert.cpp`
- `Defining BoolOp[%d] ...`
- `Defining LocalSymbol[%d] ...`
- `Defining LocalConst[%d] ...`
- `Defining Symbol[%d] ...`
- `Defining Fact[%d] ...`
- `Defining Action[%d] ...`
- `loadRules for listId=%d, file=%s`
- `%s AI file must have at least one rule`
- `.ai2`
- `.per`
- `.per2`
- `failed to parse directive`
- `failed to find open parenthesis`
- `failed to parse command`
- `%s parsing completed successfully`
- `%s - Loading`
- `loaded successfully. Parsing...`
- `Ai lexical analysis failed`
- `ERR2004: Missing identifier`
- `load`
- `load-random`
- `include`
- `defrule`
- `defconst`
- `#load-if-defined`
- `#load-if-not-defined`
- `#else`
- `#end-if`
- `parseLoadRandomCommand`
- `FileSearchParseLoadRandomCommand`
- `ERR5001: File open failed`
- `ERR5002: File read failed`
- `ERR2005: Invalid identifier`
- `ERR2003: Invalid keyword`
- `ERR6001: List full`
- `ERR2008: Missing arrow`
- `ERR2011: Missing closing parenthesis`
- `ERR2010: Missing closing quote`
- `ERR3006: Missing #end-if`
- `ERR2006: Missing file name`
- `ERR2007: Missing left-hand side (LHS) of the rule`
- `ERR2001: Missing opening parenthesis`
- `ERR2009: Missing right-hand side (RHS) of the rule`
- `ERR8001: No rules`
- `ERR3003: Preprocessor nesting too deep`
- `ERR6002: Rule too long`
- `ERR6003: String table full`
- `ERR2013: Unexpected end-of-file`
- `ERR7000: XS file was not found.`

This cluster is materially stronger than generic `.per` strings because it names the native `AIExpertEngine`, the game AI source path, rule loading, AI file validation, AI grammar tokens, preprocessing, and specific parser error classes in one contiguous native evidence region.

## New causal signal: AIExpert is connected to game-load construction
`Creating AIExpert system via load game` is particularly important. It is not proof of an individual `.per` file reaching `loadRules`, but it places AIExpert construction on a native game-load path rather than merely in an isolated editor/tool subsystem.

The correct inference is:

`game-load path -> AIExpert construction exists`

not:

`game-load path -> our chosen .per definitely loaded`.

## New causal signal: persistent-fact evaluation has a named native phase
The same `AIExpertEngine.cpp` evidence region contains:

- `Evaluating Persistent Facts`
- `Finished Evaluating Persistent Facts`

This is a major Layer 1 lead. It demonstrates that the shipped AIExpert implementation has an explicitly named persistent-fact evaluation phase in the exact current executable.

It does **not** yet establish freshness semantics. In particular, it does not distinguish:

- live fact reads,
- cached values,
- periodic refresh,
- invalidation-triggered refresh,
- explicit reevaluation,
- or fact-class-specific behavior.

However, it changes the P0-A investigation from an abstract design hypothesis into a native subsystem target: the persistent-fact phase can now be traced and experimentally correlated with observed values.

## New causal signal: rule representation/debug state is native
The same source region contains:

- `&list->ruleElements[list->ruleElementsPtr]`
- `&stringLengthByte`
- `buffer`
- `&(*list->rule[j].element)`
- `list->ruleDebugInfo[j].cString()`
- `Name failure`
- jump-out-of-bounds diagnostics
- `AIExpertEngine::ResolveBreakPoint`
- `AIDebugger`
- `No Rule`
- `defRule(`
- `End of file`
- `Next Rule:`

This supports a native internal model containing rule elements, rule debug information, a rule cursor/list representation, rule navigation, and debugger-facing rule state.

It still does not reveal the scheduler comparator, interval algorithm, or action dispatcher. Those remain P0-B/P0-C targets.

## New causal signal: scenario AI identity is explicit in native state
A separate native source cluster contains:

- `mAiScriptBaseName`
- `mAiCivNameIndex`
- `mAiPlayerName`
- `mIsCustomAI`

This demonstrates that native game/player configuration carries an explicit AI script base name and a custom-AI flag.

A separate RTTI-like symbol cluster contains:

`BaseScenario::getOrExtractPlayerAiRulesFileName(...)`

The exact mangled name identifies a native method whose apparent responsibility is obtaining or extracting a scenario player's AI rules filename. The name is strong structural evidence, but the function body and call edges have not yet been traced, so its exact semantics remain to be confirmed.

## New scenario embedding signal
The native executable also contains:

- `Failed to find AI file for scenario embedding, and embedded data is empty!: %s`
- `Scenario doesn't contain embedded AI data, and loose file cannot be found: %s`
- `No AI was found when reading scenario.`
- `mBuildListFileData`
- `mCityPlanFileData`
- `mAiRulesFileData`
- `aiRulesFileSize`
- `aiRulesFileDataSize`
- `mAiRulesType`

This is highly relevant to the deterministic scenario path. It establishes that the shipped scenario loader has a native concept of AI rules data, including both embedded AI data and a loose-file fallback/error path.

The correct model is now:

`scenario -> native scenario player AI metadata -> AI rules filename / embedded AI rules data -> AIExpert path`

with the exact transition into `loadRules` still requiring code-level trace or controlled runtime evidence.

## New native regression connection
The executable's RTTI-like strings identify:

`GamePC::RunTestScenario(PathSpec const&)`

and nearby lambda types capture the same method. The regression subsystem separately exposes `RUN_REGRESSION_TEST` and scenario-server strings.

This strengthens the earlier regression finding: a native scenario execution method exists in the retail executable. It does **not** prove that arbitrary regression names or user-created regression directories are accepted, so no invocation is inferred.

## Important parser-domain separation
Two parser domains must now be tracked separately:

### AIExpert parser
Source evidence:
`Game\\ai\\AIExpertEngine.cpp`

Key grammar:
`.per`, `.per2`, `load`, `load-random`, `include`, `defrule`, `defconst`, preprocessor directives.

### FTS/test-harness parser
Source/evidence region around `Parsing script`:
`.fts`, `FRAME`, `TIME`, `EVENTTASK`, `WAIT`, `EXECUTE`, `SET`, `GET`, `GOTOIF`, `REPORT`, `FPS_CHECK`, `MEMORY_LEAK_CHECK`.

The two must not be conflated in future reports.

## Revised evidence ladder
### CONFIRMED
1. Exact current executable contains a native AIExpert subsystem.
2. AIExpert has a native game-load construction path.
3. AIExpert contains native rule-loading diagnostics with `listId` and filename parameters.
4. `.per` and `.per2` are explicit AIExpert file types in that cluster.
5. AIExpert validates the presence of at least one rule.
6. AIExpert recognizes native `.per` grammar constructs including loads, includes, rules, constants, and preprocessor directives.
7. AIExpert has named persistent-fact evaluation start/end instrumentation.
8. Native scenario/player state carries `mAiScriptBaseName` and `mIsCustomAI`.
9. Native scenario code has `getOrExtractPlayerAiRulesFileName`.
10. Native scenario code has embedded/loose AI-rules data concepts.
11. Native regression code exposes `GamePC::RunTestScenario(PathSpec const&)`.

### NOT ESTABLISHED
1. Exact function address containing `loadRules`.
2. Exact call edge into `loadRules`.
3. Exact filesystem root selected for a custom AI.
4. Exact meaning of `listId`.
5. Whether `mAiScriptBaseName` maps directly to the final `.per` path in every mode.
6. Whether scenario-embedded AI rules bypass or feed the same `loadRules` function.
7. Whether a user-supplied pure `.per` can be loaded without installed-corpus modification.
8. Whether a successfully loaded rule is scheduled immediately or enters a separate initialization phase.
9. Persistent-fact freshness/invalidation semantics.
10. Rule scheduling order/comparator.
11. Rule-to-action dispatch.

## QC disposition
The original loader finding is **upgraded in strength but narrowed in scope**.

Upgraded because the AIExpertEngine source-path cluster, game-load construction marker, grammar/error taxonomy, persistent-fact phase, scenario AI filename method, and AI rule embedding fields jointly provide substantially stronger native evidence.

Narrowed because the generic `Parsing script` cluster is now classified primarily as FTS/test-harness parser evidence rather than `.per` evidence.

No causal promotion is made.

## Security disposition
All work remained immutable/static. No game installation files were modified. No debugger attachment, injection, hooks, memory modification, arbitrary UDP, unknown test execution, or XS was used. The pure `.per` architecture remains unchanged.

## Next discriminating investigation
The highest-value next target is now a PE-aware trace of the native AIExpert and scenario functions:

`getOrExtractPlayerAiRulesFileName -> AIExpert construction/load-game path -> loadRules -> rule-list creation`

The second target is:

`Evaluating Persistent Facts -> native fact evaluation loop -> stored fact representation -> rule consumption`

Only after those paths are structurally resolved should a microscopic pure-`.per` runtime sentinel be attempted.

## Promotion
No Layer 1 percentage change.
Layer 1 remains **89%**.
