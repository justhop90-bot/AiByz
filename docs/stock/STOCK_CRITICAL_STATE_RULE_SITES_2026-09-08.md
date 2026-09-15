# Critical Stock State Rule-Site Ledger — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Purpose:** static extraction of high-coupling stock state mutation sites. Runtime semantics remain separately qualified.

## Scope

This pass concentrates on state that can alter downstream operating policy: strategic goals, strategic numbers, timers, pending/object state, escrow and production/construction decisions.

The ledger intentionally distinguishes **source-level mutation** from **semantic ownership**. A stock module writing a channel does not automatically make it the architectural owner in AEGIS.

## Critical mutation families

| Family | Primary stock producers | Primary consumers | Architectural interpretation |
|---|---|---|---|
| Strategy goals | `init.per`, `general.per`, strategy/civ-policy regions | economy, units, buildings, research, military | Strategic intent/state; must be centralized or mediated in AEGIS. |
| Economic allocation goals/SNs | `gatherers.per`, `dawn.per`, `init.per` | gatherer tasking, dropsite logic, production | Economic demand/allocation state. |
| Construction goals | `buildings.per`, `init.per`, threat-related rules | construction placement/builders | Construction demand plus physical execution state. |
| Unit production goals | `units.per`, `init.per`, strategy rules | production/train actions | Capability demand/composition state. |
| Military goals | `tsa.per`, attack/retreat regions, `threats.per` | production, targeting, movement, retreat | Military posture and tactical state. |
| Research goals | `researches.per`, strategy regions | research actions, economy | Technology demand and age-transition state. |
| Town-size state | `buildings.per`, late-game/increase-TS regions | housing/construction/production | Infrastructure capacity state. |
| Escrow state | `escrow.per` | build/train/research authorization | Reservation/liquidity mechanism. |
| Pending-object state | `buildings.per`, `orb.per`, `general.per`, production rules | confirmation/recovery | Engine-facing observation state; not strategic intent. |
| Scout/threat state | `scoutcontrol.per`, `threats.per`, `tsa.per` | strategy, military, construction, economy | Information and threat signals. |

## Static rule-site contract

For each critical mutation, the final forensic dataset must preserve:

```text
source file + exact line
activation predicates
read state
mutation
subsequent command/action
reset/supersession path
cross-module consumer
```

This prevents a common reconstruction error: finding the writer while missing the condition that makes the writer active or the later rule that invalidates the state.

## High-value state lifecycles

### Worker allocation

```text
policy target
  → desired allocation
  → deficit
  → candidate search
  → target selection
  → task assignment
  → productive observation
  → interruption/failure
  → reselection/reallocation
```

### Construction

```text
strategic demand
  → build authorization
  → placement search
  → pending placement/object
  → builder assignment
  → foundation
  → completed structure
  → reconciliation
```

### Production

```text
strategic demand
  → production authorization
  → resource reservation
  → train/build command
  → pending object
  → completed unit
  → role/formation assignment
```

### Research

```text
strategic priority
  → affordability/prerequisite test
  → reservation/escrow
  → research authorization
  → pending research
  → completed technology
  → strategic-state reconciliation
```

### Threat

```text
sensor evidence
  → threat signal
  → policy mutation
  → defensive demand
  → execution
  → threat decay/clear
  → state reconciliation
```

## Reconstruction rule

A future AEGIS subsystem may use a stock mechanic only after its lifecycle, state dependencies, and failure/reset paths are understood. Copying a rule without its surrounding lifecycle is not an acceptable reconstruction method.

## Evidence status

This ledger is **STATIC-QUALIFIED** for source topology. It is **not RUNTIME-QUALIFIED** for interpreter timing, same-pass visibility, mutation ordering, or command side effects.

## Next extraction

The next dataset should enumerate exact rule-site tuples for the highest-risk shared channels, beginning with:

1. `control-goal`
2. `strategy-goal`
3. `unit-goal`
4. `position-goal`
5. `attack-goal`
6. `housing-goal`
7. `increase-town-size-goal`
8. economic allocation SNs
9. military posture SNs
10. escrow controls

The objective is a machine-readable dependency graph, not another prose inventory.
