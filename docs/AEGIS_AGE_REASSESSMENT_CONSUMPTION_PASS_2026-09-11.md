# AEGIS Age Transition REASSESS Consumption Pass — 2026-09-11

## Status

**IMPLEMENTED at source-contract level.**

This pass implements the downstream consumer for the Age Transition vertical's terminal REASSESS event without allowing REASSESS to manufacture a new lifecycle generation, authorize another research command, or select a strategy.

## 1. Correct consumer owner

The Age Transition publisher is `AEGIS-research-age-v0.per` and owns REASSESS publication goals `766–767`.

The correct downstream consumer is `AEGIS-civilization-state-v0.per` because Civilization State owns the next authoritative civilization snapshot derived from the World Model.

New consumer goals:

- `780` — `aegis-cs-age-reassess-generation`
- `781` — `aegis-cs-age-reassess-valid`

These are registered in the repository-wide namespace map.

## 2. Normative consumer contract

The consumer requires all of the following:

1. Age Transition has published `reassess-valid = 1`.
2. The published reassessment generation equals the Age Transition lifecycle generation.
3. The Age Transition lifecycle generation equals the current Civilization State generation.
4. The consumer has not already acknowledged that generation.

On acknowledgement it:

- records the exact Age Transition generation;
- sets the local acknowledgement bit;
- consumes the Age Transition publication token.

It does **not** increment or manufacture any generation.

## 3. Stale-outcome protection

The critical protection is:

```text
RA reassess generation
        ==
RA lifecycle generation
        ==
current Civilization State generation
```

This is stronger than merely checking that an RA token exists. If a newer World Model snapshot has already replaced the Civilization State frame, a delayed Age Transition token no longer matches the current lifecycle frame and therefore cannot be acknowledged as if it belonged to the current state.

This prevents:

```text
old RA terminal event
→ newer World Model snapshot
→ stale RA acknowledgement
→ false current-cycle reassessment
```

## 4. Generation ownership

Civilization State continues to acquire its generation only from a fresh valid World Model generation:

```text
World Model N
    ↓
Civilization State N
```

REASSESS does not alter that relationship.

A later lifecycle therefore requires another World Model snapshot rather than:

```text
RA REASSESS N
→ CS N+1
```

which is forbidden.

## 5. Evidence preservation

Age Transition's terminal confirmation remains based on engine-facing `current-age >= castle-age`, not command issuance.

The reassessment consumer does not reinterpret this as causal success and does not set `aegis-ra-causal-evidence`.

Therefore:

```text
observed age transition
≠
causal proof that this particular research request caused it
```

## 6. Independent Age Transition blocker discovered

The REASSESS boundary is now implemented, but the Age Transition vertical has a separate authoritative-observation problem.

`AEGIS-foundation.per` currently initializes:

```text
(set-goal aegis-wm-age 0)
```

rather than acquiring an engine-facing current-age fact. Civilization State then copies `aegis-wm-age` from the World Model.

Therefore `aegis-cs-age` is not currently authoritative evidence of the actual engine age.

This pass deliberately does **not** silently repair that problem. Doing so would conflate reassessment implementation with an independent World Model evidence correction.

The authoritative completion observation already exists directly inside the Age Transition module through:

```text
(current-age >= castle-age)
```

but the shared World Model age field remains unqualified.

## 7. No central controller

No monolithic reassessment controller was introduced.

Ownership remains distributed:

```text
Age Transition
    → publishes REASSESS

Civilization State
    → acknowledges exact terminal generation

World Model
    → creates next observation generation

Civilization State
    → consumes that new observation
```

## 8. Validation coverage

Static source-contract tests cover:

- consumer namespace `780–781`;
- exact RA reassessment identity;
- exact lifecycle-generation matching;
- one-shot publication consumption;
- no generation creation by REASSESS;
- World Model ownership of the next generation;
- RA publisher identity;
- causal evidence remaining fail-closed;
- World Model age authority remaining explicitly unpromoted;
- absence of a central strategy controller.

These are source-contract tests only. No target-build runtime qualification is claimed.

## 9. Final disposition

| Gate | Result |
|---|---|
| REASSESS publisher | PASS |
| Correct downstream consumer | PASS |
| Exact generation identity | PASS |
| Stale terminal protection | PASS |
| One-shot token consumption | PASS |
| New generation ownership | PASS |
| Duplicate physical authorization | PASS / unchanged |
| Causal evidence preservation | PASS |
| Central-controller avoidance | PASS |
| Engine-authoritative shared age observation | **BLOCKED** |
| Target-build runtime qualification | **NOT EXECUTED** |

The Age Transition REASSESS consumption boundary is therefore **implemented and structurally audited**, while the independent World Model age-authority defect remains explicitly unresolved.
