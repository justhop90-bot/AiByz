# AiByz / AEGIS — Repository Authority Map

**Effective:** 2026-09-05
**Canonical branch:** `main`
**Current repository head:** `8bdeb43594235980f0ab0d3d90fbace7ad00653a`

This document is the short operational map for a new engineer or AI. It deliberately separates current authority from historical material.

## 1. Start here

1. `README.md` — public project front door.
2. `CANONICAL_AUTHORITY.md` — binding authority rules.
3. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md` — current project handoff.
4. `docs/CANONICAL_QC_2026-09-05.md` — current QC disposition.
5. `docs/REPOSITORY_OPERATING_STANDARD_2026-09-05.md` — repository governance.
6. This document — authority and navigation map.
7. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md` — current ABI-audit procedure.
8. `03_HD_ARCHAEOLOGY/PASS87_END_TO_END_EVIDENCE_GRAPH_2026-09-05.md` — strategic/evidence reconstruction boundary.

## 2. Current engineering state

### Target runtime

Current target: AoE2DE `101.103.48987.0`, Update `#180059`, Steam BuildID `24094652`.

The authorized workstation capture established:

- executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

### Installed AI package

The user has restored the exact `resources\\_common\\ai` directory from Steam and states it has not been modified since restoration. Treat that directory as the **current stock-runtime baseline**.

This is an A1 provenance assertion from the authorized workstation. The next engineering task is to capture an immutable manifest/hash snapshot of that stock directory; the package must not be modified during audit.

Do not infer contamination from names such as `Promisory`, `AiBuilder`, or `testharness` appearing in the restored stock directory. Presence alone is not evidence of project modification.

## 3. Layer gates

- **Layer 1:** frozen at 89%; broad archaeology closed.
- **Layer 2:** major archaeology substantially closed; targeted evidence work only.
- **Layer 3:** active; symbolic architecture exists, numeric ABI blocked until inventory.
- **Layer 4:** blocked until ABI/build/package clearance.
- **XS:** outside scope.
- **Scenario-loader automation:** permanently retired.
- **CADE:** secondary validation candidate.

## 4. Architecture authority

First executable vertical slice:

`CAVALRY THREAT → REQUIRED CAMEL CAPABILITY → RESOURCE/CAPABILITY CHECK → PRODUCER SELECTION → COMMIT → EXECUTE → VERIFY → RECOVER/RE-ARBITRATE → REASSESS`

Mandatory state envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

The symbolic fields are defined in Passes 92–94. No numeric values are cleared yet.

## 5. Evidence authority

Use this hierarchy for machine/runtime claims:

`A1 exact installed target package/build`
`>` `A2 verified package snapshot`
`>` `A3 byte/content-equivalent repository snapshot`
`>` `A4 historical/source material`
`>` `A5 inference`

Only A1–A3 can clear a numeric ABI allocation.

For strategic archaeology, historical HD/Promisory is the reconstruction source; current target-build evidence controls runtime semantics.

## 6. Directory map

| Path | Authority / role |
|---|---|
| `03_HD_ARCHAEOLOGY/` | Historical strategy/programmer archaeology and evidence-edge reconstruction |
| `04_LAYER3_ARCHITECTURE/` | Current AEGIS architecture, contracts, ABI specifications |
| `05_RUNTIME_CANDIDATE/` | Bounded runtime/replay candidates; not automatically production |
| `12_RESEARCH/` | External research, source provenance, comparative evidence |
| `knowledge/` | Durable atomic institutional memory and ledgers |
| `docs/` | Governance, handoffs, QC, machine evidence, procedures |
| `.github/` | Repository workflow and ownership controls |

## 7. Historical material

The following are historical/superseded rather than current authority:

- `docs/PROJECT_HANDOFF_2026-09-04.md`
- `docs/QC_FULL_REPOSITORY_2026-09-04.md`
- earlier Layer-1 and Layer-2 handoffs/QC passes
- old experimental branches and PRs
- ADPromisory / byzwarcouncil-era work outside the canonical tree

Historical records are retained because they explain decisions and preserve provenance. They must not be used as current status merely because they are detailed.

## 8. Branch policy

`main` is the sole canonical starting point.

The repository accumulated a large number of dated experimental branches. They are historical evidence unless a current authority document explicitly promotes one. Do not create additional `final`, `final2`, `final3`, `master`, `canonical-final`, or equivalent authority-looking branches.

The canonical handoff branch has already been merged into `main` as commit `8bdeb43594235980f0ab0d3d90fbace7ad00653a`. The branch name remains useful as provenance but is no longer the starting authority.

## 9. Immediate engineering gate

The next work is:

`STOCK AI SNAPSHOT → IMPORT CLOSURE → SYMBOL/REFERENCE INVENTORY → CHANNEL OCCUPANCY → WRITER/READER MATRIX → ENGINE/VALIDATOR JOIN → ABI DECISION → FREEZE → FIRST .per SLICE`

Do not skip directly to `.per` implementation.
