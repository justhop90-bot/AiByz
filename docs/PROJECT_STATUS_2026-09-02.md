# AEGIS Project Status — 2026-09-02

## Executive status

**Current layer: Layer 1 — Machine Understanding**  
**State: active, not declared complete**  
**Working completion estimate: 88%**

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

### Section-aware address mapping — newly promoted

The native PE section table has now been read directly. The relevant mapping is:

- `.text`: RVA `0x1000`, raw pointer `0x400`;
- `.rodata`: RVA `0x313b000`, raw pointer `0x313a400`;
- `.rdata`: RVA `0x313c000`, raw pointer `0x313ac00`.

Therefore the relevant `.rdata` raw/virtual mapping contains a `0x1400` delta. Raw offsets must be converted through the section containing the byte rather than by adding the image base directly.

This resolves the previously dangerous raw-offset/VA ambiguity and is now a mandatory condition for all subsequent native scans.

### XS metadata-addressing pass — newly promoted at observation level

The dense XS API name/signature corpus includes identity, type/class, validity/availability, garrison, map-seed, and technology-attribute interfaces. Around the inspected `xsGetMapSeed` / `xsGetTechAttribute` tail, the raw corpus has the form:

`name → signature → binary fields → source-path/debug data`

The binary fields immediately preceding the source-path string include an all-zero 8-byte field, an 8-byte value in image data/readonly-data address space, and an 8-byte value in the `.text` address range.

The `.text`-range value is `0x1417ff3e0`. This is **not** yet promoted as a function pointer or XS handler. The bytes at that address currently decode to `ret 0xcd04`, so the field requires independent consumer/call-target corroboration.

The important methodological result is that the API registry cannot safely be investigated as a simple string-to-direct-RIP-xref problem. Indirect/indexed metadata and initialization consumers are now the primary search path.

### AIExpert / rule-engine architecture evidence

The latest native pass materially deepened the rule-engine model. Retained native vocabulary identifies `AIExpertEngine.cpp`, `loadRules`, `Defining Fact`, `Defining Action`, `ruleElementsPtr`, indexed rule elements, rule debug information, `Next Rule`, breakpoint/debugging concepts, and an explicit `Evaluating Persistent Facts` phase.

The same native corpus exposes parser and loader failures for malformed directives, missing identifiers, invalid identifiers, missing rule sides, list capacity, rule length, string-table capacity, and missing files. This supports a native rule-loading/semantic-construction subsystem rather than a purely opaque callback list, while leaving exact ownership and dispatch unproven.

The native fact vocabulary is also extensive: resource, population, building, unit, research, feasibility, player-scope, game-mode, timer, search, and strategic-number concepts are represented at the same AIExpert boundary. This establishes a broad native semantic surface for rule evaluation.

### UnitAI control-loop model

Native vocabulary supports a strong architectural hypothesis that UnitAI separates at least order state, action state, target state, and notification state, with search/recovery machinery associated with invalid or otherwise unsatisfied execution conditions.

The distinction between `currentOrder` and `CurrentAction`, together with `OrderQueue`, `NotifyQueue`, `processNotify`, `processIdle`, search diagnostics, and explicit failed/invalidated/search-required action diagnostics, is a high-value model for subsequent implementation tracing. Exact ownership, persistence, sequencing, and causal ordering remain unproven.

The latest pass strengthens the sequencing model: an update exposes current order/action/target state, processes notifications, may break notification processing on stop/new-action results, proceeds into miscellaneous processing and timer/patrol logic, and can enter search/recovery or retargeting before leaving the update. This remains native-vocabulary behavioral inference until the actual native call graph is recovered.

### QC correction to the UnitAI model

The UnitAI model is now treated explicitly as **constraint-driven architectural inference**, not recovered programmer intent. A target can become unusable independently of original AI intent; separating persistent requested work from transient execution and providing recovery is a plausible design response. The implementation must still prove whether the native controller actually follows that architecture.

The most valuable next evidence is a concrete mutation chain:

`native function → state read → condition/branch → state write → subsequent consumer`

A complete `Update` reconstruction is not required before this smaller chain can be established.

### Search subsystem

Native source-path vocabulary identifies `ai\Searching\aisearch.cpp`. Search diagnostics expose LOS, search radius, cared-about object types, defend-target restrictions, candidate ownership/classification, current-target retention, pathability, attack range, wall handling, quick-path behavior, and fallback results.

This supports a strong behavioral model in which target selection is a constrained candidate-evaluation subsystem rather than a simple nearest-object query. Exact scoring implementation remains open.

### Replay research

Replay parsing has been calibrated against multiple recordings. The research distinguishes replay observations from native machine truth and preserves uncertainty around action schemas, sequence coordinates, object references, object lifecycle, and production completion.

## Current Layer 1 completion gap

The project is not yet claiming that every material machine path is predictive.

The most important remaining gap is **native implementation closure**. Two tightly related problems dominate:

1. **Metadata-consumer closure:** recover the native structure and dispatch mechanism that consumes the embedded API name/signature region and turns an API identifier into a callable handler.
2. **State-owner closure:** recover a concrete UnitAI state mutation chain showing where order/action/target/notification state is stored, read, invalidated, and rewritten.

The AIExpert rule-engine bridge is now better constrained: rule loading, fact/action definition, rule-element storage, persistent-fact evaluation, and native semantic query vocabulary are established at the vocabulary level. The remaining bridge is to recover the actual function boundaries and connect rule evaluation to action/order issuance.

For object identity, the eventual causal chain must still resolve:

`registration/dispatch → validation → lookup → native state access → return value`

and the relationships among unit IDs, object IDs, copy IDs, native object identity, ownership, type/class, lifecycle, transformation, garrison, creation, and removal.

## Immediate work sequence

1. Use section-aware virtual-address mapping for every native artifact and discard any result produced by `imagebase + raw_offset` in `.rdata`.
2. Recover the first real consumer of the XS metadata region using indirect/indexed representation searches.
3. Recover the first defensible UnitAI mutation chain for `CurrentAction` or `CurrentOrder`.
4. Recover the first defensible `AIExpertEngine` function boundary around rule loading/evaluation.
5. Recover the actual search function boundary associated with `ai::search` / `aisearch.cpp` vocabulary.
6. Identify the initialization/registration structure that owns or transforms the API metadata.
7. Trace `xsGetUnitObjectId` end-to-end as the first representative identity path once its consumer/dispatch chain is located.
8. Test whether `CurrentAction` and `currentOrder` have distinct ownership/lifetime using native mutation evidence rather than vocabulary alone.
9. Trace related copy-ID, type/class, validity/availability, and garrison interfaces.
10. Design discriminating runtime experiments for target invalidation, action recovery, identity conversion, and lifecycle behavior.
11. Update the evidence matrix, atomic machine facts, predictive tests, and QC amendments from demonstrated results.
12. Reassess Layer 1 completion only after the predictive gate is satisfied.

## Downstream layers

Layer 2 strategic research already exists in the repository, including general AoE2 ontology, strategic axioms, decision-event schema, cross-validation, and operationalization material. It is preserved but should not be allowed to hide or bypass unresolved Layer 1 assumptions.

Layer 3 Byzantine doctrine and Layer 4 implementation remain downstream of the validated machine contract.

## Quality-control position

The project currently passes the **documentation/re-entry** requirement more strongly than the **predictive machine completion** requirement. That distinction is intentional.

A repository can be excellent institutional memory while still documenting an unfinished investigation. Status must say so plainly.

The 88% working estimate is not a completion claim. It reflects the new section-mapping and metadata-structure constraints while preserving the major implementation-closure gaps.

## Six-month re-entry instructions

A returning engineer should:

1. read `../RESEARCH_INDEX.md`;
2. read this status file;
3. read `LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`;
4. read `MACHINE_EVIDENCE_MATRIX_2026-09-02.md`;
5. read `MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`;
6. read the native archaeology log and QC addendum;
7. read `LAYER1_NATIVE_PASS_2026-09-02_UNITAI_CONTROL_LOOP_DEEPENING.md`;
8. read `LAYER1_NATIVE_PASS_2026-09-03_AIEXPERT_UNITAI_ARCHITECTURE.md`;
9. read `LAYER1_QC_AMENDMENT_2026-09-02_UNITAI_AND_METADATA.md`;
10. read `LAYER1_NATIVE_PASS_2026-09-03_METADATA_ADDRESSING_AND_RULE_LOADER_QC.md`;
11. read `OPEN_NATIVE_QUESTIONS_LAYER1.md`;
12. inspect the atomic machine ledgers;
13. continue from the immediate work sequence above.

## Status rule

Do not promote this document to "Layer 1 complete" merely because the investigation becomes large or the documentation becomes polished. Completion is an evidence decision governed by the predictive standard.
