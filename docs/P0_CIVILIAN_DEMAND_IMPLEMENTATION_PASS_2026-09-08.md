# AEGIS-BYZ — P0 CIVILIAN DEMAND IMPLEMENTATION PASS
## Villager + Housing Demand Boundary — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** STATIC-QUALIFIED CANDIDATE / NOT RUNTIME-QUALIFIED
**Implementation:** `implementation/AEGIS-civilian-demand-v0.per`

## Purpose

This pass establishes the first policy-to-substrate boundary. Civilization State is consumed as reconciled state; this module derives typed civilian demand without issuing production or construction commands.

## Contract

The module owns:

- demand generation;
- villager demand flag;
- housing demand flag;
- urgency;
- demand stage;
- source observation marker.

It does not own:

- engine facts;
- World Model publication;
- worker assignment;
- training queue execution;
- building placement;
- resource allocation;
- verification.

## Villager lifecycle

The current candidate raises villager demand when the reconciled population is below population capacity and the engine reports villager training as currently possible.

The resulting state is a request, not a command. A downstream production service must later perform economic admission, endpoint selection, command issuance and verification.

## Housing lifecycle

Housing demand is raised when housing headroom is at or below two, population headroom exists, no house is pending, and the engine reports that a house can currently be built.

This deliberately uses engine `housing-headroom`, `population-headroom`, `up-pending-objects`, and `can-build` predicates rather than inventing a synthetic building-count proxy.

## ABI discipline

The module does not depend on same-pass visibility between its own mutation and downstream execution. It consumes a generation-fenced Civilization State snapshot and publishes demand for later service consumption.

## Static qualification

Target-machine static audit:

- 58 lines;
- balanced parentheses: delta 0;
- 13 `defconst` declarations;
- referenced AEGIS symbols resolve against the current machine runtime corpus;
- new goal IDs: 421-426;
- no collision with existing AEGIS numeric IDs observed in the 300-420 range.

Source SHA-256:
`5FC984B00D256288A8F9CE4CA4A074F123ABAE20D0C3E7AFF2588A6AD869EC15`

## Three-personality review

**Archaeologist:** acceptable because the module uses documented/native predicates already present in target stock and does not claim same-pass execution semantics.

**Byzantine Architect:** correct ownership boundary. Future Byzantine strategic demand can add pressure/priority without changing the physical services.

**AI(HD)+Promisory:** acceptable only as a demand layer. Production must preserve pending state, escrow/affordability, endpoint selection, and command-vs-confirmation separation.

## Next code target

Implement the downstream villager production service as a controlled actuator:

```text
VILLAGER DEMAND
→ ECONOMIC ADMISSION
→ TRAINING AUTHORIZATION
→ QUEUE COMMAND
→ PENDING OBSERVATION
→ VILLAGER CENSUS CHANGE
→ VERIFICATION
→ DEMAND CLEAR / RETRY
```

Housing should follow as a separate construction actuator rather than being embedded in villager production.

## Promotion rule

Do not load this candidate into the production root until the Civilization State → Demand closure is runtime-tested on the target build. The current file is implementation evidence, not runtime qualification.
