# REASSESSMENT IMPLEMENTATION STATUS

The seven verticals have generation-keyed local REASSESS publication. Downstream consumption is being closed one upstream boundary at a time rather than through a central reassessment controller.

Current downstream consumption implemented at source-contract level:

- Villager Production → Civilian Demand
- Housing → Civilian Demand
- Worker Economy → Worker Role Vector
- Age Transition → Civilization State
- Anti-Cavalry → Scouting/Threat

The Anti-Cavalry pass also repaired a previously omitted source namespace collision between Age Transition `600–612` and Scouting/Threat `610–617`. Scouting/Threat now owns `642–649`; Anti-Cavalry failure state is explicitly allocated at `650`; Anti-Cavalry REASSESS acknowledgement uses `782–783`.

Remaining downstream consumers:

- Tactical Micro
- Military Production candidate

These must retain their existing qualification boundaries and must not be promoted merely because a REASSESS consumer is implemented.

See `docs/AEGIS_ANTI_CAVALRY_REASSESSMENT_CONSUMPTION_PASS_2026-09-11.md` for the Anti-Cavalry audit boundary.
