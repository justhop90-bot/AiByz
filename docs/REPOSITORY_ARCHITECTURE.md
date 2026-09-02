# Repository Architecture

## Purpose

AiByz is organized as a **research system with an implementation destination**, not as a miscellaneous code dump.

The repository has three jobs:

1. preserve evidence;
2. preserve the reasoning derived from that evidence;
3. make the next engineering action obvious.

The organization therefore separates historical archaeology, machine research, durable knowledge, and public provenance rather than mixing them into one source tree.

## Current public tree

```text
/
├── README.md
├── RESEARCH_INDEX.md
├── PROJECT_MATERIALS.md
├── PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md
├── docs/
├── knowledge/
├── 03_HD_ARCHAEOLOGY/
└── 12_RESEARCH/
```

This is the **actual current publication structure**. Older planning documents may describe a larger numbered architecture. Those descriptions are historical planning artifacts, not evidence that those directories currently exist.

## Domain responsibilities

### `docs/`

Human-readable engineering documentation: current status, machine model, evidence matrices, archaeology logs, quality control, architecture consequences, provenance, and recovery procedures.

### `knowledge/`

Institutional memory. This is the granular record of facts, hypotheses, principles, experiments, schemas, evidence history, replay adjudication, and downstream strategic knowledge.

### `03_HD_ARCHAEOLOGY/`

Historical AI/source archaeology. This domain asks what earlier AI implementations did, what problems they appear to have been solving, and which principles can be generalized. It is evidence, not automatic authority.

### `12_RESEARCH/`

External supporting research and its inventory. Material here must remain traceable to its source and role in the project.

## Authority model

The repository distinguishes four different things that are often confused:

- **Evidence:** an artifact or reproducible observation.
- **Knowledge:** a conclusion supported by evidence.
- **Architecture:** a project design decision derived from knowledge and constraints.
- **Implementation:** executable behavior that must still be validated against the real machine.

Historical source is not automatically architecture. A parser is not automatically the machine specification. A successful experiment is not automatically a universal law.

## Information flow

The preferred research flow is:

`source → evidence → observation → pattern → principle → abstraction → architecture → machine constraint → implementation requirement → validation`

The reverse flow is also useful for auditing:

`implementation → requirement → architectural decision → principle → evidence`

If an important architectural decision cannot be traced backward to evidence or an explicitly declared engineering constraint, it is an audit candidate.

## Evidence discipline

The project uses an explicit evidence ladder and preserves negative results. In particular:

- names identify vocabulary; they do not prove semantics;
- declarations establish interfaces; they do not prove implementation;
- string presence establishes a discovery surface; it does not establish a call graph;
- replay data records observations; it does not necessarily expose hidden state;
- command issuance is not execution success;
- execution success is not strategic success;
- absence is not destruction;
- failed search is not proof of absence;
- inference is not fact until the proposition itself is demonstrated.

## Historical/publication boundary

The public tree intentionally does **not** contain the former ADPromisory, AiBuilder, or ByzantineWarCouncil source/runtime trees. The cleanup is recorded in `PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md`.

Deleting those files from the current branch removes them from the current public tree. Their old contents can still exist in historical Git objects; that is a separate history-retention question and must not be described as source erasure.

## Change discipline

When adding or changing research material:

1. identify the question being answered;
2. record the evidence used;
3. distinguish observation from interpretation;
4. record uncertainty and counter-hypotheses;
5. state the practical engineering consequence;
6. record the next discriminating test where the matter is unresolved.

When deleting material, preserve provenance unless there is a specific reason not to. Public cleanup should make the current repository safer and clearer without falsifying its history.

## Six-month recovery standard

A future engineer should be able to enter through `RESEARCH_INDEX.md`, recover the current status, inspect the evidence matrix, read the relevant method and investigation records, locate the exact atomic knowledge entries, and continue from the recorded next action without relying on the original conversation.

That is the repository's primary quality criterion.
