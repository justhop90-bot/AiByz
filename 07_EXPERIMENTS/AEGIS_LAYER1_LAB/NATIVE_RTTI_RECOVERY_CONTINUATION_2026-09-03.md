# Native RTTI recovery gate — continuation
## Question
Can the decorated BaseScenario/AIExpertEngine material be promoted to callable function addresses through direct pointer evidence?
## Exact build
AoE2DE_s.exe; 101.103.48987.0; SHA-256 6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4.
## Observations
PE-aware scan confirms BaseScenario.cpp at RVA 0x31fd916; AIExpertEngine.cpp at RVA 0x31cbe90; getOrExtractPlayerAiRulesFileName decorated metadata at RVAs 0x40ad945, 0x40ada16, 0x410823d, 0x410834c; loadRules diagnostic at RVA 0x31cb558; mAiRulesFileData at RVA 0x31fde09.
Exact 64-bit absolute-pointer searches for these literal data addresses returned zero hits.
The getOrExtractPlayerAiRulesFileName occurrences are explicitly lambda/type metadata, not function bodies.
RunTestScenario likewise appears in lambda/type metadata, not a recovered body.
## Interpretation
The current evidence supports compiler-generated metadata/type records and native source provenance, but not callable entry points or call edges. No function address is promoted.
## Next discriminating test
Use a PE-aware disassembler with completed function analysis, or manually reconstruct MSVC RTTI/vftable structures and local instruction windows. Prefer the installed GUI IDA if its automation/UI path can be controlled; otherwise continue with Ghidra using a narrowly scoped analysis strategy.
## Security
No binary modification, injection, hooks, debugger attachment, memory modification, or installed AI-corpus modification.
## Promotion
No Layer 1 causal promotion. Layer 1 remains 89%.
