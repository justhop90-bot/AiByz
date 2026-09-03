# Native `.pdata` Member/Data Recovery Gate — 2026-09-03

## Status
- Exact executable: `AoE2DE_s.exe`
- Game build: `#180059`
- Executable version: `101.103.48987.0`
- Steam Build ID: `24094652`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Layer 1: **89%**

## Question
Can native `.pdata` function intervals and data-access instructions recover callable BaseScenario/AIExpert functions from the previously identified member/type metadata?

## Prior evidence
The exact binary contains coherent native AIExpert/BaseScenario source provenance, AI rule grammar diagnostics, embedded/loose AI-rule data diagnostics, `mAiScriptBaseName`, `mAiRulesFileData`, and persistent-fact phase strings. Literal diagnostic targets had zero direct RIP-relative `.text` references.

## Method
1. Parsed the PE exception directory directly.
2. Recovered 166,730 valid x64 `RUNTIME_FUNCTION` records from `.pdata`.
3. Built the set of actual function-start RVAs from those records.
4. Searched `.rdata`/`.data` for 64-bit pointers to those real function starts.
5. Inspected exact target bytes around the relevant native metadata/data locations.
6. Did not infer a function from metadata proximity.

## Observation
The `.pdata` directory is structurally valid and contains 166,730 non-zero runtime-function records.

A broad `.rdata`/`.data` scan found 70,952 64-bit values that point at `.pdata` function starts. This confirms that ordinary function-pointer/vtable-like structures exist in the binary, but the broad count is not itself class attribution.

For the selected diagnostic/member target addresses, the target literal addresses themselves do not appear as absolute 64-bit pointers. No direct callable address was therefore recovered from the target literals.

The bytes surrounding `getOrExtractPlayerAiRulesFileName` are dominated by MSVC decorated lambda/type metadata. The bytes surrounding `mAiRulesFileData` contain member-name/debug metadata followed by additional data values; these have not been attributed to a class layout or function without PE-aware structure recovery.

## Interpretation
This pass establishes a viable lower-level recovery substrate: the executable has a large, valid `.pdata` function table and many real function-pointer targets. However, the selected member-name/diagnostic strings are not directly referenced as ordinary absolute pointers. Therefore the immediate problem is attribution: identify the data structure or code object that owns these metadata records before mapping function pointers to BaseScenario or AIExpert.

## Competing hypotheses
- H1: the relevant class/vtable structure exists nearby but requires RTTI/vftable pattern recovery rather than string-pointer search.
- H2: optimized retail code references the relevant metadata indirectly through generated registration/type tables.
- H3: some of the decorated lambda/member names are retained metadata with no runtime data reference at all.

## Discriminating next test
Use the 70,952 real function-pointer targets as candidates, but constrain them with MSVC RTTI/vftable signatures and nearby TypeDescriptor/CompleteObjectLocator patterns. Then inspect only candidate function ranges for accesses to known AIExpert/BaseScenario object fields or calls into the AI parser/fact subsystem.

## Negative controls
- No raw string address was treated as a function.
- No `.pdata` proximity was treated as semantic attribution.
- No binary modification, injection, hook, debugger attachment, memory modification, or installed AI-corpus modification.

## Promotion
No Layer 1 causal promotion. This is structural recovery evidence only. The persistent-fact execution chain remains unresolved.

## Repository decision
Record as a dated laboratory gate. Do not replace earlier reports; this result narrows the recovery strategy and supersedes only the assumption that direct target-string references are likely to reveal the functions.
