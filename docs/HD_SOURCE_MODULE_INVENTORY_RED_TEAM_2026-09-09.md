# HD / Promisory Source Module Inventory — Red-Team Evidence

**Date:** 2026-09-09
**Purpose:** preserve the source-inventory evidence that triggered the final basic-capability red-team pass.

## Evidence boundary

This document does not claim that a filename proves the semantics of its contents. It records source modules that must be explicitly accounted for during direct archaeology.

The public Steam depot inventory for the AoE2DE AI package exposes the following Promisory/AI source families relevant to AEGIS coverage:

- `init.per`
- `boarhunting.per`
- `buildings.per`
- `customConstants.per`
- `dawn.per`
- `escrow.per`
- `events.per`
- `finaling.per`
- `finalingConstants.per`
- `gatherers.per`
- `general.per`
- `interaction.per`
- `orb.per`
- `researches.per`
- `resign.per`
- `scoutcontrol.per`
- `threats.per`
- `trade.per`
- `tsa.per`
- `ugp.per`
- `watercontrol`/water-related behavior
- merge/phase/update support

The repository's existing archaeology has already directly traced a subset of these areas. The remaining source families must not be marked closed merely because a corresponding AEGIS slice exists.

## Red-team interpretation

The module inventory exposes several classes of "basic" behavior that are easy to hide behind broad strategic labels:

1. opening/initialization;
2. specialized food acquisition;
3. construction and placement;
4. worker allocation;
5. interaction/team/operator state;
6. research/upgrade control;
7. scouting and route selection;
8. threat detection;
9. trade/conversion;
10. water/economic theater;
11. terminal/resignation behavior;
12. general state/search machinery;
13. phase/transition machinery;
14. temporal/event machinery.

These are precisely the areas that must be searched for mundane lifecycle behavior such as idle recovery, replacement, target invalidation, queue continuity, repair, fallback, and state reset.

## Important distinction

The current project's canonical HD closure and source-material authority remain those established in the repository's machine/source evidence. This external inventory is corroborative evidence about the shipped source family, not a replacement for the project's immutable stock snapshot.

## Required next archaeology pass

For every module/family, record:

`FILE → RULE/FUNCTION → OBSERVATION → STATE WRITE → STATE READER → GUARD → ACTION → POSTCONDITION → FAILURE → RECOVERY → STRATEGIC PURPOSE → AEGIS OWNER`

No capability should be marked CLOSED from the filename alone.
