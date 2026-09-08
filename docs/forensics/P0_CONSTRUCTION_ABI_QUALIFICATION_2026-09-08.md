# P0 Construction ABI Qualification — 2026-09-08

## Status
STATIC ABI MODEL: QUALIFIED WITH RUNTIME BOUNDARY

## Correction: AiBuilder
`AiBuilder` is stock generic example/reference material for authors building custom AIs. It is NOT part of the stock Byzantine runtime dependency graph merely because it exists in the installation. It is therefore excluded from the Byzantine reconstruction target unless a direct load/reference proves otherwise.

## Construction command families
The stock construction corpus demonstrates three materially different command families:

- `build <unit>`: native AI build command. It is used directly after `can-build` and therefore represents the simplest engine-facing construction path.
- `up-build-line <point> <point> <building>`: explicit placement/build-line path. It couples a selected point with a building-line identifier and is used after `up-can-build-line`.
- `up-build place-control 0 <building>`: placement-controller path. It delegates spatial selection to the placement subsystem after placement parameters have been established.

These must not be collapsed into one abstract operation during AEGIS implementation.

## Placement is a state machine
Observed stock patterns establish:

`construction demand → can-build authorization → placement parameterization → placement search → command → pending-placement → foundation/structure observation → builder allocation → completion`

Failure paths include deletion/reset of bad pending placements, point perturbation, retry loops, builder escalation, and strategic cancellation when a higher-priority construction requirement changes.

## Important stock evidence
The construction source explicitly:

1. tests `can-build` before issuing native construction;
2. uses `up-can-build-line` before explicit point placement;
3. establishes placement data and strategic placement parameters before `up-build place-control`;
4. detects `up-pending-placement` independently from ordinary pending objects;
5. calls `up-reset-placement` to recover from invalid/stalled placements;
6. assigns builders separately from placement issuance;
7. modifies builder count in response to urgency/threat;
8. uses bounded retry loops and geometric point perturbation for difficult placements;
9. uses construction state to modify town-size and strategic policy;
10. contains specialized construction policy for houses, camps, mills, markets, towers, castles, town centers, military infrastructure, and map-specific behavior.

## AEGIS consequence
AEGIS Construction OS must own the complete lifecycle rather than issuing scattered `build` commands from cognition or operations.

Required service boundary:

`construction.request`
`construction.admit`
`construction.reserve`
`construction.select-placement`
`construction.authorize`
`construction.issue`
`construction.observe`
`construction.assign-builders`
`construction.verify`
`construction.recover`

Cognition should request a typed construction objective. It should not directly manipulate placement state.

## ABI items still requiring live qualification
Static source establishes call families but cannot prove all interpreter side effects. Target-build runtime tests remain required for:

- whether `build` and `up-build-line` create identical pending-placement state;
- exact same-pass visibility of placement mutations;
- exact semantics of `up-reset-placement` after failed placement;
- whether builder assignment is immediately visible to object-data queries;
- command-issued versus engine-observed boundaries;
- jump behavior surrounding placement loops;
- precise failure return/state behavior of `up-can-build-line`;
- interaction between escrow authorization and placement failure.

## Evidence boundary
The construction archaeology is now complete enough that additional static searching would have diminishing value. The remaining uncertainty is interpreter/runtime semantics and must be settled experimentally.

## Review
### ABI / compiler
Do not infer command equivalence from similar outcomes. Preserve separate command paths until runtime proves equivalence.

### Byzantine strategy
Construction is strategic infrastructure: houses, dropsites, military production, defensive towers, castles, TCs, markets, docks, and farms participate in economy and military policy. Placement must remain policy-aware.

### AI(HD) behavioral regression
Preserve retry, cancellation, builder escalation, pending-placement recovery, and infrastructure continuity. A simple `request → build` replacement would regress stock behavior.

## Decision
`AiBuilder` is excluded from the stock Byzantine runtime target. `buildings.per` and its proven nested construction dependencies remain core reconstruction material. Construction now moves from archaeology to controlled runtime ABI qualification.