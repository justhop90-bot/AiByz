# AEGIS Repository-Wide Goal Namespace Map — 2026-09-11

**Authority:** `main/AegisProm` source
**Scope:** shared AegisProm `.per` goal namespace
**Status:** NORMATIVE / COLLISION REPAIR + REASSESSMENT + AUTHORIZATION BASELINE

## 1. Namespace rule

All numeric `defconst` goal identifiers in loaded AegisProm source share one engine goal namespace. A numeric slot therefore belongs to exactly one semantic field across the repository.

Rules:
1. Source under `main/AegisProm` is authoritative for AEGIS architecture.
2. `runtime/` copies do not reserve or define source goal ownership.
3. A symbol rename without numeric relocation does not repair a collision.
4. A numeric relocation preserves symbol, semantic owner, and references.
5. Lifecycle work must not allocate into an occupied slot.
6. Every new goal must be registered before source promotion.
7. Local enum values are not goal-slot allocations unless used by `defconst` goal fields.

## 2. Authoritative allocations

| Numeric block | Owner | Source | Purpose | Status |
|---|---|---|---|---|
| 490–497 | EDA | `AEGIS-economic-demand-arbitration-v0.per` | economic arbitration state + request identity | ACTIVE |
| 510–518 | WTS | `AEGIS-worker-target-selection-v0.per` | worker target-selection state | ACTIVE |
| 519–530 | WTC | `AEGIS-worker-task-command-v0.per` | worker physical task command + authorization | ACTIVE |
| 534–545 | WTV | `AEGIS-worker-task-verification-v0.per` | worker task verification state | ACTIVE |
| 546–549 | WR | `AEGIS-worker-recovery-v0.per` | recovery lifecycle base state | ACTIVE |
| 550–551 | EDA/WTS | EDA/WTS sources | request identities | ACTIVE / EXCLUSIVELY OWNED |
| 552–554 | WR | `AEGIS-worker-recovery-v0.per` | recovery disposition/observation/cycle | ACTIVE |
| 555–556 | WR | `AEGIS-worker-recovery-v0.per` | repaired failure + attempt fields | ACTIVE / REPAIRED |
| 560–561 | WTV | `AEGIS-worker-task-verification-v0.per` | repaired verification request/authorization identity | ACTIVE / REPAIRED |
| 562–566 | WLQ | `AEGIS-worker-loop-qualification-v0.per` | qualification heartbeat state | CANDIDATE / REPAIRED |
| 570–585 | HC | `AEGIS-housing-construction-v0.per` | housing lifecycle + request/authorization/evidence | ACTIVE |
| 600–612 | RA | `AEGIS-research-age-v0.per` | age-transition lifecycle + request/authorization/evidence | ACTIVE |
| 620–629 | CR | `AEGIS-cavalry-response-v0.per` | anti-cavalry lifecycle + request/authorization | ACTIVE |
| 630–637 | MP | `AEGIS-military-production-v0.per` | military-production candidate lifecycle | ACTIVE / CANDIDATE BLOCKED |
| 638–641 | CR | `AEGIS-cavalry-response-v0.per` | repaired spearman evidence | ACTIVE / REPAIRED |
| 642–649 | ST | `AEGIS-scouting-threat-v0.per` | repaired threat-observation state | ACTIVE / REPAIRED |
| 650 | CR | `AEGIS-cavalry-response-v0.per` | repaired failure state | ACTIVE / REPAIRED |
| 670–677 | MC | `AEGIS-micro-control-v0.per` | tactical micro control state | ACTIVE |
| 680–689 | MS | `AEGIS-micro-state-v0.per` | tactical micro force/state observation | ACTIVE |
| 690–699 | MG | `AEGIS-micro-groups-v0.per` | tactical micro groups | ACTIVE |
| 700–709 | MGeo | `AEGIS-micro-geometry-v0.per` | tactical geometry | ACTIVE |
| 710–716 | MG3 | `AEGIS-micro-governor-v0.per` | tactical command governor | ACTIVE |
| 720–726 | MV | `AEGIS-micro-verification-v0.per` | tactical verification state | ACTIVE |
| 730–739 | ME | `AEGIS-micro-execution-bridge-v0.per` | tactical execution authorization | ACTIVE |
| 734–735 | MC | `AEGIS-micro-control-v0.per` | stable tactical request identity | ACTIVE / RANGE PARTITION |
| 736–739 | ME | `AEGIS-micro-execution-bridge-v0.per` | tactical authorization identity/generation/expiry | ACTIVE |
| 740–743 | MV | `AEGIS-micro-verification-v0.per` | tactical request/auth/world/causal evidence | ACTIVE |
| 760–761 | WTV | `AEGIS-worker-task-verification-v0.per` | worker-economy reassessment event | ACTIVE / REASSESSMENT |
| 762–763 | VR | `AEGIS-civilian-lifecycle-reconciler-v0.per` | villager-production reassessment event | ACTIVE / REASSESSMENT |
| 764–765 | HC | `AEGIS-housing-construction-v0.per` | housing reassessment event | ACTIVE / REASSESSMENT |
| 766–767 | RA | `AEGIS-research-age-v0.per` | age-transition reassessment event | ACTIVE / REASSESSMENT |
| 768–769 | CR | `AEGIS-cavalry-response-v0.per` | anti-cavalry reassessment event | ACTIVE / REASSESSMENT |
| 770–771 | MV | `AEGIS-micro-verification-v0.per` | tactical-micro reassessment event | ACTIVE / REASSESSMENT |
| 772–773 | MP | `AEGIS-military-production-v0.per` | military-production reassessment event | ACTIVE / REASSESSMENT |
| 774–775 | CIV | `AEGIS-civilian-demand-v0.per` | villager-production reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 776–777 | CIV | `AEGIS-civilian-demand-v0.per` | housing reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 778–779 | WRV | `AEGIS-worker-role-vector-v0.per` | worker-task-verification reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 780–781 | CS | `AEGIS-civilization-state-v0.per` | age-transition reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 782–783 | ST | `AEGIS-scouting-threat-v0.per` | anti-cavalry reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 784–785 | MC | `AEGIS-micro-control-v0.per` | tactical-micro reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 786–787 | ST | `AEGIS-scouting-threat-v0.per` | military-production reassessment acknowledgement | ACTIVE / REASSESSMENT CONSUMER |
| 788–792 | MP | `AEGIS-military-production-v0.per` | military-production request + authorization identity/generation/valid/expiry | ACTIVE / CANDIDATE HARDENING |
| 793–794 | MPA | `AEGIS-micro-physical-adapter-v0.per` | physical-dispatch evidence generation/valid | ACTIVE / OWNERSHIP BOUNDARY |

## 3. Lifecycle ownership and physical authorization

Every consequential physical action must satisfy:

```text
upstream observation/demand
→ lifecycle owner
→ request identity
→ feasibility
→ authorization owner
→ physical adapter/action
→ authorization consumed
→ pending/world observation
→ verification
→ REASSESS
```

Rules:
- A lifecycle owner alone mutates its lifecycle state.
- An authorization owner alone mutates its authorization state.
- A physical adapter may issue the command and publish its own dispatch evidence, but must not mutate another module's lifecycle state.
- Verification may publish evidence and REASSESS, but must not authorize another physical command.
- REASSESS acknowledgement cannot manufacture the next upstream generation.

## 4. REASSESS boundary

All seven verticals publish one stable lifecycle-generation token per terminal generation. Consumers acknowledge the exact generation once and consume the publication token. REASSESS does not mean success, causal success, authorization, strategy selection, or promotion.

## 5. Collision/ownership repairs

Previously repaired collisions remain preserved, including 550–551, 630–633, Worker Verification/Qualification 546–547 and 555–559, and Scouting/Threat 610–617. Tactical Micro additionally required an ownership repair: the physical adapter no longer writes Micro Control lifecycle state; it publishes dispatch evidence in its own 793–794 boundary, while Micro Control consumes that evidence and advances its own lifecycle.

Housing construction likewise no longer clears `aegis-civ-housing-demand` directly. Civilian Demand owns that policy state and must react through its normal observation/REASSESS boundary.

## 6. Qualification discipline

Namespace correctness and authorization correctness do not promote a vertical. Military Production remains candidate-blocked because `aegis-mp-unit` is still not initialized in authoritative source and its count-increase confirmation remains insufficient causal evidence. Tactical Micro command-to-world-effect qualification and other causal/runtime gates remain open.
