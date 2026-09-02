# Production-to-Object Lineage — QC Pass 1

Date: 2026-09-02
Status: EMPIRICALLY CALIBRATED / LINEAGE PARTIALLY IDENTIFIABLE

## Objective

Reconstruct the lifecycle from a production command to an actual world object and then to an operational capability, without treating command issuance as proof of completion.

Target chain:

`intent -> queue command -> queue admission -> production -> object birth -> usable capability -> deployment -> reinforcement`

## Corpus

Eight local calibration recordings were re-read directly from the user's Windows machine under `AEGIS_CALIBRATION_DATA`. The parsed JSONL streams are present and readable; this pass therefore does not depend solely on expired conversation attachments or derived GitHub artifacts.

All eight streams contain ACTION records and reach POSTGAME. DE_QUEUE is present in seven games; the 2026-08-20 negative control contains no production commands.

Observed DE_QUEUE counts by game: 221, 81, 0, 1549, 1493, 476, 723, 448 commands.

Observed requested unit amounts by game: 221, 81, 0, 1695, 2803, 617, 1216, 448 units.

## Stable command schema

Every observed DE_QUEUE event in all eight calibration streams used the same payload schema:

- player_id
- object_ids
- amount
- unit_id
- sequence

This is strong evidence for a stable parsed production-command primitive in the calibrated replay/version cohort.

## What DE_QUEUE proves

A DE_QUEUE event proves that the replay contains a production-queue command with a player, producer object set, requested unit identifier, requested amount, and event sequence.

It does NOT independently prove:

- successful queue admission;
- resource payment;
- uninterrupted production;
- completion;
- object creation;
- first battlefield availability;
- deployment;
- sustained military capability.

These must remain separate reconstruction states.

## Producer-capacity evidence

`object_ids` gives the producer object set attached to the queue command. This permits reconstruction of intended production allocation and, subject to object identity validation, producer-level capacity usage.

Therefore production demand should not be modeled solely as `unit_id x amount`. The producer dimension is essential.

## Batch commitment

`amount` is not uniformly one. The corpus contains multi-unit queue events, including a reference event with amount=4. Therefore the atomic strategic production event can represent a batch commitment rather than a single-unit decision.

This introduces a measurable commitment-magnitude variable.

## Temporal evidence

The sequence field is available directly on DE_QUEUE and is the appropriate temporal join key for the current parsed event layer. It must not yet be silently equated with milliseconds. Prior temporal QC established that sequence is non-decreasing and strongly related to terminal world time, with a documented 7/8 exact terminal match and one counterexample.

Temporal proximity may establish a candidate causal window; it does not establish causality by itself.

## Object-lineage discovery

The current parsed SYNC representation does not expose individual object identities. Rich SYNC records observed in the calibration corpus contain fields including `current_time` and per-player resource/object-count summaries, but not a per-object birth ledger.

Other ACTION commands, including MOVE, expose object_ids, demonstrating that object identifiers exist in the parsed command stream. However, an object's first appearance in an ACTION stream is not sufficient proof that the object was newly produced: existing objects can receive their first recorded command long after creation, and invisible/uncommanded objects may have no immediate action.

Consequently, naïve `first_seen_object_id -> queue` matching is rejected.

## Current identifiability boundary

The calibrated parsed JSONL supports strong reconstruction of:

1. production intent/command;
2. producer allocation;
3. requested amount;
4. temporal production commitment;
5. aggregate object-count changes when rich SYNC observations are available.

It does not yet support, with sufficient confidence, universal direct linkage:

`DE_QUEUE(unit X, producer Y) -> object ID Z was born from this queue event`.

That missing link is now an explicit research boundary rather than an implicit assumption.

## Required next instrumentation

To cross the boundary, investigate the raw body binary and parser implementation for omitted operation families or hidden object-state records; compare parser output with a second independent parser/simulation representation; and construct controlled replay fixtures where a unique production event can be associated with a uniquely identifiable subsequent object action.

Controlled experiments should target:

- one producer, one unique unit;
- multiple parallel producers, same unit;
- queued batches;
- queue interruption/cancellation;
- producer destruction before completion;
- production immediately followed by MOVE/ORDER;
- transformation-producing actions;
- garrison/deployment cases;
- visibility-limited cases.

## Production capability model

The correct Layer-2 abstraction is now:

`production demand -> producer capacity -> queue commitment -> realization -> object lineage -> capability ramp`.

A unit count is only one projection of this state.

## Byzantine relevance

For the Byzantine conversion-tax doctrine, the meaningful strategic measurement is not simply "enemy produced cavalry." The system should eventually quantify:

`commitment magnitude + production capacity consumed + capability latency + transition cost + opponent response + opportunity cost`.

This permits measurement of whether a commitment forced the opponent to spend resources, production slots, timing, map control, or optionality merely to remain viable.

## Confidence ledger

CONFIRMED: DE_QUEUE schema is invariant across eight calibrated streams.

CONFIRMED: producer object_ids are present in DE_QUEUE.

CONFIRMED: amount represents non-unitary batch requests in at least one calibrated game.

CONFIRMED: sequence is present on production commands.

CONFIRMED: rich SYNC aggregate state does not provide a universal per-object identity ledger in the current parsed representation.

PROBABLE: producer allocation can support capacity reconstruction once producer lifecycle is independently established.

UNRESOLVED: queue admission versus rejected command.

UNRESOLVED: exact resource-payment event linkage.

UNRESOLVED: completion event linkage.

UNRESOLVED: object birth linkage.

UNRESOLVED: exact production-to-capability latency.

REJECTED: treating DE_QUEUE as proof of completed production.

REJECTED: treating first ACTION appearance of an object_id as proof of object birth.

## QC judgment

This pass materially improves the production model because it identifies the exact empirical boundary between what the replay parser exposes and what the strategic reconstruction wants to know. The correct response is additional instrumentation, not invented certainty.
