# AEGIS A1 Machine Evidence Index

**Capture date:** 2026-09-05
**Target build:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652 / Update #180059
**Canonical repository:** `main`
**Evidence branch:** `aegis/a1-machine-evidence-2026-09-05`

## Purpose

This directory is the durable GitHub record of machine evidence produced during A1 stock-runtime archaeology on Weebo.

The installed AI tree was restored from Steam and is treated as the current stock-runtime baseline. The machine evidence is dated and hash-bound so that local workstation state does not remain the sole authority.

## Captured artifacts

| Artifact | Weebo source | Status |
|---|---|---|
| `AEGIS_A1_LOAD_CLOSURE_2026-09-05.json` | `C:\Users\justh\AEGIS_A1_LOAD_CLOSURE_2026-09-05.json` | **Committed** |
| `AEGIS_A1_STOCK_SNAPSHOT_2026-09-05.json` | `C:\Users\justh\AEGIS_A1_STOCK_SNAPSHOT_2026-09-05.json` | **Committed as identity record** |
| `AEGIS_A1_STOCK_MANIFEST_2026-09-05.jsonl` | `C:\Users\justh\AEGIS_A1_STOCK_MANIFEST_2026-09-05.jsonl` | **Captured locally; transfer of full 517-line JSONL remains pending** |
| `AEGIS_A1_TYPED_STATE_CENSUS_2026-09-05.json` | `C:\Users\justh\AEGIS_A1_TYPED_STATE_CENSUS_2026-09-05.json` | **Captured locally; full 35,499-line transfer remains pending** |
| `AEGIS_A1_RUNTIME_TOPOLOGY_2026-09-05.json` | `C:\Users\justh\AEGIS_A1_RUNTIME_TOPOLOGY_2026-09-05.json` | **Committed as normalized topology record** |

## Stock identity

Executable SHA-256:

`6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

Stock AI package contains **516 files** in the recursive snapshot.

## Verified runtime closure

Entrypoint:

`AI (HD version).per`

Recursive source closure:

1. `AI (HD version).per`
2. `Promisory\defaultConstants.per`
3. `Promisory\finalingConstants.per`
4. `Promisory\finaling.per`

No further loads were found from those four files.

## State census

The closure currently measures:

- Goals: 87 referenced channels / 3,193 operations
- Strategic numbers: 143 referenced channels / 1,836 writes/operations
- Timers: 29 referenced channels / 83 operations
- Flags: no flag operations detected

The runtime topology also records fact/query activity and production/build/research primitives.

## Authority rule

GitHub `main` is the project's primary durable source. Local Weebo artifacts are acquisition evidence. A local artifact becomes canonical project evidence only after it is committed with provenance and its relationship to the stock baseline is explicit.

The two large local census files are deliberately marked pending rather than represented by fabricated or incomplete copies. Until their full transfer is completed, the exact local files remain the forensic originals.

## ABI gate

No numeric AEGIS goal/SN/flag/timer allocation is authorized by these captures. The evidence exists to support the collision audit and writer/reader matrix required by the ABI gate.
