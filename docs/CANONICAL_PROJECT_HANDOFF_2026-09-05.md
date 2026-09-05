# AiByz / AEGIS — Canonical Professional Engineering Handoff

**Date:** 2026-09-05  
**Repository:** `justhop90-bot/AiByz`  
**Canonical handoff branch:** `aegis/canonical-handoff-2026-09-05`  
**Canonical pre-handoff branch:** `aegis/layer2-hd-methodology-coding-2026-09-04` @ `d492ba1c776e2408f97fae0684402519b7635861`  
**Project authority:** GitHub repository state; this document supersedes conversational memory when conflicts exist.

## 1. Mission

Build AEGIS, a high-quality Byzantine AI for Age of Empires II: Definitive Edition. The intended system is a stateful strategic controller that observes the game, maintains bounded beliefs and commitments, derives capability requirements, evaluates feasible responses, executes through verified `.per` primitives, verifies world postconditions, recovers from failure, and reassesses.

AEGIS is not a transcription of HD/Promisory and is not a static build order.

## 2. Binding layer boundaries

### Layer 1 — Machine

Frozen at **89%**. Broad archaeology is closed. Scenario-loader automation/testing is permanently retired. Re-entry is permitted only when a specific implementation requirement needs one of the explicitly recorded closure targets.

### Layer 2 — HD / strategy archaeology

The major strategic reconstruction is effectively closed. The historical HD/Promisory source remains the archaeology authority; Layer-1 evidence remains the machine-semantics authority. Further Layer-2 work is permitted only for targeted evidence gaps that can change Layer-3 design.

### Layer 3 — Architecture

The current workstream. The symbolic first-slice architecture is defined and hostile-QC'd, but the numeric ABI is **not cleared**.

### Layer 4 — Runtime implementation

**0% / blocked by design** until the numeric ABI and target-build primitive evidence are cleared.

XS is permanently outside AEGIS scope.

## 3. Current architecture direction

The central AEGIS control chain is:

`ABSTRACT STRATEGIC NEED → CAPABILITY → FEASIBLE PLAN → VERIFIED AOE2DE RUNTIME PRIMITIVES → EXECUTION → POSTCONDITION → REASSESSMENT`

The first executable vertical slice is **Cavalry Threat Containment**:

`OBSERVE ENEMY → CLASSIFY CAVALRY THREAT → DEFINE CAMEL REQUIREMENT → CHECK CAPABILITY/RESOURCES → SELECT PRODUCER → COMMIT → EXECUTE → VERIFY → RECOVER/RE-ARBITRATE → REASSESS`

The architecture explicitly separates strategic vocabulary from AoE2DE runtime vocabulary and never treats command issuance as proof of world-state completion.

## 4. Current ABI gate

Passes 92–94 establish the first-slice symbolic contract and the deterministic allocation procedure.

Frozen symbolic fields:

`OBS.ENEMY_CAVALRY`  
`OBS.ENEMY_CAVALRY_AGE`  
`THREAT.CAVALRY_ACTIVE`  
`CAP.CAMEL_CURRENT`  
`CAP.CAMEL_REQUIRED`  
`CAP.CAMEL_DEFICIT`  
`CAND.PRODUCER`  
`CAND.STATUS`  
`COMMIT.VALID`  
`COMMIT.OWNER`  
`COMMIT.GEN`  
`COMMIT.STAGE`  
`EXEC.STAGE`  
`EXEC.EXPECTED_GEN`  
`RES.RESERVED`  
`RES.DISCRETIONARY`  
`ARB.EPOCH`  
`ARB.DIRTY`  
`VERIFY.LEVEL`

This is provisionally 16 goal-like fields + 3 flags. The representation may change only through an explicit ABI decision if authoritative inventory proves a safer native channel.

### Numeric ABI status

**BLOCKED.** Do not invent goal/SN/flag/timer numbers from apparent gaps or partial source inspection.

Required authority hierarchy:

`A1 exact installed target package/build > A2 verified package snapshot > A3 byte/content-equivalent repository snapshot > A4 historical/source material > A5 inference`

Only A1–A3 can clear a numeric allocation.

## 5. Deterministic ABI audit

Pass 94 defines the required pipeline:

`TARGET PACKAGE → IMMUTABLE SNAPSHOT → FILE MANIFEST → SYMBOL EXTRACTION → REFERENCE EXTRACTION → CHANNEL NORMALIZATION → COLLISION JOIN → WRITER/READER MATRIX → BUILD/VALIDATOR JOIN → ABI DECISION`

Non-negotiable invariants:

- parser failure is not absence;
- numeric equality across channels is not identity;
- declaration is not import closure;
- validator acceptance is not engine semantics;
- engine documentation is not validator acceptance;
- A5 inference cannot produce `CLEAR`;
- allocation is reproducible from immutable inputs;
- no `.per` source is changed by the audit itself.

Required machine-readable outputs are specified in Pass 94 and include snapshot manifest, symbol/reference inventories, import closure, channel occupancy, writer/reader matrix, validator findings, build profile, candidates, decisions, audit report, and run hash manifest.

## 6. Build identity

Project evidence repeatedly fingerprints the target as **AoE2DE `101.103.48987.0` / Update #180059**. This is the current target build for engineering purposes.

Important qualification: the replay/build fingerprint and public update evidence are not a substitute for an A1 installed-executable capture. Until the exact installed executable/version/hash is recorded from the authorized workstation, the build remains a target identity rather than a fully cleared A1 machine fact.

## 7. Workstation status

Authorized workstation: **Weebo** (`1aa2f154-9f15-4d83-94d1-dd0121f6bd29`).

The project has established that the device can report online/ping successfully, while the remote process/filesystem execution channel has intermittently failed with `Not connected`. A successful connection must capture the exact executable/version/hash and the live `resources\\_common\\ai` package before numeric ABI clearance.

Do not mark A1 complete merely because Weebo is online.

## 8. Evidence discipline

Evidence grades:

- **E0 / DIRECT:** directly observed in authoritative source or snapshot.
- **E1 / COMPOSED:** deterministic derivation from direct evidence.
- **E2 / AEGIS-GENERALIZATION:** new architecture derived from evidence.
- **E3 / HYPOTHESIS:** open or weakly supported.

Strategic closure and runtime closure are separate:

`CONTROL → WORLD → STRATEGIC`

A command can be controllably issued without proving that the world changed, and a world change can occur without proving strategic success.

## 9. Historical strategic model retained

The strongest durable reconstruction is:

`GAME PROBLEM → OBSERVATION → CLASSIFICATION/BELIEF → REQUIREMENT → CAPABILITY CANDIDATES → RESOURCE/TIMING EVALUATION → COMMITMENT → AUTHORITY → ACTION → POSTCONDITION → FAILURE/RECOVERY → REASSESSMENT`

Historical motifs directly supported by the archaeology include measure-to-state compression, guard-before-side-effect, search-before-commitment, escrow/protected transitions, production as a capability pipeline, threat-state/camel response, attack/retreat/restart lifecycle, geometric scouting, timers/persistent state, and fallback/recovery behavior.

Do not describe HD/Promisory as strategically empty. The project assessment is that it is a capable bot with meaningful strategic structure, materially below a decent human player. Static source alone cannot prove a particular match outcome.

## 10. Replay and CADE disposition

Reference replay evidence remains useful for corroboration. The normalized replay corpus and minimal deterministic interpreter intentionally preserve uncertainty around BUILD/DE_QUEUE/RESEARCH/DELETE lifecycle completion.

CaptureAge/CADE remains a **secondary validation adapter candidate**, not a primary research dependency. Scenario-loader automation remains retired.

## 11. Hostile-QC findings that remain binding

The following shortcuts are prohibited:

- arbitrary unused numeric ABI allocation;
- treating goals/SNs/flags/timers as interchangeable namespaces;
- equating rule order with ownership without evidence;
- assuming atomic handoff/transaction semantics;
- treating `sn-resource-control` as a universal mutex;
- treating `uniqueId` as a proven persistent entity ID;
- treating replay command order as proof of causal intent;
- treating deficit zero as objective success;
- treating candidate selection as an optimizer without an explicit policy;
- treating command issuance as completion;
- collapsing mechanical unit class into strategic role;
- silently aliasing or remapping legacy state;
- allowing parser convenience or validator behavior to become engine truth.

## 12. Next executable engineering action

The next pass is **authoritative package acquisition and ABI clearance**, not more abstract architecture.

Required sequence:

1. Capture exact installed AoE2DE executable/version/hash on Weebo.
2. Snapshot the exact imported AI package without mutation.
3. Resolve entrypoint/import closure.
4. Extract declarations, reads, writes, timers, flags, searches, aliases, and control topology.
5. Build channel occupancy maps and legacy overlap decisions.
6. Join engine, validator, and AEGIS status independently.
7. Produce the 19-field allocation candidate set.
8. Clear or reject each field deterministically.
9. Freeze the resulting numeric ABI as the sole implementation allocation source.
10. Only then begin the first `.per` vertical slice.

## 13. Authority rule for future engineers/models

When conversational memory conflicts with GitHub, **GitHub wins**.

When two GitHub documents conflict, prefer the newer committed artifact only after checking whether it explicitly supersedes the older one. Evidence-grade rules still apply.

When a current machine fact conflicts with an older repository statement, create a dated correction artifact, preserve the old evidence, and update the canonical status rather than silently rewriting history.

No research result is considered durable unless it is committed and verifiable in GitHub.

## 14. Canonical reading order

1. This document.
2. `docs/CANONICAL_QC_2026-09-05.md`.
3. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`.
4. `04_LAYER3_ARCHITECTURE/PASS93_AUTHORITATIVE_ABI_INVENTORY_SPEC_2026-09-05.md`.
5. `04_LAYER3_ARCHITECTURE/PASS92_ABI_FINALIZATION_AND_ALLOCATION_GATE_2026-09-05.md`.
6. `04_LAYER3_ARCHITECTURE/PASS91_CROSS_MODULE_CONTRACT_MATRIX_2026-09-05.md`.
7. `04_LAYER3_ARCHITECTURE/PASS91_FAILURE_TOPOLOGY_AND_INTEGRATION_TEST_PLAN_2026-09-05.md`.
8. `03_HD_ARCHAEOLOGY/PASS87_END_TO_END_EVIDENCE_GRAPH_2026-09-05.md`.
9. `docs/PROJECT_HANDOFF_2026-09-04.md` for historical handoff context.

## 15. Handoff verdict

**Project is professionally handoff-ready at the repository/evidence level.**

**Architecture is sufficiently specified for numeric ABI acquisition.**

**Numeric ABI is not cleared.**

**Runtime implementation is intentionally blocked until the ABI/build gates are satisfied.**

**GitHub is the authoritative project record.**
