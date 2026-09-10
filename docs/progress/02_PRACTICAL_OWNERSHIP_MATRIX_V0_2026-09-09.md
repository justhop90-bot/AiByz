# AEGIS Practical Ownership Matrix V0 — 2026-09-09

**Status:** First practical matrix for high-priority channels  
**Parent:** FINAL_RECONSTRUCTION_AUDIT R2  
**Evidence basis:** Runtime topology 2026-09-05 + typed census notes + existing implementation candidates  
**Scope:** Channels most relevant to civilian/economic loop and early vertical slices.  
**Not a complete stock ledger.**

## Rules

- Numeric equality ≠ semantic ownership.
- AEGIS must not hijack heavily-used stock channels as its universal control envelope.
- Every AEGIS-owned channel requires: declaration, owner, generation/validity pattern, writers, readers, reset policy.
- This matrix is a working instrument, not final clearance.

## High-traffic stock channels (do not casually claim)

### Goals (from topology)
| Symbol / channel | Approx writes | Approx reads | Notes |
|------------------|---------------|--------------|-------|
| unit-goal | 432 | 122 | Heavy stock use |
| control-goal | 335 | 142 | Heavy stock use |
| strategy-goal | 328 | 120 | Heavy stock use |
| ranged-unit-type-goal | 229 | 21 | Stock military |
| increase-town-size-goal | 171 | 10 | Stock |
| uu-up-goal | 146 | 4 | Stock |
| attack-goal | 81 | 22 | Stock attack state |
| train-civ-goal | 43 | — | Civilian related |
| farm-goal | 36 | 6 | Economy |
| escrow-purpose-goal | 24 | 1 | Escrow |
| attack-status-goal | 19 | — | Attack lifecycle |
| retreat-now-goal | 14 | — | Retreat |
| under-attack-goal | 7 | 7 | Threat |

### Strategic numbers (heavy writers)
- sn-wood/gold/food/stone-gatherer-percentage (very high write counts)
- sn-resource-control
- sn-maximum-town-size
- sn-focus-player-number / sn-target-player-number
- sn-number-explore-groups, sn-military-level, threat-related SNs

**Policy:** AEGIS shall not re-purpose the above as its primary private state without explicit, evidence-backed takeover design.

## AEGIS candidate private channels (from existing v0 code)

The current implementation candidates already claim a local namespace in the low 400s for civilian lifecycle:

| Goal | Purpose (from v0 code) | Status |
|------|------------------------|--------|
| aegis-vr-generation (441) | Lifecycle generation | Candidate only |
| aegis-vr-valid (442) | Validity flag | Candidate only |
| aegis-vr-stage (443) | Stage machine | Candidate only |
| aegis-vr-baseline-villagers (444) | Baseline census | Candidate only |
| aegis-vr-observed-villagers (445) | Observed census | Candidate only |
| aegis-vr-pending (446) | Pending flag | Candidate only |
| aegis-vr-confirmed-delta (447) | Confirmed delta | Candidate only |
| aegis-vr-attempts (448) | Attempt counter | Candidate only |
| aegis-vr-observed-at (449) | Timestamp-like | Candidate only |

These numbers are **not cleared**. They are recorded here so future allocation work has a concrete starting point and collision check target.

## Recommended AEGIS ownership pattern (to be used in all new code)

For every AEGIS-owned scalar:
```
VALID + GENERATION + STAGE + PAYLOAD + (optional) ATTEMPTS / OBSERVED-AT
```

Writer uniqueness is preferred.  
Reset must be explicit.  
Stale generation must be rejected.

## Next matrix work

1. Extract every `defconst` / goal / SN reference from the current `implementation/*.per` set into a structured table.
2. Cross-check against the large collision JSON.
3. Expand only the channels required by the first vertical slice.
4. Produce a machine-readable ownership file once the first slice is frozen.
