# AEGIS Ownership Inventory — Complete Civilian/Economic Candidate Set (2026-09-09)

**Status:** Expanded inventory covering the main civilian/economic implementation candidates  
**Rule:** Every number is experimental only. None are cleared for production.

## Compact channel map (by module)

### Civilization State (403–420)
403 generation, 404 valid, 405 stage, 406 observed-at, 407 cycle, 408 time, 409 population, 410 population-cap, 411 age, 412 food, 413 wood, 414 gold, 415 spear, 416 camel, 417 skirm, 418 cavalry, 419 archers, 420 focus-player

### Villager Production (427–432)
427 generation, 428 valid, 429 stage, 430 action, 431 attempts, 432 observed

### Civilian Census (433–440 + timer 42)
42 timer, 433 generation, 434 valid, 435 stage, 436 villagers, 437 town-centers, 438 pending-villagers, 439 observed-at, 440 cycle

### Civilian Lifecycle Reconciler (441–449)
441 generation, 442 valid, 443 stage, 444 baseline-villagers, 445 observed-villagers, 446 pending, 447 confirmed-delta, 448 attempts, 449 observed-at

### Worker Role Vector (465–478)
465 generation, 466 valid, 467 stage, 468–472 desired (food/wood/gold/stone/builder), 473–477 deficit (same), 478 observed-at

### Economic Demand Arbitration (490–497)
490 generation, 491 valid, 492 stage, 493 selected-resource, 494 selected-deficit, 495 priority, 496 urgency, 497 observed-at

### Source/Dropsite Serviceability (499–507)
499 generation, 500 valid, 501 stage, 502 resource, 503 source-count, 504 serviceable, 505 failure, 506 observed-at, 507 cycle

### Worker Task Command (519–525)
519 generation, 520 valid, 521 stage, 522 resource, 523 attempts, 524 action, 525 observed-at

### Worker Recovery (546–554)
546 generation, 547 valid, 548 stage, 549 resource, 550 failure, 551 attempts, 552 disposition, 553 observed-at, 554 cycle

## Experimental private space summary

| Block | Status |
|-------|--------|
| 42 (timer) | High collision risk — low number |
| 403–420 | Civilization state snapshot |
| 427–449 | Core civilian production + census + lifecycle |
| 465–478 | Worker role vector |
| 490–507 | Economic arbitration + source serviceability |
| 519–525 | Worker task command |
| 546–554 | Worker recovery |

**None of the above are cleared.**

## Positive observation

The candidate code consistently uses the envelope:

`GENERATION + VALID + STAGE + PAYLOAD + (optional) ATTEMPTS / OBSERVED-AT`

This matches the recommended ownership pattern and should be preserved.

## Remaining extraction

A few supporting files (worker-role-census, worker-target-selection, worker-task-verification, worker-productivity-observer, civilian-demand, economic-demand, probes) may still add a small number of channels. They should be added in a later micro-pass if needed before any freeze.
