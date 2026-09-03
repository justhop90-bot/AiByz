# Native RTTI / vftable reconstruction gate — 2026-09-03

## Question
Can MSVC RTTI/type metadata recover callable BaseScenario or AIExpertEngine function entries?

## Exact build
AoE2DE_s.exe; 101.103.48987.0; SHA-256 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.

## Method
PE-aware mapping of the exact executable followed by exact decorated-name searches and pointer-pattern checks. No binary modification or runtime instrumentation was used.

## Observations
Image base is 0x140000000. Sections include .text, .rdata, .data, .pdata and _RDATA. Exact class-name searches for MSVC RTTI spellings `.?AVBaseScenario@@`, `.?AVAIExpertEngine@@`, `.?AVAIExpert@@`, `.?AVGamePC@@`, and `.?AVScenarioPlayer@@` returned zero literal hits.

The binary does contain decorated lambda/type metadata associated with `getOrExtractPlayerAiRulesFileName@BaseScenario`, including the Result/TypedIndex/String/Age2Frame/Object<UI> signature context. `RunTestScenario@GamePC` is similarly present through lambda/function-object metadata.

The previously recovered `AIExpertEngine::` diagnostics remain present at RVAs 0x31CBDE0 and 0x31CC058. Absolute 64-bit pointer scans against the target literal addresses returned no direct pointer hits.

## Interpretation
The expected simple MSVC class TypeDescriptor route is not available from these exact literal names. The decorated lambda records are metadata, not callable entry points. This does not disprove RTTI/vtables; it means the current evidence is insufficient to reconstruct them from class-name literals alone.

## Decision
Do not promote any function address or call edge. The RTTI/vftable hypothesis remains open but the direct class-name search route is exhausted for this build.

## Next discriminating route
Use completed PE disassembly on a constrained address region, beginning from `.pdata` function ranges that overlap the native AIExpert/BaseScenario source-provenance clusters, then identify code that references the relevant diagnostic strings. Cross-check candidate functions against unwind ranges and instruction-level references. This avoids requiring class RTTI strings to be directly referenced.

## Security / provenance
Exact executable hash checked. No hooks, injection, debugger attachment, memory modification, patching, or installed-AI modification. Temporary scripts are working artifacts only.

## Promotion
No Layer 1 causal promotion. Layer 1 remains 89%.
