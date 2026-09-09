# AiByz — AEGIS Byzantine AI Engineering Repository

> Professional research, reverse-engineering, architecture, and implementation repository for a next-generation Byzantine AI for Age of Empires II: Definitive Edition.

## AI ENTRY POINT — READ THIS FIRST

**If you are an AI taking over this project, do not begin by searching the entire repository at random.**

Start with:

1. **`AI_AGENT_START_HERE.md`** — project orientation, semantic traps, authority hierarchy, and what is already solved.
2. **`docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`** — definitive unresolved-proof register and next engineering sequence.
3. **`docs/architecture/AEGIS_STOCK_SUBSYSTEM_RECONSTRUCTION_MAP_2026-09-08.md`** — stock load/provenance/subsystem/ABI reconstruction.
4. `CANONICAL_AUTHORITY.md`
5. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`
6. `docs/CANONICAL_QC_2026-09-05.md`
7. `docs/REPOSITORY_AUTHORITY_MAP_2026-09-05.md`
8. `RESEARCH_INDEX.md`

**Do not treat older handoffs, experiments, or historical passes as competing current authorities.** They remain for evidence and provenance.

## Canonical status — 2026-09-09

**GitHub `main` is the authoritative starting point.**

The project has moved beyond broad archaeology. The current frontier is **machine-truth reconciliation and targeted runtime qualification**.

### Current engineering position

| Area | Status |
|---|---|
| Layer 1 — Machine/runtime broad archaeology | **89% — frozen; broad discovery closed** |
| Layer 2 — Historical strategy archaeology | **Major reconstruction closed; targeted evidence only** |
| Layer 3A — AEGIS architecture | **Closed for design; qualification active** |
| Stock subsystem/load reconstruction | **Substantially reconstructed** |
| ABI inventory | **Substantially reconstructed; allocation still gated** |
| Runtime lifecycle semantics | **Open** |
| Complete state ownership matrix | **Open** |
| Layer 4 — Production `.per` implementation | **Blocked until required machine/ABI gates clear** |

## Current frontier

The definitive remaining-proof register is `docs/FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md`.

The first unresolved gates are:

`R1 effective load/conditional closure`
`→ R2 complete mutable-state ownership`
`→ R3 numeric/typed ABI allocation`
`→ R4 initialization semantics`
`→ R5 command lifecycle semantics`

Then close only the runtime dependencies required by the first vertical slice:

`CAVALRY THREAT CONTAINMENT`

Do not reopen broad archaeology unless a dependency or contradiction requires it.

## Permanent boundaries

- Scenario-loader automation/testing is retired unless explicitly reopened.
- XS is outside AEGIS scope.
- CaptureAge/CADE is secondary validation infrastructure.
- HD/Promisory is historical strategy evidence, not automatic target-runtime authority.
- Commands are not completion proof.
- Validator acceptance is not engine semantics.
- Apparently unused numeric channels are not automatically safe.
- Embedded native test-harness capability is not proof of retail invocability.
- AoE2Control/invasive instrumentation is not AEGIS core runtime authority.
- `ADprom` and `byzwarcouncil` are failed/theoretical experiments, not production architecture.
- Experimental V2/V3/V4 architecture is not grandfathered into the final design.

## Target runtime

Current engineering target: **AoE2DE `101.103.48987.0` / Update `#180059`**.

Authorized workstation evidence identifies:

- executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- FileVersion: `101.103.48987.0`
- ProductVersion: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- Steam BuildID: `24094652`

The installed `resources\\_common\\ai` directory is designated as the **untouched stock-runtime baseline**. Never modify it during acquisition or qualification.

## Stock-system model

The repository now explicitly distinguishes three stock evidence layers:

1. **`AI (HD version).per`** — flattened behavioral controller and primary historical behavior body.
2. **Promisory source corpus** — decomposed source/provenance material; existence does not imply runtime loading.
3. **Active stock runtime substrate** — target load closure, chiefly `defaultConstants`, `finalingConstants`, and conditional `finaling`, with only proven nested imports.

The stock subsystem reconstruction map records this distinction and should be consulted before interpreting any Promisory file.

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

Mandatory state envelope:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Evidence ladder:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

## Evidence model

Machine/runtime authority:

`A1 exact installed target package/build`
`>` `A2 verified package snapshot`
`>` `A3 byte/content-equivalent repository snapshot`
`>` `A4 historical/source material`
`>` `A5 inference`

Runtime closure:

`W0 command only → W1 accepted/pending evidence → W2 world observation → W3 operational capability → W4 strategic effect`

Never promote a lower evidence level by intuition.

## First executable vertical slice

**Cavalry Threat Containment**:

```text
enemy observation
→ threat classification
→ required camel capability
→ resource/feasibility check
→ producer selection
→ commitment
→ execution
→ postcondition verification
→ recovery/re-arbitration
→ reassessment
```

Historical control evidence is strong. Target-build world/strategic realization is still a qualification task.

## Historical strategic reconstruction

The recovered historical model is:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION/BELIEF → REQUIREMENT → CAPABILITY CANDIDATES → RESOURCE/TIMING EVALUATION → COMMITMENT → AUTHORITY → ACTION → POSTCONDITION → FAILURE/RECOVERY → REASSESSMENT`

Major recovered motifs include measure-to-state compression, guard-before-side-effect, search-before-commitment, protected transitions/escrow, production as capability acquisition, threat-driven camel response, attack/retreat/restart lifecycle, geometric scouting, timers/persistent state, and fallback/recovery.

## Repository organization

```text
AI_AGENT_START_HERE.md   AI takeover/orientation contract
03_HD_ARCHAEOLOGY/       Historical strategy/programmer archaeology
04_LAYER3_ARCHITECTURE/  Current AEGIS architecture and ABI work
05_RUNTIME_CANDIDATE/    Runtime/replay candidates and research instruments
07_EXPERIMENTS/          Experimental infrastructure when intentionally retained
12_RESEARCH/             External research and source provenance
knowledge/               Durable atomic institutional memory

docs/                    Governance, handoffs, QC, machine evidence, procedures
.github/                 Ownership and contribution controls
```

Do not renumber historical directories; their paths are part of provenance.

## Historical work

Failed experiments, earlier handoffs, and old branches are preserved because they contain negative results and explain architectural decisions. They are not current implementation authority.

## Immediate next gate

Do **not** begin production `.per` implementation yet.

The current sequence is:

`CANONICAL CONSISTENCY`
`→ EFFECTIVE LOAD / CONDITIONAL GRAPH`
`→ COMPLETE RELEVANT STATE OWNERSHIP`
`→ ABI / NUMERIC ALLOCATION GATES`
`→ TARGETED RUNTIME LIFECYCLE PROBES`
`→ CAVALRY VERTICAL QUALIFICATION`
`→ ABI FREEZE`
`→ FIRST PRODUCTION .PER SLICE`

The repository is now explicitly organized so an AI can identify **what is authoritative, what is historical, what is obsolete, what is already solved, and what still has to be proven** without relying on conversational memory.
