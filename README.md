# AiByz — AEGIS Byzantine AI Engineering Repository

> Professional research, reverse-engineering, architecture, and implementation repository for a next-generation Byzantine AI for Age of Empires II: Definitive Edition.

## Canonical status — 2026-09-09

**GitHub `main` is the authoritative starting point.**

### Final-bot authority

The current design authority is:

- `docs/AEGIS_FINAL_BOT_BLUEPRINT_AND_AUTHORITATIVE_GUIDE_2026-09-09.md` — final bot blueprint and engineering rules.
- `docs/HD_CAPABILITY_COVERAGE_AUDIT_2026-09-09.md` — source-backed closure ledger for complete HD/Promisory capability coverage.

These documents define the target architecture; they do not override machine evidence or authorize unqualified `.per` code.

Start here:

1. `CANONICAL_AUTHORITY.md`
2. `docs/AEGIS_FINAL_BOT_BLUEPRINT_AND_AUTHORITATIVE_GUIDE_2026-09-09.md`
3. `docs/HD_CAPABILITY_COVERAGE_AUDIT_2026-09-09.md`
4. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
5. `docs/CANONICAL_QC_2026-09-05.md`
6. `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
7. `docs/REPOSITORY_OPERATING_STANDARD_2026-09-05.md`
8. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`
9. `03_HD_ARCHAEOLOGY/PASS87_END_TO_END_EVIDENCE_GRAPH_2026-09-05.md`
10. `RESEARCH_INDEX.md`

Older handoffs and QC records remain as historical evidence. They are not competing authorities.

## Current engineering position

| Layer | Status |
|---|---|
| **Layer 1 — Machine/runtime** | **89% — frozen for handoff; broad archaeology closed** |
| **Layer 2 — Historical strategy archaeology** | **Major reconstruction closed; targeted evidence only** |
| **Layer 3 — AEGIS architecture** | **Blueprint established; qualification active** |
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
OBSERVE → CLASSIFY / BELIEVE → TRANSITION DETECTION
  ↓
OBJECTIVE → CAPABILITY DEMAND → DEFICIT
  ↓
CANDIDATES → RESOURCE / TIMING / POSITION / INFORMATION EVALUATION
  ↓
COMMIT → AUTHORIZE → EXECUTE
  ↓
OBSERVE RESULT → VERIFY → SUCCESS / PARTIAL / FAILURE / UNKNOWN
  ↓
RECOVER / RE-ARBITRATE → UPDATE BELIEFS → REASSESS
```

The blueprint currently defines **20 major vertical slices**, including dedicated domains for civilian lifecycle, economy/logistics, production, cavalry, infantry/ranged, siege, monks, scouting/information, force composition, battlefield command, defense/garrison, naval operations, technology, and full Byzantine strategic integration.

The first intended executable slice remains **Cavalry Threat Containment**, but it is not authorized for production implementation until the machine/ABI gate clears.

Mandatory state envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

## Evidence model

Machine/runtime authority:

`A1 exact installed target package/build`
`>` `A2 verified package snapshot`
`>` `A3 byte/content-equivalent repository snapshot`
`>` `A4 historical/source material`
`>` `A5 inference`

Only A1–A3 can clear numeric ABI allocation.

Strategic archaeology uses a separate evidence discipline: direct evidence, deterministic composition, AEGIS generalization, and hypothesis remain distinct.

## Historical strategic reconstruction

The recovered historical model is:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION/BELIEF → REQUIREMENT → CAPABILITY CANDIDATES → RESOURCE/TIMING EVALUATION → COMMITMENT → AUTHORITY → ACTION → POSTCONDITION → FAILURE/RECOVERY → REASSESSMENT`

Major recovered motifs include measure-to-state compression, guard-before-side-effect, search-before-commitment, protected transitions/escrow, production as capability acquisition, threat-driven response, attack/retreat/restart lifecycle, geometric scouting, timers/persistent state, and fallback/recovery.

The historical AI is treated as a strategic/programming corpus, not a complete specification of every game capability. The capability audit therefore remains open until the verified HD/Promisory closure has been enumerated by capability.

## Repository organization

```text
03_HD_ARCHAEOLOGY/       Historical strategy/programmer archaeology
04_LAYER3_ARCHITECTURE/  Current AEGIS architecture and ABI work
05_RUNTIME_CANDIDATE/    Runtime/replay candidates and research instruments
07_EXPERIMENTS/          Experimental infrastructure when intentionally retained
12_RESEARCH/             External research and source provenance
knowledge/               Durable atomic institutional memory

docs/                    Governance, handoffs, QC, machine evidence, procedures, blueprint
.github/                 Ownership and contribution controls
```

Do not renumber the historical directories. Their paths are part of provenance.

## Immediate engineering gates

### Historical coverage gate

`HD SOURCE INVENTORY → CAPABILITY TRACE → 20-SLICE MAPPING → GAP CLOSURE`

### Machine gate

`STOCK AI SNAPSHOT → IMPORT CLOSURE → SYMBOL / REFERENCE INVENTORY → CHANNEL OCCUPANCY → WRITER / READER MATRIX → ENGINE / VALIDATOR JOIN → ABI DECISIONS → ABI FREEZE`

### Implementation gate

`OBSERVE → BELIEVE → OBJECTIVE → DEMAND → DEFICIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER → REASSESS`

Do not begin production `.per` implementation until the applicable gates clear.
