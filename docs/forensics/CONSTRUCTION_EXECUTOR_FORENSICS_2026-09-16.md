# Construction Executor Forensics — 2026-09-16

**Status:** forensic reconstruction complete for source-visible executor behavior; runtime-only semantics remain explicitly qualified.

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652

**Primary executor source:** `AiBuilder/construction.per` (blob `9446b4bb13e4e4f732cd3b9a79d088ec3267806d`).

## 1. Executive result

The runtime-loaded AiBuilder construction layer is an engine-facing executor, not a strategic planner. It consumes existing Goal/strategic-number state and emits native construction commands. The source directly verifies that ordinary construction is issued through `build <building-type>`, while advanced placement/search paths use `up-*` primitives such as `up-build-line`, `up-find-local`, `up-find-remote`, `up-set-target-object`, `up-set-target-point`, and `up-reset-placement`.

The source does **not** establish that `build` and `up-build` are interchangeable. `build` is a normal executor primitive used throughout the ordinary building rules. `up-build-line` is a distinct advanced placement/execution primitive. Shadow additionally demonstrates `up-build place-normal/place-point` forms, but those forms are not present in the current AiBuilder construction source and therefore must not be transplanted as if their runtime semantics were proven here.

## 2. Verified construction request path

The current executor has two observable paths.

### A. Ordinary construction

Representative rules test:

- desired building count
- pending-object count where relevant
- resource/serviceability conditions
- `can-build <type>`

and then issue:

```lisp
(build <building-type>)
```

This pattern is used for town centers, houses, lumber camps, mills, mining camps, barracks, ranges, stables, workshops, blacksmiths, markets, docks, universities, monasteries, castles, outposts, watch towers, and bombard towers.

### B. Advanced placement construction

The farm-placement subsystem first establishes a search/target state, derives candidate points, validates a build line, and then emits:

```lisp
(up-build-line point3-x point3-x c: farm)
```

This is a materially different path from ordinary `build farm`.

## 3. `build` vs `up-build`

### Directly established

`build <type>` is the standard AiBuilder construction executor. It is guarded by `can-build` in the ordinary rules and therefore sits at the final execution boundary of those rules.

### Shadow evidence

Shadow contains advanced forms using `up-build` together with placement modes. This establishes that the DE AI scripting ecosystem contains a distinct `up-build` family and that Shadow used it in explicit placement transactions.

### Not yet proven

The current AiBuilder source does not expose a direct semantic equivalence table for `build` versus `up-build`, nor does source inspection alone prove whether either command means “issued”, “accepted”, “foundation created”, or “construction completed”. The project’s command-lifecycle probe contract explicitly requires these stages to be distinguished.

**AEGIS rule:** treat both as command issuance primitives until target-build runtime probes prove later lifecycle stages.

## 4. Placement modes

### AiBuilder source-visible placement mechanisms

The current executor visibly uses:

- `up-set-target-object`
- `up-get-point position-object ...`
- `up-set-target-point`
- `up-reset-placement`
- `up-build-line`
- `up-can-build-line`

The farm subsystem therefore separates candidate selection, point derivation, placement validation, and execution.

### Shadow placement forms

The Shadow corpus contains `place-normal`, `place-control`, and `place-point` arguments associated with `up-build`. These are source evidence for historical/stock advanced placement policy, but the present executor source does not independently define their semantics.

**Qualification:** placement-mode meanings remain engine-level runtime questions. Do not assign semantic labels such as “normal = automatic”, “control = controlled”, or “point = exact point” as implementation facts until the target build is probed.

## 5. Builder assignment

The inspected construction executor does not contain an explicit `up-assign-builders` call in the source examined here. Ordinary `build` rules also do not manually select individual villagers.

Therefore the verified architecture is:

```text
construction policy / prerequisites
        ↓
AiBuilder construction executor
        ↓
build / advanced up-* construction primitive
        ↓
engine-side builder selection / construction lifecycle
```

Any claim that AiBuilder itself assigns a particular builder through `up-assign-builders` is **not established by this source**.

## 6. Escrow timing

The ordinary AiBuilder construction rules inspected here use `can-build` and issue `build`; they do not visibly implement Shadow’s explicit `set-goal gl-escrow-state with-escrow` / `release-escrow` transaction around each ordinary build.

Shadow therefore demonstrates a stronger explicit commitment model than the current executor source demonstrates.

**Architectural consequence:** AEGIS should not assume that an AiBuilder `build` call creates an explicit escrow reservation. If AEGIS introduces commitment state, it must be its own authorization/commitment layer and must not be confused with engine-side resource deduction.

## 7. Pending-state lifecycle

The executor repeatedly tests:

```lisp
(up-pending-objects c: <building> <= 0)
```

and the town-size logic tests:

```lisp
(up-pending-placement c: <building>)
```

This establishes two distinct controller-visible pending concepts:

1. pending objects
2. pending placement

They are used as duplicate-suppression and placement-state guards.

The source does **not** prove that pending state implies foundation creation or eventual completion. The command-lifecycle evidence standard therefore remains:

```text
ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE
```

with each transition requiring independent evidence.

## 8. Completion/failure observability

The executor verifies construction indirectly through ordinary world-state predicates such as:

- `building-type-count-total < desired-count`
- `building-type-count-total >= ...`
- pending-object state
- pending-placement state
- resource/dropsite state

The advanced farm search additionally uses object/search state and placement validation.

This is sufficient to show that the executor participates in a feedback loop, but **not** sufficient to equate any single command or pending flag with completion.

For AEGIS, completion should be represented only after an observable world-state transition, e.g. a confirmed building count/object/foundation lifecycle signal appropriate to the specific command.

## 9. State writers and ownership

The current construction source writes several shared state channels, including:

- `desired-number-*` goals
- `temporary-goal*` scratch goals
- goal `508` as a temporary saved focus-player value in the mining-camp search
- goal `509` as a point/search payload in multiple paths
- goal `510` as a farm-demand payload
- `sn-maximum-town-size`
- `sn-camp-max-distance`
- `sn-allow-adjacent-dropsites`

This is important for ABI allocation: **508–510 are demonstrably occupied by existing construction logic and are not safe AEGIS private channels.**

The existing AEGIS civilian inventory previously marked 504–507 as experimental channels for source/dropsite serviceability; those values must also be treated as unsafe until a complete collision census proves otherwise. The current repository explicitly states that the experimental civilian numeric space is not cleared for production.

## 10. Safe numeric ABI allocation

### Verified unsafe region

At minimum, the following numeric channels are already claimed by the inspected construction/candidate system:

- 504–507 — existing AEGIS candidate source/dropsite block; not production-cleared
- 508 — construction temporary saved player number
- 509 — construction point/search payload
- 510 — construction farm-demand payload

The repository’s broader candidate inventory also contains experimental ranges 403–420, 427–449, 465–478, 490–507, 519–525, and 546–554. These are explicitly marked experimental rather than cleared.

### Allocation rule

No new production AEGIS construction channels should be allocated from an unverified numeric range merely because it appears unused in one file.

A safe channel requires:

1. full stock/engine census
2. full current AiByz writer census
3. full candidate-module census
4. load-closure check
5. collision check
6. semantic-type assignment (goal/SN/timer/etc.)
7. runtime qualification where engine visibility is material

Until that census is complete, a numeric value is **UNSAFE/UNVERIFIED**, not “free”.

## 11. Construction authority boundary

The evidence now supports the following separation:

```text
AEGIS cognition
  ↓
construction requirement / priority
  ↓
AEGIS authorization + commitment state
  ↓
existing AiBuilder desired-number-* channels
  ↓
AiBuilder feasibility / placement / execution
  ↓
build or advanced up-* command
  ↓
engine lifecycle
  ↓
independent observation
  ↓
AEGIS verification + reassessment
```

The critical prohibition is:

```text
command issued ≠ construction completed
```

and likewise:

```text
pending ≠ completed
```

## 12. Code-readiness decision

**Construction specification: READY.**

**Production construction implementation: NOT YET CLEARED.**

The remaining blocker is no longer understanding the basic executor architecture. It is runtime qualification of the engine-facing lifecycle and a complete numeric ABI collision census. Once those are closed, AEGIS can implement the authority layer without replacing AiBuilder’s proven execution machinery.

## Evidence hierarchy

- **DIRECT:** current `AiBuilder/construction.per` source.
- **COMPOSED:** comparison of current AiBuilder executor with canonical Shadow construction source.
- **INFERRED:** architectural separation of AEGIS authorization from AiBuilder execution.
- **UNCERTAIN:** exact engine lifecycle semantics of `build`, `up-build`, placement-mode arguments, and pending-state transitions until target-build runtime probes are completed.
