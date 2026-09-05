# AEGIS — Wave A Next Experiment Queue

**Date:** 2026-09-05  
**Status:** ACTIVE

## Priority 0 — Representation safety

1. Scalar goal write/read smoke test in the reserved namespace.
2. Scalar goal compare smoke test using the same value.
3. Strategic-number read/write smoke test.
4. Representative typed fact test using a concrete unit ID.
5. Representative typed fact test using a unit-line ID.
6. Validator/runtime result comparison.

## Priority 1 — Semantic state safety

7. Two-generation publication test.
8. Stale-generation rejection test.
9. Confirmed-zero test.
10. Search-no-result test.
11. Unsupported-query test.
12. Intentionally-unobserved test.
13. Search filter isolation test.
14. Publication interruption/coherence test.

## Priority 2 — Operational lifecycle

15. `can-*` versus command issuance.
16. issuance versus queue acceptance.
17. pending versus created.
18. created versus available.
19. cancellation versus stale reissue.
20. supersession versus old-generation execution.

## Priority 3 — Performance

21. Measure representative fact-query latency.
22. Measure representative search latency.
23. Measure repeated query cost.
24. Establish bounded execution cadence.
25. Establish minimum viable vertical-slice budget.

## Stop conditions

Stop and review architecture if any experiment demonstrates that a load-bearing subsystem contract cannot be represented without violating its ownership boundary.

Otherwise correct the ABI/implementation design and continue.
