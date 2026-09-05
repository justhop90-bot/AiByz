# AEGIS — Wave A Experimental Protocol

**Date:** 2026-09-05  
**Status:** ACTIVE — CONTROLLED EXPERIMENT DESIGN  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Objective

Convert the highest-risk shared semantic questions into controlled experiments that can be run against the exact target build without modifying the untouched stock baseline.

The experiments are deliberately staged. A result is useful only if the observation can distinguish competing semantic hypotheses.

## 2. Experiment families

### A — Typed ABI

**A1: Goal operation boundary**

Test representative goal IDs across:
- `set-goal`
- `goal`
- `up-modify-goal`
- `up-compare-goal`
- `up-get-focus-fact`

Questions:
- Does the operation accept the full current goal range?
- Are upper goal IDs legal in storage but illegal in specific comparison/fact contexts?
- Does an invalid target fail at parse/validation time or runtime?

**A2: Strategic-number boundary**

Test known-valid low/mid/high strategic numbers using read/write primitives and a reversible fixture. Record exact accepted range and operation-specific exceptions.

**A3: Typed identifier discrimination**

Use semantically related but distinct identifiers:
- concrete unit ID;
- unit-line ID;
- class ID;
- building ID.

Run only primitives whose documented signature distinguishes these types. The experiment must determine whether the target build enforces type distinctions at parse, validation, or runtime.

### B — State-channel safety

**B1: Writer collision fixture**

Select a candidate AEGIS channel only after comparing it against the stock collision map. Observe stock writer behavior, AEGIS writer behavior, and reader behavior separately.

**B2: Publication uniqueness**

Construct two intentionally competing writers in an isolated test fixture. The desired result is an observable failure/ambiguity rather than silent arbitration.

### C — Generation

**C1: Two-generation publication**

Publish generation N, then N+1. Consumers must be able to distinguish them deterministically.

**C2: Stale-generation rejection**

Present N to a consumer after N+1 exists. The consumer must reject or explicitly classify N as stale.

**C3: Boundary behavior**

Determine representation behavior at the chosen generation limits before assigning a permanent field.

### D — Unknown / zero / absence

**D1: Confirmed zero**

Create a state with known zero population and observe the exact fact/search output.

**D2: No-result search**

Create a state where the query has no result. Determine whether the primitive reports false, zero, empty result, or another state.

**D3: Unobserved state**

Use a deliberately unobserved target and compare the result with confirmed zero.

**D4: Pending state**

Compare pending, created, and available states separately. Historical official notes demonstrate that `up-pending-objects` and total counts have had queue-specific semantics, so this must be target-build tested rather than inferred from current documentation. citeturn0search2

## 3. Evidence discipline

Each experiment records:

`TARGET BUILD → FIXTURE → PRIMITIVE → INPUT TYPES → EXPECTED HYPOTHESES → OBSERVED RESULT → TIMING → EVIDENCE GRADE → DISPOSITION`

No experiment is allowed to rely solely on a single convenient observation when competing explanations remain viable.

## 4. Harness policy

The installed `.fts` harness artifact is known to exist, but its invocation and result semantics are still unknown. Until those semantics are qualified, controlled experiments may use a deliberately isolated AI/test fixture and externally captured logs/results rather than assuming the `.fts` harness is authoritative.

## 5. Promotion policy

A result can promote a semantic to **TARGET-BUILD QUALIFIED** only when:

1. the build identity is fixed;
2. the fixture isolates the semantic under test;
3. competing hypotheses are distinguishable;
4. the observed result is reproducible;
5. the result does not depend on an unqualified semantic;
6. the result is recorded in the shared qualification register or a linked evidence artifact.

## 6. First execution order

`A1 → A2 → A3 → D1 → D2 → D3 → D4 → C1 → C2 → C3 → B1 → B2`

This ordering minimizes the risk of building higher-level state machinery on unqualified primitive semantics.

## 7. Stop conditions

Stop and classify UNKNOWN when:

- the test cannot distinguish competing hypotheses;
- the harness semantics are not understood;
- another unqualified primitive dominates the result;
- build identity cannot be proven;
- the result depends on modified stock files without a separate modified-build label.

An UNKNOWN result is an engineering result. It is not a failure of the test.
