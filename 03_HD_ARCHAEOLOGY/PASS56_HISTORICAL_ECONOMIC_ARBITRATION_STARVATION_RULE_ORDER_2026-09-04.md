# Pass 56 — Historical Economic Arbitration / Starvation / Rule-Order Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation authority:** NONE  
**Status:** PASS WITH IMPORTANT CLOSURE  
**Predecessor:** Pass 55

## 1. Mission

Pass 55 established purpose-directed resource commitments. Pass 56 asks the next question:

```text
WHEN MULTIPLE DEMANDS ARE SIMULTANEOUSLY ELIGIBLE,
HOW DOES THE HISTORICAL AI ARBITRATE THEM?
```

Target chain:

```text
MULTIPLE DEMANDS
↓
RULE ELIGIBILITY
↓
RULE ORDER / STATE GATES
↓
FIRST EFFECTIVE ACTION
↓
RESOURCE CONSEQUENCE
↓
SUPPRESSION OF OTHER ACTIONS
↓
NEXT PASS / REASSESSMENT
```

No `.per` implementation is created.

## 2. Major finding

The archaeology now provides direct evidence that **rule ordering can function as an economic arbitration mechanism**.

The strongest source-level evidence is an explicit historical comment in the master corpus:

```text
; order of rules does matter as 1st rule that will be executed 1st,
; so next rules may not spend the resources
; so put siege training above building
```

This is unusually valuable because it is not merely inferred from source order. The historical author explicitly identifies ordering as a resource-spending control mechanism.

The consequence is:

```text
RULE ORDER
→ FIRST EFFECTIVE SIDE EFFECT
→ RESOURCE CONSUMPTION
→ LOWER RULE NO LONGER AFFORDABLE
```

Thus **priority can be encoded procedurally by placement in the rule corpus**.

## 3. Independent technical corroboration

The AoE2 AI Scripting Encyclopedia confirms that `defrule` defines rules and that behavior-changing code is organized through rules. Its broader scripting material also documents practical cases where rule ordering and state updates affect behavior.

A closely related historical AI-engine reference for the same AOE2-derived rule architecture explicitly warns that when several train rules can fire, file ordering matters and the first applicable training rule can consume the available resources.

This is useful corroboration, but the historical HD corpus itself remains the primary evidence for HD behavior.

**Evidence separation:**

```text
HD HISTORICAL COMMENT = DIRECT HD AUTHOR EVIDENCE
AOE2/DERIVED REFERENCE = TECHNICAL CORROBORATION
```

## 4. Arbitration without a scoring function

The historical mechanism does not require:

```text
score(A) = 81
score(B) = 63
```

Instead it can implement:

```text
IF A conditions are true
→ execute A

ELSE IF B conditions are true
→ execute B
```

when resource consumption makes B infeasible after A executes.

This produces **implicit priority** without explicit numeric utility.

Canonical distinction:

```text
EXPLICIT NUMERIC PRIORITY = NOT PROVEN
PROCEDURAL PRIORITY = DIRECTLY EVIDENCED
```

## 5. The critical economic mechanism: affordability collapse

Suppose two actions require overlapping resources:

```text
A requires 200 wood
B requires 175 wood
available = 200
```

If A executes first:

```text
wood → 0
B becomes unaffordable
```

The second rule does not need a `B priority = -1` state. The world/resource state itself suppresses B.

This is a powerful historical control mechanism:

```text
ORDER
+
SIDE EFFECT
+
RESOURCE STATE
=
ARBITRATION
```

It is not globally optimal merely because it is deterministic.

## 6. Historical evidence: siege above building

The direct comment at approximately line 22808 is the strongest single arbitration artifact located in this pass.

Immediately following the comment, the historical corpus contains resource-control and siege-related rules before later building/production logic.

The stated purpose is explicit:

```text
siege training should execute before building
```

because the first executed transaction can prevent later rules from spending the same resources.

This closes a previously open question from Pass 53:

> Is cross-consumer priority purely inferred from distributed gates?

**Answer:** No. At least some cross-consumer priority is explicitly encoded through **rule ordering chosen to control resource expenditure**.

## 7. `sn-resource-control` adds another arbitration layer

Rule order is not the only mechanism.

The historical corpus repeatedly uses:

```text
strategic-number sn-resource-control == 0
strategic-number sn-resource-control <= 2
strategic-number sn-resource-control == <target>
```

before setting a new commitment.

This creates a procedural lock-like effect:

```text
NO ACTIVE COMMITMENT
→ candidate may claim control

ACTIVE COMMITMENT
→ many other claim rules are blocked
```

The mechanism is not a formal mutex, but it can behave as a **distributed admission gate**.

## 8. Admission control

A recurring historical pattern is:

```text
sn-resource-control == 0
↓
strategic demand detected
↓
set resource-control = target
```

Other candidate rules commonly require:

```text
sn-resource-control <= 2
```

or another specific state.

Therefore a selected commitment can alter the eligibility landscape of subsequent rules.

This is stronger than simply “rule A appears first.”

There are two interacting arbitration dimensions:

```text
STATE GATE
+
RULE ORDER
```

## 9. Commitment replacement

The corpus also contains transitions such as:

```text
resource-control = ri-elite-eagle-warrior
+
resource condition changes
→ resource-control = ri-arbalest
```

This is direct evidence that a commitment can be redirected when local conditions make the current commitment unattractive or infeasible.

However, the exact strategic reason for every replacement is not always documented.

Therefore:

```text
STATE REPLACEMENT = DIRECT
STRATEGIC OPTIMALITY OF REPLACEMENT = NOT PROVEN
```

## 10. Cancellation vs replacement

Two distinct mechanisms must not be conflated.

### Cancellation

```text
ACTIVE CLAIM
→ invalid
→ release
→ clear
```

### Replacement

```text
ACTIVE CLAIM A
→ state changes
→ claim B becomes selected
→ control changes
```

Some historical transitions explicitly clear resource-control first. Others directly write another target.

This means future archaeology must record whether the transition is:

```text
CLEAR → SELECT
```

or:

```text
SELECT A → SELECT B
```

The latter may carry different starvation implications.

## 11. Starvation definition

For this project, define historical starvation narrowly as:

> A repeatedly eligible capability is prevented from obtaining required resources or execution opportunity because other commitments repeatedly consume or protect those resources first.

This is an analytical definition, not an engine-defined term.

Three levels:

```text
POSSIBLE STARVATION
= conditions could permit indefinite suppression

OBSERVED STARVATION
= replay/runtime demonstrates repeated suppression

PROVEN SYSTEMATIC STARVATION
= source + runtime establish a repeatable causal pattern
```

Pass 56 does **not** claim observed or proven systematic starvation.

## 12. Starvation risk is nevertheless directly encoded

The historical architecture contains the ingredients for starvation:

```text
persistent commitment
+
resource protection
+
ordered side effects
+
repeated eligibility
+
no universal fairness mechanism
```

The absence of a global fairness mechanism is not proof that starvation occurs.

Therefore:

```text
STARVATION CAPABILITY = ARCHITECTURALLY PLAUSIBLE
STARVATION OCCURRENCE = OPEN
```

## 13. Fairness is not evident

No global mechanism was recovered that says:

```text
A has waited 60s
therefore A gets priority
```

No universal round-robin resource scheduler was found.

No global aging term was established.

No universal maximum commitment age was established.

Thus historical priority appears primarily **demand/state/order driven**, not fairness driven.

This is a significant architectural characteristic, but should not be converted into a claim that the AI intentionally designed unfairness.

## 14. Resource-control mode 2 is particularly important

The historical corpus repeatedly uses:

```text
sn-resource-control == 2
```

for saving resources toward broad transitions such as Castle Age or Imperial Age and other capability targets.

Other rules commonly require `sn-resource-control < 1` or `== 0` before claiming a new target.

This creates an implicit hierarchy of availability:

```text
0 = broadly available / uncommitted
1/2 = protected strategic mode in selected controllers
>2 / target-bearing values = specialized commitment contexts
```

But because the channel is overloaded, **numeric ordering must not be interpreted as a universal priority scale**.

## 15. Immediate state changes matter

The historical scripting model permits goals and strategic numbers to be changed by actions inside rules.

The Encyclopedia's scripting documentation establishes that goals are integer state variables and rule actions modify engine state. Historical source comments also explicitly discuss situations where goals update immediately while another observation updates only on the next pass.

This creates a crucial arbitration phenomenon:

```text
RULE A executes
→ state changes immediately
→ RULE B later in same pass may see changed state
```

Where that behavior is established for the relevant predicate, rule ordering can become a same-pass state machine.

Do not generalize every fact as immediate; each engine predicate needs its own evidence.

## 16. Same-pass competition

A practical historical pattern is therefore:

```text
PASS N
├─ Rule A becomes true
│  └─ changes resource-control / goals / resources
├─ Rule B evaluated later
│  └─ sees altered state OR reduced resources
└─ Rule B no longer fires

PASS N+1
└─ new world state determines eligibility
```

This is the strongest bridge yet between:

```text
RULE ORDER
and
ECONOMIC ARBITRATION
```

## 17. Rule-order priority is local, not global

A critical limitation:

```text
Rule order can establish priority only among
rules that actually compete within the relevant execution context.
```

It does not automatically create a universal ordering over every economic decision in the AI.

Different subsystems can have separate local priorities:

```text
research priority
production priority
building priority
age-up priority
naval priority
military priority
```

The global behavior emerges from their interaction.

## 18. `disable-self` as anti-thrashing control

The historical corpus uses `disable-self` in selected controllers after one-time transitions.

This is another mechanism that can prevent a rule from repeatedly reclaiming control.

However:

```text
disable-self = local execution suppression
```

not:

```text
global fairness mechanism
```

Its use should be treated as evidence for local stabilization, not universal commitment aging.

## 19. `up-jump-rule` and control priority

The corpus also uses `up-jump-rule` in strategic transitions.

Where a jump moves evaluation into a later section, it can alter which rules are reached next and therefore change which candidate gets an opportunity to act.

This creates a second procedural arbitration primitive:

```text
RULE ORDER
+
RULE JUMP
```

The exact execution semantics of every jump target remain version-sensitive and should be runtime-verified before relying on them in Layer 3.

## 20. Resource arbitration is therefore multi-layered

Pass 56's reconstructed historical arbitration stack is:

```text
1. LOAD-TIME FILTERING
2. RULE ORDER
3. STATE GATES
4. COMMITMENT STATE
5. AFFORDABILITY
6. SIDE-EFFECT RESOURCE CONSUMPTION
7. SELF-DISABLE / JUMP / RESET
8. NEXT-PASS REASSESSMENT
```

This is a research reconstruction, not a claim that the historical developers designed a formal arbitration stack.

## 21. Strongest semantic closure

The strongest closure now is:

```text
COMPETING CAPABILITY DEMANDS
↓
CANDIDATE RULES BECOME ELIGIBLE
↓
RULE ORDER SELECTS FIRST EFFECTIVE PATH
↓
STATE / RESOURCE SIDE EFFECT OCCURS
↓
OTHER CANDIDATES MAY LOSE ELIGIBILITY
↓
COMMITMENT STATE PERSISTS
↓
NEXT PASS REASSESSES
```

This is sufficient to establish **procedural economic arbitration**.

## 22. What remains unproven

Pass 56 does not establish:

```text
GLOBAL NUMERIC PRIORITY SCORE
GLOBAL FAIRNESS POLICY
STARVATION ACTUALLY OCCURRING IN GAMEPLAY
OPTIMALITY OF RULE ORDER
UNIVERSAL SAME-PASS EVALUATION SEMANTICS FOR ALL FACTS
GLOBAL RESOURCE PORTFOLIO OPTIMIZATION
```

These remain open.

## 23. Byzantine implications

For Byzantine strategy, this finding is foundational.

Potential competing commitments include:

```text
CAMEL / HEAVY CAMEL RESPONSE
CATAPHRACT / ELITE / LOGISTICA
MONK INVESTMENT
SIEGE
NAVAL CAPABILITY
IMPERIAL TRANSITION
BLACKSMITH / MILITARY UPGRADES
```

The eventual strategic problem is not merely capability detection. It is **capability arbitration under shared resource constraints**.

Historical HD code gives us the substrate conceptually:

```text
DEMAND
→ STATE CLAIM
→ PROTECT
→ AUTHORIZE
→ SPEND
```

But it does not prove the optimal Byzantine ordering of those claims.

## 24. Updated Layer-2 economic model

The economic pillar can now be stated as:

```text
RESOURCE STOCK
+
RESOURCE FLOW
+
PURPOSE-DIRECTED ESCROW
+
COMMITMENT STATE
+
RULE-ORDER PRIORITY
+
STATE GATING
+
AFFORDABILITY
+
SIDE-EFFECT CONSUMPTION
+
RELEASE / RESET
```

The missing upper layer is:

```text
STRATEGIC VALUE / OPPORTUNITY COST
```

That remains an AEGIS research concept, not a recovered historical variable.

## 25. Evidence ledger

| Finding | Grade |
|---|---|
| Rule order can affect which resource-spending action executes first | DIRECT HD author evidence |
| First executed action can prevent later resource spending | DIRECT HD author evidence |
| Siege explicitly placed before building for resource-order reasons | DIRECT HD author evidence |
| `sn-resource-control` acts as an admission/control gate | DIRECT historical pattern |
| Resource-control can encode target identity | DIRECT historical pattern |
| Procedural priority can exist without numeric utility | DIRECT / composed |
| State changes can alter downstream rule eligibility | DIRECT / engine semantics |
| `disable-self` provides local suppression | DIRECT historical source |
| `up-jump-rule` can alter evaluation flow | DIRECT command capability; exact global effect version-sensitive |
| Starvation is possible in principle | AEGIS inference |
| Starvation actually occurs | NOT PROVEN |
| Global fairness exists | NOT PROVEN |
| Global optimizer exists | NOT PROVEN |
| Historical rule ordering is optimal | NOT PROVEN |

## 26. Final conclusion

Pass 56 closes a major economic archaeology question.

Historical HD AI does not require a centralized optimizer to arbitrate resources.

It can obtain real procedural priority from:

```text
RULE ORDER
+
STATE GATES
+
COMMITMENT STATE
+
AFFORDABILITY
+
RESOURCE CONSUMPTION
```

The decisive evidence is the historical statement that rule order matters because the first executed rule can consume resources before later rules can spend them.

Therefore the canonical Layer-2 conclusion is:

> **Historical HD AI contains procedural economic arbitration.**

It is distributed, local, deterministic in selected paths, and capable of suppressing competing actions through state and resource consequences.

It is **not proven to be globally optimal, fair, or starvation-free**.

Layer 2 remains strictly research-only. No `.per` implementation is authorized.
