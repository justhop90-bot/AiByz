# AEGIS Implementation Candidates

**Status:** Experimental / candidate modules only.  
**Rule:** Nothing in this directory is a production AI root until gates close.

## Mandatory markers

Every `.per` file here must include a header stating it is:

```text
NOT LOADED by production root
```

## Current focus

**Primary vertical slice:** Civilian Production Loop  
See `docs/progress/07_CIVILIAN_VERTICAL_SLICE_CONTRACT_V0_2026-09-09.md`

## Ownership

Numeric channels used by these modules are inventoried under `docs/progress/`.  
**No numbers are production-cleared.**

## Envelope pattern

```text
GENERATION + VALID + STAGE + PAYLOAD (+ ATTEMPTS / OBSERVED-AT)
```

## Do not

- Load these as the player-facing AI without residual-risk acceptance
- Remove the NOT LOADED marker
- Treat train/build issue as completion proof
- Allocate new goal/SN numbers without updating the ownership inventory

## Related

- Probes: `docs/progress/probes/`
- ABI policy: `docs/progress/03_ABI_ALLOCATION_POLICY_2026-09-09.md`
- Residual risk: `docs/progress/05_RESIDUAL_RISK_AND_NEXT_ACTIONS_2026-09-09.md`
