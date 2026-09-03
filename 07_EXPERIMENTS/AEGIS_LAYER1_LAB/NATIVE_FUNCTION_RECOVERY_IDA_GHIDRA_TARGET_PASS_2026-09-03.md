# AEGIS Layer 1 — Native Function Recovery Target Pass

Date: 2026-09-03
Layer 1 status: 89%
Build: AoE2DE #180059 / executable 101.103.48987.0 / Steam Build ID 24094652
Executable SHA-256: 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4

## Question
Can the native function boundary/call path for `BaseScenario::getOrExtractPlayerAiRulesFileName`, `mAiRulesFileData`, `mAiScriptBaseName`, `AIExpertEngine::loadRules`, and the persistent-fact phase be recovered from the controlled executable?

## Prior evidence
The exact executable contains coherent AIExpert and BaseScenario vocabulary, including `.per/.per2`, `loadRules for listId=%d, file=%s`, persistent-fact phase markers, `mAiScriptBaseName`, `mAiRulesFileData`, and the decorated `BaseScenario::getOrExtractPlayerAiRulesFileName` name.

## Instrument audit
IDA Free 9.4 is installed at `C:\Program Files\IDA Free 9.4\ida.exe`. No `idat.exe`/`idat64.exe` was present. GUI `ida.exe` accepts the documented `-A/-S` form but the attempted Python automation produced no marker/database artifact, so IDA scripting was not accepted as an active instrument in this pass. No conclusion about the binary was drawn from that failure.

Ghidra 12.1.3 remains available and has an existing controlled project. A targeted headless pass was executed against that project with analysis disabled, using a dedicated script directory to avoid duplicate-class contamination.

## Targeted Ghidra result
String-byte discovery recovered these native data locations:
- `getOrExtractPlayerAiRulesFileName`: 0x1440ad945, 0x1440ada16, 0x14410823d, 0x14410834c
- `mAiRulesFileData`: 0x1431fde09
- `mAiScriptBaseName`: 0x143268bf0, 0x143268db1
- `loadRules`: 0x1431cb558
- `Evaluating Persistent Facts`: 0x1431cbf48, 0x1431cbf71
- `Finished Evaluating Persistent Facts`: 0x1431cbf68

The Ghidra reference manager returned no direct references to these raw string-byte locations.

A focused raw PE scan also found zero exact 64-bit absolute pointers to all seven target locations.
A focused x86-64 RIP-relative displacement scan over `.text` found zero candidates targeting all seven exact locations.

## Important interpretation
This is a negative result about direct references to the *string-byte locations*, not evidence that the corresponding code is absent.

The previously captured raw context contains the full MSVC-decorated name for `BaseScenario::getOrExtractPlayerAiRulesFileName`, embedded among lambda/type metadata. This materially raises the probability that the undecorated name observed earlier is metadata/RTTI/debug-symbol vocabulary rather than a directly referenced executable symbol.

Therefore we reject the shortcut:
`string address -> function address`.
The next recovery target must be the metadata/function-pointer relationship, not another broad string scan.

## Competing hypotheses
H1: target names are debug/RTTI/type metadata; code is reachable through vtables or compiler-generated references.
H2: target names are diagnostic strings reached indirectly through lookup tables.
H3: Ghidra's current database lacks the relevant reference/function recovery because the prior analysis timed out/encountered thunk-body errors.
H4: the strings have no runtime code reference in the relevant path.

## Discriminating next test
1. Recover MSVC RTTI/type descriptors surrounding `BaseScenario`.
2. Locate BaseScenario vtables and enumerate function-pointer slots.
3. Match candidate function bodies against the decorated signature's class/return/parameter shape where possible.
4. Trace callers of candidate slots into scenario load/read code.
5. Repeat for AIExpertEngine persistent-fact and rule-loading objects.
6. Only promote a function boundary after an actual code/function/control-flow edge is recovered.

## Security / epistemic gate
No binary modification, DLL injection, hooks, debugger attachment, memory modification, arbitrary network protocol probing, or game-installation modification was performed.
IDA failure is an instrumentation limitation, not causal evidence.
Validator behavior remains non-runtime evidence.
Pure `.per` architecture remains unchanged.
Layer 1 remains 89%.
