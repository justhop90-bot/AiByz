# R2/R4 Semantic Mutation Argument Join — 2026-09-09

## Scope correction

For this project, **AI(HD) archaeology is the complete stock HD/Promisory corpus**, not merely the four files in the direct runtime load closure.

The archaeology corpus used by this pass is:

- `AI (HD version).per`
- every `.per` file under the installed stock `Promisory` directory (36 files)
- total corpus: **37 `.per` files**

This is deliberately distinct from the **effective/direct runtime load closure**. The latter is a separate qualification question. The presence of a file in `Promisory` does not by itself prove that the retail flattened runtime directly loads that file. Conversely, a file can be historically essential source material even when it is not directly loaded by the current flattened entry point.

The distinction is therefore:

`HD/Promisory archaeology corpus = AI(HD) + entire stock Promisory folder`

`runtime effective-load closure = independently proven load/preprocessing result`

Do not collapse these two sets.

## Machine source identity

The installed target is the previously established AoE2DE build `101.103.48987.0` / Steam BuildID `24094652`.

Previously reverified core hashes remain authoritative, including:

- `AI (HD version).per` SHA-256 `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`
- `Promisory/defaultConstants.per` SHA-256 `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad`
- `Promisory/finalingConstants.per` SHA-256 `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455`
- `Promisory/finaling.per` SHA-256 `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52`

The full Promisory directory was independently enumerated during this pass: **36 `.per` files**.

## Load-topology observation

Direct `(load ...)` scanning of the stock entry point found:

```text
AI (HD version).per
  -> Promisory/defaultConstants
  -> Promisory/finalingConstants
```

The previously established active four-file closure also includes `Promisory/finaling.per` through the stock entry/runtime construction already recorded in R1.

The full Promisory corpus contains additional source-local load directives, notably:

```text
Promisory/buildings.per  -> Promisory/extremebuildings2
Promisory/gatherers.per  -> Promisory/ugp
```

These are **not** evidence that those files are active in the ordinary retail entry-point closure. They are evidence that the Promisory source corpus itself contains further conditional/nested source topology. That topology must remain represented in archaeology and conditional-compilation analysis.

## Exact mutation parser

Added:

`docs/forensics/tools/r2_r4_semantic_mutation_parser.py`

The parser performs structural parenthesis scanning rather than line-level mutation matching. It:

1. preserves source line numbers;
2. removes semicolon comments before structural parsing;
3. tokenizes balanced parenthesized forms;
4. identifies enclosing `defrule` forms;
5. separates condition-side from action-side mutation forms where the rule contains a direct `=>` boundary;
6. identifies mutation target by **argument position**, not by same-line proximity;
7. preserves the remaining mutation arguments separately;
8. reports exact source file, source line, enclosing rule, mutation head, target, arguments, and phase;
9. does not infer execution frequency, engine semantics, ownership, or world-state completion.

### Recognized persistent/control mutation primitives in this pass

- `set-goal`
- `up-modify-goal`
- `set-strategic-number`
- `up-modify-sn`
- `enable-timer`
- `disable-timer`
- `up-set-timer`
- `up-modify-flag`
- `up-modify-group-flag`

This is an exact syntactic mutation subset, not yet a claim that these are the only state-changing operations in the HD/Promisory system. Engine-object, group, placement, stance, escrow, and other service mutations remain separate semantic classes and must not be silently folded into this ledger.

## Machine result

Structural scan over the complete 37-file corpus produced:

- **37 files**
- **14,000 recognized mutation forms**
- **13,944 action-side mutation forms**
- **56 condition-side mutation forms**
- no parser error in the balanced-form pass

Mutation-head counts:

| Primitive | Count |
|---|---:|
| `set-goal` | 5,991 |
| `up-modify-goal` | 2,642 |
| `set-strategic-number` | 3,262 |
| `up-modify-sn` | 1,048 |
| `enable-timer` | 608 |
| `disable-timer` | 166 |
| `up-modify-flag` | 221 |
| `up-modify-group-flag` | 57 |
| `up-set-timer` | 5 |
| **Total** | **14,000** |

For comparison, the same recognized primitive set inside the previously defined four-file direct-load closure produced **4,202 forms**.

That comparison is useful only as a partition of the corpus. It is **not** a statement that the remaining Promisory files are irrelevant.

## Important correction to earlier state seeds

### `cavarchers`

The exact argument-position scan confirms historical mutation activity for `cavarchers` in the broader Promisory corpus, including initialization and threat-side mutation activity. However, `cavarchers` has **no occurrence in the active four-file closure**.

Disposition remains:

`HISTORICAL_SOURCE_STATE / NOT IN ACTIVE FOUR-FILE CLOSURE`

It must therefore remain available as historical architecture evidence but must not be promoted to an active stock runtime channel without new load/runtime evidence.

### `temporary-goal2`

The broader Promisory corpus contains **408 exact mutation-target occurrences** for `temporary-goal2` in the recognized mutation subset. This is materially different from the active-closure result.

The active four-file closure still has only the previously identified commented source occurrence at `AI (HD version).per:5806`; that occurrence is not a live mutation.

Therefore:

`temporary-goal2` is a heavily used historical/general scratch-goal concept in the full Promisory corpus, but it is not established as a live mutable channel in the current four-file stock closure.

This is exactly why corpus scope and effective-load scope must remain separate.

### `sn-cavalry-threat`

The structural parser independently recovers the active mutation target as `sn-cavalry-threat` and preserves the exact source locations previously identified:

- line 5167: reset to `0`
- lines 6927, 6939, 6951, 6963: threshold values `1,2,3,4`
- lines 7006, 7016, 7031, 7045: additional active writes `1,2,1,1`

This closes the **syntactic target-position** portion of the writer graph. It does not close runtime execution frequency or semantic calibration.

### Attack state goals

The parser recovers the active mutation targets for:

- `retreat-now-goal = 20`
- `attack-status-goal = 24`
- `restart-attack-goal = 27`

The active writes occur in the flattened `AI (HD version).per` attack/retreat region. The previously identified commented `retreat-now-goal` write remains excluded from live mutation evidence.

## What this closes

This pass closes a specific ambiguity that the earlier lexical occurrence join could not close:

> When a recognized mutation primitive occurs inside a balanced expression, the first direct argument is now structurally identified as the mutation target rather than treating every symbol on the line as a possible target.

That gives R2/R4 a real `mutation_target` field with source-position evidence.

It also establishes a clean corpus partition:

`FULL HD/PROMISORY SOURCE CORPUS`

→ historical source state / conditional branches / alternative services

→ `ACTIVE DIRECT-LOAD CLOSURE`

→ runtime-sensitive state candidates

→ targeted qualification

## What remains open

This pass intentionally does **not** close:

1. conditional compilation truth for every mutation;
2. load-order/redefinition semantics;
3. whether a syntactically valid rule actually executes in the target runtime;
4. execution frequency or pass scheduling;
5. engine-owned versus script-owned state;
6. semantic ownership when multiple writers exist;
7. command acceptance or world-state realization;
8. strategic effect;
9. ABI allocation safety.

Those remain R2/R4/R5/R18 obligations as applicable.

## Next exact operation

The next pass should not restart archaeology. It should consume this structural mutation layer and join it to the existing inventories:

`mutation target → enclosing rule → exact condition set → initializer/reset context → readers → existing R2 row → R4 lifetime/disposition`

Only after that join should we extract the genuinely runtime-sensitive cells for R5.

The full Promisory corpus remains in scope throughout that process.
