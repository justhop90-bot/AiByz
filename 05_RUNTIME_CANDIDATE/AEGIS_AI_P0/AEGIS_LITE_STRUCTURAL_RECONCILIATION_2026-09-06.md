# AEGIS-Lite Structural Reconciliation — 2026-09-06

**Status:** P0 structural audit / authoritative working record  
**Target:** AoE2DE `101.103.48987.0`, Steam BuildID `24094652`  
**Repository:** `justhop90-bot/AiByz`  
**Branch:** `aegis/external-harness-v1-2026-09-05`  
**Audited HEAD:** `21fe30f8949f2b8659f61e3b47ed4042afc2f22a`

## Executive result

A fresh run of `tools/aegis_abi_audit_v2.py` against the exact current AEGIS-Lite package resolved the recursive `load` graph correctly.

The current package closure is **8 files**, not the 1-file closure recorded by the older P2 audit artifact.

The fresh audit returned:

| Metric | Result |
|---|---:|
| Closure files | 8 |
| Declaration rows | 156 |
| Numeric declarations | 156 |
| Unique symbols | 129 |
| Resolved goal operands | 356 |
| Resolved high-goal operands | 0 |

The audit additionally identified **27 duplicate declarations**. All 27 are World Model symbols duplicated verbatim between the root entrypoint and the machine-tested `AEGIS-BYZ-Engine-Carpenter-P2.per` artifact.

## Resolved load graph

```text
AEGIS-BYZ.per
├── AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per
├── AegisProm/Aegis-belief.per
├── AegisProm/Aegis-situation.per
├── AegisProm/Aegis-objectives.per
├── AegisProm/Aegis-planning.per
├── AegisProm/Aegis-decision.per
└── AegisProm/Aegis-commitment.per
```

The eight-file closure is therefore:

1. `AEGIS-BYZ.per`
2. `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`
3. `AegisProm/Aegis-belief.per`
4. `AegisProm/Aegis-commitment.per`
5. `AegisProm/Aegis-decision.per`
6. `AegisProm/Aegis-objectives.per`
7. `AegisProm/Aegis-planning.per`
8. `AegisProm/Aegis-situation.per`

## Duplicate declaration inventory

The 27 duplicated symbols are:

```text
aegis-wm-valid 300
aegis-wm-generation 301
aegis-wm-stage 302
aegis-wm-evidence 303
aegis-wm-time 304
aegis-wm-cavalry 305
aegis-wm-camel 306
aegis-wm-food 307
aegis-wm-wood 308
aegis-wm-stone 309
aegis-wm-gold 310
aegis-wm-population 311
aegis-wm-population-cap 312
aegis-wm-age 313
aegis-wm-focus-player 314
aegis-wm-enemy-present 315
aegis-wm-cycle 316
aegis-wm-observed-at 317
aegis-wm-cavalry-age 318
aegis-wm-timer 40
aegis-knight 38
aegis-camel 92
aegis-wm-stage-init 0
aegis-wm-stage-observe 1
aegis-wm-stage-qualified 2
aegis-evidence-unknown 0
aegis-evidence-current 1
```

Each appears once in `AEGIS-BYZ.per` and once in `AEGIS-BYZ-Engine-Carpenter-P2.per` with the same value.

This is not a theoretical concern. It is a concrete source/package coherence defect in the current candidate.

## Important distinction: audit defect vs source defect

The older artifact under `audit_p2_carpenter` reported a one-file closure. That artifact is stale for the current modular package.

The audit implementation itself is capable of recursively following native `load` directives. When run against the current eight-file package on the target workstation, it resolved all eight files.

Therefore the present evidence does **not** justify claiming that the audit algorithm itself failed to understand `load`. The earlier one-file result is more properly classified as a stale or incorrectly scoped audit snapshot until its original invocation is reconstructed.

## Canonical Carpenter status

Two Carpenter-related source files exist:

- `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`
- `AegisProm/Aegis-carpenter.per`

Only the P2 artifact is loaded by the current entrypoint.

The P2 artifact is also the artifact explicitly preserved by the machine-tested handoff. The standalone Carpenter file must therefore not be silently promoted to canonical status or deleted during this reconciliation.

The correct next action is an explicit ownership decision after preserving the machine-tested P2 source.

## World Model ownership defect

The current P2 artifact contains a complete copy of the World Model before its Carpenter section. The root entrypoint also contains the complete World Model implementation.

Consequently the effective source package contains two declarations and two rule sets for the World Model state envelope.

This creates unresolved questions about:

- duplicate declaration ownership;
- duplicate observation execution;
- timer-triggered rule ordering;
- generation increments;
- state mutation order;
- diagnostic attribution;
- future semantic authority.

No semantic conclusion about which duplicate wins should be inferred from static source alone. The correct disposition is **RECONCILE BEFORE EXTENSION**.

## Additional semantic findings

The current World Model uses `up-get-fact-max any-enemy unit-type-count aegis-knight`, so its current cavalry value is not established as an aggregate count across all enemies. The safe interpretation for the current 1v1-oriented probe is a maximum over the selected enemy scope; broader aggregation semantics remain a qualification item.

`aegis-knight = 38` is a concrete Knight-unit probe. It is not a qualified substitute for a Knight-line observation.

`aegis-wm-observed-at = 1` is currently an observation marker, not a timestamp. The actual sampled game time is separately stored in `aegis-wm-time`.

`aegis-wm-valid = 1` currently records an architectural qualification transition after the observation rule runs. It must not be promoted to independently corroborated semantic truth.

## What is NOT concluded

This audit does not prove:

- that the seven-layer state pipeline executes end-to-end;
- that duplicate rules currently produce an observable runtime failure;
- that every sensor has its intended semantics;
- that `aegis-wm-valid = 1` is semantically corroborated truth;
- that Knight ID `38` is a valid substitute for a Knight-line query;
- that generation N+1 rejects stale N authority at runtime;
- that Commitment causes any engine action.

Those remain separate qualification questions.

## Required next experiment

Before native Execution adapters are added, create a single reconciled package with one authoritative World Model and one authoritative Carpenter, then run:

```text
source hash
    ↓
package hash
    ↓
AoE2 executable hash
    ↓
engine load
    ↓
controlled generation N
    ↓
controlled generation N+1
    ↓
downstream propagation audit
    ↓
stale-N rejection test
    ↓
verdict
```

The UNKNOWN/zero/absence experiment must be kept separate from the generation experiment so that a failed observation cannot be mistaken for a stale-state failure.

## Disposition

**P0-STRUCT-001 — OPEN:** duplicate World Model implementation.  
**P0-STRUCT-002 — OPEN:** two Carpenter source artifacts with one loaded.  
**P0-AUDIT-001 — RESOLVED FOR CURRENT HEAD:** recursive load closure now verified at 8 files.  
**P0-AUDIT-002 — OPEN:** replace or supersede stale one-file audit artifacts with a current closure record.

**Gate:** structural reconciliation precedes Execution.
