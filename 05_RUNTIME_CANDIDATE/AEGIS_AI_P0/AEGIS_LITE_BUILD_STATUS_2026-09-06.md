# AEGIS-Lite Build Status — 2026-09-06

## Target

AoE2DE `101.103.48987.0`, Steam BuildID `24094652`.

## Current repository architecture

The current published candidate contains the seven-layer continuation:

```text
AEGIS-BYZ.per
  -> AegisProm\AEGIS-BYZ-Engine-Carpenter-P2
  -> AegisProm\Aegis-belief
  -> AegisProm\Aegis-situation
  -> AegisProm\Aegis-objectives
  -> AegisProm\Aegis-planning
  -> AegisProm\Aegis-decision
  -> AegisProm\Aegis-commitment
```

The entrypoint is AEGIS-owned and does not load stock Promisory modules.

## Implemented passes

### Architect / World Model — Pass 1

Owns aggregate, time-indexed world state and establishes the initial
semantic envelope `VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`.
It maintains a 15-second observation cadence and keeps strategy, production,
and direct commands outside the World Model boundary.

### Engine Carpenter — Pass 2

The current **machine-tested published artifact** is
`AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`. It contains the exact P2
continuation that was reconciled from the machine-tested package.

A separate `AegisProm/Aegis-carpenter.per` also exists in the repository but
is not part of the current entrypoint load graph. It is therefore not to be
silently treated as the canonical runtime Carpenter until reconciliation is
completed.

### Belief Model — Pass 3

Implemented as `AegisProm/Aegis-belief.per`.
It consumes World Model state and maintains bounded beliefs about enemy
presence and cavalry pressure. It does not issue commands, select producers,
reserve resources, or mutate World Model ownership.

### Situation Analysis — Pass 4

Implemented as `AegisProm/Aegis-situation.per`.
It consumes evaluated Belief state and produces bounded situational pressure
and urgency. It does not select objectives, units, buildings, resources, or
commands.

### Objectives — Pass 5

Implemented as `AegisProm/Aegis-objectives.per`.
It converts Situation state into a bounded objective such as monitor or
contain-cavalry without selecting concrete execution mechanisms.

### Planning — Pass 6

Implemented as `AegisProm/Aegis-planning.per`.
It converts the objective into an abstract plan and does not select concrete
units, buildings, resources, producers, or commands.

### Decision — Pass 7

Implemented as `AegisProm/Aegis-decision.per`.
It converts the abstract plan into bounded decision state without execution
or resource authority.

### Commitment — Pass 8

Implemented as `AegisProm/Aegis-commitment.per`.
It converts a valid Decision into explicit authorization/intent. Commitment
is not execution proof.

## Current goal-channel allocation

World Model: `300–318`  
Engine Carpenter: `319–321`  
Belief Model: `322–330`  
Situation Analysis: `331–338`  
Objectives: `339–346`  
Planning: `347–354`  
Decision: `355–362`  
Commitment: `363–370`

These remain implementation candidates, not frozen cross-system ABI.

## Qualification posture

The modules have been individually machine-tested during development, but
that does not constitute end-to-end semantic qualification of the complete
seven-layer state machine. In particular, native sensor semantics,
publication coherence, stale-generation rejection, UNKNOWN/zero/absence,
and engine-world correspondence remain qualification work.

Evidence classes remain:
`PROVEN`, `STOCK-EVIDENCED`, `DOCUMENTED`, `INFERRED`, `UNKNOWN`, `REJECTED`.

## Structural reconciliation finding — 2026-09-06

A fresh target-machine audit was run against the exact GitHub HEAD
`21fe30f8949f2b8659f61e3b47ed4042afc2f22a`.

The audit resolved **8 files**, **156 declaration rows**, **129 unique
symbols**, **356 resolved goal operands**, and **0 resolved high-goal
operands**.

It also exposed **27 duplicate declarations**. Every duplicate is one of
the World Model's 27 constants/state symbols, appearing once in the root
and once in `AEGIS-BYZ-Engine-Carpenter-P2.per`. This confirms a real package
coherence defect: the current P2 artifact contains a duplicated World Model
implementation.

The prior P2 audit artifact that reported a one-file closure is stale for the
current modular package and must not be used as the current closure authority.

## Current engineering gate

**DO NOT add native Execution adapters yet.**

First:

1. reconcile the duplicate World Model/Carpenter ownership;
2. freeze the intended eight-file load graph;
3. rerun and preserve the recursive closure audit;
4. prove generation N -> N+1 propagation and stale-state behavior;
5. separately qualify observation execution versus semantic evidence validity;
6. then advance to Execution.

## Design rule

AEGIS-Lite is an autonomous AEGIS-owned `.per` system. Stock Promisory code
is not an architectural dependency. Successful parsing or startup is not
semantic proof, and external observation remains corroboration rather than an
architectural dependency.
