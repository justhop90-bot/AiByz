# P0 Rule-Pass Mutation Visibility QC — 2026-09-07

## Scope
Determine what can be established about AoE2DE `.per` rule-pass semantics: rule execution, mutation visibility, jump control flow, and the boundary between one pass and the next.

## Evidence base
- Untouched local stock AI corpus under `resources\\_common\\ai\\Promisory`.
- Direct corpus inspection of `up-jump-rule` usage across 22 `.per` files.
- Stock corpus contains extensive forward and backward relative jumps.
- Official AoE2DE Update 61321 documents `AIDEBUGGING`/`AISCRIPTDEBUGGING`, including detection of infinite jump loops and display of the current script position plus goal/control-group/target state.
- Public AoE2 AI scripting references define `up-jump-rule`, `up-modify-goal`, `up-modify-sn`, `set-goal`, `set-strategic-number`, `disable-self`, and `up-log-data`.
- UserPatch release notes provide historical semantic notes for extended goals/timers, immediate strategic-number effects in some commands, and escrow state.

## Cross-reference result
The external corpus materially strengthens the ABI interpretation, but does **not** close the exact same-pass mutation question.

### Confirmed externally
1. `up-jump-rule` is documented as jumping forward or backward within the current rule set.
2. `up-log-data` is documented as an AI logging action, giving us a better candidate observation mechanism than chat output for runtime probes.
3. `set-goal` and `set-strategic-number` are documented as state mutation actions.
4. `disable-self` is documented as disabling the current rule so it will not run again.
5. `up-get-rule-id` exists and returns the zero-based ID of the current rule, providing a useful runtime control-flow probe.
6. Official DE tooling explicitly exposes the current script position and detects infinite jump loops, confirming that control-flow state is observable inside the interpreter.
7. Historical UserPatch notes explicitly document that some strategic-number changes “take effect immediately in rules,” demonstrating that at least some AI-state mutations have defined immediate visibility semantics in the engine. This is important evidence, but it must not be generalized to every goal, fact, timer, or engine-derived state.

### Still unproven
1. Whether ordinary `set-goal` writes are immediately visible to the next predicate in the same interpreter traversal.
2. Whether `up-modify-goal` has the same visibility boundary as `set-goal`.
3. Whether strategic-number writes are uniformly immediate across all consumers, despite historical documentation for specific S/N behavior.
4. Whether timer state and engine object state have the same visibility boundary as AI variables.
5. Exact start/end definition of an AI rule pass in current DE.
6. Exact behavior of backward jumps after a rule has already fired.
7. Exact ordering when multiple adjacent rules are simultaneously eligible and no jump is taken.
8. Exact command-side-effect visibility inside the same interpreter invocation.

## Established findings

### 1. A rule pass is an executing interpreter walk, not merely a declarative batch
`up-jump-rule` changes the interpreter's position within the rule set. Therefore source order and control-flow edges are execution semantics.

### 2. Rule actions are executed when their predicates are satisfied
The stock corpus contains rules whose actions mutate goals, strategic numbers, flags, escrow, timers, and other state and then immediately use jump control flow. This demonstrates that mutation and control flow are coupled within the same interpreter execution context.

### 3. Jump control can prevent otherwise adjacent rules from being evaluated
Stock uses patterns such as `up-jump-rule 1`, `up-jump-rule 2`, `up-jump-rule 4`, `up-jump-rule 11`, and larger offsets. A satisfied rule can deliberately bypass subsequent rules.

### 4. Backward jumps create loops
The corpus contains negative relative jump offsets. Official tooling specifically added infinite-jump-loop diagnostics. Therefore a pass cannot safely be modeled as a guaranteed single forward traversal of every rule.

### 5. Mutation can affect later eligibility, but exact intra-pass visibility timing is not proven globally
The external references establish that mutation commands exist and that at least some strategic-number changes are documented as taking effect immediately in rules. However, this does not establish a universal immediate-visibility contract for every mutable state category.

### 6. The engine exposes debugging state at the script cursor
Official AoE2DE documentation for Update 61321 states that `AIDEBUGGING` can show the current position of the script being parsed together with goal values, control groups, and target object/point when breakpoints or infinite jump loops trigger.

### 7. Logging can be used as an observation channel
The public scripting reference documents `up-log-data` as an action that writes formatted text to `aoelog.txt`. This is now the preferred candidate for controlled runtime observations, subject to verifying current DE behavior.

## Important negative findings

The following are NOT yet proven:

1. Exact definition of a `rule pass` in the DE interpreter.
2. Whether the interpreter restarts at rule 0 after every jump or continues from a mutable cursor.
3. Whether a rule that fires can be followed by another rule in the same update cycle after a forward jump/fall-through.
4. Whether goal writes are immediately visible to the very next predicate evaluation without caching.
5. Whether all rules are revisited until quiescence, or whether the engine imposes a bounded instruction/rule budget per update.
6. Exact behavior when a backward jump crosses a rule that has already fired in the same update.
7. Exact semantics of multiple simultaneously eligible rules without jumps.
8. Whether external engine state mutations caused by commands are observable to later predicates in the same AI interpreter invocation.

## Strong inference safe for architecture

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

## Runtime experiment required

The minimal diagnostic suite should now use both `up-log-data` and official AIDEBUGGING facilities where available.

Test matrix:

```text
A. set-goal → immediate goal read
B. up-modify-goal → immediate goal read
C. set-strategic-number → immediate SN read
D. mutation → forward jump → read
E. mutation → fall-through → read
F. bounded backward jump → mutation/read sequence
G. command → engine-state predicate in same invocation
H. command → state predicate on next update
```

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

Do not implement a simulated “all rules evaluate once, then all writes commit” model.

## Qualification status

- Rule control-flow existence: HIGH confidence.
- Forward/backward jump behavior: HIGH confidence.
- Mutable script-cursor model: HIGH confidence.
- Mutation commands and state model: HIGH confidence.
- Some documented immediate SN effects: HIGH confidence for documented cases.
- Universal same-pass goal visibility: NOT ESTABLISHED.
- Fixed rule-pass boundaries: NOT ESTABLISHED.
- Quiescent repeated evaluation semantics: NOT ESTABLISHED.
- Exact command-side-effect visibility: NOT ESTABLISHED.

## Sources and links

- Official World's Edge Update 61321 — AIDEBUGGING, AISCRIPTDEBUGGING, current script position, jump-loop diagnostics: https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/
- Official World's Edge Update 42848 — DE scripting ABI changes, strategic-number capacity, object-data and command fixes: https://www.ageofempires.com/news/aoe2de-update-42848/
- AoE2 AI Scripting Encyclopedia — command index and confidence-tagged command semantics: https://airef.github.io/commands/commands-index.html
- AoE2 AI Scripting Encyclopedia — UserPatch patch notes and historical ABI changes: https://airef.github.io/tables/up-patch-notes.html
- UserPatch Scripting Guide — command/fact/action reference: https://userpatch.aiscripters.net/reference.html
- Public AI scripting corpus used as behavioral evidence: https://gist.github.com/mateuszszulc/491e6e94797ee0fcd4a6f24229d1be3f
- Local authoritative corpus: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\Promisory`.
