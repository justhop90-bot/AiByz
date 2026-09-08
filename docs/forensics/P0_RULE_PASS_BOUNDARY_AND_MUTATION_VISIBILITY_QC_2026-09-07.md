# P0 Rule-Pass Boundary and Mutation Visibility QC — 2026-09-07

## Scope
This pass attacks the remaining interpreter ABI question: when a `.per` rule mutates a goal, strategic number, flag, timer, escrow state, or engine object, when can a later predicate observe that mutation?

## Evidence reviewed
- Untouched stock AI corpus under `resources\\_common\\ai\\Promisory`.
- `defaultConstants.per` on the authoritative machine copy.
- Stock use of goals, strategic numbers, timers, `disable-self`, and jump control.
- Official AoE2DE scripting/debugging documentation describing `AIDEBUGGING`, `AISCRIPTDEBUGGING`, current script position, goal values, target state, and infinite jump-loop detection.

## Established
1. The AI interpreter has mutable runtime state. Goals are variables whose values can be changed by `set-goal`; community scripting documentation describes them explicitly as variables.
2. Strategic numbers are likewise mutable runtime state and are changed by `set-strategic-number`.
3. Timers have explicit runtime states and are enabled/disabled by script actions.
4. `disable-self` changes future eligibility of the firing rule.
5. Jump control is executable control flow, not merely metadata. Official DE debugging exposes the current script position and detects infinite jump loops.
6. Therefore AEGIS must treat rule execution as an imperative interpreter, not as a declarative simultaneous rule set.

## Critical unresolved question
Source inspection does **not** prove the visibility boundary for a mutation made by rule A to a predicate in rule B. Three models remain technically possible from source alone:

### Model A — immediate visibility
Rule B sees A's mutation if B is reached later in the same interpreter traversal.

### Model B — pass-latched visibility
Predicates are evaluated against a state snapshot for the current pass; mutations become visible on a later pass/update boundary.

### Model C — hybrid
Some script variables are immediately visible while engine-derived facts or command side effects are refreshed only at defined interpreter/engine boundaries.

No honest claim among A/B/C is justified without a controlled runtime experiment or engine-level trace.

## Important negative finding
Searches for existing `AISCRIPTDEBUGGING` log output on the local machine did not produce usable AI-script traces. No existing AEGIS runtime log was found that establishes same-pass mutation visibility. Therefore this pass does **not** promote the scheduler ABI to GREEN.

## Engineering consequence
AEGIS must not depend on undocumented same-pass cascades. The safe architecture is generation-fenced:

```text
OBSERVE(G)
  -> DERIVE(G)
  -> DECIDE(G)
  -> AUTHORIZE(G)
  -> COMMAND(G)
  -> ENGINE MUTATION
  -> OBSERVE(G+1)
  -> VERIFY
```

A same-pass optimization may later be introduced only after qualification proves the relevant visibility semantics.

## Required qualification experiment
A minimal diagnostic AI should test, independently:

1. `set-goal` followed by a later same-pass goal predicate.
2. `set-goal` followed by a forward jump and then a predicate.
3. `set-goal` followed by ordinary fall-through.
4. `set-goal` followed by a bounded backward jump.
5. `set-strategic-number` followed by a later predicate.
6. A timer enable/disable mutation followed by a timer predicate.
7. A command that changes engine object state followed by an object-derived predicate.
8. The same cases across the next interpreter update.

Each test must expose an unambiguous observable result. The test must distinguish interpreter-variable visibility from engine-state refresh visibility.

## Confidence matrix
| Question | Confidence |
|---|---|
| Mutable AI runtime state exists | HIGH |
| Rule control flow is imperative | HIGH |
| `disable-self` affects future rule eligibility | HIGH |
| Jump-loop detection/current script position exists | HIGH |
| Same-pass goal visibility | UNPROVEN |
| Same-pass strategic-number visibility | UNPROVEN |
| Same-pass timer-state visibility | UNPROVEN |
| Same-pass engine-object visibility | UNPROVEN |
| Exact pass/update boundary | UNPROVEN |
| AEGIS may safely rely on same-pass cascades | NO |

## Status
Forensic phase only. No live AEGIS files changed. The scheduler remains ABI-UNQUALIFIED pending the controlled runtime experiment above.
