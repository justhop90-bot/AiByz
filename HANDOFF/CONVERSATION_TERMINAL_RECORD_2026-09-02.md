# Terminal Conversation Record — 2026-09-02

This document records the last substantive research state before the conversational context limit.

## Immediate request
The next phase is information, resource, and corpus preservation. The objective is a professional engineering handoff so that six months later a successor AI can recover the project's knowledge, evidence, reasoning, and direction.

## Last accepted pass
The user approved the Production Lifecycle Reconstruction pass as materially better and a strong baseline/architecture.

## Direct PC retrieval
The calibration corpus was retrieved from the Windows machine rather than relying only on preserved artifacts. Eight `.body.jsonl` streams were present and readable.

DE_QUEUE counts by recording:
- 2026-08-07: 221
- 2026-08-19: 81
- 2026-08-20: 0
- 2026-08-23: 1549
- 2026-08-29 11:10: 1493
- 2026-08-29 17:38: 476
- 2026-08-31 09:46: 723
- 2026-08-31 16:43: 448

Aggregate: 4991.

All observed DE_QUEUE payloads used:
`amount, object_ids, player_id, sequence, unit_id`.

## Terminal empirical observation
A direct inspection of a raw parsed stream showed a rich SYNC payload of the form:
`[25, 515842, {current_time: 16170, player state...}]`

This is important because it demonstrates that rich SYNC state is structurally available in the actual parsed streams, even though it is sparse. It must be mined rather than dismissed.

## Important correction
Current parsed `.body.jsonl` files are UTF-8 JSONL. An earlier encoding characterization was overgeneralized and should be corrected in future documentation.

## Production architecture accepted
Production lifecycle:
`intent -> queue command -> admission -> queued -> started -> completed -> object birth -> capability availability -> deployment -> reinforcement`

The research must preserve uncertainty at every transition.

## Why this matters
Production is a capability pipeline. `amount` measures commitment magnitude. `object_ids` identifies producers. Queue occupancy, production capacity, latency, congestion, and capability ramps can therefore become strategic state.

## Research direction after handoff
Preserve first. Then resume with:
1. Production-to-object lineage reconstruction.
2. Capability ramp reconstruction.
3. Resource-flow/production coupling.
4. Opponent response latency.
5. Decision-event reconstruction with anti-hindsight.
6. Conversion-tax measurement.
7. Byzantine strategic controller.
8. Runtime compilation into the verified AoE2DE machine contract.

## Final principle
The project must preserve the designer's thinking, not merely the implementation. Every future conclusion should remain returnable, falsifiable, and traceable to evidence.