# AEGIS — Wave A Machine Qualification Evidence

**Date:** 2026-09-05  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652  
**Status:** ACTIVE — P1 QUALIFICATION IN PROGRESS

## Established

- Build identity is stable and directly fingerprinted.
- Untouched stock HD AI closure is frozen as baseline.
- Goal capacity has authoritative evidence of 16,000.
- Scalar AEGIS namespace candidate `10000–15999` remains the Layer-2 reserved range, subject to operation-specific qualification.
- Numeric identity is not semantic identity.
- Stock AI demonstrates typed fact usage and conditional constant definitions; therefore symbol interpretation must be context-aware.
- Search, focus/target fact, pending-object, and object-data semantics have historically changed through official engine fixes.

## Still unproven

- exact target-build legality of every selected AEGIS goal operation;
- exact target-build typed fact behavior for the selected cavalry sensor;
- generation representation and stale-generation rejection;
- UNKNOWN/zero/absence distinctions;
- publication atomicity;
- command acceptance/pending/created/available lifecycle;
- cancellation/supersession behavior;
- runtime cost envelope.

## Engineering decision

Do not widen the vertical slice until these questions are resolved for the exact primitives it uses.

The project is therefore moving from architecture construction into **controlled machine qualification**, with the first target being the minimum primitive set required to represent and verify one cavalry-threat containment commitment.
