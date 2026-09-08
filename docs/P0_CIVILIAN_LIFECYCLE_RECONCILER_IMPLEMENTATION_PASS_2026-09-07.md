# P0 Civilian Lifecycle Reconciler — Implementation Pass

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Status:** STATIC CANDIDATE — NOT RUNTIME QUALIFIED  
**Implementation:** `implementation/AEGIS-civilian-lifecycle-reconciler-v0.per`

## Objective

Close the semantic gap between villager production command issuance and actual civilization state. The system must not treat `can-train`, `up-train`, or pending queue state as equivalent to a completed villager.

## Evidence basis

The stock corpus uses `up-get-fact unit-type-count villager ...` and `unit-type-count-total villager ...` as native observation patterns. The current AEGIS census therefore uses a discrete villager census rather than deriving villager count from total population. The current census also exposes pending villager state independently.

## Lifecycle contract

```text
REQUESTED → AUTHORIZED → ISSUED → PENDING → CENSUS DELTA → CONFIRMED
                                      └→ NO DELTA → FAILED
```

The reconciler captures a villager baseline when a fresh production generation reaches the issued state. Pending queue observation advances the record to `PENDING`. A later census strictly greater than the baseline is the completion evidence.

## Important correction

The previous production actuator consumed civilian demand at queue admission. That remains a candidate behavior, but this reconciler establishes the required downstream invariant: queue admission alone cannot close the civilization lifecycle. If a queued production disappears without a census increase, the lifecycle records failure and waits for a later demand generation to own re-request.

This avoids an invalid inference from population accounting or pending-object disappearance.

## State allocation

- 441 generation
- 442 valid
- 443 lifecycle stage
- 444 baseline villager census
- 445 observed villager census
- 446 pending state
- 447 confirmed census delta
- 448 attempts
- 449 observation timestamp

## Static qualification

The candidate was constructed with the existing AEGIS namespace discipline and consumes already-published census/production state. It introduces no Promisory runtime dependency and no jump control flow.

Required local checks before promotion:
- balanced parentheses
- unique AEGIS definitions
- undefined AEGIS symbols = zero
- numeric goal collision = zero
- production root unchanged
- runtime package parse/start test

## Adversarial findings

### Archaeologist
The completion predicate is intentionally based on an engine-observable discrete census. Same-pass visibility is not assumed. The implementation does not claim that a census delta identifies the exact producing Town Center; that attribution remains unqualified.

### Byzantine Architect
Civilian continuity is treated as substrate. Strategic Byzantine priorities remain upstream. The reconciler creates a reliable physical-state boundary on which economic allocation can later depend.

### AI(HD)+Promisory
The design preserves a stock-compatible behavioral distinction between production authorization, queue state, and actual unit census. Failure is not silently converted into success.

## Remaining qualification risks

1. Exact target-build timing between queue admission and census update remains runtime-dependent.
2. A census increase may be caused by another villager production request unless generation fencing prevents concurrent lifecycle ownership. The current vertical slice therefore assumes one active villager-production generation at a time; concurrency must be tested before scaling production.
3. The current pending predicate is aggregate, so multiple simultaneous villager queues are not individually attributable. This is acceptable for V0 only under the bounded single-request actuator contract.
4. Failure classification remains intentionally coarse. Later recovery must distinguish affordability failure, endpoint failure, command non-observation, cancellation, and other causes where observable evidence permits.

## Promotion decision

**Do not load this candidate into the production root.** It is an implementation artifact for the first civilian closed-loop vertical slice. Runtime qualification must use a disposable target-build package and direct engine observation.

## Next engineering target

After this pass, extend the civilian state with worker-role census and housing/infrastructure state, then build the first demand-to-worker-allocation path:

```text
CENSUS → ROLE VECTOR → ECONOMIC DEMAND → SOURCE/DROPSITE SERVICEABILITY → WORKER SELECTION → TASK COMMAND → PRODUCTIVITY → RECOVERY
```
