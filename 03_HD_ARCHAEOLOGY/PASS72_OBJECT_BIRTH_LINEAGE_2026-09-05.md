# Pass 72 — Object-Birth Lineage Archaeology

**Layer:** Layer 2 — research / archaeology only  
**Implementation:** 0%  
**Architecture:** 0%  
**Deployment:** 0%  
**Status:** PASS WITH BOUNDARY — command/queue evidence is strong; individual train-command → spawned-object identity remains unclosed  
**Predecessors:** Passes 65–71

## Mission

Determine whether the available replay, parser, historical-source, and engine-reference evidence can connect an individual production command to the specific game object that is subsequently created, without confusing a queue request, pending object, or aggregate count with object birth.

## Executive finding

The production boundary is now sharply defined:

```text
STRATEGIC DEMAND
↓
AUTHORIZATION
↓
TRAIN COMMAND
↓
QUEUE / PENDING
↓
OBJECT BIRTH
↓
DEPLOYMENT
```

The historical Promisory source closes the first part of this chain for the Byzantine camel response. Replay parsing corroborates concrete production commands. Public replay documentation confirms that recorded-game bodies are command streams whose moves are applied to mutate game state, while full game-state quantities at arbitrary times generally require replaying the match through the game engine. citeturn0search0turn0search2

The available project evidence does **not** currently provide a universally reliable mapping of:

```text
TRAIN COMMAND #N
→ QUEUE SLOT #N
→ OBJECT ID #N
→ CREATION EVENT
```

Therefore L8 object birth remains open.

## 1. Why this boundary matters

A replay action such as:

```text
TRAIN camel-line
```

is an instruction/request in the recorded command stream. It is not itself proof that a Camel object entered the world.

Likewise:

```text
pending camel count > 0
```

proves pending production state, not object creation.

And:

```text
camel count increased
```

would still require careful temporal and ownership matching before assigning that increase to a particular train command.

The mandatory distinction is:

```text
COMMAND
≠
QUEUE ADMISSION
≠
PENDING OBJECT
≠
OBJECT BIRTH
≠
DEPLOYED UNIT
```

## 2. What replay files actually provide

Public parser documentation describes the `.aoe2record` body as a sequence of timestamped player actions/moves. The header is an initial-state snapshot; the body records subsequent moves. citeturn0search2turn0search4

This gives excellent evidence for **intent/action chronology** but does not automatically expose every intermediate engine state transition.

That explains a key forensic result from the AEGIS interpreter work:

```text
ACTION STREAM
→ highly observable

ENGINE WORLD STATE
→ only partially reconstructable without replaying the engine
```

This is not a parser defect. It is a property of the evidence source.

## 3. Pending-object evidence is real but has a different meaning

The technical scripting reference documents `up-pending-objects` and related total-count commands. It also records a historical UserPatch change making total object counts include units that are training or queued. citeturn0search5turn0search6

This is important because it proves the engine itself distinguishes pending production from completed object population.

Therefore:

```text
EXISTING COUNT
≠
EXISTING + PENDING COUNT
```

and:

```text
PENDING
≠
BORN
```

This validates the Layer-2 realization boundary rather than closing it.

## 4. Strongest available lifecycle model

The most defensible lifecycle is:

```text
CAPABILITY DEMAND
↓
RESOURCE / AUTHORITY GATE
↓
CAN-TRAIN
↓
TRAIN COMMAND
↓
QUEUE ACCEPTANCE?
↓
PENDING
↓
TRAINING COMPLETION?
↓
OBJECT BIRTH
↓
PLACEMENT / INITIAL POSITION
↓
DEPLOYMENT
```

Each question mark is an evidence boundary, not an assumed failure.

## 5. Historical source versus replay source

The historical source is strongest for:

```text
WHY THE CONTROLLER ISSUES TRAIN
```

The replay is strongest for:

```text
WHEN A TRAIN ACTION WAS RECORDED
```

An engine replay/state extractor would be strongest for:

```text
WHICH OBJECT WAS ACTUALLY CREATED
```

Therefore no single source currently closes the whole chain.

This is exactly why the project has maintained separate evidence grades rather than treating one source as universal.

## 6. Byzantine camel case

The historical chain remains:

```text
MOUNTED / CAVARCHER SIGNAL
↓
CAMEL RESPONSE CONDITIONS
↓
TRAINCAMEL
↓
PRODUCER SEARCH
↓
CAN-TRAIN
↓
TRAIN CAMEL-LINE
```

Replay corroboration shows concrete Byzantine camel-line production commands in reference games.

But the evidence does not yet establish a one-to-one lineage such as:

```text
seq 2,945,313
→ Stable X
→ queue slot Y
→ Camel object ID Z
→ creation timestamp T
```

Without that lineage, the correct closure remains L6/L7 rather than L8.

## 7. Why aggregate correlation is insufficient

Suppose:

```text
T0 = train camel command
T1 = camel population rises by 1
```

That is strong correlation.

It is not automatically identity proof because another Camel could have been:

- already training;
- queued earlier;
- completed at approximately the same time;
- created by another producer;
- represented differently by the parser;
- affected by an unobserved lifecycle event.

Therefore the interpreter's existing matching hierarchy remains appropriate:

```text
1. exact object ID
2. exact producer/builder/actor ID + operation
3. exact type + temporal + spatial correlation
4. aggregate correlation
5. heuristic inference
```

Levels 4–5 can support hypotheses but should not promote an object-birth claim to high-confidence causal closure.

## 8. CaptureAge / engine replay implication

CaptureAge's investigated native layer exposes object/entity and production-state concepts, including combat-unit creation and production-queue records. This demonstrates that an engine-replay environment can represent the lifecycle at a richer level than a raw command parser.

However, the project's prior archaeology did not establish a clean, supported external contract that takes an arbitrary `.aoe2record` and emits a trustworthy object-birth ledger suitable for AEGIS forensic use.

Therefore:

```text
CADE = PROMISING VALIDATION BACKEND
≠
CURRENTLY CERTIFIED OBJECT-BIRTH ORACLE
```

This preserves the evidence boundary established in earlier passes.

## 9. New distinction: command lineage versus object lineage

The project should now explicitly maintain two separate provenance graphs.

### Command lineage

```text
STRATEGIC STATE
↓
RULE
↓
AUTHORITY
↓
COMMAND
↓
REPLAY EVENT
```

### Object lineage

```text
COMMAND
↓
QUEUE ENTRY
↓
PENDING OBJECT
↓
CREATION
↓
OBJECT ID
↓
INITIAL POSITION
↓
SUBSEQUENT ORDERS
```

The first graph is substantially better established.

The second remains incomplete.

This distinction prevents a major category error: assuming that because the command lineage is closed, the object lineage is automatically closed.

## 10. Consequence for battlefield analysis

The missing object identity propagates forward.

Without L8:

```text
OBJECT BIRTH
↓
DEPLOYMENT
↓
ENGAGEMENT
↓
EFFECT
```

cannot be established at individual-object resolution.

Therefore battlefield-effect claims must remain bounded unless independent state/event evidence identifies the participating object or a sufficiently exact population transition.

## 11. Current external parser landscape

Current public parser projects reinforce the boundary rather than eliminate it.

`aoc-mgz` supports modern DE records and describes the record as initial state plus command/move stream; its documentation notes that arbitrary-time resources/kills/etc. cannot simply be read without replaying the match in-game. citeturn0search2

`mgz-fast` is intentionally stripped down for fast header/body parsing and likewise treats the body as operations rather than a complete world-state timeline. citeturn0search1

A separate 2026 project documenting current DE replay tooling similarly describes CaptureAge as obtaining rich live state by replaying the growing record through the actual game engine, rather than consuming a direct telemetry stream. citeturn0search0

This independently supports the AEGIS conclusion that command parsing and world-state reconstruction are distinct problems.

## 12. Hostile QC

**Claim:** `train` proves object creation.  
**Verdict:** REJECTED.

**Claim:** pending-object count proves object birth.  
**Verdict:** REJECTED.

**Claim:** a population increase immediately after `train` proves one-to-one identity.  
**Verdict:** REJECTED without stronger lineage evidence.

**Claim:** parser inability to promote object birth means the unit did not spawn.  
**Verdict:** REJECTED.

**Claim:** CaptureAge's internal entity vocabulary proves the project can already extract object lineage.  
**Verdict:** REJECTED. Representation capability is not the same as a certified extraction pipeline.

**Claim:** command chronology plus aggregate correlation is enough for battlefield-effect proof.  
**Verdict:** REJECTED.

## 13. Evidence ledger

| Proposition | Grade |
|---|---|
| Historical AI issues concrete camel train commands | DIRECT |
| Replay body records production actions | DIRECT |
| Pending production is distinct from completed population | DIRECT |
| `up-pending-objects` represents pending train/build state | DIRECT |
| Train command precedes any resulting completion | DIRECT / mechanical |
| Exact train-command → queue-entry identity | NOT PROVEN |
| Exact queue-entry → object-ID identity | NOT PROVEN |
| Object birth after a particular historical train command | NOT PROVEN |
| Object deployment linkage | NOT PROVEN |
| Object engagement linkage | NOT PROVEN |
| Battlefield effect | NOT PROVEN |
| Raw replay parser alone can reconstruct arbitrary-time world state | REJECTED |
| Engine replay can expose richer lifecycle state | DIRECT capability evidence |
| Certified external object-birth extraction pipeline exists in AEGIS | NOT PROVEN |

## 14. Updated realization ladder

```text
L0  THREAT OBSERVED
L1  THREAT CLASSIFIED
L2  RESPONSE ELIGIBLE
L3  RESPONSE STATE ACTIVATED
L4  PRODUCER SELECTED
L5  FEASIBILITY CONFIRMED
L6  TRAIN COMMAND ISSUED
L7  QUEUE / PENDING ESTABLISHED
L8  OBJECT BIRTH
L9  DEPLOYMENT
L10 ENGAGEMENT
L11 EFFECT VERIFIED
```

Current historical Byzantine camel closure:

```text
L0–L6 = CLOSED
L7      = CORROBORATED / NOT UNIVERSALLY PROMOTED
L8–L11  = OPEN
```

## 15. Research consequence

Pass 72 does not produce a new implementation requirement. It produces a sharper **evidence boundary**.

The central lesson is:

> A recorded command stream can establish what the controller attempted, but object-birth provenance requires either exact lifecycle records or deterministic engine replay/state reconstruction.

This is a major reason the project must preserve the distinction between control closure and world closure.

## 16. Closure

Pass 72 closes the methodological question of **what evidence is required to claim object birth** and confirms that the currently available command/pending evidence does not universally meet that standard.

The strongest defensible model is:

```text
HISTORICAL CONTROLLER
→ AUTHORIZED PRODUCTION
→ TRAIN COMMAND
→ QUEUE/PENDING
→ [WORLD ENGINE]
→ OBJECT BIRTH
```

The `[WORLD ENGINE]` boundary is currently the unresolved bridge.

No implementation, architecture construction, runtime promotion, or `.per` artifact is authorized by this pass.
