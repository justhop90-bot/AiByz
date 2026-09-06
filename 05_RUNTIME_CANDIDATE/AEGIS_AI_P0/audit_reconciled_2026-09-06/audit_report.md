# AEGIS-Lite Recursive Closure Audit — 2026-09-06

**Audited source HEAD:** `21fe30f8949f2b8659f61e3b47ed4042afc2f22a`  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`  
**Audit tool:** `tools/aegis_abi_audit_v2.py`  
**Audit execution:** target workstation `Weebo`

## Result

The current AEGIS-Lite entrypoint resolves an **8-file recursive load closure**.

| Metric | Result |
|---|---:|
| Closure files | 8 |
| Declaration rows | 156 |
| Numeric declarations | 156 |
| Unique symbols | 129 |
| Resolved goal operands | 356 |
| Resolved high-goal operands (512–16000) | 0 |
| Duplicate declarations | 27 |

## Closure

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

## Duplicate declaration result

The 27 duplicate declarations are the World Model state/constants (`300–318`, timer `40`, concrete unit constants `38/92`, stage constants, and evidence constants). They occur once in the root and once in `AEGIS-BYZ-Engine-Carpenter-P2.per`.

This is a **source/package coherence defect**, not proof of a runtime failure.

## Audit interpretation

The older P2 audit snapshot that recorded a one-file closure is stale for the current modular package. The audit implementation itself successfully traversed the current `load` graph when invoked against the current package.

No semantic ABI promotion is implied by this static result. Parser/audit acceptance remains distinct from target-build runtime semantics.

## Gate

This audit is a structural gate only. It does not prove end-to-end state propagation, sensor semantics, stale-generation rejection, UNKNOWN/zero/absence handling, command acceptance, or world-state effect.
