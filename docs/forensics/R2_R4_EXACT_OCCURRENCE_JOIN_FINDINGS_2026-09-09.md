# AEGIS / AiByz — R2/R4 Exact Occurrence Join Findings

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** MACHINE-CHECKED STATIC PASS — R2/R4 remain open

## 1. Exact source verification

The exact four-file stock closure was read directly from the installed target package and rehashed during this pass:

| File | Bytes | SHA-256 |
|---|---:|---|
| `AI (HD version).per` | 1,167,238 | `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c` |
| `Promisory/defaultConstants.per` | 33,628 | `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad` |
| `Promisory/finalingConstants.per` | 10,515 | `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455` |
| `Promisory/finaling.per` | 29,232 | `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52` |

The canonical GitHub `symbol_inventory.jsonl` contains **5,259 lexical `defconst` declaration records / 1,480 unique symbols**. A deterministic scan of the exact installed four-file closure reproduced those counts and indexed **28,691 exact lexical symbol occurrences**.

The reproducible scanner is:

`docs/forensics/tools/r2_r4_exact_occurrence_join.py`

## 2. Critical active-closure finding: `cavarchers` is absent

An exact search of all four active stock-closure files found **zero occurrences** of `cavarchers`.

The symbol does exist in the broader historical Promisory corpus, including:

- `Promisory/const.per`
- `Promisory/customConstants.per`
- `Promisory/init.per`
- `Promisory/researches.per`
- `Promisory/threats.per`
- `Promisory/units.per`

Therefore the historical writer/reader chain involving `cavarchers` cannot be promoted into the active four-file runtime state graph merely because those historical source files exist.

**Correct disposition:**

`cavarchers = HISTORICAL_SOURCE_STATE / NOT IN ACTIVE FOUR-FILE CLOSURE`

This is a concrete correction to the earlier broad R2/R4 seed interpretation.

## 3. Critical active-closure finding: `temporary-goal2` is not active in the observed occurrence

The only occurrence of `temporary-goal2` in the four-file closure is:

`AI (HD version).per:5806`

```text
;    (up-modify-goal temporary-goal2 c:- 1)
```

The surrounding active rule uses `math-goal` and `math-goal2`; the `temporary-goal2` mutation is present as commented source text.

Thus `temporary-goal2` is **not established as live stock runtime state** by this closure scan.

The farthest-pair algorithm remains valuable historical evidence, but its historical scratch channel must not be mistaken for a live target-build state channel.

## 4. `sn-cavalry-threat` is an active stock state channel

The exact source contains the declaration:

`AI (HD version).per:24`

```text
(defconst sn-cavalry-threat 65)
```

It has an explicit reset/write in the stock initialization/controller region:

`AI (HD version).per:5167`

```text
(set-strategic-number sn-cavalry-threat 0)
```

It also has active threshold writers at:

- `6927` → `1`
- `6939` → `2`
- `6951` → `3`
- `6963` → `4`
- `7006` → `1`
- `7016` → `2`
- `7031` → `1`
- `7045` → `1`

The first threshold group is driven by `players-unit-type-count focus-player` over cavalry lines including knight, scout-cavalry, tarkan, war-elephant, camel and cataphract lines.

The source also contains numerous readers/guards of the form `strategic-number sn-cavalry-threat ...` across economy, research, production, and military control regions.

This proves the **static source dependency graph**.

It does not yet prove:

- rule execution frequency;
- writer precedence when multiple rules are eligible;
- exact persistence across controller cycles;
- engine/runtime observability timing;
- strategic consequence.

Those remain qualification questions.

## 5. Attack-state channels are active stock state

The exact source contains:

- `retreat-now-goal = 20` at line 52;
- `attack-status-goal = 24` at line 56;
- `restart-attack-goal = 27` at line 59.

The source contains active writes and reads for all three. One `retreat-now-goal` write at line 34002 is explicitly commented and therefore must not be counted as an active writer without a separate lexical interpretation.

The existence of these channels and their source transitions is established. Their complete target-runtime lifecycle is not.

## 6. Exact declaration-count discrepancy: 4,893 vs 4,892

The typed census reports:

`numeric_defconst_declarations = 4,893`

The canonical symbol inventory contains **4,892 integer-valued records**.

The exact difference is:

`Promisory/defaultConstants.per:99`

```text
(defconst gate-descending-open 91);(defconst gate-descending-open 99)
```

The inventory records the first declaration. The census's lexical numeric counter captures both textual `defconst` forms.

This is not evidence of a changed package. It is a parser/counting-rule discrepancy. The second textual form must be classified under the actual `.per` lexical grammar before it can be considered active.

The correct accounting is therefore:

- 5,259 lexical inventory declaration records;
- 4,892 integer-valued inventory records;
- 4,893 integer-valued textual `defconst` matches in the census;
- one extra textual match at `defaultConstants.per:99`.

No number from this discrepancy is to be used for ABI allocation.

## 7. What the occurrence join proves

The occurrence index preserves:

- source path;
- source line;
- source SHA-256;
- raw source text;
- enclosing-rule candidate;
- mutation-operation candidate;
- declaration records from the canonical inventory.

It establishes an exact **lexical occurrence graph** for the four-file closure.

It does not by itself establish semantic argument positions, active preprocessing, rule scheduling, runtime state lifetime, command acceptance, world completion, or strategic effect.

## 8. Next static operation

The next pass is narrow:

`LEXICAL RULE`
`→ EXACT MUTATION ARGUMENT POSITIONS`
`→ RULE / CONDITION RECONSTRUCTION`
`→ INITIALIZER / RESET / REINITIALIZER CLASSIFICATION`
`→ R2 OWNER JOIN`
`→ R4 LIFETIME JOIN`
`→ RUNTIME-REQUIRED CELL EXTRACTION`

Only after that should R5 begin.

## 9. Disposition

**R2 — OPEN.**  
**R4 — OPEN.**  
**Four-file lexical occurrence join — COMPLETE.**  
**Historical-to-active correction for `cavarchers` and `temporary-goal2` — COMPLETE.**  
**Semantic operation-position join — OPEN.**  
**Numeric ABI allocation — BLOCKED.**  
**Runtime lifecycle qualification — NOT STARTED.**
