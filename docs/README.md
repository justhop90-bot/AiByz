# AEGIS Documentation

This directory contains the project's **human-readable engineering record**. It explains the machine, the evidence behind the model, the architectural consequences, the research methods, and the quality controls needed to continue the work.

## Current priority

**Layer 1 — Machine Understanding** is the active frontier.

The project is deliberately aiming beyond vocabulary-level familiarity. The completion standard is predictive: for a sufficiently specified state and input, a future engineer should be able to trace the relevant machine path and explain what the system will do next, including uncertainty and failure paths.

## Read in this order

### Orientation

1. [`../README.md`](../README.md) — public project overview.
2. [`../RESEARCH_INDEX.md`](../RESEARCH_INDEX.md) — repository navigation.
3. [`PROJECT_STATUS_2026-09-02.md`](PROJECT_STATUS_2026-09-02.md) — current state and next actions.
4. [`REPOSITORY_ARCHITECTURE.md`](REPOSITORY_ARCHITECTURE.md) — organization and authority model.

### Machine understanding

5. [`LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`](LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md) — the completion and evidence standard.
6. [`MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`](MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md) — consolidated machine model.
7. [`MACHINE_EVIDENCE_MATRIX_2026-09-02.md`](MACHINE_EVIDENCE_MATRIX_2026-09-02.md) — evidence and confidence by claim.
8. [`MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md`](MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md) — architectural implications.
9. [`LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md`](LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md) — native investigation history.
10. [`LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md`](LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md) — QC and six-month recovery standard.
11. [`NATIVE_OBJECT_IDENTITY_DOSSIER_2026-09-02.md`](NATIVE_OBJECT_IDENTITY_DOSSIER_2026-09-02.md) — identity topology research.
12. [`OPEN_NATIVE_QUESTIONS_LAYER1.md`](OPEN_NATIVE_QUESTIONS_LAYER1.md) — unresolved questions and next investigations.

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
