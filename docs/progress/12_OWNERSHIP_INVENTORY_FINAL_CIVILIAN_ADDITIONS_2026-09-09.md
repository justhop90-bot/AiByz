# Ownership Inventory — Final Civilian Additions (2026-09-09)

**Status:** Completes the main civilian/economic candidate channel list  
**Rule:** All numbers remain experimental / uncleared.

## Newly recorded channels

### Civilian Demand (`AEGIS-civilian-demand-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-civ-demand-generation | 421 | Generation |
| aegis-civ-villager-demand | 422 | Demand flag |
| aegis-civ-housing-demand | 423 | Demand flag |
| aegis-civ-urgency | 424 | Urgency |
| aegis-civ-stage | 425 | Stage |
| aegis-civ-observed-at | 426 | Observed-at |

### Worker Role Census (`AEGIS-worker-role-census-v0.per`)
| Symbol | Number | Role |
|--------|--------|------|
| aegis-wrc-timer | 43 | Timer (high collision risk) |
| aegis-wrc-generation | 450 | Generation |
| aegis-wrc-valid | 451 | Validity |
| aegis-wrc-stage | 452 | Stage |
| aegis-wrc-food | 453 | Role count |
| aegis-wrc-forager | 454 | Role count |
| aegis-wrc-shepherd | 455 | Role count |
| aegis-wrc-hunter | 456 | Role count |
| aegis-wrc-fisherman | 457 | Role count |
| aegis-wrc-farmer | 458 | Role count |
| aegis-wrc-wood | 459 | Role count |
| aegis-wrc-gold | 460 | Role count |
| aegis-wrc-stone | 461 | Role count |
| aegis-wrc-builder | 462 | Role count |
| aegis-wrc-observed-at | 463 | Observed-at |
| aegis-wrc-cycle | 464 | Cycle |

## Updated experimental space summary

| Block | Contents |
|-------|----------|
| 42–43 | Timers (high risk) |
| 403–420 | Civilization state |
| 421–426 | Civilian demand |
| 427–449 | Villager production + census + lifecycle |
| 450–464 | Worker role census |
| 465–478 | Worker role vector |
| 490–507 | Economic arbitration + source serviceability |
| 519–525 | Worker task command |
| 546–554 | Worker recovery |

**Still zero production clearances.**
