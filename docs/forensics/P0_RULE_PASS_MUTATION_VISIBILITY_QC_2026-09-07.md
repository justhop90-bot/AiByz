# P0 Rule-Pass Mutation Visibility QC — 2026-09-07

## Scope
Determine what can be established about AoE2DE `.per` rule-pass semantics: rule execution, mutation visibility, jump control flow, and the boundary between one pass and the next.

## Evidence base
- Untouched local stock AI corpus under `resources\\_common\\ai\\Promisory`.
- Direct corpus inspection of `up-jump-rule` usage across 22 `.per` files.
- Stock corpus contains extensive forward and backward relative jumps.
- Official AoE2DE update 61321 documents `AIDEBUGGING`/`AISCRIPTDEBUGGING`, including detection of infinite jump loops and display of the current script position plus goal/control-group/target state. This is strong engine-level evidence that the interpreter maintains a mutable script cursor and detects control-flow loops.
- Public AI scripting reference defines `up-jump-rule` as a jump forward or backward within the current rule set, and `up-modify-goal`, `up-modify-sn`, and related operations as state mutation actions.

## Established findings

### 1. A rule pass is an executing interpreter walk, not merely a declarative batch
`up-jump-rule` changes the interpreter's position within the rule set. Therefore source order and control-flow edges are execution semantics, not documentation decoration.

### 2. Rule actions are executed when their predicates are satisfied
The stock corpus contains rules whose actions mutate goals, strategic numbers, flags, escrow, timers, and other state and then immediately use jump control flow. This demonstrates that mutation and control flow are coupled within the same interpreter execution context.

### 3. Jump control can prevent otherwise adjacent rules from being evaluated
Stock uses patterns such as `up-jump-rule 1`, `up-jump-rule 2`, `up-jump-rule 4`, `up-jump-rule 11`, and much larger offsets. Therefore a satisfied rule can deliberately bypass subsequent rules. This is stronger than merely giving one rule a higher abstract priority.

### 4. Backward jumps create loops
The corpus contains negative relative jump offsets. Official tooling specifically added infinite-jump-loop diagnostics. Therefore a single pass cannot safely be modeled as a guaranteed single forward traversal of every rule.

### 5. State mutation can affect later eligibility, but exact intra-pass visibility timing is not proven by `.per` source alone
A subsequent rule that reads a goal/strategic number/flag after a previous rule writes it is evidence of intended same-execution dependency, but source inspection alone cannot establish whether the engine snapshots all facts at pass start, reads mutable state on each predicate evaluation, or has other caching boundaries. This distinction must not be guessed.

### 6. The engine explicitly exposes debugging state at the script cursor
Official AoE2DE documentation for Update 61321 states that `AIDEBUGGING` can show the current position of the script being parsed together with goal values, control groups, and target object/point when breakpoints or infinite jump loops trigger. This supports a cursor-based interpreter model and makes direct runtime probing feasible.

## Important negative findings

The following are NOT yet proven:

1. Exact definition of a `rule pass` in the DE interpreter.
2. Whether the interpreter restarts at rule 0 after every jump or continues from a mutable cursor.
3. Whether a rule that fires can be followed by another rule in the same update cycle after a forward jump/fall-through.
4. Whether goal/strategic-number/flag writes are immediately visible to the very next predicate evaluation without any caching.
5. Whether all rules are revisited until quiescence, or whether the engine imposes a bounded instruction/rule budget per update.
6. Exact behavior when a backward jump crosses a rule that has already fired in the same update.
7. Exact semantics of multiple simultaneous eligible rules without jumps.
8. Whether external engine state mutations caused by commands are observable to later predicates in the same AI interpreter invocation, versus only a later AI update.

## Strong inference that is safe for architecture

AEGIS should NOT rely on accidental same-pass propagation for correctness.

Use an explicit generation/cycle protocol:

```text
OBSERVE(G)
   ↓
DERIVE(G)
   ↓
DECIDE(G)
   ↓
AUTHORIZE(G)
   ↓
COMMAND(G)
   ↓
VERIFY(G+1 or later)
```

Within a cycle, modules may publish state, but consumers should be written so that stale-state rejection is explicit through generation IDs. This protects AEGIS from unknown interpreter caching/pass boundaries.

## Runtime experiment required to close the ABI question

A minimal diagnostic script should contain two adjacent rules:

```per
(defrule
    (true)
=>
    (set-goal TEST-A 1)
)

(defrule
    (goal TEST-A == 1)
=>
    (set-goal TEST-B 1)
)
```

A second experiment should add a forward jump over the observer rule. A third should add a backward jump with a bounded counter. The script should emit state using engine-supported debugging/logging facilities rather than chat output.

The tests must distinguish:

```text
same interpreter invocation
same AI update
later AI update
```

Only after these tests should AEGIS claim a precise cycle/transaction ABI.

## Engineering consequence

The correct AEGIS scheduler abstraction is presently:

```text
ENGINE UPDATE
    │
    ├── interpreter executes reachable rule graph
    │       ├── predicates read engine/AI state
    │       ├── actions mutate state
    │       └── jumps alter reachable control flow
    │
    └── next engine update / interpreter invocation
```

Do not implement a simulated "all rules evaluate once, then all writes commit" model. The stock corpus and official debugging facilities are inconsistent with treating `.per` as a pure declarative batch language.

## Qualification status

- Rule control-flow existence: HIGH confidence.
- Forward/backward jump behavior: HIGH confidence.
- Mutable script-cursor model: HIGH confidence.
- Same-pass state visibility: NOT ESTABLISHED.
- Fixed rule-pass boundaries: NOT ESTABLISHED.
- Quiescent repeated evaluation semantics: NOT ESTABLISHED.
- Exact command-side-effect visibility: NOT ESTABLISHED.

## Sources

Official AoE2DE Update 61321: AI scripting debugging support, including current script position and infinite jump-loop diagnostics.

Public AoE2 AI scripting reference: `up-jump-rule`, `up-modify-goal`, `up-modify-sn`, and related interpreter actions.

Local authoritative corpus: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\Promisory`.
