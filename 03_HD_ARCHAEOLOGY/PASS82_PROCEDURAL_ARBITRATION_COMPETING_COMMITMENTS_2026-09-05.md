# PASS 82 — PROCEDURAL ARBITRATION OF COMPETING COMMITMENTS

**Layer:** 2 — HD archaeology / evidence only  
**Status:** Research only; no `.per` implementation, runtime splice, deployment, or Layer-1 scenario work.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**Predecessor:** Pass 81

## Executive result

Pass 82 attacks the central remaining economic question:

> **When two objectives are simultaneously eligible and compete for the same finite resources, what determines which one gets the execution opportunity?**

The answer is now substantially stronger than the earlier generic "rule order matters" formulation.

Historical HD evidence supports a **distributed procedural arbitration mechanism** composed of:

```text
RULE ORDER
+
STATE GATES
+
COMMITMENT / RESOURCE-CONTROL STATE
+
AFFORDABILITY
+
SIDE-EFFECT RESOURCE CONSUMPTION
+
LOCAL SELF-SUPPRESSION / CONTROL-FLOW
```

The strongest direct evidence is an explicit historical author comment stating that rule order matters because the first rule executed can consume resources so later rules cannot spend them, with the concrete instruction to put siege training above building. This is corroborated by surrounding executable patterns in which specialized resource-control states suppress alternative consumers.

The key refinement is that priority is not simply "the first rule in the file." It is the first **effective** candidate after load-time conditions, facts, state gates, current resource state, and control-flow conditions have been applied.

## 1. Direct closure: procedural economic arbitration

The historical corpus contains an unusually explicit author comment:

```text
order of rules does matter as 1st rule that will be executed 1st,
so next rules may not spend the resources,
so put siege training above building
```

This directly connects:

```text
rule ordering
→ first execution
→ resource consumption
→ suppression of later spending
```

The surrounding executable corpus contains resource-sensitive predicates and production/building actions, so the comment is corroborated by executable structure rather than standing alone as an aspirational note.

**Evidence grade:** DIRECT historical author evidence.

## 2. Correct formulation: first effective path

The statement "first rule wins" is too broad.

The defensible formulation is:

> Among rules evaluated in the relevant execution context, the first rule that becomes effective and performs the relevant side effect can alter the state and resource conditions seen by later competing rules.

A rule placed first can fail because its facts are false. A later rule can win when earlier candidates are ineffective.

Therefore:

```text
TEXTUAL ORDER ≠ AUTOMATIC EXECUTION
TEXTUAL ORDER + ELIGIBILITY + STATE = PROCEDURAL PRIORITY
```

## 3. Candidate × state is the true arbitration surface

A candidate does not have a fixed execution priority independent of state.

The useful model is:

```text
Candidate
×
Current state
×
Rule position
×
Execution context
=
Effective opportunity
```

Relevant context includes:

- load-time inclusion/exclusion;
- facts;
- goals;
- strategic numbers;
- timers;
- resources;
- queue state;
- `can-*` predicates;
- control-flow operations.

This is a conditional procedural system, not a universal ranking table.

## 4. State gates are part of arbitration

Historical source repeatedly uses conditions such as:

```text
sn-resource-control == 0
sn-resource-control <= 2
sn-resource-control == TARGET
```

These gates change which candidates are even eligible to compete.

A typical historical pattern is:

```text
FREE CONTROL
↓
TARGET CONDITIONS TRUE
↓
SET RESOURCE-CONTROL = TARGET
↓
OTHER CLAIM RULES BECOME FALSE
```

Thus a commitment can change the future candidate set.

This is stronger than static source ordering:

```text
state
→ candidate eligibility
→ arbitration surface
```

**Evidence grade:** DIRECT historical pattern.

## 5. Resource consumption is an implicit veto

When two eligible actions consume overlapping resources, the first effective side effect can make the later action unaffordable:

```text
A eligible
B eligible
resources sufficient for A
↓
A executes
↓
resources decrease
↓
B affordability fails
```

The system therefore does not need an explicit "B loses" command. The resource state itself can suppress B.

This is the mechanism behind procedural economic arbitration.

## 6. Explicit priority vs procedural priority

### Explicit priority

A mechanism directly represents:

```text
A > B
```

No universal historical mechanism of this form has been recovered.

### Procedural priority

Code structure produces:

```text
A reached first
→ A executes
→ state/resources change
→ B no longer executes
```

This is directly supported in relevant historical contexts.

Therefore:

```text
GLOBAL NUMERIC PRIORITY = NOT PROVEN
PROCEDURAL PRIORITY = PROVEN IN RELEVANT CONTEXTS
```

## 7. `sn-resource-control` is admission control, not a score

Historical `sn-resource-control` usage can prevent broad classes of actions from claiming resources while a specialized objective is active.

Operationally, this behaves as a stateful admission gate:

```text
FREE
→ claims permitted

SPECIALIZED STATE
→ selected claims permitted
→ other claims blocked or altered
```

But the channel is overloaded with different values and meanings.

Correct:

```text
resource-control = stateful admission policy
```

Incorrect:

```text
resource-control = universal utility score
```

## 8. Replacement changes future eligibility

Historical source contains transitions that replace one target-bearing control state with another.

Conceptually:

```text
A active
↓
B becomes eligible
↓
control state changes
↓
A's future rules may stop qualifying
↓
B's future rules may begin qualifying
```

This establishes state replacement. It does not prove that the historical controller evaluated A and B using a centralized utility function.

**Evidence grade:** DIRECT for state replacement; AEGIS interpretation for candidate-set terminology.

## 9. Cancellation and replacement are different

Two lifecycle forms must remain separate:

```text
A → release/reset → FREE
```

versus:

```text
A → B
```

The first opens an opportunity for subsequent candidates. The second transfers the state directly to another target.

This distinction matters for fairness and starvation analysis.

Historical source demonstrates both state behaviors but does not establish a universal fairness policy governing either.

## 10. Same-pass competition remains a narrow open question

Pass 81 identified same-pass handoff as the highest-value unresolved issue.

Pass 82 narrows it but does not falsely close it:

```text
Rule A writes shared state
↓
later rules operate against shared state
```

The broader procedural arbitration model is established without needing the stronger claim.

The exact proposition below remains open:

```text
Rule A releases commitment
AND
Rule B later in the same pass
reads the released value
AND
Rule B claims it
```

No dedicated single-execution state-provenance trace has yet closed that exact edge.

**Status:** OPEN, non-blocking.

## 11. Historical arbitration loop

The strongest normalized loop is:

```text
OBSERVE STATE
↓
ELIGIBLE RULE PATHS
↓
PROCEDURAL ORDER
↓
FIRST EFFECTIVE SIDE EFFECT
↓
RESOURCE / GOAL / SN MUTATION
↓
COMPETING CONDITIONS CHANGE
↓
COMMITMENT CONTINUES / REPLACES / RELEASES
↓
NEXT PASS
```

"Eligible rule paths" is an analytical abstraction. It does not claim that the historical AI explicitly generated an in-memory candidate array.

## 12. No evidence of a universal argmax optimizer

Nothing recovered establishes a mechanism equivalent to:

```text
for candidate in candidates:
    score(candidate)
select argmax(score)
execute(selected)
```

The evidence instead supports:

```text
ordered conditional rules
→ first effective path
→ state/resource mutation
→ changed downstream eligibility
```

This distinction is fundamental to the eventual AEGIS architecture.

## 13. Starvation risk is structurally identifiable

A starvation risk exists when:

```text
A repeatedly eligible
+
B repeatedly preempts A
+
B consumes/protects required resources
+
A has no stronger procedural opportunity
+
A has no fairness escape
```

This is still a structural risk, not proof of indefinite gameplay starvation.

Required evidence for stronger closure would be a controlled trace demonstrating repeated A eligibility, repeated B preemption, and sustained A suppression.

Therefore:

```text
STARVATION MECHANISM = PLAUSIBLE
STARVATION OCCURRENCE = OPEN
```

## 14. Fairness remains unproven

No universal historical mechanism has been recovered for:

```text
waiting-time aging
round-robin arbitration
maximum commitment age
forced release after N failures
minimum resource share
```

The narrow conclusion is:

> No universal fairness mechanism has been recovered from the inspected historical architecture.

This does not prove every local subsystem is unfair.

## 15. `disable-self` is local stabilization

Historical use of `disable-self` can stop a rule from repeatedly firing after its local transition.

That can reduce local thrashing:

```text
transition
↓
disable rule
↓
rule cannot immediately reclaim same opportunity
```

But it is not a global fairness system and does not prove ownership transfer.

## 16. `up-jump-rule` is control-flow priority

`up-jump-rule` can influence which rule section is reached next.

Its correct classification is:

```text
CONTROL-FLOW PRIORITY
```

rather than direct resource priority.

The command capability is known; every historical jump topology remains version-sensitive and should be runtime-verified before implementation.

## 17. External corroboration

Community scripting examples independently demonstrate the standard production pattern:

```text
(unit-type-count-total knight-line < N)
(can-train knight-line)
→
(train knight-line)
```

and analogous production rules for villagers and siege. This corroborates the conditional-rule execution substrate, but does not independently prove the historical HD economic arbitration comment. citeturn2search0

Public historical AI examples also expose the practical use of target-bearing `sn-resource-control` states, including transitions that protect resources for upgrades or specialized production and later restore normal control. citeturn2search3turn2search4

Official AoE2DE patch history confirms that AI training/research queue controls affect the semantics of `can-train`, `train`, `up-can-train`, and related commands, reinforcing the conclusion that command eligibility is state-dependent rather than a universal receipt. citeturn0search2

## 18. Byzantine implication

The eventual Byzantine controller must arbitrate among competing demands such as:

```text
Camel response
Cataphract / Elite / Logistica
Monks
Siege
Naval investment
Blacksmith upgrades
Imperial transition
Defensive infrastructure
```

Historical archaeology does not establish an optimal ordering among these.

It does establish the execution substrate on which such competition can occur:

```text
THREAT / OBJECTIVE
↓
ELIGIBILITY
↓
COMMITMENT / RESOURCE POLICY
↓
PROCEDURAL ORDER
↓
AFFORDABILITY
↓
SIDE EFFECT
↓
STATE CHANGE
↓
REASSESSMENT
```

AEGIS will eventually add explicit strategic valuation above this substrate. That is Layer 3 design, not historical reconstruction.

## 19. Architectural boundary recovered

### Historical substrate

```text
facts
state
resources
rules
commitments
procedural order
side effects
```

### AEGIS strategic layer

```text
candidate generation
utility / value
opportunity cost
risk
tempo
option value
fairness / starvation protection
```

The two must not be conflated.

The correct eventual relationship is:

```text
AEGIS STRATEGY
↓
prioritizes intent
↓
HD EXECUTION SUBSTRATE
↓
rules + state + resources + commands
```

## 20. Hostile QC

Rejected:

- Entire AI is globally first-rule-wins.
- `sn-resource-control` is a universal numeric priority score.
- Higher resource-control value means higher priority.
- Every resource competition is intentional.
- Every replacement is a negotiated handoff.
- `disable-self` provides global fairness.
- `up-jump-rule` proves global strategic priority.
- Structural starvation risk proves starvation occurs.
- Historical rule order is strategically optimal.
- Historical AI contains a universal argmax optimizer.
- Same-pass release→claim is fully proven.

## 21. Evidence ledger

| Proposition | Grade |
|---|---|
| Rule order can determine which competing resource-spending action gets first opportunity | DIRECT HD author evidence |
| First executed action can alter resources available to later actions | DIRECT HD author evidence |
| Siege was explicitly ordered above building for resource reasons | DIRECT HD author evidence |
| Shared resource-control state gates candidate rules | DIRECT historical source |
| Resource consumption can suppress later affordability | DIRECT / composed |
| Procedural priority exists without a universal numeric utility score | DIRECT / composed |
| Replacement changes future eligibility | DIRECT state evidence + AEGIS interpretation |
| No universal numeric priority score recovered | NEGATIVE RESEARCH RESULT |
| No universal fairness mechanism recovered | NEGATIVE RESEARCH RESULT |
| Starvation is structurally possible | AEGIS inference |
| Starvation occurs systematically in gameplay | NOT PROVEN |
| Global optimizer exists | NOT PROVEN |
| Same-pass release→successor claim | OPEN |
| AEGIS should add strategic valuation above the HD substrate | AEGIS DESIGN REQUIREMENT |

## 22. Closure

Pass 82 closes the broad procedural-arbitration question.

The historical HD AI can arbitrate competing economic demands without a proven centralized optimizer through:

```text
ELIGIBILITY
+
RULE ORDER
+
SHARED STATE GATES
+
COMMITMENT STATE
+
AFFORDABILITY
+
RESOURCE CONSUMPTION
=
PROCEDURAL ECONOMIC ARBITRATION
```

The correct term is **first effective path**, not first textual rule.

The historical priority mechanism is therefore emergent from ordered conditional rules and mutable state rather than necessarily represented as one explicit priority variable.

This is a major AEGIS finding: the HD execution substrate already contains genuine procedural arbitration, but its historical policy does not substitute for explicit strategic valuation.

## 23. Next target: failure-to-execution feedback

The highest-value remaining Layer-2 question is now:

```text
COMMITMENT SELECTED
↓
ACTION ATTEMPTED
↓
EXPECTED STATE CHANGE
↓
STATE CHANGE ABSENT / PARTIAL / SUCCESSFUL
↓
RETRY / BACKOFF / REPLACE / RELEASE
```

Target failure classes:

```text
NO OPPORTUNITY
RESOURCE FAILURE
PRODUCER FAILURE
QUEUE FAILURE
TEMPORAL FAILURE
INVALIDATED TARGET
PARTIAL PROGRESS
SUCCESS
```

This directly connects commitment state to adaptive control and is more valuable than further exact-ID archaeology.

## 24. Layer status

**Layer 1:** 89%; scenario automation remains retired.  
**Layer 2:** ~99%+; procedural economic arbitration materially closed.  
**Layer 3:** 0%; no implementation.  
**Deployment:** 0%.

## Pass 82 conclusion

The historical HD AI does not need a visible priority manager to possess procedural priority.

It can create priority through:

```text
WHEN A IS ELIGIBLE
+
WHERE A APPEARS
+
WHAT STATE A WRITES
+
WHAT RESOURCES A CONSUMES
+
WHICH LATER RULES A MAKES INEFFECTIVE
```

That is procedural arbitration.

It is real, useful, and directly relevant to AEGIS—but it is not an optimizer, not a fairness system, and not proof of globally rational behavior.

The next pass therefore moves one level deeper into the control loop: **how historical AI policy detects and responds when an attempted action fails to produce the expected state transition.**
