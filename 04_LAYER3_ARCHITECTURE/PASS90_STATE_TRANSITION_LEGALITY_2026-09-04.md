# AEGIS Layer 3 — Pass 90 State Transition Legality Table

Date: 2026-09-04
Status: architecture contract

## 1. Core state machine

`FREE → TARGET_SELECTED → AUTHORIZED → COMMAND_ELIGIBLE → ISSUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

Failure/recovery edges may return to `TARGET_SELECTED`, `FREE`, or `REASSESS`, depending on cause. No state may silently imply a later state.

## 2. Legality matrix

| From | Event / guard | To | Legal? | Required evidence |
|---|---|---|---|---|
| FREE | valid candidate found | TARGET_SELECTED | YES | candidate validity |
| TARGET_SELECTED | hard constraints pass + ownership acquired | AUTHORIZED | YES | feasibility + owner |
| TARGET_SELECTED | hard constraint fails | FREE | YES | failed predicate |
| AUTHORIZED | command-stage guard passes | COMMAND_ELIGIBLE | YES | valid commit + producer + resources |
| AUTHORIZED | target/producer disappears | REASSESS | YES | invalidation observation |
| COMMAND_ELIGIBLE | side-effect rule fires | ISSUED | YES | command occurrence |
| ISSUED | engine/queue evidence | PENDING | YES | pending/queue observation |
| ISSUED | no acceptance evidence | REASSESS/WAIT | YES | timeout/evidence policy |
| PENDING | queue completion evidence | CREATED | YES | aggregate or stronger creation evidence |
| PENDING | queue cancellation/failure | REASSESS | YES | failure evidence |
| CREATED | capability availability evidence | AVAILABLE | YES | world observation |
| AVAILABLE | deployment evidence | DEPLOYED | YES | spatial/task evidence |
| DEPLOYED | battlefield interaction | EFFECTIVE | YES | objective-specific postcondition |
| EFFECTIVE | objective invalidated | REASSESS | YES | objective validity failure |
| any active | generation mismatch | REJECT_STALE | YES | generation comparison |
| any active | owner mismatch | REJECT_UNAUTHORIZED | YES | ownership guard |
| any active | commitment invalid | RESET/REASSESS | YES | `COMMIT.VALID=0` |

## 3. Forbidden inference edges

The following are explicitly illegal:

- `CAN-TRAIN → TRAINED`
- `TRAIN → QUEUED`
- `QUEUED → CREATED` without completion evidence
- `CREATED → DEPLOYED` without deployment evidence
- `DEFICIT=0 → OBJECTIVE_SUCCESS`
- `TIMER_TRIGGERED → COMMITMENT_EXPIRED` unless the state contract explicitly binds them
- `RESERVED → OWNERSHIP_TRANSFER`
- `STATE_WRITE → AUTHORITY_TRANSFER`
- `DIRTY=0 → NO_EVENT`
- parser uncertainty → gameplay failure

## 4. Candidate-selection protocol

Selection must not accidentally recreate first-feasible-wins.

**Ordered-policy mode:** evaluate candidates in a deliberately frozen policy order, with the order itself documented as policy.

**Best-so-far mode:** maintain an incumbent candidate and compare each feasible candidate against it using an explicit comparator. The first feasible candidate becomes only the initial incumbent, not the automatic winner.

The Cavalry Slice will use the simpler mode initially, provided the comparator and tie-break rules are frozen before implementation.

## 5. Recovery legality

Recovery is not synonymous with retry. Each failure is classified as economic, producer, queue-capacity, lifecycle, temporal, target-invalidity, partial-progress, or evidence failure. The recovery policy may retain policy state, repair execution conditions, release commitment state, or re-arbitrate.

## 6. Objective validity

`CAPABILITY_DEFICIT=0` means the measured capability requirement is satisfied. It does not prove the strategic objective succeeded. Objective success requires an independent postcondition (`V8` level) defined by the objective contract.

## 7. Review watchdog

An active commitment must have an exit/watchdog condition. If progress evidence does not arrive within the allowed interval, the controller must enter review/recovery rather than remaining indefinitely authoritative.
