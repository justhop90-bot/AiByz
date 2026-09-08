# AEGIS-BYZ — P0 VILLAGER PRODUCTION ACTUATOR IMPLEMENTATION PASS

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** STATIC-QUALIFIED CANDIDATE / NOT RUNTIME-QUALIFIED
**Implementation:** `implementation/AEGIS-villager-production-v0.per`

## Objective

The third implementation pass establishes the first physical actuator in the AEGIS civilian lifecycle. Civilization demand remains policy; this module performs bounded engine interaction and records whether queue admission becomes observable.

## Contract

```text
CIVILIAN DEMAND(G)
  -> ACTUATOR ADMISSION(G)
  -> CAN-TRAIN / ENDPOINT CHECK
  -> COMMAND ISSUED(G)
  -> PENDING ENGINE STATE OBSERVED
  -> DEMAND CONSUMED
```

Completion is deliberately not claimed. A pending villager proves queue admission evidence, not completed unit production. Completion belongs to the later census/verification layer.

## ABI choices

The actuator uses the stock-proven physical primitive `up-train escrow-state c: villager`, guarded by `can-train villager` and a Town Center count. This preserves engine escrow semantics instead of inventing a parallel resource payment model.

The actuator uses generation fencing and a maximum of two command attempts. It does not use jumps, same-pass assumptions, or command-success assumptions.

## State allocation

Goals 427-432:

- generation
- valid
- stage
- action
- attempts
- observed

Stages:

`INIT=0`, `AUTHORIZED=1`, `ISSUED=2`, `WAITING=3`, `FAILED=4`.

## Adversarial findings

### Archaeologist

The critical ABI distinction is preserved: `can-train` authorizes an attempt; `up-train` issues a command; `up-pending-objects` provides later engine evidence. None is treated as proof of completion.

### Byzantine Architect

Villager production is infrastructure supporting Byzantine adaptation, not a Byzantine strategy rule. The actuator therefore accepts demand rather than selecting economic composition itself.

### AI(HD)+Promisory

The stock behavioral contract of villager production is retained at the engine boundary: affordability/eligibility precedes `up-train`, and pending state is observable afterward. The design intentionally does not reproduce stock jump topology.

## Static qualification

Target-machine static checks must confirm balanced syntax, unique AEGIS goal allocation, and absence of undefined AEGIS symbols before any runtime package is attempted. Runtime qualification remains mandatory.

## Known limitation

The module consumes villager demand as soon as pending queue admission is observed. This is intentional for the current lifecycle but creates a required downstream contract: if the queued villager later fails to complete, census/verification must generate a fresh demand rather than relying on the original request remaining active.

Therefore the next pass must implement villager census and production confirmation, followed by reconciliation of demand against actual civilian population.

## Promotion rule

Do not load this candidate into the production root until a disposable target-build runtime package demonstrates parse/start, demand admission, command issuance, pending observation, and correct recovery behavior without duplicate issuance.
