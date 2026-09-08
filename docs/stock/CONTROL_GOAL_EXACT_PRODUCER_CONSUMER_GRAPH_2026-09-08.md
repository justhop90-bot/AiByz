# Stock `control-goal` Exact Producer/Consumer Graph — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`  
**Corpus:** restored target-build `AI (HD version).per` + Promisory source corpus  
**Status:** STATIC DECONSTRUCTION — NOT runtime qualified

## Executive result

`control-goal` is a genuinely distributed coordination channel. It must not be treated as a simple strategic goal owned by the main controller.

The behavioral census identifies **480 rule sites across 3 source files**:

| Source | Sites |
|---|---:|
| `AI (HD version).per` | 452 |
| `init.per` | 17 |
| `interaction.per` | 11 |

The concentration in the flattened controller is high, but the existence of independent initialization and interaction consumers/producers makes this a cross-system interface.

## Static topology

```text
                 STRATEGIC / INITIAL STATE
                         │
                         ▼
                    control-goal
                    /    |     \
                   /     |      \
                  ▼      ▼       ▼
             controller  init  interaction
                  │        │       │
                  └────────┼───────┘
                           ▼
                    control decisions
                           │
                 ┌─────────┼─────────┐
                 ▼         ▼         ▼
              economy   military   cooperation
                           │
                           ▼
                      engine state
                           │
                           ▼
                      reconciliation
```

This graph expresses static coupling, not proven interpreter ordering.

## Why `control-goal` is dangerous to copy literally

Unlike a purely local parameter, the same numeric channel can be observed by rules belonging to different historical subsystems. A direct AEGIS translation would therefore risk recreating an implicit global control register.

The correct reconstruction question is:

> What semantic control states were historically multiplexed through this channel, and which of those states actually require persistent representation in AEGIS?

## Source roles

### `AI (HD version).per`

Dominant behavioral surface. It contains the main strategic/control decisions that read and mutate the channel.

### `init.per`

Initialization role. This demonstrates that control state can be established or conditioned before the main controller's steady-state behavior.

### `interaction.per`

Interaction/cooperation role. This is the strongest evidence that `control-goal` is not merely an internal strategy selector; external/inter-agent interaction logic participates in its state surface.

## Static ownership hypothesis

The channel appears to multiplex multiple concepts that should be separated in AEGIS:

```text
ControlGoal
   ├── strategic mode
   ├── coordination mode
   ├── interaction/cooperation state
   ├── execution-control disposition
   └── validity/generation
```

Do not freeze these as final names until exact writer/read-site semantics have been extracted.

## Required lifecycle analysis

For every writer site, determine whether the mutation means:

- initialize;
- enter mode;
- leave mode;
- suppress another behavior;
- enable another subsystem;
- coordinate with another actor;
- recover from failure;
- reset stale state;
- or merely store an intermediate calculation.

For every reader, identify whether it is:

- a guard;
- a mode selector;
- a suppression condition;
- an execution prerequisite;
- or an interaction response.

## AEGIS reconstruction rule

Do not create one global AEGIS integer equivalent to `control-goal`.

Instead, extract the semantic states and give each an explicit owner and lifecycle.

The historical numeric channel becomes evidence for behavior, not the AEGIS interface itself.

## Target-build boundary

Static extraction cannot prove:

- same-pass mutation visibility;
- exact rule scheduling;
- persistence across interpreter passes;
- whether interaction writes are immediately consumed;
- exact reset timing;
- command side effects associated with a given control state.

Those remain target-build runtime qualification items.

## Four-interface conclusion

The four originally selected distributed channels now have static graph documents:

```text
position-goal → spatial/topological coordination

enemy-goal    → enemy/target coordination

farm-goal     → economic/infrastructure feedback

control-goal  → distributed control/interaction coordination
```

This closes the first distributed-interface extraction set.

## Next phase

The next static pass should stop treating the four interfaces independently and **join them into one cross-system graph**. In particular:

```text
strategy-goal
    ↓
control-goal
    ↓
position-goal / enemy-goal
    ↓
farm-goal / unit-goal / attack-goal
    ↓
construction / production / military / economy
```

The objective is to identify feedback cycles, authority boundaries, and state that must be split when rehosted under AEGIS.

No runtime qualification is implied by this document.
