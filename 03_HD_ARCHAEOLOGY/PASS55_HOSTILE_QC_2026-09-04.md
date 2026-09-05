# Pass 55 — Hostile QC

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation authority:** NONE  
**Verdict:** PASS — with explicit evidence boundaries

## 1. QC objective

Attempt to falsify the Pass 55 claim that the historical HD AI contains a genuine purpose-directed resource commitment mechanism spanning protection, feasibility, authorization, action, and release/reset.

The QC specifically rejects any conclusion that requires:

- a centralized optimizer;
- a hidden utility function;
- successful runtime completion without replay evidence;
- modern AEGIS concepts being relabeled as historical variables.

## 2. Falsification test: is escrow merely a passive resource buffer?

**Failed falsification.**

The historical corpus explicitly pairs escrow percentage activation with `escrow-purpose-goal`, whose definition states that it tracks what escrow is used for. Multiple later rules read that purpose and decide when to release or cancel it.

Therefore the strongest conclusion is more than “escrow exists.”

**PASS:** purpose-directed commitment is directly encoded in selected historical controllers.

## 3. Falsification test: is `sn-resource-control` just a numeric priority level?

**Failed falsification.**

The corpus sets the same strategic-number channel to named targets including technologies, units, siege, and navy. Later rules compare the channel against those targets.

Therefore the channel can function as a target-bearing control register.

**PASS:** it is not safe to model `sn-resource-control` as only an ordinal 0/1/2/3 state machine.

## 4. Falsification test: does affordability prove action?

**Passed falsification.**

`can-research-with-escrow`, `can-train-with-escrow`, and `can-build-with-escrow` are facts, while `research`, `train`, and `build` are actions. The historical chains frequently place release between feasibility and action.

**PASS:** affordability remains an authorization gate, not proof of world effect.

## 5. Falsification test: does release prove completion?

**Passed falsification.**

Release is frequently followed by an action; other paths release because a commitment becomes invalid. Therefore release is a control transition, not a completion event.

**PASS:** release ≠ completion.

## 6. Falsification test: is production authorization actually connected to resource commitment?

**Failed falsification.**

The battering-ram chain selects `battering-ram` as resource-control state, invokes wood-saving behavior, checks `can-train-with-escrow`, releases wood/gold, trains the ram, and resets resource-control to 0.

**PASS:** selected production authorization chain is historically closed at source level.

## 7. Falsification test: is research authorization actually connected to resource commitment?

**Failed falsification.**

The historical corpus repeatedly uses escrow-aware research predicates followed by release and `research` actions. Byzantine Greek Fire is a direct civilization-specific example.

**PASS:** selected research authorization chains are historically closed at source level.

## 8. Falsification test: are cancellations real or inferred?

**Failed falsification.**

The unique-unit escrow controller explicitly turns escrow percentages off, releases food/gold, and clears the purpose goal when prerequisites disappear or the AI is under attack under the specified population condition.

**PASS:** selected invalidation/emergency-release behavior is direct historical evidence.

## 9. Falsification test: is cross-consumer interaction merely theoretical?

**Failed falsification.**

The same resource-control and escrow mechanisms are used for Town Centers, blacksmith technologies, unique-unit upgrades, siege, navy, Imperial Age, halberdier, and civilization-specific research.

**PASS:** cross-consumer interaction is directly present.

## 10. Falsification test: does this prove global arbitration?

**Passed falsification.**

No evidence recovered in this pass establishes a single global candidate set, utility function, portfolio optimizer, or mathematically ranked cross-consumer choice mechanism.

**REJECTED CLAIM:** “HD AI had a global resource optimizer.”

The defensible conclusion is distributed priority/eligibility encoded by state, rule ordering, conditions, and commitment mechanisms.

## 11. Falsification test: does this prove optimality?

**Passed falsification.**

The historical source proves that a target can be protected and authorized. It does not prove the target was strategically optimal.

**REJECTED CLAIM:** “historical resource control was optimal.”

## 12. Falsification test: does this prove runtime manifestation?

**Passed falsification.**

Source archaeology proves executable historical intent and control structure. Replay archaeology still has unresolved pending lifecycle transitions and does not yet universally promote queue/build/research actions to completed world effects.

**REJECTED CLAIM:** “every source-level commitment has been replay-verified.”

## 13. Falsification test: is Byzantine evidence generic rather than civilization-specific?

**Failed falsification.**

The historical corpus contains a `#load-if-defined BYZANTINE-CIV` block in which resource-control state, naval/military unit counts, escrow-aware research feasibility, and Greek Fire research are directly connected.

**PASS:** at least one Byzantine-specific resource commitment chain is directly evidenced.

## 14. Falsification test: did Pass 55 accidentally become Layer 3?

**Passed falsification.**

No `.per` implementation was created. The artifact contains only archaeological conclusions, evidence boundaries, reconstructed semantic models, and future design implications.

**PASS:** Layer boundary preserved.

## 15. Final evidence ledger

| Claim | Result |
|---|---|
| Escrow exists | DIRECT |
| Escrow can be purpose-directed | DIRECT |
| Purpose is explicitly stored in a goal | DIRECT |
| Resource-control is a persistent control channel | DIRECT |
| Resource-control can encode target identity | DIRECT |
| Escrow-aware affordability gates research | DIRECT |
| Escrow-aware affordability gates production | DIRECT |
| Escrow-aware affordability gates building | DIRECT |
| Release can precede authorized action | DIRECT |
| Commitments can be cancelled | DIRECT |
| Selected emergency displacement exists | DIRECT |
| Cross-consumer interaction exists | DIRECT |
| Byzantine Greek Fire commitment exists | DIRECT |
| Global optimizer exists | NOT PROVEN |
| Global opportunity-cost calculation exists | NOT PROVEN |
| Historical strategy is optimal | NOT PROVEN |
| Every action completes successfully | NOT PROVEN |
| Every source chain is replay-verified | NOT PROVEN |

## 16. QC verdict

**PASS.**

Pass 55 survives hostile review because its strongest claims are source-level and narrowly scoped.

The central canonical finding is:

```text
HISTORICAL HD AI
=
DISTRIBUTED RESOURCE-COMMITMENT CONTROL

not

GLOBAL ECONOMIC OPTIMIZER
```

The most important remaining archaeological task is now not proving that escrow exists. That is closed.

The next economic question is **arbitration order and starvation behavior**:

```text
MULTIPLE SIMULTANEOUS DEMANDS
↓
WHICH COMMITMENT WINS?
↓
WHICH COMMITMENT IS SUPPRESSED?
↓
CAN A LOWER-PRIORITY COMMITMENT STARVE?
↓
WHEN DOES THE CONTROLLER SWITCH?
↓
WHAT HAPPENS WHEN TWO ACTIONS BECOME FEASIBLE IN THE SAME PASS?
```

That is the highest-value continuation for the economic archaeology.

**Pass 55 Hostile QC: PASS.**

Layer 2 remains strictly research-only.