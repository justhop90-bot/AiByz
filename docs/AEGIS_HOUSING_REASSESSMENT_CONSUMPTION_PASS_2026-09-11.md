# AEGIS Housing REASSESSMENT Consumption Pass — 2026-09-11

## Scope

This pass audits and implements downstream consumption of the housing vertical's terminal REASSESS publication.

The housing lifecycle publisher is `AEGIS-housing-construction-v0.per`, which publishes the terminal lifecycle generation through goals 764/765. The consumer is the existing civilian-demand owner, `AEGIS-civilian-demand-v0.per`.

## Normative cycle

`housing lifecycle generation -> REASSESS publication -> one civilian-demand acknowledgement -> newer civilization-state generation -> new civilian-demand generation -> new housing request`

REASSESS itself never increments `aegis-civ-demand-generation` and never selects the next housing action.

## Implementation

Added to `AEGIS-civilian-demand-v0.per`:

- `aegis-civ-housing-reassess-generation = 776`
- `aegis-civ-housing-reassess-valid = 777`

The acknowledgement requires:

1. `aegis-hc-reassess-valid == 1`;
2. published housing generation equals the housing lifecycle generation;
3. the civilian-demand acknowledgement generation differs from the published housing generation.

On acknowledgement, civilian demand records the exact housing lifecycle generation, marks its local acknowledgement state, and clears the housing publisher token. It does not advance the civilian-demand generation.

## New-generation ownership

The only civilian-demand generation advance remains:

`qualified civilization-state generation != current civilian-demand generation`

followed by copying `aegis-cs-generation` into `aegis-civ-demand-generation`.

Therefore the housing REASSESS event cannot manufacture a fresh demand generation or recreate a stale housing request.

## Duplicate/stale protections

Housing admission already requires both:

- `aegis-hc-generation != aegis-civ-demand-generation`
- `aegis-hc-valid == 0`

The request identity is copied from the civilian-demand generation. Consequently a terminal housing lifecycle cannot overwrite an active lifecycle, and the same civilian-demand generation cannot create a second housing lifecycle after terminal reassessment.

## Evidence boundary retained

The housing module observes a real increase in house count as world evidence, but it does not equate that observation with causal success. Confirmation still requires `aegis-hc-causal-evidence == 1`; otherwise the lifecycle fails closed with `aegis-hc-failure-causality-unproven`.

No causal-evidence writer was invented in this pass.

## Validation

Added:

`tests/vertical_slices/test_housing_reassessment_consumption.py`

The tests verify:

- generation-keyed housing publication;
- exact one-shot acknowledgement;
- no generation creation at REASSESS;
- civilization-state ownership of new demand generations;
- active-request protection;
- single-use authorization;
- world-evidence versus causal-evidence separation;
- absence of a housing/global reassessment controller.

These are static source-contract tests, not target-build runtime qualification.

## Promotion status

**Housing REASSESS downstream consumption: IMPLEMENTED at source-contract level.**

**Housing vertical: NOT FULLY QUALIFIED.** Causal attribution remains an independent blocker, and no claim of engine-runtime success is made by this pass.

The architecture remains distributed: housing publishes its own terminal result; civilian demand acknowledges it; civilization state owns the next genuine observation generation; housing production owns consequential execution.
