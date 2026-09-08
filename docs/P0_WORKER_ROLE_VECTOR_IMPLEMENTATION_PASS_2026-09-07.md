# P0 Worker Role Vector Implementation Pass — 2026-09-07

## Status

IMPLEMENTATION CANDIDATE / STATIC-QUALIFIED ONLY.
The candidate is not loaded by the production AEGIS root and is not runtime-qualified.

Target runtime: AoE2DE 101.103.48987.0 / BuildID 24094652.

## Objective

Create the first explicit reconciliation layer between engine-observed worker roles and a desired civilian role vector.
The layer computes positive role deficits. It does not select workers, choose resource sources, issue task commands, or perform strategic arbitration.

Pipeline established:

WORKER ROLE CENSUS → DESIRED ROLE VECTOR → ROLE DEFICIT VECTOR → ECONOMIC DEMAND

## Evidence used

The untouched stock AI directly uses semantic worker classifications including:

- villager-food
- villager-forager
- villager-shepherd
- villager-hunter
- villager-fisherman
- villager-farmer
- villager-wood
- villager-gold
- villager-stone
- villager-builder

Stock `gatherers.per` also retrieves role counts with `up-get-fact unit-type-count`, confirming that role counts can be observed as engine facts rather than reconstructed solely from action/order state.

## Architectural decision

The worker-role vector is an observation/reconciliation boundary. Desired role counts are policy inputs. The implementation therefore keeps the following concepts separate:

1. observed engine role count
2. desired role count
3. positive deficit
4. worker candidate selection
5. source qualification
6. task command
7. productivity confirmation

A role deficit does not imply that an arbitrary worker should immediately be retasked.

## V0 implementation

File: `implementation/AEGIS-worker-role-vector-v0.per`

Goal allocation: 465–478.

State includes:

- generation
- validity
- stage
- desired food/wood/gold/stone/builder
- deficit food/wood/gold/stone/builder
- observation timestamp

The vector is fenced by worker-role-census generation. A fresh census creates a new reconciliation frame.

Negative arithmetic results are clamped to zero. V0 therefore represents unmet demand, not surplus magnitude.

## Important limitation

V0 intentionally contains conservative zero policy targets. This is an architecture/ABI candidate, not the final economic policy. Non-zero Byzantine targets must be supplied by the downstream demand/arbitration layer after strategic priorities are defined.

This prevents the role-vector layer from silently becoming the economy's strategic brain.

## ABI qualification status

OBSERVED:
- stock recognizes the worker-role identifiers above in `unit-type-count` predicates.
- stock retrieves worker-role counts with `up-get-fact unit-type-count ...`.

IMPLEMENTED:
- AEGIS worker-role generation fencing.
- explicit desired/observed/deficit separation.
- bounded positive-deficit computation.

STATIC-QUALIFIED:
- candidate has balanced parentheses.
- goal allocation does not overlap the existing AEGIS 300–464 allocation.
- no undefined AEGIS references were detected during local static audit.
- candidate is absent from the production root load graph.

UNQUALIFIED:
- exact target-build behavior of the candidate arithmetic sequence.
- same-pass visibility assumptions.
- whether all desired-role values should be represented as goals, constants, or later service inputs.
- semantic overlap/exclusivity relationships among stock worker classifications.
- whether multiple role counts can legitimately overlap for the same worker under all engine states.

## Reviewer decisions

### Archaeologist

Accepted the observation boundary because role counts are taken from engine facts already used by stock. Rejected any assumption that role identifiers imply immutable worker identity or that role totals are automatically mutually exclusive.

### Byzantine Architect

Accepted the separation between economic policy and worker mechanics. Final Byzantine allocation must be driven by strategic demand, resource portfolio state, opponent pressure, infrastructure, and timing rather than hard-coded opening percentages in this layer.

### AI(HD)+Promisory

Accepted explicit desired-versus-actual reconciliation as the behavioral contract. Stock's deeper gatherer subsystem remains the reference for later worker selection, interruption handling, source qualification, and reallocation; its historical control flow should not be copied wholesale.

## Next dependency

The next layer should turn deficits into typed economic demand while preserving generation, priority, urgency, reason, and bounded expiry. Worker selection must remain downstream of demand arbitration.

The eventual civilian economic loop is:

DESIRED ROLE VECTOR → OBSERVED ROLE VECTOR → DEFICIT → DEMAND → ARBITRATION → ELIGIBLE WORKERS → SOURCE/DROPSITE QUALIFICATION → TASK COMMAND → ENGINE OBSERVATION → PRODUCTIVITY/RECOVERY.
