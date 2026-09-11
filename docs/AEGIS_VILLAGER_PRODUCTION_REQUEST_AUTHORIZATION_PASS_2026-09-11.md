# AEGIS Villager Production — Canonical Request/Authorization Pass

**Date:** 2026-09-11  
**Status:** IMPLEMENTED BOUNDARY / NOT QUALIFIED  
**Reference:** Canonical lifecycle contract v0.1  
**Purpose:** Apply the Worker Economic request-identity and authorization pattern to Villager Production without collapsing queue admission into completion.

## 1. Normative lifecycle

```text
CIVILIAN DEMAND
→ REQUEST ID
→ AUTHORIZATION
→ PHYSICAL TRAIN
→ PENDING / QUEUE ADMISSION
→ WORLD-STATE OBSERVATION
→ CAUSAL VERIFICATION
→ CONFIRMED
→ REASSESS
```

Failure remains fail-closed and must be recovered/reassessed by the appropriate higher-level owner.

## 2. Request identity

`aegis-civ-demand-generation` is the authoritative upstream request identity for this slice. `AEGIS-villager-production-v0.per` copies it into:

- `aegis-vp-request-id`
- `aegis-vp-authorization-id`
- `aegis-vp-authorization-generation`

The production module does not invent a downstream request ID.

## 3. Authorization boundary

Authorization is created at the consequential production boundary only after a fresh qualified civilian demand generation is admitted. Physical `up-train escrow-state c: villager` requires valid authorization and the existing engine affordability/TC predicates.

Authorization is single-use and is consumed on physical dispatch. A generation mismatch invalidates authorization and fails closed.

## 4. Pending/completion distinction

`up-pending-objects c: villager >= 1` remains **queue-admission evidence only**. It moves the lifecycle to `WAITING/PENDING`; it does not close the request and does not prove that a villager was created.

This preserves the previously established invariant that demand consumption or queue presence cannot be treated as completion.

## 5. Causal verification

The lifecycle reconciler now preserves the pre-dispatch villager baseline and observes a later census increase. The census increase is recorded as world-state evidence but is **not automatically considered causal**.

Completion requires all of:

1. positive census delta over the request baseline;
2. preserved request identity;
3. preserved authorization identity;
4. explicit causal-evidence state.

The current source contains **no proven writer for `aegis-vr-causal-evidence`**. Therefore the slice cannot falsely promote a concurrent census increase to causal completion. This is intentional fail-closed behavior and remains a qualification blocker until an engine-proven attribution mechanism exists.

## 6. What was deliberately not changed

- No XS.
- No runtime copy promoted into source.
- No claim that `can-train` means execution/completion.
- No claim that pending means spawned villager.
- No claim that census delta alone proves causality.
- No weakening of the qualification registry.
- No strategic-policy changes.

## 7. Qualification status

**NOT QUALIFIED.** The request/authorization boundary is implemented, but causal attribution and canonical reassessment remain open lifecycle requirements. This pass therefore improves contract conformance without manufacturing qualification evidence.

## 8. Template status

Villager Production now serves as the second implementation reference after Worker Economic tasking. The reusable pattern is semantic:

```text
upstream request identity
→ downstream identity propagation
→ explicit consequential authorization
→ single-use physical authorization
→ pending as intermediate evidence
→ request-bound world evidence
→ explicit causal attribution
→ no success credit without causal proof
→ reassessment
```

The remaining slices must adapt this pattern to their own physical action and evidence semantics rather than copying these symbols or code mechanically.
