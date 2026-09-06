# AEGIS-Lite Build Status — 2026-09-06

## Target

AoE2DE `101.103.48987.0`, Steam BuildID `24094652`.

## Current architecture

```text
AEGIS-BYZ.per
  -> Aegis-carpenter
  -> Aegis-belief
```

The entrypoint is AEGIS-owned and does not load stock Promisory modules.

## Implemented passes

### Architect / World Model — Pass 1

Owns qualified, aggregate, time-indexed world state. It establishes the
semantic envelope `VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`,
maintains a 15-second observation cadence, and keeps strategy/commands outside
the World Model boundary.

### Engine Carpenter — Pass 2

Separated into `AegisProm/Aegis-carpenter.per`.
It maps the World Model to native AoE2DE primitives observed in the target
retail package and provides bounded runtime diagnostics.

The user independently tested the external `load` path and reported that the
Architect entrypoint started normally with the Carpenter module loaded.
This establishes startup/load compatibility for that experiment; it does not
by itself qualify every Carpenter sensor semantic.

### Belief Model — Pass 3

Implemented as `AegisProm/Aegis-belief.per`.
It consumes qualified World Model state and maintains bounded beliefs about
enemy presence and cavalry pressure. It does not issue commands, select
producers, reserve resources, or mutate World Model ownership.

Cavalry interpretation currently uses deterministic thresholds:
`0 = NONE`, `1–3 = LIGHT`, `4+ = HEAVY`.
Confidence is represented separately from the belief level.

## Current goal-channel allocation

World Model: `300–318`
Engine Carpenter: `319–321`
Belief Model: `322–330`

These remain implementation candidates, not frozen cross-system ABI.

## Qualification posture

The AEGIS-Lite build is intentionally progressing before exhaustive ABI
qualification. Runtime semantic questions remain tracked as UNKNOWN rather
than silently promoted by successful startup.

Evidence classes remain:
`PROVEN`, `STOCK-EVIDENCED`, `DOCUMENTED`, `INFERRED`, `UNKNOWN`, `REJECTED`.

## Next architectural pass

Situation Analysis: consume World Model + Belief state and produce bounded
situational assessments without yet selecting objectives or issuing commands.

## Design rule

AEGIS-Lite is being built as an autonomous AEGIS-owned `.per` system. Stock
Promisory code is not an architectural dependency.
