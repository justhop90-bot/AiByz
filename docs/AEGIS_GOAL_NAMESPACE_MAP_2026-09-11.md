# AEGIS Repository-Wide Goal Namespace Map — 2026-09-11

**Authority:** `main/AegisProm` source
**Scope:** shared AegisProm `.per` goal namespace
**Status:** NORMATIVE / COLLISION REPAIR BASELINE

## 1. Namespace rule

All numeric `defconst` goal identifiers in loaded AegisProm source share one engine goal namespace. A numeric slot therefore belongs to exactly one semantic field across the repository.

Rules:

1. Source under `main/AegisProm` is authoritative for AEGIS architecture.
2. `runtime/` copies do not reserve or define source goal ownership.
3. A symbol rename without a numeric relocation does not repair a collision.
4. A numeric relocation must preserve the symbol, semantic owner, and all references to that symbol.
5. Existing semantic ownership is not changed by namespace repair.
6. Lifecycle work must not allocate into an occupied slot.
7. Every new goal must be registered here before source promotion.
8. `0` values used as local enum values are not namespace allocations unless assigned to a `defconst` goal slot; enum literals remain module-local constants.

## 2. Authoritative repaired allocations

| Numeric block | Owner | Source | Purpose | Status |
|---|---|---|---|---|
| 490–497 | EDA | `AEGIS-economic-demand-arbitration-v0.per` | economic arbitration state + request identity | ACTIVE |
| 510–518 | WTS | `AEGIS-worker-target-selection-v0.per` | worker target-selection state | ACTIVE |
| 519–530 | WTC | `AEGIS-worker-task-command-v0.per` | worker physical task command + authorization | ACTIVE |
| 546–549 | WR | `AEGIS-worker-recovery-v0.per` | recovery lifecycle base state | ACTIVE |
| 550–551 | EDA/WTS | `AEGIS-economic-demand-arbitration-v0.per`, `AEGIS-worker-target-selection-v0.per` | request identities | ACTIVE / EXCLUSIVELY OWNED |
| 552–554 | WR | `AEGIS-worker-recovery-v0.per` | recovery disposition/observation/cycle | ACTIVE |
| 555–556 | WR | `AEGIS-worker-recovery-v0.per` | **repaired failure + attempt fields** | ACTIVE / REPAIRED |
| 570–585 | HC | `AEGIS-housing-construction-v0.per` | housing lifecycle + request/authorization/evidence | ACTIVE |
| 600–612 | RA | `AEGIS-research-age-v0.per` | age-transition lifecycle + request/authorization/evidence | ACTIVE |
| 620–629 | CR | `AEGIS-cavalry-response-v0.per` | anti-cavalry lifecycle + request/authorization | ACTIVE |
| 630–637 | MP | `AEGIS-military-production-v0.per` | military-production candidate lifecycle | ACTIVE / CANDIDATE BLOCKED |
| 638–641 | CR | `AEGIS-cavalry-response-v0.per` | **repaired spearman baseline/observed/world/causal evidence** | ACTIVE / REPAIRED |
| 670–677 | MC | `AEGIS-micro-control-v0.per` | tactical micro control state | ACTIVE |
| 680–689 | MS | `AEGIS-micro-state-v0.per` | tactical micro force/state observation | ACTIVE |
| 690–699 | MG | `AEGIS-micro-groups-v0.per` | tactical micro functional groups | ACTIVE |
| 700–709 | MGeo | `AEGIS-micro-geometry-v0.per` | tactical geometry | ACTIVE |
| 710–716 | MG3 | `AEGIS-micro-governor-v0.per` | tactical command governor | ACTIVE |
| 720–726 | MV | `AEGIS-micro-verification-v0.per` | tactical verification state | ACTIVE |
| 730–739 | ME | `AEGIS-micro-execution-bridge-v0.per` | tactical execution authorization bridge | ACTIVE |
| 734–735 | MC | `AEGIS-micro-control-v0.per` | stable tactical request identity | ACTIVE / SHARED RANGE PARTITION |
| 736–739 | ME | `AEGIS-micro-execution-bridge-v0.per` | tactical authorization identity/generation/expiry | ACTIVE |
| 740–743 | MV | `AEGIS-micro-verification-v0.per` | tactical request/auth/world/causal evidence | ACTIVE |

**Important:** the ranges above describe numeric goal-slot ownership, not semantic stage values. Stage constants such as `stage-authorized = 1` are ordinary symbolic enum values and are not competing global goal slots.

## 3. Collision repairs performed

### 3.1 Goals 550–551

Previous collision:

- `aegis-eda-request-id = 550`
- `aegis-wr-failure = 550`
- `aegis-wts-request-id = 551`
- `aegis-wr-attempts = 551`

Repair:

- EDA request identity remains **550**.
- WTS request identity remains **551**.
- Worker Recovery `failure` moved **550 → 555**.
- Worker Recovery `attempts` moved **551 → 556**.

Semantic ownership did not change. Only the numeric slots changed.

### 3.2 Goals 630–633

Previous collision:

- Military Production owned **630–637**.
- Anti-Cavalry owned **630–633**.

Repair:

- Military Production retains **630–637** unchanged.
- Anti-Cavalry baseline spears moved **630 → 638**.
- Anti-Cavalry observed spears moved **631 → 639**.
- Anti-Cavalry world evidence moved **632 → 640**.
- Anti-Cavalry causal evidence moved **633 → 641**.

Semantic ownership did not change. Only the numeric slots changed.

## 4. Why these owners were retained

The repair intentionally keeps the fields with their existing semantic owners rather than moving the entire blocks of either vertical.

- EDA remains the authoritative owner of economic request identity.
- WTS remains the downstream carrier of that identity.
- Worker Recovery remains the owner of recovery failure/attempt state.
- Military Production remains the owner of its candidate production lifecycle.
- Anti-Cavalry remains the owner of its spearman production evidence.

This avoids an architectural change disguised as a namespace repair.

## 5. Reserved allocation discipline

The repaired slots **555–556** and **638–641** are now occupied and must not be reused.

The following ranges are explicitly protected from future lifecycle allocation because they are already occupied by current source architecture:

- 490–497
- 510–530
- 546–556
- 570–585
- 600–612
- 620–641
- 670–743

Future lifecycle fields must be allocated outside these occupied blocks and then added to this ledger before source use.

## 6. Runtime/source separation

Runtime copies may contain experimental initializers or integration behavior. They do not receive namespace authority merely because they contain a symbol assignment. A runtime-only numeric use cannot be used to justify changing canonical source ownership.

## 7. Qualification gate

This repair clears the **numeric namespace collision blocker only**. It does not clear:

- authorization expiry semantics;
- active-request supersession in Worker Command/Villager Production;
- canonical reassessment publication;
- causal verification gaps;
- Military Production candidate qualification.

Those remain independent lifecycle gates.

## 8. Required validator invariant

A repository namespace validator should fail if any two source `defconst` declarations assign the same numeric goal slot, except where the duplicate numeric literal is an explicitly declared local enum value rather than a goal slot.

The authoritative test condition is:

```text
GLOBAL_GOAL_SLOT -> exactly one semantic owner
```

A symbol can be referenced by many modules; the numeric goal slot cannot have two owners.
