# Pass 57 — Dynamic Commitment Switching & Recovery Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation authority:** NONE  
**Status:** PASS / MAJOR CLOSURE  
**Predecessor:** Pass 56

## Mission
Determine whether historical AI resource commitments are reversible and how controllers recover when a commitment succeeds, fails, becomes invalid, or is superseded.

## Executive finding
Historical HD AI uses explicit resource-control identities, escrow, release/reset paths, and controller state changes that demonstrate **reversible commitments**. A commitment is not necessarily permanent once established.

Canonical lifecycle reconstruction:

```text
OPEN
↓ demand
CLAIMED
↓
SAVING
↓
STILL VALID / INVALID
↓
AFFORDABLE
↓
AUTHORIZED
↓
EXECUTING
↓
COMPLETED
```

With recovery branches:

```text
INVALID → RELEASE → OPEN
REPLACED → NEW COMMITMENT
WAITING → REASSESS
```

This is a research reconstruction, not a literal historical FSM.

## Direct findings

- `sn-resource-control` is repeatedly used as a specific commitment identity, not merely as a universal numeric priority.
- Commitments protect resources through escrow.
- Successful execution can clear resource-control.
- Invalidating conditions can clear resource-control.
- Some historical controllers redirect one commitment to another target.
- Strategic pressure can override a savings state in selected historical paths.
- The system therefore contains rule-mediated preemption/recovery mechanisms.

## Critical distinction

```text
COMMITMENT ≠ AUTHORITY
ESCROW ≠ OWNERSHIP
STATE WRITE ≠ EXCLUSIVE CONTROL
```

A state value only becomes an effective gate when surrounding readers enforce it.

## Commitment transition taxonomy

### Completion
```text
CLAIM
→ resource protection
→ affordability
→ side effect
→ release/reset
```

### Invalidation
```text
CLAIM
→ prerequisite disappears
→ release/reset
→ candidate reopened
```

### Replacement
```text
CLAIM A
→ state changes
→ CLAIM B
```

### Continued waiting
```text
CLAIM
→ still valid
→ remain protected
→ retry/reassess
```

Cancellation and replacement must remain separate archaeological categories.

## Commitment half-life

AEGIS research introduces **commitment half-life** as an analytical concept:

```text
INITIATION
→ EXPECTED VALIDITY WINDOW
→ REASSESSMENT
→ REINFORCEMENT OR RELEASE
```

This is not an engine term and is not claimed as historical implementation vocabulary.

## Open questions

- Is commitment age explicitly represented?
- Are timers used as commitment expiration mechanisms in the HD corpus?
- Can release and successor claim occur in the same pass?
- Which controllers can overwrite another controller's commitment?
- Does resource commitment decay, or only explicit release/reset remove it?
- Are some commitments effectively sticky because of rule topology?

## Byzantine implication

Byzantines have multiple legitimate resource claimants: Camels, Cataphracts, Monks, Siege, Navy, Imperial transition, and upgrades. Therefore a Byzantine controller must eventually be able to abandon or redirect a counter commitment when the threat state changes.

Historical evidence supports the substrate conceptually:

```text
DEMAND
→ CLAIM
→ PROTECT
→ AUTHORIZE
→ SPEND
→ COMPLETE / INVALIDATE
→ RELEASE
→ REOPEN
```

It does **not** prove the optimal Byzantine policy for choosing among these commitments.

## Evidence ledger

| Finding | Grade |
|---|---|
| Resource commitments represented explicitly | DIRECT |
| Named resource-control values identify intended expenditures | DIRECT |
| Commitments protect resources through escrow | DIRECT |
| Successful execution can clear commitment | DIRECT |
| Invalid conditions can clear commitment | DIRECT |
| Strategic pressure can override selected savings states | DIRECT |
| Commitment is reversible | DIRECT / COMPOSED |
| Commitment replacement exists | DIRECT |
| Global preemptive scheduler exists | NOT PROVEN |
| Global utility optimization exists | NOT PROVEN |
| Universal fairness exists | NOT PROVEN |
| Commitment expiration/half-life is an engine feature | NOT PROVEN |
| Same-pass release → successor claim | OPEN |

## Layer boundary

No `.per` implementation or architecture implementation is created. Layer 2 remains research-only.
