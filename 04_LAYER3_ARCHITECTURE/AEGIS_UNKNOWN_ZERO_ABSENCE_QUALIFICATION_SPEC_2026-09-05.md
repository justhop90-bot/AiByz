# AEGIS — UNKNOWN / ZERO / ABSENCE Qualification Specification

**Date:** 2026-09-05  
**Status:** QUALIFICATION SPECIFICATION — NOT IMPLEMENTATION

## Objective

Determine whether engine-facing evidence can preserve the distinction among:

- confirmed zero;
- search no-result;
- unsupported query;
- intentionally unobserved state.

## Controlled cases

### Case A — confirmed zero
A controlled state in which the queried population is known to be empty.

### Case B — search no-result
A valid search/filter query that returns no matching object.

### Case C — unsupported query
A query whose target/parameter is intentionally invalid or unavailable.

### Case D — unobserved
A state for which AEGIS has not acquired evidence.

## Required result

Determine whether each case produces a distinct engine-observable outcome. If not, the ambiguity must remain explicit in the AEGIS semantic layer rather than being converted into a strategic boolean.

## Historical warning

Official updates have changed search behavior and object-data semantics, including search stacking and pending-object visibility. Therefore the experiment must run against the current target executable.

## Promotion

No UNKNOWN→FALSE coercion is permitted merely because a primitive returned zero, false, or no search result.
