# AEGIS / AiByz — R2/R4 Joined State Lifecycle Ledger

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** OPEN — machine-checked static join; runtime qualification not yet complete

## 0. Why this artifact exists

R2 and R4 are not separate archaeology programs.

- **R2** asks who owns mutable state and controls its lifetime.
- **R4** asks how that state is initialized, reset, reinitialized, and invalidated.

This ledger is the single reconciliation surface for both questions.

It references existing inventories rather than copying them. The authoritative raw evidence remains the existing symbol inventory, typed census, collision map, load closure, ABI registries, and historical state graph.

## 1. Exact target source closure used for this pass

The installed four-file stock closure was read directly and rehashed:

| File | Bytes | SHA-256 |
|---|---:|---|
| `AI (HD version).per` | 1,167,238 | `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c` |
| `Promisory/defaultConstants.per` | 33,628 | `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad` |
| `Promisory/finalingConstants.per` | 10,515 | `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455` |
| `Promisory/finaling.per` | 29,232 | `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52` |

The existing GitHub symbol inventory contains 5,259 lexical `defconst` records / 1,480 unique symbols. An exact lexical occurrence scan of the installed closure reproduced that declaration cardinality and indexed 28,691 symbol-bearing occurrences.

## 2. Critical active-closure corrections

This pass found two historical/lexical traps that materially affect the R2/R4 join.

### 2.1 `cavarchers` is NOT present in the four-file active stock closure

An exact search of:

- `AI (HD version).per`
- `Promisory/defaultConstants.per`
- `Promisory/finalingConstants.per`
- `Promisory/finaling.per`

found **zero occurrences** of `cavarchers`.

The symbol is present in the broader historical Promisory corpus, including `Promisory/threats.per`, `researches.per`, `units.per`, `init.per`, `const.per`, and `customConstants.per`.

Therefore the earlier R2/R4 seed classification of `cavarchers` as an active-stock mutable channel was too broad. Its correct current classification is:

`HISTORICAL_SOURCE_STATE — NOT IN ACTIVE FOUR-FILE CLOSURE`

It remains useful historical evidence, but it cannot be treated as a current runtime state channel without an explicit load/provenance bridge.

### 2.2 `temporary-goal2` occurs only in commented historical code in the active flattened file

The only occurrence found in the four-file closure is:

`AI (HD version).per:5806`

with exact source text:

```text
;    (up-modify-goal temporary-goal2 c:- 1)
```

The line is inside an otherwise active `defrule`, but the `temporary-goal2` operation itself is prefixed by the source's comment marker. The active rule uses `math-goal` and `math-goal2` on the surrounding lines.

Therefore `temporary-goal2` must **not** be treated as an active stock runtime state channel from this occurrence. The historical farthest-pair algorithm remains valid historical evidence, but it does not establish that this symbol is live in the target four-file closure.

This is precisely the kind of distinction R1/R4 must preserve: historical source presence, lexical presence, and active runtime presence are different evidence classes.

## 3. Canonical R2/R4 fields

Every relevant mutable channel must ultimately have:

```text
symbol
channel_type
numeric_value
all_declarations
initializer_sites
initializer_kind
initializer_condition
first_writer
subsequent_writers
readers
guards
resetters
reinitializers
lifetime_boundary
owner_candidate
authority_effect
active_load_status
static_evidence_grade
runtime_probe_required
probe_result
disposition
```

Source hash is part of evidence identity.

## 4. Evidence-backed active-stock seed rows

| Symbol | Channel | Numeric declaration | Exact active-stock evidence | Current interpretation | Remaining gap | Disposition |
|---|---|---:|---|---|---|---|
| `sn-cavalry-threat` | SN | 65 | declaration at `AI (HD version).per:24`; reset at line 5167; active writers at 6927, 6939, 6951, 6963, 7006, 7016, 7031, 7045; numerous active readers | Real active stock strategic-number channel | Rule execution/lifetime semantics, writer arbitration, runtime observability | RUNTIME_REQUIRED |
| `retreat-now-goal` | GOAL | 20 | declaration at line 52; active writes/tests across attack-control region; one commented write at 34002 is separately identified | Real active stock goal channel | Complete ownership/lifetime and target-build transition realization | RUNTIME_REQUIRED |
| `attack-status-goal` | GOAL | 24 | declaration at line 56; active writes/tests across attack-control region | Real active stock goal channel | Complete ownership/lifetime and target-build transition realization | RUNTIME_REQUIRED |
| `restart-attack-goal` | GOAL | 27 | declaration at line 59; active writes/tests at 35153–35171 | Real active stock goal channel | Complete reset/re-entry and target-build realization | RUNTIME_REQUIRED |
| `cavarchers` | historical mutable state | — | zero occurrences in active four-file closure; present in historical Promisory modules | Historical-only state until an active-load bridge is proven | Effective-load provenance if ever needed | HISTORICAL_ONLY |
| `temporary-goal2` | historical/commented scratch | — | only active-closure occurrence is commented line 5806 | Not established as live stock state | None for current active closure; historical algorithm remains separate evidence | HISTORICAL_ONLY |

## 5. `sn-cavalry-threat` writer structure now statically closed as a source graph

The exact active source contains an unconditional initialization/reset action:

```text
5161: (defrule
5162:     (true)
5163: =>
...
5167:     (set-strategic-number sn-cavalry-threat 0)
...
```

The same active source contains threshold writers:

- line 6927 → `1` when the specified cavalry-line composition exceeds the first thresholds;
- line 6939 → `2` at the second thresholds;
- line 6951 → `3` at the third thresholds;
- line 6963 → `4` at the fourth thresholds;
- line 7006 → `1` under a time/zero-threat/stable condition;
- line 7016 → `2` under a stronger cavalry/time/stable condition;
- line 7031 → `1` under a flush-specific early condition;
- line 7045 → `1` under an early Castle-Age/time/civilization condition.

This establishes a **static writer graph**, not runtime priority or execution frequency.

In particular, the presence of a `(true)` reset rule must not be interpreted as "reset once at startup" until target runtime rule-evaluation semantics prove that behavior. The source alone establishes the action and its condition; it does not establish how often the rule fires.

## 6. Important declaration-count discrepancy

The typed census reports `numeric_defconst_declarations = 4,893`.

The canonical symbol inventory contains 4,892 integer-valued rows.

The exact difference is:

`Promisory/defaultConstants.per:99`

```text
(defconst gate-descending-open 91);(defconst gate-descending-open 99)
```

The inventory captures the first declaration. The typed census's lexical numeric counter captures both textual `defconst` forms.

This is not evidence of a changed package. It is evidence that the two inventory procedures count textual declaration forms differently. The second form must be semantically classified by the `.per` lexical grammar before it can be considered active.

The discrepancy is now explicitly tracked rather than silently averaged away.

## 7. Owner determination rules

Owner is not synonymous with writer.

A symbol may have multiple writers while retaining one semantic owner only if those writers are structurally governed by the same ownership contract. Otherwise the row remains unresolved/conflicted.

Required authority classes:

- `ENGINE_AUTHORITATIVE`
- `AEGIS_AUTHORITATIVE`
- `DERIVED_CACHE`
- `OBSERVATIONAL`

A reader never becomes an owner merely by consuming a value.

## 8. Initialization classification

Use only:

`DECLARATION_DEFAULT`
`LOAD_TIME_ASSIGNMENT`
`UNCONDITIONAL_RUNTIME_INIT`
`CONDITIONAL_RUNTIME_INIT`
`FIRST_USE_WRITE`
`RESET_REINIT`
`ENGINE_PROVIDED`
`UNKNOWN`

A declaration is not automatically an active runtime initializer.

A writer is not automatically a resetter.

A historical source occurrence is not automatically an active-load occurrence.

## 9. What the exact lexical occurrence join does and does not prove

The reproducible occurrence index records:

- exact source path;
- exact source line;
- exact source SHA-256;
- raw source text;
- enclosing-rule candidate;
- mutation-operation candidates;
- declaration records joined from the canonical inventory.

It intentionally does **not** yet claim:

- argument-position semantics;
- comment/preprocessor semantics beyond separately observed source evidence;
- rule execution order;
- runtime frequency;
- engine-owned state lifetime;
- command acceptance/completion;
- strategic effectiveness.

Those require separate qualification.

## 10. R2/R4 status

**R2 — OPEN.**  
**R4 — OPEN.**  
**Static lexical occurrence join — COMPLETE for the four-file closure.**  
**Semantic operation-position join — NEXT.**  
**Historical-to-active provenance correction — COMPLETE for the two identified symbols above.**  
**Runtime lifecycle qualification — NOT YET STARTED.**

## 11. Next operation

The next pass is no longer a broad inventory pass.

It is:

`EXACT MUTATION ARGUMENT PARSING`
`→ RULE/CONDITION RECONSTRUCTION`
`→ INITIALIZER / RESET CLASSIFICATION`
`→ R2 OWNER JOIN`
`→ R4 LIFETIME JOIN`
`→ UNRESOLVED-CELL EXTRACTION`
`→ R5 TARGETED RUNTIME QUALIFICATION`

No numeric ABI allocation occurs before these gates close.
