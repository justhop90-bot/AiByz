# R2 — Civilian Census v0 Runtime Rung

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Status:** READY FOR MANUAL TARGET-BUILD EXECUTION  
**Qualification state:** S4 static / S5 unproven

## Objective

Prove the smallest useful AEGIS runtime unit:

`TARGET ENGINE → AEGIS ROOT → FOUNDATION → CIVILIAN CENSUS → NATIVE FACT OBSERVATION`

The census module must execute and publish a valid observation frame without requiring demand, worker allocation, military policy, or physical production.

## Module under test

`AegisProm/AEGIS-civilian-census-v0.per`

Current source hash recorded from repository snapshot:
`f0157efe6bd457411585fe6b3f82ed36dcd33f9b`

The module declares its purpose as an engine-observable civilian census and explicitly separates observation from strategic policy and worker allocation.

## Preconditions

- exact target AoE2DE build identified;
- canonical source snapshot recorded;
- no scenario-loader automation;
- no invasive game attachment;
- qualification root contains no unqualified AEGIS modules;
- test is repeatable manually.

## Stimulus

Start an ordinary target-build game/session using the supported normal game path.

The first test does not need a strategic challenge. It needs only enough normal game time for the census bootstrap and timer-triggered observation rules to execute.

Do not alter the source during the run.

## Expected lifecycle

1. `game-time < 2` enables census timer 42.
2. timer fires;
3. census resets its validity/stage;
4. native villager count is read;
5. native town-center count is read;
6. native game time is read;
7. census cycle/generation advances;
8. census reaches QUALIFIED;
9. validity becomes 1;
10. pending-villager observation is recorded separately.

These expectations come from the source contract; they are hypotheses until target-engine evidence confirms them.

## Evidence required for PASS

### E1 — Load

Evidence that the exact tested source was the source loaded by the target engine.

### E2 — Execution

Evidence that the census initialization/observation rules executed in the target engine.

### E3 — Observation

Evidence consistent with the expected villager/TC/time census frame.

### E4 — Repeatability

At least two independent runs produce the same bounded observation contract without manual state mutation.

### E5 — Isolation

No demand, production, military, worker allocation, or other unqualified module is required to explain the result.

## Failure conditions

Fail closed if:

- the load cannot be proven;
- the game/session hangs or terminates before evidence is obtained;
- census values appear only in source/static artifacts;
- a later module is required to make the census fire;
- observed state cannot be distinguished from pre-existing engine state;
- evidence depends on an unproven side channel.

## Promotion

R2 passes only as an isolated runtime observation module. It does not promote the civilian production slice and does not authorize production-root promotion.

After R2 passes twice, R3 may admit civilization-state-v0.
