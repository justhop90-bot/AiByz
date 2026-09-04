# AoE2DE Observation Semantics Archaeology — QC Pass 1
Date: 2026-09-04
Status: ACCEPT WITH CORRECTIONS — WORKING CANON

## QC objective
Audit Pass 18 for source fidelity, semantic overreach, lifecycle claims, and separation between historical mechanism and AEGIS generalization.

## Checks
1. Verified source is the supplied Promisory archive.
2. Object-data field inventory was derived from exact source occurrences.
3. Numeric field definitions were checked against source constants.
4. `object-data-progress-value` is directly used in production/building/research control.
5. `object-data-researching` is directly used to distinguish active research/building candidates.
6. `object-data-id` is directly read into goals in multiple modules.
7. Search discovery/filtering/selection/extraction chains are directly observable.
8. Scout centroid construction is directly traceable through repeated object selection and coordinate accumulation.
9. Scout threat aggregation is directly traceable through weighted counts.
10. The claim that object-data is an active observation interface is DIRECT/COMPOSED, not speculative.
11. The claim that search state acts as an intermediate computational workspace is COMPOSED.
12. The claim that the programmer possessed a unified entity-component architecture remains INFERRED/PROBABLE and is explicitly labeled accordingly.
13. The source supports lifecycle-aware filtering; it does not prove a modern explicit enum/state-machine abstraction.
14. The source supports identity continuity for selected subsystems; it does not prove universal identity persistence across all systems.
15. The source provides richer object-level observation primitives than normalized replay ACTION payloads tested in Passes 15–17.
16. This does not establish that those fields can be reconstructed from `.aoe2record` by mgz-fast.
17. Replay W2 production lineage therefore remains OPEN.
18. Scenario-loader is not reintroduced.
19. AEGIS inheritance/rejection items are design recommendations, not historical claims.
20. Pass 19 should investigate lower-level parser/runtime structures before any replay W2 promotion.

## Important correction gate
Do not state that `object-data-progress-value` universally means "construction progress". Its historical uses span production/building/research-related control. The safe statement is that it is a numeric object progress field used by the program in lifecycle/availability decisions.

Do not state that `status-pending = 0`, `status-ready = 2`, and `status-resource = 3` are complete universal engine status semantics without qualification. They are source-defined constants used by the program.

## Verdict
**ACCEPT WITH CORRECTIONS.**
Pass 18 substantially improves the strategic-code model and identifies a stronger runtime research target, but parser-level W2 closure remains unresolved.
