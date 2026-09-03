# AiByz Research Index

This is the repository's **human navigation map**. If you have not worked on AiByz before, use this page to find the right level of information without reading the entire repository in arbitrary order.

## 1. Start here

| Document | What it answers |
|---|---|
| [`README.md`](README.md) | What AiByz is, why it exists, and the overall project model. |
| [`docs/PROJECT_STATUS_2026-09-02.md`](docs/PROJECT_STATUS_2026-09-02.md) | Where the project stands today and what happens next. |
| [`docs/REPOSITORY_ARCHITECTURE.md`](docs/REPOSITORY_ARCHITECTURE.md) | Why information is separated into research, evidence, knowledge, and implementation domains. |
| [`PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md`](PUBLIC_REPOSITORY_PROVENANCE_AUDIT_2026-09-02.md) | What was removed from the public tree and why. |

## 2. Understand the machine first

Layer 1 is the current engineering priority.

### Recommended sequence

1. [`docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`](docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md) — completion standard and evidence rules.
2. [`docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`](docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md) — consolidated machine model.
3. [`docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md`](docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md) — claim-by-claim evidence and confidence.
4. [`docs/MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md`](docs/MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md) — what the evidence means for future architecture.
5. [`docs/LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md`](docs/LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md) — native investigation record.
6. [`docs/LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md`](docs/LAYER1_NATIVE_ARCHAEOLOGY_QC_ADDENDUM_2026-09-02.md) — quality control, negative evidence, experiments, and re-entry requirements.
7. [`docs/LAYER1_NATIVE_PASS_2026-09-02_UNITAI_CONTROL_LOOP_DEEPENING.md`](docs/LAYER1_NATIVE_PASS_2026-09-02_UNITAI_CONTROL_LOOP_DEEPENING.md) — UnitAI control-loop reconstruction and direct-reference experiments.
8. [`docs/LAYER1_NATIVE_PASS_2026-09-03_AIEXPERT_UNITAI_ARCHITECTURE.md`](docs/LAYER1_NATIVE_PASS_2026-09-03_AIEXPERT_UNITAI_ARCHITECTURE.md) — latest native AIExpert, UnitAI, search, rule-representation, and fact/action vocabulary reconstruction.
9. [`docs/NATIVE_OBJECT_IDENTITY_DOSSIER_2026-09-02.md`](docs/NATIVE_OBJECT_IDENTITY_DOSSIER_2026-09-02.md) — current object/unit identity research boundary.
10. [`docs/OPEN_NATIVE_QUESTIONS_LAYER1.md`](docs/OPEN_NATIVE_QUESTIONS_LAYER1.md) — unresolved native questions and the next discriminating investigations.
11. [`knowledge/LAYER1_MACHINE_FACTS.jsonl`](knowledge/LAYER1_MACHINE_FACTS.jsonl) — atomic machine facts.
12. [`knowledge/MACHINE_INVESTIGATION_HISTORY.jsonl`](knowledge/MACHINE_INVESTIGATION_HISTORY.jsonl) — chronological investigation record.

### Layer 1 in one sentence

We are moving from **knowing the names of mechanisms** toward **being able to predict their causal behavior**.

## 3. Historical AI archaeology

[`03_HD_ARCHAEOLOGY/`](03_HD_ARCHAEOLOGY/) contains the historical research stream used to recover how earlier AI systems were structured and what design problems they were solving.

Read:

- `README.md` — scope and evidence boundary.
- `HD_EXPLICIT_RECONSTRUCTION_PASS1.md` — directly visible behavior.
- `HD_IMPLICIT_STRATEGIC_PRINCIPLES_PASS2.md` — principles inferred from repeated behavior.
- `HD_DESIGNER_LOGIC_RECONSTRUCTION.md` — reconstruction of design intent.
- `HD_PROGRAMMER_MACHINE_BRIDGE_PASS1.md` — relationship between strategy and machine constraints.
- `FORENSIC_METHOD.md` — method used to keep observation and interpretation separate.
- `FORENSIC_SUBSYSTEM_WORKBOARD.md` — investigation tracking.

Historical archaeology is evidence. It is not automatically current implementation authority.

## 4. Replay research

Replay-derived material is under `knowledge/replay/`.

The most useful entry points are:

- `REPLAY_EVENT_MODEL_V1.md` — event model.
- `ACTION_SCHEMA_ADJUDICATION_V1.md` — action payload interpretation.
- `ACTION_SCHEMA_REGISTRY_V1.json` — machine-readable action registry.
- `REPLAY_TEMPORAL_ADJUDICATION_V1.md` — timing and sequence reasoning.
- `REPLAY_TEMPORAL_SEMANTICS_QC_DEEP_PASS_V2.md` — deeper temporal quality control.
- `OBJECT_LIFECYCLE_RECONSTRUCTION_QC_PASS1.md` — object lifecycle evidence rules.
- `PRODUCTION_OBJECT_LINEAGE_QC_PASS1.md` — production and object-birth reasoning.
- `REPLAY_CALIBRATION_TRIPLE_PASS_2026-09-02.md` — calibration corpus results.

Replay data is treated as an observation instrument. It does not automatically reveal hidden native state.

## 5. Institutional memory

`knowledge/` is the durable reasoning layer.

Important files include:

- `README.md` — knowledge policy.
- `KNOWLEDGE_PRESERVATION_STANDARD.md` — how claims are recorded.
- `MACHINE_ONTOLOGY.jsonl` — machine concepts and relationships.
- `LAYER1_MACHINE_FACTS.jsonl` — atomic facts.
- `MACHINE_EXPERIMENT_SCHEMA.json` — experiment structure.
- `MACHINE_INVESTIGATION_HISTORY.jsonl` — chronological evidence history.
- `LAYER2_STRATEGIC_AXIOMS.jsonl` — strategic knowledge prepared for later use.
- `LAYER2_GENERAL_AOE2_ONTOLOGY.jsonl` — general strategic ontology.

## 6. Supporting research

`12_RESEARCH/` holds external supporting material and its inventory. This domain should explain where outside material came from and how it is allowed to influence project conclusions.

## 7. How to interpret evidence

AiByz uses an explicit evidence ladder. In practical terms:

**direct runtime/native evidence > reproduced experiment > independent corroboration > reasoned inference > hypothesis**

A statement should not be made stronger merely because it appears in several documents. The documents should point back to the evidence that actually establishes it.

Particularly important distinctions:

- **Observation:** what a tool or runtime actually showed.
- **Interpretation:** what that observation most likely means.
- **Inference:** a conclusion that follows from multiple observations.
- **Hypothesis:** a proposed explanation that still needs a discriminating test.
- **Architecture:** a design decision made after the evidence is strong enough.

## 8. Six-month recovery procedure

If you return after forgetting the project:

1. Read this file and the root README.
2. Read the current project status.
3. Read the Layer 1 predictive standard.
4. Read the evidence matrix before reading conclusions.
5. Read the machine monograph.
6. Read the native archaeology log and QC addendum.
7. Read the latest UnitAI native pass.
8. Read the latest AIExpert/UnitAI architecture pass.
9. Read the open-question register.
10. Inspect the atomic knowledge ledgers for exact claims.
11. Only then inspect historical archaeology and downstream strategy material.
12. Continue from the explicitly recorded next action rather than reconstructing plans from memory.

## 9. What not to do

- Do not treat old source code as the specification.
- Do not treat a parser's guess as native truth.
- Do not turn a convenient assumption into an engine fact.
- Do not delete failed experiments merely because they failed.
- Do not let documentation hide uncertainty.
- Do not implement Layer 4 behavior against an undocumented Layer 1 assumption.

## Current research frontier

The immediate frontier is now a three-way native closure problem: **AIExpert rule execution, UnitAI state mutation, and native API metadata dispatch**. The latest pass establishes strong native vocabulary for rule loading, fact/action definition, rule-element storage, persistent-fact evaluation, UnitAI order/action/notification state, retryable recovery, and constrained search. Direct RIP-relative and absolute-pointer scans of the tested AI diagnostic region remain negative, so the next step is implementation-level function-boundary recovery rather than more broad string searching.
