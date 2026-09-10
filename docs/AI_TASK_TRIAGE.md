# AEGIS / AiByz — AI Task Triage

**Effective:** 2026-09-10
**Purpose:** Reduce wasted AI work and prevent reopening closed questions.

## First decision

Before doing anything, classify the request as one of:

1. **Proof** — establish or falsify a machine/runtime claim.
2. **Architecture** — resolve a design question using already-qualified evidence.
3. **Implementation** — write candidate `.per` only when gates permit.
4. **Qualification** — test a candidate against the target runtime.
5. **Documentation** — record a decision, evidence package, or supersession.
6. **Repository hygiene** — organize references without changing semantics.

Do not mix categories unless the dependency is explicit.

## Do-not-spend-time list

Unless current authority explicitly reopens them, do not spend implementation effort on:

- broad Layer-1 archaeology;
- broad Layer-2 archaeology;
- scenario-loader automation;
- XS integration;
- ADprom as architecture;
- byzwarcouncil as architecture;
- unqualified numeric allocation;
- speculative ownership of stock channels;
- replay claims that exceed W0/W1 evidence;
- copying historical bot code merely because it looks complete;
- branch-by-branch archaeology when a canonical register already answers the question.

Historical material may still be searched when it is the evidence required to answer a specific unresolved claim.

## Current priority queue

### P0 — Authority consistency

Confirm that a proposed decision agrees with current `main`, Final Audit, progress docs, and supersession rules. If not, stop and reconcile.

### P1 — R1 load / conditional closure

Resolve remaining effective-load uncertainty with evidence. Do not infer runtime dependency from source presence.

### P1 — R2 ownership

Complete the mutable-state ownership matrix needed by the first slice. Every state/channel used by candidate production logic needs an identified owner, writer, reader, guard, reset, and generation/lifecycle behavior where applicable.

### P1 — R3 numeric / typed ABI

No allocation is cleared merely because a value appears unused or a validator accepts it. Allocation requires evidence-backed ownership/ABI clearance.

### P1 — R5 command lifecycle

Qualify the distinction between issued, accepted, pending, created, available, and effective for actions relied upon by the civilian slice.

### P2 — Civilian Production Loop qualification

Only after its prerequisite gates are closed. Keep the slice minimal and observable.

### P3 — Later strategic slices

Cavalry Threat Containment and other broader strategy work remain secondary until the current qualification frontier permits expansion.

## Required output for every substantive task

End the task with:

- **Question:**
- **Evidence inspected:**
- **Finding:**
- **Evidence level:**
- **Status:**
- **What remains unknown:**
- **Gate affected:**
- **Repository artifact updated:**
- **Next minimum action:**

## Escalation rule

If the next action would require guessing engine semantics, changing an ABI assumption, or promoting production `.per` without the required gate, stop. Document the blocker instead of improvising.

## Efficiency rule

Prefer one decisive evidence package over many speculative edits. Prefer updating an existing canonical artifact over creating a new report. Prefer a falsifiable probe over a long argument from analogy.
