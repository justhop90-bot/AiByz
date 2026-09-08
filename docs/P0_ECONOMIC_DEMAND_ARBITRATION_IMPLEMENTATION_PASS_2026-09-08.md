# P0 Economic Demand and Arbitration — Implementation Pass

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652

**Status:** STATIC CANDIDATES — NOT RUNTIME QUALIFIED

## Scope

This pass establishes the boundary between worker-role reconciliation and physical worker tasking. Economic demand describes unmet civilian role requirements. Arbitration selects one actionable resource demand from competing demands. Neither module issues worker commands or selects resource sources.

## Implemented artifacts

- `implementation/AEGIS-economic-demand-v0.per`
- `implementation/AEGIS-economic-demand-arbitration-v0.per`

Economic demand goals: 479–489.
Arbitration goals: 490–497.

## Architecture

```text
WORKER ROLE CENSUS
        ↓
WORKER ROLE VECTOR
        ↓
ECONOMIC DEMAND
        ↓
DEMAND ARBITRATION
        ↓
WORKER TARGET SELECTION
        ↓
SOURCE / DROPSITE QUALIFICATION
        ↓
TASK COMMAND
        ↓
ENGINE OBSERVATION
        ↓
VERIFICATION / RECOVERY
```

## Economic demand contract

V0 copies positive worker-role deficits for food, wood, gold, and stone into a typed demand frame. Demand carries generation, priority, urgency, and observation time. The module deliberately does not translate worker count into resource-per-minute forecasts; that requires later economic measurement and Byzantine policy.

## Arbitration contract

V0 selects one resource demand. High urgency is considered before ordinary deficit magnitude. Otherwise the largest positive deficit wins. Equal deficits use a deterministic food → wood → gold → stone tie order. This is an implementation convenience for deterministic V0 behavior, not a claim that final Byzantine economic doctrine should use this fixed ordering.

## Important correction to earlier framing

The previous economic-demand implementation was initially created locally but was not found in the repository during verification. It has now been explicitly archived. GitHub commits for the two implementation artifacts are recorded separately below.

- Economic demand commit: `26751ce207c1a3993abe5514f510a5068598ef06`
- Arbitration commit: `f8b2c289d683ea7f13b903ab700ddd4d49f0ab2b`

## Evidence classification

### OBSERVED

Stock AEGIS/Promisory forensics establish engine-visible worker role classifications and stock use of goal mutation/comparison idioms.

### CORRELATED

Worker-role deficits are a reasonable intermediate representation between observed worker state and economic tasking, consistent with the stock gatherer architecture.

### INFERRED

The V0 arbitration policy—urgency first, then largest deficit, then deterministic tie-break—is an engineering policy, not a recovered stock engine rule and not runtime-proven Byzantine doctrine.

### IMPLEMENTED

The demand and arbitration state machines exist as isolated candidates and are not loaded by the production root.

### STATIC-QUALIFIED

Both candidates have balanced parentheses and isolated goal allocations. No production-root load change was made.

### NOT RUNTIME QUALIFIED

No claim is made that the target interpreter exposes all goal mutations in the same evaluation pass. No claim is made about exact scheduler timing, re-entry, or command-side effects.

## Architectural boundary

Economic demand is not resource reservation. Arbitration is not authorization. A selected gold deficit does not authorize a miner to move, does not reserve gold, does not prove a mining camp exists, and does not prove a source is serviceable.

The required downstream chain remains:

`DEMAND → ARBITRATION → RESERVATION → WORKER ELIGIBILITY → SOURCE/DROPSITE QUALIFICATION → COMMAND → OBSERVE → VERIFY → RECOVER`.

## Risks

1. V0 consumes aggregate role deficits and therefore does not yet account for protected workers or workers already committed to construction/military-support tasks.
2. V0 does not yet model source availability, dropsite service distance, task load, threat, or infrastructure state.
3. A single selected resource intentionally leaves competing demands pending; starvation prevention and bounded fairness belong to the next arbitration revision.
4. The fixed tie order is not final doctrine.
5. Goal visibility across interpreter passes remains an ABI qualification item.

## Promotion decision

**Do not load into production.** The next implementation target is worker-target selection: exclude protected/invalid workers, identify eligible candidates, and connect the selected economic demand to a physical worker without assuming that command issuance equals productivity.
