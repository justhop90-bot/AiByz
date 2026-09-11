# REASSESSMENT IMPLEMENTATION STATUS

The seven verticals have generation-keyed local AegisProm REASSESS publication. Downstream consumption is being closed one upstream boundary at a time rather than through a central reassessment controller.

Current downstream consumption implemented at source-contract level:

- Villager Production → Civilian Demand
- Housing → Civilian Demand
- Worker Economy → Worker Role Vector
- Age Transition → Civilization State
- Anti-Cavalry → Scouting/Threat
- Tactical Micro → Micro Control
- Military Production candidate → Scouting/Threat

The Anti-Cavalry pass also repaired a previously omitted source namespace collision between Age Transition `600–612` and Scouting/Threat `610–617`. Scouting/Threat now owns `642–649`; Anti-Cavalry failure state is explicitly allocated at `650`; Anti-Cavalry REASSESS acknowledgement uses `782–783`.

The Tactical Micro pass uses `784–785` for Micro Control acknowledgement of Micro Verification REASSESS.

The Military Production pass uses `786–787` for Scouting/Threat acknowledgement of Military Production REASSESS. This is lifecycle consumption only and does not promote the candidate.

Qualification boundaries remain independent of reassessment consumption. Military Production remains `CANDIDATE_BLOCKED / NOT_QUALIFIED` because its source selector `aegis-mp-unit` is not initialized. Causal evidence and target-build runtime evidence also remain open.

See `docs/AEGIS_MILITARY_PRODUCTION_REASSESSMENT_CONSUMPTION_PASS_2026-09-11.md` for the Military Production audit boundary.
