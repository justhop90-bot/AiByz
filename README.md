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
- `04_PROMISORY/` — Promisory/ADPromisory research substrate.
- `05_PORPHYRA/` — canonical control and implementation history.
- `06_REPLAYS/` — empirical replay evidence.
- `07_NATIVE_ENGINE/` — native analysis and reverse-engineering evidence.
- `08_AEGIS_ARCHITECTURE/` — system architecture and execution contracts.
- `09_BYZANTINE_DOCTRINE/` — Byzantine specialization.
- `10_EXPERIMENTS/` — controlled experiments and lessons.
- `11_TOOLCHAIN/` — validators, parsers, deployment and research tooling.
- `12_RESEARCH/` — external supporting research.
- `knowledge/` — atomic durable knowledge records and cross-layer ledgers.
- `99_ARCHIVE/` — superseded/uncertain material retained for provenance.

## Canonical authorities

- **PORPHYRA V2.2.2** — immutable control baseline.
- **V3** — designated strategy source/fossil; mined for useful intent, not copied wholesale.
- **HD/2013 AI** — principal strategic archaeology specimen.
- **Experimental OMEGA/ADPromisory** — research evidence only.

## Knowledge standard

Claims are explicitly classified as fact, mechanical fact, heuristic, strategic/tactical/transition/economic principle, failure heuristic, engine workaround, historical artifact, bug compensation, hypothesis, or lesson. Evidence strength and epistemic status are preserved.

The project follows:

`evidence → observation → pattern → principle → abstraction → architecture → machine interface → validation → runtime evidence`

## Layer 1 re-entry map

Start with `docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md` for the operational machine model. Then read `docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md` for claim-level confidence and open questions, followed by `docs/MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md` for the architectural deductions. `docs/MACHINE_RECONSTRUCTION_PROCEDURE.md` defines how to independently reproduce the reasoning.

The atomic history is in `knowledge/MACHINE_INVESTIGATION_HISTORY.jsonl`. The monograph deliberately records both positive and negative evidence. It is therefore not a polished narrative that erases uncertainty; it is a controlled reconstruction of the state of knowledge.

## Security and provenance

Restricted/proprietary AoE2 binaries and stock source are not published merely because they are useful. Hashes, manifests, derived analysis, methodology, and project-owned knowledge may be preserved where appropriate. See `docs/SECURITY_AND_PROVENANCE.md`.

## Continuation principle

A competent engineer who was not present for the original work should be able to determine from this repository what was learned, why it is believed, what failed, what remains uncertain, why the architecture looks the way it does, and where the next engineering action belongs.

A documentation pass is not complete because it is long. It is complete only when an independent engineer can re-enter the project and reproduce the reasoning chain without relying on the original conversation.

## Current work

Layer 2 Phase 1: **Explicit Strategic Knowledge Reconstruction** from the HD corpus, followed by implicit/meta reconstruction and generalization into an AoE2 strategic ontology.
