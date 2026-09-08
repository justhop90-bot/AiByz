# P0 Source / Logistics Forensic QC — 2026-09-07

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Corpus:** untouched stock `resources\_common\ai\Promisory` on Weebo
**Disposition:** QC of prior P0 resource-source and dropsite findings

## Purpose

This report is the QC layer over the preceding source-failure and dropsite-logistics reports. It records which claims survived direct reinspection, which required qualification, and which remain hypotheses.

## Finding 1 — source task load: CONFIRMED

`gatherers.per` explicitly reads `object-data-tasks-count` for resource objects and removes candidates above source-specific load limits. Wood and farm examples were directly re-read. This is engine-visible source concurrency/load state used by allocation logic.

## Finding 2 — farm reassignment: CONFIRMED, narrowed

Around `gatherers.per` 3370+, stock searches farms, removes farms with `object-data-tasks-count >= 1`, stores a farm identity, then selects a villager whose current target is `forage-food` or `sheep-food` under worker-count conditions and issues `action-default` to the farm.

This proves explicit food-source role conversion in this controller. It does **not** prove a single global food-role manager or a universal fallback ordering.

## Finding 3 — dropsite policy: CONFIRMED

`gatherers.per` contains numerous `dropsite-min-distance` predicates for food, wood, gold, stone, hunting, and fish-related policy. The predicate is therefore a real operational input to stock economic decisions.

## Finding 4 — logistics parameters: CONFIRMED, state-dependent

`init.per` sets `sn-minimum-dropsite-buffer = 13`, `sn-required-forest-tiles = 10`, `sn-camp-max-distance = 12`, and `sn-mill-max-distance = 18`. Maximum drop-distance controls are initially set to zero (fish-boat to -1) and later active values are established, including food 8, wood 20, gold 10, stone 10, and hunt 12.

These are observed rule parameters, not immutable global constants.

## Finding 5 — lumber camp response: CONFIRMED

`buildings.per` around line 2026 contains a direct rule requiring `goal buildlumber yes`, wood discovery, `dropsite-min-distance wood > 5`, an existing lumber camp, `sn-camp-max-distance <= 30`, and `can-build lumber-camp`. It enables adjacent dropsites, sets separation distance 4, increases `sn-camp-max-distance` by 4, and builds a lumber camp.

This is direct evidence of infrastructure response to poor wood service distance.

## Finding 6 — adaptive camp threshold: CONFIRMED but resource/context specific

`buildings.per` contains separate wood/gold/stone rules comparing `dropsite-min-distance` with `sn-camp-max-distance` and incrementing the threshold. The rules differ by resource and context. The correct abstraction is **resource-specific adaptive camp-placement policy**, not one universal migration algorithm.

## Finding 7 — exact distance semantics: OPEN

The corpus proves `dropsite-min-distance` is an engine-level spatial predicate used by stock. It does not prove that its value equals exact worker path length. AEGIS documentation should use `delivery/service distance` until the engine metric is independently characterized.

## Finding 8 — fishing: CONFIRMED for task selection, lifecycle still open

`watercontrol.per` filters fishing ships by carry state and current target, finds `ocean-fish-class`, removes fish candidates below a carry threshold, and issues `action-default`. This proves active deep-fish task selection and carry-aware source filtering. It does not prove a generic fish depletion/recovery manager.

## Finding 9 — command versus state: CONFIRMED

`action-default` is the command primitive after selection. Later stock logic reads target/order/carry/task-load state. Therefore command issuance must not be treated as proof of productive assignment.

## Finding 10 — distributed architecture: SUPPORTED, not absolute

Relevant evidence is distributed across `gatherers.per`, `boarhunting.per`, `buildings.per`, `general.per`, and `watercontrol.per`. This supports distributed subsystem controllers, but cannot exclude an unseen engine-level service.

## Corrections to prior language

1. Use **food portfolio/source substitution**, not a fixed food hierarchy.
2. Use **resource-specific adaptive camp-placement policy**, not a universal camp migration algorithm.
3. Treat numeric thresholds as observed rule parameters whose values can change.
4. Treat `dropsite-min-distance` as a service/delivery predicate, not proven path length.
5. Treat labels such as `SOURCE_EXHAUSTED_OR_UNAVAILABLE` as AEGIS normalization categories, not stock event names.
6. Keep source-specific lifecycle detectors separate until common semantics are proven.

## Architectural result

The prior architecture survives QC with stricter boundaries:

```text
STRATEGY
  ↓
ECONOMIC DEMAND
  ↓
SOURCE / CAPACITY ALLOCATION
  ↓
DROPSITE SERVICEABILITY
  ↓
INFRASTRUCTURE REQUIREMENT
  ↓
WORKER ASSIGNMENT
  ↓
COMMAND
  ↓
ENGINE STATE OBSERVATION
  ↓
PRODUCTIVITY / FAILURE
  ↓
RECOVERY / RESELECTION
```

No runtime implementation is authorized by this QC alone.

## Next forensic target

Threat-driven civilian evacuation; worker-death/recount latency; construction interruption and builder replacement; source-status enum semantics; and cross-resource failure convergence.
