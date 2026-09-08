# P0 Total-Rework Baseline — 2026-09-07

## Purpose

This report establishes the machine-verified starting point for the total rework of AEGIS-BYZ. The previous implementation state is explicitly non-authoritative. The stock AI and the current machine corpus are being treated as separate evidence sources.

## Target machine

AoE2DE installation:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE`

Authoritative stock AI directory:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

Target build:
`101.103.48987.0 / BuildID 24094652`

## Machine-verified root finding

`AI (HD version).per` and the current `AEGIS-BYZ.per` are byte-for-byte identical.

- Lines: 36,141 each
- Bytes: 1,167,238 each
- SHA-256: `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`

The current `AEGIS-BYZ.per` begins with direct Promisory runtime loads:

```per
(load "Promisory\\defaultConstants")
(load "Promisory\\finalingConstants")
```

and also loads `Promisory\\finaling` in its final conditional section.

Therefore the current root is not an AEGIS-integrated final bot. It is the stock flattened AI under the AEGIS filename, with direct Promisory dependencies.

## Machine-verified AegisProm stock rehosts

The following files are byte-for-byte identical to their Promisory source counterparts:

- `AegisProm\\AEGIS-stock-defaultConstants.per` == `Promisory\\defaultConstants.per`
  - 33,628 bytes
  - SHA-256 `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad`
- `AegisProm\\AEGIS-stock-finalingConstants.per` == `Promisory\\finalingConstants.per`
  - 10,515 bytes
  - SHA-256 `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455`
- `AegisProm\\AEGIS-stock-finaling.per` == `Promisory\\finaling.per`
  - 29,232 bytes
  - SHA-256 `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52`

`AegisProm\\AEGIS-BYZ-FINAL-CIVOS.per` and `AegisProm\\AEGIS-civilization-os.per` are both 36,141-line stock-derived corpora and are not independent civilization implementations. They contain the same 2,429 rules and 4,222 `defconst` declarations as the stock flattened corpus, with only loader/comment differences visible in their hashes.

## Current AegisProm corpus inventory

The current AegisProm directory contains 40 `.per` files. Important subsystem sizes:

| File | Lines | Rules | Defconst |
|---|---:|---:|---:|
| AEGIS-foundation.per | 208 | 1 | 155 |
| Aegis-economy-final.per | 66 | 5 | 2 |
| Aegis-execution-final.per | 104 | 8 | 0 |
| Aegis-military-final.per | 59 | 5 | 0 |
| AEGIS-operations-final.per | 119 | 9 | 3 |
| Aegis-verification-final.per | 89 | 7 | 2 |
| Aegis-recovery-final.per | 67 | 4 | 1 |
| Aegis-belief-final.per | 55 | 5 | 0 |
| Aegis-situation-final.per | 75 | 6 | 0 |
| Aegis-objectives-final.per | 73 | 6 | 0 |
| Aegis-planning-final.per | 79 | 7 | 0 |
| Aegis-decision-final.per | 31 | 3 | 0 |
| Aegis-commitment-final.per | 38 | 4 | 0 |
| AEGIS-stock-defaultConstants.per | 941 | 0 | 683 |
| AEGIS-stock-finalingConstants.per | 400 | 0 | 266 |
| AEGIS-stock-finaling.per | 1,090 | 116 | 0 |
| AEGIS-BYZ-FINAL-CIVOS.per | 36,141 | 2,429 | 4,222 |
| AEGIS-civilization-os.per | 36,141 | 2,429 | 4,222 |

Additional V0 subsystem files include civilian census/demand/lifecycle, economic arbitration, source/dropsite serviceability, villager production, worker role/target/task/productivity/recovery/verification, and dynamic-loop probes.

## Architectural conclusion

The project must not treat the 36k stock corpus as the AEGIS brain. It is the civilization operating system/body that must be understood and reconstructed as a service substrate under AEGIS strategic cognition.

Required final shape:

```text
AEGIS-BYZ.per
  -> AEGIS cognition
  -> Civilization State / reconciliation
  -> Demand + arbitration
  -> Economy / Construction / Production / Information / Military services
  -> ABI / engine commands
  -> Engine state
  -> Observation / verification / recovery
  -> cognition
```

AEGIS cognition must own strategic intent. The civilization substrate must own reliable physical execution. The ABI must remain explicitly qualified rather than assumed.

## Rework rules

1. Previous implementation is salvageable only after independent verification.
2. Inspect the entire stock main `.per` and the entire AegisProm corpus before rebuilding major subsystems.
3. Build complete subsystems, not disposable integration candidates.
4. Every major subsystem receives three reviews:
   - ABI/compiler/reverse-engineering
   - Byzantine strategy/civilization
   - AI(HD)/behavioral regression
5. Static QC is mandatory after implementation.
6. Runtime qualification is mandatory before calling a subsystem runtime-qualified.
7. Promisory may be studied and rehosted where legally/technically required, but the final AEGIS runtime must not depend on the `Promisory\\` directory.
8. No claim of integration, qualification, or completion may be made without machine evidence.
9. Preserve and archive material discoveries, rejected designs, and qualification evidence.
10. Do not start by copying the stock AI into the AEGIS root again. The stock corpus is the reference civilization OS whose interfaces and behavior must be deconstructed and then deliberately reconstructed beneath AEGIS control.

## Status

**BASELINE: VERIFIED — TOTAL REWORK AUTHORIZED**

This report is the authoritative machine-state baseline for the new reconstruction phase. It supersedes any prior assumption that the current 36,141-line `AEGIS-BYZ.per` is an integrated AEGIS final bot.
