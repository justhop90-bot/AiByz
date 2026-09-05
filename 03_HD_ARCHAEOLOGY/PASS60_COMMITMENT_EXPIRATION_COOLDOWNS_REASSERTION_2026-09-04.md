# Pass 60 — Commitment Expiration, Cooldowns & Reassertion Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Status:** PASS WITH EVIDENCE-BOUNDARY CORRECTIONS

## Mission
Determine whether historical commitments have explicit expiration, cooldown, or reassertion behavior, and clarify what timers can and cannot prove.

## Core temporal model

```text
T0 = same-rule state mutation
T1 = same-pass rule ordering
T2 = next-pass observation
T3 = real-time timer interval
```

This separates controller-state time from world-observation time.

## Major conclusions

### 1. Timer ≠ commitment expiration
A timer only becomes a commitment timeout when surrounding rules explicitly connect timer state to commitment release/reassertion.

### 2. Timer ≠ authority
A running timer does not own a controller or resource channel.

### 3. `disable-self` ≠ cooldown
`disable-self` is rule-lifecycle suppression. It should not be treated as a timer-based temporal gate.

### 4. Timer + rule condition = temporal gating

```text
TIMER STATE
+
RULE CONDITION
=
TEMPORAL GATE
```

## Evidence hierarchy correction

Some useful cooldown and timer patterns were recovered from an AOE2-derived scripting-family reference rather than directly from the shipped HD historical corpus. They are strong engine-family evidence but must not be mislabeled as direct HD historical behavior.

Historical HD claims require historical-corpus evidence or local runtime corroboration.

## Initialization

Timers and extended goals require explicit initialization discipline. Defaults varied by engine/version and should not be assumed.

## Timer-state semantics

Public technical documentation exposes timer state through mechanisms including:

- `timer-triggered`
- `enable-timer`
- `disable-timer`
- `up-timer-status`

`up-timer-status` is particularly valuable because it distinguishes disabled/running/triggered states.

## Temporal sampling

AEGIS introduces **temporal sampling rate** as an analytical concept:

> how frequently a controller is allowed to reconsider a condition.

Also:

```text
OBSERVATION LATENCY
= delay before a world-derived fact reflects a transition
```

Controlled latency can be deliberate stabilization; uncontrolled latency is engine/update limitation.

## Reassertion model

A controller may repeatedly attempt to establish a commitment when a gate reopens:

```text
OPEN
↓
CLAIM
↓
BLOCKED / WAITING
↓
REASSESS
↓
REASSERT
```

This does not prove oscillation in every historical HD controller.

## Timer limit

The scripting environment exposes a finite timer budget (50 timers in the documented AoE2 context). This creates potential timer-multiplexing pressure, but timer multiplexing has not been established as a historical HD design pattern.

## Byzantine implication

Byzantine reaction quality requires balancing:

```text
RESPONSIVENESS
↕
STABILITY
↕
COMPUTATIONAL COST
```

The civilization's broad counter space increases the importance of temporal arbitration, but no Byzantine-specific historical timer controller has been proven from this pass.

## Evidence ledger

| Finding | Grade |
|---|---|
| Timers have disabled/running/triggered states | DIRECT technical evidence |
| `up-timer-status` inspects timer state | DIRECT technical evidence |
| Timer/goal state can be composed | DIRECT / COMPOSED |
| Timers can implement cooldown windows | DIRECT scripting-family evidence |
| Timers can implement active windows | DIRECT scripting-family evidence |
| Timers can be cancelled/restarted | DIRECT scripting-family evidence |
| `disable-self` is local rule suppression | DIRECT |
| Timer automatically expires commitments | FALSE / REJECTED |
| Timer automatically grants authority | FALSE / REJECTED |
| Every historical HD controller uses timer cooldowns | NOT PROVEN |
| Byzantine-specific historical timer controller | NOT PROVEN |
| Timer multiplexing in historical HD | OPEN |
| Same-pass release → successor claim | OPEN |
| Historical temporal priority inversion | OPEN |

## QC corrections carried forward

Do not describe all cooldown evidence as direct HD evidence. Do not claim timers synchronize controller and world clocks by themselves. Do not equate timers with commitment expiration or authority. Preserve engine-version boundaries.

## Layer boundary

No `.per` implementation or architecture implementation. Research only.
