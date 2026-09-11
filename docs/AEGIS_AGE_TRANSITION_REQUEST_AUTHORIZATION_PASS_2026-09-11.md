# AEGIS Age Transition Request / Authorization Pass — 2026-09-11

**Status:** IMPLEMENTED / NOT QUALIFIED
**Reference:** Canonical Lifecycle Contract v0.1
**Scope:** `AegisProm/AEGIS-research-age-v0.per`

## Result

The Age Transition slice now has an explicit request-identity and authorization boundary while preserving its distinct research semantics and engine-facing completion evidence.

```text
WORLD OBSERVATION
  -> AGE-TRANSITION REQUIREMENT / REQUEST
  -> FEASIBILITY
  -> RESEARCH AUTHORIZATION
  -> RESEARCH COMMAND
  -> ENGINE AGE OBSERVATION
  -> WORLD_STATE_VERIFIED / CONFIRMED
```

## Request identity

The existing World Model generation is used as the request-generation identity because the source currently has no separate age-demand writer. The request is created only when the previous lifecycle is inactive.

This is important: a newer World Model snapshot cannot reset an already-issued age-transition request merely because the world model advanced another generation. The lifecycle remains alive until the engine outcome is observed or an explicit failure path invalidates it.

## Research authorization

Feasibility remains separate from authorization.

Authorization requires the existing age-transition conditions:

- `current-age == feudal-age`
- `can-research castle-age`
- food >= 800
- gold >= 200

Those predicates authorize the specific research request; they do not constitute completion evidence.

Authorization carries:

- request identity;
- authorization identity;
- authorization generation;
- authorization validity;
- generation-based expiry state.

The authorization is consumed at `(research castle-age)`, preventing duplicate physical research requests for the same request record.

No native time-based authorization clock has been invented. Generation supersession is the explicit source-level expiry mechanism.

## Verified age-transition evidence

The original and correct completion boundary is preserved:

```text
(current-age >= castle-age)
```

The source records this as `aegis-ra-world-evidence` and `aegis-ra-observed-age`, then transitions to confirmed.

Critically, the implementation does **not** declare success immediately after `(research castle-age)`.

It also does **not** treat continued Feudal age immediately after one command as failure. There is no proven source-level research timeout in this slice, so the lifecycle waits for the actual engine-facing age transition instead of manufacturing a timeout.

## Baseline semantics

`aegis-ra-baseline-age` continues to represent the existing Feudal-to-Castle target baseline (`2`). It is not substituted with `aegis-wm-age`, because the current World Model source initializes `aegis-wm-age` to zero rather than acquiring a verified engine age fact. The civilization-state layer merely consumes that World Model value. Therefore it would be incorrect to upgrade the World Model value into authoritative observed-age evidence.

The verified completion evidence remains the direct `current-age` predicate at the research module's engine-facing boundary.

## Causality

The canonical contract distinguishes:

```text
WORLD_STATE_VERIFIED
```

from a separate causal claim about why the world reached that state.

For Age Transition, observing `current-age >= castle-age` is the required completion evidence for the registry's `WORLD_STATE_VERIFIED` stage. The source does not invent a separate causal-evidence mechanism or claim that the static `.per` rule proves causality beyond that verified engine state.

`aegis-ra-causal-evidence` remains reserved for future engine-proven attribution rather than being falsely set by command issuance.

## Idempotency

The physical research command remains bounded by `aegis-ra-attempts < 1`, and authorization is consumed on dispatch. Re-evaluation therefore cannot issue the same research request repeatedly.

A retry after a failed lifecycle must originate from reassessment with a new request/authorization identity rather than reusing the consumed authorization.

## Important correction made during implementation

The first implementation draft would have treated one issued research request that was still Feudal as immediate failure. That was rejected because no proven timeout exists. It would have conflated `not yet observed` with `failed` and violated the evidence rules.

The final source therefore waits for the actual `current-age >= castle-age` transition.

## Qualification status

**NOT QUALIFIED.**

The canonical boundary is implemented, but registry promotion still requires target-build runtime/engine evidence and the broader reassessment/qualification chain. This pass does not manufacture evidence or promote the slice merely because the source is structurally complete.
