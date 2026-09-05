# AEGIS — Wave A Static Semantic Evidence

**Date:** 2026-09-05
**Status:** ACTIVE — STATIC QUALIFICATION COMPLETE WHERE POSSIBLE
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Disposition

Wave A has been pushed as far as static evidence safely permits. No unresolved runtime behavior is being promoted to truth.

| Gate | Static result | Runtime disposition |
|---|---|---|
| Q-01 Build identity | Target executable and stock AI closure fingerprinted | Qualified for testing |
| Q-02 Typed ABI | Goal namespace/candidate channel map and typed parameter distinctions established | Runtime/validator qualification required |
| Q-03 Ownership/collision | Channel-aware stock goal audit found no resolved stock goal operands in AEGIS reserved scalar range | Allocation remains provisional until validator/runtime evidence |
| Q-04 Identity/generation | Architecture requires explicit identity/generation continuity | Runtime representation test required |
| Q-05 Scope/freshness | Architecture requires scope and current-vs-last-known distinction | Runtime representation test required |
| Q-06 UNKNOWN/zero/absence | Architecture forbids collapse of unknown/absence into false/zero | Engine/search behavior test required |

## Key evidence

### Typed ABI

The current specialist parameter reference distinguishes semantic parameter types including `BuildingId`, `ClassId`, `Defconst`, and other typed identifiers. Numeric equality therefore cannot be treated as semantic equivalence. citehttps://airef.github.io/parameters/parameters-index.html

### Fact operations

`up-get-fact` and `up-get-focus-fact` read facts into goals and are documented as High cost. `up-get-object-data`, `up-get-object-target-data`, and `up-get-object-type-data` are documented as Very High cost. This supports both typed-ABI qualification and explicit runtime-budget treatment. citehttps://airef.github.io/commands/commands-index.html

### Engine drift

Official Update 177723 documents fixes to `up-send-scout`, `players-unit-type-count`, Treaty-expiry object classification, and `Object-data-next-attack`, demonstrating that AI-engine semantics can change through updates. citehttps://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/

## Static conclusion

The architecture is not blocked by missing conceptual machinery. The remaining Wave A uncertainty is machine-semantic:

`TYPED ABI → GENERATION → SCOPE/FRESHNESS → UNKNOWN/ABSENCE`

These questions must be resolved by target-build evidence before they become implementation contracts.

## Hard rule

A validator PASS may establish syntax/accepted representation. It does not establish lifecycle, publication coherence, command acceptance, world consequence, or strategic correctness.

A runtime observation may establish behavior for the tested build/configuration. It does not automatically generalize across future builds.
