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
It owns timer cadence, World Model state, qualification, and evidence-state
transitions. Native fact acquisition is delegated to the Engine Carpenter.

### Engine Carpenter — Pass 2

The canonical loaded artifact is `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`.
It is the sole production native sensor adapter. It acquires native engine facts
and writes them into Architect-owned World Model goals. It does not define the
semantic meaning of those goals or authorize downstream behavior.

The former unloaded `AegisProm/Aegis-carpenter.per` was removed during the
2026-09-06 structural reconciliation after its SHA-256 was recorded. Git
history preserves the source for forensic recovery.

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

## Structural reconciliation — COMPLETED

The 2026-09-06 reconciliation established one authoritative owner for each
boundary and removed the duplicated World Model implementation from the
active closure.

Final target-machine audit result:

| Metric | Result |
|---|---:|
| Closure files | 8 |
| Declaration rows | 129 |
| Unique symbols | 129 |
| Resolved goal operands | 237 |
| Resolved high-goal operands | 0 |
| Duplicate declarations | 0 |

The equality of declaration rows and unique symbols is the audit indication
that the prior 27 duplicate declarations are gone from the loaded package.

The authoritative closure is documented in:

`AEGIS_LITE_STRUCTURAL_RECONCILIATION_2026-09-06.md`

Source/executable binding is documented in:

`AEGIS_LITE_RECONCILED_SOURCE_HASH_2026-09-06.md`

## Qualification posture

The modules were individually machine-tested during development, but that does
not constitute end-to-end semantic qualification of the complete seven-layer
state machine. Native sensor semantics, generation propagation, stale-generation
rejection, UNKNOWN/zero/absence, and engine-world correspondence remain open.

Evidence classes remain:
`PROVEN`, `STOCK-EVIDENCED`, `DOCUMENTED`, `INFERRED`, `UNKNOWN`, `REJECTED`.

## Current engineering gate

**DO NOT add native Execution adapters yet.**

The next work is now:

1. controlled load of the reconciled eight-file package on the target machine;
2. generation N -> N+1 propagation qualification;
3. stale-generation rejection qualification;
4. separate UNKNOWN/zero/absence experiment;
5. only then advance to the Execution skeleton.

## Machine package prepared

A disposable local package matching the reconciled eight-file closure has been
prepared at:

`C:\Users\justh\Games\Age of Empires 2 DE\76561198093432383\mods\local\AEGIS-P0-Reconciled`

The stock AI installation and mod-status state were not overwritten by this
preparation step.

## Design rule

AEGIS-Lite is an autonomous AEGIS-owned `.per` system. Stock Promisory code
is not an architectural dependency. Successful parsing or startup is not
semantic proof, and external observation remains corroboration rather than an
architectural dependency.
