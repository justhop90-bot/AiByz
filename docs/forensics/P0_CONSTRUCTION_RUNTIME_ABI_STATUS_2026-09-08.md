# P0 Construction Runtime ABI — Status

**Date:** 2026-09-08
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** RUNTIME-QUALIFICATION GATE ACTIVE

## Decision

Static construction archaeology is sufficient to define the experiment set, but it is not sufficient to certify interpreter timing or state persistence. Final Construction OS implementation remains blocked until target-build runtime evidence is captured.

## Atomic runtime questions

1. **Placement-token persistence** — determine whether `up-build place-control` retains placement state across a transient authorization/escrow failure or clears the managed-placement buffer.
2. **Jump evaluation boundary** — determine whether `up-jump-rule` can skip the evaluation frame required for construction command registration or pending-state observation.
3. **Builder-assignment latency** — determine when `up-assign-builders` becomes observable relative to successful `up-can-build-line`, placement issuance, foundation creation, and object-data state.
4. **Placement reinitialization control** — after a failed placement, determine whether the identical placement-data initialization must be replayed before a subsequent successful attempt.

## Required evidence

Each experiment must run on the exact target build and isolate one variable. Evidence must distinguish same-pass visibility, subsequent-pass visibility, engine-tick delay, and asynchronous/conditional behavior. No result is promoted from comments or documentation alone.

## Architecture consequence

AEGIS Construction must model placement authorization, placement state, builder policy, foundation observation, and recovery as separate lifecycle states. It must not assume that command issuance equals engine acceptance or that a placement buffer survives failure.

## Current classification

- Static command families: **STATIC-QUALIFIED**
- Construction lifecycle model: **STATIC-QUALIFIED / RUNTIME-UNQUALIFIED**
- Placement-token persistence: **UNQUALIFIED**
- Jump/placement timing: **UNQUALIFIED**
- Builder assignment timing: **UNQUALIFIED**
- Reinitialization semantics: **UNQUALIFIED**
- Final Construction OS implementation: **BLOCKED pending runtime evidence**
