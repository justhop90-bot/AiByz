# AEGIS Layer 2 Static Namespace Audit — 2026-09-05

## Scope
This pass is deliberately **static-only**. No AEGIS code was written, no stock files were modified, and no AoE2 runtime was launched.

Target build evidence: AoE2DE `101.103.48987.0`; untouched stock `/ai` installation baseline.

## Authoritative machine result
The stock HD entrypoint is `AI (HD version).per`.
Its recursive source closure is exactly four files:

1. `AI (HD version).per`
2. `Promisory/defaultConstants.per`
3. `Promisory/finalingConstants.per`
4. `Promisory/finaling.per`

No further loads were found in that closure.

## Goal-reference resolution
Across the four-file closure:
- 2,051 `set-goal` lines were found.
- 122 `up-modify-goal` lines were found.
- 1,016 `up-compare-goal` lines were found.
- 5,483 goal-operation references were resolved against numeric `defconst` declarations.
- **0 resolved goal-operation references target goal IDs 512–16,000.**
- **0 active goal-operation lines use a literal goal ID >=512.**

The unresolved goal operands are either comments/legacy text or low numeric literals/implicit scratch symbols. They do not establish an active high-goal allocation in the HD closure.

## Critical distinction: full stock tree vs runtime closure
A scan of all 50 `.per` files in the installed stock tree found high numeric goal uses in non-closure modules, including `Promisory/buildings.per` and `Promisory/paphosConstants.per`.
Therefore **"the entire stock /ai directory never uses high goals" is false**.

The defensible statement is narrower and stronger: **the actual stock HD runtime closure loaded by `AI (HD version).per` contains no resolved high-goal state allocation.**

## External semantic evidence
World's Edge's Update Preview 125283 explicitly increased available goals from 512 to 16,000. The current AoE2 AI Scripting Encyclopedia lists goals as 1–16,000 and describes goals as integer storage variables.

This establishes capacity, not ownership. Static absence establishes non-reference in the observed closure, not runtime reservation.

## Engineering conclusion
The high-goal region is now **STATICALLY QUALIFIED AS A CANDIDATE AEGIS NAMESPACE RELATIVE TO THE STOCK HD CLOSURE**, not yet runtime-proven ownership.

No numeric allocation is authorized by this document.

## Remaining Layer 2 gates
1. Define a namespace policy that avoids all known stock-loaded and future-conflict hazards.
2. Resolve command-specific restrictions for high/extended goals from authoritative semantics.
3. Freeze symbolic ABI rules before implementation.
4. Perform runtime legality/isolation/persistence only after Layer 2 static design is declared complete and explicitly authorized.

**Layer 2 status: 94/100 — static namespace/semantic characterization substantially closed; runtime gates intentionally deferred by project rule.**
