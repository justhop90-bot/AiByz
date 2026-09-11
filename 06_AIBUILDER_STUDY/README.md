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

## Governing study path

The study proceeds in this order:

`SOURCE → ABI → OWNERSHIP → LIVENESS → AUTHORITY → RUNTIME QUALIFICATION → VERTICAL SLICE → AEGIS POLICY`

The governing work plan is [`06_NEXT_PATH.md`](06_NEXT_PATH.md). It is the controlling sequence for this study.

### Gate A — Static ABI

Reconcile the Goal, working/register, timer, Strategic Number, operation-width, and alias inventories against the actual source. In particular, distinguish repository allocation from engine-safe allocation. The range 122–479 is not treated as free ABI merely because the current AiBuilder root does not allocate it.

### Gate B — Ownership and liveness

Trace each selected policy channel completely:

`declaration → all writers → all readers → predicates → feasibility → action request → downstream consumer → reassessment`

Existing traces are evidence for the individual channels they cover; they do not authorize generalization to untraced Goals.

### Gate C — Runtime authority

Use one deliberately minimal qualification to answer the narrow runtime question static source cannot answer: whether a proposed writer can affect an existing consumer at the relevant execution point. The tester is not a discovery mechanism.

### Gate D — Vertical slice

Promote one complete production lifecycle. The governing first slice is the **Civilian Production Loop**, not a broad military override layer.

### Gate E — AEGIS policy

Only after the substrate and authority boundaries are established should Byzantine policy be layered onto the existing execution machinery.

## Current conclusions

- `AiBuilder.per` is the composition root; the loaded execution corpus is under `AiBuilder/`.
- `constantsUP.per` is foundational and loads first.
- The root establishes working Goal state including `local-total` 495 through `temporary-goal` 510, with structured search-state and scratch reuse that must not be treated as automatically safe for Byzantine storage.
- Root timers currently include `town-size-timer` 1 through `naval-attack-timer` 5; arbitrary new timer allocation remains unauthorized.
- Module load order is explicit and materially affects state reuse and execution assumptions.
- `phaseUpdate.per` is the major producer of `desired-*` policy inputs.
- `economy.per`, `construction.per`, and `militaryUnits.per` consume those policy inputs to perform resource, construction, and training behavior.
- `technologies.per` provides upgrade/research behavior and escrow management.
- `market.per` contains reactive resource-exchange behavior.
- The blanket proposal to replace `unit-type-count` with `unit-type-count-total` in `technologies.per` is disproven by the current static trace; those rules use specific unit types appropriate to the upgrades they guard.
- `previous-phase` is a direct static defect candidate because the current corpus shows it being read without a corresponding writer; its runtime effect and any repair remain separate questions.
- `any-enemy` semantics for primitives not demonstrated in the corpus remain unconfirmed and must not be silently promoted to production assumptions.
- Goals 48, 49, and 57 have individual source-backed existing-channel traces. Those traces establish static ownership/liveness facts for those channels only; runtime writer precedence and world-state causality remain unproven.
- Goal 54 is the next military-channel trace target only after its actual source occurrences are recovered and inspected; inventory-table presence alone is insufficient evidence.
- UC-04 has been narrowed: symbolic-to-numeric binding is directly established by the composition root. The remaining UC-04' question is extension legality, slot safety, duplicate behavior, and declaration-order/loader effects. New Goal allocation remains unauthorized.

## What this section is not

This is not a Byzantine strategy specification, not a replacement for AEGIS, and not permission to start writing a large override layer. It is the substrate investigation required before doing that safely.

## Next study artifact

[`06_NEXT_PATH.md`](06_NEXT_PATH.md) is now the governing forward plan. The immediate work is static reconciliation and ownership/liveness closure, followed by one frozen runtime authority qualification. No Byzantine implementation is authorized before those gates pass.
