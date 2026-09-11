# AEGIS Production Reservation Authority v0.1 — Implementation Record

Date: 2026-09-11
Status: IMPLEMENTED IN `AegisProm`; NOT PROMOTED TO `runtime/`

## Purpose

Production Reservation Authority v0.1 closes the cross-producer ownership gap identified between Military Production and Cavalry Response. Both producers can target `spearman-line`; producer-local authorization alone does not establish exclusive ownership of that conflicting production opportunity.

The reservation authority therefore owns only the exclusive right to claim the conflict resource. It does not own strategy, producer lifecycle, physical production, world-state verification, causal confirmation, or strategic success.

## Certified namespace

The implementation uses the certified contiguous block 806–817:

| Goal | Symbol |
|---:|---|
| 806 | `aegis-pr-generation` |
| 807 | `aegis-pr-state` |
| 808 | `aegis-pr-reservation-id` |
| 809 | `aegis-pr-owner` |
| 810 | `aegis-pr-request-id` |
| 811 | `aegis-pr-authorization-id` |
| 812 | `aegis-pr-authorization-generation` |
| 813 | `aegis-pr-valid` |
| 814 | `aegis-pr-expiry` |
| 815 | `aegis-pr-resource-key` |
| 816 | `aegis-pr-unit-line` |
| 817 | `aegis-pr-release-reason` |

No slots above 817 were allocated.

## Implemented state machine

`FREE → RESERVED → IN_FLIGHT → RELEASE_PENDING → RELEASED`

Conflicts are denied/deferred by leaving the existing reservation untouched; there is no persistent DENIED ownership state.

## Implemented boundaries

- Reservation grant requires a current producer authorization.
- Only one active reservation may exist for the resource domain.
- Reservation identity is request-bound.
- Physical dispatch remains producer-owned.
- Producer dispatch now requires matching reservation owner, request, authorization, generation, resource key, and unit-line.
- Stale generation moves an active reservation to `RELEASE_PENDING` with `STALE_GENERATION`.
- Zero expiry is fail-closed.
- Terminal producer outcomes request explicit release.
- Release requires identity agreement and is idempotent.
- Reservation authority never executes `up-train`.
- Reservation authority never writes causal evidence.
- Reservation authority never declares strategic success.

## Producer integration

`AEGIS-military-production-v0.per` and `AEGIS-cavalry-response-v0.per` now require the reservation boundary before executing `up-train escrow-state c: spearman-line`.

This preserves the separation:

`AUTHORIZATION → RESERVATION → PHYSICAL DISPATCH → WORLD OBSERVATION → CAUSAL ATTRIBUTION`

Reservation ownership is an attribution input, not causal proof.

## Military Production qualification remains blocked

The reservation authority does not resolve the independent Military Production selector blocker. `aegis-mp-unit` initialization remains a separate qualification issue in the source implementation. The reservation authority must not be used to hide or conflate that blocker.

## Runtime promotion boundary

The repository's `runtime/` tree remains unchanged by this implementation. Its current production-root copies are a separate, older runtime snapshot and do not implement the current ACAP authorization contract. Promoting the reservation authority into that tree without synchronizing the complete producer ABI would create a mixed-generation runtime.

Promotion therefore remains a separate gate requiring:

1. complete runtime/source ABI synchronization;
2. selector initialization resolution;
3. static validator success;
4. runtime lifecycle evidence; and
5. causal attribution evidence.

## Tests added

`tests/vertical_slices/test_production_reservation_authority_v01.py` statically checks the certified namespace, state machine, exclusive ownership, authorization binding, stale/expiry fencing, producer dispatch gates, and idempotent release boundary.

## Qualification status

**Implementation:** COMPLETE for the bounded `AegisProm` source slice.

**Qualification:** NOT YET QUALIFIED.

**Promotion:** BLOCKED pending runtime synchronization and evidence gates.
