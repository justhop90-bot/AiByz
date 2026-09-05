# AEGIS — Implementation Readiness Decision

**Date:** 2026-09-05  
**Status:** NOT YET READY FOR BROAD IMPLEMENTATION

## Decision

AEGIS is **architecturally ready** but **not yet machine-qualified for broad production implementation**.

## Why

The remaining blockers are concentrated in shared machine semantics rather than subsystem architecture:

- typed ABI;
- state-channel ownership;
- generation/stale authority;
- UNKNOWN/zero/absence;
- search isolation;
- publication coherence;
- operational lifecycle;
- cancellation/supersession;
- runtime cost/latency.

These are cross-system concerns. Solving them once through qualification is materially safer than independently approximating them in every subsystem.

## What is authorized

- disposable qualification experiments;
- target-build evidence acquisition;
- ABI registry updates backed by evidence;
- harness discovery;
- minimal vertical-slice qualification design;
- controlled runtime experiments when their exact scope is known.

## What is not authorized by this decision

- broad production `.per` bot implementation;
- claiming runtime-validated semantics from documentation;
- allocating channels solely by numeric convenience;
- inventing universal state/manager abstractions to avoid qualification;
- treating unresolved UNKNOWN as FALSE;
- treating command issuance as completion.

## Next gate

Close the minimum P1 Wave-A gates required by the Cavalry Threat Containment slice, then implement only the smallest slice needed to validate the architecture against reality.
