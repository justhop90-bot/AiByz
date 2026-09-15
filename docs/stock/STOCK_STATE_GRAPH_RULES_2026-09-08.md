# Stock State-Graph Rule Extraction Contract — 2026-09-08

**Status:** STATIC DECONSTRUCTION

The persistent-channel graph identifies the interfaces. This document defines the exact evidence required to turn those interfaces into a machine-level dependency graph.

## Required edge record

```text
EDGE_ID
CHANNEL
SOURCE_FILE
RULE_START
RULE_END
ACTIVATION_CONTEXT
READ_OPERATION
WRITE_OPERATION
RESET_OPERATION
OTHER_STATE_READS
OTHER_STATE_WRITES
OBJECT_SEARCHES
ENGINE_ACTIONS
PROBABLE_CONSUMER
PROBABLE_PRODUCER
LIFECYCLE_ROLE
EVIDENCE_STATUS
NOTES
```

## Four distributed channels

### `control-goal`

Primary question: what control state crosses the controller, initialization, and interaction layers, and which state transitions depend on it?

Required joins:

```text
control-goal mutation
 → control/interaction action
 → affected subsystem
 → resulting state read
 → reset/supersession
```

### `position-goal`

Primary question: which rules use the channel as a spatial intermediary, and which object/search primitives consume the resulting position?

Required joins:

```text
position producer
 → coordinate/search operation
 → endpoint or target
 → engine action
 → observed object state
```

### `enemy-goal`

Primary question: where is enemy identity established, transformed, consumed, and replaced?

Required joins:

```text
enemy observation
 → enemy-goal
 → threat/target classification
 → military/construction/research response
 → stale-target reset/replacement
```

### `farm-goal`

Primary question: how does food-infrastructure demand propagate from policy into construction and then back into economy state?

Required joins:

```text
farm demand
 → build eligibility
 → placement
 → builder assignment
 → pending foundation
 → completed farm
 → economic capacity
```

## Static classification rules

A rule is a **producer** when its side effect establishes or changes the channel value.

A rule is a **consumer** when its conditions or actions branch on the channel value.

A rule is a **resetter** when it explicitly clears, replaces, invalidates, or supersedes the channel state.

A rule may occupy multiple roles.

A rule is **not** considered an engine action merely because it changes a goal/SN. Engine-facing classification requires an actual command/action primitive or an explicitly established intermediate operation.

## Evidence discipline

The graph may record a structural edge as `STATIC-QUALIFIED` when the source relationship is directly visible.

It must remain `TARGET-BUILD-UNKNOWN` when the question depends on interpreter scheduling, mutation visibility, pending transitions, or command completion.

It must never upgrade an inferred semantic relationship to observed runtime behavior.

## Reconstruction objective

The final graph should allow the engineer to answer, for any important state mutation:

> Who produced this state, under what activation context, who consumed it, what physical action did it authorize, what evidence confirmed the result, and what mechanism invalidated or replaced it?

That is the minimum required understanding before freezing AEGIS ownership contracts.
