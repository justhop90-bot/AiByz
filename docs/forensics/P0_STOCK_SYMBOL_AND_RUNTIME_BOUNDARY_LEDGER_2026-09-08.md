# P0 Stock Symbol / Runtime Boundary Ledger — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Purpose:** Record the exact boundary established during the stock-system reconstruction pass and prevent future architectural regressions.

## Runtime boundary

The stock `AI (HD version).per` begins by loading:

```per
(load "Promisory\\defaultConstants")
(load "Promisory\\finalingConstants")
```

and reaches a conditional:

```per
#else
(load "Promisory\\finaling")
#end-if
```

Therefore `finaling` must be treated as part of the source's conditional compilation structure, not assumed to be an unconditional import in every possible build context.

## Authoritative ABI namespaces

`defaultConstants.per` defines the core FactId namespace, including:

- game-time = 0
- population-cap = 1
- population-headroom = 2
- housing-headroom = 3
- food/wood/stone/gold amounts = 5/6/7/8
- escrow-amount = 9
- dropsite-min-distance = 12
- soldier/attack/defend counts = 13/14/15
- warboat counts = 16/17/18
- current-age = 19
- civilization = 21
- player-number = 22
- player-in-game = 23
- unit-count = 24
- unit-type-count = 25
- unit-type-count-total = 26
- building-count = 27
- building-type-count = 28
- building-type-count-total = 29
- population = 30
- military-population = 31
- civilian-population = 32
- random-number = 33
- resource-amount = 34
- player-distance = 35
- allied-goal/allied-sn = 36/37
- resource-percent = 38
- enemy/building/unit town facts = 39–46
- Gaia facts = 47–49
- current-age-time = 50
- timer-status = 51
- tribute/treaty/battle-royale facts = 52–55

It also defines object classes, foundations, research states and timer states.

## Object-data namespace

`finalingConstants.per` defines object-data fields from ID 0 through at least 84. Important fields include identity, type/class, action/order, target, coordinates, HP, range/speed, dropsite/resource/carry, garrison, status, player, attack stance, action time, target ID, formation, task count, attacker state, progress, distance, map-zone, idling, movement, reload/attack timing, training, research, gather type, language, group flags, hero flags, base/upgrade type, ownership and capture flags.

These fields provide the raw observation capability needed for AEGIS worker, construction, scouting and military state reconciliation.

## Stock lifecycle identifiers already established

The existing forensic corpus has established the following semantic distinctions:

```text
policy/authorization
    != feasibility
    != command
    != pending
    != completion
    != verified outcome
```

Examples:

```text
trainvillager
up-can-train escrow-state villager
up-train escrow-state villager
pending villager
civilian-population
```

Likewise:

```text
resource demand
    != worker-role target
    != source selection
    != task assignment
    != productive outcome
```

and:

```text
construction request
    != placement
    != foundation
    != builder assignment
    != completion
```

## Active versus provenance-only source files

The target Promisory directory contains 37 files. The presence of a file does not establish runtime loading.

Directly evidenced active nested imports:

```text
buildings.per -> extremebuildings2.per
gatherers.per -> ugp.per
```

Commented imports such as those in `init.per` and `merge.per` are provenance only until an active load path is demonstrated.

Experimental/compatibility source includes `merge1b`, `merge2`, `merge2b`, `merge3`, `merge3b`, `merge4`, `paphosConstants`, `event`, and `events`. Their presence does not make them ordinary Byzantine runtime dependencies.

## Finaling semantics

Direct inspection demonstrates that `finaling.per` performs real behavior, including:

- exploration-group configuration;
- idle-unit thresholds;
- enemy-sighted response configuration;
- wall targeting;
- escrow percentage setup;
- population-cap retrieval;
- attack/capture flag clearing;
- naval filtering;
- direct production rules;
- jump-based flow control;
- maintenance timers;
- rule-pass timing state;
- AI turn-time estimation;
- resignation handling;
- post-resignation cleanup;
- unit reset behavior.

Therefore finaling is a runtime-supervision subsystem, not cosmetic tail code.

## Reconstruction rule

The final AEGIS implementation must:

1. preserve the engine ABI semantics that are actually required;
2. preserve behavioral contracts demonstrated by stock AI;
3. explicitly reimplement ownership under AEGIS;
4. avoid Promisory runtime imports;
5. retain experimental source only when a concrete dependency or desired feature is established;
6. never infer runtime dependency from directory membership or commented historical loads.

## Current evidence status

| Claim | Status |
|---|---|
| AI(HD) is the main flattened behavioral body | OBSERVED |
| defaultConstants is runtime-loaded by AI(HD) | OBSERVED |
| finalingConstants is runtime-loaded by AI(HD) | OBSERVED |
| finaling is conditional-source loaded by AI(HD) | OBSERVED |
| finaling contains runtime behavior | OBSERVED |
| buildings imports extremebuildings2 in its source | OBSERVED |
| gatherers imports ugp in its source | OBSERVED |
| merge/init historical loads are active runtime dependencies | REJECTED / NOT OBSERVED |
| experimental merge/paphos files are ordinary Byzantine runtime dependencies | NOT OBSERVED |
| every flattened AI region has exact source-file correspondence | UNQUALIFIED |
| complete goal/SN/action reader-writer closure | UNQUALIFIED |
| AEGIS runtime equivalence | UNQUALIFIED |

**Boundary:** static source reconstruction is now sufficiently established to begin subsystem-specific reconstruction. Further progress should come from targeted subsystem passes, not another generic inventory pass.
