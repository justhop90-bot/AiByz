# AiByz — AEGIS Byzantine AI Research

> A research and engineering repository for understanding Age of Empires II: Definitive Edition deeply enough to build a high-quality Byzantine AI.

## What this project is

AiByz is the long-term research record for **AEGIS**, a planned next-generation Byzantine AI for **Age of Empires II: Definitive Edition (AoE2DE)**.

The project is deliberately being built in stages. We are not starting with a pile of AI rules and hoping that enough rules become intelligent. We are first trying to understand the system the AI actually runs on, then understand how strong AoE2 decisions work, then specialize that knowledge for the Byzantines, and only then turn the resulting model into runtime code.

In plain language, the project asks four questions:

1. **How does the game and its AI machinery actually work?**
2. **What makes a strong AoE2 decision strong?**
3. **What is uniquely powerful about Byzantine strategy?**
4. **How can those answers be implemented reliably inside the real game environment?**

The repository exists so that the answers, evidence, failed experiments, and reasoning survive even if the original developers disappear for months.

## Current focus: Layer 1 — understand the machine

The project is currently prioritizing **Layer 1: Machine Understanding**.

The standard is intentionally high. We do not consider a mechanism understood merely because we know its name or have seen a script example. For important execution paths, we want to know the causal chain:

**input/state → trigger → dispatch → processing → state change → observable result → next consequence**

That means studying the AI script environment, rule execution, state representation, command paths, native interfaces, object identity, timing, replay boundaries, diagnostics, and failure behavior. Native reverse engineering is being used as evidence where it can answer questions that documentation and scripts cannot.

The current Layer 1 target is **predictive machine understanding**: given a sufficiently specified state and input, we should be able to explain what the relevant machine layers will do next, and distinguish what is proven from what is still inferred.

## Research layers

| Layer | Purpose | Current state |
|---|---|---|
| **1 — Machine** | Understand the execution environment and native/runtime mechanisms. | **Active** |
| **2 — Strategy** | Reconstruct general AoE2 decision-making and competitive causality. | Prepared / downstream |
| **3 — Byzantine Doctrine** | Turn general strategy into Byzantine-specific doctrine. | Downstream |
| **4 — Implementation** | Build, test, validate, and promote the runtime AI. | Downstream |

The layers are ordered intentionally. Later architecture should not depend on undocumented assumptions about earlier layers.

## How to navigate this repository

If you are new to the project, read in this order:

1. **This README** — what the project is and why it is structured this way.
2. **[`RESEARCH_INDEX.md`](RESEARCH_INDEX.md)** — the map of the repository and the recommended reading paths.
3. **[`docs/PROJECT_STATUS_2026-09-02.md`](docs/PROJECT_STATUS_2026-09-02.md)** — current state, completed work, open work, and next actions.
4. **[`docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`](docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md)** — the standard used to decide whether machine knowledge is good enough.
5. **[`docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`](docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md)** — the current machine model.
6. **[`docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md`](docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md)** — what is known, how strongly it is supported, and what remains open.
7. **[`docs/LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md`](docs/LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md)** — quality-control and recovery standard for the native investigation.
8. **[`knowledge/`](knowledge/)** — the atomic, durable knowledge base.
9. **[`03_HD_ARCHAEOLOGY/`](03_HD_ARCHAEOLOGY/)** — historical AI archaeology and reconstructed design logic.
10. **[`12_RESEARCH/`](12_RESEARCH/)** — external research material and its provenance.

## Repository map

```text
AiByz/
├── README.md                         # Public front door
├── RESEARCH_INDEX.md                 # Human navigation and reading map
├── PROJECT_MATERIALS.md              # Project material inventory / boundary
├── PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md
│                                      # Public-tree provenance and cleanup record
│
├── docs/                             # Human-readable engineering documentation
│   ├── PROJECT_STATUS_2026-09-02.md
│   ├── LAYER1_*                      # Layer 1 standards, archaeology, QC, re-entry
│   ├── MACHINE_*                     # Machine model, evidence, consequences, QC
│   ├── REPOSITORY_ARCHITECTURE.md
│   └── SECURITY_AND_PROVENANCE.md
│
├── knowledge/                        # Institutional memory / durable knowledge
│   ├── LAYER1_MACHINE_FACTS.jsonl
│   ├── MACHINE_ONTOLOGY.jsonl
│   ├── MACHINE_INVESTIGATION_HISTORY.jsonl
│   ├── MACHINE_EXPERIMENT_SCHEMA.json
│   ├── replay/                       # Replay evidence and adjudication
│   └── LAYER2_*                       # Strategy knowledge prepared for later layers
│
├── 03_HD_ARCHAEOLOGY/                # Historical AI/source archaeology
│   ├── explicit reconstruction
│   ├── implicit strategic principles
│   ├── designer-logic reconstruction
│   └── forensic methods and ledgers
│
└── 12_RESEARCH/                      # Supporting research and source inventory
```

## The central research principle

The project treats **knowledge, not code, as the durable product**.

A useful result is therefore recorded as a chain:

`source → evidence → observation → pattern → principle → abstraction → architecture → implementation requirement → validation`

This matters because a copied rule can become obsolete. A demonstrated principle, its evidence, its limitations, and the reason it was chosen remain useful even when the implementation changes.

## Evidence discipline

The repository distinguishes evidence levels instead of presenting every plausible idea as fact. In particular:

- a symbol name is not its semantics;
- a declaration is not its implementation;
- a replay field is an observation, not necessarily the complete internal state;
- issuing a command is not proof that the command succeeded;
- a successful command is not proof that the strategic objective succeeded;
- absence is not proof of destruction;
- a failed search is not proof that a mechanism does not exist;
- inference remains inference until evidence demonstrates the proposition itself.

Native findings, replay observations, historical-source observations, model inference, and hypotheses are kept distinguishable.

## Historical material and the public boundary

The public repository preserves **knowledge about historical material**, not complete restricted source trees or proprietary game binaries.

Historical implementations can be valuable research specimens. They are therefore mined for evidence, design patterns, failures, and programmer intent without being treated automatically as current architecture.

The repository has deliberately removed the former source trees and runtime files associated with **ADPromisory, AiBuilder, and ByzantineWarCouncil** from the current development line. Their historical existence may remain visible in Git history because deleting a file from a branch does not erase historical commits; the current public tree is the authoritative publication boundary.

See `PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md` for the cleanup record.

## What "done" means

A Layer is not complete because its documentation is long. It is complete when an independent engineer can reproduce the reasoning behind it.

For Layer 1, that means critical machine paths have:

- reproducible evidence;
- explicit uncertainty;
- traced causal paths;
- documented failure and rejection behavior;
- known cross-layer boundaries;
- predictive tests where practical;
- and no material unacknowledged black boxes.

## Current next action

The immediate native investigation is instruction-level reference recovery around the embedded engine-facing API signatures, followed by end-to-end tracing of high-value object-identity APIs. The goal is to turn the current vocabulary-level evidence into implementation-level understanding of lookup, identity, lifetime, validation, and return-value behavior.

## Project status

**Layer 1 — Machine Understanding: active.**

The repository is intentionally conservative about completion claims. Existing documentation records substantial progress, but the predictive completion gate has not been declared satisfied merely because the vocabulary and evidence surface have been mapped.

---

**For contributors:** start with `RESEARCH_INDEX.md`. Do not promote a hypothesis to a fact, overwrite an evidence record without preserving provenance, or treat historical code as canonical without an explicit authority decision.
