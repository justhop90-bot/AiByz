# AEGIS Layer 1 — Native Function Recovery Gate — 2026-09-03

## Result

The planned PE-aware recovery instrument could not be executed because the installed IDA Free 9.4 deployment exposes `ida.exe` only; no `idat64.exe`/`ida64.exe` batch executable was present under the inspected installation root.

## Evidence boundary

The exact retail executable remains verified. String/symbol archaeology still establishes the native BaseScenario and AIExpert vocabulary, but this pass did not recover a callable function address, xref, or control-flow edge.

## Disposition

No function address was inferred from string offsets. No binary modification, injection, hook, debugger attachment, memory modification, or guessed invocation was performed.

## Next discriminating instrument

Use the installed GUI-capable IDA deployment or another PE-aware static disassembler available on the authorized machine to recover code/data boundaries and xrefs for `getOrExtractPlayerAiRulesFileName`, `mAiRulesFileData`, `mAiScriptBaseName`, `loadRules`, and the persistent-fact evaluation region.

Layer 1 remains 89%.
