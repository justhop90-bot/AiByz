# AiByz / AEGIS — Canonical Professional Engineering Handoff

**Effective:** 2026-09-05
**Repository:** `justhop90-bot/AiByz`
**Canonical branch:** `main`
**Status:** authoritative starting record

> This document is the current handoff. The previous version is preserved in Git history. The key correction is that the installed AoE2DE AI directory has now been explicitly designated by the project owner as a restored, untouched stock Steam baseline.

## 1. Mission

Build AEGIS, a high-quality Byzantine AI for Age of Empires II: Definitive Edition. AEGIS is intended to be a stateful strategic controller that observes the game, maintains bounded beliefs and commitments, derives capability requirements, evaluates feasible responses, executes through verified `.per` primitives, verifies world postconditions, recovers from failure, and reassesses.

AEGIS is not a transcription of HD/Promisory and is not a static build order.

## 2. Current layer status

| Layer | Status | Authority |
|---|---|---|
| Layer 1 — Machine/runtime | **89%, frozen for handoff** | Current target-build evidence |
| Layer 2 — HD/strategy archaeology | **Major reconstruction closed; targeted evidence only** | Historical HD/Promisory source |
| Layer 3 — AEGIS architecture | **Active; symbolic contract defined; numeric ABI blocked** | Current architecture passes |
| Layer 4 — Runtime implementation | **Blocked by design** | Cleared only after ABI gate |

Permanent boundaries:

- Scenario-loader automation/testing is retired.
- XS is outside AEGIS scope.
- CADE is secondary validation infrastructure.
- Historical source is evidence, not automatic implementation authority.
- Commands are not completion proof.
- Validator acceptance is not engine semantics.
- Apparent numeric gaps are not safe ABI allocation.

## 3. Current target build

The authorized workstation capture identifies:

- executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam BuildID: `24094652`
- Update: `#180059`

This is the current A1 executable identity for the engineering target.

## 4. Current stock AI package baseline

The project owner has restored the complete directory:

`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

from Steam and states that it has not been modified since restoration.

**Disposition: CURRENT STOCK-RUNTIME BASELINE.**

This correction supersedes older repository language suggesting that the installed AI tree was necessarily contaminated or that the live package had not been acquired. Names appearing inside this restored directory — including `Promisory`, `AiBuilder`, or `testharness` — are not evidence of project modification by themselves.

The directory is evidence to be captured, not edited. The next pass must produce an immutable file manifest, hashes, entrypoint record, and recursive import closure from this exact tree.

## 5. Architecture

The central AEGIS control chain is:

`WORLD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT → CAPABILITY → COMMIT → AUTHORIZE → EXECUTE → VERIFY → RESULT CLASSIFICATION → RECOVER/RE-ARBITRATE → REASSESS`

The first executable vertical slice is **Cavalry Threat Containment**:

`OBSERVE ENEMY → CLASSIFY CAVALRY THREAT → DEFINE CAMEL REQUIREMENT → CHECK CAPABILITY/RESOURCES → SELECT PRODUCER → COMMIT → EXECUTE → VERIFY → RECOVER/RE-ARBITRATE → REASSESS`

Mandatory state envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

## 6. ABI gate

The symbolic first-slice contract is defined by Passes 92–94. The numeric ABI remains blocked until current package inventory is complete.

Authority hierarchy:

`A1 exact installed target package/build > A2 verified package snapshot > A3 byte/content-equivalent repository snapshot > A4 historical/source > A5 inference`

Only A1–A3 can clear numeric allocation.

Required deterministic sequence:

`TARGET PACKAGE → IMMUTABLE SNAPSHOT → FILE MANIFEST → SYMBOL EXTRACTION → REFERENCE EXTRACTION → CHANNEL NORMALIZATION → COLLISION JOIN → WRITER/READER MATRIX → BUILD/VALIDATOR JOIN → ABI DECISION`

Non-negotiable rules:

- parser failure is not absence;
- numeric equality across channels is not identity;
- declaration is not import closure;
- validator acceptance is not engine semantics;
- engine documentation is not validator acceptance;
- A5 inference cannot produce `CLEAR`;
- allocation must be reproducible from immutable inputs;
- the audit must not modify the stock baseline.

## 7. Historical strategic reconstruction

The recovered historical model is:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION/BELIEF → REQUIREMENT → CAPABILITY CANDIDATES → RESOURCE/TIMING EVALUATION → COMMITMENT → AUTHORITY → ACTION → POSTCONDITION → FAILURE/RECOVERY → REASSESSMENT`

Major evidence-backed motifs include measure-to-state compression, guard-before-side-effect, search-before-commitment, protected transitions/escrow, production as capability acquisition, threat-driven camel response, attack/retreat/restart lifecycle, geometric scouting, timers/persistent state, and fallback/recovery.

The project assessment is that the historical HD AI is a capable strategic controller, materially below a decent human player. Static source archaeology does not prove individual match outcomes.

## 8. Evidence discipline

Use these distinctions:

- **DIRECT:** directly observed in authoritative source or snapshot.
- **COMPOSED:** deterministic composition of direct evidence.
- **AEGIS-GENERALIZATION:** project-owned design derived from evidence.
- **HYPOTHESIS:** unresolved interpretation.

Keep closure separate:

`CONTROL → WORLD → STRATEGIC`

Do not collapse a command, a world transition, and a strategic result into one claim.

## 9. Repository organization

```text
03_HD_ARCHAEOLOGY/       Historical strategy/programmer archaeology
04_LAYER3_ARCHITECTURE/  Current AEGIS architecture and ABI work
05_RUNTIME_CANDIDATE/    Runtime/replay candidates and research instruments
07_EXPERIMENTS/          Experimental infrastructure
12_RESEARCH/             External research and source provenance
knowledge/               Durable atomic institutional memory

docs/                    Governance, handoffs, QC, evidence, procedures
.github/                 Ownership and contribution controls
```

Historical directory numbering is retained for path stability and provenance.

## 10. Historical work

Older handoffs, QC passes, experimental branches, and failed approaches are retained because they explain how the project arrived here. They are not alternate authority.

See `docs/ARCHIVED_WORK_AND_BRANCHES_2026-09-05.md`.

## 11. Immediate next engineering action

Do not begin `.per` implementation yet.

Execute:

1. Snapshot the restored stock `resources\\_common\\ai` tree without mutation.
2. Record file sizes, hashes, timestamps, and acquisition metadata.
3. Identify the actual AI entrypoint.
4. Resolve recursive load/import closure.
5. Extract declarations, reads, writes, timers, flags, searches, aliases, and control topology.
6. Build channel occupancy and legacy-overlap maps.
7. Join engine semantics, validator behavior, and AEGIS design status independently.
8. Produce ABI candidates and deterministic clear/reject decisions.
9. Freeze the numeric ABI.
10. Only then write the first production `.per` vertical slice.

## 12. Handoff rule

A future engineer/model starts from `main`, not from an arbitrary branch, PR, or old handoff.

When a current machine observation corrects an older document, the correction is committed explicitly and the older record remains recoverable in Git history.

**Current starting point:** stock package acquisition and ABI clearance.
