# Pass 76 — Internal ID Allocation vs Production Object Identity

**Layer:** Layer 2 — research / archaeology only  
**Research completeness:** 99%  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%

## Mission

Attack the remaining `MakeObjectAction.obj_id → Entity.id` ambiguity after Pass 75, while preventing a subtler category error: confusing the replay library's own dynamically allocated model-object IDs with game-level object IDs.

## Finding

The `uncage-model` implementation makes the separation stronger than previously documented.

A model's `object()` value is the `ModelBorrow`/`ModelBorrowOwned` internal `id`. `Document::by_id()` resolves that same internal document namespace. Model references are populated by `Document::replace_ref()`, which registers a model in the document and stores the returned internal ID into the reference. The patcher therefore operates on a document-object namespace that is created by the replay library itself.

Consequently:

```text
REPLAY DOCUMENT ID
      ≠ semantically GAME ENTITY ID
```

Numerical equality could occur accidentally; it cannot be assumed as identity.

## Direct evidence

`ModelWithDocument::object()` returns the holder's internal `id`; it does not read an `Entity.id` field. `Document::by_id()` takes a `usize` and resolves a model from the document. fileciteturn675file0

`set_model`, `map_create_model`, `list_create_model`, and `list_insert_model` all call `Document::replace_ref(...)` and receive a returned `usize` model-object ID. This shows that model-object identity is assigned by the replay document when a model is registered. fileciteturn675file0

The patcher consequently reports `PatcherSelectorMatch.object_id = top.object()`, i.e. the document-model identity, not a field from the contained `Entity`. fileciteturn658file0

The playback example confirms the operational distinction: it receives `_match.object_id`, resolves it through `Document::by_id`, casts the model to `Entity`, and then separately reads `ent.id`; `ent.id` is what it stores in `prev_value` for entity-level tracking. fileciteturn656file0

## Revised identity taxonomy

There are now at least four relevant identity domains:

```text
I1 = patcher/document model-object ID (usize)
I2 = World.entities map key (i32)
I3 = Ref target, which points into I1
I4 = Entity.id (i32), the game entity field
```

Production introduces another field:

```text
I5 = MakeObjectAction.obj_id (i16)
```

The strongest proven relationships are:

```text
I3 → I1
I1 → Entity model
Entity model → I4
```

The following remain unproven:

```text
I2 = I4
I5 = I4
I5 = I1
I5 = I2
```

This is the cleanest formulation yet of the identity problem.

## Why this matters for object-birth archaeology

A selector that fires on `World.entities` creation is a real creation observation at the model layer. But its `object_id` is not itself enough to establish the game's entity identity. The forensic procedure must resolve the model and extract `Entity.id` from the resulting entity model.

Likewise, a `MakeObjectAction` is a production-action observation. Its `obj_id` cannot be matched against a selector's internal `object_id` unless the producer semantics explicitly establish that relationship. More importantly, matching two numbers is not proof if they came from different namespaces.

Therefore the correct empirical join is:

```text
MakeObjectAction
    obj_id = X

        JOIN only if semantic bridge proven

Entity
    id = Y
```

and not:

```text
if X == selector.object_id:
    assume same object
```

## Production model remains intact

The building model contains a reference to `current_production_queue_action` and a `production_queue`. The queue record contains `unit_id`, `tech_id`, and `unit_count`. `MakeObjectAction` contains `obj_id` and `work_done`. These fields remain useful for reconstructing production state, but field presence alone does not establish cross-namespace identity. fileciteturn663file0 fileciteturn661file0

## New forensic rule

**Never join replay-model object references to game entity identity by numeric equality alone.**

A valid join must use one of:

1. direct source semantics establishing the identity relation;
2. a library-provided reference from the action model to the entity model;
3. a state transition trace that proves the two fields refer to the same object across creation and subsequent mutation;
4. an independently validated engine/debug oracle.

## Highest-value next target

The research target is now narrower than ever:

```text
Locate the source-side decoder/populator for MakeObjectAction.obj_id.
```

Search specifically for:

- patch generation for model type 23;
- serialization/deserialization of action fields 7 and 8;
- CADE/native-to-model conversion;
- code that constructs `MakeObjectAction` instances;
- code that interprets action type/state and object IDs;
- any model documentation generated from native structures.

If no such source exists in the repository, the remaining bridge should be classified as an empirical/native-engine question rather than a replay-model question.

## Hostile QC

Rejected:

- `PatcherSelectorMatch.object_id == Entity.id`.
- `World.entities` key == `Entity.id` without producer evidence.
- `MakeObjectAction.obj_id == Entity.id` from naming alone.
- numeric equality between two IDs as semantic proof.
- a created model-object selector match as proof of a specific train command.
- `work_done` as an assumed completion threshold.

## Evidence ledger

| Proposition | Grade |
|---|---|
| Replay document assigns its own model-object IDs | DIRECT |
| `object()` exposes the internal model-object ID | DIRECT |
| `Document::by_id()` resolves that namespace | DIRECT |
| Model references point into that internal namespace | DIRECT |
| Patcher selector matches expose internal object IDs | DIRECT |
| Playback resolves internal object ID before reading `Entity.id` | DIRECT |
| `Entity.id` is a separate game-entity field | DIRECT |
| `MakeObjectAction.obj_id` exists | DIRECT |
| Internal model ID = game Entity.id | REJECTED |
| `MakeObjectAction.obj_id = Entity.id` | NOT PROVEN |
| `MakeObjectAction.obj_id = internal model ID` | NOT PROVEN |
| `World.entities` key = Entity.id | NOT PROVEN |
| Complete train → object-birth identity bridge | OPEN |

## Disposition

**PASS.** Pass 76 materially tightens identity semantics and prevents false joins. The unresolved bridge is now specifically assigned to `MakeObjectAction.obj_id` population/decoder semantics or empirical native-engine observation. No Layer-3 implementation or runtime modification occurred.
