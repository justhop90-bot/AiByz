# AEGIS — Goal Namespace Operation Qualification Specification

**Date:** 2026-09-05  
**Status:** QUALIFICATION SPECIFICATION — NOT IMPLEMENTATION

## Objective

Establish the exact legal and observable behavior of the reserved AEGIS scalar-goal range on the installed target build.

## Test matrix

For a disposable qualification goal in the candidate namespace, independently test:

1. `set-goal` write;
2. `goal` read;
3. `up-modify-goal` write;
4. `up-compare-goal` read/compare;
5. fact-to-goal output where relevant;
6. high-value boundary values;
7. adjacent stock-range values as negative controls.

## Required distinction

A goal value being within the global 16,000-goal capacity does not establish that every primitive accepts every goal in every context. Operation-specific legality must be measured.

## Required evidence

Each result records:

`build fingerprint + primitive + exact argument types + goal ID + expected value + observed value + validator result + runtime result + timing`

## Promotion

A candidate namespace entry becomes implementation-qualified only after the exact operation(s) used by the AEGIS subsystem are directly demonstrated on the target build.

## Safety

No stock goal is redefined, repurposed, or overwritten during qualification.
