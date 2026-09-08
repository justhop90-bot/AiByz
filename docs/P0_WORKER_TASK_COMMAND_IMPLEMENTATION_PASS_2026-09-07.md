# P0 Worker Task Command — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate implemented and statically reviewed; NOT runtime-qualified; NOT loaded by production root.

## Objective

Cross the boundary from qualified worker/source state into one bounded physical resource-task command. The adapter supports wood, gold, and stone in V0. Food remains deferred to a dedicated food-portfolio adapter.

## Stock contract recovered

The stock gatherer corpus demonstrates the local-worker/remote-resource pattern: establish a local worker search, establish a remote resource search, set the target object for each search, then issue `up-target-objects 0 action-default -1 -1`. This is materially stronger evidence than inventing a new task primitive.

## Implemented lifecycle

ARBITRATED DEMAND → WORKER SELECTION → SOURCE/SERVICE QUALIFICATION → COMMAND AUTHORIZATION → LOCAL/REMOTE SEARCH → TARGET OBJECT BINDING → `up-target-objects` → ISSUED.

Only one worker command is admitted per arbitrated generation. Attempt count is fenced at one. Command issuance is explicitly not treated as productivity or confirmation.

## Protection boundary

The command adapter excludes loaded workers, attack-action workers, builders, repair-order workers, and enter-order workers from the local candidate search. This is a conservative V0 protection set derived from observed stock filtering. It is not claimed to be the complete stock protected-worker contract.

## Critical predecessor corrections discovered during this pass

1. The original worker-target-selection candidate allocated goals 490–498, colliding with the already-established economic-demand-arbitration goals 490–497. It also referenced non-existent arbitration field names and selected workers already classified into the destination role. This was corrected to goal range 510–518, correct arbitration fields, and `villager-class` candidate selection so controlled retasking remains possible.
2. The original source/dropsite candidate marked gold and stone serviceable without requiring a positive source count and bound the requested resource through an incorrect arbitration field. This was corrected before command execution work proceeded. Wood now receives a positive-source gate as well.
3. The task command adapter therefore consumes the corrected predecessors, not the superseded versions.

## Evidence state

OBSERVED: stock `up-target-objects` command pattern and local/remote search topology.
CORRELATED: this topology is the appropriate AEGIS physical task boundary.
IMPLEMENTED: bounded resource command adapter for wood/gold/stone.
STATIC-QUALIFIED: balanced candidate, isolated goals 519–525, no production-root load, no Promisory runtime dependency.
UNQUALIFIED: exact target-build command side effects, search mutation visibility, target-object binding semantics under the candidate's rule scheduling, and whether `action-default` yields the expected gathering behavior in every supported resource context.

## Explicit non-claims

`COMMAND_ISSUED` does not mean `WORKER_PRODUCTIVE`.
A selected worker does not prove the source is reachable after command issuance.
A source search result does not prove successful delivery to a dropsite.
No completion or productivity state is inferred here.

## Next engineering target

Build the post-command worker productivity observer/reconciler. It must determine whether the issued worker actually entered a productive gather state, distinguish command-not-observed from source/task failure, and hand bounded failures to recovery without assuming that command issuance succeeded.