# AEGIS / AiByz — R2/R4 Exact Occurrence Join Findings

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** MACHINE-CHECKED STATIC PASS — R2/R4 remain open

## 1. What was actually checked

The exact installed stock package was read directly from:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

The four-file load closure was hashed again during this pass:

| File | Bytes | SHA-256 |
|---|---:|---|
| `AI (HD version).per` | 1,167,238 | `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c` |
| `Promisory/defaultConstants.per` | 33,628 | `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad` |
| `Promisory/finalingConstants.per` | 10,515 | `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455` |
| `Promisory/finaling.per` | 29,232 | `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52` |

The existing GitHub `symbol_inventory.jsonl` was retrieved from `origin/main` at commit `71bd4b40e63779bee4f3ca74a7e3c1954fd7adc9` and contains **5,259 lexical `defconst` declaration records / 1,480 unique symbols**.

A deterministic source scan against the exact installed four-file closure reproduced those **5,259 lexical declaration records / 1,480 unique symbols** and indexed **28,691 exact lexical symbol occurrences**.

The reproducible scanner is:

`docs/forensics/tools/r2_r4_exact_occurrence_join.py`

## 2. Critical finding: the 4,893-vs-4,892 discrepancy is real but not a missing source declaration

The repository's typed census reports:

`numeric_defconst_declarations = 4,893`

The canonical symbol inventory contains:

`4,892` rows whose `value` is an integer numeric string.

The exact set difference is one row:

`Promisory/defaultConstants.per:99` — `gate-descending-open = 99`

Inspection of the exact source line shows:

```text
(defconst gate-descending-open 91);(defconst gate-descending-open 99)
```

The inventory records the first declaration (`91`) and not the second textual `defconst` occurrence. The typed census's numeric declaration counter includes both textual declarations.

Therefore the discrepancy is **not evidence that the stock package changed** and **not evidence that the inventory lost an active declaration**. It is evidence that the two artifacts use different lexical counting rules for an inline second `defconst` occurrence.

The line must remain semantically classified before anyone treats the second `99` as an active declaration. This pass intentionally does **not** assume comment/separator semantics merely from punctuation.

### Consequence

The earlier shorthand statement that the census and inventory were both simply "4,893 numeric declaration rows" is too coarse and must not be repeated.

The exact current accounting is:

- **5,259** lexical `defconst` records in the canonical symbol inventory;
- **4,892** integer-valued rows in that inventory;
- **4,893** integer-valued textual `defconst` matches in the typed census;
- the one additional textual match is the second `gate-descending-open` occurrence on line 99.

This is now a tracked parser/lexical-definition discrepancy.

## 3. Why this matters for R2/R4

A state-ownership ledger cannot safely treat every textual declaration as an active runtime declaration.

Likewise, it cannot discard a textual declaration merely because an inventory parser recorded only one declaration from a line.

The correct evidence chain is:

`RAW BYTES → EXACT SOURCE LINES → LEXICAL OCCURRENCES → OPERATION PARSING → ACTIVE LOAD/PREPROCESSING → RUNTIME QUALIFICATION`

R2/R4 operate primarily in the middle of that chain. R1 remains responsible for the active-program boundary.

## 4. Occurrence join result

The first exact lexical occurrence join found:

- **5,259** inventory declaration rows;
- **1,480** unique symbols;
- **28,691** exact lexical occurrences across the four-file stock closure;
- **5,266** declaration-context occurrences;
- **3,632** mutation-context occurrences;
- **19,793** reference occurrences.

These role labels are deliberately provisional:

- `DECLARATION_CONTEXT` means the source line contains a `defconst` context;
- `MUTATION_CONTEXT` means a recognized mutation primitive occurs on the same source line;
- `REFERENCE` means the symbol occurs without either recognized context.

A `MUTATION_CONTEXT` row does **not** prove that the symbol is the mutation target. Argument-position parsing is the next required refinement.

The occurrence index is therefore an **evidence index**, not a semantic ownership ledger.

## 5. What remains to be parsed

The next static refinement is narrow and mechanical:

1. parse mutation argument positions rather than classifying an entire line as a write;
2. reconstruct exact rule boundaries and conditions;
3. distinguish source-code tokens from comments/disabled text using a verified `.per` lexical rule;
4. identify initialization candidates separately from ordinary writes;
5. identify reset/clear operations separately from writes;
6. join those operations to the existing historical writer/reader graph;
7. emit the canonical R2/R4 rows;
8. mark only the cells that still require target-runtime evidence.

No broad archaeology is needed for this step.

## 6. Important negative result

The static pass did **not** discover evidence that justifies numeric ABI allocation.

The existing proposed cavalry range `10000–10015` remains blocked. The occurrence join does not change that disposition.

It also did not justify promoting historical `cavarchers`, attack/retreat goals, escrow state, or any other channel to runtime-qualified status merely because their source occurrences can be found.

## 7. R2/R4 disposition

**R2 — OPEN.**  
**R4 — OPEN.**  
**R2/R4 static occurrence join — substantially advanced; argument-position/lexical-semantic refinement remains.**  
**Runtime qualification — not started from this artifact.**

## 8. Provenance rule

All claims above are tied to the exact four-file stock hashes listed in Section 1 and to the GitHub inventory snapshot identified above. If any source hash changes, this occurrence join is stale and must be regenerated.
