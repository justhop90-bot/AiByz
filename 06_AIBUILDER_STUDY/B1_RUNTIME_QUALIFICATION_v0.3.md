# B1 Runtime Authority Qualification v0.3

**Status:** FROZEN — execution artifact

**Target:** existing AiBuilder Goal 49, `desired-number-spearmen`

**Purpose:** qualify one existing-channel authority relationship at runtime. This experiment does not establish general Goal semantics, general writer precedence, Byzantine ownership, or policy architecture.

## 1. Questions

B1 separates three propositions:

- **P1 — Rule recurrence:** the experimental intervention rule is evaluated repeatedly in this configuration. The source corpus provides only UNCERTAIN / COMPOSED support for engine-level `(true)` firing semantics.
- **P2 — Writer precedence:** the experimental writer can affect the value observed by the existing Goal-49 consumer under the tested conditions.
- **P3 — Lifecycle persistence:** the experimental authority remains effective across a genuine phase transition, if one occurs naturally in the unmodified test environment.

P1, P2, and P3 are separate questions. No production count alone proves all three.

## 2. Static reference chain

```text
phaseUpdate.per
    ↓
Goal 49: desired-number-spearmen
    ↓
militaryUnits.per
    ↓
unit-type-count-total spearman-line < desired-number-spearmen
    ↓
can-train spearman-line
    ↓
train spearman-line
```

The existing consumer is not modified by B1.

## 3. Intervention artifact

The experimental intervention writes only Goal 49 and introduces no new Goal, timer, scratch register, or policy state.

```lisp
(defrule
  (true)
  =>
  (chat-local-to-self "B1 test artifact v0.3 loaded")
  (disable-self))

(defrule
  (true)
  =>
  (set-goal desired-number-spearmen 20))
```

The first rule is instrumentation only. It is not evidence that the second rule fires repeatedly.

The second rule is the experimental writer. Its intended test value is `20`, chosen to be distinguishable from the existing phase-policy value.

### Evidence classification of `(true)`

The corpus contains repeated-use patterns whose functional design is consistent with recurring evaluation of `(true)`, but the corpus does not directly establish engine-level firing semantics.

**Status: UNCERTAIN / COMPOSED SUPPORT.**

B1 may provide runtime evidence for this specific intervention pattern, but a result must not be generalized into a universal claim about every `(true)` rule.

## 4. Preconditions

Before execution:

1. Goal 49 is confirmed in the current ABI/source inventory.
2. `phaseUpdate.per` remains unchanged for the test.
3. `militaryUnits.per` remains unchanged for the test.
4. The test artifact writes only `desired-number-spearmen`.
5. No new Goal is declared.
6. No new timer is declared.
7. No scratch/register Goal is used as test state.
8. The existing Goal-49 consumer remains the execution path.
9. Spearman feasibility conditions are characterized sufficiently to distinguish authority evidence from resource/population/queue failure.
10. The test configuration is otherwise unchanged from the selected baseline.

No artificial phase-transition mechanism is added.

## 5. B1-0 — Instrument Integrity

**Question:** Did the intended test artifact load and execute in the selected configuration?

Required evidence:

- artifact present in the loaded AI;
- no prohibited Goal/timer/scratch allocation;
- instrumentation behavior observed, if available;
- test configuration identified;
- no modification to the existing Goal-49 consumer.

**Outcome:**

- **CONFIRMED** — artifact integrity and execution evidence are sufficient.
- **INCONCLUSIVE** — execution cannot be established cleanly.
- **DISPROVEN** — the artifact demonstrably did not execute or violated the test contract.

B1-0 failure or inconclusive status prevents an authority conclusion.

## 6. B1-1 — Repeated Intervention / Writer Precedence

**Question:** Can the additive writer affect the value observed by the existing Goal-49 consumer under the tested conditions?

The strongest evidence is at the consumer boundary. Downstream production is corroborating evidence only and must be interpreted with feasibility, queueing, population, timing, and competing rules characterized.

A production count that remains near the phase-policy value is **not**, by itself, proof that the phase writer won: a one-shot intervention or feasibility constraint can produce the same observation.

A result consistent with the experimental value across repeated intervention opportunities is strong evidence that the additive writer is effective in this configuration, provided competing explanations are insufficient.

**Outcome:**

- **CONFIRMED** — the existing consumer exhibits behavior consistent with Goal 49 remaining at the experimental value across repeated intervention opportunities, with feasibility conditions characterized and no competing explanation sufficient to account for the result.
- **INCONCLUSIVE** — observations do not uniquely distinguish effective repeated intervention from alternative explanations.
- **DISPROVEN** — sufficiently discriminating evidence demonstrates that the additive writer cannot affect the existing consumer under the tested conditions.

B1-1 CONFIRMED qualifies only this tested Goal-49 relationship.

## 7. B1-2 — Existing Consumer Response

**Question:** Once an effective experimental value is established, does the unchanged `militaryUnits.per` consumer respond through its existing feasibility and training path?

Required evidence distinguishes:

1. Goal value at the consumer boundary;
2. consumer evaluation;
3. feasibility state;
4. training request;
5. resulting engine transition, where observable.

An action request is not completion evidence. A later unit count is not automatically causal ownership evidence.

**Outcome:**

- **CONFIRMED** — the existing consumer responds to the qualified Goal value through the existing execution path.
- **INCONCLUSIVE** — the consumer/action boundary cannot be separated from competing explanations.
- **DISPROVEN** — the existing consumer demonstrably does not respond to the qualified Goal value under satisfiable conditions.

## 8. B1-3 — Conditional Lifecycle Observation

**Question:** Does the qualified authority persist across a genuine phase transition?

B1-3 is executable only if the unmodified test configuration naturally produces a genuine phase transition. The experiment may not manufacture one by changing phase configuration merely to satisfy this protocol.

If no genuine phase transition occurs:

**B1-3 = NOT APPLICABLE / NOT EXECUTED.**

This is not a failure and is not evidence against authority.

If a genuine transition occurs and B1-1 was CONFIRMED:

- **CONFIRMED** — the experimental value remains effective across the transition under the tested conditions.
- **DISPROVEN** — the value demonstrably loses authority to the phase writer or another characterized writer after the transition.
- **INCONCLUSIVE** — observations cannot distinguish persistence from another cause.

If B1-1 is not CONFIRMED, B1-3 is not executed as an authority test.

## 9. Promotion rule

B1 passes runtime authority qualification only when:

- B1-0 = CONFIRMED;
- B1-1 = CONFIRMED;
- B1-2 = CONFIRMED.

B1-3 is reported separately and is conditional on a genuine phase transition.

A B1 pass authorizes the next narrow runtime qualification experiment. It does **not** authorize:

- Byzantine ownership of Goal 49 in production;
- generalization to Goals 48, 54, 57, 61, or other channels;
- civilian-channel authority;
- new Goal allocation;
- new timer allocation;
- scratch-register use as AEGIS state;
- a broad Byzantine override layer;
- claims about universal `(true)` semantics;
- claims about `any-enemy` semantics;
- a complete Byzantine policy.

## 10. Tester observation contract

The tester reports observations from the unmodified test run. The tester is not asked to perform a discovery campaign or infer engine semantics.

The result record should contain only:

- configuration/run identity;
- artifact execution evidence;
- observed Goal/consumer evidence where available;
- feasibility observations;
- action-request evidence;
- physical/world-state evidence where available;
- phase-transition evidence, if any;
- timestamps or event ordering sufficient to establish sequence;
- anomalies or contradictions.

The tester does not select additional probes in response to an ambiguous result.

## 11. Result vocabulary

**CONFIRMED:** required evidence supports the proposition with no material contradiction.

**DISPROVEN:** sufficiently discriminating evidence contradicts the proposition.

**INCONCLUSIVE:** evidence does not uniquely distinguish the competing explanations.

**NOT APPLICABLE / NOT EXECUTED:** a conditional portion of the protocol could not validly run under the unmodified test conditions.

INCONCLUSIVE is not failure. It blocks promotion of the proposition until a better-qualified experiment exists.

## 12. Scope boundary

B1 is a single-channel runtime qualification. It is necessary and insufficient for a working Byzantine policy.

The next qualification may reuse this experimental shape on another existing channel, but each channel receives its own evidence and result. No cross-channel authority is assumed.
