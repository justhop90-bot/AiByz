# AEGIS Ownership Inventory from implementation/*.per — 2026-09-09

**Status:** Extracted inventory of all numeric channels currently claimed by the candidate implementation set  
**Parent:** Practical Ownership Matrix V0 + FINAL_RECONSTRUCTION_AUDIT R2/R3  
**Rule:** Every number below is **experimental / candidate only**. None are cleared for production.

## Extracted ranges (from current v0 files)

### Civilian Census (`AEGIS-civilian-census-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-census-timer | 42 | Timer |
| aegis-census-generation | 433 | Generation |
| aegis-census-valid | 434 | Validity |
| aegis-census-stage | 435 | Stage |
| aegis-census-villagers | 436 | Payload |
| aegis-census-town-centers | 437 | Payload |
| aegis-census-pending-villagers | 438 | Payload |
| aegis-census-observed-at | 439 | Observed-at |
| aegis-census-cycle | 440 | Cycle counter |

### Villager Production (`AEGIS-villager-production-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-vp-generation | 427 | Generation |
| aegis-vp-valid | 428 | Validity |
| aegis-vp-stage | 429 | Stage |
| aegis-vp-action | 430 | Action type |
| aegis-vp-attempts | 431 | Attempts |
| aegis-vp-observed | 432 | Observed flag |

### Civilian Lifecycle Reconciler (`AEGIS-civilian-lifecycle-reconciler-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-vr-generation | 441 | Generation |
| aegis-vr-valid | 442 | Validity |
| aegis-vr-stage | 443 | Stage |
| aegis-vr-baseline-villagers | 444 | Baseline |
| aegis-vr-observed-villagers | 445 | Observed |
| aegis-vr-pending | 446 | Pending |
| aegis-vr-confirmed-delta | 447 | Delta |
| aegis-vr-attempts | 448 | Attempts |
| aegis-vr-observed-at | 449 | Observed-at |

### Worker Role Vector (`AEGIS-worker-role-vector-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-wrv-generation | 465 | Generation |
| aegis-wrv-valid | 466 | Validity |
| aegis-wrv-stage | 467 | Stage |
| aegis-wrv-desired-food/wood/gold/stone/builder | 468–472 | Desired |
| aegis-wrv-deficit-food/wood/gold/stone/builder | 473–477 | Deficit |
| aegis-wrv-observed-at | 478 | Observed-at |

### Economic Demand Arbitration (`AEGIS-economic-demand-arbitration-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-eda-generation | 490 | Generation |
| aegis-eda-valid | 491 | Validity |
| aegis-eda-stage | 492 | Stage |
| aegis-eda-selected-resource | 493 | Selection |
| aegis-eda-selected-deficit | 494 | Deficit |
| aegis-eda-priority | 495 | Priority |
| aegis-eda-urgency | 496 | Urgency |
| aegis-eda-observed-at | 497 | Observed-at |

## Observed pattern in the v0 code (positive)

Almost every module already follows the recommended envelope:

```
GENERATION + VALID + STAGE + PAYLOAD(s) + (optional) ATTEMPTS / OBSERVED-AT
```

This is good discipline and should be preserved.

## Collision / safety notes

- Timer `42` is low and may collide with stock timer usage; treat as high-risk until proven free.
- The blocks 427–449, 465–478, 490–497 are the current experimental private space used by the civilian vertical.
- **None of these numbers are cleared.** Before any production promotion they must be checked against the full typed census / collision map and, where necessary, runtime-validated.

## Next inventory step

1. Finish extraction from the remaining implementation files (worker-task-*, source-dropsite, recovery, etc.).
2. Produce a single CSV/JSON ownership file once the first vertical slice is frozen.
3. Run collision checks against `AEGIS_A1_STATE_CHANNEL_COLLISION_MAP_2026-09-05.json`.
