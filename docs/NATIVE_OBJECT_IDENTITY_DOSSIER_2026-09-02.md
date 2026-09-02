# Native Object / Unit Identity Dossier — 2026-09-02

## Status

Active Layer 1 investigation. This dossier deliberately separates established machine vocabulary from demonstrated identity semantics.

## Why this dossier exists

AEGIS requires an object model that can survive replay reconstruction, strategic observation, production lineage, garrison, transformation, combat, and lifecycle analysis. The project previously had a useful conceptual lifecycle model, but the surviving native evidence is richer than the closure summary made explicit.

The central problem is not whether the engine has objects. The evidence strongly establishes an object/unit interface. The problem is identifying the exact namespaces and relationships without guessing.

## Evidence observed

The PASS29 native extraction contains the following function-like interfaces/signatures:

- `xsIsObjectAvailable(objectId, playerId)`
- `xsIsObjectValid(objectId, playerId)`
- `xsGetObjectClass(playerId, objectId)`
- `xsGetObjectCopyId(playerId, objectId)`
- `xsGetObjectType(playerId, objectId)`
- `xsGetObjectCount(playerID, id)`
- `xsGetObjectCountTotal(playerID, id)`
- `xsGetPlayerUnitIds(playerId, objectOrClassId, arrayId)`
- `xsGetUnitObjectId(unitId)`
- `xsGetUnitOwner(unitId)`
- `xsGetUnitTargetUnitId(unitId)`
- `xsGetUnitType(unitId)`
- `xsGetUnitClass(unitId)`
- `xsGetUnitCopyId(unitId)`
- `xsGetUnitGroupId(unitId)`
- `xsGetUnitPosition(unitId)`
- `xsGetUnitMoveTarget(unitId)`
- `xsGetUnitHitpoints(unitId)`
- `xsGetUnitBuildPoints(unitId)`
- `xsGetGarrisonedInUnitId(unitId)`
- `xsGetGarrisonedUnitIds(unitId)`
- `xsCreateUnit(objectId, playerId, location, ...)`

The extraction also contains `gameIDOfResourceObject`, `obj->id`, `uniqueID`, and `UnitAI`/AI-module vocabulary.

## What this establishes

At the NATIVE-VOCABULARY level, the shipped executable contains distinct concepts named as objects and units, with APIs relating them to type, class, copy, owner, target, position, group, tasks, hitpoints, build progress, garrison, and creation.

This is strong evidence for an object/unit-oriented simulation interface.

It does not yet establish the exact internal class hierarchy, storage layout, identity-generation algorithm, or equality relationship among all numeric identifiers.

## Namespace discipline

AEGIS currently treats these as separate semantic candidates:

`unit_id`

`object_id`

`object_type_id`

`object_class_id`

`copy_id`

`game_id`

`unique_id`

They must not be collapsed into one generic `id` field until implementation evidence demonstrates equivalence.

## Relationship currently permitted

The existence of `xsGetUnitObjectId(unitId)` establishes a native operation that maps a unit identifier to an object identifier or object-like identifier.

It does not, from the signature alone, establish whether the returned value is:

- the object's primary storage ID;
- a game-wide object number;
- a copy/generation identifier;
- a handle into another table;
- or another native identity representation.

The relationship therefore remains `UNIT_TO_OBJECT_RELATION`, not yet a fully specified identity theorem.

## Lifecycle implications

The presence of validity/availability queries and garrison/creation interfaces makes several lifecycle states mechanically plausible, but plausibility is not proof of transition semantics.

AEGIS therefore retains the following observation model:

`UNKNOWN -> OBSERVED -> CREATED_OR_INFERRED -> ACTIVE`

Possible active substates include movement, gathering, combat, production, garrison, transformation, damage, and idle.

Possible terminal or non-observed states include destruction, deletion, transformation, garrison, ownership change, hidden/out-of-observation, parser loss, and unknown.

The absence of an object reference is never sufficient by itself to choose among these states.

## Replay evidence boundary

The fresh 2026-09-02 parser run extracted object references from 6,858 ACTION records. It observed 27,369 object-ID references and 4,411 distinct numeric values.

The parser's action decoders intentionally discard some fields and contain documented guesses for some action families. Consequently, a decoded numeric value is an `OBJECT_REFERENCE_CANDIDATE`, not automatically a stable engine object ID.

Some fresh values are extremely large, including values near the unsigned 32-bit ceiling. Such values must be investigated as possible packed/sentinel/encoding artifacts before being interpreted as literal object identities.

## Required native promotions

The following propositions require targeted Ghidra or runtime evidence before promotion:

1. `unit_id -> object_id` exact mapping semantics.
2. Whether `object_id` is stable for the full object lifetime.
3. Whether IDs are reused after deletion.
4. Meaning of `copy_id`.
5. Meaning of `gameID`.
6. Meaning of `uniqueID`.
7. Whether `obj->id` equals any public/script-visible identifier.
8. Whether garrison preserves unit identity or replaces it.
9. Whether transformation preserves object identity, unit identity, both, or neither.
10. Whether ownership changes preserve identity.
11. How object creation allocates identity.
12. Whether replay action references directly encode the same namespace.

## Targeted Ghidra search plan

Priority targets:

- native implementations of `xsGetUnitObjectId`;
- native implementations of `xsGetObjectType`, `xsGetObjectClass`, `xsGetObjectCopyId`;
- native implementations of `xsGetUnitType`, `xsGetUnitClass`, `xsGetUnitCopyId`;
- native implementations of `xsIsObjectValid` and `xsIsObjectAvailable`;
- native implementations of garrison accessors;
- callers of object creation;
- references to `obj->id`;
- references to `gameIDOfResourceObject`;
- references to `uniqueID` in game-object contexts;
- structures/classes containing object identity fields;
- cross-references between UnitAI and object/unit accessors.

For each target, record address, function boundary confidence, decompiler/native instruction evidence, callers, callees, accessed fields, and competing interpretations.

## Runtime promotion experiments

If native implementation remains ambiguous, controlled experiments should create known objects, issue identity-querying script calls, transform/garrison/delete them, and record returned values across transitions. Each experiment must bind to the exact executable hash and exact AI source hash.

## Current conclusion

**CONFIRMED:** the controlled executable exposes a rich object/unit identity interface.

**CONFIRMED:** unit and object concepts are not merely aggregate counts; explicit per-unit/per-object queries exist.

**CONFIRMED:** a native unit-to-object query exists.

**NOT YET CONFIRMED:** the exact identity namespace relationship among unit ID, object ID, copy ID, game ID, unique ID, and replay action references.

**NOT YET CONFIRMED:** exact lifecycle transition semantics for creation, destruction, deletion, transformation, garrison, and ownership change.

This boundary is intentional. The correct next step is targeted native implementation recovery, not semantic extrapolation.
