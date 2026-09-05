# PASS 78 — PRODUCTION COMMAND `objId` / `uniqueId` FORENSIC BRIDGE

**Layer:** 2 — HD archaeology / evidence only  
**Status:** Research only; no `.per`, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`

## Executive result

Pass 78 found a substantially more relevant production-side identity clue in the CADE RPC schema: the explicit `Command.Make` message contains **both `objId` and `uniqueId`**, alongside `unitId` and `unitPlayerId`.

```text
message Make {
    int32 unitId = 1;
    uint32 unitPlayerId = 2;
    int32 objId = 3;
    int32 uniqueId = 4;
}
```

This is important because the previously isolated replay-state `MakeObjectAction.obj_id` is now demonstrably adjacent to an explicit production-command `objId` concept in the same ecosystem.

However, this does **not** yet close the identity bridge. The repository provides no direct source evidence in the inspected code that establishes:

```text
Command.Make.objId
        =
MakeObjectAction.obj_id
        =
Entity.id
```

Nor does it establish what `uniqueId` means, whether it is globally unique, command-local, a queue token, a production-request identifier, or another engine-side identifier.

The result is therefore a **new high-value candidate bridge, not a closed bridge**.

---

## 1. Direct evidence: CADE production command schema

The public `crates/uncage-client/proto/cade_api.proto` defines a `Command` oneof containing a `Make` command.

The `Make` payload has four fields:

```text
unitId = 1
unitPlayerId = 2
objId = 3
uniqueId = 4
```

This is direct protocol evidence that the CADE command interface represents production/make requests with both an object identifier and a separate unique identifier.

**Evidence grade:** DIRECT.

Source: `crates/uncage-client/proto/cade_api.proto`, commit `9bc90f67f22aec47bb050cdea5b73a5fec0d629e`.

---

## 2. Why this changes the investigation

Previously the production side was:

```text
TRAIN / production command
        ↓
MakeObjectAction.obj_id
        ↓
???
        ↓
Entity.id
```

Pass 78 adds a concrete command-level identity namespace:

```text
CADE Command.Make
├── unitId
├── unitPlayerId
├── objId          ← candidate production object/type identity
└── uniqueId       ← candidate request/lifecycle identity
```

The important observation is not that these fields are equal to replay fields. It is that the production API itself distinguishes **object identity information** from **unique/request identity information**.

That makes it plausible that an eventual forensic chain could contain more than one identifier:

```text
production request identity
        ↓
command objId / uniqueId
        ↓
engine production action
        ↓
MakeObjectAction.obj_id
        ↓
world entity identity
```

But the arrows remain hypotheses until directly connected.

---

## 3. Critical namespace separation

The current evidence supports at least six candidate identity domains:

| ID | Domain | Type | Current interpretation | Grade |
|---|---|---:|---|---|
| I1 | uncage document model | `usize` | allocator slot / model-object identity | DIRECT |
| I2 | `World.entities` | `i32` | world map key | DIRECT |
| I3 | `Ref` | internal | points into I1 | DIRECT |
| I4 | `Entity.id` | `i32` | game entity field | DIRECT |
| I5 | `MakeObjectAction.obj_id` | `i16` | production action payload field | DIRECT |
| I6a | `Command.Make.objId` | `i32` | CADE production-command object field | DIRECT |
| I6b | `Command.Make.uniqueId` | `i32` | CADE production-command unique field; semantics unresolved | DIRECT field / UNKNOWN semantics |

The crucial unproven joins are now:

```text
I6a = I5
I6a = I4
I6a = I2
I6b = I6a
I6b = I5
I6b = I4
```

No numeric equality should be promoted to semantic identity.

---

## 4. `uniqueId` is especially important

The existence of both:

```text
objId
uniqueId
```

in the same `Make` command means they should **not** be casually collapsed into one identity concept.

The name `uniqueId` strongly suggests a distinct purpose, but the semantics cannot be inferred from naming alone.

Required evidence before assigning meaning:

1. producer-side construction of `Make` commands;
2. all writes to `objId` and `uniqueId`;
3. all reads of those fields;
4. whether `uniqueId` increments, recycles, or derives from another counter;
5. whether the same value appears in replay/model state;
6. whether either field survives into world-state entity identity.

Until then:

```text
uniqueId = UNKNOWN SEMANTICS
```

not:

```text
uniqueId = object ID
```

---

## 5. Search result: no direct consumer bridge found

Repository search for `obj_id` returned the model declaration and another unrelated `inside_obj_id` field, but did not expose a separate producer/consumer implementation connecting `MakeObjectAction.obj_id` to `Command.Make.objId` or `Entity.id`.

Search for `uniqueId` likewise exposed the protocol definition but did not produce a semantic implementation in the inspected repository.

Therefore the present result is a **protocol-level clue**, not source-level identity closure.

---

## 6. New forensic chain

The best current representation is:

```text
                    CADE RPC
                       │
                Command.Make
                 /          \
             objId        uniqueId
                │              │
                ?              ?
                │              │
        engine production action
                │
        MakeObjectAction
                │
             obj_id
                │
                ?
                │
          World Entity
                │
            Entity.id
```

The only closed edges in this diagram are the structural presence of the respective fields/models. The semantic arrows marked `?` remain unresolved.

---

## 7. Revised highest-value targets

### Target A — CADE command construction

Locate the code that constructs the protobuf `Make` message. Determine exactly where `objId` and `uniqueId` originate.

Questions:

- Is `objId` copied from a selected unit/master/unit type?
- Is `uniqueId` generated client-side?
- Is either field returned by the engine?
- Is either field echoed into replay/state?

### Target B — model type 23 population

Continue tracing model type 23 / field 7 from native state into `MakeObjectAction.obj_id`.

The decisive result would be a direct assignment/conversion such as:

```text
make.objId → action.obj_id
```

or:

```text
engine.production_id → action.obj_id
```

### Target C — simultaneous command/state capture

If source tracing remains unavailable, capture a production event in which:

```text
Command.Make.objId
Command.Make.uniqueId
MakeObjectAction.obj_id
producer building
Entity.id
```

are all visible in the same temporal window.

### Target D — `uniqueId` lifecycle experiment

Across many production commands, test whether `uniqueId`:

- increments monotonically;
- repeats across players;
- repeats across buildings;
- survives cancellation;
- survives completion;
- appears in later state;
- maps one-to-one to an object.

This can distinguish request identity from object identity.

---

## 8. Hostile QC

Rejected claims:

1. `Command.Make.objId == MakeObjectAction.obj_id` merely because both are named `objId`.
2. `Command.Make.objId == Entity.id` because all three concern production.
3. `uniqueId` is a globally unique production ID because of its name.
4. `uniqueId == Entity.id`.
5. `uniqueId == objId`.
6. CADE protobuf field order proves semantic identity.
7. A production command's presence proves completion.
8. `MakeObjectAction` presence proves object birth.
9. Numeric coincidence across command/state/world namespaces closes lineage.
10. CADE's command schema alone proves what the engine does with these identifiers.

---

## 9. Evidence ledger

| Proposition | Grade |
|---|---|
| CADE exposes a `Command.Make` command | DIRECT |
| `Make` has `unitId` | DIRECT |
| `Make` has `unitPlayerId` | DIRECT |
| `Make` has `objId` | DIRECT |
| `Make` has `uniqueId` | DIRECT |
| `MakeObjectAction` has `obj_id` | DIRECT |
| `MakeObjectAction.obj_id` is field 7 / `i16` | DIRECT |
| `Command.Make.objId` semantically equals `MakeObjectAction.obj_id` | NOT PROVEN |
| `Command.Make.objId` semantically equals `Entity.id` | NOT PROVEN |
| `Command.Make.uniqueId` semantics | UNKNOWN |
| `uniqueId` is globally unique | NOT PROVEN |
| production command → exact object birth | NOT PROVEN |

---

## 10. Disposition

**Layer 1:** unchanged at 89%.  
**Layer 2:** strengthened; production-command identity now has an additional concrete protocol namespace.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

### Pass 78 conclusion

The investigation has uncovered the first explicit **production-command identity pair** that can potentially connect command lineage to replay action lineage: `Make.objId` and `Make.uniqueId`.

This is a meaningful advance because it gives the next pass a concrete upstream target rather than searching only for the downstream `MakeObjectAction.obj_id` field.

The bridge is still open. The next pass should attack the construction/consumption of `Command.Make`, with special attention to `uniqueId`. If that identifier is shown to survive from production command into state/action records, it may become the missing lifecycle correlation key. If it does not, we will have strong evidence that command identity and world-object identity are separate namespaces.
