# AEGIS Layer 1 — Native AI Path Function-Recovery Gate

Date: 2026-09-03
Build: 101.103.48987.0 / game build #180059 / Steam Build ID 24094652
Executable SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4

## Question
Can the scenario AI path be promoted from string/metadata structure to a native causal function path linking player AI identity, scenario AI data, and AIExpert rule loading?

## Prior evidence
The exact retail executable contains AIExpert diagnostics for `loadRules(listId,file)`, scenario AI fields including `mAiRulesFileData`, `mAiRulesType`, and `aiRulesFileDataSize`, player fields including `mAiScriptBaseName` and `mIsCustomAI`, and the native symbol `BaseScenario::getOrExtractPlayerAiRulesFileName(...)`.

## Pass performed
A PE byte-level targeted scan was repeated against the exact verified executable. Targets included the AIExpert loader diagnostic, persistent-fact instrumentation, player AI identity fields, scenario AI-rule fields, and the scenario filename resolver. Exact offsets were recorded in `NATIVE_AI_PATH_OFFSETS_2026-09-03.txt` during the pass; the large contextual extraction was intentionally discarded because raw ASCII decoding of executable code/data produced high-noise output and was not suitable as evidence.

## Results
- `mAiScriptBaseName`: 2 occurrences, offsets 52852720 and 52853169.
- `mAiRulesFileData`: 1 occurrence, offset 52414985.
- `mAiRulesType`: 1 occurrence, offset 52414392.
- `aiRulesFileDataSize`: 1 occurrence, offset 52414896.
- `getOrExtractPlayerAiRulesFileName`: 4 occurrences, offsets 67813189, 67813398, 68184125, 68184396.
- `loadRules for listId=%d, file=%s`: 1 occurrence, offset 52207960.
- `Evaluating Persistent Facts`: 2 occurrences, offsets 52210504 and 52210545.
- `Fact[%d] evaluated persistently to %s`: 1 occurrence, offset 52212336.

## Negative result
The pass did not recover a trustworthy function body address, caller edge, ABI, or control-flow path from these byte/string locations. A mangled-symbol search for candidate `loadRules` forms also did not produce a usable callable address. This is an instrumentation/format limitation, not evidence that the native functions do not exist.

## Evidence interpretation
The structural model remains supported:

`player AI identity + scenario AI-rule data -> BaseScenario AI resolution -> AIExpert rule loading`

But the causal arrows remain unpromoted. String offsets alone cannot establish that one function calls another, nor that a particular field is read at a particular transition.

## Quality-control decision
No Layer 1 proposition is promoted from this pass. No runtime invocation was guessed. No binary modification, injection, hook, debugger attachment, memory modification, or arbitrary test-harness protocol activity was performed.

## Next discriminating instrument
Use an actual PE-aware disassembly database with recovered function boundaries and xrefs, or a symbol-equivalent build artifact, to resolve the resolver body and its callers. Separately recover the AIExpert persistent-fact loop and identify the storage operation following persistent evaluation.

## Layer status
Layer 1 remains 89%.
