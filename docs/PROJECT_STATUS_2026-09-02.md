# AEGIS Project Status — 2026-09-02

## Executive status

**Current layer: Layer 1 — Machine Understanding**  
**State: active, not declared complete**

The project has accumulated a substantial operational and research record, but the current completion standard is deliberately stricter than simple familiarity with the AI scripting vocabulary. The remaining work is to turn important machine-facing observations into causal, implementation-level, and experimentally predictive understanding.

## Project objective

Build a high-quality Byzantine AI for AoE2DE by establishing the machine contract first, reconstructing general strategic intelligence second, specializing that intelligence for the Byzantine civilization third, and implementing the validated architecture last.

## What has been established

### Repository and knowledge system

- A public research repository structure now separates documentation, durable knowledge, historical archaeology, and supporting research.
- The public tree no longer contains the former ADPromisory, AiBuilder, or ByzantineWarCouncil source/runtime material.
- Provenance and cleanup decisions are recorded separately from active architecture.
- A six-month recovery standard is now part of the repository's quality criteria.

### Layer 1 methodology

- A predictive machine-understanding standard has been established.
- An explicit evidence ladder separates direct evidence, reproduction, corroboration, inference, and hypothesis.
- Negative results are retained rather than silently discarded.
- Critical paths are modeled as causal spines rather than collections of isolated facts.
- Programmer-intent reconstruction is treated as a separate evidentiary task from determining runtime behavior.

### Native investigation

The investigation has established a useful native evidence surface around script-facing engine APIs and AI-related symbols. The exact AoE2DE executable and controlled Ghidra environment are recorded in the native archaeology documents.

High-value script-facing identity interfaces identified in native signature data include object/copy ID, class/type, validity/availability, and garrison-related functions. Native debug/source strings also expose concepts such as `obj->id`, `uniqueID`, and AI module names.

These findings establish the **research surface**, not the full semantics of the APIs. The important unresolved question is how those interfaces map to native object state and lifecycle.

### Replay research

Replay parsing has been calibrated against multiple recordings. The research distinguishes replay observations from native machine truth and preserves uncertainty around action schemas, sequence coordinates, object references, object lifecycle, and production completion.

## Current Layer 1 completion gap

The project is not yet claiming that every material machine path is predictive.

The most important remaining gap is **instruction-level and end-to-end native tracing**. In particular, the project needs to recover consumers of embedded script-facing API signatures and trace representative functions through:

`registration/dispatch → validation → lookup → native state access → return value`

For object identity, this must eventually resolve the relationships among unit IDs, object IDs, copy IDs, native object identity, ownership, type/class, lifecycle, transformation, garrison, creation, and removal.

## Immediate work sequence

1. Recover instruction-level references to the embedded engine-facing signature region, with x86-64 RIP-relative and indirect-reference handling.
2. Identify candidate consumer functions for high-value identity APIs.
3. Trace `xsGetUnitObjectId` end-to-end as the first representative identity path.
4. Trace related copy-ID, type/class, validity/availability, and garrison interfaces.
5. Build an implementation-backed identity topology.
6. Design discriminating runtime experiments that connect native identity to script-visible and replay-visible observations.
7. Update the evidence matrix and predictive tests.
8. Reassess Layer 1 completion only after the predictive gate is satisfied.

## Downstream layers

Layer 2 strategic research already exists in the repository, including general AoE2 ontology, strategic axioms, decision-event schema, cross-validation, and operationalization material. It is preserved but should not be allowed to hide or bypass unresolved Layer 1 assumptions.

Layer 3 Byzantine doctrine and Layer 4 implementation remain downstream of the validated machine contract.

## Quality-control position

The project currently passes the **documentation/re-entry** requirement more strongly than the **predictive machine completion** requirement. That distinction is intentional.

A repository can be excellent institutional memory while still documenting an unfinished investigation. The status should say so plainly.

## Six-month re-entry instructions

A returning engineer should:

1. read `../RESEARCH_INDEX.md`;
2. read this status file;
3. read `LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`;
4. read `MACHINE_EVIDENCE_MATRIX_2026-09-02.md`;
5. read `MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`;
6. read the native archaeology log and QC addendum;
7. read `OPEN_NATIVE_QUESTIONS_LAYER1.md`;
8. inspect the atomic machine ledgers;
9. continue from the immediate work sequence above.

## Status rule

Do not promote this document to "Layer 1 complete" merely because the investigation becomes large or the documentation becomes polished. Completion is an evidence decision governed by the predictive standard.
