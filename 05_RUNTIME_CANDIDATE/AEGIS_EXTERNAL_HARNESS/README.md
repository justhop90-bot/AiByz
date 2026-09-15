# AEGIS External Runtime Harness v1

Status: **IMPLEMENTATION SCAFFOLD — NOT YET RUNTIME-QUALIFIED**

This harness is the first implementation artifact for Layer 3B machine qualification. It deliberately does **not** depend on the embedded AoE2DE test-harness path and does not inject, patch, hook, or modify the retail executable.

## Architecture

`experiment manifest -> immutable build capture -> disposable AI package -> retail launch -> process/lifecycle evidence -> replay capture -> replay parser -> derived events -> verdict`

Live memory instrumentation is an optional adapter boundary, not a core dependency. Any adapter that requires process injection or memory modification remains outside the default security profile and must never be silently enabled.

## Evidence model

Every run records:

- exact executable path, version, and SHA-256;
- experiment identity and schema version;
- AI package source and hash;
- launch arguments and environment policy;
- process start/exit state;
- stdout/stderr and supervisor timing;
- replay artifact hashes when produced;
- parsed replay metadata when available;
- explicit verdict and limitations.

The harness never upgrades `UNKNOWN` to `PASS` merely because a process exited successfully.

## Verdicts

- `PASS_RUNTIME_CONFIRMED`
- `PASS_CROSS_CORROBORATED`
- `OBSERVED_WITH_LIMITATIONS`
- `FAIL_RUNTIME_BEHAVIOR`
- `FAIL_HARNESS`
- `UNKNOWN`
- `NOT_APPLICABLE`

## First qualification campaign

1. Build identity
2. Player identity / perspective
3. Game clock
4. Object identity
5. Unit owner/type
6. Visibility boundary
7. Cavalry observation
8. Command-vs-world-transition timing
9. Pending/queued-vs-created/available lifecycle
10. Replay/live timestamp correlation
11. Restart/repeatability
12. Zero/absence/UNKNOWN semantics

## Non-goals

This package does not allocate AEGIS ABI channels, does not ship production `.per` logic, and does not claim current engine semantics that have not been experimentally discriminated on build `101.103.48987.0`.
