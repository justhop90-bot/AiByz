# `position-goal` Exact Static Producer/Consumer Graph — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Status:** STATIC DECONSTRUCTION; runtime semantics remain separately qualified

## Corpus result

A direct scan of the restored target-build `AI (HD version).per` plus the 36-file Promisory corpus found **368 behavioral rule blocks** containing `position-goal` across **11 behaviorally relevant source files**.

The broader lexical footprint is 14 files because several constant/declaration files mention the symbol without participating in behavioral rule blocks.

### Behavioral source distribution

| Source | Rule blocks containing `position-goal` |
|---|---:|
| `AI (HD version).per` | 197 |
| `init.per` | 94 |
| `units.per` | 33 |
| `buildings.per` | 24 |
| `escrow.per` | 11 |
| `general.per` | 11 |
| `interaction.per` | 6 |
| `researches.per` | 4 |
| `boarhunting.per` | 2 |
| `threats.per` | 2 |
| `tsa.per` | 1 |

## Exact producer surface

There are **8 static writer sites** in the behavioral corpus.

### Initialization / default state

`init.per`:

- lines **289–306**: establishes `position-goal = flank` during initialization.
- lines **622–626**: changes `position-goal` to `pocket` under the relevant conditional branch.
- lines **627–631**: changes `position-goal` to `flank` under the alternate branch.
- lines **632–641**: changes `position-goal` to `flank` when the nomad/land-nomad and distance predicates apply.
- lines **642–647**: changes `position-goal` to `pocket` under the relevant `UP-MICHI-STYLE` branch.

### Controller strategy state

`AI (HD version).per`:

- lines **5121–5160**: initialization/reset rule explicitly sets `position-goal = 0` while resetting a wider strategic state bundle.
- lines **5252–5263**: sets `position-goal = pocket` and simultaneously sets strategy/unit/control state for pocket strategy.
- lines **5264–5273**: sets `position-goal = flank` for the alternate topology.

The eight writer sites are therefore not eight independent strategic decisions. Five belong to initialization/topology setup; three belong to controller initialization/strategy transition.

## Static writer interpretation

The strongest source-level conclusion is:

```text
position-goal is established primarily as a map/topology classification state.
```

The initial values are `flank` or `pocket`, with the controller also using `0` as a reset/default sentinel during a broad initialization rule.

This is stronger than calling `position-goal` merely a generic coordinate variable. The downstream uses must still be traced before assigning a final AEGIS semantic type.

## Consumer surface

The remaining **360 behavioral rule blocks** are consumers or mixed consumer/side-effect blocks. They are distributed across economy, construction, production, military, research, scouting/interaction and general support.

The recurring downstream primitive families include:

- `up-get-point`
- `up-set-target-point`
- `up-set-target-object`
- `up-find-local`
- `up-find-remote`
- `up-filter-distance`
- `up-target-objects`
- `build`
- other engine-facing targeting/placement operations

The important point is that `position-goal` is rarely the final action. It is an **intermediate coordination signal** that changes which spatial/search/target path later rules use.

## Key topology

```text
                 initialization / map classification
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
                 pocket               flank
                    │                   │
                    └─────────┬─────────┘
                              ↓
                       position-goal
                              ↓
                 spatial/search consumers
                    │       │       │
                    ↓       ↓       ↓
                economy  building  military
                    │       │       │
                    └───────┴───────┘
                            ↓
                     engine-facing action
```

## Important static examples

The controller transition around lines 5252–5273 demonstrates coupling of three state channels:

```text
position-goal
strategy-goal
unit-goal
control-goal
```

The pocket rule writes all four together. The flank rule changes only `position-goal`.

This asymmetry matters: the historical controller does not treat every position classification as a complete strategy transition.

Construction consumers are particularly important because `position-goal` appears alongside placement/building operations. These relationships must not be simplified into “position-goal = building location”; the same state is consumed elsewhere.

## Reset / invalidation

Static extraction identifies explicit writer/reset behavior but does **not** prove an engine-level invalidation lifecycle. In particular, the `0` assignment in the broad AI initialization rule is a source-level reset sentinel, not proof that `0` universally means “invalid position” at runtime.

Future graph work must distinguish:

```text
initialization reset
vs.
strategy transition
vs.
consumer interpretation
vs.
runtime invalidation
```

## AEGIS implication

Do **not** reproduce `position-goal` as one global AEGIS integer.

The reconstruction candidate should be a typed spatial posture/context object with explicit ownership, e.g. conceptually:

```text
SpatialPosture
 ├─ topology classification
 ├─ strategic position role
 ├─ selected endpoint/target
 ├─ validity/generation
 └─ consumers
```

The exact AEGIS representation is deferred until the other distributed channels are joined.

## Evidence boundary

**STATIC-QUALIFIED:** source locations, writer count, source distribution, visible state mutations and visible downstream primitive usage.

**TARGET-BUILD-UNKNOWN:** interpreter pass timing, same-pass mutation visibility, precise runtime meaning of sentinel `0`, persistence of state between rule passes, and whether every downstream consumer observes the same mutation epoch.

No runtime experiment was performed for this extraction.
