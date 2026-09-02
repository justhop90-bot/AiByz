# Layer 1 Native Archaeology Log — 2026-09-02

## Status

**Layer:** 1 — Machine Understanding  
**Branch:** `aegis/pass6-operationalization`  
**Scope:** Native executable archaeology and predictive machine-understanding baseline  
**Executable:** `AoE2DE_s.exe`  
**Analysis framework:** Ghidra 12.1.3 PUBLIC  
**Method:** Controlled, reproducible headless analysis plus targeted native-memory archaeology

---

## 1. Purpose

This document records the methodological transition from symbol-oriented native analysis to representation-aware native archaeology after direct symbol inventory failed to expose the target engine-facing API as ordinary Ghidra symbols.

The objective is not merely to locate familiar strings. The objective is to establish an evidence chain from executable representation to implementation, and ultimately to a predictive causal model of the machine sufficient to explain and experimentally predict behavior at the AI/runtime boundary.

The current investigation focuses on the native object/unit identity topology because identity is a prerequisite for reliable reasoning about AI observations, commands, lifecycle, replay correspondence, and postconditions.

---

## 2. Evidence discipline

The investigation uses the following evidence ladder:

1. **RUNTIME-IDENTITY** — exact executable and cryptographic identity.
2. **SCRIPT-CONSUMED** — content demonstrably consumed by the runtime/script system.
3. **NATIVE-VOCABULARY** — strings, symbols, diagnostics, or metadata embedded in the native executable.
4. **SOURCE-CONTRACT** — source/declaration material establishing an interface or contract.
5. **NATIVE-IMPLEMENTATION** — disassembly/decompilation demonstrating actual implementation behavior.
6. **RUNTIME-EXPERIMENT** — controlled execution demonstrating a proposition.
7. **INFERENCE** — reasoned interpretation constrained by evidence.
8. **HYPOTHESIS** — plausible but unverified explanation.
9. **HISTORICAL** — provenance useful for context but not current runtime truth.

A discovered string is therefore recorded as vocabulary until an implementation or controlled experiment establishes semantics. A declaration is treated as a contract surface, not proof of implementation. A replay field is treated as an observation, not as a complete representation of internal state.

---

## 3. Controlled analysis baseline

### 3.1 Target

Exact native executable:

`[LOCAL_AOE2DE_INSTALL]\AoE2DE_s.exe`

The exact local installation path is intentionally redacted from the public record. Build identity is fixed by version, size, and SHA-256.

The investigation is attached to the controlled Ghidra project:

`AEGIS_CONTROLLED_HEADLESS_2026-09-02/AOE2_NATIVE_CONTROLLED_20260902`

The historical Pass33 analysis remains preserved and is not modified by this work.

### 3.2 Reproducibility

Headless analysis was launched with Ghidra's `analyzeHeadless.bat`, using the controlled project and a bounded timeout. The initial full analysis did not emit a clean terminal marker before timeout, but the project database persisted and was subsequently reopened successfully. Subsequent targeted scripts were run against the persisted database with `-noanalysis` where appropriate.

This distinction is material: completion of a post-analysis script is not equivalent to completion of every background analysis phase. Each artifact therefore records its own provenance rather than inheriting an assumed global completion state.

---

## 4. Native symbol inventory

A controlled Java/Ghidra inventory enumerated the program's named symbols.

Observed result:

- Program: `AoE2DE_s.exe`
- Language: `x86:LE:64:default`
- Named symbols: **772**
- Total reported program symbols/entries: **122,946**

The inventory exposed numerous Wwise/audio-related names but did **not** expose the target engine-facing functions, such as `xsGetUnitObjectId`, as ordinary named Ghidra symbols.

### Interpretation

This is a methodological boundary, not evidence that the functions do not exist.

The negative result establishes that symbol lookup is insufficient for this API surface. The investigation therefore changed representation strategy: from symbol-name discovery to raw-memory, string-region, reference, and ultimately instruction-level analysis.

**Evidence level:** NATIVE-VOCABULARY / negative symbol evidence.

---

## 5. Native API vocabulary discovered

Targeted native-memory archaeology identified a contiguous signature/string region containing engine-facing API names including:

- `xsGetUnitObjectId(unitId)`
- `xsGetUnitCopyId(unitId)`
- `xsGetObjectCopyId(playerId, objectId)`
- `xsGetUnitClass(unitId)`
- `xsGetObjectClass(playerId, objectId)`
- `xsGetUnitType(unitId)`
- `xsGetObjectType(playerId, objectId)`
- `xsIsObjectValid(objectId, playerId)`
- `xsIsObjectAvailable(objectId, playerId)`
- `xsGetGarrisonedInUnitId(unitId)`
- `xsGetGarrisonedUnitIds(unitId)`
- `xsGetUnitAttributeTypesHeld(unitId, attributeType, ...)`
- `xsGetPlayerUnitIds(playerId, objectOrClassId, arrayId)`
- `xsCreateUnit(objectId, playerId, location, ...)`

Additional native vocabulary includes:

- `gameIDOfResourceObject(...)`
- `obj->id`
- `uniqueID`
- `UnitAI`
- `UnitAIModule.cpp`
- `TribeUnitAIModule.cpp`
- diagnostic fields/labels such as `CurrentAction`, `CurrentTarget`, `CurrentTargetType`, and `Current Position`.

### What this proves

The executable contains an explicit native vocabulary for:

- unit identity,
- object identity,
- copy identity,
- ownership,
- unit type/class,
- validity/availability,
- garrison relationships,
- player-to-unit enumeration,
- unit creation,
- and native unit-AI modules.

### What this does not prove

The strings alone do **not** establish:

- equality relationships among unit ID, object ID, copy ID, game ID, and `uniqueID`;
- field offsets for `obj->id`;
- lifetime or reuse rules;
- transformation semantics;
- ownership-change semantics;
- whether replay object references are equal to native object IDs;
- whether the API strings are registration metadata, documentation, diagnostics, or another runtime representation;
- the precise native implementation behind each API entry point.

Those propositions remain open until implementation/reference evidence or controlled experiments establish them.

---

## 6. Why ordinary Ghidra data xrefs failed

A first exhaustive defined-data traversal searched defined data for target strings and attempted to resolve references. It produced:

`defined_data=566194 hits=0 refs=0`

This result is retained as a negative control.

A subsequent raw-memory scan located the target byte sequences, but a direct reference lookup still produced no useful xrefs. Inspection showed why: the signatures occur in a contiguous raw/undefined native signature region rather than as individually defined Ghidra string-data objects.

The distinction is critical.

Ghidra's data-reference machinery operates on its defined representation. If the relevant bytes are not represented as a Ghidra `Data` object, querying references to a nominal string address can fail to expose the real instruction-level relationship.

A containing-data probe was therefore attempted using Ghidra's `Listing.getDataContaining(Address)`. It likewise did not produce useful references because the signature bytes were not represented as the expected defined data objects.

### Methodological conclusion

**Zero Ghidra data xrefs is not equivalent to zero native references.**

The appropriate next layer is instruction-level reference recovery, especially x86-64 RIP-relative addressing and registration-table traversal.

---

## 7. Raw native-region observation

The native-region probe established that the API signatures are physically embedded in a contiguous native string/signature area.

This materially changes the search strategy. Rather than treating each API name as an independent global string, the region should be treated as a structured native table or metadata block candidate.

The correct questions are now:

1. What instructions reference this region?
2. Is the region indexed by hash, pointer, ordinal, or name?
3. Is there a registration structure pairing signature/name with native function address?
4. What code consumes the region during initialization?
5. Can the consumer be traced to an exported/native dispatch mechanism?
6. Does the dispatch path reach object lookup code?
7. What native object structure is returned or queried?

These questions are more informative than additional broad string searches.

---

## 8. Object identity research boundary

The immediate machine-understanding target is the identity topology:

`script-visible unit identity -> native lookup -> object representation -> identity fields -> ownership/type/class -> lifecycle -> API result`

The investigation must also test the reverse/adjacent paths:

`native object -> unit representation -> script-visible identity`

`object -> copy identity -> transformation/replacement`

`object -> garrison relationship -> child unit identity`

`player -> object/class query -> enumeration -> returned unit/object identifiers`

`creation -> object insertion -> active object -> mutation -> transformation/removal`

No equality between these identifiers will be asserted solely from names. Each relationship must be promoted by implementation evidence or controlled runtime evidence.

---

## 9. Predictive causal-spine requirement

For each critical native mechanism, the final Layer 1 model must be able to express:

**PRECONDITION -> TRIGGER -> DISPATCH -> PROCESSING -> STATE TRANSITION -> POSTCONDITION**

For object identity, a satisfactory trace will identify, where applicable:

- caller/entry mechanism;
- argument representation;
- validation;
- lookup structure;
- object retrieval;
- identity field access;
- ownership/type/class resolution;
- return-value encoding;
- failure behavior;
- object lifetime implications;
- subsequent observable consequence.

The desired endpoint is predictive rather than descriptive: given sufficiently specified state and input, the investigator should be able to predict the relevant machine transition and then verify that prediction experimentally.

---

## 10. Programmer-intent reconstruction

The native code is treated as an engineered system rather than a bag of functions. For significant mechanisms, intent reconstruction will distinguish:

1. **Observed mechanism** — what the executable demonstrably does.
2. **Constraint** — technical or architectural condition shaping the mechanism.
3. **Design rationale** — why the implementation structure is consistent with a particular purpose.
4. **Supported intent** — rationale supported by callers, callees, ownership, repeated patterns, state lifetime, error handling, or source remnants.
5. **AI implication** — what the mechanism permits or prevents at the AI boundary.

The presence of `UnitAIModule.cpp` and `TribeUnitAIModule.cpp` is evidence that the executable retains native source/provenance vocabulary associated with unit-AI subsystems. It is not, by itself, proof of the complete original source architecture.

Competing hypotheses will remain explicit when evidence cannot discriminate between them.

---

## 11. Current hypothesis register

### H1 — API signatures are part of a native dispatch/registration representation
**Status:** plausible, unverified.  
**Evidence:** contiguous signature region containing multiple consistently formatted engine-facing APIs.  
**Required promotion:** instruction-level consumer/reference chain and dispatch implementation.

### H2 — Unit and object identities are intentionally distinct native concepts
**Status:** strongly supported at vocabulary level, implementation relationship unresolved.  
**Evidence:** paired `xsGetUnit*` and `xsGetObject*` API families plus `obj->id`, `uniqueID`, copy-ID vocabulary.  
**Required promotion:** implementation traces showing distinct storage/lookup paths or conversion functions.

### H3 — Native unit-AI modules participate in the same object/unit identity domain
**Status:** plausible, unverified.  
**Evidence:** `UnitAI`, `UnitAIModule.cpp`, `TribeUnitAIModule.cpp` and unit/object API vocabulary coexist in the executable.  
**Required promotion:** call/data-flow evidence connecting the modules to object/unit structures.

### H4 — Replay object references are native object IDs
**Status:** unverified and explicitly rejected as an assumption.  
**Evidence against premature promotion:** replay contains large numeric references and parser-side best-guess decoders; numeric equality alone is insufficient.  
**Required promotion:** controlled cross-layer correlation between replay event, runtime object, and native API result.

---

## 12. Preserved negative results

Negative results are first-class evidence because they constrain methodology.

Preserved artifacts include:

- `native_inventory.txt`
- `native_identity_xrefs.txt`
- `native_identity_neighborhood.txt`
- `native_string_pointers.txt`
- `native_string_probe.txt`
- `native_unitai_xrefs.txt`
- `native_identity_containing_xrefs.txt`
- `native_pointer_scan.txt` when produced by the current pointer-reference experiment

The absence of useful xrefs in these artifacts must not be summarized as absence of native implementation. They document failed representation assumptions and guide the next archaeological layer.

---

## 13. Immediate next investigation

The next experiment is instruction-level pointer/reference recovery.

The current pointer-scan experiment searches executable memory for exact little-endian 64-bit occurrences of target string addresses and source/debug-string addresses. Because x86-64 code commonly references static data through RIP-relative addressing rather than embedding absolute eight-byte pointers, a zero-result pointer scan will not terminate the investigation.

If direct pointer occurrences are absent, the next method is:

1. locate the signature region precisely;
2. identify nearby table/structure boundaries;
3. scan executable instructions for RIP-relative displacements resolving into that region;
4. cluster referencing functions;
5. decompile the strongest consumer candidates;
6. identify registration/dispatch structure;
7. trace selected API entries into implementation;
8. recover object lookup and identity field semantics.

This is the shortest path from native vocabulary to native implementation.

---

## 14. Layer 1 completion implications

Layer 1 will not be marked complete merely because the API surface has been catalogued.

Completion requires that all material AI-facing causal paths have no unacknowledged black boxes, including:

- simulation timing/update order;
- AI scheduler and dispatch;
- rule evaluation;
- fact/goal state mutation;
- command generation;
- command validation/dispatch/execution;
- object/unit identity;
- object lifecycle;
- relevant state structures;
- cross-layer state boundaries;
- failure/rejection behavior;
- replay observation boundaries.

The present investigation closes an important vocabulary/representation gap but does not yet close the implementation gap. The project therefore remains in active Layer 1 archaeology.

---

## 15. Engineering rule

**Do not build strategic abstractions on an identity model whose native semantics have not been demonstrated.**

A bot that cannot distinguish observation identity from native object identity, copy identity, lifecycle identity, and replay reference identity can produce internally coherent but mechanically false reasoning. The purpose of this archaeology is to eliminate that class of error before higher-level architecture is allowed to depend on it.

---

## Provenance

Primary evidence sources for this entry:

- controlled Ghidra project for `AoE2DE_s.exe`;
- generated Ghidra archaeology scripts under the controlled investigation directory;
- generated native inventory/reference artifacts;
- native executable raw-memory observations;
- previously established project evidence hierarchy and Layer 1 predictive standard.

This document intentionally distinguishes observed evidence from inference and hypothesis. Future findings should update hypotheses only when the new evidence demonstrates the proposition itself.
