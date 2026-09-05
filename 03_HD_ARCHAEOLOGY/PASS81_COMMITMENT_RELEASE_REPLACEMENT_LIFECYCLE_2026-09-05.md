# PASS 81 — COMMITMENT RELEASE / REPLACEMENT LIFECYCLE

**Layer:** 2 — HD archaeology / evidence only  
**Status:** Research only; no `.per`, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`

## Executive result

Pass 81 investigates the next practical question after Pass 80:

> **When historical AI policy reserves resources for one objective, what evidence shows that the reservation is released, replaced, or abandoned?**

The strongest result is that the historical AI does not use a single immutable commitment mechanism. Instead, it uses several mutable state channels together:

```text
sn-resource-control
training-goals
escrow state
research-pending state
timers
```

Historical source repeatedly demonstrates the following lifecycle pattern:

```text
FREE / NORMAL SPENDING
        ↓
RESERVE FOR TARGET
        ↓
TARGET PROGRESSES OR CONDITION CHANGES
        ↓
RELEASE / RESET / REASSIGN
        ↓
NORMAL SPENDING OR NEW TARGET
```

The most important direct evidence is not that `sn-resource-control` is a formal lock. It is that historical rules **explicitly write new values into the same shared control channel and later restore it**, while other state such as escrow is explicitly released. This proves mutable reservation-like behavior, but not a formal ownership or mutex abstraction.

The research therefore supports an AEGIS commitment model while preserving a hard evidence boundary:

> **Historical AI demonstrates resource reservation and release behavior, but the sources do not establish a first-class commitment object, owner field, lock primitive, or atomic handoff protocol.**

## 1. Direct evidence: `sn-resource-control` is a shared mutable control channel

Historical AI material defines `sn-resource-control` as a strategic-number channel and uses values to alter what classes of spending are permitted.

Examples include values representing:

```text
0 = normal/free spending
1 = navy
2 = research / saving
>2 = specific target identity
```

The exact value meanings vary by historical controller and context; therefore the channel should not be treated as a globally standardized enum.

The important structural fact is that multiple rules read and write the same strategic number.

**Evidence grade:** DIRECT for shared read/write usage; AEGIS interpretation for the term "commitment channel."

## 2. Reservation is represented by state, not by a dedicated lock

Historical examples show patterns such as:

```text
if target is eligible
→ set sn-resource-control = target
→ alter training goal / escrow behavior
```

and later:

```text
if target completed / no longer required / condition changed
→ release escrow
→ reset sn-resource-control
→ restore training goal
```

This is materially different from an explicit transactional lock API.

The safe model is:

```text
SHARED STATE REPRESENTS CURRENT INTENT / RESOURCE POLICY
```

not:

```text
SHARED STATE IS A MUTEX
```

## 3. Strong direct example: technology reservation and release

Historical AI source contains a particularly useful sequence around economy upgrades.

A controller can enter a resource-control state while preparing for an upgrade, including escrow behavior used to accumulate the required resources. Later rules explicitly release escrow and restore normal resource control after the upgrade becomes executable or is completed.

Representative lifecycle:

```text
NORMAL CONTROL
↓
ACCUMULATE / RESERVE FOR UPGRADE
↓
ESCROW / RESOURCE PROTECTION
↓
RESEARCH
↓
RELEASE ESCROW
↓
RESTORE NORMAL CONTROL
```

The exact historical controller contains additional conditions, so this is a normalized lifecycle representation, not a literal single-rule implementation.

**Evidence grade:** DIRECT for the constituent state transitions; AEGIS-generalized for the lifecycle abstraction.

## 4. Release does not necessarily mean success

This distinction is essential.

A state reset can happen because:

1. the target completed;
2. the target became invalid;
3. the strategy changed;
4. another target replaced it;
5. the resource reservation was no longer needed;
6. a fallback path took control;
7. the controller intentionally reopened spending.

Therefore:

```text
release ≠ success
```

and likewise:

```text
reset ≠ failure
```

The historical source demonstrates state transitions, but the semantic reason for every individual reset must be established from its guards and neighboring rules.

## 5. Replacement is directly visible in the rule system

Historical AI contains rules where a resource-control value associated with one target is replaced by another target's value.

Examples include transitions of the general form:

```text
sn-resource-control <= normal-threshold
AND
new target conditions
→
set sn-resource-control = NEW-TARGET
```

There are also rules that move from specialized control back to normal control:

```text
sn-resource-control == TARGET
AND
completion / state condition
→
set sn-resource-control = 0
```

This establishes **state replacement**, but not an explicit transaction protocol.

**Evidence grade:** DIRECT for state replacement patterns; AEGIS-generalized for "commitment replacement."

## 6. Goal state participates in the same lifecycle

Historical controllers also use goals as mutable state variables.

A common pattern is:

```text
train-civ-goal = normal civilian production
```

then:

```text
set train-civ-goal = TARGET / UPGRADE STATE
```

and later:

```text
set train-civ-goal = normal state
```

The Age of Empires II community documentation explicitly describes goals as mutable variables: `defconst` assigns a goal identifier, while `set-goal` changes the value stored in that goal. citeturn0search0

Therefore goal mutation is a genuine state transition mechanism, not merely a label change.

## 7. Escrow is a stronger reservation primitive than `sn-resource-control`

`sn-resource-control` only changes controller policy around resource use.

Escrow, by contrast, has explicit commands such as:

```text
set-escrow-percentage
release-escrow
```

Historical AI uses these to protect resources for specific research objectives and later releases them.

That gives us a useful hierarchy:

```text
POLICY RESERVATION
    sn-resource-control / goals

RESOURCE RESERVATION
    escrow

EXECUTION STATE
    research-pending / queue state

WORLD REALIZATION
    completed technology / existing units
```

These are distinct mechanisms and should not be conflated.

## 8. `research-pending` is a lifecycle observation, not ownership

Historical rules use `up-research-status` to distinguish states such as research pending from other technology states.

This allows the controller to avoid repeatedly treating an upgrade as merely "available" when it has already entered a pending state.

The correct semantic boundary is:

```text
research available
≠
research authorized
≠
research pending
≠
research completed
```

This is structurally analogous to the production evidence ladder from Pass 80.

## 9. Timer state can delimit a commitment window

Historical scripts use timers to create active windows, cooldowns, and repeated control intervals.

A representative pattern is:

```text
ENABLE TIMER
↓
RUNNING
↓
TRIGGERED
↓
CONSUMER RULE
↓
DISABLE / RESTART
```

Timers therefore can delimit the temporal lifetime of a controller state.

However:

```text
timer expiration ≠ commitment expiration
```

unless the rules explicitly connect the timer event to release/reset behavior.

Timers are therefore **temporal infrastructure**, not commitments themselves.

## 10. The most important unresolved question: same-pass handoff

The historical evidence strongly supports mutable shared state.

The unresolved issue is whether one controller can release a resource reservation and another controller can claim it in the **same script pass**, with no intervening pass required.

The conceptual sequence is:

```text
RULE A
release sn-resource-control
        ↓
RULE B
observes free state
        ↓
RULE B
claims new target
```

There is strong general evidence that goals and strategic numbers are mutable state and that rule order affects later actions. Community documentation also demonstrates multiple rules operating on shared goal values. citeturn0search0

But the exact historical proposition:

> "A releases a reservation and B observes and claims it later in the same pass"

has not been directly traced at the individual state-provenance level.

**Status:** HIGH-VALUE UNRESOLVED.

## 11. Procedural arbitration now has a stronger formal interpretation

Passes 56, 69, 70 and 71 established that historical AI has procedural competition rather than a proven centralized optimizer.

Pass 81 adds the commitment lifecycle:

```text
CANDIDATE
↓
ELIGIBILITY
↓
CLAIM / RESERVATION STATE
↓
RESOURCE PROTECTION
↓
EXECUTION OPPORTUNITY
↓
PROGRESS OBSERVATION
↓
RELEASE / REPLACE / CONTINUE
```

Competing controllers therefore interact through:

```text
shared state
+
resource state
+
rule order
+
side effects
+
queue state
+
timers
```

This is a much stronger description of historical arbitration than calling `sn-resource-control` a lock.

## 12. Commitment state machine for AEGIS analysis

The following is an AEGIS analytical state machine, not an official engine primitive:

```text
C0 FREE
  ↓
C1 CANDIDATE SELECTED
  ↓
C2 COMMITMENT ACTIVE
  ↓
C3 RESOURCES PROTECTED
  ↓
C4 EXECUTION PENDING
  ↓
C5 PROGRESS OBSERVED
  ├──────────────→ C6 COMPLETE
  │                    ↓
  │                  C0 FREE
  │
  ├──────────────→ C7 INVALIDATED
  │                    ↓
  │                  C0 FREE
  │
  └──────────────→ C8 REPLACED
                       ↓
                  C2 NEW COMMITMENT
```

This state machine should remain architecture guidance only until Layer 3 begins.

## 13. Commitment failure taxonomy

Pass 81 refines the previous failure model:

### C-F1 — Claim failure
The controller never successfully establishes the intended shared state.

### C-F2 — Reservation failure
The controller claims policy state but cannot protect the necessary resources.

### C-F3 — Execution failure
The commitment remains active but the action never progresses.

### C-F4 — Stale commitment
The original reason for reservation disappears while the reservation remains active.

This is particularly dangerous because stale commitments can starve competing objectives.

### C-F5 — Replacement race
Two controllers alternately rewrite shared state, causing oscillation or starvation.

### C-F6 — Release failure
The target completes or becomes invalid but the reservation state is not restored.

### C-F7 — Handoff ambiguity
A reservation is released, but evidence is insufficient to determine which subsequent controller legitimately claimed the resources.

### C-F8 — Evidence failure
The observed state transition is real, but its causal owner cannot be proven.

## 14. New AEGIS engineering rule: every commitment needs an exit condition

The historical evidence strongly motivates a Layer-3 design constraint:

> **Every AEGIS commitment must have explicit continuation, success, invalidation, replacement, and timeout/recovery conditions.**

At minimum:

```text
COMMIT
├── continue while valid
├── complete → release
├── invalidate → release
├── replace → release + successor claim
└── stale/timeout → recovery + release
```

This is an AEGIS architectural requirement derived from historical failure modes and state semantics, not a claim that the HD AI already implements a formal commitment manager.

## 15. Hostile QC

Rejected:

- `sn-resource-control` is a formal mutex.
- `sn-resource-control` has one universal semantic enum across all historical scripts.
- setting a resource-control value proves ownership.
- setting escrow proves a strategic commitment exists.
- escrow release proves the associated objective succeeded.
- resetting a goal proves the objective completed.
- timer expiration proves commitment expiration.
- `research-pending` proves the research completed.
- state replacement proves two controllers intentionally negotiated a handoff.
- same-pass release→claim is proven merely because goals/SNs are mutable.

## 16. Evidence ledger

| Proposition | Grade |
|---|---|
| Goals are mutable state values | DIRECT community scripting reference |
| Historical AI repeatedly reads/writes `sn-resource-control` | DIRECT historical source |
| Historical AI uses specialized resource-control states | DIRECT historical source |
| Historical AI resets specialized resource-control states | DIRECT historical source |
| Historical AI explicitly releases escrow | DIRECT historical source |
| Historical AI uses research-pending state | DIRECT historical source |
| Historical AI uses timers for temporal control windows | DIRECT historical source |
| `sn-resource-control` is a formal mutex | REJECTED / NOT PROVEN |
| Escrow is a strategic commitment object | NOT PROVEN |
| Reset always means completion | REJECTED |
| Release always means success | REJECTED |
| Same-pass release→successor claim | HIGH-VALUE UNRESOLVED |
| Commitment state machine C0–C8 | AEGIS-GENERALIZATION |
| Every Layer-3 commitment should have explicit exit conditions | AEGIS ENGINEERING REQUIREMENT |

## 17. Disposition

The exact-ID archaeology remains parked as an optional forensic enhancement.

The production-observability branch is now strong enough to support a practical commitment investigation without exact object identity.

The next research target should therefore be the **arbitration boundary**:

```text
COMMITMENT A
     ↓
RESOURCE STATE
     ↓
RULE ORDER
     ↓
COMPETING COMMITMENT B
     ↓
WHO WINS?
```

Specifically, we need to determine from historical source whether competing resource reservations are prevented by explicit guards, resolved by rule order, or both, and whether there are examples of one target invalidating another target's reservation before execution.

## 18. Layer status

**Layer 1:** 89%; scenario automation remains retired.  
**Layer 2:** ~99%+; commitment lifecycle materially strengthened.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

## Pass 81 conclusion

The most useful result is a correction to our vocabulary.

Historical HD AI does not expose a formal commitment manager. What it does expose is enough mutable state machinery for controllers to **reserve policy, protect resources, wait for execution, observe progress, release state, and replace objectives**.

That distinction matters enormously for AEGIS.

We should not reproduce an imagined lock system. We should reproduce the **observable lifecycle properties** that the evidence supports, while adding explicit ownership, invalidation, and handoff semantics only when we enter Layer 3 and design beyond the historical implementation.

The next high-value question is therefore not "what is the lock?" It is:

> **How does procedural rule order arbitrate two simultaneously eligible commitments competing for the same finite resource pool?**
