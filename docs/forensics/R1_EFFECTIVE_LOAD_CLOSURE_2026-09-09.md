# AEGIS / AiByz — R1 Effective Stock Load Closure

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** PARTIALLY CLOSED — direct import closure machine-recorded; conditional preprocessing semantics remain open

## Purpose

Execute unresolved-proof obligation **R1** from `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md` without reopening broad HD archaeology.

The question is not “what files exist?” It is:

> What exact source/load set contributes to the effective stock program for the target build, including conditional branches, nested imports, symbol availability, duplicate/redefinition behavior, and load order?

## 1. Machine-recorded direct closure

The repository's machine-generated stock audit contains `_local_stock_audit_2026-09-06/import_closure.json`.

Its recorded closure is exactly:

1. `AI (HD version).per`
2. `Promisory/defaultConstants.per`
3. `Promisory/finaling.per`
4. `Promisory/finalingConstants.per`

This establishes the repository's current direct-load boundary for the target stock snapshot. It is stronger than an inference from the Promisory directory tree.

## 2. Nested-import distinction

The reconstruction map separately records nested imports inside source modules such as:

```text
Promisory/buildings.per -> Promisory/extremebuildings2
Promisory/gatherers.per -> Promisory/ugp
```

These are **not evidence that those modules are independently loaded by the stock flattened entry point**. They matter only when the containing source module is itself part of an active load path, or when the flattened controller contains the corresponding behavior directly.

Likewise, commented loaders in `init.per` and `merge.per` are provenance evidence, not active dependencies.

## 3. What R1 now establishes

### CLOSED / high confidence

- The target snapshot has a recorded four-file direct import closure.
- The entire Promisory directory must not be treated as the stock runtime.
- `AI (HD version).per` is the primary flattened behavioral body.
- `defaultConstants`, `finalingConstants`, and `finaling` are the recorded runtime substrate at the direct-load boundary.
- Nested imports must be evaluated through their parent load path rather than by directory membership.
- Commented historical loaders are excluded from active dependency claims.

### STILL OPEN

The current `import_closure.json` is a file-set closure, not yet a complete **effective-program closure**. The following remain to be proven:

1. exact conditional predicates surrounding the `finaling` load;
2. preprocessor state/branch selection for the target retail execution;
3. symbol availability after branch elimination;
4. duplicate/redefinition resolution and load-order effects;
5. whether any nested import becomes active under a proven target condition;
6. a deterministic machine-readable rule graph connecting active loads to resulting rules/symbols.

Therefore R1 must **not** be marked fully closed yet.

## 4. Required next artifact

Build an effective-load graph with these fields:

`source -> load site -> condition -> condition evidence -> active/inactive -> nested load -> resulting symbols/rules -> load order -> duplicate/redefinition outcome -> evidence grade`

The graph should be generated from the exact target stock snapshot and retained with a content hash. It should explicitly distinguish:

- direct active load;
- conditional active load;
- conditional inactive load;
- nested active load;
- commented/provenance-only reference;
- unresolved condition.

## 5. Gate decision

**R1 gate: NOT CLEARED.**

The direct file-set boundary is sufficiently established that broad import archaeology should stop. The remaining work is a narrow preprocessing/effective-program reconstruction problem.

This result does **not** authorize AEGIS runtime implementation yet. R2 (state ownership), R3 (numeric ABI allocation), R4 (initialization semantics), and R5 (command lifecycle) remain independent gates.

## Evidence

- `_local_stock_audit_2026-09-06/import_closure.json`
- `docs/architecture/AEGIS_STOCK_SUBSYSTEM_RECONSTRUCTION_MAP_2026-09-08.md`
- `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`

## Anti-regression rule

Future agents must not reopen a general “find all Promisory dependencies” investigation unless new target-build evidence contradicts this closure. The unresolved problem is **effective conditional semantics**, not directory discovery.
