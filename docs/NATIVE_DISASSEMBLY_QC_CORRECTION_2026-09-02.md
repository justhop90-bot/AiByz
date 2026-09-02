# Native Disassembly QC Correction — 2026-09-02

## Status

**Layer 1 evidence correction: active. Prior individual-string zero-reference result is downgraded pending complete native analysis.**

## 1. Why this correction exists

A prior Layer 1 dossier reported that a clean Ghidra disassembly experiment returned `0 direct instruction references` for selected `xsGet*` API strings. That statement was too strong as a claim about the executable as a whole.

The controlled re-test established that the headless disposable project did not retain a complete instruction listing between script invocations. A post-disassembly operand scan performed after reopening the project observed only **7 instructions** in the `.text` listing.

Therefore, a reference scan over that listing cannot be treated as exhaustive native reference coverage.

## 2. What remains valid

The following observations remain directly supported:

- the exact executable contains the targeted API name/signature strings;
- the strings occupy a dense native metadata/signature region;
- raw-byte searches found no exact tested 32-bit image-relative RVA representation and no exact tested absolute 64-bit VA representation for the selected strings;
- the executable contains native scripting vocabulary including `BXSSyscallEntry`, `mParameters`, `mCallerContext`, `mContext`, `numberParameters`, and related load/save diagnostics;
- native object-identity vocabulary includes `obj->id` and `uniqueID` alongside AI-module source remnants.

These findings do not depend on the incomplete instruction listing.

## 3. What is downgraded

The following claim is **not currently promoted to machine fact**:

> No native instruction references the targeted API metadata strings.

The evidence only demonstrated that no references were recovered by the specific incomplete Ghidra listing used in that experiment.

The earlier dossier should therefore be read as a structural metadata investigation, not as proof that the strings are statically unreferenced.

## 4. Corrected experiment

A fresh full-analysis Ghidra project was launched from an exact byte-identical copy of the executable.

Runtime identity was preserved by SHA-256:

`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

The full-analysis run is deliberately isolated from the historical Pass33 project and the disposable no-analysis project. Its purpose is to establish a persistent, analysis-complete listing suitable for instruction/reference interrogation.

At the time this dossier was written, the full-analysis process remained active and was producing native-analysis/thunk records. No conclusions are drawn from it until completion and verification.

## 5. Required verification after completion

1. confirm full-analysis process completion;
2. record analysis log and terminal state;
3. verify instruction coverage/count and function inventory;
4. rerun exact-string reference queries;
5. scan operands for targets in the complete `.rdata` metadata interval;
6. inspect data/reference chains for `BXSSyscallEntry` diagnostics;
7. compare direct string references with table-level and indirect representations;
8. preserve both positive and negative results with exact methodology.

## 6. Methodological rule added

A Ghidra command returning `success=true` is **not sufficient evidence of complete disassembly**.

For Layer 1 native-reference claims, the evidence record must establish:

`binary identity -> memory mapping -> analysis/disassembly completeness -> instruction coverage -> reference extraction -> target result`

If instruction coverage is incomplete or unverified, a zero-reference result is an **experiment result**, not an executable-level negative fact.

## 7. Consequence for the machine-understanding frontier

The investigation remains centered on:

`API metadata -> registration/lookup -> dispatcher -> native implementation -> object model`

The immediate priority is now to obtain a genuinely complete native instruction/reference substrate before interpreting absence of references.
