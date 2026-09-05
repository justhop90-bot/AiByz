# Pass 58 — Dynamic Commitment Switching & Recovery QC

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Status:** PASS / QC CLOSED WITH BOUNDARIES

## Purpose
Hostile QC of the commitment-switching model established in Pass 57.

## Corrections

1. A commitment must not be treated as permanent merely because a resource-control value persists.
2. `sn-resource-control` values are controller-dependent; numeric values such as 1/2/3 are not a universal priority scale.
3. Clearing a commitment proves state transition, not necessarily strategic abandonment.
4. Replacing commitment A with B proves replacement, not optimality.
5. Resource-control should be called an admission/commitment channel rather than a formal mutex.
6. Economic lock-in is an AEGIS analytical abstraction; the historical evidence more precisely establishes **commitment persistence pressure**.
7. Controller oscillation is not to be generalized from related scripting-family evidence into a universal AoE2 HD historical behavior.

## Strengthened model

```text
OPEN
↓
CLAIM
↓
PROTECT / SAVE
↓
VALIDITY CHECK
├── invalid → RELEASE → OPEN
├── replaced → NEW CLAIM
├── still valid → WAIT / REASSESS
└── affordable → AUTHORIZE
                ↓
              ACTION
                ↓
             COMPLETE
                ↓
             RELEASE
```

## New research targets

- commitment persistence frequency
- explicit expiration timers
- facts that revoke commitments
- controller overwrite behavior
- sticky commitments caused by rule order
- same-pass release → successor claim
- repeated claim/release oscillation

## Evidence boundary

Historical HD evidence establishes reversible commitments and selected replacement/release paths. It does not establish a centralized scheduler, global utility optimizer, universal fairness, or a universal commitment timeout.

## Byzantine implication

The correct eventual Byzantine model must permit commitment revision as threat, affordability, timing, or strategic state changes. It must not assume that selecting one counter permanently reserves the economy.

## Layer boundary

Research only. No `.per` implementation, architecture implementation, or deployment.
