# Pass 75 — Model-Reference / Entity-Identity Bridge

**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Research completeness:** 99% (unchanged; this pass materially strengthens an unresolved proof edge but does not close runtime/object-birth execution)

## Mission

Continue the Pass-74 object-birth investigation by attacking the most important unresolved ambiguity: whether the state-delta system's internal model-reference IDs are the same thing as the game's concrete `Entity.id`, and whether the production/action path can be followed through the model graph without conflating those identity domains.

## Executive finding

Pass 75 produces a significant refinement and partial closure of the identity model.

The `uncage-model` implementation explicitly defines `Ref` as an internal document/model reference containing a `usize`, while `ModelWithDocument::object()` and `Document::by_id()` operate on that same internal model-object ID namespace. The playback example then demonstrates the critical distinction in live code: a selector match returns an internal `object_id`; that object is resolved through `Document::by_id(...)` and cast to `Entity`; the actual game's `Entity.id` is then read separately and used as the stable entity key for HP tracking.

Therefore:

```text
PATCH / SELECTOR OBJECT ID
        ≠ automatically GAME ENTITY ID

internal model-object ID
        ↓ Document::by_id()
Entity model
        ↓ ent.id
concrete game-entity ID
```

This is stronger than the Pass-74 statement that the relationship was merely unknown. We now have direct implementation evidence that the replay tooling intentionally keeps an internal model-object reference separate from `Entity.id`.

However, the central production bridge remains open:

```text
MakeObjectAction.obj_id
        ?
Entity.id
```

The source inspected still does not contain an explicit assignment, comparison, or lookup proving that equality. The correct next target is therefore not generic state archaeology; it is a targeted search for the producer/action decoder or source-side population logic that establishes the semantic meaning of `MakeObjectAction.obj_id`.

## 1. Internal reference IDs are a separate namespace

`crates/uncage-model/src/references.rs` defines:

```text
Ref(Option<usize>)
ModelRef<T> { inner: Ref, ... }
```

and `Reference::from_id`, `Reference::get`, `set`, and `reset` operate on this internal `usize` reference. `ModelRef<T>` adds a model-type constraint but still stores the same `Ref` identity. fileciteturn652file0

`crates/uncage-model/src/document.rs` exposes `Document::by_id(id: usize)` and `ModelWithDocument::object() -> usize`, establishing that the replay document has its own model-object identity space. The document resolves references by these IDs. fileciteturn653file0

This means a future forensic extractor must never silently label an internal `object_id` as an AoE2 game `Entity.id`.

## 2. The playback example proves the distinction operationally

The repository's playback example installs a selector for created entries in `WorldFields::Entities` and receives a `PatcherSelectorMatch` containing `object_id`. It then calls:

```text
patcher.document().by_id(_match.object_id)
```

and casts the resolved model to `Entity`. Only after resolving the model does the example read `ent.id`. It then uses `ent.id` as the key for persistent HP tracking. fileciteturn656file0

This is direct operational evidence for the following chain:

```text
World.entities creation
        ↓
Patcher selector match
        ↓
internal model object_id
        ↓
Document::by_id(object_id)
        ↓
Entity model
        ↓
Entity.id
```

The example is not merely defining fields; it demonstrates how the library expects callers to move between the internal document identity and the game's entity identity.

## 3. World.entities is a keyed map, but its values are references

The `World` model declares:

```text
entities: BTreeMap<i32, Ref>
```

while `Entity` separately declares:

```text
id: i32
master_id: i16
owner_id: i8
...
```

The key/value relationship therefore cannot be assumed to mean `World.entities[key] == Entity.id` without inspecting how the state producer populates the map. The value is explicitly a `Ref`, i.e. a model reference. fileciteturn645file0 fileciteturn652file0

This yields three distinct identifiers that must remain separate in AEGIS evidence:

```text
A = World.entities map key
B = internal model-object ID / Ref target
C = Entity.id (game entity identity)
```

The playback code directly demonstrates B → Entity model → C. It does not by itself prove A == C.

## 4. Selector-created semantics provide a real creation observation point

`Patcher::apply_patch` handles `PushCreateAndAssignKey` by creating a model, inserting it into a map/list field, pushing the newly created model's internal ID onto the stack, and marking the path as `Created`. Selector matches are emitted with the current top model's internal `object_id`. fileciteturn658file0

This is important because it gives the forensic pipeline a genuine state-model creation event:

```text
state patch
↓
new model allocated
↓
internal model ID assigned
↓
path marked Created
↓
selector match emitted
↓
model resolved
↓
Entity.id read
```

Thus the state-delta framework can identify the creation of an `Entity` model without pretending that its internal model ID is the same as the game's `Entity.id`.

## 5. Production action remains a separate identity problem

`MakeObjectAction` is model type 23 and extends the generic `Action` model. It contains:

```text
obj_id: i16
work_done: f32
```

The parent `Action` contains generic action state including `type`, `state`, targets, target coordinates, and `timer`. fileciteturn661file0

The important negative result remains:

```text
MakeObjectAction.obj_id
        ≠ proven Entity.id
```

The field's name strongly suggests object identity, but field naming is not sufficient evidence. No inspected source code performs an explicit `obj_id == Entity.id` assertion, lookup, or assignment.

## 6. New provenance model

The strongest current identity graph is now:

```text
                 INTERNAL REPLAY MODEL SPACE

World.entities map
      │
      │ Ref
      ▼
model-object ID B
      │
      │ Document::by_id(B)
      ▼
Entity model
      │
      ├── Entity.id = C
      ├── master_id
      ├── owner_id
      ├── position
      └── state / hp

Production side:

Building.current_production_queue_action
      │
      │ Ref
      ▼
model-object ID D
      │
      │ Document::by_id(D)
      ▼
MakeObjectAction
      │
      ├── obj_id = X
      └── work_done
```

The missing edge is therefore precisely:

```text
X = MakeObjectAction.obj_id
        ↓ ?
C = Entity.id
```

and not the broader, less precise question “does the replay contain entity IDs?” It does.

## 7. Stronger object-birth proof standard

The proof standard should now require an explicit four-identity trace where applicable:

```text
T0 COMMAND
player P
producer/game entity C_B
unit/type U

T1 PRODUCTION MODEL
building model-object B_M
current_production_queue_action → action model D_M
queue record unit_id = U

T2 ACTION MODEL
D_M resolves to MakeObjectAction
obj_id = X
work_done = W

T3 CREATION MODEL
World.entities creation selector emits internal model-object E_M
E_M resolves to Entity
Entity.id = Y
owner/type/master/position recorded

T4 IDENTITY BRIDGE
X ↔ Y proven by direct source semantics or empirical state trace
```

This is substantially more rigorous than comparing aggregate counts or timestamps.

## 8. Hostile QC

The following claims remain rejected:

- `PatcherSelectorMatch.object_id` is the AoE2 game entity ID — **REJECTED**.
- `World.entities` map key is automatically `Entity.id` — **NOT PROVEN**.
- `MakeObjectAction.obj_id` is automatically `Entity.id` — **NOT PROVEN**.
- `ProductionQueueRecord.unit_id` identifies a concrete spawned object — **REJECTED**; it is a queue/type field.
- `work_done` reaching an assumed numeric threshold proves object creation — **NOT PROVEN**.
- A created `Entity` model proves a specific preceding train command caused it — **NOT PROVEN**.
- The existence of all model fields means AEGIS can currently extract a complete production lineage from `.aoe2record` — **REJECTED**.

## 9. Highest-value next research target

The search target is now sharply narrowed:

```text
Find source code that populates MakeObjectAction.obj_id
OR
find source code that creates/updates Entity.id in relation to MakeObjectAction
OR
find an empirical state-delta trace where both fields can be observed for the same production event.
```

Priority order:

1. Producer/action decoding or model-population code.
2. Entity creation/population code.
3. Existing example code that inspects MakeObjectAction and Entity together.
4. Only then, local replay execution once the workstation connection is restored.

The workstation remains unavailable for actual replay execution until an authorized filesystem/process call succeeds; the online/ping state must not be mistaken for executable connectivity.

## 10. Evidence ledger

| Proposition | Grade |
|---|---|
| `Ref` stores an internal `usize` model reference | DIRECT |
| `Document::by_id` resolves internal model-object IDs | DIRECT |
| `ModelWithDocument::object()` exposes internal model-object ID | DIRECT |
| `World.entities` stores `Ref` values | DIRECT |
| `Entity` has a separate `id` field | DIRECT |
| Playback resolves selector `object_id` through `Document::by_id` before reading `Entity.id` | DIRECT |
| Created selector path can expose a newly created model-object ID | DIRECT |
| `MakeObjectAction` has `obj_id` and `work_done` | DIRECT |
| Selector/model object ID equals `Entity.id` | REJECTED |
| `World.entities` key equals `Entity.id` | NOT PROVEN |
| `MakeObjectAction.obj_id` equals `Entity.id` | NOT PROVEN |
| Complete train-command → object-birth lineage is currently extractable | NOT PROVEN |
| The identity problem has been narrowed to a specific X→Y bridge | STRONGLY SUPPORTED |

## Disposition

**PASS.** This pass materially improves the forensic model and eliminates one major source of identifier conflation. It does not close object-birth lineage because the production-action `obj_id` → game `Entity.id` semantic bridge remains unproven.

Layer 2 remains research-only. No `.per` implementation, runtime splicing, architecture construction, or deployment occurred.
