# AEGIS Tactical Micro Request / Authorization Pass — 2026-09-11

**Status:** IMPLEMENTED / NOT QUALIFIED

## Architecture preserved

The Tactical Micro vertical remains distributed:

```text
World / threat observation
  -> Micro Control (intent + request identity)
  -> Micro Targeting (candidate search/filter)
  -> Micro State (local force evaluation)
  -> Micro Groups (functional role populations)
  -> Micro Geometry (target/fallback point)
  -> Micro Governor (command selection / epoch)
  -> Micro Execution Bridge (authorization)
  -> Micro Physical Adapter (physical dispatch)
  -> Micro Verification (post-dispatch evidence)
  -> Reassess
```

The implementation does **not** collapse these responsibilities into one state machine. Targeting continues to own candidate preparation; geometry continues to own point preparation; the governor continues to select the tactical command; the bridge owns execution authorization; the physical adapter owns the actual command primitive; verification owns post-dispatch evidence. Existing targeting and geometry behavior remains intact. fileciteturn155file0L2-L2 fileciteturn132file0L2-L2

## Request identity

`AEGIS-micro-control-v0.per` now owns the stable tactical request identity:

- `aegis-mc-request-id`
- `aegis-mc-request-generation`

The identity is derived from the World Model generation and remains stable through the distributed execution path.

A newer World Model generation cannot silently overwrite an active request. A new request is admitted only after the prior tactical lifecycle has been closed by verification.

## Authorization boundary

The Execution Bridge now owns the authorization record:

- request identity;
- authorization identity;
- authorization generation;
- authorization expiry;
- authorization-valid state.

The bridge accepts only the supported physical commands currently implemented by the adapter: engage, disengage, and regroup. Pursuit remains a governor-level command until a physical pursuit adapter is separately qualified.

This is intentional: a command vocabulary entry is not treated as evidence that a physical capability exists.

## Physical boundary

The Physical Adapter now requires:

1. valid tactical request;
2. authorized tactical stage;
3. matching request identity;
4. matching authorization generation;
5. prepared target/fallback geometry;
6. single unused attempt.

Authorization is consumed when the physical command is issued.

The existing physical forms are preserved, including `action-attack-move`, `action-stop`, and `action-move`. The adapter does not declare completion merely because a command primitive was emitted. fileciteturn154file0L2-L2

## Verification boundary

Verification now carries the same request identity and the bridge authorization identity.

The verifier remains deliberately conservative:

- command dispatch is not success;
- a nonempty friendly-force observation after engage is only partial/world-state evidence;
- no-target is a failure;
- no causal tactical success is invented from the command itself.

The existing verifier's unknown/partial/failed result model is preserved. fileciteturn149file0L2-L2

## Expiry and idempotency

No undocumented time clock is introduced.

Authorization expiry is generation-based. A mismatched authorization generation fails closed.

Physical idempotency remains bounded to one attempt per tactical request. This prevents repeated rule evaluation from turning one semantic request into repeated physical dispatches.

## Reassessment

After physical dispatch, the adapter moves the lifecycle to `REASSESS` rather than claiming success. Verification observes the bounded post-dispatch state and publishes partial/failed evidence where proven.

Verification closes the request by invalidating the Micro Control lifecycle after an observed result, allowing a subsequent World Model generation to establish a fresh request identity.

## Qualification status

**NOT QUALIFIED.**

This pass establishes the canonical request/authorization boundary without disturbing the distributed Tactical Micro architecture. Qualification still requires target-build runtime and engine-specific evidence demonstrating the complete physical command and world-state transition, plus stronger causal outcome evidence where applicable.

The current source already contains real physical adapter commands, but their existence is not by itself proof that the intended tactical world-state outcome occurs. fileciteturn135file0L2-L2
