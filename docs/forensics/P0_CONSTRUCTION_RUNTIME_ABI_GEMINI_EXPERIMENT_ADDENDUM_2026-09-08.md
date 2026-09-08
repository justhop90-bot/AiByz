# P0 Construction Runtime ABI — Experimental Addendum

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** EXPERIMENTAL PROTOCOL — no runtime claims made

## Purpose

This addendum sharpens the runtime qualification program around three temporal questions identified during independent review.

## Experiment CR-RT-01 — Placement-token persistence

Determine whether `up-build place-control` retains its managed-placement target state across evaluation cycles when authorization conditions temporarily become false.

Controlled sequence:
1. establish placement data;
2. confirm build-line/build authorization;
3. issue managed placement;
4. force a transient escrow/resource authorization failure before physical construction;
5. restore authorization;
6. observe whether the original placement target is retained, cleared, or partially retained.

Required evidence: placement-data state, pending-placement state, command issuance, and resulting foundation/object state across consecutive evaluation cycles.

## Experiment CR-RT-02 — Jump/placement evaluation boundary

Determine whether `up-jump-rule` changes the interpreter frame in which placement registration becomes visible.

Compare otherwise identical rules with and without the jump. Record:
- rule evaluation order;
- placement command issuance;
- pending-placement visibility;
- pending-object visibility;
- subsequent rule eligibility;
- retry count and timing.

Do not infer same-pass semantics from eventual construction success.

## Experiment CR-RT-03 — Builder assignment latency

Determine the temporal relationship between successful placement admission and `up-assign-builders`.

Record the first evaluation/tick in which each becomes observable:
`up-can-build-line → up-build-line → up-assign-builders → pending-placement → foundation/pending-object → builder/task visibility`.

Repeat with a deliberately failed placement to distinguish assignment acceptance from actual builder attachment.

## Experiment CR-RT-04 — Reinitialization control

After a failed or cleared placement attempt, repeat the exact placement initialization sequence. Determine whether reinitialization is mandatory, harmless, or rejected while stale placement state exists.

## Interpretation rules

Results must be classified independently as OBSERVED, CORRELATED, INFERRED, or RUNTIME-QUALIFIED. Static documentation may define command syntax but cannot establish these temporal semantics on the target build.

## Architectural consequence

Until CR-RT-01 through CR-RT-04 are runtime-qualified, AEGIS Construction OS must not assume that placement state survives authorization failure, that jumps preserve required placement frames, or that builder assignment is immediately observable.
