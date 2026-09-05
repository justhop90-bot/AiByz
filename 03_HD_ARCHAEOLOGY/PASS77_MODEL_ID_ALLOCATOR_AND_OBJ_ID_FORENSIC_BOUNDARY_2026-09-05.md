# PASS 77 — MODEL-ID ALLOCATOR AND `obj_id` FORENSIC BOUNDARY

**Layer:** 2 — HD archaeology / evidence only  
**Date:** 2026-09-05  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Prior canonical commit:** `fb149b0adad0040e29cd1b89203ff6476e95f2f5` (Pass 76)  
**Status:** Research only. No `.per` implementation, runtime splice, deployment, or Layer-1 scenario work.

## Executive result

Pass 77 materially closes the semantics of the **replay-document model-object ID allocator** and makes the remaining production identity question narrower.

The `uncage-model` implementation proves that its internal model-object IDs are allocator slots, not game entity IDs. IDs are assigned when models are registered, can be recycled after removal, and are resolved through `Document::by_id()`. This makes numeric equality between a replay-model object ID and `Entity.id` even less defensible as an identity join.

The production-side field `MakeObjectAction.obj_id` remains a decoded `i16` payload field. The repository search performed in this pass found its declaration but no source-side semantic conversion that maps it to `Entity.id`, `World.entities` keys, or the document-model namespace. Therefore the central bridge remains **UNPROVEN**.

The next investigation should target the producer/decoder of model type 23 or an empirical state trace that simultaneously exposes `MakeObjectAction.obj_id`, the producing building, and the resulting `Entity.id`.

---

## 1. Direct evidence examined

### 1.1 `MakeObjectAction`

`crates/uncage/src/model.rs` declares model type 23:

```text
#[uncage(type = 23)]
pub struct MakeObjectAction {
    #[uncage(extends)]
    pub parent: Action,
    #[uncage(index = 7)]
    pub obj_id: i16,
    #[uncage(index = 8)]
    pub work_done: f32,
}
```

The parent `Action` model contains generic action fields including `type`, `state`, `target_id`, `target_2_id`, target coordinates, and timer.

**Evidence grade:** DIRECT.

Source: `crates/uncage/src/model.rs` at commit `9bc90f67f22aec47bb050cdea5b73a5fec0d629e`.

### 1.2 Internal model-object IDs are allocated by the document store

`crates/uncage-model/src/document.rs` defines:

```text
struct ModelHolder {
    id: usize,
    cell: ModelRc,
}
```

`ModelWithDocument::object()` returns this internal `usize` ID.

`Document::replace_ref()` registers the supplied model and assigns the returned store ID to the `Ref`:

```text
let id = self.get_mut().register(model);
if let Some(old_id) = _ref.set(id) {
    self.remove(old_id);
}
id
```

`InnerDocument::register()` calls `ItemStore::insert()` and stores the assigned index in `ModelHolder.id`.

**Evidence grade:** DIRECT.

### 1.3 The allocator recycles IDs

`ItemStore` maintains:

```text
items: Vec<Option<T>>
free: VecDeque<usize>
```

Insertion first consumes a previously freed index when available:

```text
if let Some(id) = self.free.pop_front() {
    self.items[id] = Some(item);
    return id;
}
```

Removal takes the item and pushes the index into `free`:

```text
self.items[index].take()
self.free.push_back(index)
```

Therefore an internal model-object ID is **not a globally unique lifetime identity**. It is an address/slot within the document's model store and may be reused after removal.

**Evidence grade:** DIRECT.

### 1.4 `Document::by_id()` resolves the internal namespace

`Document::by_id(id: usize)` looks up the supplied ID in the document's model store and returns a `ModelBorrow` whose `id` is that same internal model ID.

This establishes:

```text
Ref
 ↓
internal document model ID (I1)
 ↓
Document::by_id()
 ↓
model object
```

It does **not** establish:

```text
I1 == Entity.id
```

**Evidence grade:** DIRECT.

### 1.5 Patcher selector matches use the internal model ID

`crates/uncage-model/src/patcher.rs` defines:

```text
pub struct PatcherSelectorMatch {
    pub object_id: usize,
    pub path: Path,
    pub selector_key: usize,
}
```

On a matched mutation, the patcher emits:

```text
object_id: top.object()
```

Since `top.object()` is the `ModelWithDocument::object()` ID, selector `object_id` is the document-model namespace, not the embedded `Entity.id` field.

**Evidence grade:** DIRECT.

---

## 2. New identity taxonomy

The evidence now supports five separate identity domains:

| ID | Domain | Type | Meaning | Status |
|---|---|---:|---|---|
| I1 | `uncage-model` document | `usize` | allocator slot / model-object ID | DIRECT |
| I2 | `World.entities` | `i32` | map key for entity references | DIRECT |
| I3 | `Ref` | internal reference | points into I1 | DIRECT |
| I4 | `Entity.id` | `i32` | game entity field | DIRECT |
| I5 | `MakeObjectAction.obj_id` | `i16` | action payload field at model index 7 | DIRECT |

Proven structural relations:

```text
I3 → I1
I1 → model object
model object → I4 when that object is an Entity model
```

The following remain unproven:

```text
I2 = I4
I5 = I4
I5 = I1
I5 = I2
```

The allocator evidence strengthens the negative conclusion: even if an `I1` value numerically equals an `I4` value at one instant, that equality is not sufficient to establish semantic identity because I1 values can be recycled.

---

## 3. Production identity chain after Pass 77

The strongest defensible chain is now:

```text
TRAIN / PRODUCTION INTENT
        ↓
PRODUCTION BUILDING
        ↓
production queue / current production action
        ↓
MakeObjectAction model (type 23)
        ↓
obj_id : i16       ← unresolved semantic bridge
        ↓
???
        ↓
World entity model
        ↓
Entity.id : i32
```

A separate replay-document reference chain exists:

```text
Ref
 ↓
I1 document model ID
 ↓
Document::by_id()
 ↓
Entity model
 ↓
I4 Entity.id
```

There is currently no source evidence connecting the `obj_id` field to that reference chain.

---

## 4. Important negative result

Pass 77 rules out an especially tempting but invalid shortcut:

```text
MakeObjectAction.obj_id
        ==
PatcherSelectorMatch.object_id
        ==
Entity.id
```

There is no evidence for this three-way identity.

More strongly, `PatcherSelectorMatch.object_id` is demonstrably an I1 document-model ID, while `MakeObjectAction.obj_id` is an I5 `i16` field. Their equal numeric values would still not prove semantic equivalence.

Likewise, because I1 allocator slots can be reused, an I1 number should not be persisted as a lifetime object identifier without an independent generation/lifetime proof.

---

## 5. What this means for object-birth proof

A production object-birth proof still requires something equivalent to:

```text
T0: producer B has production action A
T1: A is MakeObjectAction
T2: A.obj_id = X
T3: the same semantic object is introduced into world state
T4: resulting Entity.id = Y
T5: X ↔ Y is proven by a semantic reference, decoder rule, or synchronized empirical trace
T6: ownership/type/time/position are consistent
```

Without T5, an observed queue event plus an aggregate unit-count increase remains correlation rather than exact object lineage.

---

## 6. Highest-value next targets

### Target A — model-type-23 producer/decoder

Find the code that constructs or populates `MakeObjectAction` instances from native/replay data. Specifically search for:

- model type `23` construction;
- field index `7` assignment;
- `obj_id` serialization/deserialization;
- action decoding from native state;
- generated model documentation that describes type 23 field 7;
- any conversion layer between CADE/native structures and `uncage` models.

### Target B — simultaneous empirical trace

If source semantics remain unavailable, obtain one state trace where all of the following are observed for the same production event:

```text
producer building identity
MakeObjectAction.obj_id
production unit/type identity
world entity creation
Entity.id
creation timestamp
initial position
```

A repeated trace across multiple object births would be much stronger than one numeric coincidence.

### Target C — lifetime/reuse test

Because I1 IDs are explicitly recycled, any future empirical join must test whether the candidate identifier survives model removal/recreation. If it does not, it cannot serve as a lifetime game-object identity.

---

## 7. Hostile QC

The following claims remain rejected:

1. `obj_id` is `Entity.id` because both contain the word “id”.
2. `obj_id` is the patcher selector's `object_id` because both identify models in some context.
3. Numeric equality between any two namespaces proves identity.
4. An I1 document-model ID is a globally unique object identifier.
5. A queue `unit_id` is a concrete world object ID.
6. `work_done` reaching an assumed threshold proves object creation.
7. A model-type-23 presence proves a train command completed.
8. A unit-count increase proves which train command created which unit.
9. A replay selector match proves a specific production command caused the matched object to exist.
10. CADE availability alone constitutes an authoritative object-birth oracle.

---

## 8. Evidence ledger

| Proposition | Grade | Reason |
|---|---|---|
| `MakeObjectAction` is model type 23 | DIRECT | source declaration |
| `obj_id` is field index 7 and `i16` | DIRECT | source declaration |
| `work_done` is field index 8 and `f32` | DIRECT | source declaration |
| `ModelWithDocument::object()` returns internal `usize` | DIRECT | source implementation |
| `Document::by_id()` resolves that internal ID | DIRECT | source implementation |
| model IDs are allocated by `ItemStore::insert()` | DIRECT | source implementation |
| freed model IDs are recycled | DIRECT | source implementation |
| patcher selector `object_id` is internal model ID | DIRECT | `top.object()` call |
| `obj_id` maps to selector `object_id` | NOT PROVEN | no semantic bridge found |
| `obj_id` maps to `Entity.id` | NOT PROVEN | no semantic bridge found |
| `obj_id` maps to `World.entities` key | NOT PROVEN | no semantic bridge found |
| train command → exact object birth | NOT PROVEN | bridge still open |
| aggregate production count → exact object identity | NOT PROVEN | correlation only |

---

## 9. Layer and implementation disposition

**Layer 1:** unchanged at 89%; scenario-loader automation remains retired.  
**Layer 2:** strengthened; the identity namespace model is more complete.  
**Layer 3:** unchanged at 0%; no implementation was performed.  
**Deployment:** 0%; no runtime modification occurred.

**Pass 77 conclusion:** the replay-document allocator semantics are now directly established, and they make namespace conflation even less defensible. The remaining `MakeObjectAction.obj_id → concrete world Entity.id` bridge is the critical unresolved production-lineage edge.
