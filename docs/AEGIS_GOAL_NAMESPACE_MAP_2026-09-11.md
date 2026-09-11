# AEGIS Repository-Wide Goal Namespace Map — 2026-09-11

**Authority:** `main/AegisProm` source
**Scope:** shared AegisProm `.per` goal namespace
**Status:** NORMATIVE / COLLISION REPAIR + REASSESSMENT BOUNDARY BASELINE

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

## 2. Authoritative allocations

| Numeric block | Owner | Source | Purpose | Status |
|---|---|---|---|---|
| 490–497 | EDA | `AEGIS-economic-demand-arbitration-v0.per` | economic arbitration state + request identity | ACTIVE |
| 510–518 | WTS | `AEGIS-worker-target-selection-v0.per` | worker target-selection state | ACTIVE |
| 519–530 | WTC | `AEGIS-worker-task-command-v0.per` | worker physical task command + authorization | ACTIVE |
| 534–545 | WTV | `AEGIS-worker-task-verification-v0.per` | worker task verification state | ACTIVE |
| 546–549 | WR | `AEGIS-worker-recovery-v0.per` | recovery lifecycle base state | ACTIVE |
| 550–551 | EDA/WTS | `AEGIS-economic-demand-arbitration-v0.per`, `AEGIS-worker-target-selection-v0.per` | request identities | ACTIVE / EXCLUSIVELY OWNED |
| 552–554 | WR | `AEGIS-worker-recovery-v0.per` | recovery disposition/observation/cycle | ACTIVE |
| 555–556 | WR | `AEGIS-worker-recovery-v0.per` | repaired failure + attempt fields | ACTIVE / REPAIRED |
| 560–561 | WTV | `AEGIS-worker-task-verification-v0.per` | repaired verification request/authorization identity | ACTIVE / REPAIRED |
| 562–566 | WLQ | `AEGIS-worker-loop-qualification-v0.per` | qualification heartbeat state | CANDIDATE / REPAIRED |
| 570–585 | HC | `AEGIS-housing-construction-v0.per` | housing lifecycle + request/authorization/evidence | ACTIVE |
| 600–612 | RA | `AEGIS-research-age-v0.per` | age-transition lifecycle + request/authorization/evidence | ACTIVE |
| 620–629 | CR | `AEGIS-cavalry-response-v0.per` | anti-cavalry lifecycle + request/authorization | ACTIVE |
| 630–637 | MP | `AEGIS-military-production-v0.per` | military-production candidate lifecycle | ACTIVE / CANDIDATE BLOCKED |
| 638–641 | CR | `AEGIS-cavalry-response-v0.per` | repaired spearman baseline/observed/world/causal evidence | ACTIVE / REPAIRED |
| 642–649 | ST | `AEGIS-scouting-threat-v0.per` | repaired threat-observation state | ACTIVE / REPAIRED |
| 650 | CR | `AEGIS-cavalry-response-v0.per` | repaired anti-cavalry failure state | ACTIVE / REPAIRED |
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
| 760–761 | WTV | `AEGIS-worker-task-verification-v0.per` | worker-economy reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 762–763 | VR | `AEGIS-civilian-lifecycle-reconciler-v0.per` | villager-production reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 764–765 | HC | `AEGIS-housing-construction-v0.per` | housing reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 766–767 | RA | `AEGIS-research-age-v0.per` | age-transition reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 768–769 | CR | `AEGIS-cavalry-response-v0.per` | anti-cavalry reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 770–771 | MV | `AEGIS-micro-verification-v0.per` | tactical-micro reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 772–773 | MP | `AEGIS-military-production-v0.per` | military-production candidate reassessment generation/valid event | ACTIVE / REASSESSMENT |
| 774–775 | CIV | `AEGIS-civilian-demand-v0.per` | civilian-demand acknowledgement of villager-production REASSESS | ACTIVE / REASSESSMENT CONSUMER |
| 776–777 | CIV | `AEGIS-civilian-demand-v0.per` | civilian-demand acknowledgement of housing REASSESS | ACTIVE / REASSESSMENT CONSUMER |
| 778–779 | WRV | `AEGIS-worker-role-vector-v0.per` | worker-role-vector acknowledgement of worker-task-verification REASSESS | ACTIVE / REASSESSMENT CONSUMER |
| 780–781 | CS | `AEGIS-civilization-state-v0.per` | civilization-state acknowledgement of age-transition REASSESS | ACTIVE / REASSESSMENT CONSUMER |
| 782–783 | ST | `AEGIS-scouting-threat-v0.per` | scouting/threat acknowledgement of anti-cavalry REASSESS | ACTIVE / REASSESSMENT CONSUMER |

## 3. Reassessment boundary rule

Every registered vertical now has a local reassessment publisher owned by the vertical's registry-defined `REASSESS` owner. The publisher emits a stable lifecycle-generation token exactly once per terminal request generation and raises a local `reassess-valid` event bit.

Consumers acknowledge the exact published lifecycle generation once. Acknowledgement is not a new observation and cannot manufacture a new lifecycle generation. The consuming owner remains responsible for waiting for and consuming its own next upstream observation/demand generation.

The event means only:

```text
THIS VERTICAL LIFECYCLE HAS REACHED A TERMINAL OBSERVED OUTCOME.
RECONSIDERATION IS NOW PERMITTED.
```

It does **not** mean:

- strategic success;
- causal success where causal evidence is absent;
- permission to issue another physical command;
- a particular next strategy;
- authorization for another vertical.

The consuming owner remains responsible for the next observation/demand/classification generation. No monolithic reassessment controller is introduced.

## 4. Collision repairs performed

### 4.1 Goals 550–551

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

### 4.2 Goals 630–633

Previous collision:

- Military Production owned **630–637**.
- Anti-Cavalry owned **630–633**.

Repair:

- Military Production retains **630–637** unchanged.
- Anti-Cavalry baseline spears moved **630 → 638**.
- Anti-Cavalry observed spears moved **631 → 639**.
- Anti-Cavalry world evidence moved **632 → 640**.
- Anti-Cavalry causal evidence moved **633 → 641**.

### 4.3 Worker Verification / Qualification collisions

Two pre-existing omissions in the earlier namespace ledger were corrected during this pass:

- Worker Task Verification request identity `546` collided with Worker Recovery generation `546`; moved **546 → 560**.
- Worker Task Verification authorization identity `547` collided with Worker Recovery valid `547`; moved **547 → 561**.
- Worker Loop Qualification occupied `555–559`, colliding with repaired Worker Recovery `555–556`; moved **555–559 → 562–566**.

Semantic ownership and symbol names were preserved in every relocation. These were namespace repairs only.

### 4.4 Scouting/Threat collision

The Anti-Cavalry reassessment audit exposed an additional pre-existing source namespace collision omitted from the earlier ledger:

- Age Transition owned **600–612**.
- Scouting/Threat owned **610–617**.

The overlapping slots were not safe to leave in source. Scouting/Threat was therefore relocated as a semantic block:

- `aegis-st-generation` **610 → 642**
- `aegis-st-valid` **611 → 643**
- `aegis-st-enemy-age` **612 → 644**
- `aegis-st-cavalry` **613 → 645**
- `aegis-st-cavalry-archer` **614 → 646**
- `aegis-st-knight` **615 → 647**
- `aegis-st-threat` **616 → 648**
- `aegis-st-confidence` **617 → 649**

All symbol references remain semantic-symbol based; this is a numeric namespace repair, not an architectural change.

The Anti-Cavalry failure field was also found to be referenced without a source `defconst`. It is now explicitly allocated at **650** as `aegis-cr-failure`.

## 5. Reserved allocation discipline

Occupied/protected blocks now include:

- 490–497
- 510–530
- 534–556
- 560–566
- 570–585
- 600–612
- 620–650
- 670–743
- 760–783

Future lifecycle fields must be allocated outside these occupied blocks and then added to this ledger before source use.

## 6. Runtime/source separation

Runtime copies may contain experimental initializers or integration behavior. They do not receive namespace authority merely because they contain a symbol assignment. A runtime-only numeric use cannot be used to justify changing canonical source ownership.

## 7. Qualification gate

The reassessment boundary clears the **publication-boundary blocker** only. It does not imply that all seven verticals are qualified.

Remaining independent gates include:

- causal verification gaps;
- target-build runtime evidence;
- military-production selector initialization;
- complete downstream consumption of reassessment events;
- tactical command-to-world-effect qualification;
- authoritative engine-age observation in the World Model.

## 8. Required validator invariants

A repository namespace validator should fail if any two source `defconst` declarations assign the same numeric goal slot, except where the duplicate numeric literal is an explicitly declared local enum value rather than a goal slot.

A lifecycle validator should additionally require:

```text
registered vertical
    -> terminal outcome
    -> exactly one reassessment token per lifecycle generation
    -> no strategy selection at the reassessment publisher
```

The authoritative namespace condition remains:

```text
GLOBAL_GOAL_SLOT -> exactly one semantic owner
```
