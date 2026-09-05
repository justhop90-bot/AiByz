# AEGIS — Generation / Stale Authority Qualification Specification

**Date:** 2026-09-05  
**Status:** QUALIFICATION SPECIFICATION — NOT IMPLEMENTATION

## Objective

Determine whether the chosen scalar state representation can prevent an obsolete commitment or execution context from being accepted after a newer publication supersedes it.

## Minimum experiment

1. publish generation G;
2. capture a dependent commitment/action context;
3. publish generation G+1;
4. attempt to use the G context;
5. observe whether the controller can distinguish stale from current;
6. verify that G+1 remains authoritative.

## Required evidence

- generation storage semantics;
- comparison semantics;
- initialization semantics;
- update semantics;
- publication coherence;
- stale-use behavior;
- failure behavior when generation evidence is unavailable.

## Architectural rule

If the engine cannot directly enforce stale-generation rejection, AEGIS must not pretend it can. The implementation contract must then move the check to a layer where it can be observed and enforced without creating a hidden second authority system.
