# AEGIS / AiByz — Canonical Authority

**Effective:** 2026-09-05

GitHub is the authoritative project record for AEGIS / AiByz.

## Canonical state

- Canonical handoff branch: `aegis/canonical-handoff-2026-09-05`
- Canonical source baseline: `d492ba1c776e2408f97fae0684402519b7635861`
- Canonical handoff: `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
- Canonical QC: `docs/CANONICAL_QC_2026-09-05.md`
- Latest architecture specification: `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`

## Authority rules

1. Prefer the newest committed evidence-backed artifact when documents conflict.
2. Preserve superseded artifacts; do not erase research history to hide contradictions.
3. Machine facts require machine evidence at the appropriate authority class.
4. Numeric ABI allocation requires A1/A2/A3 evidence; A4/A5 can never clear it.
5. No `.per` implementation is authorized merely because an identifier appears unused.
6. Engine semantics, validator acceptance, and AEGIS design status are independent dimensions.
7. XS is outside project scope.
8. Scenario-loader automation is retired.
9. CADE is secondary validation infrastructure, not project authority.
10. Every durable research/engineering result must be committed and independently verifiable in GitHub.

## Current gate

`BUILD/PACKAGE ACQUISITION → ABI INVENTORY → COLLISION AUDIT → NUMERIC ABI FREEZE → .per IMPLEMENTATION`

The numeric ABI is currently **BLOCKED**. This is an intentional safety gate, not an unfinished design accident.
