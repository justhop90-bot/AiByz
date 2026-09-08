# Promisory Source Module Census — 2026-09-08

**Source:** restored target-build AI package on Weebo
**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Purpose:** static deconstruction of the complete Promisory source substrate.

This census is intentionally separate from the A1 normal-HD runtime closure. It measures the source corpus present under `Promisory/`; it does not claim that every module is independently loaded by the current normal-HD entrypoint.

## Module inventory

| Module | Lines | `defrule` | `defconst` | Dominant constructs observed | Role for reconstruction |
|---|---:|---:|---:|---|---|
| `boarhunting.per` | 1,236 | 101 | 0 | goal/SN modification, food acquisition | Food acquisition lifecycle |
| `buildings.per` | 13,117 | 1,048 | 0 | build/placement, pending objects, builder assignment | Construction OS |
| `const.per` | 5,965 | 0 | 4,717 | constants | Core vocabulary/state definitions |
| `customConstants.per` | 8,064 | 1 | 6,454 | constants | Extended vocabulary / patch-maintained definitions |
| `dawn.per` | 457 | 40 | 0 | goal/SN reconciliation | Worker allocation/reconciliation |
| `defaultConstants.per` | 941 | 0 | 683 | constants | Current normal-HD load closure |
| `escrow.per` | 3,386 | 346 | 0 | escrow, goals, flags | Resource reservation/control |
| `event.per` | 4 | 1 | 0 | event disable | Event substrate |
| `events.per` | 6 | 1 | 0 | player-name/chat event | Event substrate |
| `extremebuildings2.per` | 1,010 | 73 | 0 | placement geometry | Construction placement support |
| `finaling.per` | 1,090 | 116 | 0 | train/research/finalization | Current normal-HD load closure |
| `finalingConstants.per` | 400 | 0 | 266 | constants | Current normal-HD load closure |
| `gatherers.per` | 5,325 | 449 | 0 | worker allocation/search/SN control | Economic worker OS |
| `general.per` | 7,605 | 582 | 0 | search/goals/object control | Shared AI services |
| `ImprovementBucketsConst.per` | 4,386 | 1 | 3,527 | constants | Historical/reference constants |
| `ImprovementBucketsTestConst.per` | 813 | 0 | 580 | constants | Historical/reference constants |
| `init.per` | 10,725 | 909 | 0 | initialization/goals/spatial economy | Bootstrap + operating doctrine |
| `interaction.per` | 4,501 | 406 | 0 | communication/cooperation | Cross-player interaction |
| `merge.per` | 1 | 0 | 0 | empty/merge marker | Packaging artifact |
| `merge1b.per` | 212 | 0 | 182 | constants | Packaging/reference artifact |
| `merge2.per` | 0 | 0 | 0 | empty | Packaging artifact |
| `merge2b.per` | 8 | 0 | 0 | merge marker | Packaging artifact |
| `merge3.per` | 0 | 0 | 0 | empty | Packaging artifact |
| `merge3b.per` | 0 | 0 | 0 | empty | Packaging artifact |
| `merge4.per` | 193 | 9 | 16 | taunt/flag/SN behavior | Packaging/reference artifact |
| `orb.per` | 4,515 | 308 | 0 | object search/filter/control | Object-management services |
| `paphosConstants.per` | 525 | 0 | 417 | constants | Historical/reference constants |
| `researches.per` | 7,023 | 629 | 0 | research/age policy | Research OS |
| `resign.per` | 890 | 83 | 0 | defeat/resign state | Terminal-state policy |
| `scoutcontrol.per` | 1,342 | 104 | 0 | scouting/waypoints/threat response | Information/scouting OS |
| `threats.per` | 1,822 | 163 | 0 | threat sensing, goals, SNs, facts | Threat-response signaling |
| `trade.per` | 1,306 | 97 | 0 | commodity trading | Trade economy |
| `tsa.per` | 12,769 | 962 | 0 | military state/control | Tactical/military OS |
| `ugp.per` | 324 | 54 | 0 | object costs/availability | Generic production support |
| `units.per` | 13,786 | 1,049 | 0 | production, goals, SNs | Unit production/role OS |
| `watercontrol.per` | 1,055 | 72 | 0 | naval object control | Water/naval support |

## Static internal load edges

A direct scan of all 36 Promisory `.per` files in the restored package found **two explicit internal `load` edges**:

```text
Promisory/buildings.per
    → Promisory/extremebuildings2

Promisory/gatherers.per
    → Promisory/ugp
```

No other explicit `(load "...")` statements were found inside the 36-file Promisory corpus during this scan.

This is a **source-level load graph**, not a runtime execution graph. It must be joined with the actual entrypoint closure before any module is classified as current runtime-loaded.

## Current normal-HD closure distinction

The dated A1 closure separately establishes:

```text
AI (HD version).per
    → Promisory/defaultConstants.per
    → Promisory/finalingConstants.per
    → Promisory/finaling.per
```

Those four files contain no further loads. Therefore:

- the complete Promisory directory is a **source substrate / archaeology corpus**;
- the four-file chain is the **captured normal-HD runtime closure**;
- source presence is not proof of current runtime reachability;
- historical module responsibility is not proof of current load order.

## Reconstruction significance

The census establishes that the historical Promisory substrate is not a monolithic rule file. It is a family of specialized stateful services with materially different control surfaces.

The largest behavioral modules are:

1. `units.per` — production/role control
2. `buildings.per` — construction/placement
3. `tsa.per` — tactical/military control
4. `init.per` — initialization/operating doctrine
5. `researches.per` — research/age control
6. `general.per` — shared object/search services
7. `gatherers.per` — worker/economic control

This supports the current architectural conclusion that AEGIS should recover **capabilities and invariants** from these systems rather than reconnecting the historical source tree as a runtime dependency.

## Next static join

The next deconstruction join should be:

`module → symbol declarations → readers → writers → resetters → goals/SNs/timers → object/search state → cross-module consumers → lifecycle`

That join is the required precursor to assigning AEGIS ownership.
