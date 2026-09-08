# P0 Construction Runtime ABI Qualification Protocol — 2026-09-08

## Status
PROTOCOL DEFINED — RUNTIME RESULTS NOT YET CLAIMED

## Objective
Qualify the target-build interpreter semantics of the three stock construction command paths without collapsing them into one abstraction:

1. native `build <unit>`;
2. explicit `up-build-line <point> <point> <building>`;
3. placement-controller `up-build place-control 0 <building>`.

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.

## Evidence rule
A runtime claim is promoted only from direct target-build observation. Static source establishes what stock code asks the interpreter to do; it does not establish exact command side effects, pass timing, or state visibility.

## Experiment matrix

### R1 — Native build
Question: after `can-build` succeeds and `build` is issued, which observable states appear and in what order?

Record at minimum:
- command-issued point;
- foundation existence;
- pending-object state;
- pending-placement state;
- builder assignment;
- object-data target/action/order/status;
- completion;
- command failure/no-op behavior.

### R2 — Explicit build-line
Question: after `up-can-build-line` succeeds and `up-build-line` is issued, does the resulting lifecycle match native `build`?

Do not assume equivalence. Record the same state vector as R1 plus selected placement point and any placement-control state.

### R3 — Placement controller
Question: after placement parameters are established and `up-build place-control 0 <building>` is issued, which state is created before a foundation exists?

Record:
- placement data before issuance;
- placement data immediately after issuance;
- pending-placement;
- pending-object;
- selected point;
- builder assignment;
- foundation;
- completion.

### R4 — Failed explicit placement
Force an invalid or occupied placement candidate while keeping construction otherwise authorized.

Determine whether `up-can-build-line` fails cleanly, leaves placement state, changes placement state, or requires explicit reset.

### R5 — Reset semantics
Create a pending/stalled placement and issue `up-reset-placement`.

Record exactly which state is cleared and which state survives. Test whether the upstream construction demand remains recoverable.

### R6 — Builder assignment visibility
Issue construction followed by `up-assign-builders` and inspect object/task data in the same pass and subsequent passes.

Determine whether assignment is immediately queryable or becomes visible only after an engine/state refresh boundary.

### R7 — Pending-placement versus pending-object
Create a construction that reaches placement/pending state and query both predicates independently.

Determine whether:
- pending-placement implies pending-object;
- pending-object implies pending-placement;
- they represent different lifecycle intervals;
- either can remain true after reset/failure.

### R8 — Same-pass mutation visibility
Use a minimal probe where rule A mutates placement/goal/object state and rule B immediately tests it.

Repeat with and without `up-jump-rule`.

The result must identify whether the mutation is visible:
- later in the same pass;
- only on a subsequent pass;
- only after jump/re-entry;
- or only after engine synchronization.

### R9 — Jump topology
Construct equivalent probes with:
- no jump;
- jump by 1;
- jump over the observer;
- jump into a construction retry block.

Record rule firing order and whether placement commands repeat, suppress, or become unreachable.

### R10 — Escrow interaction
Test authorized construction with sufficient escrow, then deliberately make placement fail.

Determine whether escrow is:
- consumed at authorization;
- consumed at command issuance;
- consumed only when the engine accepts placement;
- restored on placement failure/reset;
- or otherwise retained until completion/cancellation.

## Required telemetry
For every run capture:

```text
pass / rule identity
command issued
strategic state
resource state
escrow state
placement state
pending-placement
pending-object
foundation state
builder state
object-data state
point state
timer state
jump transition
next observable state
```

## Controls
Each experiment must have a control run that changes only the tested variable. Do not infer timing from unrelated games. Prefer deterministic scenarios with fixed starting resources, fixed building availability, and isolated construction objectives.

## Qualification gates

`RUNTIME-QUALIFIED` requires:
1. repeatable observation on target build;
2. at least one control comparison;
3. state-transition ordering recorded;
4. failure behavior recorded where applicable;
5. no contradiction with stock source evidence.

If evidence is ambiguous, retain `INFERRED` or `UNQUALIFIED` rather than promoting the claim.

## AEGIS implementation consequence
Until R1–R10 are qualified, AEGIS Construction OS must not implement an assumed unified `construction.issue` primitive that erases differences between native build, build-line, and placement-controller paths.

The eventual service may unify them at the API boundary, but the implementation must preserve a command-path discriminator internally:

```text
construction.issue
  ├── native-build
  ├── explicit-build-line
  └── placement-controller
```

## Review angles

### ABI / compiler
No command equivalence or same-pass visibility is assumed.

### Byzantine architecture
Placement failure must preserve strategic demand and permit recovery. Defensive and infrastructure placement remain policy-aware.

### AI(HD) + Promisory regression
The stock retry, reset, builder escalation, pending-placement handling, and jump topology must survive reconstruction unless runtime evidence demonstrates a stronger AEGIS replacement.

## Current decision
The static construction archaeology is complete enough to stop searching for more source evidence. The project now requires controlled runtime qualification on the real target interpreter before Construction OS implementation begins.
