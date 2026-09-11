# AEGIS Lifecycle Invariant Repair Pass — 2026-09-11

**Status:** IMPLEMENTATION PASS / QUALIFICATION STILL BLOCKED
**Scope:** `main/AegisProm`
**Authority:** `docs/AEGIS_CANONICAL_LIFECYCLE_CONTRACT_V0_1.md`

## Executive result

This pass repairs the two concrete cross-slice lifecycle defects that were safe to correct without inventing new engine semantics:

1. **Active-request idempotency:** Worker Task Command and Villager Production now require their local lifecycle to be invalid (`valid == 0`) before admitting a newer upstream generation. A newer observation/demand cannot overwrite an outstanding physical lifecycle.
2. **Authorization supersession expiry:** authorization validity is now invalidated against the **upstream owner's generation**, rather than comparing authorization generation with the same local generation copied into the authorization record. This makes generation supersession an effective source-level expiry mechanism without inventing a wall-clock timer.

The same supersession-expiry correction was applied to Housing, Age Transition, Anti-Cavalry, and Tactical Micro Execution Bridge.

## Repairs

| Slice | Repair | Result |
|---|---|---|
| Worker Economy / Task Command | admission requires `aegis-wtc-valid == 0` | **FIXED** |
| Worker Economy / Task Command | authorization expires when WTS generation advances | **FIXED** |
| Villager Production | admission requires `aegis-vp-valid == 0` | **FIXED** |
| Villager Production | authorization expires when civilian-demand generation advances | **FIXED** |
| Housing | authorization expires when civilian-demand generation advances | **FIXED** |
| Age Transition | authorization expires when World Model generation advances | **FIXED** |
| Anti-Cavalry | authorization expires when threat generation advances | **FIXED** |
| Tactical Micro / Execution Bridge | authorization record now binds to Micro Control generation; expiry follows Micro Control supersession | **FIXED** |

## Semantic ownership preserved

No repaired module writes another module's lifecycle state as a shortcut.

- EDA remains owner of economic arbitration request identity.
- WTS remains owner of worker-selection request identity.
- WTC remains owner of physical worker-task authorization/dispatch boundary.
- VP remains owner of villager-production authorization/dispatch boundary.
- Housing remains owner of housing construction lifecycle.
- Age Transition remains owner of research/age-transition lifecycle.
- Anti-Cavalry remains owner of its bounded physical production endpoint.
- Tactical Micro Execution Bridge remains the authorization bridge; the physical adapter remains the physical command owner.
- Military Production remains a separate blocked candidate and was not used as an incidental repair target.

## Evidence discipline

No repair converts command issuance, pending queue state, or numeric count change into causal proof.

In particular:

- `can-train` remains feasibility, not authorization or completion.
- `up-train` remains physical action, not success.
- pending objects remain pending evidence.
- observed capability counts remain world-state evidence unless a separate causal writer exists.
- Age Transition continues to use engine-facing `current-age` as its completion evidence.

## Expiry policy

The repaired expiry condition is **generation supersession**, not native time expiry.

A source authorization is valid only while the generation of the upstream request it authorized remains current. When the upstream owner publishes a newer generation, the downstream authorization fails closed.

This is deliberately weaker than a proven game-time timer and must not be described as a native timer-based authorization timeout.

## Remaining lifecycle blockers

The following are intentionally **not** claimed fixed by this pass:

### 1. Canonical reassessment publication

Most verticals still terminate by local invalidation or local terminal state. The repository contract requires a normalized reassessment boundary after consequential success, failure, expiry, recovery, or material contradiction. No new cross-module writer was invented merely to make the audit look green.

### 2. Causal verification

Housing, Villager Production, Anti-Cavalry, and Military Production still lack a generally proven request-specific causal writer. World-state change must remain distinct from causal attribution.

### 3. Military Production qualification

`AEGIS-military-production-v0.per` remains `CANDIDATE_BLOCKED`. Its selector/authorization lifecycle has not been promoted by these repairs.

### 4. Runtime/engine qualification

The source repairs are static architectural corrections. They do not constitute target-build qualification of every `.per` operation or prove timer/goal ABI behavior at runtime.

## Qualification posture

The lifecycle gate therefore moves from:

> **P0/P1 active-request and inert-expiry defects**

to:

> **ACTIVE-REQUEST IDEMPOTENCY: REPAIRED**  
> **GENERATION-SUPERSESSION EXPIRY: REPAIRED**  
> **CAUSAL VERIFICATION: OPEN**  
> **CANONICAL REASSESSMENT: OPEN**  
> **MILITARY PRODUCTION: CANDIDATE BLOCKED**  
> **RUNTIME QUALIFICATION: OPEN**

No qualification promotion is implied by this pass.
