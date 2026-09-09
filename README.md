# AiByz — AEGIS Byzantine AI Engineering Repository

> Professional research, reverse-engineering, architecture, and implementation repository for a next-generation Byzantine AI for Age of Empires II: Definitive Edition.

## Canonical status — 2026-09-09

**GitHub `main` is the authoritative starting point.**

### Final-bot authority

There is now **one current final-bot plan**:

- `docs/AEGIS_MASTER_PLAN.md` — the single active design, capability, architecture, qualification, and implementation plan.

The master plan consolidates the former blueprint, HD capability-coverage ledger, basic-capability red-team findings, and line-by-line blueprint reconciliation. Those dated documents are historical provenance only and are no longer competing planning authorities.

Start here:

1. `CANONICAL_AUTHORITY.md`
2. `docs/AEGIS_MASTER_PLAN.md`
3. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
4. `docs/CANONICAL_QC_2026-09-05.md`
5. `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
6. `docs/REPOSITORY_OPERATING_STANDARD_2026-09-05.md`
7. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`
8. `03_HD_ARCHAEOLOGY/PASS87_END_TO_END_EVIDENCE_GRAPH_2026-09-05.md`
9. `RESEARCH_INDEX.md`

Older handoffs, QC records, forensic reports, and failed experiments remain historical evidence. They are not competing current plans.

## Current engineering position

| Layer | Status |
|---|---|
| **Layer 1 — Machine/runtime** | **89% — frozen for handoff; broad archaeology closed** |
| **Layer 2 — Historical strategy archaeology** | **Major reconstruction closed; targeted evidence only** |
| **Layer 3 — AEGIS architecture** | **Master plan established; qualification active** |
| **Layer 4 — Runtime `.per` implementation** | **Blocked until package/ABI clearance** |

Permanent boundaries:

- Scenario-loader automation/testing is retired.
- XS is outside AEGIS scope.
- CaptureAge/CADE is secondary validation infrastructure.
- HD/Promisory is historical strategy evidence, not automatic runtime authority.
- Commands are not completion proof.
- Validator acceptance is not engine semantics.
- Apparently unused numeric channels are not automatically safe.
- No prototype is production authority merely because it is named `final`.

## Target runtime

Current engineering target: **AoE2DE `101.103.48987.0` / Update `#180059`**.

Authorized workstation evidence identifies:

- executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam BuildID: `24094652`

The current installed `resources\\_common\\ai` directory has been restored from Steam and is designated by the project owner as the **untouched stock-runtime baseline**. The next evidence action is to capture its immutable manifest and hashes. Do not modify that baseline during acquisition.

## Final architecture

AEGIS is a stateful strategic controller:

```text
WORLD
  ↓
OBSERVE → CLASSIFY / BELIEVE → TRANSITION / REGIME
  ↓
OBJECTIVE → CAPABILITY DEMAND → DEFICIT
  ↓
CANDIDATES → RESOURCE / TIMING / POSITION / INFORMATION / RISK EVALUATION
  ↓
COMMIT → AUTHORIZE → EXECUTE
  ↓
OBSERVE RESULT → VERIFY → SUCCESS / PARTIAL / FAILURE / UNKNOWN
  ↓
RECOVER / RE-ARBITRATE → UPDATE BELIEFS → REASSESS
```

The master plan defines **20 major vertical slices** plus a cross-cutting control plane for regime/transition state, resource control, bounded search, execution policy, lifecycle hygiene, communication isolation, and terminal behavior.

The first intended executable slice remains **Cavalry Threat Containment**, but it is not authorized for production implementation until the machine/ABI gate clears.

Mandatory state envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

## Evidence model

Machine/runtime authority:

`A1 installed target package/build > A2 verified package snapshot > A3 equivalent repository snapshot > A4 historical source > A5 inference`

Only A1–A3 can clear numeric ABI allocation.

Strategic archaeology uses a separate evidence discipline: direct evidence, deterministic composition, AEGIS generalization, and hypothesis remain distinct.

## Repository organization

```text
03_HD_ARCHAEOLOGY/       Historical strategy/programmer archaeology
04_LAYER3_ARCHITECTURE/  Current AEGIS architecture and ABI work
05_RUNTIME_CANDIDATE/    Runtime/replay candidates and research instruments
07_EXPERIMENTS/          Experimental infrastructure when intentionally retained
12_RESEARCH/             External research and source provenance
knowledge/               Durable atomic institutional memory

docs/                    Governance, master plan, QC, machine evidence, procedures
.github/                 Ownership and contribution controls
```

The master plan is the only current final-bot planning document. Evidence documents remain in their appropriate strata and should be updated only when they are themselves the underlying evidence record.

## Immediate engineering gates

### Historical coverage gate

`HD SOURCE INVENTORY → CAPABILITY TRACE → 20-SLICE MAPPING → GAP CLOSURE`

### Machine gate

`STOCK AI SNAPSHOT → IMPORT CLOSURE → SYMBOL / REFERENCE INVENTORY → CHANNEL OCCUPANCY → WRITER / READER MATRIX → ENGINE / VALIDATOR JOIN → ABI DECISIONS → ABI FREEZE`

### Implementation gate

`OBSERVE → BELIEVE → REGIME → OBJECTIVE → DEMAND → DEFICIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER → REASSESS`

Do not begin production `.per` implementation until the applicable gates clear.
