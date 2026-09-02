# Final Conversation Pass — Production Lifecycle Reconstruction

Date: 2026-09-02
Status: strong architectural baseline; empirical lineage remains unfinished.

## Direct PC evidence
The calibration corpus was successfully located on the user's Windows machine at the existing AEGIS calibration directory. Eight `.body.jsonl` streams were inspected directly rather than relying only on preserved summaries.

The eight recordings yielded DE_QUEUE counts of 221, 81, 0, 1549, 1493, 476, 723, and 448 respectively. Across the corpus, DE_QUEUE payload schema was invariant:

`amount, object_ids, player_id, sequence, unit_id`

The eight-game aggregate is 4991 DE_QUEUE actions.

## Critical parser correction
The current `.body.jsonl` streams read successfully as UTF-8 JSONL. An earlier conversation characterization treated parsed JSONL as UTF-16; that must not be generalized. Encoding is an artifact property and must be verified per file/toolchain stage.

## Production state machine
Production should be reconstructed as:

UNREQUESTED -> INTENDED -> QUEUE_COMMAND -> ADMITTED -> QUEUED -> STARTED -> COMPLETED -> OBJECT_CREATED -> CAPABILITY_AVAILABLE -> DEPLOYED -> REINFORCED

Failure branches include REJECTED, CANCELLED, INTERRUPTED, DESTROYED_BEFORE_DEPLOYMENT, PARSER_UNRESOLVED, and UNKNOWN.

## Evidence boundaries
- DE_QUEUE proves a decoded queue command.
- It does not by itself prove successful admission.
- Admission does not prove completion.
- Completion does not prove battlefield availability.
- Battlefield availability does not prove strategic usefulness.

## Commitment magnitude
`amount` permits batch commitments. Production analysis must retain amount rather than expanding it into indistinguishable unit events without lineage. A batch is a commitment to capability production and consumes resources, queue capacity, time, and optionality.

## Producer identity
`object_ids` identifies the producer objects associated with the queue command. Producer identity is therefore central to reconstructing production capacity, parallelism, queue congestion, and bottlenecks.

## Latency model
For a production item or batch:
- Tq = queue commitment
- Ta = admission candidate
- Ts = production start candidate
- Tc = completion candidate
- Tv = first usable/battlefield availability
- Td = deployment/reinforcement

Derived intervals may include queue latency, production latency, capability latency, and deployment latency. These must remain candidates until evidence establishes each transition.

## Capability ramp
A force should be represented as a capability trajectory, not a single unit count. Five queued cavalry units may produce a sequence of 1, 2, 3, 4, 5 operational units over time. Opponent pressure should be evaluated against this ramp.

## Strategic production economics
Production consumes:
- resources;
- queue time;
- production slots;
- infrastructure;
- attention/decision capacity;
- optionality;
- future reinforcement capacity.

Production capacity is therefore itself a strategic resource. A future optimizer should estimate state-dependent shadow value for resources, production slots, buildings, and time.

## Byzantine implication
A production transition should eventually be measured by the burden it imposes on the opponent: resource expenditure, production lock-in, response latency, transition delay, map displacement, and lost optionality. This is the empirical route to conversion-tax measurement.

## Required next empirical work
1. Link DE_QUEUE events to object birth candidates.
2. Establish producer/building identity continuity.
3. Detect queue cancellation/interruption signatures.
4. Estimate completion latency distributions.
5. Measure first usable capability.
6. Reconstruct parallel production and congestion.
7. Quantify replacement production after losses.
8. Cross-check production against technology/resource state.
9. Measure false lineage links and unresolved births.
10. Preserve raw evidence and confidence at every transition.

## Verdict
This pass establishes the architecture of production reconstruction and confirms that the required queue evidence is available on the PC. It does not yet establish empirical completion or object-lineage accuracy. That distinction is mandatory.