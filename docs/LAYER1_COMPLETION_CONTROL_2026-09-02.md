# AEGIS Layer 1 Completion Control — 2026-09-02

## Purpose

This document is the active control record for completing Layer 1 (Machine) to the AEGIS engineering standard. It supersedes conversational memory as the operational checklist while preserving prior evidence rather than rewriting it.

The objective is not to produce a plausible explanation of AoE2DE. The objective is to establish a reproducible, evidence-bounded machine model for the exact controlled executable and to document every unresolved proposition that could affect implementation.

## Epistemic standard

AEGIS uses the following evidence ladder:

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
- A claim is promoted only when evidence demonstrates the proposition itself.

## Current controlled runtime

Executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`

Version: `101.103.48987.0`

Size: `71,648,568` bytes

SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

PE: PE32+, x86:LE:64 Windows

All native claims in this control record refer to this build unless explicitly marked otherwise.

## Layer 1 completion gate

Layer 1 is complete when all of the following are either CONFIRMED/STRONG with adequate evidence or explicitly closed as bounded unknowns that cannot affect the current architecture:

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
- XS registration and relevant capability boundaries are mapped;
- native object/unit identity topology is characterized;
- replay-observable identifiers are mapped to native concepts only where evidence permits;
- critical native call relationships are independently verified;
- negative evidence and failed searches are preserved;
- reproducibility metadata exists for every major native pass;
- open questions have explicit promotion tests;
- architecture contains no undocumented dependency on a stronger claim than the evidence supports.

## Native object/unit priority investigation

The highest-value remaining Layer 1 enrichment is identity topology, not generic parser development.

The recovered native vocabulary includes:

- `xsGetUnitObjectId`;
- `xsGetObjectType`;
- `xsGetObjectClass`;
- `xsGetObjectCopyId`;
- `xsGetObjectCount`;
- `xsGetObjectCountTotal`;
- `xsGetPlayerUnitIds`;
- `xsGetUnitOwner`;
- `xsGetUnitTargetUnitId`;
- `xsGetUnitTaskCount`;
- `xsGetGarrisonedInUnitId`;
- `xsGetGarrisonedUnitIds`;
- `xsIsObjectAvailable`;
- `xsIsObjectValid`;
- `gameIDOfResourceObject`;
- `obj->id`;
- `uniqueID`.

These names establish an object/unit-oriented native surface. They do not, by themselves, establish that every named identifier is the same namespace.

The investigation must therefore answer separately:

1. What is a unit identifier?
2. What is an object identifier?
3. What is a copy identifier?
4. What is a class identifier?
5. What is a type identifier?
6. What is a game ID?
7. What is a unique ID?
8. Is `unit_id -> object_id` a direct relation, lookup, or derived value?
9. Which identifiers are stable across a unit's lifetime?
10. Which identifiers are reused?
11. How are garrison, transform, deletion, creation, and ownership transitions represented?
12. Which replay action references correspond to which native identity namespace?

No answer may be promoted merely because the names appear intuitive.

## Ghidra control

The historical Pass33 project remains preserved and must not be overwritten or used as the sole reproducibility reference.

A separate controlled headless analysis was initiated on 2026-09-02 using Ghidra `12.1.3_PUBLIC` against the exact controlled executable. The project is isolated under:

`01_MACHINE\INVESTIGATION\AEGIS_CONTROLLED_HEADLESS_2026-09-02`

The purpose is differential validation: determine which observations reproduce independently of the original GUI session and which are artifacts of configuration, analysis state, or manual intervention.

The controlled run must record loader, language/compiler, analysis configuration, logs, completion state, discovered functions, entry points, externals, thunks, memory blocks, strings, references, and known analysis failures.

Broad analysis is index generation. It is not semantic proof. Critical claims require targeted verification.

## Parser boundary

Replay parsing is subordinate evidence. The parser can establish what was encoded/decoded in a recording; it cannot by itself establish the complete internal simulation state.

The current DE parser exposes object references in many action families. A fresh forensic parse on 2026-09-02 successfully decoded the reference recording with zero malformed records. It produced 6,858 ACTION records and 27,369 object-ID references spanning 4,411 distinct numeric values.

Some decoded values are clearly suspicious as literal stable object identities, including very large unsigned values. Therefore numeric replay references remain `OBJECT_REFERENCE_CANDIDATE` until their namespace and encoding are established.

## Promotion protocol for object tracking

A replay identity claim may be promoted only through one or more of:

- direct native implementation showing the namespace;
- repeated replay continuity with independent corroboration;
- explicit creation/destruction/transform/garrison evidence;
- controlled runtime experiment linking an observable reference to a known object;
- convergent native and replay evidence.

Absence alone never proves destruction. A missing reference may represent garrison, transform, observation limits, parser loss, ownership transition, deletion, or another unobserved state.

## Six-month re-entry requirement

An engineer returning after six months must be able to answer from this repository:

- which executable is authoritative;
- what evidence classes mean;
- which machine claims are confirmed versus inferred;
- how the rule scheduler is known to work;
- what UP and XS actually expose;
- what object/unit identity concepts exist;
- what replay parsing can and cannot prove;
- why the architecture has its current boundaries;
- what remains open;
- what experiment or native analysis promotes each open question;
- which artifacts are historical and which are controlled-runtime evidence.

If this cannot be answered from the repository, the documentation is incomplete regardless of how much text exists.

## Change control

Every new Layer 1 finding must be dated, tied to a concrete artifact or experiment, classified by evidence level, state what it proves, state what it does not prove, and identify the promotion/demotion path. Corrections amend prior claims; they do not erase the historical reasoning that produced them.
