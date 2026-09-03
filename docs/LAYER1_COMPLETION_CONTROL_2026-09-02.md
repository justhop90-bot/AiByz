# AEGIS Layer 1 Completion Control — Final Investigation Position

**Final investigation position:** 89%  
**Investigation phase:** CLOSED / HANDOFF  
**Completion certification:** NOT SATISFIED

## Purpose

This document is the active control record for Layer 1 (Machine Understanding). It defines the evidentiary standard and the conditions under which the layer may be called complete. The investigation phase is now closed at 89%; this document remains the governing gate for any future evidence that reopens the layer.

The objective is not to produce a plausible explanation of AoE2DE. The objective is to establish a reproducible, evidence-bounded machine model for the exact controlled executable and to document every unresolved proposition that could affect implementation.

## Evidence ladder

1. RUNTIME-IDENTITY — exact installed executable identity and cryptographic hash.
2. SCRIPT-CONSUMED — behavior demonstrably exposed to or consumed by AI scripts.
3. NATIVE-VOCABULARY — strings, signatures, diagnostics, RTTI-like names, or embedded identifiers.
4. SOURCE-CONTRACT — independent source/archive evidence describing a contract or interface.
5. NATIVE-IMPLEMENTATION — verified native function body, call relationship, field access, or state transition in the controlled binary.
6. RUNTIME-EXPERIMENT — controlled observation on the controlled build.
7. INFERENCE — interpretation supported by convergent evidence but not directly demonstrated.
8. HYPOTHESIS — plausible explanation awaiting evidence.
9. HISTORICAL — preserved artifact whose relationship to the controlled runtime is not established.

A weaker evidence class may motivate investigation but may not silently become a stronger class.

## Non-negotiable rules

- A symbol name is vocabulary, not semantics.
- A declaration is a contract surface, not an implementation.
- A string reference is not a call graph.
- A decompiler rendering is not automatically correct source.
- A replay field is an observation, not necessarily the underlying engine state.
- Absence is not destruction.
- Command issuance is not execution success.
- Execution success is not strategic postcondition success.
- A validator result is not automatically a runtime result.
- Historical source is not automatically shipped-runtime source.
- Intuitive naming never promotes a claim.
- A metadata pointer near an API signature is not semantic API ownership.
- `.pdata` function geometry is structural evidence, not semantic naming.
- A PDB filename is not authenticated symbol evidence without GUID/age matching.
- A claim is promoted only when evidence demonstrates the proposition itself.

## Controlled runtime

Executable: `[LOCAL_AOE2DE_INSTALL]\AoE2DE_s.exe`  
Version: `101.103.48987.0`  
Size: `71,648,568` bytes  
SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`  
PE: PE32+, x86:LE:64 Windows

The exact local installation path is intentionally redacted from the public record. All native claims in this control record refer to this build unless explicitly marked otherwise.

## Layer 1 completion gate

Layer 1 is complete only when the following are either CONFIRMED/STRONG with adequate evidence or explicitly closed as bounded unknowns that cannot affect the architecture:

- executable identity is fixed;
- script acquisition/loading boundary is mapped;
- rule representation is characterized;
- scheduler ordering/interval semantics are bounded;
- dynamic rule lifecycle is characterized;
- interpreter boundary is bounded;
- facts/goals/SNs/timers/search state are typed and range-bounded where required;
- UP APIs used by AEGIS have an argument/return/effect ledger;
- action/order/target execution boundaries are mapped;
- failure/invalidation/completion semantics are mapped;
- native object/unit identity topology is characterized to the degree required by implementation;
- replay-observable identifiers are mapped to native concepts only where evidence permits;
- critical native call relationships are independently verified;
- negative evidence and failed searches are preserved;
- reproducibility metadata exists for every major native pass;
- open questions have explicit promotion tests;
- architecture contains no undocumented dependency on a stronger claim than the evidence supports.

**XS is explicitly excluded from the completion gate.** XS may remain machine archaeology when useful, but it is not a ByzBot implementation dependency and cannot block Layer 1 completion.

## Final investigation findings

### `.pdata` function geometry

The controlled PE contains 166,741 physical 12-byte `.pdata` slots; 166,730 contain non-zero runtime-function records and 11 are trailing zero padding. Valid starts are unique and monotonically ordered, with no overlaps among valid runtime-function intervals. Function interval statistics: minimum 1 byte, median 91 bytes, mean 275.17 bytes, maximum 106,696 bytes; aggregate interval coverage is 45,879,189 bytes, approximately 88.88% of `.text` raw size.

This provides an independent native coordinate system for targeted instruction/data-flow archaeology. It is not a semantic inventory of 166,730 source-level functions.

### CodeView/PDB

The executable contains CodeView `RSDS` data with PDB GUID `b04f37aa-ccf9-48da-ad19-583ffb4bb36d`, age `1`, and an embedded build-system path ending in `AoE2DE_s.pdb`. No matching local PDB was established. A future PDB may be used only after GUID/age authentication against the controlled executable.

### AI diagnostic anchors

Correct section-aware mapping plus full `.text` Capstone scanning found zero RIP-relative references to seven selected AI diagnostic/source anchors; executable-wide exact 64-bit-pointer scanning also found zero occurrences. This is bounded negative evidence for those representations, not proof of absence of the AI subsystem.

### Metadata pointer false positive

A correctly mapped metadata-area pointer led to `0x1417FF3E0`, a valid `.pdata` function start. Direct disassembly showed cleanup/destructor-like behavior. The candidate is therefore rejected as an XS API implementation association. Pointer proximity does not establish semantic ownership.

### Ghidra

The historical Pass33 workspace is preserved. The separate controlled headless analysis successfully imported/saved the exact executable but timed out at 1800 seconds during `Disassemble Entry Points` with `CreateThunkFunctionCmd` / `body must contain the entry point`. Broad analysis completion is therefore not certified; targeted `.pdata`-bounded verification is the preferred method.

## Final causal frontier

The remaining 11% is concentrated in:

1. rule-loader/parser implementation boundary;
2. rule-representation ownership/mutation;
3. persistent-fact result mutation and freshness/cache semantics;
4. scheduler comparator/interval transition path;
5. rule/handler-to-native-action bridge;
6. `CurrentOrder -> CurrentAction` mutation chain;
7. action failure/invalidation/completion propagation;
8. required object-identity lifecycle edges;
9. one experimentally predictive `.per` end-to-end path.

No one of these may be declared closed from vocabulary alone.

## Final architectural consequence

The most defensible authority model remains:

`OBSERVATION -> BELIEF / MACHINE FACTS -> STRATEGIC INTENT -> TACTICAL REQUEST -> NATIVE VALIDATION / ACCEPTANCE -> EXECUTION -> OBSERVED RESULT -> RECONCILIATION -> RETAIN / RETRY / RETARGET / REPLACE / ABANDON`

This is an engineering architecture derived from convergent evidence. It is not a claim that the shipped engine literally contains these exact classes.

## Six-month re-entry

A returning engineer should begin with `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`, then the research index, predictive standard, this completion control, evidence matrix, machine monograph, native archaeology/QC records, atomic facts, and open questions. The final investigation position is **89%** until new evidence demonstrates a material change.

## Change control

Every future Layer 1 finding must be dated, tied to a concrete artifact or experiment, classified by evidence level, state what it proves, state what it does not prove, and identify the promotion/demotion path. Corrections amend prior claims; they do not erase the historical reasoning that produced them.
