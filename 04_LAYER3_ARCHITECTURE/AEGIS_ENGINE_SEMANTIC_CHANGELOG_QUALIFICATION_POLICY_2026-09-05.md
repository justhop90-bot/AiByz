# AEGIS — Engine Semantic Changelog Qualification Policy

**Date:** 2026-09-05  
**Status:** ACTIVE

## Policy

AoE2DE engine updates are treated as potential ABI/semantic changes even when release notes do not explicitly mention a primitive used by AEGIS.

## Required response to every executable change

1. fingerprint executable;
2. compare Steam build identity;
3. classify affected AI/script surfaces;
4. rerun P1 gates touching those surfaces;
5. rerun the minimal Cavalry vertical-slice smoke test;
6. invalidate runtime qualification that depended on changed semantics until requalified.

## Why

Official update history demonstrates that AI behavior has been corrected repeatedly, including search stacking, focus/target facts, pending-object visibility, object-data fields, exploration commands, and argument edge cases. A release note therefore cannot be assumed exhaustive enough to preserve a behavioral ABI.

## Qualification principle

**Build identity is part of the meaning of runtime evidence.**

A passing experiment on build A is not automatically a passing experiment on build B.
