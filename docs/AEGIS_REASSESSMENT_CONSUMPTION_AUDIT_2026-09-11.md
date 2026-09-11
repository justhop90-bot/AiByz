# AEGIS REASSESSMENT downstream-consumption audit — 2026-09-11

## Finding

The existing seven REASSESS publishers correctly create local, generation-keyed publication tokens, but the source audit does **not** support claiming complete downstream consumption yet. The current architecture contains several places where the upstream generation owner is not demonstrably advanced by the REASSESS token itself.

This is intentional: the reassessment boundary must not manufacture work.

## Required invariant

For every vertical:

`terminal lifecycle generation -> REASSESS publication -> one acknowledgement -> newer upstream generation -> new request`

The forbidden shortcut is:

`terminal lifecycle generation -> REASSESS -> same-generation request`

That shortcut would permit stale outcomes and duplicate physical requests.

## Current audit disposition

| Vertical | Publisher present | Downstream generation source identified | Promotion status |
|---|---:|---:|---|
| worker_economy | YES | worker-role-vector generation | BLOCKED pending exact consumer wiring audit |
| villager_production | YES | civilization-state generation | BLOCKED pending exact consumer wiring audit |
| housing | YES | civilization-state generation | BLOCKED pending exact consumer wiring audit |
| age_transition | YES | current-age/world observation | BLOCKED pending exact consumer wiring audit |
| anti_cavalry | YES | scouting/threat generation | BLOCKED pending exact consumer wiring audit |
| tactical_micro | YES | world/threat observation generation | BLOCKED pending exact consumer wiring audit |
| military_production | YES | selector/requirement generation | CANDIDATE_BLOCKED; selector initialization remains unresolved |

## Critical distinction

A local publisher such as the villager reconciler records its lifecycle generation and sets `reassess-valid`. That is a correct publication boundary. It does not prove that the civilian demand owner has consumed that event, advanced its own input generation, and created exactly one new request. The source currently shows the reconciler publishing the token; the downstream consumption path must therefore be proven independently.

The same rule applies to housing, age, anti-cavalry, tactical micro, worker economy, and military production.

## Why no automatic same-generation reset was added

A tempting implementation would clear the reassessment bit and immediately increment the lifecycle generation. That is rejected. It would create a synthetic generation with no new observation, allow a terminal outcome to trigger a duplicate request, and blur causal ownership.

The correct owner of a new generation is the owner of the upstream observation/demand state, not the terminal verifier.

## No monolithic controller

The audit explicitly rejects a global reassessment service. Each vertical must consume its own publication through its existing upstream owner. Cross-vertical orchestration belongs to the strategic/control plane only if independently qualified; it cannot be smuggled into the reassessment boundary.

## Tests added

`tests/vertical_slices/test_reassessment_consumption_contract.py` checks:

- all seven registered publishers expose generation-keyed reassessment state;
- publication is guarded by generation inequality;
- reassessment cannot select strategy;
- military production remains candidate-blocked;
- no global reassessment controller source file exists.

These are static architecture tests. They do not constitute target-build runtime qualification.

## Final audit conclusion

**REASSESS publication: implemented.**

**REASSESS downstream consumption: contract established, but not promoted to qualified until each of the seven consumers is proven to acknowledge the event and require a genuinely newer upstream generation.**

This conservative boundary is deliberate. It prevents a superficially complete loop from becoming an architecture that silently manufactures generations or repeats stale physical actions.
