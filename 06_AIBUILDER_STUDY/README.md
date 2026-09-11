# AiBuilder Study

**Status:** ACTIVE — substrate study, not production code

This section is dedicated to understanding the existing **AiBuilder** corpus before AEGIS/ByzBot code is promoted on top of it.

## Scope

The study covers both layers of the AiBuilder source currently present in this repository:

1. **`AiBuilder.per`** — the composition root, initialization, Goal/working-state allocation, timer allocation, phase configuration, strategic-number setup, and module load order.
2. **`AiBuilder/`** — the loaded execution modules:
   - `constantsUP.per`
   - `phaseUpdate.per`
   - `general.per`
   - `market.per`
   - `economy.per`
   - `technologies.per`
   - `construction.per`
   - `militaryUnits.per`
   - `militaryBehavior.per`

The source itself remains authoritative for what the corpus actually contains. This directory records what we can prove about that source and clearly separates established facts from hypotheses and runtime questions.

## Purpose

AiBuilder is being studied as a **candidate execution substrate**, not adopted as the AEGIS architecture by assumption.

The immediate objective is to establish an engineering-grade execution contract:

`ROOT → LOAD ORDER → STATE/ABI → CONDITIONS → POLICY INPUTS → FEASIBILITY → ACTION REQUEST → ENGINE → RESULT`

Only after that contract is sufficiently understood should Byzantine policy be layered onto it.

## Evidence discipline

Every significant finding must be classified:

- **DIRECT** — explicitly established by the current source corpus.
- **COMPOSED** — established by combining multiple direct source facts.
- **INFERRED** — reasonable interpretation not directly established.
- **HYPOTHESIS** — proposed behavior requiring validation.
- **UNCONFIRMED** — syntax/semantics not established by the corpus.
- **DISPROVEN** — contradicted by positive evidence.
- **RUNTIME-UNKNOWN** — static source analysis cannot establish the engine behavior.

Absence from the corpus is **not** proof that an engine primitive does not exist.

## Hard rules

1. Do not invent `.per` primitives, argument forms, Goal IDs, Strategic Numbers, timers, or engine semantics.
2. Do not globally replace primitives because a pattern merely looks suspicious; trace each use and its functional purpose.
3. Do not copy ADProm/byzwarcouncil architecture into this study.
4. Do not treat a strategy hypothesis as a reverse-engineering fact.
5. Do not treat an action request (`build`, `train`, `research`, `buy`) as proof that the world changed.
6. Preserve the distinction between observation, belief, authorization, request, pending state, world transition, attribution, and confirmation.
7. The tester is a validation authority, not the mechanism for discovering undocumented syntax or semantics.
8. Existing AiBuilder behavior must be understood before adding Byzantine overrides.

## Current source boundary

At the beginning of this study, the repository contains the root `AiBuilder.per` plus the nine-module `AiBuilder/` corpus listed above. The current repository source is the object under study; installed runtime files and historical AI(HD)/Promi sources are separate evidence layers and must not be silently conflated with this corpus.

## Study sequence

### Phase A — Structural reconstruction

- Establish exact load order.
- Inventory every Goal definition and numeric allocation visible in the root.
- Inventory timers and their allocation.
- Inventory Strategic Numbers used by each module.
- Map every module's inputs, outputs, state mutations, and dependencies.

### Phase B — Execution semantics

- Trace representative rules from condition → action.
- Identify feasibility gates (`can-build`, `can-train`, `can-buy`, escrow conditions, pending-object conditions).
- Determine where AiBuilder requests actions versus where it can actually establish completion.
- Identify rule-order and state-persistence dependencies.

### Phase C — Defect and hazard audit

- Undefined/unresolved symbols.
- Duplicate or conflicting state allocation.
- Goal spans used by multi-Goal operations.
- Timer allocation hazards.
- Phase-transition defects.
- Cross-module scratch-state hazards.
- Difficulty-conditional compilation hazards.
- Action-without-confirmation paths.

### Phase D — Vertical-slice qualification

Select a small number of representative execution paths and trace them completely before permitting Byzantine policy work to depend on them. The first candidate is **unique-unit production / Cataphract production**, because it exercises phase policy, desired counts, feasibility, production, and reassessment without requiring a new production subsystem.

## First conclusions

- `AiBuilder.per` is a real composition root; there is no `AiBuilder/aibuilder.per` file to treat as an alternative root.
- `constantsUP.per` is foundational and is loaded first.
- The root establishes working Goal state including `local-total` 495 through `temporary-goal` 510, and the search-state goals are deliberately grouped there.
- Root timers currently include `town-size-timer` 1 through `naval-attack-timer` 5.
- Module load order is explicit and materially affects state reuse and execution assumptions.
- `phaseUpdate.per` is the major producer of `desired-*` policy inputs.
- `economy.per`, `construction.per`, and `militaryUnits.per` consume those policy inputs to perform resource, construction, and training behavior.
- `technologies.per` provides upgrade/research behavior and escrow management.
- `market.per` contains reactive resource-exchange behavior.
- `militaryBehavior.per` controls military targeting, grouping, and attack behavior.
- The blanket proposal to replace `unit-type-count` with `unit-type-count-total` in `technologies.per` is **disproven by the current static trace**; those rules use specific unit types appropriate to the upgrades they guard.
- `previous-phase` is a direct static defect candidate because the current corpus shows it being read without a corresponding writer; the runtime effect of any repair remains a runtime-semantics question.
- `any-enemy` semantics for primitives not demonstrated in the corpus remain unconfirmed and must not be silently promoted to production assumptions.

## What this section is not

This is not a Byzantine strategy specification, not a replacement for AEGIS, and not permission to start writing a large override layer. It is the substrate investigation required before doing that safely.

## Next study artifact

`02_EXECUTION_CONTRACT.md` records the initial module-by-module contract and its evidence status. It is intentionally conservative and will be revised as source tracing establishes stronger evidence.
