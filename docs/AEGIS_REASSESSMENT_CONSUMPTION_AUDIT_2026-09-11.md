# AEGIS REASSESSMENT downstream-consumption audit — 2026-09-11

## Finding

The villager-production vertical now has an explicit downstream REASSESS acknowledgement boundary in the civilian-demand owner. The implementation preserves the required evidence direction:

`terminal lifecycle generation -> REASSESS publication -> one acknowledgement -> newer civilization-state generation -> new demand generation -> new production request`

REASSESS itself does **not** create or increment a generation.

## Civilian-demand acknowledgement

`AegisProm/AEGIS-civilian-demand-v0.per` now owns two local acknowledgement fields:

- `aegis-civ-reassess-generation = 774`
- `aegis-civ-reassess-valid = 775`

The acknowledgement rule requires all of the following:

1. villager reconciler has published `aegis-vr-reassess-valid == 1`;
2. the published generation equals the reconciler's current lifecycle generation;
3. the civilian-demand acknowledgement generation differs from the published generation.

The consumer then records the exact lifecycle generation, marks its local acknowledgement state, and clears the publisher's one-shot publication token. It does not increment `aegis-civ-demand-generation`.

This establishes one-consumption semantics without creating a central controller.

## New-generation gate

The civilian-demand generation transition remains owned by civilization state:

`aegis-cs-valid == 1` AND `aegis-cs-generation != aegis-civ-demand-generation`

Only then may civilian demand copy the newer civilization-state generation into `aegis-civ-demand-generation`.

Therefore the forbidden path is structurally absent:

`REASSESS -> increment demand generation -> repeat old request`

The accepted path is:

`REASSESS acknowledgement -> wait -> newer civilization-state generation -> demand regeneration`

## Villager-production end-to-end audit

### 1. World observation

Civilization state consumes the published World Model only when its generation differs, then copies the World Model snapshot and publishes a qualified civilization-state generation. This is the authoritative upstream observation boundary.

### 2. Civilian demand

Civilian demand consumes only a qualified civilization-state generation that differs from its own generation. It resets typed demand and then derives villager/housing demand from the new state.

### 3. Production admission

Villager production requires:

- qualified civilian stage;
- villager demand needed;
- `aegis-vp-valid == 0`;
- production generation different from civilian-demand generation.

This prevents a newer demand from overwriting an active production lifecycle.

### 4. Request identity

The production lifecycle copies the civilian-demand generation into its request identity. Authorization identity is likewise tied to that generation.

### 5. Authorization

Authorization is explicit and single-use. Physical dispatch requires authorization validity, correct stage/action, engine train feasibility, and a real Town Center endpoint. Dispatch uses `up-train escrow-state c: villager`.

### 6. Pending state

Pending queue admission is treated as intermediate evidence. It does not equal completed villager creation.

### 7. Completion verification

The lifecycle reconciler compares the census villager count against the pre-dispatch baseline and requires request/authorization identity agreement plus explicit causal evidence before entering confirmed state.

### 8. Causal-verification blocker remains real

The source initializes `aegis-vr-causal-evidence` to zero and tests it for one before confirmation, but the source audit finds no writer that establishes that evidence. Therefore the vertical still cannot claim proven causal completion from a concurrent census increase.

This is a deliberate fail-closed condition, not an implementation defect to be hidden.

### 9. REASSESS publication

Confirmed and failed terminal reconciler states publish the lifecycle generation through `aegis-vr-reassess-generation` / `aegis-vr-reassess-valid`.

### 10. REASSESS consumption

Civilian demand now acknowledges that exact published generation once and clears the one-shot publication token. A second pass cannot acknowledge the same token because the token has been consumed and the acknowledgement generation already matches it.

### 11. Next-cycle authorization

A new production request cannot be created merely because REASSESS occurred. Civilization state must first publish a genuinely newer generation, civilian demand must consume that generation, and only then can villager production admit a new lifecycle.

## Invariant audit

| Invariant | Result |
|---|---|
| REASSESS is not a generation source | **PASS** |
| Civilian demand acknowledges exact VR generation | **PASS — source-level** |
| Duplicate acknowledgement blocked by generation identity | **PASS — source-level** |
| New demand requires newer civilization-state generation | **PASS — source-level** |
| Active villager request cannot be overwritten | **PASS — source-level** |
| Physical authorization is single-use | **PASS — source-level** |
| Pending is not completion | **PASS** |
| Completion requires causal evidence | **PASS — fail-closed** |
| Causal evidence has a proven writer | **NO — blocker remains** |
| Target-build runtime qualification | **NOT EXECUTED** |

## Test coverage added

`tests/vertical_slices/test_reassessment_consumption_contract.py` now checks:

- civilian REASSESS acknowledgement identity;
- one-shot publisher-token consumption;
- upstream-only demand generation advancement;
- active villager request protection;
- single-use production authorization;
- absence of causal-evidence fabrication;
- villager REASSESS publication;
- existing no-central-controller and military-production candidate gates.

These are static source-contract tests. They do not constitute AoE2DE target-build runtime qualification.

## Promotion decision

**Civilian-demand REASSESS consumption: IMPLEMENTED at source-contract level.**

**Villager-production REASSESS loop: ARCHITECTURALLY CLOSED against stale-generation and duplicate-request shortcuts.**

**Villager-production vertical: NOT FULLY QUALIFIED.** The remaining qualification blocker is explicit causal attribution from the physical villager train request to a later census increase. No causal evidence is manufactured to close that gap.

The next vertical may therefore be audited using the same pattern, while this vertical remains honest about the distinction between command issuance, queue admission, world-state observation, causal verification, and strategic success.
