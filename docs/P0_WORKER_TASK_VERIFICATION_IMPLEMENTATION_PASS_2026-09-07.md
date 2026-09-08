# P0 Worker Task Verification — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate implemented and archived; NOT runtime-qualified; NOT loaded by production root.

## Objective

Strengthen post-command observation so AEGIS does not equate command issuance with successful task attachment. V0 observes worker and target presence after the task-command generation.

## Contract

COMMAND_ISSUED → OBSERVING → TASK_OBSERVED or FAILURE.

The candidate records generation, resource, worker visibility, task visibility, target visibility, result, failure, observation time, and cycle. It issues no commands.

## Evidence basis

Stock worker logic uses object-data action, order, target, carry, and search-state operations to distinguish worker states. The AEGIS observer therefore uses those same observable dimensions rather than treating an action-default command as self-authenticating.

## Important limitation

V0 does NOT prove that the worker is actually gathering, nor that resource income is positive. Target visibility is only evidence that a task relationship exists in the observable object state. Action/order semantics, target identity, cargo progression, source status, and net resource change still require target-build runtime qualification.

## Failure classes

V0 distinguishes worker missing from target not observed. A broader task-not-observed class is retained as an ABI/behavioral boundary but is not asserted from ambiguous aggregate observations. Future recovery must distinguish target loss, source exhaustion, threat block, command rejection, worker death, stale state, and strategic cancellation.

## Qualification states

OBSERVED: stock object-state fields and search/filter idioms.
CORRELATED: worker + target visibility is stronger evidence than command issuance alone.
IMPLEMENTED: generation-fenced verification adapter.
STATIC-QUALIFIED: candidate-only, structurally isolated, no production-root load.
UNQUALIFIED: exact target-build mutation timing, action/order meaning in this observation context, target attribution, source attribution, cargo progression, income confirmation, and same-pass visibility.

## Next engineering target

Build bounded worker recovery/reassignment. Recovery must consume verification failure classes without conflating source failure with worker failure, and must return failed demand to arbitration rather than directly issuing an uncontrolled replacement command.