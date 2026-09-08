# P0 External AI Scripting ABI Cross-Reference — 2026-09-07

## Purpose
Cross-reference the current AEGIS forensic findings against external AoE2 AI scripting references before committing further architectural assumptions.

## Source hierarchy

### Tier 1 — Current-version / official
1. World's Edge, AoE2DE Update 61321:
   https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-61321/
   - AIDEBUGGING
   - AISCRIPTDEBUGGING
   - current script position diagnostics
   - infinite jump-loop detection
   - goal/control-group/target diagnostics

2. World's Edge, AoE2DE Update 42848:
   https://www.ageofempires.com/news/aoe2de-update-42848/
   - strategic-number capacity change 303 → 511
   - object-data-action/order fixes
   - up-can-build behavior
   - up-garrison unit-line support
   - path-distance changes
   - other DE ABI changes

### Tier 2 — High-value technical reference
3. AoE2 AI Scripting Encyclopedia command index:
   https://airef.github.io/commands/commands-index.html
   - command/fact/action inventory
   - confidence labels
   - `up-jump-rule`
   - `up-get-rule-id`
   - `up-log-data`
   - `up-modify-goal`
   - `up-modify-sn`
   - `up-train`
   - `up-train-site-ready`
   - `up-can-*`
   - `disable-self`

4. AoE2 AI Scripting Encyclopedia UserPatch patch notes:
   https://airef.github.io/tables/up-patch-notes.html
   - historical ABI changes
   - immediate-effect notes for specific strategic-number behavior
   - extended goal/timer initialization
   - escrow-included / escrow-deducted semantics
   - `up-release-escrow`
   - `up-modify-escrow`
   - training queue semantics

5. UserPatch Scripting Guide:
   https://userpatch.aiscripters.net/reference.html
   - lower-level scripting command/fact/action reference
   - `up-jump-rule`
   - `up-log-data`
   - goal/SN/object/search primitives

### Tier 3 — Behavioral corpus
6. Public AoE2 AI scripting corpus:
   https://gist.github.com/mateuszszulc/491e6e94797ee0fcd4a6f24229d1be3f
   - real-world use of `set-goal`
   - `disable-self`
   - strategic-number predicates
   - goal-driven strategy transitions

## Cross-reference matrix

| Topic | External support | Local stock evidence | Status |
|---|---|---|---|
| `up-jump-rule` is control flow | Strong | Extensive use | HIGH |
| Forward/backward jumps | Strong | Extensive use | HIGH |
| `disable-self` disables current rule | Strong | Extensive use | HIGH |
| Goal mutation exists | Strong | Extensive use | HIGH |
| Strategic-number mutation exists | Strong | Extensive use | HIGH |
| Some SN mutations are documented immediate | Strong, version/history specific | Stock-dependent | HIGH for cited cases |
| Universal same-pass goal visibility | None | Inconclusive | UNPROVEN |
| Exact pass boundary | None | Inconclusive | UNPROVEN |
| Infinite jump loops are real interpreter failure mode | Official | Negative jumps in corpus | HIGH |
| Script cursor is observable | Official | Runtime not yet exercised | HIGH |
| `up-log-data` available as diagnostic channel | Strong | Needs current-runtime qualification | HIGH command existence |
| Escrow is native execution state | Strong | Direct stock use | HIGH |
| Escrow-included vs deducted semantics | Strong historical reference | Direct stock use | HIGH |
| Production goal arbitration | Behavioral + local | Direct stock evidence | HIGH |
| Single universal production FIFO | No | Not found | HIGH negative finding |
| Queue endpoint state matters | Strong command docs + local | Direct stock filters | HIGH |
| Building count proves queue availability | No | Contradicted by stock filters | HIGH negative finding |
| Construction participates in escrow | Strong historical reference + local | Direct stock evidence | HIGH |

## Important correction to earlier reasoning

Earlier reports treated the unresolved mutation-visibility question as if external documentation might have no useful evidence. That was too broad.

The external corpus does provide meaningful evidence that **specific state categories and commands have defined timing semantics**. In particular, historical UserPatch notes explicitly state that `sn-enable-training-queue` “takes effect immediately in rules” and that it affects the relevant training commands. This demonstrates that immediate state visibility exists for at least that documented mechanism.

However, that evidence cannot be generalized to all goal writes, strategic numbers, timers, search state, or engine object state. The correct conclusion is therefore:

```text
SOME mutation visibility semantics are documented.
UNIVERSAL mutation visibility semantics are not established.
```

## Revised ABI model

Do not model the interpreter as either:

```text
PURE SNAPSHOT
```

or:

```text
EVERY WRITE IMMEDIATELY VISIBLE TO EVERYTHING
```

Use a typed visibility model until runtime qualification closes the remaining gaps:

```text
AI VARIABLE STATE
  goal / SN / flag / timer
        │
        ├── documented immediate cases
        ├── documented deferred/next-pass cases, if any
        └── unknown cases requiring probe

ENGINE OBJECT STATE
  unit / building / queue / resource
        │
        └── likely separate refresh boundary; UNPROVEN
```

## Revised runtime experiment

Because `up-log-data` is documented, the test harness should prefer it over chat output.

Required probes:

```text
P01  set-goal → goal read
P02  up-modify-goal → goal read
P03  set-SN → SN read
P04  mutation → fall-through → read
P05  mutation → forward jump → read
P06  mutation → backward jump → read
P07  mutation → next update → read
P08  command → engine-state read same invocation
P09  command → engine-state read next update
P10  up-get-rule-id at known checkpoints
```

Use AIDEBUGGING/AISCRIPTDEBUGGING where launch configuration permits it. Record whether observations occur in the same interpreter invocation, same AI update, or later update.

## Architecture impact

The existing AEGIS generation-fencing architecture remains correct and becomes better justified:

```text
OBSERVE(G)
 → DERIVE(G)
 → DECIDE(G)
 → AUTHORIZE(G)
 → COMMAND(G)
 → OBSERVE(G+1)
 → VERIFY
```

Generation IDs should be used as freshness contracts rather than as an assumption about exact interpreter pass boundaries.

## Findings that remain authoritative from local forensic work

The external references do not replace the untouched current-stock corpus. They reinforce, clarify, or constrain it.

The following local findings remain authoritative for the current DE build:
- civilian worker allocation is feedback-based rather than a fixed worker registry
- source selection uses status, task load, spatial serviceability, and resource-specific policy
- dropsite topology is part of resource serviceability
- threat response is distributed rather than one global civilian evacuation manager
- production arbitration is distributed through goals, suppression, rule topology, escrow, and endpoint state
- production endpoints are operational objects rather than mere building counts
- escrow is an engine-facing transactional substrate
- command issuance is not equivalent to confirmed execution

## Negative findings preserved

No external source found during this pass establishes:
- exact current DE rule-pass start/end boundaries
- exact same-pass visibility of every goal mutation
- exact same-pass visibility of every engine command
- exact intra-update ordering for all simultaneously eligible rules
- exact current-build instruction budget/quiescence semantics

These remain runtime qualification targets.

## Source maintenance rule

Future ABI claims should cite at least one source from each applicable layer:

```text
CURRENT STOCK
     +
OFFICIAL DE DOCUMENTATION
     +
SCRIPTING REFERENCE / HISTORICAL ABI
     +
RUNTIME EXPERIMENT WHEN TIMING IS INVOLVED
```

When sources disagree, current stock and direct runtime evidence take precedence for the target build; historical documentation should be treated as version-scoped evidence rather than universal law.

## Qualification status

This cross-reference materially increases confidence in the documented command/ABI layer, but it does not eliminate the need for the targeted runtime mutation-visibility experiment.
