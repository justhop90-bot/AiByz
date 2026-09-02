# Temporal Semantics — Deep QC Pass V2

Date: 2026-09-02
Status: strengthened calibration finding; not yet universal engine proof

## QC objective
Re-test the temporal adjudication against raw parsed calibration streams, parser implementation, and independent parser documentation.

## Finding 1 — ACTION.sequence is much stronger than a generic ordering field
The eight-game calibration corpus was re-read from the PC. All ACTION sequence streams were non-decreasing. Sequence values are not unique: multiple commands can share one sequence coordinate.

Seven of eight recordings have:
`last ACTION sequence == POSTGAME.world_time`

The eighth has:
`POSTGAME.world_time - last ACTION sequence = 3500`

The eighth terminal ACTION is a MOVE rather than RESIGN, so the recording contains a post-last-action interval before the terminal world_time.

This materially strengthens the hypothesis that ACTION.sequence is a simulation-time coordinate or command-time stamp rather than merely an ordinal event counter.

## Finding 2 — parser implementation independently constrains the interpretation
The preserved mgz-fast snapshot decodes ACTION.sequence as a little-endian unsigned 32-bit integer appended to each action record.

The parser does not generate the value. It reads the value from the replay stream and attaches it to the decoded action payload.

Therefore the temporal hypothesis is not an artifact of our JSON normalization layer.

## Finding 3 — SYNC.current_time has an explicit parser interpretation
The preserved parser source labels `current_time` as:
`duration from beginning in ms`

Rich SYNC records therefore provide an independent temporal observation with a documented parser interpretation.

The final rich SYNC precedes terminal world_time in every full calibration recording. The observed gaps are variable rather than a fixed cadence.

## Finding 4 — three temporal roles should not be collapsed
The current evidence supports three distinct temporal concepts:

1. ACTION sequence — command-associated replay-time coordinate candidate.
2. SYNC current_time — periodic synchronization observation, interpreted by parser as milliseconds from beginning.
3. POSTGAME world_time — terminal simulation-time value.

They correlate strongly but serve different observational roles.

## Finding 5 — sequence must not be renamed to milliseconds yet
The evidence is strong enough to promote temporal semantics, but not enough to prove that ACTION.sequence's unit is milliseconds.

Until native/format evidence establishes the unit, normalized schemas should retain:
`event_sequence`
`replay_time_candidate`
`temporal_confidence`

A derived field `simulation_time_ms` may be populated only when justified by an explicit calibration rule.

## Practical consequence — event simultaneity
Equal sequence values must be represented as a temporal cluster, not artificially ordered by file position. File position remains a secondary serialization coordinate.

This enables atomic decision windows such as:
`one temporal coordinate -> multiple commands -> resulting state transition`

## Practical consequence — action-to-state latency
For every command we can eventually measure:
`command_time -> first observable consequence -> stabilized consequence`

This is foundational for production latency, military response latency, building completion, economic shock recovery, and initiative-transfer analysis.

## Practical consequence — stale observation detection
A state reconstruction should maintain:
`state_value`
`observed_at`
`source_kind`
`freshness = current_event_time - observed_at`

A rich SYNC may be authoritative for its snapshot but stale for a later decision event.

## Practical consequence — decision information sets
A decision event at sequence T must only consume observations whose timestamps are <= T and whose visibility conditions permit the player to know them.

This gives the replay system an explicit anti-hindsight firewall.

## Practical consequence — temporal windows
Strategic outcomes should be evaluated using predefined windows rather than arbitrary replay excerpts:
- immediate: seconds-scale response
- tactical: capability realization / engagement window
- strategic: transition window
- long horizon: game outcome / economic conversion

Exact durations must be calibrated rather than invented.

## Practical consequence — production reconstruction
A DE_QUEUE command at T does not mean the unit exists at T. We can now distinguish:
`commanded -> admitted -> queued -> started -> completed -> available`

The same temporal machinery will expose production latency and production bottlenecks.

## Practical consequence — object lifecycle
Object disappearance at T must be adjudicated using events before/after T, object ownership, transformations, garrisoning, deletion commands, and visibility. Temporal proximity becomes evidence without becoming causality by default.

## Practical consequence — initiative transfer
If Player A acts at T and Player B responds at T+Δ, Δ becomes a measurable response-latency candidate. Repeated distributions across games can reveal which actions systematically compress the opponent's decision budget.

## Deeper extrapolation — replay as a causal measurement instrument
The replay should eventually expose not just `what happened`, but the measurable intervals between strategic stages:
`belief -> commitment -> command -> execution -> capability -> opponent response -> conversion`

Those intervals are potential empirical signatures of strategic style.

## Deeper extrapolation — Byzantine conversion tax
A Byzantine action can eventually be evaluated by the burden it imposes on the opponent across multiple clocks:
resource cost + production lock-in + travel time + response latency + transition delay + map displacement + attention/decision pressure.

This is substantially richer than counting units killed or resources spent.

## Remaining falsifiers
The temporal hypothesis must still survive:
- parser/format archaeology identifying the semantic name of sequence;
- tests across additional patches/save versions;
- wrap/reset tests;
- recordings with pauses, lag, unusual terminal behavior, and spectator conditions;
- comparison against a ground-truth engine replay timeline where available.

## QC verdict
The previous V1 finding was correct but underpowered. V2 promotes the evidence from `single-reference strong correlation` to `eight-game replicated calibration correlation + parser-source support`.

Promotion remains PROBABLE, not CONFIRMED, because the exact native meaning and unit of ACTION.sequence remain unproven.

The next pass should therefore proceed with object lifecycle reconstruction while preserving this temporal uncertainty explicitly.
