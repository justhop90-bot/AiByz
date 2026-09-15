# AEGIS Engineering Control Plane — 2026-09-08

This document supplements the existing repository authority model. It does not replace `CANONICAL_AUTHORITY.md`, the canonical handoff, or the dated Layer 1/2 archaeology.

## Design decision

Gemini's proposed `docs/`, `state/`, `evidence/`, and `harness/` split is adopted, with four adjustments:

1. **No stock-source mirroring.** The restored Steam AI tree remains an external A1 evidence source. The repository stores hashes, manifests, inventories, and derived knowledge—not a second mutable copy of stock Promisory.
2. **`state/` is a registry, not an allocation.** It records ownership and evidence status. It does not authorize numeric channels until the ABI gate clears them.
3. **`harness/` is qualification infrastructure, not current implementation.** Existing experiments remain historical/retired where so designated. No new runtime probe is implied by this directory.
4. **`docs/stock/` is a reconstruction index.** It maps stock topology, load closure, subsystem responsibilities, and cross-system state without becoming a runtime dependency.

## Repository control plane

```text
public sources / official docs / historical source
                ↓
          evidence ledger
                ↓
       stock reconstruction
                ↓
      state + syntax registries
                ↓
       AEGIS architecture
                ↓
       implementation source
                ↓
     static → runtime → stress QC
```

## Current phase

**TOTAL-SYSTEM DECONSTRUCTION.**

The immediate target is complete understanding of the stock HD/Promisory substrate and its control topology. Do not jump from this control plane into construction probes, worker-loop experiments, or production `.per` implementation merely because a registry exists.

## Authority classes

| Class | Meaning | Can clear ABI? |
|---|---|---:|
| A1 | Exact target-build installed package/build evidence | Yes |
| A2 | Verified package snapshot | Yes |
| A3 | Byte/content-equivalent repository snapshot | Yes |
| A4 | Historical/source/public documentation | No |
| A5 | Engineering inference | No |

## Claim states

`OBSERVED` → `CORRELATED` → `INFERRED` → `IMPLEMENTED` → `STATIC-QUALIFIED` → `RUNTIME-QUALIFIED` → `STRESS-QUALIFIED`

A claim may be `REJECTED` or `UNQUALIFIED` at any stage.

## Mandatory invariants

- Stock AI is evidence, never an accidental AEGIS runtime dependency.
- Promisory is fully deconstructed as source material, then rehosted/reimplemented under AEGIS ownership as appropriate.
- Numeric equality is not ownership.
- Validator acceptance is not engine semantics.
- Command issuance is not completion.
- World transition is not strategic success.
- A hypothesis never becomes ABI authority by repetition.
- Every AEGIS state channel has one owner and a documented lifecycle.
- Every generated `.per` module must consume the registries rather than inventing local ABI facts.
- Runtime qualification begins only after the relevant subsystem has been deconstructed and its test contract is explicit.
