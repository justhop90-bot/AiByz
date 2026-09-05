# PASS 79 — `uniqueId` CROSS-COMMAND NAMESPACE FORENSICS

**Layer:** 2 — HD archaeology / evidence only  
**Status:** Research only; no `.per`, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`

## Executive result

Pass 79 attacked the strongest remaining static-source target: the semantics of `Command.Make.uniqueId`.

A second independent CADE implementation of the same RPC schema was located in `ddk220-light/aoe2-unit-analyzer`. Its checked-in `cade_api.proto` reproduces the same command schema, including `Make.uniqueId`. More importantly, inspection of the protocol shows that the field name `uniqueId` is not confined to production: the same command-level concept occurs in **Make, Research, Build, and BuildWall** messages.

This materially changes the prior hypothesis space.

The strongest defensible interpretation is now:

> `uniqueId` is a **cross-command operation/request identity candidate**, not a field that can safely be presumed to mean the concrete world-object ID.

This is still a semantic hypothesis, not a proven engine specification. The schema establishes field presence and reuse across command types; it does not establish generation, lifetime, uniqueness scope, or correlation behavior.

## 1. Direct evidence: repeated `uniqueId` use across command families

The CADE protobuf defines:

```text
Make:
    unitId
    unitPlayerId
    objId
    uniqueId

Research:
    unitId
    unitPlayerId
    techId
    uniqueId
    extend
    buildingIds

Build:
    unitPlayerId
    location
    objId
    uniqueId
    frame
    extend
    instant
    ...

BuildWall:
    unitPlayerId
    location1
    location2
    objId
    uniqueId
    extend
    instant
    ...
```

The primary source is `librematch/delta-play-replay/crates/uncage-client/proto/cade_api.proto`; an independent AoE2 tool repository also carries the same schema at `scenario_builder/grpc/cade_api.proto`.

**Evidence grade:** DIRECT for field existence and cross-command reuse.

## 2. Why this weakens the `uniqueId = spawned object ID` hypothesis

If `uniqueId` were simply the identity of a newly created world object, its presence on `Research` is immediately problematic: research does not create a world entity in the same sense as Make/Build.

Likewise, `BuildWall` contains both an `objId` and a `uniqueId`, while its operation is a building construction request. The schema therefore separates at least two identifiers in operations that may have different lifecycle semantics.

This does **not** prove that `uniqueId` is a request ID. It does establish that the naive interpretation:

```text
uniqueId = concrete spawned Entity.id
```

is no longer a good default hypothesis.

## 3. Revised identity taxonomy

The current forensic taxonomy becomes:

| ID | Domain | Current interpretation | Grade |
|---|---|---|---|
| I1 | uncage document model | allocator slot / model-object identity | DIRECT |
| I2 | `World.entities` | world map key | DIRECT |
| I3 | `Ref` | reference into model namespace | DIRECT |
| I4 | `Entity.id` | game entity field | DIRECT |
| I5 | `MakeObjectAction.obj_id` | production action payload identifier | DIRECT |
| I6a | `Command.Make.objId` | Make command object field | DIRECT field; semantics open |
| I6b | `Command.Make.uniqueId` | cross-command operation identity candidate | DIRECT field; semantics open |

The most important unresolved joins remain:

```text
I6a → I5
I6a → I4
I6a → I2
I6b → I5
I6b → I4
I6b → I2
```

## 4. New hypothesis ranking

### H1 — `uniqueId` is an operation/request correlation identifier

**Status:** strongest current hypothesis, NOT PROVEN.

Reason: the same field name occurs across Make, Research, Build, and BuildWall, whose resulting world-state effects differ substantially.

### H2 — `uniqueId` is an engine-internal command transaction identifier

**Status:** plausible, NOT PROVEN.

This is compatible with cross-command reuse but requires engine-side evidence.

### H3 — `uniqueId` is the eventual world entity ID

**Status:** weakened substantially; NOT PROVEN.

Research's use of the field makes a universal object-ID interpretation difficult to defend.

### H4 — `uniqueId == objId`

**Status:** rejected as an assumption.

The schema deliberately exposes both fields separately.

### H5 — `uniqueId` is globally unique for the entire game

**Status:** UNKNOWN.

The name is insufficient evidence.

## 5. Important distinction: `objId` may itself be semantic, not lifecycle identity

The schema also contains `objId` on multiple construction-oriented commands:

```text
TransformObject.objId
Make.objId
Build.objId
BuildWall.objId
```

This creates a second cross-command pattern.

Therefore the more disciplined model is:

```text
COMMAND
├── operation-specific object/master/type field(s)
└── operation identity / correlation candidate
```

rather than:

```text
COMMAND
└── object ID
```

The exact semantics of `objId` remain unresolved too.

## 6. Cross-command matrix

| Command | `objId` | `uniqueId` | Immediate implication |
|---|---:|---:|---|
| Make | yes | yes | production has two ID fields |
| Research | no | yes | `uniqueId` cannot be assumed to mean spawned object ID |
| Build | yes | yes | construction has two ID fields |
| BuildWall | yes | yes | wall construction has two ID fields |
| TransformObject | yes | no | `objId` also exists outside Make |

This is one of the strongest static clues obtained in the identity investigation so far.

## 7. Consequence for object-birth correlation

The correct target is no longer:

```text
Make.uniqueId == Entity.id ?
```

as the first question.

The correct target sequence is:

```text
1. What generates uniqueId?
2. What consumes uniqueId?
3. What lifetime does uniqueId have?
4. Is uniqueId echoed into later command/state records?
5. What does objId identify?
6. Does either identifier survive into MakeObjectAction?
7. Does either identifier survive into Entity.id?
```

Only after those are answered should an object-birth join be attempted.

## 8. Highest-value empirical test

For a controlled production event, record:

```text
world time
player
producer/unitId
Make.unitId
Make.unitPlayerId
Make.objId
Make.uniqueId
MakeObjectAction.obj_id
MakeObjectAction.work_done
production queue record
new Entity.id
new Entity.owner_id
new Entity.type
new Entity position
```

Then repeat for:

1. multiple units produced by one building;
2. multiple buildings producing the same unit;
3. different players;
4. cancelled/interrupted production;
5. research;
6. building construction.

A repeated identifier that crosses operation boundaries is particularly valuable for determining whether it is request-level rather than object-level.

## 9. Hostile QC

Rejected:

- `uniqueId` means globally unique object ID because of its name.
- `uniqueId == Entity.id`.
- `uniqueId == MakeObjectAction.obj_id`.
- `uniqueId == objId`.
- repeated schema naming alone proves lifetime semantics.
- Research's `uniqueId` proves it is a transaction ID; it only makes that hypothesis stronger.
- `objId` is necessarily a unit type, master ID, or world object ID without producer-side evidence.

## 10. Evidence ledger

| Proposition | Grade |
|---|---|
| `Command.Make` has `uniqueId` | DIRECT |
| `Command.Research` has `uniqueId` | DIRECT |
| `Command.Build` has `uniqueId` | DIRECT |
| `Command.BuildWall` has `uniqueId` | DIRECT |
| `uniqueId` is reused across command families | DIRECT |
| `uniqueId` is an operation/request correlation ID | STRONG HYPOTHESIS |
| `uniqueId` is a world Entity ID | WEAKENED / NOT PROVEN |
| `uniqueId` is globally unique | NOT PROVEN |
| `Make.objId == MakeObjectAction.obj_id` | NOT PROVEN |
| `Make.objId == Entity.id` | NOT PROVEN |
| `uniqueId == Entity.id` | NOT PROVEN |

## 11. Disposition

**Layer 1:** unchanged at 89%; scenario automation remains retired.  
**Layer 2:** strengthened materially. The static-source search has now established a cross-command `uniqueId` namespace and weakened the most dangerous identity assumption.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

### Pass 79 conclusion

The production identity problem is now better framed as a **multi-identifier lifecycle problem**.

The evidence no longer supports treating `uniqueId` as a likely concrete spawned-object ID by default. Its presence across Make, Research, Build, and BuildWall makes a command/operation correlation role substantially more plausible.

The next high-value target is therefore not more schema archaeology. It is **identifier lifecycle observation**: determine where these fields are generated, whether they recur in subsequent state/action records, and whether their values persist across the operation boundary.
