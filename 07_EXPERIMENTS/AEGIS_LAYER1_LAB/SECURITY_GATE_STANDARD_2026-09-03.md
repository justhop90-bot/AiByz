# AEGIS Layer 1 Security Gate Standard — 2026-09-03

## Purpose
Raise the parser-qualification and native-adapter gates from functional qualification to fail-closed laboratory controls.

## Trust boundaries

1. The supplied AoE2ScenarioParser is external laboratory tooling, never ByzBot runtime code.
2. AoE2DE_s.exe is executable only after exact SHA-256 verification.
3. Generated scenarios are test fixtures, never executable code.
4. The game installation is read-only evidence/capability input; experiments write only to an isolated lab run root.
5. Parser and runtime failures are infrastructure failures, never causal evidence.
6. XS is excluded from the ByzBot architecture and from calibration fixtures.

## Gate A — Parser qualification

- Exact source-tree digest is mandatory.
- Import must resolve to the qualified tree.
- Only the documented scenario version is admitted.
- Fixture validation rejects XS script-call conditions/effects.
- Parser bundled XS execution facilities are prohibited.
- Fixture output must remain outside the installed game AI tree.
- Provenance records source digest, fixture digest, scenario version, and test result.

## Gate B — Native runtime qualification

- Exact executable digest is mandatory before every launch.
- Runtime uses argv, never a shell.
- Run directory must resolve beneath the AEGIS lab run root.
- Game-installation paths are never writable experiment destinations.
- Child environment is sanitized; credentials and unrelated environment state are not inherited.
- Timeout is mandatory; timed-out processes are killed and reaped.
- stdout/stderr are captured as raw artifacts.
- Process exit is not a game-state observation.
- No DLL injection, hooks, debugger attachment, memory patching, or process modification.

## Promotion gate

A gate passing proves instrumentation integrity only. It does not promote a Layer 1 causal proposition. Promotion requires controlled observations, competing-hypothesis discrimination, provenance, reproducibility, and an explicit adjudication record.

## Fail-closed rule

Any provenance mismatch, path violation, forbidden XS element, unexpected executable, unsupported scenario version, timeout-reap failure, or missing required artifact fails the run. No fallback, silent substitution, or automatic repair is permitted.

## Current status

Parser qualification: PASS for the supplied snapshot and DE 1.58 fixture.
Native runtime qualification: foundation PASS; native game-load/observation calibration remains pending.
Layer 1: 89%; no causal promotion.
