# P0 Stock Runtime Coverage Audit — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Machine:** Weebo  
**Authoritative stock corpus:** `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`  
**Purpose:** Determine what the existing Promisory/AI archaeology already covers, identify the remaining reconstruction boundary, and reconcile the current machine runtime with the repository's historical AEGIS assembly records.

## 1. Executive result

This pass confirms that a large amount of the Promisory subsystem archaeology is already complete. The project should **not restart Promisory deconstruction from zero**.

The existing repository already contains dedicated forensic/QC work covering civilian lifecycle, worker tasking, interruption/recovery, source failure, dropsite logistics, object status, worker accounting, threat interaction, resource failure, economic demand/allocation, contention/preemption, worker target selection, production arbitration, rule control flow, mutation visibility, escrow, and external ABI cross-reference.

The remaining problem is therefore not primarily conceptual discovery of individual Promisory mechanisms. It is **system reconstruction and ownership mapping**:

```text
complete stock AI behavior
        +
Promisory runtime substrate
        +
AI(HD) behavioral contracts
        ↓
complete stock-system dependency/ownership map
        ↓
AEGIS-owned civilization operating system
        ↓
AEGIS cognition
```

This is the correct next engineering boundary.

## 2. Existing forensic coverage

The current repository contains the following substantive P0 investigations:

- `P0_CIVILIAN_LIFECYCLE_FORENSICS.md`
- `P0_CIVILIAN_LIFECYCLE_FORENSICS_v2.md`
- `P0_DROPSITE_RESOURCE_LOGISTICS_FORENSICS.md`
- `P0_ECONOMIC_CONTENTION_AND_PREEMPTION_QC_2026-09-07.md`
- `P0_ECONOMIC_DEMAND_TO_WORKER_ALLOCATION_QC_2026-09-07.md`
- `P0_ESCROW_RESERVATION_AND_EXECUTION_QC_2026-09-07.md`
- `P0_EXTERNAL_ABI_CROSS_REFERENCE_2026-09-07.md`
- `P0_OBJECT_STATUS_SEMANTICS_QC_2026-09-07.md`
- `P0_PRODUCTION_QUEUE_ARBITRATION_QC_2026-09-07.md`
- `P0_RESOURCE_SOURCE_FAILURE_FORENSICS.md`
- `P0_RESOURCE_STATUS_AND_CROSS_RESOURCE_FAILURE_QC_2026-09-07.md`
- worker accounting/builder continuity QC
- threat interaction/recovery QC
- worker target/assignment QC
- rule control-flow/jump ABI QC
- rule-pass mutation visibility QC

These are not merely notes. Several establish explicit stock mechanisms and their AEGIS architectural consequences.

### Already strongly established

The existing evidence establishes, among other things:

1. `trainvillager` is an authorization/policy state rather than the physical production operation.
2. `up-can-train escrow-state villager` participates in production feasibility.
3. `up-train escrow-state villager` is a distinct physical production operation.
4. Pending production and completed population must remain separate state.
5. `dawn.per` converts policy percentages into integer worker-role targets.
6. `gatherers.per` performs spatial/candidate-based worker and source selection.
7. Generic stock gathering frequently uses `action-default` after target selection.
8. Construction and resource tasking are coupled through infrastructure state.
9. Builder allocation is a specialized worker state.
10. Escrow is real execution-relevant state, not merely internal bookkeeping.
11. Escrow supports multi-request arbitration and execution gating.
12. Production, age-up, research, construction and military spending compete through the same economic control plane.
13. Stock control flow uses `up-jump-rule` as actual program control, so source order is behaviorally meaningful.
14. Exact same-pass mutation/scheduling semantics remain runtime-qualification questions.

These findings should be treated as existing research inputs rather than re-discovered from scratch.

## 3. Actual stock load graph discovered on the machine

A fresh machine scan of all `.per` files found 95 files under the stock AI directory, including the stock Promisory corpus, AI(HD), AiBuilder, and current AEGIS artifacts.

For **active `load` statements** in the principal stock files:

```text
AI (HD version).per
  -> Promisory\defaultConstants
  -> Promisory\finalingConstants
  -> Promisory\finaling

AEGIS-BYZ.per (current machine state)
  -> Promisory\defaultConstants
  -> Promisory\finalingConstants
  -> Promisory\finaling

Promisory\buildings.per
  -> Promisory\extremebuildings2

Promisory\gatherers.per
  -> Promisory\ugp

Promisory\init.per
  -> no active merge load (the visible merge load is commented)

Promisory\merge.per
  -> no active merge1b load (the visible load is commented)

AiBuilder.per
  -> its own AiBuilder subsystem files
```

The scan also found commented historical loads such as `extremeBuildings`, `merge`, and `merge1b`. These are provenance evidence but are **not active runtime dependencies** and must not be represented as active imports without further proof.

### Important interpretation

The runtime load graph is shallower than the total source provenance suggests.

AI(HD) is a large flattened behavioral corpus. Its relationship to Promisory is therefore not adequately described as “AI(HD) loads all Promisory modules.” The more accurate model is:

```text
AI(HD) flattened behavioral corpus
        │
        ├── contains large amounts of civilization behavior
        │
        └── depends at runtime on selected Promisory constants/finalization substrate

Promisory standalone corpus
        │
        ├── exposes additional operational source material
        └── provides provenance for mechanisms represented in the flattened AI
```

This distinction matters enormously for the AEGIS reconstruction.

## 4. Current machine-state correction

Fresh SHA-256 inspection on Weebo produced:

```text
AEGIS-BYZ.per
1167238 bytes
8A554A90A18F7983A949F7BEF3B767E09732BCE87DCA3B9546FE782F098DE51C

AI (HD version).per
1167238 bytes
8A554A90A18F7983A949F7BEF3B767E09732BCE87DCA3B9546FE782F098DE51C

AegisProm\AEGIS-BYZ-FINAL-CIVOS.per
1167245 bytes
A593B33717D4E862E496FD1EF98694E5F862C974A3FEE368BBD1A3B66BBE2596

Promisory\finaling.per
29232 bytes
95E18EB8B765A7F87EA499C25ED944D0E04C9ABF932B70D8821EF1154D872E52
```

Therefore the current live `AEGIS-BYZ.per` is **byte-identical to the untouched stock `AI (HD version).per`**.

This is decisive machine evidence. The current live entry point is not an AEGIS controller; it is the stock flattened AI body with its stock Promisory runtime loads.

The previously assembled `AegisProm\AEGIS-BYZ-FINAL-CIVOS.per` is a separate derived artifact. It is 7 bytes larger than stock and differs at minimum by its AEGIS header/comment; its hash is different. Its existence does not make it the live entry point.

## 5. Reconciliation with previous AEGIS assembly records

The repository contains a prior assembly record stating that `AEGIS-BYZ-FINAL-CIVOS.per` was a self-contained stock-derived civilization substrate with its three runtime constant dependencies rehosted under `AegisProm\AEGIS-stock-*`.

That record remains useful as an **assembly artifact record**, but it cannot be interpreted as proof that the live root is using that artifact.

The current machine proves otherwise: `AEGIS-BYZ.per` currently loads the original `Promisory\defaultConstants`, `Promisory\finalingConstants`, and `Promisory\finaling` and is byte-identical to `AI (HD version).per`.

Accordingly, the project status is:

```text
Historical AEGIS self-owned civilization artifact: EXISTS
Current live AEGIS entry-point integration: NOT PRESENT
Stock AI behavioral corpus: PRESENT
Promisory runtime dependency at current root: PRESENT
```

This is a correction to the current machine-state interpretation, not a rejection of the earlier forensic work.

## 6. What the project has already deconstructed sufficiently

The following domains have enough existing forensic coverage to move into reconstruction/implementation planning rather than repeat conceptual archaeology:

### Civilian/economic substrate

- villager production lifecycle;
- pending/completion distinction;
- worker role accounting;
- worker allocation;
- resource/source selection;
- dropsite/serviceability concepts;
- worker tasking;
- worker productivity observation;
- interruption/recovery;
- economic demand;
- contention/preemption;
- escrow/reservation;
- production arbitration.

### Failure/state semantics

- object status;
- resource-source failure;
- cross-resource failure;
- threat versus task failure;
- generation fencing;
- pending state;
- command versus completion distinction.

### Interpreter/control-flow

- `up-jump-rule` forward/backward control-flow role;
- relative-jump fragility;
- rule ordering as effective program structure;
- important mutation-visibility uncertainty;
- external ABI corroboration.

### Architecture

- AEGIS state envelope;
- Civilization OS concept;
- service-contract model;
- cognition/execution separation;
- verification/recovery model;
- stock-to-AEGIS ownership concept.

## 7. Remaining reconstruction domains

The next work should focus on **coverage gaps**, not restart the completed P0 civilian archaeology.

### P0 remaining

1. Complete stock load/import closure, including the exact relationship between flattened AI(HD) behavior and Promisory source modules.
2. Build a complete stock symbol inventory:
   - definitions;
   - readers;
   - writers;
   - goals;
   - strategic numbers;
   - timers;
   - searches;
   - object-data fields;
   - action/order identifiers.
3. Map AI(HD) behavioral regions to actual operational services.
4. Map Promisory source mechanisms to those same services.
5. Identify where AI(HD) duplicates, specializes, or overrides Promisory behavior.
6. Identify stock systems that have not yet received dedicated forensic coverage.
7. Establish explicit preserve/reimplement/adapt/replace/supersede decisions.

### High-priority uncovered/undercovered operational families

- full construction operating system;
- complete military operating system / TSA integration;
- scouting/information operating system;
- research and age operating system;
- water/fishing operating system;
- trade operating system;
- late-game/cooperation/support systems;
- initialization and bootstrap dependencies;
- full interaction command substrate;
- stock AI-to-Promisory behavioral interface;
- civ-specific policy partitioning across the flattened corpus.

These are not necessarily completely unexplored. The classification is that their **complete ownership/dependency reconstruction has not yet been demonstrated by the current forensic corpus**.

## 8. New architecture conclusion

The final bot should not be described as:

```text
AEGIS + AI(HD)
```

nor as:

```text
AEGIS + Promisory
```

The correct target is:

```text
                    AEGIS-BYZ
                        │
             ┌──────────┴──────────┐
             │                     │
        Strategic Cognition    Civilization OS
             │                     │
       belief/situation       economy/workers
       objectives/planning    construction
       decision/commitment    information
             │                 military
             │                 technology
             │                 trade/water
             │                 late game
             └──────────┬──────────┘
                        │
                 AEGIS-owned ABI
                        │
                    AoE2DE engine
```

The Civilization OS must preserve the operational behavior represented by both the flattened AI and the Promisory substrate where required, while the AEGIS runtime eventually owns the implementation rather than depending on the Promisory directory.

## 9. Evidence boundary reached in this pass

This pass has reached a natural evidence boundary.

We now have direct machine evidence sufficient to establish:

- the authoritative stock directory contains 95 `.per` files;
- the principal stock AI entry point has only three active Promisory imports;
- additional Promisory files have internal active imports (`buildings -> extremebuildings2`, `gatherers -> ugp`);
- some historical imports are commented and therefore not active dependencies;
- the current `AEGIS-BYZ.per` is byte-identical to stock AI(HD);
- the separate AEGIS civilization artifact exists but is not the current entry point;
- the repository already contains substantial Promisory deconstruction and should be reused;
- the next major objective is complete stock behavioral/dependency coverage and ownership mapping, not another restart of civilian archaeology.

What this pass **does not** prove:

- exact semantic equivalence between every Promisory source module and every AI(HD) flattened region;
- complete symbol-level reader/writer closure;
- complete civ-specific ownership partition;
- runtime equivalence of the AEGIS-derived civilization artifact;
- ABI qualification of unresolved interpreter micro-order questions;
- successful AEGIS integration in live gameplay.

Those remain open and explicitly tracked.

## 10. Next engineering gate

The next pass should produce:

```text
STOCK LOAD CLOSURE
        ↓
SYMBOL INVENTORY
        ↓
GOAL / SN / TIMER WRITER-READER MATRIX
        ↓
AI(HD) REGION → PROMISORY SERVICE MAP
        ↓
PRESERVE / REIMPLEMENT / ADAPT / REPLACE MATRIX
        ↓
AEGIS CIVILIZATION OS BUILD SPEC
```

Only then should the new final runtime be assembled.

## Status

**P0 STOCK COVERAGE AUDIT: STATICALLY COMPLETE FOR THIS PASS**  
**Existing Promisory civilian forensics: REUSED, NOT RESTARTED**  
**Current live AEGIS entry point: REJECTED AS FINAL**  
**Next objective: COMPLETE STOCK SYSTEM / OWNERSHIP RECONSTRUCTION**  
**Runtime qualification: NOT YET COMPLETE**
