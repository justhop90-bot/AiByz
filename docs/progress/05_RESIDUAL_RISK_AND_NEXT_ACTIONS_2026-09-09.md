# AEGIS Residual Risk & Next Actions — 2026-09-09 (updated after Pass 2)

**Status:** Working decision record  
**Parent:** FINAL_RECONSTRUCTION_AUDIT_2026-09-09.md

## What is now stronger

- Static load closure documented at high confidence.
- Practical ownership matrix + concrete inventory of channels used by current civilian candidates.
- Conservative ABI allocation policy published; **zero numbers cleared**.
- Command-lifecycle probe pack designed; skeletons exist.
- First vertical slice (Civilian Production Loop) has an explicit contract.

## What remains blocked for production coding

1. **R5 Command lifecycle** — requires live target-build probe results.
2. **Numeric clearance** — the experimental blocks 427–449, 465–478, 490–497 and timer 42 are unproven.
3. **World realization** beyond controlled civilian pending/census signals.
4. Full stock ownership matrix (only the practical subset exists).

## Acceptable residual risk for limited candidate coding

Candidate / experimental coding that continues the existing civilian style is acceptable when:

- Every channel carries generation + validity.
- No claim is made that later lifecycle stages are proven.
- All new numbers are listed in the ownership inventory.
- Modules remain explicitly marked “NOT LOADED by production root” / candidate.

Production roots and any claim of a playable AI remain blocked.

## Recommended next actions (priority order)

1. **Execute probes** CL-1 and CL-3 on the exact target build; commit evidence records.
2. Finish ownership extraction for the remaining `implementation/*.per` files.
3. Collision-check the experimental numeric blocks against the full typed census.
4. Freeze the civilian vertical-slice contract after the first successful live runs.
5. Only then begin limited production-oriented coding under the residual-risk rules above.

## Authority note

This document does not supersede the Final Reconstruction Audit. It records progress and residual risk after the 2026-09-09 autonomy passes.
