# P0 Worker Target Selection — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate implemented and statically reviewed; NOT runtime-qualified; NOT loaded by production root.

## Objective

Translate one arbitrated economic demand into a bounded candidate-worker search without issuing a resource task command. The module deliberately stops before source selection, dropsite qualification, task command, and productivity verification.

## Evidence basis

The stock gatherer corpus demonstrates local worker searches followed by explicit filters over object-data action, order, target, carry, distance, and task load. Stock also uses semantic worker classifications such as villager-wood, villager-gold, and villager-stone. This implementation preserves that separation: worker-role classification identifies the candidate population; object-state filters remove obviously unsuitable workers.

## Implemented contract

ARBITRATED DEMAND → SELECTION FRAME → ROLE-CLASSIFIED WORKER SEARCH → PROTECTION/STATE FILTERS → DISTANCE ORDER → CANDIDATE COUNT.

The selection layer records the arbitrated resource, requested worker count, candidate count, generation, observation timestamp, and cycle. It does not mutate economic demand and does not issue action-default/action-gather/action-build commands.

## Protection boundary

V0 excludes workers carrying resources and workers whose current order is build. This is intentionally conservative. It does not yet claim a universal protected-worker policy, nor does it classify all attack, repair, enter, hunt, gather, or construction states. Those states require the dedicated worker-state/recovery pass.

## Resource boundary

Food/wood/gold/stone candidate populations are selected from the engine's semantic worker-role classifications. A source is not selected here. In particular, a wood worker is not automatically assigned to a tree, and a gold worker is not automatically assigned to a mining camp or gold object.

## Qualification state

OBSERVED: stock worker-role classifications and stock search/filter idioms.
CORRELATED: role-classified local searches are appropriate candidate populations for downstream task selection.
IMPLEMENTED: AEGIS candidate-worker search for the four economic resource roles.
STATIC-QUALIFIED: balanced candidate file, isolated goal range, no production-root load, no Promisory dependency.
UNQUALIFIED: exact target-build runtime semantics of the candidate search, filter mutation visibility, same-pass state visibility, and whether the resulting local-total is the desired attribution boundary.

## Known limitations

1. V0 uses the arbitrated demand as a worker-count request; it does not account for workers already productive in the requested role.
2. It does not yet perform protected-worker exclusion equivalent to the full stock gatherer corpus.
3. It does not select source/dropsite relationships.
4. It does not issue a task command.
5. It does not prove productivity.
6. It does not resolve aggregate worker attribution under concurrent controllers.

## Next engineering target

Recover and implement source/dropsite serviceability before task issuance. The required pipeline is:

CANDIDATE WORKER → SOURCE CANDIDATES → OBJECT STATUS → TASK LOAD → SERVICE DISTANCE → DROPSITE → THREAT/ELIGIBILITY → RANK → TASK COMMAND.

No command should be issued until those qualification boundaries are explicit.