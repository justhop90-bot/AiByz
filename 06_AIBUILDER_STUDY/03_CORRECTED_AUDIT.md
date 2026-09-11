# AiBuilder Corrected Static Audit — ByzBot Part One, Revision 2

**Status:** Study record / substrate audit
**Authority:** Evidence-first; no Byzantine production code authorized by this document.
**Source:** User-supplied `ByzBot Part One, Corrected: The AiBuilder Execution Contract and Revised Static Audit`.

## Purpose

This document records the corrected substrate audit supplied by the co-scripter. It is preserved as an audit input, not automatically promoted to repository fact. Claims below retain the source's evidence classifications and must remain distinguished from independently verified repository findings.

## Methodological rules

1. **Not found is not does not exist.** A primitive absent from the current corpus is unconfirmed, not disproven.
2. **Goal allocation is not assumed to be automatic.** New symbolic Goal names require an established allocation mechanism before production use.
3. **Shared scratch Goals require temporal read/write analysis.** Numeric/name reuse is not itself a collision verdict.
4. **Static soundness is distinct from runtime semantics.** A source repair can be statically coherent while its engine-time behavior remains unvalidated.
5. **Do not globally replace `unit-type-count` with `unit-type-count-total`.** The corrected audit concludes the upgrade rules in `technologies.per` intentionally test the specific unit type to which each upgrade applies.
6. **Enemy infrastructure observation is not enemy army composition.** Building observations should be modeled as evidence supporting a belief, not as direct observation of units.
7. **Primitive existence and primitive semantics are separate confidence dimensions.**
8. **Selector syntax requires evidence.** `any-enemy` must not be generalized from other selectors without support.
9. **Timer allocation must be established before adding new timers.**
10. **Byzantine thresholds are strategy hypotheses, not reverse-engineering discoveries.**
11. **Prefer policy modification over duplicated production machinery.**

## Corrected `temporary-goal` finding

The audit performs a temporal read/write review of `temporary-goal` in `general.per`, `construction.per`, and `militaryBehavior.per`. Under the stated load order, it classifies the current reuse as **SAFE REUSE**, conditional on preserving load order and preventing an intervening writer.

**Engineering constraint:** A future Byzantine policy module should not use `temporary-goal`; it should receive an independently allocated namespace once Goal allocation is established.

## Corrected phase-policy finding

`previous-phase` has no writer in the examined corpus. The audit therefore classifies the phase configuration behavior as a direct static defect, while explicitly separating that finding from the engine's same-pass evaluation semantics.

Proposed repair:

```text
(set-goal previous-phase current-phase)
```

The repair is classified as **STATICALLY SOUND / RUNTIME REQUIRES VALIDATION**.

## Corrected technology finding

The blanket recommendation to replace `unit-type-count` with `unit-type-count-total` in `technologies.per` is rejected by the audit. The upgrade chain checks the concrete unit type to which each technology applies (for example militia → man-at-arms → long swordsman → two-handed swordsman → champion). The source argues that this is the correct condition for deciding whether enough applicable units exist to justify the upgrade.

**Disposition:** No technology change is authorized from this claim alone.

## Enemy-observation boundary

The audit distinguishes:

`OBSERVATION → BELIEF → CONFIDENCE → ACTION`

from treating an infrastructure observation as direct army-composition evidence.

It classifies the following as unconfirmed from the supplied corpus:

- `players-building-type-count any-enemy <building> ...`
- `players-unit-type-count any-enemy <unit> ...`
- new timer allocation mechanism
- new Goal allocation mechanism
- engine signal emission relied upon by `event-detected trigger`

This means Byzantine counter-unit logic must not be implemented using those forms until independently established.

## Module execution contract captured by the audit

### `phaseUpdate.per`

- Produces the phase-dependent `desired-*` policy goals and upgrade/training policy inputs.
- Mutates `current-phase`.
- `previous-phase` is identified as unwritten.
- Configuration rules currently recur because of that defect.

### `economy.per`

- Consumes desired economy goals.
- Projects them into gatherer strategic numbers.
- Contains an unconditional `(true)` rule that rewrites those SNs every pass.
- The audit classifies this as a direct static finding and proposes dirty-state gating.

### `construction.per`

- Consumes desired building policy.
- Performs feasibility checks and building-placement actions.
- Uses a substantial scratch/search-state mechanism.
- Farm placement is classified as a maintainability concern, not proven functionally broken.

### `militaryUnits.per`

- Consumes desired unit-count goals.
- Uses `can-train` before issuing training actions.
- The audit does not promote assumptions about generic unique-unit handling without tracing the underlying definitions.

### `technologies.per`

- Consumes upgrade policy goals.
- Uses escrow and research feasibility.
- The corrected audit finds no basis for the earlier blanket `unit-type-count` replacement.

### `militaryBehavior.per`

- Consumes attack/spread policy and timing state.
- Writes relevant strategic numbers and attack actions.
- Uses timers to gate behavior.
- No confirmed defect is claimed by this audit.

### `market.per`

- Reacts to resource/price conditions.
- Buys/sells commodities.
- The audit characterizes it as crisis-reactive rather than identifying that as a correctness defect.

### `general.per`

- Projects explorer policy into strategic numbers.
- Performs search/group management.
- Reuses scratch Goals and search state.
- The audit flags unconditional search setup as a minor performance concern, not a correctness defect.

## Evidence register from the supplied audit

| ID | Finding | Classification | Disposition |
|---|---|---|---|
| D-01 | `previous-phase` not written | DIRECT STATIC | Confirmed by supplied audit; runtime repair still requires validation |
| D-02 | unconditional economy SN rewrite | DIRECT STATIC | Confirmed by supplied audit; repair requires validation |
| D-03 | outpost rule writes `desired-number-docks` | DIRECT STATIC | Confirmed by supplied audit; source location should be independently rechecked before edit |
| D-04 | difficulty-specific constants appear undefined in examined corpus | DIRECT STATIC | Must distinguish repository-wide absence from local absence before repair |
| D-05 | signal emission uncertain | DIRECT/UNCERTAIN | Do not rely on signal path without evidence |
| DP-01 | blanket `unit-type-count` replacement | DISPROVEN | Rejected |
| DP-02 | farm spiral must be deleted | DISPROVEN AS STATED | Retain pending functional evidence |
| UC-01 | enemy building-type selector | UNCONFIRMED | Block production use |
| UC-02 | enemy unit-type count | UNCONFIRMED | Block production use |
| UC-03 | new timer allocation | UNCONFIRMED | Block new timers |
| UC-04 | new Goal allocation | UNCONFIRMED | Block new Goals |
| UC-05 | signal emission | UNCERTAIN | Block reliance |

## Important audit limitation

The supplied document itself states that its load-order conclusion is partly based on the prior directive rather than a complete independent reading of `AiBuilder.per`. Therefore this record **does not promote that load order to final repository fact by itself**. The next study pass must inspect the actual current root file and all loaded modules directly and reconcile the result.

## Gate

**Gate status: NOT PROMOTED TO IMPLEMENTATION AUTHORITY.**

Before Byzantine policy code is written, the AiBuilder study should establish from the actual current repository:

1. complete root load order;
2. Goal allocation/binding mechanism;
3. timer allocation/binding mechanism;
4. complete Goal/SN/timer writer-reader matrix;
5. command widths for multi-Goal operations;
6. cross-module scratch-state lifetimes;
7. primitive syntax and semantic confidence;
8. phase-policy write timing;
9. unresolved symbol definitions across the full composition root.

This document is therefore a **study artifact and audit baseline**, not a green light for Part Two.
