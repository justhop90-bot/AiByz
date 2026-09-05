# Pass 74 — State-Delta Production Lineage Schema

**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Status:** PASS — object-lineage schema materially strengthened; executable replay correlation remains unperformed

## Mission

Attack the exact Pass-73 question: whether the documented engine/state-delta model contains enough identity and production fields to support an individual production-command → object-birth correlation.

## Executive finding

Pass 74 found the strongest evidence yet for the missing bridge.

The public `librematch/delta-play-replay` source model does not merely describe a generic entity table. Its `World` model contains an `entities` map keyed by integer identifiers. Its `Entity` model contains an explicit `id`, `master_id`, `owner_id`, world coordinates, and object `type`. Its `BuildingEntity` model contains both a `current_production_queue_action` reference and a `production_queue` collection. Its `ProductionQueueRecord` contains `unit_id`, `tech_id`, and `unit_count`. Its action model includes a dedicated `MakeObjectAction` with an `obj_id` field and `work_done`.

This changes the forensic assessment materially.

We now have direct source evidence for the following simultaneous concepts:

```text
WORLD
├── ENTITIES[id]
│   ├── entity.id
│   ├── owner_id
│   ├── master_id / type
│   └── world position
│
└── BUILDING
    ├── current production action
    └── production queue
         ├── unit_id
         ├── tech_id
         └── unit_count

MAKE-OBJECT ACTION
└── obj_id
    └── work_done
```

This is substantially closer to a deterministic production/object lineage ledger than the generic “state deltas exist” finding of Pass 73.

It still does **not** prove that the repository's current implementation can be pointed at one of our `.aoe2record` files and produce the complete chain automatically.

## 1. Direct source evidence

The source file `crates/uncage/src/model.rs` defines a `World` object with an `entities: BTreeMap<i32, Ref>` collection. The same source defines `Entity` with fields including `id`, `master_id`, `owner_id`, `world_x`, `world_y`, `world_z`, and `type`. fileciteturn585file0 fileciteturn589file0

This is direct evidence that the model can distinguish a specific world entity from its master/type metadata and owner.

## 2. Production queue is a first-class modeled object

The same source defines `BuildingEntity` with:

```text
current_production_queue_action: Ref
production_queue: ModelVec<ProductionQueueRecord>
```

and defines `ProductionQueueRecord` with:

```text
unit_id
tech_id
unit_count
```

This is stronger than merely having aggregate “units in production.” The state model explicitly preserves producer-side queue information. fileciteturn592file0

## 3. Object-production action contains an object ID

The source defines `MakeObjectAction` as an action subtype and gives it:

```text
obj_id: i16
work_done: f32
```

This is the most important new forensic finding of the pass. The state model therefore has an action representation whose semantic payload includes the object/master object identifier being made, rather than only a generic “production happened” flag. fileciteturn592file0

The existence of this field is **not yet equivalent to a proven one-to-one mapping to the final world entity ID**. The relationship between `MakeObjectAction.obj_id` and `Entity.id` must be established before using them as interchangeable identifiers.

That distinction is mandatory.

## 4. New identity layers

Pass 74 requires at least three identity domains to remain separate:

```text
QUEUE UNIT ID
    = unit/type identity used by production queue

MAKE-OBJECT obj_id
    = object/master-object identity carried by production action

WORLD ENTITY id
    = concrete world-entity identity
```

A future extractor must determine whether these are:

```text
identical
or
related by a deterministic lookup
or
independent identifiers
```

The current source proves their existence, not their equality.

## 5. Producer-side linkage

A production building carries:

```text
current_production_queue_action
production_queue
```

while a concrete world entity carries:

```text
owner_id
master_id
world position
state
hp
```

This suggests a possible producer-to-object chain:

```text
BUILDING ENTITY B
↓
CURRENT PRODUCTION ACTION A
↓
MAKE-OBJECT A.obj_id
↓
WORLD ENTITY E
```

But the repository source inspected here does not yet prove the exact reference semantics connecting `current_production_queue_action` to a particular `MakeObjectAction` and then to `Entity.id`.

Therefore this remains a **high-confidence research hypothesis**, not closed lineage.

## 6. Production queue gives an additional discriminator

A queue record contains `unit_id` and `unit_count`. Therefore a candidate object creation can potentially be constrained by:

```text
producer building
+
queued unit type
+
queue count transition
+
current production action
+
object creation
```

This is materially stronger than matching only on unit type and time.

For a Byzantine Camel case, the desired evidence becomes:

```text
Byzantine Stable B
↓
queue record unit_id = CAMEL
↓
current production action A
↓
A = MakeObjectAction
↓
A.obj_id = X
↓
world entity E
↓
E.id = Y
E.owner_id = Byzantine
E.master_id/type = Camel
```

The final X→Y mapping remains the key unresolved identity question.

## 7. Work-progress signal

`MakeObjectAction.work_done` provides a second potential lifecycle discriminator.

If the state stream records changes to this field over time, a production action may expose a progression such as:

```text
work_done = 0
↓
work_done increases
↓
work_done reaches completion condition
↓
object becomes world entity
```

This is a promising research route, but the source declaration alone does not establish the exact numeric completion semantics or event ordering. Those must be measured from actual state-delta data.

## 8. Revised object-birth proof standard

The minimum acceptable proof should now be upgraded to:

```text
T0
TRAIN COMMAND
player = P
producer = B
unit_id = U

T1
BUILDING STATE
B.current_production_queue_action = A
B.production_queue contains U

T2
ACTION STATE
A is MakeObjectAction
A.obj_id = X
work_done = ...

T3
WORLD STATE
Entity.id = Y
Entity.owner_id = P
Entity.master_id/type = U
Entity.position = (x,y,z)

T4
IDENTITY BRIDGE
X ↔ Y proven
```

Only T4 closes exact command-to-object identity.

## 9. What remains unproven

Even with the newly discovered schema, the following remain open:

```text
TRAIN COMMAND → queue entry
queue entry → MakeObjectAction
MakeObjectAction.obj_id → World Entity.id
completion threshold → creation event
creation event → first deployed state
```

This is a much smaller and more concrete uncertainty set than before Pass 74.

## 10. Local execution attempt status

The authorized workstation was checked as an available research target, but the Remote Desktop Commander session reported the machine as **not connected** when the AEGIS-AI-LAB directory was requested.

Therefore no local replay-engine invocation was falsely claimed.

This is an infrastructure-access limitation, not evidence that the state-delta route fails.

The next local test must be performed only when the workstation connection is available.

## 11. Hostile QC

### Claim: `MakeObjectAction.obj_id` proves final world entity ID.

**REJECTED.** The field is direct evidence of an object identifier inside the action model. Equality with `Entity.id` is not established.

### Claim: `ProductionQueueRecord.unit_id` identifies a concrete unit object.

**REJECTED.** It is explicitly a queue record's unit identity; it should not be conflated with a world-object identifier.

### Claim: `Entity.id` alone proves the entity was created by a particular train command.

**REJECTED.** Producer/action/queue linkage remains necessary.

### Claim: a production action containing `obj_id` proves successful completion.

**REJECTED.** Action state and work progress still require lifecycle interpretation.

### Claim: existence of this schema means AEGIS can already extract object lineage.

**REJECTED.** Schema capability is not executable integration.

### Claim: failure to access the workstation means the engine path is unavailable.

**REJECTED.** The local experiment was blocked by connectivity, not by an observed engine/API failure.

## 12. Evidence ledger

| Proposition | Grade |
|---|---|
| Delta-play-replay models world entities by integer-keyed identity | DIRECT |
| Entity model contains explicit ID, owner, type/master and coordinates | DIRECT |
| Building model contains current production action reference | DIRECT |
| Building model contains production queue | DIRECT |
| Production queue records contain unit ID and count | DIRECT |
| MakeObjectAction contains object ID and work progress | DIRECT |
| Queue unit ID = world entity ID | NOT PROVEN |
| MakeObjectAction.obj_id = world Entity.id | NOT PROVEN |
| Current production action resolves deterministically to a completed world entity | NOT PROVEN |
| Exact train command → object birth | NOT PROVEN |
| State stream can expose enough information to test the identity bridge | STRONGLY SUPPORTED |
| AEGIS can currently execute the state-delta replay path locally | NOT TESTED — workstation unavailable |

## 13. Updated confidence map

```text
RAW COMMAND
    │
    ├── player / producer / unit / time
    │
    ▼
PRODUCTION QUEUE
    │
    ├── unit_id / count
    │
    ▼
CURRENT PRODUCTION ACTION
    │
    ├── MakeObjectAction
    ├── obj_id
    └── work_done
    │
    ▼
WORLD ENTITY
    │
    ├── id
    ├── owner_id
    ├── master_id/type
    └── world position
```

Every downward edge except the final identity bridge now has direct schema support or an explicit parser-side representation. The edges' runtime semantics still require empirical validation.

## 14. Layer-2 disposition

Pass 74 is a **material breakthrough in schema archaeology**, not an object-birth closure.

The research frontier has moved from:

```text
“Does a richer state path even exist?”
```

to:

```text
“Can we execute it and prove the identity bridge?”
```

That is exactly the kind of narrowing we want from Layer 2.

No `.per` implementation, architecture construction, runtime promotion, or deployment was performed.
