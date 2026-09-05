# AiByz — AEGIS Byzantine AI Engineering Repository

> Professional research, reverse-engineering, architecture, and implementation repository for a next-generation Byzantine AI for Age of Empires II: Definitive Edition.

## Canonical status — 2026-09-05

**GitHub `main` is the authoritative starting point.**

Start here:

1. `CANONICAL_AUTHORITY.md`
2. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
3. `docs/CANONICAL_QC_2026-09-05.md`
4. `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
5. `docs/REPOSITORY_OPERATING_STANDARD_2026-09-05.md`
6. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`
7. `03_HD_ARCHAEOLOGY/PASS87_END_TO_END_EVIDENCE_GRAPH_2026-09-05.md`
8. `RESEARCH_INDEX.md`

Older handoffs and QC records remain in the repository as historical evidence. They are not competing authorities.

## Current engineering position

| Layer | Status |
|---|---|
| **Layer 1 — Machine/runtime** | **89% — frozen for handoff; broad archaeology closed** |
| **Layer 2 — Historical strategy archaeology** | **Major reconstruction closed; targeted evidence only** |
| **Layer 3 — AEGIS architecture** | **Active; symbolic contract defined; numeric ABI blocked** |
| **Layer 4 — Runtime `.per` implementation** | **Blocked until package/ABI clearance** |

Permanent boundaries:

- Scenario-loader automation/testing is retired.
- XS is outside AEGIS scope.
- CaptureAge/CADE is secondary validation infrastructure.
- HD/Promisory is historical strategy evidence, not automatic runtime authority.
- Commands are not completion proof.
- Validator acceptance is not engine semantics.
- Apparently unused numeric channels are not automatically safe.

## Target runtime

Current engineering target: **AoE2DE `101.103.48987.0` / Update `#180059`**.

Authorized workstation evidence identifies:

- executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam BuildID: `24094652`

The current installed `resources\\_common\\ai` directory has been restored from Steam and is designated by the project owner as the **untouched stock-runtime baseline**. The next evidence action is to capture its immutable manifest and hashes. Do not modify that baseline during acquisition.

## Architecture

AEGIS is a stateful strategic controller:

```text
WORLD
  ↓
OBSERVE → CLASSIFY / BELIEVE → OBJECTIVE → REQUIREMENT
  ↓
CAPABILITY CANDIDATES → RESOURCE / TIMING EVALUATION
  ↓
COMMIT → AUTHORIZE → EXECUTE → VERIFY
  ↓
RESULT CLASSIFICATION → RECOVER / RE-ARBITRATE → REASSESS
```

The first executable vertical slice is **Cavalry Threat Containment**:

```text
enemy cavalry observation
→ threat classification
→ required camel capability
→ capability/resource check
→ producer selection
→ commitment
→ execution
→ postcondition verification
→ recovery/re-arbitration
→ reassessment
```

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

Major recovered motifs include measure-to-state compression, guard-before-side-effect, search-before-commitment, protected transitions/escrow, production as capability acquisition, threat-driven camel response, attack/retreat/restart lifecycle, geometric scouting, timers/persistent state, and fallback/recovery.

The project assessment is that the historical HD AI is a capable strategic controller, materially below a decent human player, rather than a toy ruleset. Static archaeology does not prove individual match outcomes.

## Repository organization

```text
03_HD_ARCHAEOLOGY/       Historical strategy/programmer archaeology
04_LAYER3_ARCHITECTURE/  Current AEGIS architecture and ABI work
05_RUNTIME_CANDIDATE/    Runtime/replay candidates and research instruments
07_EXPERIMENTS/          Experimental infrastructure when intentionally retained
12_RESEARCH/             External research and source provenance
knowledge/               Durable atomic institutional memory

docs/                    Governance, handoffs, QC, machine evidence, procedures
.github/                 Ownership and contribution controls
```

Do not renumber the historical directories. Their paths are part of provenance.

## Historical work

Failed experiments, earlier handoffs, and old branches are preserved because they contain negative results and explain architectural decisions. They are not current implementation authority.

See `docs/ARCHIVED_WORK_AND_BRANCHES_2026-09-05.md` for the disposition model.

## Immediate next gate

Do **not** begin `.per` implementation yet.

The next engineering sequence is:

`STOCK AI SNAPSHOT`
`→ IMPORT CLOSURE`
`→ SYMBOL / REFERENCE INVENTORY`
`→ CHANNEL OCCUPANCY`
`→ WRITER / READER MATRIX`
`→ ENGINE / VALIDATOR JOIN`
`→ ABI DECISIONS`
`→ ABI FREEZE`
`→ FIRST .per VERTICAL SLICE`

The project is now organized so that a future engineer or AI can recover the current state from GitHub without relying on conversational memory.
