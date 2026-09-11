# B-OBS Runtime Qualification v0.1

**Status:** PREPARED — execution artifact

**Target:** `players-building-type-count any-enemy <building>`

**Purpose:** determine whether the existing enemy-building observation primitive can be used in a narrow, non-mutating condition. This is an observation qualification only. It does not establish unit-composition observation, player-selector semantics in general, or Byzantine policy authority.

## 1. Question

Does the existing primitive:

```lisp
(players-building-type-count any-enemy <building>)
```

load successfully and evaluate against an actual enemy-owned building in the selected test configuration?

The experiment is deliberately narrower than a full enemy-composition system.

## 2. Static evidence boundary

The corpus contains uses of `players-building-type-count` with player selectors other than `any-enemy`. The current source evidence therefore supports the primitive's existence and syntax family, but does not by itself establish the engine semantics of `any-enemy` for this operation.

**Status of the specific proposition:** RUNTIME UNKNOWN.

No claim is made that `any-enemy` is universally valid for every player-scoped primitive merely because it appears plausible.

## 3. Artifact shape

The test artifact is observational only. It does not write a Goal, timer, scratch register, Strategic Number, production quota, or other policy state.

The test condition should use a building type whose construction is guaranteed by the selected enemy test configuration. The instrumentation action is a local chat message.

Conceptual artifact:

```lisp
(defrule
  (players-building-type-count any-enemy <known-building-type> > 0)
  =>
  (chat-local-to-self "B-OBS enemy building condition fired")
  (disable-self))
```

`<known-building-type>` must be replaced only with an existing building constant whose identity is already established by the source corpus/test configuration. No new symbolic ABI is introduced by this experiment.

The `disable-self` is instrumentation control, not policy state. Its one-shot behavior remains separately qualified rather than assumed to establish general rule-lifetime semantics.

## 4. Preconditions

1. The selected building type is statically identified.
2. The enemy test configuration is known to produce that building.
3. The AI artifact loads without modifying AiBuilder's existing policy channels.
4. No Goal, timer, scratch register, or Strategic Number is allocated by the test.
5. The condition is the only observation under qualification.
6. The enemy is actually present in the test configuration.

## 5. Observation criteria

### CONFIRMED

The artifact loads, the enemy produces the selected building, and the condition fires in temporal correspondence with the enemy building existing.

### INCONCLUSIVE

The artifact loads but the test cannot distinguish selector failure from timing, building identity, enemy setup, or instrumentation ambiguity.

### DISPROVEN

The primitive demonstrably fails to parse/load or sufficiently controlled evidence establishes that `any-enemy` does not identify the enemy for this operation under the tested conditions.

A parse/load failure should be reported separately from a semantic failure when the evidence permits that distinction.

## 6. What this does NOT establish

A pass does not establish:

- `players-unit-type-count any-enemy` semantics;
- arbitrary player-selector compatibility across primitives;
- enemy unit composition observation;
- nearest-enemy semantics;
- full enemy intelligence;
- Byzantine policy authority;
- any Goal/timer allocation legality.

A pass establishes only the tested building-observation relationship.

## 7. Next use

If confirmed, the result supports a first coarse Byzantine observation slice based on known enemy infrastructure. A separate qualification is still required before using enemy unit-composition counts as authoritative policy input.
