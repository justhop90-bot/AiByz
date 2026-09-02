# AiByz — AEGIS Byzantine Intelligence Project

> **Long-term engineering memory and implementation repository for AEGIS.**

AiByz is not merely a collection of AoE2DE AI scripts. It is the durable technical and intellectual record of the AEGIS project: machine knowledge, strategic knowledge, archaeological evidence, experiments, failures, architecture, provenance, and validated implementation.

## Mission

Build a next-generation Byzantine AI for Age of Empires II: Definitive Edition by first understanding the machine, then reconstructing competitive strategy as an explicit intelligence model, and only then implementing civilization-specific doctrine and runtime behavior.

## Engineering layers

### Layer 1 — Machine

Operational understanding of the AoE2DE AI execution substrate: `.ai/.per` loading, rule execution, scheduling, goals, strategic numbers, timers, facts, actions, UP/native interfaces, XS capability boundaries, diagnostics, validation, deployment, verification, and recovery.

**Status: operationally closed.** Native reverse engineering may continue as evidence enrichment without blocking higher layers.

### Layer 2 — Strategy

General competitive intelligence: causal game-state modeling, economy, production, military capability, technology, map/position, timing, information, opponent beliefs, transitions, resource taxation, initiative/tempo, and failure-state reasoning.

**Status: active.**

### Layer 3 — Byzantine Doctrine

Civilization-specific strategic doctrine derived from the general strategic ontology. Central thesis: make enemy commitments pay a conversion tax while preserving Byzantine strategic flexibility.

### Layer 4 — Implementation

Validated architecture translated into Layer-1-compatible runtime code, followed by controlled validation, replay testing, and promotion gates.

## Repository structure

- `00_CONSTITUTION/` — authority, governance, safety, change control.
- `01_MACHINE/` — native machine investigation and engine contract.
- `02_STRATEGY/` — general strategic intelligence.
- `03_HD_ARCHAEOLOGY/` — HD source archaeology and reconstructed knowledge.
- `04_PROMISORY/` — historical substrate references and project-owned research notes; raw source remains quarantined.
- `05_PORPHYRA/` — canonical control and implementation history.
- `06_REPLAYS/` — empirical replay evidence.
- `07_NATIVE_ENGINE/` — native analysis and reverse-engineering evidence.
- `08_AEGIS_ARCHITECTURE/` — system architecture and execution contracts.
- `09_BYZANTINE_DOCTRINE/` — Byzantine specialization.
- `10_EXPERIMENTS/` — controlled experiments and lessons.
- `11_TOOLCHAIN/` — validators, parsers, deployment and research tooling.
- `12_RESEARCH/` — external supporting research.
- `knowledge/` — **primary institutional-memory layer: atomic facts, principles, meta-knowledge, evidence, cross-layer mappings, failures, and lessons.**
- `99_ARCHIVE/` — superseded/uncertain material retained for provenance.

## Knowledge is the durable product

The runtime bot is an executable consequence of the research. The `knowledge/` directory is therefore treated as a first-class engineering artifact, not a notes folder.

The target is to preserve nearly everything learned from historical code, the engine, competitive strategy, experiments, and replays while avoiding redistribution of source material itself.

A mature knowledge record should allow an engineer who never saw the original source or conversation to reconstruct:

- what the system did;
- what evidence established it;
- what the original programmer appears to have been solving;
- which substrate constraints shaped the implementation;
- what alternative explanations exist;
- what failed;
- what general principle survives the implementation;
- what AEGIS should preserve, replace, or reject;
- and what experiment should validate the conclusion.

The canonical transformation is:

`source -> evidence -> observation -> pattern -> principle -> abstraction -> architecture -> machine constraint -> implementation requirement -> validation`

The implementation is not the knowledge. **The reasoning chain is the knowledge.**

See `knowledge/README.md` and `knowledge/KNOWLEDGE_PRESERVATION_STANDARD.md`.

## Project materials and publication boundary

The repository is an institutional-memory layer, not a public mirror of the game or of historical/vendor-derived source trees.

### Material classes

1. **Canonical project source** — project-owned AEGIS/PORPHYRA implementation and contracts.
2. **Strategy fossils** — historical AI material used for archaeology and knowledge recovery.
3. **Research substrate** — Promisory/ADPromisory material used as evidence where permitted; complete source remains outside the public tree.
4. **Machine evidence** — hashes, extraction reports, native-analysis findings, interface ledgers, and diagnostics.
5. **Empirical evidence** — replay-derived observations and controlled experiments.
6. **Derived knowledge** — principles, state models, schemas, architecture, methodologies, and lessons.
7. **Evidence exhibits** — small, isolated, attributed historical snippets with original explanation.

### Public-repository rule

Full proprietary game files, executables, complete stock/vendor-derived source trees, and other restricted artifacts remain outside the public repository. Their identity may be preserved with cryptographic hashes, inventories, provenance records, and derived analysis.

**Modified source is not automatically clean source.** If a tree is substantially derived from stock, historical, vendor, or otherwise restricted material, it remains quarantined unless redistribution rights are established.

The public repository may publish the *knowledge about the source* at high density. Where a historical implementation materially demonstrates a concept, use small, isolated, attributed excerpts with surrounding explanation. Excerpts are evidence exhibits, not substitutes for the original source.

The preferred public form is therefore:

`source identity -> isolated evidence -> forensic interpretation -> general principle -> AEGIS abstraction -> implementation requirement`

rather than:

`copy historical source -> rename it -> call it architecture`.

### Current quarantine decision

The following source-derived material was removed from the public knowledge branch:

- `ADPromisory/`
- `AiBuilder/`
- `ByzantineWarCouncil.per`
- `ByzantineWarCouncil.ai`

The cleanup is documented in `PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md`. Deletion from the current branch does not by itself erase earlier Git history; historical-object cleanup is a separate operation.

## Canonical authorities

- **PORPHYRA V2.2.2** — immutable control baseline.
- **V3** — designated strategy source/fossil; mined for useful intent, not copied wholesale.
- **HD/2013 AI** — principal strategic archaeology specimen.
- **Experimental OMEGA/ADPromisory** — research evidence only.

## Knowledge standard

Claims are explicitly classified as fact, mechanical fact, heuristic, strategic/tactical/transition/economic principle, meta-knowledge, failure heuristic, engine workaround, historical artifact, bug compensation, hypothesis, or lesson. Evidence strength and epistemic status are preserved.

Historical snippets are used heavily when they improve understanding, but always as contextual exhibits. A good explanation should contain more reasoning than copied syntax.

The project follows:

`evidence -> observation -> pattern -> principle -> abstraction -> architecture -> machine interface -> validation -> runtime evidence`

## Layer 1 re-entry map

Start with `docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md` for the operational machine model. Then read `docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md` for claim-level confidence and open questions, followed by `docs/MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md` for the architectural deductions. `docs/MACHINE_RECONSTRUCTION_PROCEDURE.md` defines how to independently reproduce the reasoning.

The atomic history is in `knowledge/MACHINE_INVESTIGATION_HISTORY.jsonl`. The monograph deliberately records both positive and negative evidence. It is therefore not a polished narrative that erases uncertainty; it is a controlled reconstruction of the state of knowledge.

## Security and provenance

Restricted/proprietary AoE2 binaries and stock source are not published merely because they are useful. Hashes, manifests, derived analysis, methodology, and project-owned knowledge may be preserved where appropriate. See `docs/SECURITY_AND_PROVENANCE.md` and `PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md`.

## Continuation principle

A competent engineer who was not present for the original work should be able to determine from this repository what was learned, why it is believed, what failed, what remains uncertain, why the architecture looks the way it does, and where the next engineering action belongs.

A documentation pass is not complete because it is long. It is complete only when an independent engineer can re-enter the project and reproduce the reasoning chain without relying on the original conversation.

## Current work

Layer 2: **Strategic Knowledge Reconstruction** — explicit behavior, implicit principles, meta-knowledge, generalization, cross-validation, transition/counter-transition modeling, resource-tax reasoning, and eventual Byzantine specialization.
