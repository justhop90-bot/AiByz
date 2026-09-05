# Pass 61 — Timer & Temporal-State Provenance QC

**Date:** 2026-09-04
**Layer:** Layer 2 — research / archaeology only
**Implementation authority:** NONE
**Status:** PASS WITH EVIDENCE-BOUNDARY CORRECTIONS
**Predecessor:** Pass 56 canonical artifact; incorporates Pass 60 analysis

## Mission
Determine what timers actually represent in the historical/derived AoE2 AI scripting environment, distinguish timer state from controller state, and prevent timer/cooldown/commitment-expiration concepts from being conflated.

## Major correction
The strongest cooldown example located is in the AOE2-derived SWGB scripting reference, not the shipped AoE2 HD historical corpus. It is therefore direct engine-family evidence, not direct HD historical evidence.

Correct evidence boundary:

- Timer/cooldown mechanism exists in the AOE2-derived scripting family: DIRECT.
- Cooldown can prevent repeated controller/state writes in the documented example: DIRECT.
- Shipped historical AoE2 HD uses that exact pattern universally: NOT PROVEN.
- Byzantine historical AI uses that exact pattern: NOT PROVEN.

## Timer ontology
Public command documentation exposes `timer-triggered`, `enable-timer`, `disable-timer`, and `up-timer-status`; the latter distinguishes disabled, running, and triggered states.

Therefore:

```text
TIMER != merely a countdown
TIMER = temporal engine state
```

A timer must be modeled with provenance:

```text
INITIAL STATE
→ ENABLE / DISABLE
→ RUNNING
→ TRIGGERED
→ CONSUMER
→ RESET / DISABLE / RESTART
```

## Critical distinctions

```text
TIMER STATE != CONTROLLER STATE
TIMER EXPIRATION != COMMITMENT EXPIRATION
TIMER != AUTHORITY
NEXT PASS != TIMER INTERVAL
STATE WRITE != EXCLUSIVE OWNERSHIP
```

A cooldown exists only when timer state is combined with rule conditions that gate behavior.

## Logical-pass timing
The AOE2-derived scripting reference explicitly documents a case where an observation requires the next script pass while goals update immediately. The script deliberately inserts intermediate goal states to create an additional processing tick.

Therefore:

```text
same-rule mutation
≠
same-pass downstream evaluation
≠
next-pass observation
≠
real-time timer interval
```

These are separate temporal layers.

## Revised temporal model

```text
T0 — state mutation inside rule execution
T1 — later rule evaluation in the same processing sequence
T2 — next script pass / refreshed observations
T3 — real-time timer interval
```

Do not assume every fact observes at T0/T1. Predicate-specific semantics require evidence.

## Timer + goal controller
The documented economy example combines goal state and timer state:

```text
READY
→ action
→ COOLDOWN state
→ timer running
→ timer triggers
→ READY
```

The controller state therefore emerges from:

```text
GOAL + TIMER + RULE CONDITIONS
```

not from the timer alone.

## Timer roles
Analytical taxonomy:

1. Active-window timer — bounds a behavior's active period.
2. Cooldown timer — delays re-eligibility.
3. Watchdog timer — candidate pattern requiring further historical closure; not yet established universally.

A timer may also be used to reduce repeated state writes / computational load.

## Initialization requirement
Version documentation warns that extended goals/timers have initialization semantics that changed across engine versions and recommends explicit initialization. Archaeology must therefore trace:

```text
initializer
→ first writer
→ first consumer
→ resetter
→ re-enabler
```

An isolated timer consumer is insufficient evidence of semantic ownership.

## Resource limits
The documented engine limits include 50 timers. Timer scarcity means historical controllers may combine timers with goals, strategic numbers, flags, and rule gates rather than allocate one timer per semantic process. Timer multiplexing remains an open historical-corpus question.

## Authority correction
No single primitive establishes authority. Authority is an emergent property of eligibility, rule order, state gates, commitment state, resource effects, timer state, and control flow in a specific controller chain.

## Open questions

- Same-pass resource release → successor claim.
- Historical HD timer ownership/multiplexing.
- Explicit commitment expiration in shipped HD corpus.
- Historical priority inversion caused by temporal gating.
- Historical Byzantine timer usage.
- Watchdog/timeout semantics in HD corpus.

## Evidence hierarchy

| Finding | Grade |
|---|---|
| Timer has disabled/running/triggered states | DIRECT technical reference |
| Timer can implement cooldown | DIRECT in AOE2-derived reference |
| Cooldown can prevent reassertion | DIRECT in AOE2-derived reference |
| Goals can provide persistent state | DIRECT |
| Goal + timer can form local controller state | DIRECT / COMPOSED |
| Next-pass observation can differ from immediate goal mutation | DIRECT in derived reference; version-bound |
| Timer universally represents commitment expiration | REJECTED |
| Timer grants authority | REJECTED |
| Historical HD universal cooldown architecture | NOT PROVEN |
| Historical Byzantine timer strategy | NOT PROVEN |

## Layer boundary
No `.per` implementation, architecture implementation, deployment, or runtime modification is created by this artifact.
