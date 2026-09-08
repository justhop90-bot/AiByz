# P0 Worker Recovery — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate implemented and archived; NOT runtime-qualified; NOT loaded by production root.

## Objective

Convert a verified worker-task failure into a bounded recovery disposition without allowing the recovery layer to issue uncontrolled replacement commands. Recovery either permits a bounded retry or returns control upstream to economic arbitration.

## Contract

VERIFICATION FAILURE → RECOVERY REVIEW → BOUNDED RETRY or UPSTREAM RE-ARBITRATION → CLOSED.

Recovery records generation, resource, failure class, attempt count, disposition, observation time, and cycle. It is generation-fenced against the command generation.

## Evidence basis

Existing AEGIS forensic work establishes that stock recovery is distributed and distinguishes worker/task/source conditions. Stock gatherer logic also uses explicit object-state checks rather than treating all worker failure as one state. The recovery implementation therefore preserves failure classification and avoids a universal replacement action.

## Retry policy

V0 retries only the target-not-observed verification failure while the attempt count remains below two. Worker-missing failures and exhausted attempt budgets return upstream. This is deliberately conservative and is not claimed to reproduce stock retry policy.

## Important boundary

Recovery does not select a new worker, source, or dropsite. It emits a disposition boundary. The economic scheduler remains responsible for deciding whether demand is still valid and, if so, re-arbitrating and reselecting.

## Qualification states

OBSERVED: stock distributed recovery and explicit worker/task/source failure distinctions.
CORRELATED: bounded recovery plus upstream re-arbitration is safer than direct replacement commands.
IMPLEMENTED: generation-fenced worker recovery state machine.
STATIC-QUALIFIED: isolated candidate; no production-root load; no Promisory runtime dependency.
UNQUALIFIED: target-build failure-state mutation timing, exact verification-state persistence, retry timing, and whether the referenced upstream generations are visible in the same evaluation pass.

## Known limitation

The current verification V0 has intentionally coarse failure semantics. A future recovery revision must add explicit source failure, threat block, target loss, command non-observation, and strategic-obsolescence classes. It must not infer those causes merely from worker disappearance.

## Vertical slice status

The civilian economic control loop now has a complete conceptual path:

DEMAND → ARBITRATION → WORKER SELECTION → SOURCE/DROPSITE QUALIFICATION → COMMAND → VERIFICATION → RECOVERY → RE-ARBITRATION.

The next engineering frontier is stronger task-state observation and source-specific recovery, followed by controlled integration into the production runtime only after ABI/dynamic qualification.