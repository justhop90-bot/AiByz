# AEGIS Documentation

This directory contains the project's **human-readable engineering record**. It explains the machine, the evidence behind the model, the architectural consequences, the research methods, and the quality controls needed to continue the work.

## Current Layer 1 position

**Layer 1 — Machine Understanding: 89% working completion position.**  
**Investigation phase: CLOSED / HANDOFF.**  
**Completion certification: NOT SATISFIED.**

The investigation deliberately stopped before claiming predictive closure. The remaining work is concentrated in implementation-level causal edges: persistent-fact mutation/freshness, scheduler state mutation, rule-to-action bridging, UnitAI order/action mutation, failure propagation, required identity lifecycle edges, and one predictive end-to-end path.

## Read in this order

### Orientation

1. [`../README.md`](../README.md) — public project overview and final Layer 1 position.
2. [`../RESEARCH_INDEX.md`](../RESEARCH_INDEX.md) — repository navigation.
3. [`LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`](LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md) — authoritative six-month recovery handoff.
4. [`PROJECT_STATUS_2026-09-02.md`](PROJECT_STATUS_2026-09-02.md) — final status and bounded frontier.
5. [`REPOSITORY_ARCHITECTURE.md`](REPOSITORY_ARCHITECTURE.md) — organization and authority model.

### Machine understanding

6. [`LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`](LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md) — completion and evidence standard.
7. [`LAYER1_COMPLETION_CONTROL_2026-09-02.md`](LAYER1_COMPLETION_CONTROL_2026-09-02.md) — governing completion gate; XS explicitly excluded.
8. [`MACHINE_EVIDENCE_MATRIX_2026-09-02.md`](MACHINE_EVIDENCE_MATRIX_2026-09-02.md) — evidence and confidence by claim.
9. [`MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`](MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md) — consolidated machine model.
10. [`MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md`](MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md) — architectural implications.
11. [`LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md`](LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md) — native investigation history.
12. [`LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md`](LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md) — QC and recovery standard.
13. [`LAYER1_NATIVE_PASS_2026-09-03_AIEXPERT_UNITAI_ARCHITECTURE.md`](LAYER1_NATIVE_PASS_2026-09-03_AIEXPERT_UNITAI_ARCHITECTURE.md) — AIExpert/UnitAI architecture evidence.
14. [`LAYER1_NATIVE_PASS_2026-09-03_PERSISTENT_FACT_AND_GAMESTATE_QC.md`](LAYER1_NATIVE_PASS_2026-09-03_PERSISTENT_FACT_AND_GAMESTATE_QC.md) — fact/game-state boundary.
15. [`LAYER1_NATIVE_PASS_2026-09-03_PDATA_AND_METADATA_DISPATCH_QC.md`](LAYER1_NATIVE_PASS_2026-09-03_PDATA_AND_METADATA_DISPATCH_QC.md) — `.pdata` function geometry and metadata validation.
16. [`LAYER1_NATIVE_PASS_2026-09-03_PDATA_PDB_RIP_QC.md`](LAYER1_NATIVE_PASS_2026-09-03_PDATA_PDB_RIP_QC.md) — `.pdata`, CodeView/PDB, and direct-reference tests.
17. [`NATIVE_OBJECT_IDENTITY_DOSSIER_2026-09-02.md`](NATIVE_OBJECT_IDENTITY_DOSSIER_2026-09-02.md) — identity topology research.
18. [`OPEN_NATIVE_QUESTIONS_LAYER1.md`](OPEN_NATIVE_QUESTIONS_LAYER1.md) — final unresolved questions and promotion tests.

### Methods and governance

- [`KNOWLEDGE_PRESERVATION_STANDARD.md`](KNOWLEDGE_PRESERVATION_STANDARD.md) — how durable knowledge is recorded.
- [`ARCHITECTURE_TRACEABILITY.md`](ARCHITECTURE_TRACEABILITY.md) — evidence-to-architecture traceability.
- [`MACHINE_RECONSTRUCTION_PROCEDURE.md`](MACHINE_RECONSTRUCTION_PROCEDURE.md) — independent reconstruction procedure.
- [`SECURITY_AND_PROVENANCE.md`](SECURITY_AND_PROVENANCE.md) — public/private evidence boundary.
- [`LAYER1_REENTRY_EXAMINATION.md`](LAYER1_REENTRY_EXAMINATION.md) — re-entry examination.

## Epistemic rule

Every important statement should be understood in terms of **what was observed, what was inferred, how strong the evidence is, what remains uncertain, and what test could distinguish competing explanations**.

A long document is not automatically a strong document. A strong document lets another engineer reproduce the reasoning.

## Relationship to `knowledge/`

`docs/` is the explanatory layer. `knowledge/` is the durable, more granular institutional-memory layer.

Use `docs/` to understand the project. Use `knowledge/` to recover exact claims, ledgers, schemas, evidence history, and machine-readable records.

## Relationship to historical archaeology

`03_HD_ARCHAEOLOGY/` contains historical research. It is deliberately separated from the current machine contract so that historical implementation patterns cannot silently become present-day specifications.

## Relationship to replay research

Replay evidence is primarily indexed under `knowledge/replay/`. It is treated as an empirical observation source and must not be confused with complete visibility into hidden native state.

## Final handoff rule

The Layer 1 investigation is closed at 89%. If work resumes, do not restart generic vocabulary collection. Start from the final handoff, inspect the evidence matrix, then attack the smallest unresolved implementation edge with `.pdata`-bounded native analysis and controlled falsification.
