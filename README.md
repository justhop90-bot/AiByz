# AiByz — AEGIS Byzantine AI Research

> A research and engineering repository for understanding Age of Empires II: Definitive Edition deeply enough to build a high-quality Byzantine AI.

## What this project is

AiByz is the long-term research record for **AEGIS**, a planned next-generation Byzantine AI for **Age of Empires II: Definitive Edition (AoE2DE)**.

The project is deliberately being built in stages. We are not starting with a pile of AI rules and hoping that enough rules become intelligent. We first established the machine contract, then reconstructed general AoE2 decision-making, then specialize that knowledge for the Byzantines, and only then turn the resulting model into runtime code.

The repository exists so that the answers, evidence, failed experiments, corrections, and reasoning survive even if the original developers disappear for months.

## Current position — Layer 1 investigation closed at 89%

**Layer 1 — Machine Understanding: 89% working completion position.**

The investigation phase is now **closed for handoff**. It is not certified complete. The remaining work is concentrated in implementation-level causal closure: verified native state mutations, the rule-to-action bridge, scheduler details, failure propagation, required object-lifecycle edges, and at least one experimentally predictive end-to-end path.

The final recovery document is `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`. The latest three-pass QC is recorded in `docs/QC_THREE_PASS_2026-09-03_PASS1_REPOSITORY_INTEGRITY.md`, `docs/QC_THREE_PASS_2026-09-03_PASS2_EXTERNAL_CROSS_REFERENCE.md`, and `docs/QC_THREE_PASS_2026-09-03_PASS3_PROMOTION_AND_ACTION_PLAN.md`. The subsequent whole-repository audit is `docs/QC_LIBRARY_INTEGRITY_2026-09-03.md`.

## Research layers

| Layer | Purpose | Current state |
|---|---|---|
| **1 — Machine** | Understand the execution environment and native/runtime mechanisms. | **Investigation closed at 89%; completion gate unsatisfied** |
| **2 — Strategy** | Reconstruct general AoE2 decision-making and competitive causality. | Prepared / downstream |
| **3 — Byzantine Doctrine** | Turn general strategy into Byzantine-specific doctrine. | Downstream |
| **4 — Implementation** | Build, test, validate, and promote the runtime AI. | Downstream |

The layers are ordered intentionally. Later architecture should not depend on undocumented assumptions about earlier layers.

## Latest QC disposition

The repository has now passed an additional whole-repository integrity audit. The main tree contains 108 tracked files: 88 Markdown, 10 JSON, and 10 JSONL. All JSON and JSONL records parse successfully, and 51 relative Markdown links were checked with no missing targets. No stale `91%` or retired `7,715` rule-count claim remains in the main tree.

A separate audit of active PR #12 found one concrete documentation defect: its professional handoff referenced a non-existent `07_EXPERIMENTS/AEGIS_LAYER1_LAB/MACHINE_EXPERIMENT_SCHEMA.json`. That path was corrected on the PR branch to the canonical `knowledge/MACHINE_EXPERIMENT_SCHEMA.json` location.

The audit also re-verified the historical FLWL RunList signature against the exact controlled executable using actual hexadecimal bytes. The signature produced **0 matches**. An earlier intermediate probe that rendered escaped byte tokens was invalid as a byte-pattern test and is not used as evidence.

The latest qualified rule-corpus measurement remains **7,831 syntactically reachable `defrule` definitions across 28 reachable `.per/.per2/.xs` files under conservative conditional-branch inclusion**. This is a corpus statistic, not a claim that 7,831 rules execute in every game. The older 7,715 figure is retired.

## Layer 1 result in one sentence

We progressed from script/replay vocabulary to a bounded machine model with native AI semantics, explicit uncertainty, and an independent `.pdata` function-coordinate layer; the remaining gap is implementation-level causal closure.

## Authoritative native build

All native findings are scoped to the controlled `AoE2DE_s.exe` build recorded in `docs/LAYER1_COMPLETION_CONTROL_2026-09-02.md`. Its SHA-256 is `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`. Do not generalize native addresses or structures to another executable without re-verification.

## What Layer 1 established

- The AI pipeline includes bootstrap/profile selection plus `.per` / `.per2` rule material; native diagnostic material also contains `.ai2` terminology. These labels should not be collapsed into one file type without evidence.
- Native rule state contains IDs, priorities, intervals, sorted-rule state, and rule-group concepts.
- Native AI vocabulary establishes fact initialization and a distinct persistent-fact evaluation phase.
- Native feasibility/validation forms a machine-executability boundary separate from strategic desirability.
- UnitAI exposes distinct order/action/target/notification/search/recovery concepts at the vocabulary/diagnostic level.
- Native search includes substantial filtering, ownership, LOS, pathability, range, and target-selection machinery.
- Unit/object/copy/class/type/owner identity concepts must not be conflated merely because they are numeric.
- The controlled PE contains 166,730 non-zero `.pdata` runtime-function records across 166,741 physical slots, providing an independent function-boundary coordinate system.
- CodeView `RSDS` data identifies a PDB GUID and age, but no authenticated matching PDB was found locally; it remains a future lead.
- Direct RIP-relative and exact absolute-pointer searches against selected AI anchors returned zero results for those representations; this is bounded negative evidence, not proof of absence.
- A metadata-area pointer to a valid native function was investigated and rejected as an XS API association after direct disassembly showed cleanup/destructor-like behavior.

## How to navigate this repository

1. `RESEARCH_INDEX.md` — complete human navigation map.
2. `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md` — final Layer 1 investigation record and six-month recovery entry point.
3. `docs/QC_THREE_PASS_2026-09-03_PASS1_REPOSITORY_INTEGRITY.md` — repository integrity pass.
4. `docs/QC_THREE_PASS_2026-09-03_PASS2_EXTERNAL_CROSS_REFERENCE.md` — external/source cross-reference pass.
5. `docs/QC_THREE_PASS_2026-09-03_PASS3_PROMOTION_AND_ACTION_PLAN.md` — promotion and forward-work pass.
6. `docs/QC_LIBRARY_INTEGRITY_2026-09-03.md` — whole-repository QC, corrected paths, and new RunList/rule-set corroboration.
7. `12_RESEARCH/NEW_MATERIAL_INGEST_2026-09-03.md` — latest evidence ingestion record.
8. `docs/PROJECT_STATUS_2026-09-02.md` — current project position.
9. `docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md` — predictive completion standard.
10. `docs/LAYER1_COMPLETION_CONTROL_2026-09-02.md` — evidence and completion control.
11. `docs/MACHINE_EVIDENCE_MATRIX_2026-09-02.md` — claim-by-claim evidence register.
12. `docs/MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md` — consolidated machine model.
13. `docs/LAYER1_NATIVE_ARCHAEOLOGY_LOG_2026-09-02.md` and its QC addenda — native investigation history.
14. `knowledge/` — atomic institutional memory.
15. `03_HD_ARCHAEOLOGY/` — historical AI archaeology.
16. `07_EXPERIMENTS/AEGIS_LAYER1_LAB/` — active native experiment tooling and controlled evidence when the adapter branch is promoted.
17. `12_RESEARCH/` — supporting research and provenance.

## Central research principle

The project treats **knowledge, not code, as the durable product**.

A useful result is therefore recorded as:

`source → evidence → observation → pattern → principle → abstraction → architecture → implementation requirement → validation`

A copied rule can become obsolete. A demonstrated principle, its evidence, limitations, and rationale remain useful when implementation changes.

## Evidence discipline

The repository distinguishes evidence levels instead of presenting every plausible idea as fact:

- a symbol name is vocabulary, not semantics;
- a declaration is a contract surface, not its implementation;
- a string reference is not a call graph;
- a decompiler rendering is not automatically correct source;
- a replay field is an observation, not necessarily complete internal state;
- issuing a command is not proof of execution success;
- execution success is not proof of strategic success;
- absence is not destruction;
- a failed search is not proof that a mechanism does not exist;
- validator behavior is not automatically runtime behavior;
- historical source is not automatically shipped-runtime source;
- a pointer into a valid function is not proof of semantic ownership;
- `.pdata` function geometry is structural evidence, not semantic function naming;
- a matching PDB filename is not an authenticated symbol source without GUID/age verification.

## Historical material and public boundary

The public repository preserves knowledge about historical material, not complete restricted source trees or proprietary game binaries. Historical implementations are research specimens, not automatically current-runtime authority.

The current public tree remains the development/publication boundary. Historical source-derived exposure in Git history remains controlled rather than certified-clean history.

## What completion means

Layer 1 is not complete because the documentation is long. It is complete only when critical machine paths have reproducible evidence, explicit uncertainty, traced causal paths, documented failure behavior, known cross-layer boundaries, predictive tests where practical, and no material unacknowledged black boxes.

The final investigation stopped at 89% because no native AI implementation edge was promoted without evidence demonstrating the proposition itself.

## Final Layer 1 frontier

If native investigation resumes, the highest-value targets are:

1. persistent-fact result mutation and freshness;
2. `CurrentOrder -> CurrentAction` state mutation;
3. rule/handler-to-native-action bridge;
4. action failure/invalidation/completion propagation;
5. required object identity lifecycle closure;
6. one predictive end-to-end `.per` causal experiment.

The scheduler frontier is now more sharply specified: historical external evidence supports a `RunList(AIExpert*, listId, statsOutput)` architecture in an older DE integration, while current-build signature matching is negative. Public scripting documentation also exposes a rule-set execution context through `up-get-rule-id` and `up-jump-rule`. Neither source proves the current scheduler implementation.

## Six-month recovery

A returning engineer should read `RESEARCH_INDEX.md`, then `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`, then the three-pass QC documents, then `docs/QC_LIBRARY_INTEGRITY_2026-09-03.md`, the predictive standard, completion control, evidence matrix, machine monograph, native archaeology/QC documents, and atomic knowledge ledgers. The final position is **89%**, investigation closed for handoff, completion gate unsatisfied.

**For contributors:** do not promote a hypothesis to a fact, overwrite an evidence record without preserving provenance, or treat historical code as canonical without an explicit authority decision.
