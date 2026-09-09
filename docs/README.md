# AEGIS Documentation

This directory contains the project's human-readable engineering record.

## Current final-bot plan — READ THIS FIRST

**`AEGIS_MASTER_PLAN.md` is the single active planning authority for the final AEGIS/ByzBot.**

It contains the current:

- final architecture;
- 20 capability slices;
- cross-cutting control plane;
- HD/Promisory lessons relevant to design;
- historical capability-closure ledger;
- machine/ABI gate;
- implementation gate;
- first executable vertical slice;
- prototype policy;
- definition of done.

Do **not** create or follow another blueprint, addendum, reconciliation, or revised final-bot plan. When new evidence changes the design, update `AEGIS_MASTER_PLAN.md` and preserve the underlying evidence in its proper evidence/research location.

Older dated planning documents are retained only where needed for provenance/history. They do not compete with the master plan.

## Current Layer 1 position

**Layer 1 — Machine Understanding: 89% working completion position.**  
**Investigation phase: CLOSED / HANDOFF.**  
**Completion certification: NOT SATISFIED.**

The investigation deliberately stopped before claiming predictive closure. Remaining work is targeted implementation-level causal evidence only where required by runtime qualification.

## Read in this order

1. `../README.md` — public project overview and current status.
2. `../RESEARCH_INDEX.md` — repository navigation.
3. `AEGIS_MASTER_PLAN.md` — **single current final-bot plan**.
4. `CANONICAL_PROJECT_HANDOFF_2026-09-05.md` — governance/handoff context.
5. `CANONICAL_QC_2026-09-05.md` — QC authority.
6. `REPOSITORY_AUTHORITY_MAP_2026-09-05.md` — authority boundaries.
7. `REPOSITORY_OPERATING_STANDARD_2026-09-05.md` — operating rules.
8. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md` — machine qualification procedure.
9. `03_HD_ARCHAEOLOGY/` — historical source evidence.
10. `docs/MACHINE_EVIDENCE/` — current machine evidence.

## Evidence strata

- `03_HD_ARCHAEOLOGY/` — historical HD/Promisory evidence.
- `04_LAYER3_ARCHITECTURE/` — architecture and ABI qualification evidence/procedures.
- `docs/MACHINE_EVIDENCE/` — target-build machine/package evidence.
- `docs/forensics/` — detailed forensic evidence.
- `05_RUNTIME_CANDIDATE/` — replay/runtime research instruments.
- `12_RESEARCH/` — external/comparative research.
- `knowledge/` — durable atomic institutional memory.

These strata contain evidence and procedures, not competing final-bot plans.

## Epistemic rule

Every important statement should be understood in terms of what was observed, what was inferred, how strong the evidence is, what remains uncertain, and what test could distinguish competing explanations.

A long document is not automatically a strong document. A strong document lets another engineer reproduce the reasoning.

## Relationship to `knowledge/`

`docs/` is the explanatory/governance layer. `knowledge/` is the durable, granular institutional-memory layer.

Use the master plan for **what we are building and what happens next**. Use evidence/knowledge records when exact historical or machine claims must be recovered.

## Final operating rule

**One plan. Many evidence records.**

The master plan changes when the project's current design or next action changes. Evidence records change only when the underlying evidence itself is updated, corrected, or superseded.
