# P0 Rule Control-Flow and Jump ABI QC — 2026-09-07

## Scope

Authoritative local corpus: AoE2DE stock `resources\\_common\\ai\\Promisory` on Weebo.

This pass establishes the semantics and architectural significance of `up-jump-rule`, with emphasis on the execution graph used by `escrow.per`, `units.per`, `researches.per`, and `buildings.per`.

No live AEGIS runtime files were modified.

## Executive finding

`up-jump-rule` is a real control-flow primitive, not a scheduling hint. It moves execution forward or backward within the current rule set. Therefore stock AI behavior cannot be modeled as an unordered set of independent rules.

The effective program is a rule graph containing:

- ordinary sequential rule evaluation;
- forward skips for conditional suppression;
- backward jumps for loops/re-entry;
- rule-local state mutations that change later rule eligibility;
- explicit endpoint commands after precondition gates.

The rule graph itself is part of the AI's operational semantics.

## External ABI corroboration

The established AI scripting reference describes `up-jump-rule` as jumping forward or backward within the current rule set. Its examples explicitly use positive deltas to skip rules and negative deltas to loop. It also warns that `#load` blocks can make relative jump targets unreliable.

This corroborates the local stock corpus but is not being used as a substitute for local evidence.

## Local corpus scale

Direct local Python inspection counted `up-jump-rule` occurrences across the stock Promisory corpus:

- `escrow.per`: 181 active textual occurrences
- `units.per`: 237
- `researches.per`: 66
- `buildings.per`: 353
- `general.per`: 173
- `init.per`: 189
- `gatherers.per`: 124
- `tsa.per`: 235

Across the 36 `.per` files inspected, 22 contained the construct.

The stock AI therefore relies on jump-based control flow extensively; this is not an exceptional mechanism.

## Positive-jump semantics

A positive jump skips subsequent rules in the current rule set.

Local evidence in `researches.per` demonstrates the pattern:

```per
(defrule
    (goal strategy fast-imp)
    (unit-type-count-total villager < fi-vills)
=>
    (up-jump-rule 2))
```

This is followed by two rules belonging to the section being bypassed.

Another local example:

```per
(defrule
    (up-compare-goal total-food-amount >= 700)
    ...
=>
    (research feudal-age)
    ...
    (up-jump-rule 2))
```

The jump is therefore structural control flow: execute the selected branch, then bypass the next rule block rather than merely recording a priority.

## Negative-jump semantics

The scripting ABI also supports negative deltas. The stock corpus contains negative jumps in `researches.per`, `buildings.per`, `general.per`, `init.per`, and other files.

The external scripting reference gives the canonical loop form:

```per
(defrule
    (up-compare-goal gl-value < 3)
=>
    (up-modify-goal gl-value c:+ 1)
    (up-jump-rule -1)
)
```

Therefore the same primitive supports both branch suppression and repeated evaluation.

## Why this changes the scheduler model

A conventional scheduler model would be:

```text
RULE A
RULE B
RULE C
RULE D

all eligible rules compete for execution
```

Stock is closer to:

```text
        A
       / \
      /   \
     B     D
     |     |
     C     E
      \   /
       \ /
        F
```

A rule can alter whether later rules are even visited during the current pass.

Consequently, rule ordering and jump destinations are part of effective priority.

## Escrow-specific consequence

`escrow.per` is especially important because it separates request accumulation from execution.

The file begins with an unconditional release phase:

```per
(up-release-escrow)
(set-escrow-percentage wood 0)
(set-escrow-percentage food 0)
(set-escrow-percentage gold 0)
(set-escrow-percentage stone 0)
(up-modify-escrow wood c:= 0)
(up-modify-escrow food c:= 0)
(up-modify-escrow gold c:= 0)
(up-modify-escrow stone c:= 0)
```

Research execution is then selected by escrow flags:

```per
(up-compare-flag escrow-flag == 1)
(can-research-with-escrow castle-age)
=>
(research castle-age)
```

The same pattern is repeated for many research technologies.

Later in the same file, request rules add costs and set bit flags. The final materialization stage writes the accumulated costs into native escrow:

```per
(up-modify-escrow wood g:= cost-wood)
(up-modify-escrow food g:= cost-food)
(up-modify-escrow gold g:= cost-gold)
(up-modify-escrow stone g:= cost-stone)
```

This confirms a two-phase structure:

```text
REQUEST / ACCUMULATE
        ↓
ESCROW MATERIALIZATION
        ↓
CAN-* WITH ESCROW
        ↓
PHYSICAL EXECUTION
```

## Units-specific consequence

`units.per` contains endpoint staging rules such as:

```per
(goal trainarcher yes)
(goal temporary-goal 1579175)
(up-can-train 0 c: archer-line)
=>
(up-full-reset-search)
(up-find-local c: archery-range c: 240)
...
(up-target-point 0 action-train c: archer-line)
(set-goal temporary-goal3 1579193)
```

A later rule validates the staged state and executes:

```per
(goal trainarcher yes)
(nand (goal temporary-goal3 1579193)
      (up-compare-goal local-total >= 1))
(goal siegereq yes)
(can-train archer-line)
=>
(train archer-line)
```

This is not a single atomic `train` decision. It is a staged execution pipeline:

```text
production intent
 → endpoint capability
 → endpoint search
 → target staging
 → staged-state confirmation
 → global authorization
 → physical train
```

## `siegereq` is a coordination gate, not a universal priority queue

Multiple production endpoints use `goal siegereq yes` before issuing physical commands.

This establishes a cross-cutting authorization gate, but the corpus does not support treating it as a complete global scheduler.

It coexists with:

- individual train goals;
- endpoint-specific `up-can-train` checks;
- local building searches;
- resource affordability;
- escrow flags;
- suppression rules;
- strategic-number state;
- jump-based control flow.

Therefore `siegereq` should be modeled as an execution authorization state, not as proof of a centralized queue.

## Relative jump fragility

The external scripting reference explicitly warns that relative `up-jump-rule` targets can be invalidated by inserted `#load` blocks.

This has direct implications for AEGIS:

1. Relative jumps should be minimized in newly written AEGIS code.
2. AEGIS modules should avoid control flow whose correctness depends on distant rule counts.
3. Module boundaries should be stable.
4. Any unavoidable relative jump requires a local proof that its target remains stable.
5. AEGIS should prefer explicit state machines and direct rule-local transitions over long relative-jump chains.

## Important negative findings

This pass does NOT establish:

- exact engine micro-order between every eligible rule;
- whether every rule is evaluated exactly once per outer interpreter pass;
- whether a rule that mutates state can immediately cause another rule to fire in the same internal pass in every case;
- a universal runtime cost model for backward jumps;
- a centralized stock scheduler;
- deterministic priority independent of rule order.

Those require runtime instrumentation or a validated engine ABI test harness.

## AEGIS architectural prescription

The correct AEGIS control model is:

```text
STRATEGIC STATE
      ↓
DEMANDS
      ↓
ARBITRATION
      ↓
RESERVATION / ESCROW
      ↓
EXECUTION AUTHORIZATION
      ↓
ENDPOINT STAGING
      ↓
PHYSICAL COMMAND
      ↓
VERIFICATION
      ↓
RECOVERY
```

The AEGIS scheduler must therefore be an explicit state machine rather than an accidental consequence of source-file rule ordering.

Rule ordering remains relevant because the AoE2 interpreter still executes `.per` rules, but strategic priority should be represented explicitly in AEGIS state instead of relying on opaque relative jumps.

## Qualification status

Static confidence: HIGH for `up-jump-rule` being a forward/backward rule-control primitive and for its extensive use in the stock corpus.

Runtime confidence: NOT ESTABLISHED for exact same-pass micro-order and engine scheduling behavior.

Implementation status: NO LIVE AEGIS CHANGE.

## Source references

Primary evidence: untouched local stock corpus on Weebo, especially `Promisory/escrow.per`, `Promisory/units.per`, `Promisory/researches.per`, and `Promisory/buildings.per`.

Secondary ABI corroboration: AoE2 AI scripting reference describing `up-jump-rule` as forward/backward control flow and warning about relative targets around `#load` blocks.
