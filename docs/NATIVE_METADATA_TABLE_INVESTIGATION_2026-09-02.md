# Native API Metadata Table Investigation — 2026-09-02

## Status

**Layer 1 native archaeology: active. Evidence state: structural metadata confirmed; registration/dispatch path unresolved.**

This dossier records the post-disassembly investigation of the native XS/API signature region in the exact `AoE2DE_s.exe` build. It intentionally separates executable observations from hypotheses about how the scripting binding is implemented.

## 1. Runtime identity

Executable:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`

Known identity from the controlled machine baseline:

- PE32+ / x86-64
- image base: `0x140000000`
- file size: `71,648,568` bytes
- file/product version: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

The executable identity is unchanged from the Layer 1 machine baseline.

## 2. Investigation question

The immediate question was:

> What native structure references the API signature metadata, and can that structure lead us toward the binding registration or dispatcher?

The investigation began with the API family because the signatures provide unusually strong native vocabulary for object identity and AI-facing state access.

## 3. API signature cluster

The following signature strings were recovered from native read-only data:

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

The strings occur in a dense signature/name region rather than as isolated ordinary application strings.

## 4. Structural observation

For the object-identity family, the binary contains a repeated two-string pattern:

1. short API name, e.g. `xsGetUnitObjectId`
2. signature form, e.g. `int xsGetUnitObjectId(int32_t unitId)`

The entries are contiguous and ordered with neighboring APIs. This is strong evidence for an API metadata vocabulary/registry surface.

It does **not** by itself prove the existence of a conventional C/C++ array of `{name, signature, function}` records.

## 5. Disassembly experiment

A clean disposable Ghidra project was created from the exact executable. The experiment explicitly disassembled `.text` before reference inspection, avoiding dependence on the noisy full-analysis Pass33 state.

Ghidra disassembly completed successfully.

Instruction-level reference inspection for the exact addresses of the individual API name strings returned:

`0 direct instruction references`

for every tested target in the API family.

Therefore the current evidence does not show ordinary `.text` instructions directly addressing these individual strings.

## 6. Independent raw-binary validation

A separate raw-byte search tested the 32-bit image-relative RVAs of the same strings throughout the executable. No exact four-byte occurrences were found for any tested target.

Earlier testing also found no exact absolute 64-bit pointer occurrences.

The negative results are mutually consistent:

- no exact absolute 64-bit pointer representation observed;
- no exact 32-bit RVA representation observed;
- no Ghidra instruction reference recovered to the individual string addresses.

These results rule out only the tested direct representations. They do **not** rule out indirect addressing, table-level references, computed references, hashes, relocation-mediated construction, runtime registration, or a generic string lookup/registration mechanism.

## 7. Important adjacent native evidence

The same native data corpus contains:

- `obj->id`
- `uniqueID`
- source-path remnants for `UnitAIModule.cpp`
- source-path remnants for `TribeUnitAIModule.cpp`
- diagnostics containing `CurrentAction`
- diagnostics containing `CurrentTarget`
- diagnostics containing `CurrentTargetType`
- diagnostics containing `Current Position`
- diagnostics describing attackers and closest attackers

The object-construction diagnostic is particularly important because it prints three distinct values:

`obj_id`, `obj->id`, and `uniqueID`.

This demonstrates that the native program itself distinguishes these labels at the source/debug vocabulary level. It does not yet establish their equality, lifetime, or cross-layer mapping.

## 8. Current evidence classification

### Demonstrated

- The executable contains a dense native API name/signature vocabulary.
- Object/unit identity APIs are present as native metadata.
- Unit/object class/type/copy/object-ID and garrison relationships are represented in the API vocabulary.
- Native AI-module source remnants exist in the executable.
- Native diagnostics distinguish `obj_id`, `obj->id`, and `uniqueID` in their formatting vocabulary.
- The tested API strings have no recovered direct instruction references in the controlled disassembly experiment.

### Not demonstrated

- The concrete registration record layout.
- The native function address corresponding to any `xsGet*` API.
- The dispatcher/lookup implementation.
- Whether registration is static, constructor-driven, generated, or dynamically assembled.
- Whether the short name and signature are stored in a single record.
- Whether a hash or another identifier is used instead of direct string pointers.
- The exact relationship between `obj_id`, `obj->id`, and `uniqueID`.
- Whether an API's script-visible argument type exactly equals its internal argument type.

## 9. Working hypotheses, explicitly unpromoted

### H1 — Table-level registration

The signature/name strings belong to a larger registry whose records are referenced indirectly or through a generated table.

### H2 — Generic registration routine

A startup/initialization routine may enumerate metadata and register bindings through a generic mechanism, making individual string references difficult to recover as direct callers.

### H3 — Hash/lookup registration

The runtime may convert names to hashes or other compact identifiers and subsequently dispatch through an indexed structure.

### H4 — Generated/native binding layer

The metadata may be emitted by a binding generator or macro system, with the executable retaining source-like signature strings while the callable implementation is stored elsewhere.

None of these hypotheses has been promoted to fact.

## 10. Next experiment

The correct next search target is therefore **not** the individual strings. It is the surrounding metadata structure and its references.

Priority sequence:

1. map the complete contiguous signature/name region;
2. identify alignment/padding boundaries;
3. identify neighboring non-string bytes and candidate record boundaries;
4. test candidate pointer/RVA/hash representations against the complete region rather than one string;
5. locate references to the containing block or candidate table;
6. inspect functions surrounding recovered references;
7. search for registration/initialization loops using multiple API names/signatures as anchors;
8. only then attempt to identify the callable implementation for `xsGetUnitObjectId`.

## 11. Methodological significance

The zero-reference result is not a dead end. It changes the abstraction level of the investigation.

The previous question was:

`Who references this string?`

The better question is now:

`What native mechanism consumes this entire API metadata corpus?`

This is consistent with the Layer 1 predictive standard: recover the causal mechanism rather than equating vocabulary presence with executable semantics.

## 12. Layer 1 consequence

The object-identity dossier can safely state that the executable contains native identity vocabulary and that the API surface is structurally organized. It cannot yet state that the recovered `xsGet*` names have been traced to their native implementations.

The machine-understanding frontier therefore remains:

`API metadata -> registration/lookup -> dispatcher -> native implementation -> object model`

The unresolved middle of that chain is now the highest-value native archaeology target.
