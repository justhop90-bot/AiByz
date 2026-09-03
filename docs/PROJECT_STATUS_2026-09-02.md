# AEGIS Project Status — 2026-09-02

## Executive status

**Current layer: Layer 1 — Machine Understanding**  
**State: active, not declared complete**

The project has accumulated a substantial operational and research record, but the completion standard is deliberately stricter than familiarity with AI scripting vocabulary. The remaining work is to turn important machine-facing observations into causal, implementation-level, and experimentally predictive understanding.

## Project objective

Build a high-quality Byzantine AI for AoE2DE by establishing the machine contract first, reconstructing general strategic intelligence second, specializing that intelligence for the Byzantine civilization third, and implementing the validated architecture last.

## What has been established

### Repository and knowledge system

- A public research repository structure separates documentation, durable knowledge, historical archaeology, and supporting research.
- The public tree no longer contains the former ADPromisory, AiBuilder, or ByzantineWarCouncil source/runtime material.
- Provenance and cleanup decisions are recorded separately from active architecture.
- A six-month recovery standard is part of the repository's quality criteria.

### Layer 1 methodology

- A predictive machine-understanding standard has been established.
- An explicit evidence ladder separates direct evidence, reproduction, corroboration, inference, and hypothesis.
- Negative results are retained rather than silently discarded.
- Critical paths are modeled as causal spines rather than collections of isolated facts.
- Programmer-intent reconstruction is treated as a separate evidentiary task from determining runtime behavior.

### Native investigation

The investigation has established a useful native evidence surface around script-facing engine APIs and AI-related symbols. The exact AoE2DE executable and controlled Ghidra environment are recorded in the native archaeology documents.

High-value script-facing identity interfaces identified in native signature data include object/copy ID, class/type, validity/availability, and garrison-related functions. Native debug/source strings also expose concepts such as `obj->id`, `uniqueID`, and AI module names.

A full executable `.text` instruction scan was used as a discriminating negative test. No direct RIP-relative references were recovered to the tested API signature addresses, the widened signature region, or the selected UnitAI diagnostic strings. This establishes a representation constraint for the tested addressing mode; it does **not** prove that the metadata or diagnostics are unused, nor does it prove that the actual consumer is indirect. Competing representations must be tested rather than assumed.

### UnitAI control-loop model

Native vocabulary supports a strong architectural hypothesis that UnitAI separates at least order state, action state, target state, and notification state, with search/recovery machinery associated with invalid or otherwise unsatisfied execution conditions.

The distinction between `currentOrder` and `CurrentAction`, together with `OrderQueue`, `NotifyQueue`, `processNotify`, `processIdle`, search diagnostics, and explicit failed/invalidated/search-required action diagnostics, is a high-value model for subsequent implementation tracing. Exact ownership, persistence, sequencing, and causal ordering remain unproven.

### QC correction to the UnitAI model

The UnitAI model is now treated explicitly as **constraint-driven architectural inference**, not recovered programmer intent. A target can become unusable independently of original AI intent; separating persistent requested work from transient execution and providing recovery is a plausible design response. The implementation must still prove whether the native controller actually follows that architecture.

The most valuable next evidence is a concrete mutation chain:

`native function → state read → condition/branch → state write → subsequent consumer`

A complete `Update` reconstruction is not required before this smaller chain can be established.

### Replay research

Replay parsing has been calibrated against multiple recordings. The research distinguishes replay observations from native machine truth and preserves uncertainty around action schemas, sequence coordinates, object references, object lifecycle, and production completion.

## Current Layer 1 completion gap

The project is not yet claiming that every material machine path is predictive.

The most important remaining gap is **native implementation closure**. Two tightly related problems dominate:

1. **Metadata-consumer closure:** recover the native structure and dispatch mechanism that consumes the embedded API name/signature region and turns an API identifier into a callable handler.
2. **State-owner closure:** recover a concrete UnitAI state mutation chain showing where order/action/target/notification state is stored, read, invalidated, and rewritten.

For object identity, the eventual causal chain must still resolve:

`registration/dispatch → validation → lookup → native state access → return value`

and the relationships among unit IDs, object IDs, copy IDs, native object identity, ownership, type/class, lifecycle, transformation, garrison, creation, and removal.

## Immediate work sequence

1. Recover indirect/indexed consumers of the embedded engine-facing signature region. Do not repeat broad direct-string xref scans unless a new representation hypothesis requires them.
2. Enumerate competing metadata representations before selecting a dispatch hypothesis.
3. Identify the initialization/registration structure that owns or transforms the API metadata.
4. Trace `xsGetUnitObjectId` end-to-end as the first representative identity path once its consumer/dispatch chain is located.
5. In parallel, identify a concrete UnitAI state-owner candidate and recover one real read → condition → write → consumer chain.
6. Test whether `CurrentAction` and `currentOrder` have distinct ownership/lifetime using native mutation evidence rather than vocabulary alone.
7. Trace related copy-ID, type/class, validity/availability, and garrison interfaces.
8. Design discriminating runtime experiments for target invalidation, action recovery, identity conversion, and lifecycle behavior.
9. Update the evidence matrix, atomic machine facts, predictive tests, and QC amendments from demonstrated results.
10. Reassess Layer 1 completion only after the predictive gate is satisfied.

## Downstream layers

Layer 2 strategic research already exists in the repository, including general AoE2 ontology, strategic axioms, decision-event schema, cross-validation, and operationalization material. It is preserved but should not be allowed to hide or bypass unresolved Layer 1 assumptions.

Layer 3 Byzantine doctrine and Layer 4 implementation remain downstream of the validated machine contract.

## Quality-control position

The project currently passes the **documentation/re-entry** requirement more strongly than the **predictive machine completion** requirement. That distinction is intentional.

A repository can be excellent institutional memory while still documenting an unfinished investigation. Status must say so plainly.

## Six-month re-entry instructions

A returning engineer should:

1. read `../RESEARCH_INDEX.md`;
2. read this status file;
3. read `LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`;
4. read `MACHINE_EVIDENCE_MATRIX_2026-09-02.md`;
5. read `MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`;
6. read the native archaeology log and QC addendum;
7. read `LAYER1_NATIVE_PASS_2026-09-02_UNITAI_CONTROL_LOOP_DEEPENING.md`;
8. read `LAYER1_QC_AMENDMENT_2026-09-02_UNITAI_AND_METADATA.md`;
9. read `OPEN_NATIVE_QUESTIONS_LAYER1.md`;
10. inspect the atomic machine ledgers;
11. continue from the immediate work sequence above.

## Status rule

Do not promote this document to "Layer 1 complete" merely because the investigation becomes large or the documentation becomes polished. Completion is an evidence decision governed by the predictive standard.
