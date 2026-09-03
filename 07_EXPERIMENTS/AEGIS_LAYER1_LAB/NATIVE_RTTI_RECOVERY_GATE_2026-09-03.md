# Native RTTI Recovery Gate — 2026-09-03

## Status
Layer 1 remains 89%. No causal promotion.

## Question
Can PE-aware tooling recover callable function boundaries or xrefs for the native BaseScenario and AIExpert targets identified by string archaeology?

## Controlled binary
- File: `AoE2DE_s.exe`
- Game build: `#180059`
- Executable version: `101.103.48987.0`
- Steam Build ID: `24094652`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Size: `71648568` bytes

## Instruments
Ghidra 12.1.3 was used through its PE loader. A no-analysis targeted scan independently reproduced the previously identified target data locations.

Targets reproduced:
- `getOrExtractPlayerAiRulesFileName`: `0x1440AD945`, `0x1440ADA16`, `0x14410823D`, `0x14410834C`
- `mAiRulesFileData`: `0x1431FDE09`
- `mAiScriptBaseName`: `0x143268BF0`, `0x143268DB1`
- `loadRules`: `0x1431CB558`
- persistent-fact strings: `0x1431CBF48`, `0x1431CBF71`, `0x1431CBF68`

Ghidra's reference manager returned zero direct references to these literal data locations.
## Observation
The `getOrExtractPlayerAiRulesFileName` occurrences are embedded in decorated MSVC compiler metadata, including a lambda/type context. They are not ordinary exported function symbols. `AIExpertEngine::` occurrences likewise sit in a diagnostic/source-metadata region containing `AIExpertEngine.cpp`, rule-element/debug identifiers, and parser diagnostics.

A direct raw-byte scan found no literal `. ?AVBaseScenario@@` or `. ?AVAIExpertEngine@@` type-descriptor strings in the exact spelling tested. This negative result does not establish absence of RTTI; the binary may use decorated variants, folded metadata, or references that require PE-aware interpretation.

## Discriminating interpretation
H1: literal strings can be mapped directly to functions — rejected for these targets.
H2: compiler metadata/type structures must be reconstructed before callable boundaries can be recovered — supported.
H3: absence of direct data references means the native subsystem is unused — rejected as an inference; the same targets are supported independently by coherent native AIExpert/BaseScenario evidence.

## Tooling boundary
A full Ghidra auto-analysis attempt reached the disassembly-entry-point phase and exceeded the available analysis window. The no-analysis targeted import succeeded and is therefore the validated fast path for PE mapping. IDA Free 9.4 GUI exists, but the installed package lacks the expected headless `idat64.exe`; automated GUI-script execution has not yet been validated.

## Security
No binary modification, DLL injection, hooks, debugger attachment, process-memory modification, or installed AI-corpus modification was performed.

## Promotion
No callable function address, call edge, scheduler edge, or persistent-fact storage edge is promoted by this pass. The finding is an instrumentation/recovery result only.

## Next discriminating test
Recover MSVC RTTI/type metadata and candidate vftables for `BaseScenario` and `AIExpertEngine`, then inspect only the resulting local function bodies and callers. The objective is to establish an actual code-flow edge into AI filename extraction and `AIExpertEngine::loadRules`, followed by the persistent-fact phase.
