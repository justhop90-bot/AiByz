# P0 Research → Capability Change Lifecycle Closure — 2026-09-08

## Scope

This pass establishes the stock research lifecycle from the installed AoE2DE target corpus for build 101.103.48987.0 / BuildID 24094652, with primary evidence from `Promisory/researches.per`.

Status: **STATIC ARCHITECTURAL CLOSURE**. Runtime equivalence is not claimed.

## Core finding

Stock research is not a single boolean transition. The observable architecture separates at least four concepts:

```text
research availability
        ↓
policy authorization
        ↓
engine research command
        ↓
observed capability/state change
        ↓
consumer re-evaluation
```

The stock corpus also uses research state as an input to unrelated policy systems, proving that research completion is a cross-subsystem state transition rather than merely a terminal command.

## Evidence: age advancement

`researches.per` lines 50–91 contains multiple Feudal Age authorization paths. The command is guarded by `can-research feudal-age`, then executes `research feudal-age`, mutates `sn-current-age`, enables boar hunting, and changes maximum town size. Different policy branches use food totals, villager population, flank state, enemy age, strategy, strategy type, pending villagers, and timers.

Representative stock sequence:

```text
policy conditions
 → can-research feudal-age
 → research feudal-age
 → sn-enable-boar-hunting := 1
 → sn-current-age := dfeudal
 → maximum-town-size adjustment
```

Critically, the source does not establish that the `research` action itself proves completion at the same evaluation instant.

## Evidence: Castle / Imperial

The stock file directly uses:

```text
(can-research castle-age)
=>
(research castle-age)
...
(set-strategic-number sn-current-age fcastlea)
```

and later:

```text
(can-research imperial-age)
=>
(research imperial-age)
...
(set-strategic-number sn-current-age imperial)
```

Therefore `sn-current-age` is an AI strategic representation coupled to the research decision path. It must not automatically be treated as an independent engine-authoritative completion sensor without runtime qualification.

## Evidence: research state is consumed elsewhere

The installed corpus contains extensive uses of `research-available`, `research-pending`, and `research-complete` across `dawn.per`, `boarhunting.per`, `interaction.per`, `general.per`, `orb.per`, `extremebuildings2.per`, and other services.

Examples include:

- `research-complete` gating construction/economic behavior.
- `research-pending` gating technology-dependent military decisions.
- `research-available` participating in affordability/admission decisions.
- `up-research-status` being used to inspect technology state.

This establishes a downstream capability-consumer graph:

```text
Research state
   ↓
Economy / Construction / Military / Interaction / Scouting services
```

## Evidence: technology can be conditional on observed force state

The stock unique-upgrade section uses conditions such as:

```text
(goal uugoal yes)
(can-research my-unique-unit-upgrade)
=>
(research my-unique-unit-upgrade)
```

and also derives `uugoal` from physical unit counts and strategic conditions. Thus research authorization can depend on already-observed capability state while the resulting technology subsequently changes the available capability set.

## Evidence: research affects military demand

The stock corpus contains research-gated military decisions, including attack/retreat and composition logic. `interaction.per` also uses research state when deciding which military coordination messages and unit recommendations are valid.

This creates a feedback relationship:

```text
Military state / strategic demand
        ↓
Research authorization
        ↓
Technology completion
        ↓
New military capability
        ↓
Composition / posture re-evaluation
```

## Canonical AEGIS lifecycle

The research subsystem should therefore be modeled as:

```text
DEMANDED
   ↓
ELIGIBLE
   ↓
AUTHORIZED
   ↓
ISSUED
   ↓
PENDING
   ↓
COMPLETED / OBSERVED
   ↓
CAPABILITY RECONCILED
   ↓
CONSUMERS INVALIDATED / RE-EVALUATED
```

Terminal/error states:

```text
FAILED + CLASSIFIED
SUPERSEDED
EXPIRED
INVALIDATED
```

## Important separation

These must remain distinct:

```text
can-research X
      ≠
research X
      ≠
research-pending X
      ≠
research-complete X
      ≠
capability physically observed
```

Likewise:

```text
sn-current-age
      ≠
independent proof of engine completion
```

unless runtime qualification demonstrates equivalence for the target build and specific transition.

## Cross-system capability propagation

A completed technology should invalidate or re-evaluate dependent consumers. AEGIS should not require every subsystem to rediscover technology state independently.

Target topology:

```text
                 RESEARCH OS
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
       Economy   Construction  Military
          │          │          │
          └──────────┼──────────┘
                     ↓
              Strategy / Demand
```

Research OS owns technology lifecycle state. Consumers own their response to capability changes.

## Runtime gaps

Not established statically:

1. Exact timing between `research X` and `research-pending` / `research-complete` visibility.
2. Whether `research X` is an admission command, immediate state mutation, or both at a given evaluation boundary.
3. Exact lifetime and identity semantics of pending research.
4. Whether multiple research endpoints can be simultaneously pending and how stock arbitration behaves.
5. Whether `up-research-status` is equivalent to the engine's authoritative research state at every scheduling point.
6. Whether `sn-current-age` is guaranteed to remain synchronized with actual age state after interruptions or unusual game conditions.
7. Exact failure/retry semantics for a research command that is no longer admissible after the rule fires.
8. Exact consumer invalidation timing after completion.

These are runtime-qualification targets, not reasons to invent semantics.

## Engineering decision

**Research/capability lifecycle is now statically closed at the architectural contract level.**

No research implementation should yet be promoted into the production AEGIS root solely from this evidence.

The next P0 layer is the common **Verification & Recovery / Reconciliation OS**, which must unify civilian production, construction, military response, and research into one evidence-driven lifecycle model without confusing commands, pending state, strategic mirrors, and physical completion.
