# AEGIS Runtime Module Ladder v0.1

**Date:** 2026-09-11  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Scope:** Establish the runtime path without match automation or scenario-loader automation.

## Decision

Match automation is retired. Runtime qualification will proceed as an **incremental module-integration ladder**.

The unit of qualification is not the entire AEGIS bot at first. It is:

> **stock target engine + canonical `AEGIS-BYZ.per` runtime root + one selected AEGIS module + the minimum dependencies required by that module.**

Each rung must establish that the selected module can coexist with the canonical root/load environment before another module is admitted.

This is an integration ladder, not a new architecture.

## Core rule

A module is not considered runtime-qualified merely because:

- its `.per` file exists;
- static tests pass;
- the root contains a `(load ...)` statement;
- the engine starts;
- a command appears in a replay;
- a goal changes.

A rung advances only when target-build evidence demonstrates the module's claimed behavior and the module's interactions with already-qualified modules.

## Runtime ladder

### R0 — Engine/session reachability

Purpose: prove we can reliably launch the exact target build and obtain an observable session without modifying the game or relying on match automation.

Required evidence:

- exact executable/build identity;
- process starts;
- session reaches a usable game state;
- session can be exited/repeated;
- logs/replay/output channel identified;
- no claim yet about AEGIS execution.

Status: **OPEN**.

### R1 — Foundation-only

Load only the minimum canonical foundation required for a harmless AEGIS observation module.

Purpose: establish that the AEGIS source-loading path itself is viable.

No strategic or physical behavior is credited.

### R2 — One-module observation

First target: `AEGIS-civilian-census-v0`.

Required proof:

`LOAD → INITIALIZE → TIMER → NATIVE FACT READ → CENSUS FRAME → VALID`

The census module is intentionally first because it observes villagers, town centers, pending villager objects, and game time without issuing a physical production command.

The source explicitly describes itself as an observation adapter rather than strategic policy or worker allocation. fileciteturn237file0

### R3 — Observation + state consumer

Add `AEGIS-civilization-state-v0` only after R2 passes.

Required proof:

`CENSUS → CIVILIZATION STATE`

No production command yet.

### R4 — Demand generation

Add `AEGIS-civilian-demand-v0`.

Required proof:

`STATE → DEMAND`

Demand must remain a service request, not a train command. The current implementation explicitly maintains that boundary. fileciteturn238file0

### R5 — Physical production adapter

Add `AEGIS-villager-production-v0`.

Required proof:

`DEMAND → AUTHORIZATION → PHYSICAL REQUEST → ENGINE ACCEPTANCE/PENDING`

Pending is not completion.

### R6 — Lifecycle reconciliation

Add `AEGIS-civilian-lifecycle-reconciler-v0`.

Required proof:

`REQUEST → PENDING → BASELINE DELTA → COMPLETION OR FAIL → CLOSE/REASSESS`

The reconciler already encodes this distinction and explicitly refuses to treat pending as completion. fileciteturn239file0

### R7 — Civilian Production Loop vertical slice

Integrate R2–R6 and qualify the complete causal chain:

`WORLD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT → DEMAND → AUTHORIZE → EXECUTE → PENDING → WORLD TRANSITION → CAUSAL CONFIRMATION → REASSESS`

This is the first meaningful S5 target.

### R8+ — Additional modules

After the civilian slice passes, admit additional modules one at a time according to dependency and risk, rather than loading the whole tree at once.

Each module gets its own rung and evidence record.

### FINAL — Canonical whole-system root

Only after individual modules and bounded combinations are qualified do we return to the complete `AEGIS-BYZ.per` root and test the assembled system.

Whole-system qualification is a separate claim from individual module qualification.

## Isolation method

For each rung, create a **qualification root** derived mechanically from the canonical `AEGIS-BYZ.per` load contract.

The qualification root must:

1. retain the exact target constants/foundation required by the selected module;
2. load exactly the selected module and its already-qualified dependencies;
3. exclude unqualified AEGIS modules;
4. contain no alternate strategy implementation;
5. carry an explicit rung identifier;
6. record the source SHA/hash manifest;
7. never be promoted to production merely because it passes a rung.

This prevents unrelated modules from masking a failure.

## What “works” means

Every rung uses the same five evidence gates:

1. **Load** — target engine actually loads the tested source.
2. **Execute** — the module's rules actually fire in the target engine.
3. **Observe** — expected engine-observable state appears.
4. **Attribute** — the observation can be causally tied to the module's authorized action, where the module claims an action.
5. **Integrate** — adding the next qualified module does not invalidate the previous contract.

For observation-only modules, Gate 4 is attribution of the observed frame to the module's execution, not physical-command causality.

## Failure discipline

A failed rung does not trigger a jump to the next module.

Instead:

`FAIL → isolate → diagnose → patch → static suite → repeat same rung`

No later module is allowed to hide an earlier failure.

## Runtime evidence packet

Every rung receives:

- `RUNG.md`
- `SOURCE-MANIFEST.json`
- `LOAD-MANIFEST.json`
- `STIMULUS.md`
- `TRACE.jsonl`
- `EVIDENCE.json`
- `RESULT.md`
- `HASHES.txt`

The packet must distinguish:

`source presence / load / rule execution / state observation / command acceptance / pending / world transition / causal confirmation`.

## First executable target

**R2 — Civilian Census v0.**

It is the correct first module because it has no physical command authority and therefore gives us the cleanest answer to the first runtime question:

> **Can the exact target engine load the AEGIS runtime source and execute one bounded AEGIS observation service while the rest of AEGIS remains excluded?**

If R2 fails, do not proceed upward. Fix the runtime boundary first.

## Non-goals

This framework does not:

- resurrect scenario-loader automation;
- require automated match control;
- claim strategic effectiveness;
- promote candidate modules to production;
- infer engine semantics from source vocabulary;
- treat replay command streams as completion evidence;
- replace the canonical AEGIS architecture.

## Promotion rule

A module's maturity remains S3/S4 until target-build evidence supports S5. A complete civilian vertical slice remains unqualified until its causal lifecycle is demonstrated. S5 does not imply S6.
