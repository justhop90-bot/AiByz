# AEGIS Civilian Vertical Slice Contract V0 — 2026-09-09

**Status:** Working contract for the first production-oriented vertical slice  
**Authority parent:** FINAL_RECONSTRUCTION_AUDIT + Forward Engineering Manual Rev 2  
**Choice rationale:** The existing `implementation/*.per` candidates already concentrate on the civilian/economic loop. This is the natural first slice.

## Slice goal (plain language)

Produce a bounded, observable civilian production + worker-demand loop that:

1. Observes current villagers and pending production (census).
2. Decides whether more villagers are needed (demand).
3. Issues at most a bounded number of train commands.
4. Distinguishes issued → pending → confirmed (or failed) using generation fencing.
5. Does **not** claim strategic effect beyond “a villager was requested and the engine showed pending / census change”.

## In-scope modules (current candidates)

- Civilian census
- Civilization / civilian demand
- Villager production
- Civilian lifecycle reconciler
- (Supporting) worker-role census / vector and economic demand arbitration as pure demand signals

## Out of scope for this slice

- Full economic scheduler / optimal gatherer ratios
- Source and dropsite selection quality
- Construction OS
- Military / threat / camel response
- Any claim of long-term strategic improvement

## Required observable evidence (minimum for “slice works”)

| Stage | Required evidence |
|-------|-------------------|
| Census | Engine fact read for villager count + pending-objects signal published with generation |
| Demand | A generation-stamped demand flag set only when policy says “need villager” |
| Issue | `can-train` + train/up-train command under bounded attempts |
| Pending | `up-pending-objects` (or equivalent) shows pending villager |
| Confirm / Fail | Census increase above baseline **or** explicit failure when pending disappears without increase |

## Explicit non-claims

- Pending ≠ completed villager.
- Command issued ≠ accepted by engine.
- This slice does not prove the full command lifecycle for all unit types.
- No numeric channel used by the slice is production-cleared.

## Success definition (Go criteria)

1. On the target build, a controlled single-TC game shows the full issued → pending → confirmed (or clean failure) path at least three times with logged evidence.
2. All channels used by the slice appear in the ownership inventory with generation + validity.
3. Residual risk document is updated with the actual probe results.

## Failure / residual-risk definition

If pending or census signals cannot be observed reliably, the slice remains candidate-only and production coding stays blocked for any module that assumes later lifecycle stages.

## Relationship to Cavalry Threat Containment

Cavalry → camel remains a high-value strategic slice. It is deliberately sequenced after the civilian loop has demonstrated basic command-lifecycle observability, because the same lifecycle questions apply to military production.
