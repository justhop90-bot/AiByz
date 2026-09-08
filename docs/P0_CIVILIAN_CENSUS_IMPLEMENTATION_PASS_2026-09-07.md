# AEGIS-BYZ — P0 CIVILIAN CENSUS IMPLEMENTATION PASS

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** STATIC-QUALIFIED CANDIDATE / NOT RUNTIME-QUALIFIED
**Implementation:** `implementation/AEGIS-civilian-census-v0.per`

## Purpose

This pass adds the missing observation boundary required to close villager production verification. It is intentionally a dedicated engine-observation adapter rather than adding raw acquisition to Civilization State.

## Evidence from stock

The untouched stock AI uses `up-get-fact unit-type-count villager ...` and `up-get-fact unit-type-count-total villager ...` during initialization, and separately uses `up-get-fact building-type-count-total town-center ...`. This establishes that these native fact forms are part of the stock target-build scripting corpus.

The census therefore observes:

- villager count;
- Town Center count;
- pending villager production;
- observation time;
- monotonically advancing census generation/cycle.

## Contract

```text
ENGINE
  -> NATIVE CENSUS FACTS
  -> COMPLETE CENSUS FRAME
  -> QUALIFIED OBSERVATION
  -> CIVILIZATION STATE / VERIFICATION
```

Pending production is explicitly independent from population-minus-villagers arithmetic. This avoids treating population composition as a substitute for queue state.

## ABI discipline

No jumps are used. No same-pass visibility is required by downstream consumers. The module does not issue production commands. `up-get-fact` is used only for observation; `up-pending-objects` is used only as a pending-state signal.

Timer 42 is isolated from the existing AEGIS Operations timer 41 and is not enabled by the production root because this remains a candidate.

## Static qualification

Target-machine audit:

- 60 lines;
- balanced parentheses: delta 0;
- AEGIS goal IDs 433-440;
- no undefined AEGIS symbols against the current AEGIS namespace;
- no production-root load added;
- candidate hash: `216FF03C968630EB6AA838A08069FA889C0C3E7EF05A987216B25013EAC6173C5`.

## Adversarial review

**Archaeologist:** native fact acquisition belongs here rather than in the semantic state layer; command semantics remain unclaimed.

**Byzantine Architect:** census is neutral infrastructure. Byzantine policy consumes the census but does not own the measurement mechanism.

**AI(HD)+Promisory:** stock's discrete villager census and pending-state concepts are preserved without importing stock control-flow topology.

## Critical limitation

Static qualification does not establish target-build timer cadence, same-pass fact visibility, pending-object refresh timing, or the exact relationship between a completed villager and the next census frame. Those require runtime qualification.

## Next implementation target

Build a reconciliation/verification consumer that compares:

`requested villager demand -> pending state -> observed villager census`

and handles success, timeout/failure, duplicate prevention, and generation advancement. Housing census should be added alongside that consumer so the first civilian lifecycle can close without relying on raw `housing-headroom` alone.

## Promotion rule

Do not load this candidate into the production root until disposable target-build runtime testing proves census acquisition, timer behavior, pending observation, completion observation, and generation continuity.
