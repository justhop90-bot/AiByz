# R2/R4 Semantic Mutation Argument + Rule-Scope Join — 2026-09-09

## Scope
Full HD/Promisory archaeology corpus: `AI (HD version).per` plus every `.per` under `Promisory` (37 files). The four-file effective runtime closure remains a separate load-status question.

## Method
Deterministic line-aware lexical scan. Comments are stripped with string-literal awareness. Recognized mutation heads: `set-goal`, `up-modify-goal`, `set-strategic-number`, `up-modify-sn`, `enable-timer`, `disable-timer`, `up-set-timer`, `up-modify-flag`, `up-modify-group-flag`. Each mutation is joined to its enclosing `defrule`, source line, exact target argument, RHS arguments, and rule condition text. No engine semantics, execution frequency, ownership, or runtime activation are inferred.

## Machine totals
- Corpus files: **37**
- Recognized mutation rows: **14,000**
- Mutation heads: GOAL 8,633; SN 4,310; TIMER 779; FLAG 221; GROUP_FLAG 57
- Unique source files containing recognized mutations: **22**
- Unique enclosing rules: **6,182**
- Every recognized mutation row joined to an enclosing rule and non-empty condition scope.
- Counts agree with the previously established 14,000-row semantic mutation census.

## Key channel joins

### `sn-cavalry-threat`
- 9 mutation rows, all in `AI (HD version).per`.
- Reset: line 5167 → `0`, rule beginning line 5161, condition `(true)`.
- Threshold writes: 6927→1, 6939→2, 6951→3, 6963→4.
- Additional contextual writes: 7006→1, 7016→2, 7031→1, 7045→1.
- The first threshold family is driven by enemy cavalry-line counts including magyar-huszar, boyar, knight, scout-cavalry, tarkan, war-elephant, camel, and cataphract lines.
- Later writes add time, stable, strategy, military-population, civilization, and age conditions.
- Static writer graph is therefore now rule-scoped; execution frequency and lifetime remain runtime-sensitive.

### `retreat-now-goal`
- 13 mutation rows, all in `AI (HD version).per`.
- Active writes include escalation to `1` and reset to `0`.
- Retreat writers are conditioned by attack coordination, age, tower/TC/castle-arrow threats, siege availability, military level, population, monk threat, timers, and victory-time / town-size conditions.
- No commented mutation is counted as an active writer.

### `attack-status-goal`
- 19 mutation rows, all in `AI (HD version).per`.
- Values observed include `retreat`, `tsa`, `groups`, and `0`.
- Writers are coupled to retreat state, attack-group state, timers, target-player state, town-size constraints, victory-time, wonder/relic conditions, and military readiness.

### `restart-attack-goal`
- 3 mutation rows, all in `AI (HD version).per`.
- Activation begins when `increase-town-size-goal` is `2` and maximum town size reaches `40` or more.
- Reset conditions include ally-proximity, attack-group count/minimum size, and maximum-town-size constraints.

### `cavarchers`
- 11 mutation rows in the full corpus, all historical Promisory source.
- Initialization: `Promisory/init.per:183` → `0`.
- Ten historical writers are in `Promisory/threats.per:624–655`, using `up-modify-sn` from `temporary-goal`.
- Exact search of the active four-file closure found zero occurrences.
- Disposition: **historical source state; not active in the four-file runtime closure**.

### `temporary-goal2`
- 408 mutation rows in the full corpus.
- It is a heavily reused historical scratch channel across Promisory subsystems.
- In the active four-file closure, the only occurrence is the commented source text at `AI (HD version).per:5806`; live code around it uses `math-goal` / `math-goal2`.
- Disposition: **historical/commented in active closure; not established as live stock runtime state**.

## R2/R4 consequence
The join closes the next static dimension: **mutation target → exact rule → condition scope → RHS/action context**. This is stronger than lexical occurrence evidence but still does not prove execution, ownership, scheduler frequency, or engine semantics.

The next ledger step is to join these rule-scoped mutations against declaration, initializer, reset/reinitializer, readers, and load-status evidence for each state channel. Owner and lifetime dispositions remain evidence-graded rather than inferred from writer count.

## Boundaries
1. Source mutation proves a textual mutation site, not that the rule executes.
2. A reset-like writer is not automatically a one-time initializer.
3. Full-corpus presence does not establish active retail load.
4. Historical channels remain distinct from the active four-file runtime closure.
5. Numeric allocation remains blocked by R3 until typing, collision, load, ownership, validator/compiler, and runtime gates close.
