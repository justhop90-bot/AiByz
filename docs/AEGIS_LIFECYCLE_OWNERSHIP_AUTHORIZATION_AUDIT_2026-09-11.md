# AEGIS Lifecycle Ownership + Physical Authorization Audit — 2026-09-11

## Executive result

A repository-wide audit was performed across all seven registered verticals while preserving the existing REASSESS publication/consumption boundaries.

Result: **two ownership defects were found and repaired, and one authorization gap was found and hardened.**

The defects were:

1. Tactical Micro physical adapter mutated Micro Control lifecycle state and attempt count. The adapter now publishes its own dispatch evidence; Micro Control alone advances its lifecycle and owns its attempt counter.
2. Housing Construction directly cleared `aegis-civ-housing-demand`, mutating Civilian Demand policy state from a downstream executor. Housing now publishes terminal state only; Civilian Demand remains the policy owner and consumes REASSESS.
3. Military Production had physical production without an explicit request/authorization boundary. It now has request identity, authorization identity/generation/valid/expiry and requires current authorization at dispatch. It remains candidate-blocked and is not promoted.

## Normative ownership rule

For every vertical:

```text
UPSTREAM OBSERVATION/DEMAND
    ↓
LIFECYCLE OWNER
    ↓
REQUEST IDENTITY
    ↓
FEASIBILITY
    ↓
AUTHORIZATION OWNER
    ↓
PHYSICAL ACTION / ADAPTER
    ↓
AUTHORIZATION CONSUMED
    ↓
PENDING / WORLD OBSERVATION
    ↓
VERIFICATION OWNER
    ↓
REASSESS PUBLICATION
    ↓
DOWNSTREAM ACKNOWLEDGEMENT
    ↓
NEW UPSTREAM GENERATION
```

A module may consume another module's published evidence/token where the contract explicitly assigns that acknowledgement, but it must not silently become the owner of the producer's lifecycle state.

## Seven-vertical audit

### 1. Worker Economy

Path:
`WRC → WRV → Economic Demand → Arbitration → Target Selection → Task Command → Task Verification → REASSESS → WRV`

Lifecycle ownership remains distributed. WTV owns verification and REASSESS publication; WRV acknowledges it. WTC owns physical task dispatch and its authorization. WTV does not authorize a second command.

Physical actions are guarded by WTC authorization validity, request identity and current generation. Authorization is consumed on dispatch. Food remains fail-closed because no dedicated food adapter exists.

Result: **PASS at source-contract level.** Causal productivity remains unproven.

### 2. Villager Production

Path:
`Civilization State → Civilian Demand → Villager Production → Census/Reconciler → REASSESS → Civilian Demand`

VP owns request/authorization and physical `up-train escrow-state c: villager`. The reconciler owns completion verification and publishes REASSESS. Civilian Demand acknowledges the exact terminal generation.

Pending queue evidence is not completion. Causal evidence remains explicitly required and currently lacks a proven writer.

Result: **PASS at source-contract level.**

### 3. Housing

Path:
`Civilization State → Civilian Demand → Housing Construction → world observation → REASSESS → Civilian Demand`

Housing owns its lifecycle and authorization. During this audit a downstream-policy ownership defect was found: HC had directly cleared `aegis-civ-housing-demand` on confirmation. That mutation has been removed. Civilian Demand now remains the sole owner of its policy field.

Physical `(build house)` requires current housing authorization and consumes that authorization. World evidence and causal evidence remain distinct.

Result: **PASS after ownership repair at source-contract level.** Causal attribution remains open.

### 4. Age Transition

Path:
`World Model → Age Transition → research authorization → research → current-age verification → REASSESS → Civilization State`

RA owns request/authorization. Physical `research castle-age` requires current engine feasibility and authorization. Completion uses direct engine-facing `current-age >= castle-age`, not command issuance.

Civilization State acknowledges only when the RA lifecycle generation exactly matches the current CS frame. REASSESS does not create a new CS generation.

Result: **PASS at authorization/reassessment level.** Authoritative World Model age observation remains a separate blocker.

### 5. Anti-Cavalry

Path:
`Scouting/Threat → Cavalry Response → feasibility → authorization → spearman production → pending/world evidence → REASSESS → Scouting/Threat`

CR owns request and authorization identity. Physical `up-train escrow-state c: spearman-line` requires current authorization and consumes it. ST acknowledges terminal CR generations exactly once.

A spear-count increase remains world-state evidence, not causal proof. No causal evidence is manufactured.

Result: **PASS at source-contract level.** Runtime and causality remain open.

### 6. Tactical Micro

Path:
`World Model → Micro Control → targeting/geometry/governor → Execution Bridge → Physical Adapter → Micro Verification → REASSESS → Micro Control`

The audit found an actual ownership defect: the physical adapter was writing `aegis-mc-stage` and `aegis-mc-attempts`. Those fields belong to Micro Control.

Repair:
- physical adapter now owns only dispatch evidence fields `793–794`;
- dispatch evidence is keyed to the MC request generation;
- MC consumes that evidence and alone advances `authorized → issued` and increments attempts;
- MV only verifies and publishes REASSESS;
- MC consumes MV REASSESS and closes its own lifecycle.

The Execution Bridge continues to own tactical authorization. The physical adapter consumes authorization and clears it after dispatch. Pursuit remains unqualified as a separate physical capability.

Result: **PASS after ownership repair at source-contract level.** Command-to-world-effect qualification remains open.

### 7. Military Production

Path:
`Scouting/Threat → Military Production candidate → feasibility → authorization → production → pending/observation → REASSESS → Scouting/Threat`

The audit found that the candidate's physical production had no explicit authorization identity. That gap is now hardened with:
- request ID `788`;
- authorization ID `789`;
- authorization generation `790`;
- authorization valid `791`;
- authorization expiry `792`.

Physical spearman production requires authorization validity, authorization-generation equality with the current ST generation, authorization/request identity equality, attempt bound, and engine feasibility. Authorization is consumed on dispatch.

This change does **not** promote the candidate. Selector initialization remains unresolved and causal evidence is still insufficient.

Result: **PASS for authorization boundary; candidate remains NOT_QUALIFIED.**

## REASSESS preservation audit

All seven existing publisher/consumer boundaries remain intact:

- WTV → WRV
- VR → CIV
- HC → CIV
- RA → CS
- CR → ST
- MV → MC
- MP → ST

Consumers acknowledge exact published lifecycle generations and consume one-shot publisher tokens. No consumer increments or manufactures its upstream observation generation.

The audit deliberately did not replace the distributed design with a central reassessment controller.

## Evidence gates preserved

The following remain normative:

- command issuance is not completion;
- queue admission is not completion;
- world-state change is not automatically causal attribution;
- unknown and failed outcomes receive no success credit;
- REASSESS is not strategic success;
- REASSESS is not authorization;
- REASSESS does not choose the next strategy;
- a candidate vertical cannot promote itself through a successful-looking trace;
- target-build runtime evidence remains separate from source-contract evidence.

## Namespace result

The namespace map was extended for:
- `788–792` Military Production authorization;
- `793–794` Micro Physical Adapter dispatch evidence.

No existing reassessment allocation was reused.

## Test coverage

Added:
`tests/vertical_slices/test_lifecycle_ownership_authorization_audit.py`

The tests check all seven REASSESS boundaries, exact consumer identities, Tactical Micro ownership separation, Military Production authorization, Housing policy ownership, authorization consumption across physical actions, absence of REASSESS generation shortcuts, and absence of a monolithic reassessment controller.

These are static source-contract tests. No target-build runtime qualification is claimed.

## Final disposition

**Lifecycle ownership: CLOSED at source-contract level after repairs.**

**Physical authorization: CLOSED for the seven current physical-action boundaries, with Military Production hardened but still candidate-blocked.**

**REASSESS boundaries: PRESERVED.**

**Evidence gates: PRESERVED.**

**Qualification: NOT promoted.** Existing causal, runtime, selector, and authoritative-observation blockers remain explicit.
