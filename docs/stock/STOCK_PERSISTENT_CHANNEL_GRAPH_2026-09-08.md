# Stock Persistent Channel Graph — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Corpus:** restored target-build `AI (HD version).per` + Promisory source corpus
**Status:** STATIC DECONSTRUCTION — NOT runtime qualified

## Purpose

This document is the first semantic join above the rule-site census. It separates channels by likely control role and identifies the source surfaces that must be traced before AEGIS ownership contracts are frozen.

The underlying extraction is lexical. A high read/write count does not by itself prove semantic ownership or interpreter scheduling.

## Channel graph

| Channel | Primary source surface | Coupling | Static role hypothesis | Required downstream join |
|---|---|---:|---|---|
| `strategy-goal` | `AI (HD version).per` | 1 source / 710 sites | Strategic intent / strategy state | strategy transitions → demand → economy/military/production |
| `unit-goal` | `AI (HD version).per` | 1 / 928 | Unit demand/composition state | unit policy → production authorization → engine queue |
| `control-goal` | AI + `init.per` + `interaction.per` | 3 / 480 | Cross-system control/cooperation state | control mutation → affected service → reconciliation |
| `position-goal` | AI + 10 Promisory services | 11 / 370 | Spatial coordination / location state | position producer → object/search consumer → engine action |
| `enemy-goal` | AI + 7 Promisory services | 8 / 232 | Enemy identity/target coordination | enemy observation → target selection → military/building response |
| `attack-goal` | AI + `init.per` | 2 / 137 | Attack demand/state | attack policy → target/group → execution → retreat/restart |
| `ranged-unit-type-goal` | `AI (HD version).per` | 1 / 272 | Composition/unit-type selection | composition policy → production |
| `increase-town-size-goal` | `AI (HD version).per` | 1 / 194 | Infrastructure/population expansion | housing/town-size policy → construction |
| `farm-goal` | buildings + AI + init + researches | 4 / 99 | Food infrastructure demand | farm demand → placement/builders → economy |
| `housing-goal` | `AI (HD version).per` | 1 / 17 | Housing demand | housing policy → construction |
| `under-attack-goal` | `AI (HD version).per` | 1 / 44 | Threat/defensive state | threat detection → defense/retreat/recovery |
| `retreat-now-goal` | `AI (HD version).per` | 1 / 16 | Immediate retreat disposition | military execution → recovery/restart |
| `restart-attack-goal` | `AI (HD version).per` | 1 / 3 | Attack restart transition | retreat/recovery → re-engagement |
| `anti-cavalry-threat-goal` | `AI (HD version).per` | 1 / 53 | Threat signal | enemy composition → military composition |
| `forward-threat-goal` | `AI (HD version).per` | 1 / 15 | Forward-position threat signal | spatial/threat state → defense/attack |
| `monk-threat-goal` | `AI (HD version).per` | 1 / 37 | Monk threat signal | enemy observation → counter-unit/reaction |
| `enemy-fortifications-goal` | `AI (HD version).per` | 1 / 17 | Fortification threat signal | target observation → siege/attack response |
| `escrow-purpose-goal` | `AI (HD version).per` | 1 / 35 | Economic reservation purpose | demand → reservation → authorization |

## High-value graph A: strategy to execution

```text
strategy-goal
    ↓
unit-goal / ranged-unit-type-goal
    ↓
production policy
    ↓
engine authorization / queue
    ↓
object and population state
    ↓
military state
    ↓
attack-goal
```

This is a reconstruction hypothesis grounded in the observed channel populations. Exact rule-level edges are the next extraction target.

## High-value graph B: spatial state

```text
position-goal
    ↓
position/object/search services
    ↓
endpoint selection
    ↓
construction / worker / military consumer
    ↓
engine-facing action
    ↓
observed object state
```

The 11-source spread makes `position-goal` a particularly important interface candidate. It must not be copied as a single global variable into AEGIS without scoping.

## High-value graph C: enemy state

```text
enemy-goal
    ↓
scouting / object / military / research consumers
    ↓
threat classification
    ↓
composition / defense / target policy
    ↓
attack or construction response
```

The source spread means enemy identity and enemy threat must remain separate concepts in the AEGIS architecture even if the historical controller sometimes uses one channel as an intermediary.

## High-value graph D: infrastructure demand

```text
increase-town-size-goal
        ↓
housing-goal / farm-goal / construction demand
        ↓
placement
        ↓
builder assignment
        ↓
foundation / pending object
        ↓
completed infrastructure
        ↓
worker/economic state
```

This graph is especially important because it demonstrates the coupling between strategic population pressure, construction, and economic capacity.

## Scratch-state boundary

The graph deliberately excludes `temporary-goal*` from semantic ownership. The full census shows these registers cross many modules and are reused for unrelated calculations. AEGIS should use scoped temporary computation instead of reproducing these shared scratch registers as global semantic state.

## Ownership rule for AEGIS reconstruction

No channel is promoted into the final AEGIS ABI merely because it is frequent in stock.

Promotion requires:

1. identified producer;
2. identified consumers;
3. reset/supersession behavior;
4. lifecycle semantics;
5. valid value domain;
6. collision analysis;
7. target-build evidence status;
8. explicit AEGIS owner.

## Next extraction

The next static pass should populate exact rule-site edges for the four genuinely distributed channels first:

1. `control-goal`
2. `position-goal`
3. `enemy-goal`
4. `farm-goal`

For each site, capture activation predicate, state mutation, engine-facing action, downstream consumer, and reset/supersession path.

No runtime qualification is implied by this document.
