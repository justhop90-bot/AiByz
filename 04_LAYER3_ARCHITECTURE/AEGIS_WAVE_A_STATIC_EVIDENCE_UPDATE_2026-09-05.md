# AEGIS — Wave A Static Evidence Update

**Date:** 2026-09-05  
**Status:** STATIC EVIDENCE RECORDED — RUNTIME STILL OPEN  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Exact HD entrypoint closure

Direct inspection of the installed stock AI confirms the normal HD entrypoint closure is exactly:

1. `AI (HD version).per`
2. `Promisory/defaultConstants.per`
3. `Promisory/finalingConstants.per`
4. `Promisory/finaling.per`

No deeper `.per` load was discovered from those four files.

## 2. Exact closure declaration census

The four-file closure contains:

- **5,259** `defconst` declaration rows;
- **1,480** unique declared symbols;
- **4,892** declarations with numeric values.

This is direct target-package evidence and supersedes estimates derived from partial source inspection.

## 3. Candidate AEGIS goal namespace collision result

The Layer-2 reserved candidate scalar-goal namespace is `10000–15999`.

A direct scan of the exact four-file HD runtime closure found:

- **0** occupied numeric values in `10000–15999`.

This is strong collision evidence for the HD closure, but it is not by itself final ABI clearance. The complete allocation gate still requires the broader stock/package inventory, validator compatibility, and target-build operation-specific legality.

## 4. Typed identifier finding: `knight-line`

The installed stock AI does **not** treat `knight-line` as one universal numeric identity.

Examples from `AI (HD version).per` include conditional definitions such as:

- `knight-line → steppe-lancer-line` under `JURCHENS-CIV`;
- `knight-line → hei-guang-cavalry-line` under `SHU-CIV`;
- `knight-line → hei-guang-cavalry-line` under `WEI-CIV`;
- `knight-line → hei-guang-cavalry-line` under `WU-CIV`.

`knight` is separately defined in at least the WEI block as `hei-kuang-cavalry`.

This is decisive static evidence against treating `knight-line` as synonymous with concrete unit ID `knight 38` or with a fixed universal line ID. It is a symbolic, conditionally defined unit-line alias in the stock HD AI package.

### Engineering consequence

The historical `up-get-focus-fact unit-type-count knight-line ...` validator issue cannot be resolved by simply replacing `knight-line` with `knight 38` without changing semantics. The correct next experiment is to test the exact compound signature against the target validator/engine and record whether the engine accepts the conditional line symbol in that fact context.

## 5. `temporary-goal` finding

The exact four-file closure contains one source comment explicitly stating that temporary scratch goals are used without being `defconst`-defined:

`; these are temporary-goal 1 and 2 respectively, but they haven't been defconsted yet for some reason`

The runtime code immediately uses literal goals `60` and `61` in that block.

### Engineering consequence

Absence of a `defconst temporary-goal` declaration is **not sufficient evidence that the semantic concept is invalid**. Conversely, the comment does not prove that every arbitrary use of a symbol named `temporary-goal` is legal. The target-build test must distinguish symbolic declaration validity from scratch-goal usage and operation-specific legality.

## 6. Fact IDs

The stock closure defines:

- `unit-type-count = 25`
- `unit-type-count-total = 26`

The specialist reference independently documents these fact families and distinguishes trained-only counts from totals including queued units. Official update history also confirms that total-count and pending-object semantics have changed over time.

Therefore Q-02 and Q-06 must treat these as typed fact semantics, not merely integer constants.

## 7. Evidence disposition

| Finding | Evidence | Status |
|---|---|---|
| Exact HD closure | direct installed source | STATIC PASS |
| 10000–15999 unoccupied in closure | direct installed source | STATIC PASS / ABI candidate evidence |
| `knight-line` conditional aliasing | direct installed source | STATIC PASS |
| `knight` distinct from `knight-line` | direct installed source | STATIC PASS |
| temporary scratch goals not necessarily defconsted | direct installed source/comment | STATIC PASS |
| `unit-type-count=25` | direct installed source | STATIC PASS |
| compound `up-get-focus-fact` + `unit-type-count` + `knight-line` runtime legality | not established | OPEN P1 |
| final numeric ABI clearance | not established | OPEN P1 |
| UNKNOWN/zero/no-result semantics | not established | OPEN P1 |

## 8. Next experiments

The highest-value experiments remain:

1. exact typed compound fact signatures;
2. goal operation boundaries;
3. SN operation boundaries;
4. UNKNOWN/zero/no-result semantics;
5. generation representation;
6. publication coherence.

No static result above is promoted to runtime truth without a target-build experiment.
