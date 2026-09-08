# AEGIS / ByzBot — Final Vertical-Slice Gap Analysis

**Date:** 2026-09-08
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652
**Scope:** static implementation audit; no runtime performed

## Executive finding

The prototype has a real end-to-end control skeleton, but it is **not yet the final Cavalry Threat Containment vertical slice**. The missing piece is not another architecture layer; it is the concrete capability-demand and production-control plane between tactical intent and engine execution.

Stock remains reference evidence only. AEGIS is an independent runtime and must not load stock AI as an intelligence parent or state authority.

## Current chain actually present

```text
World Model
  -> Belief
  -> Situation
  -> Objective
  -> Planning
  -> Decision
  -> Commitment
  -> Execution
  -> Verification
  -> Recovery
```

This is a useful control skeleton, but Planning currently selects a unit branch directly from situation/world-state conditions. That is not yet the required:

```text
Threat -> Objective -> Capability Demand -> Deficit -> Production Load
       -> Arbitration -> Execution -> Evidence -> Reassessment
```

## Blocking gaps for the first real vertical slice

### 1. Threat observation contract

The prototype assumes `aegis-wm-cavalry`, `aegis-wm-archers`, and related world-model fields already exist. Foundation currently publishes them from sensor slots, but the complete target-build acquisition implementation and typed fact surface must be supplied by the final independent observation service.

### 2. Capability demand

There is no authoritative force-demand object between Objective and Planning/Production. A Contain objective must produce a typed requirement such as required camel capability, target quantity, urgency, generation, and validity. This is demand, not a command.

### 3. Deficit computation

The prototype lacks the final `required - current - effective-pending` calculation. The deficit must distinguish existing capability from pending/queued capability and avoid double-counting transactions.

### 4. Production Director

The final architecture requires an explicit Production Director. It consumes capability deficits, converts them into economic/resource loads, arbitrates against civilian and other military demand, and publishes an execution-eligible production request. Current `Aegis-execution-final.per` reaches directly into economic state and `can-train`; that is too early in the pipeline for the final architecture.

### 5. Producer selection

Camel production requires a concrete producer-selection/serviceability contract. The current Camel execution rule only checks `can-train camel-line`; it does not establish producer identity, queue ownership, reservation, or pending transaction identity.

### 6. Execution evidence

The execution module records `ISSUED` immediately after `train`. That is useful as an intention/issuance boundary but does not establish `ACCEPTED/QUEUED`, `PENDING`, `CREATED`, `AVAILABLE`, or `DEPLOYED`. Verification currently uses aggregate unit-count growth as a proxy. The final slice must preserve the full evidence ladder and explicitly mark unsupported transitions as unknown.

### 7. Recovery transaction identity

Recovery is architecturally promising, but resetting execution generation to `-1` and relying on later recapture is a prototype mechanism. Final retry identity must be tied to a defined transaction/generation protocol rather than sentinel values whose semantics have not been qualified.

### 8. Numeric ABI

`AEGIS-foundation.per` values in the 300–400 range remain prototype allocations. They must not be promoted. Final numeric assignment must be regenerated from the complete typed inventory and collision audit.

## Important prototype defects not to carry forward

- Planning is policy-coupled to current World Model fields instead of consuming a capability-demand contract.
- Camel/Skirmisher/Spearman branches are chosen before a production deficit is computed.
- Execution has direct `can-train`/`train` paths for multiple unit types.
- Verification treats aggregate unit-count increase as sufficient confirmation; this is only a provisional vertical-slice proxy.
- Foundation uses provisional numeric storage and a provisional timer.
- Construction timing remains behind the explicit adapter boundary already established by the readiness gate.

## Correct implementation order from here

1. Freeze the symbolic contracts; do not freeze prototype numbers.
2. Build the independent World Observation service and publish one coherent generation.
3. Build Cavalry Threat Belief/Situation using only that published frame.
4. Build Containment Objective.
5. Add **Cavalry Capability Demand**: desired capability, required count, current count, effective pending count, deficit, urgency, provenance.
6. Add **Production Director**: deficit -> producer candidates -> resource load -> arbitration -> authorized production request.
7. Add **Execution Bridge** as the only native production authority.
8. Add observation-backed evidence transitions and conservative verification.
9. Add bounded recovery with explicit transaction identity.
10. Assemble the minimal independent `.ai` root and mechanically verify reachable closure.

## Verdict

The project is **implementation-ready, but the existing final-named modules are not themselves the final implementation**. The first production code should be a new independent vertical slice assembled from the frozen contracts, with the prototype modules mined for algorithms and state semantics rather than copied wholesale.

No runtime certification is claimed by this document.
