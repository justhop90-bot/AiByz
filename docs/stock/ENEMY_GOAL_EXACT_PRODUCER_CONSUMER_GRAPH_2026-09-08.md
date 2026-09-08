# `enemy-goal` Exact Static Producer/Consumer Graph — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Status:** STATIC DECONSTRUCTION; runtime semantics remain separately qualified

## Corpus result

The target-build flattened `AI (HD version).per` plus the complete 36-file Promisory source corpus contains **232 behavioral rule blocks** referencing `enemy-goal` across **8 behaviorally relevant source files**.

The behavioral footprint is:

| Source | Behavioral rule blocks |
|---|---:|
| `AI (HD version).per` | 181 |
| `interaction.per` | 18 |
| `general.per` | 10 |
| `init.per` | 8 |
| `units.per` | 6 |
| `buildings.per` | 4 |
| `tsa.per` | 3 |
| `threats.per` | 2 |

## Exact producer surface

The source contains a broad mutation surface: **36 behavioral writer sites** set or modify `enemy-goal`.

The writer distribution is dominated by the flattened controller, with additional writes in interaction, initialization, general, unit, building, military and threat services.

This is materially different from `position-goal`: `enemy-goal` is not primarily initialized once and then consumed. It is repeatedly re-established by different operating paths.

## Static role classification

The safest source-level interpretation is:

```text
enemy-goal = enemy/target coordination state
```

It is **not yet safe** to call it a pure enemy identity register.

Why:

1. multiple subsystems write it;
2. military and threat code consume it;
3. interaction/general paths also touch it;
4. the controller repeatedly mutates it;
5. source context shows it participating in target-selection and enemy-related decisions.

Therefore the historical channel appears to bridge **enemy identity, target context, and response policy**, depending on rule context.

## High-level topology

```text
                 enemy observation / policy
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
       enemy identity               target context
             │                           │
             └─────────────┬─────────────┘
                           ↓
                      enemy-goal
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       military         threats         interaction
          ↓                ↓                ↓
    composition       classification    cooperation
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                    downstream response
```

## Important distinction: enemy vs threat vs target

The extraction strongly supports keeping three concepts separate in AEGIS:

```text
EnemyIdentity
ThreatAssessment
TargetSelection
```

Historical `enemy-goal` can participate in the bridge between these concepts, but that does not justify collapsing them into one AEGIS variable.

For example, an observed enemy civilization/player is not equivalent to a current threat, and a threat is not necessarily the currently selected attack target.

## Producer classes

The 36 writers should be classified in the next machine extraction into these categories:

### Observation-derived

Rules that establish enemy context from player/object/scouting information.

### Strategic selection

Rules that select an enemy context as part of strategy or military posture.

### Target/reaction selection

Rules that establish an enemy context for a downstream action.

### Interaction/cooperation

Rules that modify enemy-related state because of communication/cooperation logic.

### Reset/replacement

Rules that clear or replace stale enemy context.

A single rule may belong to multiple classes.

## Consumer surface

The 232 behavioral blocks include **182 read sites** in the current static census, in addition to the writer/mixed blocks.

The major consumer domains are:

```text
scouting / observation
       ↓
threat assessment
       ↓
military target selection
       ↓
unit composition / production
       ↓
attack / defense

construction/building response
       ↓
fortification / defensive decisions

interaction / cooperation
       ↓
ally/enemy context
```

The exact rule-site edges remain the next machine extraction layer; the source distribution establishes the cross-system coupling but not every semantic edge.

## Reset and supersession

Unlike a simple static identity constant, `enemy-goal` has repeated mutation across operating paths. This makes **supersession analysis mandatory**.

The next extraction must identify whether a writer:

- replaces the current enemy context;
- clears it;
- changes it conditionally;
- writes a temporary selection;
- establishes a long-lived strategic choice.

A raw write count cannot distinguish these lifecycles.

## AEGIS implication

Do not allocate a single global `enemy-goal` integer in the AEGIS state ABI.

The preferred reconstruction boundary is:

```text
EnemyContext
 ├─ player identity
 ├─ observed confidence / freshness
 ├─ threat assessment reference
 ├─ target-selection reference
 ├─ source/generation
 └─ validity
```

Then expose typed views to military, construction, research and interaction services.

This preserves the historical coupling while preventing the historical ambiguity from becoming AEGIS architecture.

## Evidence boundary

**STATIC-QUALIFIED:** source distribution, behavioral rule count, broad writer/read surfaces and cross-system participation.

**TARGET-BUILD-UNKNOWN:** exact temporal ordering, whether a given mutation is visible to later rules in the same interpreter pass, persistence duration, precise sentinel semantics, and the runtime distinction between enemy identity and target context.

No runtime experiment was performed for this extraction.
