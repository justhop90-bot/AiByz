# AEGIS Typed Goal / Strategic-Number / Timer ABI Manifest

**Date:** 2026-09-11  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Scope:** all 49 files currently present under `main/AegisProm`  
**Purpose:** authoritative working inventory of AEGIS-owned numeric Goal/SN/Timer channels; not runtime qualification.

## 1. Binding interpretation

The current AI Scripting Encyclopedia is internally inconsistent in its summary text, but its detailed Goals section and UserPatch documentation establish the conservative ABI used here: standard AI goals are 1–512; Goals 1–40 cannot be used with several extended-output commands; goals 509–512 are unsafe for four-goal extended commands; extended cost-data heads are 41–508. Strategic numbers are 0–511; timers are 1–50. Therefore this manifest treats Goal IDs >512 as **ABI-UNQUALIFIED**, not automatically invalid forever: target-build evidence would be required to clear any extension. citeturn2search0turn2search3

The key distinction is **typed ABI**. A number reused by a Goal, SN, unit ID, order ID, class ID, etc. is not automatically a collision because command parameters carry expected types. The Encyclopedia explicitly describes parameter typing and `GoalId` as a distinct parameter type. citeturn2search5turn2search7

`up-get-search-state` writes four consecutive goals, so a head goal must have sufficient following goal slots. The documented extended-goal range for four-goal cost operations is 41–508; the same four-slot safety principle applies to search-state use. citeturn2search1turn2search3

## 2. Executive result

- **AegisProm files audited:** 49/49.
- **AEGIS-owned state Goal channels at or below 512:** 162.
- **AEGIS-owned state Goal channels above 512:** 164 — **ABI-UNQUALIFIED** under the conservative target-build gate.
- **AEGIS-owned custom Strategic Numbers:** 0 direct `set-strategic-number`/`strategic-number` uses found in the 49 AegisProm files.
- **Timer symbols:** 4 defined/used: 42, 43, 60, 300.
- **Timer IDs 42 and 43:** within the documented 1–50 timer range.
- **Timer IDs 60 and 300:** **ABI-INVALID** as timer IDs and must not remain as timer channels.
- **Stock SN definitions:** present in `AEGIS-stock-defaultConstants`; these are imported engine symbols, not AEGIS-owned custom SN allocations.
- **Worker target-selection hard defect:** `local-total` is used as a Goal identifier but is not defined under that exact name; stock finaling defines `gl-local-total` instead. This is independent of the numeric ABI issue.
- **Worker target-selection numeric defect:** `aegis-wts-needed=514`, `selected=515`, `observed-at=516`, `cycle=517`, `candidates=518` are above the conservative 512 Goal ABI boundary.

## 3. Complete 49-module manifest

Status codes:
- **STOCK** — imported stock/finaling ABI definitions; not an AEGIS allocation.
- **VALID-CANDIDATE** — numeric Goal channel is within 1–512, but still requires collision/ownership/runtime clearance before production use.
- **UNQUALIFIED>512** — AEGIS Goal channel above the conservative 512 Goal ABI boundary.
- **TIMER-VALID-CANDIDATE** — timer ID 1–50; still requires ownership/runtime clearance.
- **TIMER-INVALID** — timer ID outside 1–50.
- **NONE** — module owns no Goal/SN/Timer channels.

| # | Module | Typed ABI channels | Status |
|---:|---|---|---|
| 1 | `Aegis-belief-final.per` | Goals 340–343: generation, valid, threat, confidence | VALID-CANDIDATE |
| 2 | `AEGIS-Carpenter-final.per` | Goals 330–332: sensor-pass, runtime-ok, generation | VALID-CANDIDATE |
| 3 | `AEGIS-cavalry-response-v0.per` | Goals 620–624: generation, valid, stage, attempts, baseline | UNQUALIFIED>512 |
| 4 | `AEGIS-civilian-census-v0.per` | Timer 42; Goals 433–440: generation, valid, stage, villagers, town-centers, pending-villagers, observed-at, cycle | VALID-CANDIDATE + TIMER-VALID-CANDIDATE |
| 5 | `AEGIS-civilian-demand-v0.per` | Goals 421–426: demand-generation, villager-demand, housing-demand, urgency, stage, observed-at | VALID-CANDIDATE |
| 6 | `AEGIS-civilian-lifecycle-reconciler-v0.per` | Goals 441–449: generation, valid, stage, baseline-villagers, observed-villagers, pending, confirmed-delta, attempts, observed-at | VALID-CANDIDATE |
| 7 | `AEGIS-civilization-state-v0.per` | Goals 403–420: generation, valid, stage, observed-at, cycle, time, population, population-cap, age, food, wood, gold, spear, camel, skirm, cavalry, archers, focus-player | VALID-CANDIDATE |
| 8 | `Aegis-commitment-final.per` | Goals 390–392: generation, valid, kind | VALID-CANDIDATE |
| 9 | `Aegis-decision-final.per` | Goals 380–382: generation, valid, approve | VALID-CANDIDATE |
| 10 | `AEGIS-dynamic-worker-loop-probe-v0.per` | Timer 60; Goals 560–563: trigger, observed, stage, cycle | TIMER-INVALID + UNQUALIFIED>512 |
| 11 | `AEGIS-economic-demand-arbitration-v0.per` | Goals 490–497: generation, valid, stage, selected-resource, selected-deficit, priority, urgency, observed-at | VALID-CANDIDATE |
| 12 | `AEGIS-economic-demand-v0.per` | Goals 479–489: generation, valid, stage, food-demand, wood-demand, gold-demand, stone-demand, priority, urgency, observed-at, cycle | VALID-CANDIDATE |
| 13 | `Aegis-economy-final.per` | Goals 583–587: generation, valid, food-pressure, wood-pressure, gold-pressure | UNQUALIFIED>512 |
| 14 | `Aegis-execution-final.per` | Goals 395–397: generation, valid, stage | VALID-CANDIDATE |
| 15 | `AEGIS-foundation.per` | Timer 300; Goals 301–319: valid, generation, stage, observed-at, cycle, time, population, population-cap, age, food, wood, gold, spear, camel, skirm, cavalry, archers, focus-player, evidence | TIMER-INVALID + VALID-CANDIDATE |
| 16 | `AEGIS-housing-construction-v0.per` | Goals 570–578: generation, valid, stage, baseline-houses, observed-houses, pending, attempts, observed-at, failure | UNQUALIFIED>512 |
| 17 | `AEGIS-integration-candidate-v0.per` | No Goal/SN/Timer channels | NONE |
| 18 | `AEGIS-micro-control-v0.per` | Goals 670–677: generation, valid, stage, intent, target-ready, observed, failure, attempts | UNQUALIFIED>512 |
| 19 | `AEGIS-micro-execution-bridge-v0.per` | Goals 730–733: generation, valid, authorized, purpose | UNQUALIFIED>512 |
| 20 | `AEGIS-micro-geometry-v0.per` | Goals 700–708: generation, valid, target-ready, fallback-ready, target-x, target-y, distance, pivot, stage | UNQUALIFIED>512 |
| 21 | `AEGIS-micro-governor-v0.per` | Goals 710–716: generation, valid, command, epoch, age, expected, reissue | UNQUALIFIED>512 |
| 22 | `AEGIS-micro-groups-v0.per` | Goals 690–699: generation, valid, frontline, anticav, ranged, siege, reserve, damaged, screen, pursuit | UNQUALIFIED>512 |
| 23 | `AEGIS-micro-physical-adapter-v0.per` | No locally defined Goal/SN/Timer channels; consumes upstream Goals | NONE |
| 24 | `AEGIS-micro-state-v0.per` | Goals 680–689: generation, valid, stage, friendly, enemy, cav-risk, advantage, retreat-risk, state, observed-at | UNQUALIFIED>512 |
| 25 | `AEGIS-micro-targeting-v0.per` | No locally defined Goal/SN/Timer channels; consumes upstream Goals | NONE |
| 26 | `AEGIS-micro-verification-v0.per` | Goals 720–726: generation, valid, stage, result, observed, failure, attempts | UNQUALIFIED>512 |
| 27 | `Aegis-military-final.per` | Goals 588–591: generation, valid, ready, threat | UNQUALIFIED>512 |
| 28 | `AEGIS-military-production-v0.per` | Goals 630–637: generation, valid, stage, unit, attempts, baseline, observed, pending | UNQUALIFIED>512 |
| 29 | `Aegis-objectives-final.per` | Goals 360–362: generation, valid, kind | VALID-CANDIDATE |
| 30 | `AEGIS-operations-final.per` | Goals 592–594: generation, valid, cycle | UNQUALIFIED>512 |
| 31 | `Aegis-planning-final.per` | Goals 370–373: generation, valid, kind, stage | VALID-CANDIDATE |
| 32 | `Aegis-recovery-final.per` | Goals 580–582: generation, valid, attempts | UNQUALIFIED>512 |
| 33 | `AEGIS-research-age-v0.per` | Goals 600–605: generation, valid, stage, attempts, baseline-age, observed-age | UNQUALIFIED>512 |
| 34 | `AEGIS-scouting-threat-v0.per` | Goals 610–617: generation, valid, enemy-age, cavalry, cavalry-archer, knight, threat, confidence | UNQUALIFIED>512 |
| 35 | `Aegis-situation-final.per` | Goals 350–352: generation, valid, state | VALID-CANDIDATE |
| 36 | `AEGIS-source-dropsite-serviceability-v0.per` | Goals 499–507: generation, valid, stage, resource, source-count, serviceable, failure, observed-at, cycle | VALID-CANDIDATE |
| 37 | `AEGIS-stock-defaultConstants.per` | Defines stock Goal/SN/object/class constants; no AEGIS-owned Goal/SN/Timer allocation | STOCK |
| 38 | `AEGIS-stock-finalingConstants.per` | Defines stock/finaling Goals 98–115 plus many typed object/research constants; no AEGIS-owned SN/Timer allocation | STOCK |
| 39 | `AEGIS-threat-recovery-v0.per` | Goals 650–656: generation, valid, stage, underattack, enemy-town, retreat, observed-at | UNQUALIFIED>512 |
| 40 | `Aegis-verification-final.per` | Goals 398–400: generation, valid, observed | VALID-CANDIDATE |
| 41 | `AEGIS-villager-production-v0.per` | Goals 427–432: generation, valid, stage, action, attempts, observed | VALID-CANDIDATE |
| 42 | `AEGIS-worker-loop-qualification-v0.per` | Goals 555–559: generation, valid, stage, progress, cycle | UNQUALIFIED>512 |
| 43 | `AEGIS-worker-productivity-observer-v0.per` | Goals 526–533: generation, valid, stage, resource, observed, failure, observed-at, cycle | UNQUALIFIED>512 |
| 44 | `AEGIS-worker-recovery-v0.per` | Goals 546–554: generation, valid, stage, resource, failure, attempts, disposition, observed-at, cycle | UNQUALIFIED>512 |
| 45 | `AEGIS-worker-role-census-v0.per` | Timer 43; Goals 450–464: generation, valid, stage, food, forager, shepherd, hunter, fisherman, farmer, wood, gold, stone, builder, observed-at, cycle | VALID-CANDIDATE + TIMER-VALID-CANDIDATE |
| 46 | `AEGIS-worker-role-vector-v0.per` | Goals 465–478: generation, valid, stage, desired-food/wood/gold/stone/builder, deficit-food/wood/gold/stone/builder, observed-at | VALID-CANDIDATE |
| 47 | `AEGIS-worker-target-selection-v0.per` | Goals 510–518: generation, valid, stage, resource, needed, selected, observed-at, cycle, candidates | 510–512 simple-only candidate; 513–518 UNQUALIFIED>512 |
| 48 | `AEGIS-worker-task-command-v0.per` | Goals 519–525: generation, valid, stage, resource, attempts, action, observed-at | UNQUALIFIED>512 |
| 49 | `AEGIS-worker-task-verification-v0.per` | Goals 534–545: generation, valid, stage, resource, worker-visible, task-visible, target-visible, carry-visible, result, failure, observed-at, cycle | UNQUALIFIED>512 |

## 4. Strategic-number ABI

**AEGIS-owned custom SN allocation: none.** AegisProm contains no direct `set-strategic-number` or `strategic-number` uses in the 49-file audit. The stock-default constants file defines the engine's named SN registry, including the current stock symbols in the 242–295 range. Those are **stock engine controls**, not AEGIS-owned storage.

The Encyclopedia documents 512 SN IDs, 0–511, and recommends custom use starting at SN 510 and descending because DE may add SNs; SN 511 has known DE bugs. This is a candidate policy, not a production clearance. citeturn2search2

**AEGIS rule:** do not allocate a custom SN until the exact target-build SN registry has been reconciled against the installed stock constants and target behavior. If we later need custom SN storage, candidate IDs begin at 510 and descend, with 511 excluded pending explicit target-build evidence.

## 5. Timer ABI

| Timer symbol | ID | Owner | Status | Reason |
|---|---:|---|---|---|
| `aegis-census-timer` | 42 | civilian census | TIMER-VALID-CANDIDATE | 42 is within documented 1–50 range |
| `aegis-wrc-timer` | 43 | worker-role census | TIMER-VALID-CANDIDATE | 43 is within documented 1–50 range |
| `aegis-dp-timer` | 60 | dynamic worker-loop probe | TIMER-INVALID | documented timer IDs stop at 50 |
| `aegis-wm-timer` | 300 | foundation/world model | TIMER-INVALID | documented timer IDs stop at 50 |

The timer IDs are distinct from the numeric seconds passed to `enable-timer`; the invalidity here concerns the first timer-ID argument. The actual uses were inspected in the installed AegisProm corpus.

## 6. Goal-space occupancy and candidate policy

Current AEGIS-owned Goal channels at or below 512 occupy:

`301–319, 330–343, 350–352, 360–362, 370–373, 380–382, 390–392, 395–400, 403–440, 441–449, 450–478, 479–489, 490–497, 499–507, 510–512`.

That is **162 occupied AEGIS state Goal IDs** in the conservative 1–512 space. The gaps inside this space are candidates only; they are not cleared allocations.

Current AEGIS-owned channels above 512 occupy:

`513–518, 519–525, 526–533, 534–545, 546–554, 555–559, 560–563, 570–578, 580–582, 583–587, 588–594, 600–605, 610–617, 620–624, 630–637, 650–656, 670–677, 680–689, 690–699, 700–708, 710–716, 720–726, 730–733`.

These **164 channels are not promoted**. They require either migration into cleared Goal space or exact target-build evidence establishing an extended goal ABI.

## 7. Critical findings exposed by this manifest

### P0 — Worker target-selection ABI overflow
`aegis-wts-needed=514` is not safe under the conservative 512-goal ABI. `aegis-wts-selected=515`, `observed-at=516`, `cycle=517`, and `candidates=518` are likewise above the standard boundary. The module also uses `local-total` without defining that exact identifier. `AEGIS-stock-finalingConstants` defines `gl-local-total=106`; an identifier is not inferred merely because a similarly named symbol exists.

### P0 — Timer overflow
`aegis-dp-timer=60` and `aegis-wm-timer=300` are invalid timer IDs under the documented 1–50 timer ABI. They must be migrated to owned timer IDs in 1–50 before runtime qualification.

### P1 — Extended-goal heads must be audited by command
Any AEGIS goal used as the head of `up-get-search-state`, point, cost-data, guard-state, or similar multi-goal operations must have sufficient consecutive goal space. The Encyclopedia documents `up-get-search-state` as a four-goal output and the UserPatch notes explicitly restrict four-goal cost-data heads to 41–508. citeturn2search1turn2search3

### P1 — Numeric equality is not cross-type collision
The manifest intentionally does **not** treat every equal integer as a collision. For example, Goal 620 and stock action ID 620 are different typed operands. The Encyclopedia's parameter model explicitly distinguishes GoalId, SN, ActionId, OrderId, ClassId, etc. citeturn2search5turn2search7

## 8. Immediate engineering disposition

1. Freeze all runtime promotion claims for modules using Goal IDs >512.
2. Do not blindly compress the modules yet.
3. Build a second-pass **command-width map** identifying every multi-goal output head and its required contiguous span.
4. Reserve a contiguous AEGIS Goal bank inside the verified 1–512 space.
5. Migrate >512 state channels into that bank with a generated symbol-renaming map.
6. Replace timer IDs 60 and 300 with verified 1–50 timer slots.
7. Correct undefined identifier `local-total` to the explicitly defined/owned symbol only after tracing its intended writer/reader semantics; do not perform a cosmetic rename.
8. Re-run the package validator after migration.
9. Only then resume manual target-runtime loading.

## 9. Evidence boundary

This manifest establishes **static source facts and documented ABI constraints**. It does not establish that any AEGIS Goal/SN/Timer channel has been accepted, initialized, written, read, or persisted correctly by the target engine. Runtime qualification remains a separate gate.

The project ABI policy remains binding: numeric vacancy is not permission, historical/inferred evidence does not clear a production allocation, and every channel needs typed ownership plus evidence before promotion. fileciteturn264file0

## 10. Primary references

- AoE2 AI Scripting Encyclopedia — Data Limits: goals, SNs, timers, extended-goal restrictions. citeturn2search0
- AoE2 AI Scripting Encyclopedia — Commands Index: `up-get-search-state` and other GoalId outputs. citeturn2search1
- AoE2 AI Scripting Encyclopedia — SN Index: SN 0–511 and custom-SN guidance. citeturn2search2
- UserPatch Patch Notes — four-goal extended-cost-data head range 41–508. citeturn2search3
- AoE2 AI Scripting Encyclopedia — Parameter Index / command typing. citeturn2search5turn2search7
- Repository ABI allocation policy: `docs/progress/03_ABI_ALLOCATION_POLICY_2026-09-09.md`. fileciteturn264file0
