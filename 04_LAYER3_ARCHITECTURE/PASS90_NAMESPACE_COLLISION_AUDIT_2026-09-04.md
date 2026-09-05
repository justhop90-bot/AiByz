# AEGIS Layer 3 — Pass 90 Namespace Collision Audit

Date: 2026-09-04
Status: OPEN / PRE-CODE GATE

## 1. Finding

The previous `G0–G511` compatibility allocation is rejected as an implementation allocation. It is only a historical compatibility range. Official evidence documents strategic numbers through 511 and a later goal expansion to 16000, so goals and strategic numbers must be treated as separate, build-sensitive namespaces. citeturn0search1turn1search2

## 2. Collision domains

Before any `.per` implementation, audit all of:

1. imported `defconst` goal IDs;
2. imported strategic-number constants;
3. flags;
4. timer IDs (0–49 historical limit in project evidence);
5. search IDs / search state variables;
6. temporary/scratch goals;
7. historical AI state channels retained by the package;
8. Porphyra baseline channels if the implementation imports any of them;
9. engine-reserved constants;
10. validator profile expectations;
11. project-owned AEGIS ABI symbols.

## 3. Namespace policy

- A goal ID is never reused because it is merely unused in one file.
- An SN ID is never assumed compatible with a goal ID.
- A scratch channel must be explicitly marked scratch and have a lifetime/consumer contract.
- A migrated legacy constant keeps its identity unless a deliberate adapter remaps it.
- Symbolic names are canonical; numeric assignments are generated/audited artifacts.
- Every assignment records source, build scope, owner, readers, writers, and collision status.

## 4. Required audit record

Each allocation must have:

`symbol | channel | numeric_id | source | owner | readers | writers | lifetime | sentinel | build_min | build_max_tested | validator_status | collision_status`

Collision status values:

- `CLEAR`
- `COLLIDES_LEGACY`
- `COLLIDES_ENGINE`
- `COLLIDES_VALIDATOR`
- `BUILD_DEPENDENT`
- `UNRESOLVED`

Only `CLEAR` may enter implementation.

## 5. Build profiles

A profile must identify:

`profile_id, build_min, build_max_tested, goal_range, sn_range, timer_range, supported_primitives, validator_profile, known_incompatibilities`

The project may not call an engine primitive “supported” merely because the current validator accepts its syntax. Engine support, validator support, and AEGIS implementation support are independent columns.

## 6. Immediate gate

**NO CODE ALLOCATION YET.** The authorized workstation is currently unreachable at the filesystem/process layer, so live extraction of the installed AI constants cannot be completed. This document therefore defines the audit contract but does not falsely declare the namespace collision-free.

The next implementation-enabling action is to obtain the authoritative constant inventory from the workstation or an equivalently authoritative project snapshot, then generate the concrete allocation table.
