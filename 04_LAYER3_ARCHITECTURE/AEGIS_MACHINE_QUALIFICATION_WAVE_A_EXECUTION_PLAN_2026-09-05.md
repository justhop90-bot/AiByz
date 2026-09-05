# AEGIS — Machine Qualification Wave A Execution Plan

**Date:** 2026-09-05  
**Status:** ACTIVE  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652

## Objective

Turn the remaining P1 Wave-A questions into controlled target-build experiments without writing the production bot.

## Order

### A. Typed ABI

1. Prove scalar goal write/read boundary.
2. Prove goal comparison boundary separately from goal storage.
3. Prove strategic-number read/write boundary.
4. Prove typed fact signatures with representative concrete IDs and unit-line IDs.
5. Record validator behavior separately from runtime behavior.

### B. Generation

6. Establish a minimal two-generation publication pattern.
7. Confirm stale-generation rejection can be represented with qualified primitives.
8. Test initialization and transition semantics.
9. Test boundary/wrap behavior only if the chosen representation can approach it.

### C. UNKNOWN / ZERO / ABSENCE

10. Establish a confirmed-zero case.
11. Establish a no-result search case.
12. Establish an intentionally unobserved case.
13. Establish an unsupported/invalid query case.
14. Determine whether each case can be distinguished without heuristic inference.

## Rules

- Use disposable qualification scripts, never production AEGIS code.
- Keep the stock `/ai` baseline untouched.
- Each experiment must have one hypothesis and one falsifiable observation.
- Do not infer semantics from validator output alone.
- Do not infer absence from parser/search failure.
- Do not use numeric identity as a substitute for typed identity.
- Do not promote a result until the exact target executable identity is recorded.
- If a result contradicts a load-bearing architecture invariant, stop and reopen only the owning architectural pass.

## Exit criteria

Wave A closes when each P1 question is either:

- directly demonstrated on the target build;
- demonstrated with an explicit target-build limitation; or
- formally blocked with a named next test and no false semantic assumption.

Only after Wave A should the Cavalry Threat Containment vertical slice begin implementation qualification.
