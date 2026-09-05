# AEGIS — Layer 3B Phase Exit Criteria

**Date:** 2026-09-05  
**Status:** ACTIVE

Layer 3B exits only when the project can truthfully claim that the machine semantics required for the first vertical slice are known well enough to implement without semantic guessing.

## Mandatory exits

### Build
- target executable fingerprint recorded;
- stock AI baseline frozen;
- regression trigger defined.

### ABI
- required goal/SN/fact signatures qualified;
- semantic parameter types qualified;
- reserved channels cleared by collision audit;
- no numeric-only allocation accepted.

### State
- identity and generation behavior qualified;
- scope propagation qualified;
- current vs last-known semantics qualified;
- UNKNOWN/zero/absence semantics qualified;
- publication coherence qualified.

### Lifecycle
- command vs acceptance distinguished;
- pending vs created distinguished;
- created vs available distinguished where relevant;
- cancellation/supersession qualified;
- stale authority cannot resurrect obsolete work.

### Runtime
- expensive evidence operations measured;
- bounded search/candidate work established;
- controller/world latency measured;
- no P1 test relies on an unbounded rule/search loop.

### Vertical slice
- Cavalry Threat Containment passes controlled success;
- controlled failure/deviation does not produce false success;
- verification can distinguish operational result from strategic success;
- recovery does not silently invent a new objective/decision.

## Hard stop

If any load-bearing result is UNKNOWN, Layer 3B does not silently promote the uncertainty into implementation. It remains a named qualification gap with an owner and next experiment.

## Architecture reopening rule

Architecture reopens only if target-build evidence falsifies a load-bearing architectural invariant and no implementation/ABI correction can preserve the invariant without changing subsystem authority or boundary.
