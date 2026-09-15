# Goal Registry

This is the authoritative schema for AEGIS goal-channel ownership. It is **not** a declaration that any numeric value is currently cleared.

| Goal | Owner | Purpose | Read/Write | Lifecycle | Valid range | Reserved? | Collision status | Source/evidence |
|---|---|---|---|---|---|---|---|---|
| — | — | Registry row placeholder | — | — | — | — | NOT ALLOCATED | ABI gate |

## Allocation rule

A goal becomes `ALLOCATED` only after stock occupancy, writer/reader usage, validator behavior, target-build semantics, ownership, lifecycle, and collision review all agree. Numeric gaps alone never authorize allocation.

## Current protected design channels

The AEGIS foundation conceptually reserves symbolic channels for world model, belief, situation, objectives, planning, decision, commitment, execution, verification, recovery, services, sensors, economy, and military state. Their numeric mapping remains subject to the ABI gate.
