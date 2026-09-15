# AEGIS-Lite Generation Propagation Experiment — 2026-09-06

**Status:** TEST PROTOCOL — probe prepared, runtime execution pending  
**Purpose:** prove or falsify end-to-end generation propagation through the current seven-layer AEGIS-Lite chain.

## Hypothesis

For a valid World Model publication at generation `N`, every downstream layer should consume and publish the same generation before Commitment authorization. A later World Model publication at `N+1` must supersede the prior context without allowing stale `N` authority to masquerade as current.

## Instrumentation

`AegisProm/Aegis-generation-probe.per` is a non-mutating diagnostic module. It is **not loaded by the current production candidate**. It records the seven generation values and validity values when a new authorized Commitment generation is observed.

## Phase A — propagation

1. Start the exact candidate package on the target build.
2. Add only the generation probe to a disposable test package; do not modify the source candidate in place.
3. Capture the first authorized Commitment generation.
4. Record the probe line:

```text
WM=N Belief=N Situation=N Objective=N Planning=N Decision=N Commitment=N
```

5. Confirm the corresponding validity values.
6. Allow the World Model timer to produce another observation.
7. Capture the next probe event and require:

```text
WM=N+1 Belief=N+1 Situation=N+1 Objective=N+1 Planning=N+1 Decision=N+1 Commitment=N+1
```

## Phase B — stale authority

The propagation probe alone does not prove stale rejection. A separate experiment must retain a valid `N` context, publish `N+1`, then attempt to reuse `N` and observe whether the current chain rejects it.

Required verdicts:

- `PASS`: stale `N` cannot become current after `N+1` is authoritative.
- `FAIL`: stale `N` remains executable/authoritative.
- `UNKNOWN`: the engine does not expose enough evidence to distinguish the cases.

## Phase C — invalid observation isolation

Do not combine UNKNOWN/zero/absence testing with the generation experiment. A failed sensor result must not be interpreted as a generation failure.

Required cases remain:

- confirmed zero;
- search no-result;
- unsupported query;
- unobserved state.

## Evidence binding

Every runtime result must record:

- exact source/package hash;
- exact executable SHA-256;
- target build/version;
- disposable package location;
- probe source hash;
- observed generation sequence;
- raw diagnostic output;
- verdict and evidence class.

## Current disposition

**Probe source:** statically audited and accepted as experimental instrumentation.  
**Runtime propagation:** UNKNOWN until executed.  
**Stale-generation rejection:** UNKNOWN.  
**Execution:** intentionally out of scope.
