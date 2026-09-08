# P0 Threat / Death / Construction Forensic QC — 2026-09-07

Target: AoE2DE 101.103.48987.0 / BuildID 24094652
Corpus: untouched stock resources/_common/ai/Promisory on Weebo
Status: forensic evidence; implementation deferred.

## QC result

The prior source/logistics findings survive QC with important qualifications. Stock has first-class threat data and uses it to gate specific civilian operations, but this pass does NOT prove a universal worker-evacuation manager. Worker population is refreshed by facts/census in init.per; no dedicated worker-death event handler was found in the inspected paths. Construction has explicit pending-placement, pending-object, builder-count, foundation/status, and failed-placement machinery, but a universal builder-replacement service remains unproven.

## Threat evidence

init.per refreshes `gl-threat-time`, `gl-threat-player`, `gl-threat-source`, and `gl-threat-target` with `up-get-threat-data`, alongside population, civilian population, military population, `unit-type-count villager`, and `unit-type-count-total villager`.

gatherers.per uses `up-enemy-units-in-town >= 1` to suppress/terminate livestock micro behavior. buildings.per uses the same condition, together with `underattack`/`defend`, to suppress farm-building logic.

Therefore threat response is proven to be operation-specific. It is NOT proven that stock globally stops and evacuates all villagers.

## Death/accounting evidence

The stock census rule obtains both villager counts into goals. dawn.per and units.per consume these counts for allocation and production. No inspected rule provides a dedicated villager-death event that directly decrements a role ledger.

Safe model:

engine population changes -> subsequent fact refresh -> count-dependent rules react

Exact refresh interval remains OPEN. AEGIS must attach freshness/observed-at metadata to worker aggregates rather than treating role counts as permanent truth.

## Construction evidence

buildings.per repeatedly distinguishes `up-pending-placement`, `up-pending-objects`, `can-build`, `villager-builder`, `actionid-build`, `status-pending`, and actual building counts.

House construction explicitly finds a non-builder villager, computes placement, then calls `up-assign-builders c: house c: 1` and issues the build operation. Other structures use different builder counts.

This proves construction is a multi-state transaction and builder assignment is distinct from placement.

## Failed placement / foundation recovery

A general.per lumber-camp path detects a pending lumber camp and calls `up-reset-placement`. A buildings.per path detects a pending lumber/mining camp with near-zero hitpoints, deletes the failed object, resets placement, enables adjacent dropsites, and increases `sn-camp-max-distance`.

This is concrete recovery, not a generic retry assumption:

pending -> validate -> failed foundation -> delete/reset -> adapt policy -> re-place

Builder replacement for a surviving foundation is NOT yet proven as a universal mechanism.

## Architecture correction

Do not implement a binary global safety switch. AEGIS should distinguish:

REQUEST EXISTS
REQUEST EXECUTABLE
REQUEST BLOCKED BY THREAT
REQUEST INVALIDATED

Threat observation is global; safety policy is local to the affected subsystem.

## Normalized AEGIS failure categories

SOURCE_FAILURE
SERVICEABILITY_FAILURE
WORKER_FAILURE
THREAT_BLOCK
CONSTRUCTION_PLACEMENT_FAILURE
CONSTRUCTION_FOUNDATION_FAILURE
CONSTRUCTION_BUILDER_SHORTAGE
POPULATION_ACCOUNTING_CHANGE
TASK_TARGET_LOSS
TASK_ORDER_FAILURE

These labels are AEGIS normalization categories, not stock event names.

## Negative findings

Not proven: universal civilian evacuation; immediate event-driven worker-death accounting; exact census cadence; universal builder replacement; one centralized civilian safety manager; one common construction recovery state machine for every building type.

## Next

Inspect interaction.per and remaining civilian controllers for hidden threat-driven orders. Then map source-status enum semantics and cross-resource failure convergence, including wood/gold/stone/fishing/livestock/deer/forage.
