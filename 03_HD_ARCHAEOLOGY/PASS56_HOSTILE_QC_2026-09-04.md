# Pass 56 — Hostile QC

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Verdict:** PASS WITH EVIDENCE BOUNDARIES

## 1. Primary claim under attack

Claim:

> Historical HD AI contains procedural economic arbitration in which rule ordering, state gates, commitment state, affordability, and resource consumption can determine which competing action gets the available resources.

## 2. Strongest direct evidence

The historical corpus contains an explicit comment stating that rule order matters because the first rule executed can consume resources so later rules cannot spend them, followed by the instruction to place siege training above building.

This directly supports procedural resource arbitration.

## 3. Could the comment be stale or aspirational?

The comment alone would be insufficient if disconnected from executable code. It is not disconnected: the surrounding corpus contains ordered resource-control, production, and building rules whose eligibility depends on state and affordability.

Therefore the comment is corroborated by executable structure.

**PASS.**

## 4. Does this prove first-rule-wins globally?

No.

The evidence supports first-effective-path priority in relevant competing rule contexts. It does not establish a universal scheduler semantics for every rule in every subsystem.

**Rejected overclaim:** “the entire AI is globally first-rule-wins.”

## 5. Does resource consumption really suppress later actions?

Yes at the economic mechanism level: the historical comment explicitly describes this behavior, and affordability predicates are resource-sensitive.

But the exact resource accounting and evaluation timing of every engine fact remains version-sensitive.

**PASS WITH SCOPE LIMIT.**

## 6. Is `sn-resource-control` a numeric priority scale?

No.

Historical writers assign both small numeric modes and target identifiers. Therefore numeric magnitude cannot safely be treated as universal priority.

**PASS:** it is a control/admission channel, not a universal score.

## 7. Is starvation proven?

No.

The architecture contains plausible ingredients for starvation, but source evidence alone cannot establish that a capability is actually starved indefinitely in gameplay.

**Rejected overclaim:** “HD AI definitely starves lower-priority plans.”

## 8. Is fairness absent?

No global fairness mechanism was recovered in this pass. That supports:

```text
GLOBAL FAIRNESS = NOT PROVEN
```

It does not prove that every local subsystem is unfair or that no hidden engine mechanism exists.

## 9. Is replacement equivalent to cancellation?

No.

Direct writes from one target-bearing resource-control state to another are distinct from release-and-clear paths. The two should remain separate in the evidence model.

**PASS.**

## 10. Does `disable-self` prove anti-thrashing architecture?

Only locally.

It proves a rule can suppress its own future firing. It does not prove a global commitment scheduler.

**PASS WITH SCOPE LIMIT.**

## 11. Does `up-jump-rule` prove global priority?

No.

It proves a control-flow capability. Its use can influence which rules are reached, but the exact runtime behavior of every jump path requires target-runtime verification.

**PASS WITH VERSION BOUNDARY.**

## 12. Byzantine claim under attack

Claim:

> The arbitration findings matter directly to Byzantine strategy.

This is strategically valid but should remain an AEGIS interpretation rather than historical Byzantine source evidence.

The historical corpus does provide Byzantine-specific resource-control/Greek Fire logic, but it does not establish an optimal Byzantine arbitration order across Cataphracts, Camels, Monks, Siege, Navy, and Imperial Age.

**PASS WITH EVIDENCE SEPARATION.**

## 13. Final QC ledger

| Claim | Verdict |
|---|---|
| Historical rule order matters economically | DIRECT |
| First effective action can consume resources before later actions | DIRECT |
| Siege-over-building ordering was explicitly intended | DIRECT |
| State gates contribute to procedural priority | DIRECT |
| Resource-control can gate new commitments | DIRECT |
| Procedural priority exists without numeric utility | DIRECT / COMPOSED |
| Starvation is possible as a structural risk | INFERRED |
| Starvation occurs in gameplay | NOT PROVEN |
| Global fairness exists | NOT PROVEN |
| Global optimizer exists | NOT PROVEN |
| Rule order is globally optimal | NOT PROVEN |
| All facts observe state at the same instant | NOT PROVEN |
| Layer 2 implementation occurred | NO |

## 14. QC verdict

**PASS.**

The central claim survives because the strongest evidence is unusually explicit: historical source commentary identifies rule order as a resource-spending priority mechanism, and executable surrounding logic corroborates the mechanism.

Canonical result:

```text
HISTORICAL ECONOMIC ARBITRATION
=
PROCEDURAL PRIORITY
+
STATE GATING
+
COMMITMENT CONTROL
+
AFFORDABILITY
+
RESOURCE CONSEQUENCE
```

Not:

```text
GLOBAL OPTIMIZER
```

Not:

```text
PROVEN STARVATION
```

Not:

```text
PROVEN FAIRNESS
```

Layer 2 remains 100% research/archaeology and 0% implementation.