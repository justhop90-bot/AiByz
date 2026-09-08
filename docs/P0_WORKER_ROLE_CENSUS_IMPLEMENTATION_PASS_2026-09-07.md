# P0 Worker Role Census — Implementation Pass

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Status:** STATIC CANDIDATE — NOT RUNTIME QUALIFIED  
**Implementation:** `implementation/AEGIS-worker-role-census-v0.per`

## Objective

Establish an engine-observable worker-role vector before implementing economic allocation. AEGIS must measure operational worker state rather than infer roles from villager identity or from the commands it previously issued.

## Stock evidence recovered

The untouched stock `Promisory/gatherers.per` directly uses these semantic role identifiers with `unit-type-count`:

- `villager-food`
- `villager-forager`
- `villager-shepherd`
- `villager-hunter`
- `villager-fisherman`
- `villager-farmer`
- `villager-wood`
- `villager-gold`
- `villager-stone`
- `villager-builder`

The same stock corpus also directly retrieves role counts using `up-get-fact unit-type-count`, including farmer, forager, and shepherd. Therefore V0 uses the engine's own role classification instead of rebuilding it from action/order fields.

## Implementation

The candidate allocates goals 450–464 and publishes one role vector every five seconds after a bootstrap timer. It records an observation timestamp, generation, cycle, validity, and stage.

No strategic-number policy, worker selection, resource source selection, or task command is included. This is deliberately an observation service.

## Architecture

```text
ENGINE CIVILIAN STATE
        ↓
WORKER ROLE CENSUS
        ↓
ROLE VECTOR
        ↓
ECONOMIC ARBITRATION
        ↓
WORKER TARGETING / TASKING
```

## Important semantic boundary

`villager-wood`, `villager-gold`, etc. are engine semantic classifications observed from the current worker state. They are not persistent identities. A worker may change role as commands, tasks, interruptions, and resource conditions change.

The aggregate `villager-food` value should not be treated as a mutually exclusive bucket until target-build runtime evidence establishes its relationship to the more specific food-role classifications. V0 records it as a separate engine observation rather than deriving or reconciling it algebraically.

## Static qualification

Local audit on the candidate:

- 61 lines
- parenthesis delta = 0
- 19 AEGIS definitions
- undefined AEGIS symbols = 0
- goal range = 450–464
- no production-root load entry
- no Promisory dependency
- no jump control flow

## Three-personality review

### Archaeologist
The implementation relies on stock-observed engine facts rather than inferred task state. It does not assume same-pass visibility or that role census updates immediately after a command.

### Byzantine Architect
The vector is intentionally strategy-neutral. Later Byzantine policy can express demand for food, wood, gold, stone, or military-support roles without corrupting the observation layer.

### AI(HD)+Promisory
Using the engine's own worker-role facts preserves a key stock behavioral contract: the economic controller reasons from current worker classification rather than assuming its previous assignment succeeded forever.

## Qualification risks

1. The exact update cadence of role classification is not runtime-qualified.
2. `villager-food` may overlap semantically with specific food roles; no algebraic identity is asserted.
3. Builder state is observed, but the role census does not identify the construction target. Builder continuity requires a separate object/task service.
4. Idle/interrupted state is not represented as a simple complementary count. It must be recovered through worker object/action/order observations.
5. Role census is aggregate; individual worker identity and source/dropsite assignment remain separate services.

## Promotion decision

**Candidate only. Do not load into production.** Runtime qualification must establish that each role fact parses, updates, and remains coherent across task reassignment and interruption.

## Next engineering target

Build the first economic demand-to-role-deficit adapter. It should compare desired role counts against this observed vector, explicitly account for protected workers, and produce typed worker-target demand without issuing resource commands yet.
