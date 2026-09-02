# Layer 2 — Pass 5: Cross-Validation, Causal Stress Testing, and Adjudication

## 0. Purpose and research posture

Pass 4 constructed an implementation-independent causal ontology from the recovered HD/2013 AI. Pass 5 exists to prevent that ontology from becoming an elegant but unfalsifiable philosophy.

The research question is no longer merely:

> What strategic concepts can be inferred?

It is:

> Which inferred concepts survive independent justification, explicit boundary conditions, measurable-state requirements, counterexamples, and empirical falsification?

The governing transformation is:

`historical observation -> reconstructed control event -> generalized claim -> validity conditions -> independent support -> measurement model -> counterexample -> falsifier -> adjudication -> AEGIS requirement`

Pass 5 therefore treats every important generalization as a **claim under test**, not as an axiom simply because it is intuitively attractive or appears repeatedly in historical code.

## 1. Evidence hierarchy

Evidence is ranked rather than blended.

### E0 — Direct game/engine fact
A mechanically established property of the game or execution environment.

### E1 — Direct historical implementation evidence
The recovered HD/2013 source explicitly exhibits the behavior.

### E2 — Repeated historical pattern
The behavior occurs in multiple independent control events or subsystems.

### E3 — Independent strategic justification
The relationship follows from general AoE2 mechanics, competitive theory, or established causal reasoning independent of the historical implementation.

### E4 — Empirical observation
Replays, controlled tests, measurements, or repeated experiments support the claim.

### E5 — Model inference
The claim is a useful AEGIS abstraction inferred from stronger evidence but not itself directly observed.

A claim becomes strong only when these layers converge. Historical implementation alone does not prove universality.

## 2. Epistemic discipline

The following statuses are mandatory:

- `CONFIRMED` — evidence converges and material counterexamples have not broken the claim within its declared domain.
- `PROBABLE` — substantial convergent evidence, but calibration or broader testing remains.
- `CONTEXT_DEPENDENT` — valid only under declared conditions.
- `HEURISTIC` — operationally useful approximation rather than a general law.
- `HYPOTHESIS` — plausible model awaiting meaningful validation.
- `DISPROVEN` — materially contradicted by evidence.
- `OBSOLETE` — historically useful but no longer applicable to the target runtime/game state.
- `ENGINE_SPECIFIC` — true because of execution-substrate behavior rather than game strategy.

No claim may be promoted merely because it is elegant.

## 3. Validation protocol

For each claim, perform the following sequence:

1. **Historical trace** — identify the source behavior that generated the claim.
2. **Independent rationale** — derive why the relationship could be true without relying on the source author's implementation.
3. **Domain declaration** — state where the relationship applies and where it does not.
4. **Observable state** — identify the measurements required to evaluate it.
5. **Hidden variables** — list quantities the controller cannot directly observe.
6. **Confounders** — identify alternate explanations for the apparent relationship.
7. **Counterexample construction** — deliberately construct states where the claim should fail.
8. **Falsifier** — specify an observation or experiment that would materially invalidate it.
9. **Adjudication** — classify the claim after testing.
10. **AEGIS consequence** — only then derive required state, policy, or architecture.

## 4. Critical correction to Pass 4: conditionality

Several Pass-4 statements were too universal in wording.

The correct form of a strategic law is generally:

`relationship + conditions + horizon + objective + uncertainty boundary`

For example:

Weak:

> Position modifies capability value.

Stronger:

> Position modifies the expected value of a capability when the capability's effectiveness depends materially on geography, access, exposure, reinforcement geometry, or resource proximity, evaluated over a declared time horizon and objective.

Likewise:

> Resources have opportunity cost.

becomes:

> A resource commitment has opportunity cost equal to the value of the best materially feasible alternative conversion displaced by the commitment, conditioned on timing, prerequisites, liquidity, uncertainty, and reversibility.

This conditional formulation is now the preferred form for future ontology work.

# 5. Adjudication of the 20 Pass-4 strategic axioms

## AX-001 — Strategy as causal state transformation

**Claim:** AoE2 strategy is better modeled as transformation of state than as static build-order lookup.

**Historical support:** Strong. The recovered AI repeatedly changes strategy, economic allocation, military selection, and temporal state in response to observations.

**Independent support:** Strong. A build order is a prior policy; actual game state changes through opponent action, map geometry, resource availability, damage, technology, and timing.

**Required measurements:** state, action, time, resource flow, capability, opponent response.

**Counterexample:** A deterministic closed environment with no opponent variation could make a fixed sequence sufficient. This does not invalidate the claim for adversarial games; it defines its domain.

**Adjudication:** `PROBABLE`, domain = adaptive adversarial AoE2 play.

**AEGIS requirement:** Preserve explicit state and transition semantics rather than representing strategy as one immutable label.

## AX-002 — Capability over raw unit count

**Claim:** Capability is a more useful strategic object than unit count.

**Reasoning:** Unit count is observable evidence; capability incorporates composition, technology, production, resources, position, readiness, reinforcement, and timing.

**Counterexample:** For some narrow combat calculations, unit count is itself a sufficient statistic. Therefore capability must not replace raw observations; it must sit above them.

**Adjudication:** `CONTEXT_DEPENDENT`, but strongly justified at strategic-planning level.

**AEGIS requirement:** Maintain both raw facts and derived capability estimates.

## AX-003 — State-dependent resource value

**Claim:** Marginal resource value changes with state.

**Support:** Resource scarcity, prerequisites, timing windows, competing conversions, and market/conversion opportunities make a unit of resource non-equivalent across states.

**Counterexample:** In a state with no feasible alternative use before the horizon, the marginal value may collapse toward its immediate exchange value.

**Adjudication:** `PROBABLE` with explicit horizon and feasibility conditions.

**AEGIS requirement:** Resource ledger must include demand, reservation, projection, and alternative conversion value.

## AX-004 — Production as capability pipeline

**Claim:** Production is downstream of strategic demand and upstream of future capability.

**Counterexample:** Emergency production can be selected from immediate threat without a fully formed long-horizon plan. This does not invalidate the pipeline; it establishes that the objective can be survival/stabilization and that the pipeline can operate at short horizon.

**Adjudication:** `PROBABLE`.

**AEGIS requirement:** Model capacity, queue, throughput, prerequisites, reinforcement, and replacement—not only train commands.

## AX-005 — Transition control

**Claim:** Strong play depends on entering favorable transitions and denying unfavorable ones.

**Hidden variables:** opponent's actual objective and preparation state.

**Counterexample:** Some engagements are locally decisive without requiring meaningful strategic transition control.

**Adjudication:** `PROBABLE`, especially at macro/strategic horizon.

## AX-006 — Probabilistic opponent model

**Claim:** Opponent modeling should preserve alternatives rather than force one deterministic prediction.

**Independent rationale:** Partial observability makes multiple hidden states compatible with the same observation.

**Counterexample:** When the opponent's state is completely observable and deterministic, a distribution is unnecessary.

**Adjudication:** `PROBABLE` for partially observed play; not a universal computational requirement.

**AEGIS requirement:** Belief records require support, contradiction, confidence, alternatives, and age.

## AX-007 — Enemy commitment taxes

**Claim:** Responses can be evaluated by the costs they impose on enemy commitments.

**Critical refinement:** A tax is not inherently good. It is strategically valuable only when imposed cost exceeds the response's opportunity and exposure cost or advances a superior objective.

**Adjudication:** `PROBABLE` as an evaluation lens, not a standalone optimization criterion.

## AX-008 — Value of information

**Claim:** Information has value when it changes expected decision quality.

**Refinement:** The correct conceptual expression is:

`VOI = E[best achievable outcome after information] - E[best achievable outcome now] - acquisition cost`

Acquisition cost includes time, scout risk, resource cost, opportunity cost, and delayed action.

**Counterexample:** If all feasible actions have the same value regardless of the information, VOI is approximately zero.

**Adjudication:** `PROBABLE`.

## AX-009 — Initiative as strategic resource

**Claim:** Initiative changes who must respond.

**Critical refinement:** Initiative is not synonymous with attacking first. A defender can possess initiative if their threat, positioning, or information forces the opponent into constrained responses.

**Adjudication:** `PROBABLE`.

**Measurement:** response demand, response deadline, action-set restriction, retained alternatives.

## AX-010 — Failure signatures

**Claim:** Major commitments require explicit failure recognition and recovery.

**Counterexample:** A trivial low-cost action may not justify explicit failure machinery.

**Adjudication:** `CONTEXT_DEPENDENT` by commitment importance.

**AEGIS requirement:** Every consequential commitment should carry expected result, warning signature, failure signature, abort condition, and fallback objective.

## AX-011 — Separation of epistemic/control states

**Claim:** Observation, belief, classification, objective, authorization, execution, and verification must not be collapsed.

**Support:** This is partly architectural rather than strategic. Collapsing these states creates epistemic errors and makes recovery ambiguous.

**Adjudication:** `PROBABLE`; architectural requirement for robust autonomous control.

## AX-012 — Position-dependent capability

**Claim:** Geometry changes capability value.

**Counterexample:** Some capabilities are nearly position-invariant within a local region or time horizon.

**Adjudication:** `PROBABLE`, conditional on geographic dependence.

## AX-013 — Commitment destroys option value

**Claim:** Strategic commitment should include transition and option cost.

**Refinement:** Option loss is not always negative; a commitment can deliberately sacrifice flexibility to obtain a superior irreversible advantage.

Thus:

`commitment_value = expected_gain + option_gain/loss + denial_value - total_commitment_cost`

**Adjudication:** `PROBABLE`.

## AX-014 — Temporal hysteresis

**Claim:** Reactive strategic controllers need hysteresis where observations and consequences operate on different timescales.

**Counterexample:** A perfectly synchronized instantaneous controller with no noisy observations would not need hysteresis.

**Historical support:** Strong through timer/self-disable/reset patterns.

**Adjudication:** `PROBABLE`, especially for reactive rule systems.

## AX-015 — Retreat preserves option value

**Claim:** Withdrawal can preserve strategic value.

**Critical boundary:** Retreat can also surrender map control, initiative, resources, or timing. It is not inherently beneficial.

**Adjudication:** `CONTEXT_DEPENDENT`.

**Decision test:** compare expected future capability after withdrawal against expected value of continued engagement, including objective loss and exposure.

## AX-016 — Counter transition requirements

**Claim:** Countering an enemy transition can outperform countering visible units.

**Counterexample:** When the immediate visible force is already decisive, transition prediction may add little value.

**Adjudication:** `PROBABLE` for macro/strategic counterplay.

## AX-017 — Resource allocation follows demand

**Claim:** Gather allocation should respond to strategic demand rather than static percentages.

**Counterexample:** Stable fixed allocations can be near-optimal in constrained, repetitive states and can be useful as priors.

**Adjudication:** `PROBABLE` as adaptive-controller principle; static ratios remain valid fallback priors.

## AX-018 — Failure is evidence

**Claim:** Failed actions should update beliefs.

**Critical refinement:** Failure only updates a belief to the extent that the outcome was diagnostic. A failure caused by an unrelated stochastic event should not strongly invalidate the underlying hypothesis.

**Adjudication:** `PROBABLE`.

**AEGIS requirement:** Failure records need causal attribution and diagnostic confidence.

## AX-019 — Compression of high-dimensional state

**Claim:** Historical rule systems compress observations into reusable strategic variables.

**Evidence:** Strong historical pattern.

**Generalization boundary:** This explains a design pattern, not necessarily the sole reason for every state variable.

**Adjudication:** `PROBABLE` meta-knowledge.

## AX-020 — Timers/resets as control primitives

**Claim:** Timers, self-disable patterns, resets, and restart states can stabilize reactive control.

**Critical refinement:** Individual timer instances can instead encode pacing, cooldown, sequencing, or engine workarounds. The control interpretation must be established per subsystem.

**Adjudication:** `PROBABLE` meta-principle; `ENGINE_SPECIFIC` when tied to substrate semantics.

# 6. Counterexample library

Pass 5 establishes a reusable adversarial test family.

### CEX-01 — Mass without reinforcement
A numerically larger army has poor reinforcement distance and production capacity. Smaller local force may possess superior effective capability.

**Tests:** military-count fallacy.

### CEX-02 — Resource abundance without production
Large stockpiles exist, but insufficient production capacity prevents timely conversion.

**Tests:** resource-only optimization.

### CEX-03 — Production without resources
Many production buildings exist, but resource throughput cannot sustain queues.

**Tests:** infrastructure-only power model.

### CEX-04 — Strong counter, wrong timing
The nominal counter is superior but completes after the enemy's timing window.

**Tests:** static counter tables.

### CEX-05 — Strong army, bad position
An army wins in open terrain but is trapped, denied reinforcement, or unable to access the relevant objective.

**Tests:** position-independent capability models.

### CEX-06 — Information that arrives too late
Perfect scouting arrives after the decision deadline.

**Tests:** information-without-time models.

### CEX-07 — Correct hypothesis, nondiagnostic failure
A strategically sound action fails because of an unrelated execution event.

**Tests:** naive failure-as-proof updating.

### CEX-08 — Retreat destroys the objective
Withdrawal preserves army mass but abandons the only critical resource or position.

**Tests:** retreat-as-automatic-preservation models.

### CEX-09 — Commitment improves position
A commitment destroys optionality but creates an irreversible advantage whose value exceeds the flexibility sacrificed.

**Tests:** simplistic optionality maximization.

### CEX-10 — Initiative without conversion
An actor forces repeated reactions but gains no economic, military, positional, or timing advantage.

**Tests:** initiative treated as intrinsically valuable.

### CEX-11 — Tax at excessive cost
A response imposes a large enemy tax but costs more than the enemy commitment is worth.

**Tests:** conversion-tax maximization without response-cost accounting.

### CEX-12 — Multiple equivalent transitions
Several distinct transitions accomplish the same objective at similar expected value.

**Tests:** single-plan opponent/controller assumptions.

### CEX-13 — Hidden transition
The opponent's visible composition remains unchanged while infrastructure/resource allocation indicates a different transition.

**Tests:** unit-count-only opponent models.

### CEX-14 — Stale observation
A previously accurate enemy classification persists after the opponent changes state.

**Tests:** belief aging.

### CEX-15 — Oscillation
Noisy observations alternate between two strategy classifications faster than either strategy can mature.

**Tests:** hysteresis necessity.

# 7. New concepts promoted by Pass 5

Pass 5 adds several concepts that Pass 4 did not sufficiently formalize.

## 7.1 Feasibility set

Optimization must occur only after impossible or strategically unreachable transitions are excluded.

`feasible_actions(S,t,H) -> admissible action set`

The feasibility set is conditioned by resources, production, prerequisites, geography, travel time, technology, population, information, and decision deadline.

## 7.2 Best alternative

Every meaningful decision should be compared against the strongest materially feasible alternative—not against a zero-action baseline alone.

`regret(action) = value(best_feasible_alternative) - value(action)`

This makes opportunity cost operational.

## 7.3 State value versus transition value

A state may be mediocre in isolation but valuable because it enables a superior transition. Conversely, a superficially powerful state may be strategically poor because it blocks future conversion.

`StrategicValue = StateValue + TransitionValue + OptionValue + DenialValue + InformationValue`

The terms are conceptual and may interact nonlinearly.

## 7.4 Reversibility

Commitments should be classified by exit cost:

`reversible -> recoverable -> expensive_to_reverse -> effectively_irreversible`

Reversibility changes appropriate confidence thresholds and reserve requirements.

## 7.5 Substitutability

An objective may have multiple capability solutions. A mature controller must search a set of substitutions rather than assume one canonical build.

## 7.6 Diagnosticity

Not every observation or failure is equally informative.

`diagnosticity(outcome, hypothesis) = expected belief separation produced by the outcome`

This prevents overreacting to noisy or nondiagnostic events.

## 7.7 Robustness

Expected-value maximization is insufficient when state estimates are uncertain. A robust action retains acceptable performance across plausible hidden states.

Conceptually:

`robust_value(a) = E[V(a)] - uncertainty_penalty - tail_risk`

This is a research construct, not a calibrated formula.

## 7.8 Action-set restriction

Initiative and denial can be represented as changes to the opponent's feasible action set, not merely as positive score.

`ΔDecisionSet = feasible_actions_before - feasible_actions_after`

This provides a more measurable interpretation of strategic pressure.

## 7.9 Dependency graph

Every capability should eventually expose a dependency graph:

`objective <- capability <- composition <- production <- infrastructure/resources/technology/position/time`

This allows the controller to attack prerequisites rather than symptoms.

## 7.10 Horizon

Every strategic claim must declare a time horizon. The correct action can differ at 20 seconds, 2 minutes, and 10 minutes.

## 8. Causal versus correlational evidence

A recurring danger is confusing repeated association with causation.

For example:

`enemy cavalry observed -> own anti-cavalry production increases`

does not establish:

`cavalry observation causes optimal anti-cavalry production`.

The historical implementation may encode a heuristic, matchup convention, difficulty compensation, or engine limitation.

Pass 5 therefore requires causal questions:

- If the input changed while everything else remained approximately constant, would the decision change?
- If the decision changed, would the world-state outcome change?
- Is the relationship mediated by a hidden prerequisite?
- Is the effect robust across map, civilization, age, and economy?
- Does the relationship reverse under a changed objective or horizon?

## 9. Universal law versus conditional heuristic

A useful classification test is:

### Universal candidate
The relationship follows from mechanics or necessary structure and survives meaningful domain changes.

### Conditional principle
The relationship is broadly valid but only under identifiable conditions.

### Heuristic
The relationship is an efficient approximation that trades exactness for computational simplicity.

### Historical artifact
The relationship exists because of a particular implementation or historical context.

This distinction is essential for preserving the designer's thinking without inheriting obsolete assumptions.

## 10. Measurement ontology

A strategic concept is not runtime-ready merely because it has a definition.

Each concept should eventually map to:

`concept -> observable inputs -> derived variables -> uncertainty -> decision relevance -> measurement frequency -> expiration -> validation`

Example:

**Timing window**

Observable inputs:
- current time;
- preparation progress;
- enemy preparation evidence;
- travel time;
- production completion;
- technology completion;
- estimated reaction time.

Derived:
- earliest feasible arrival;
- enemy response deadline;
- capability differential;
- expected window duration.

Uncertainty:
- hidden enemy production;
- unseen resource allocation;
- pathing/execution variance.

Decision relevance:
- whether to commit now, scout, delay, or switch transition.

## 11. Strategic evaluation must remain non-additive until proven otherwise

Pass 4 used a linear conceptual score. Pass 5 establishes a warning: many strategic variables interact multiplicatively or conditionally.

Examples:

- military capability may be nearly worthless without position;
- technology may be worthless without the composition it upgrades;
- production capacity may be worthless without resource throughput;
- information may be worthless after the decision deadline;
- initiative may be worthless without conversion;
- optionality may be worth sacrificing for an irreversible advantage.

Therefore the future evaluator should begin with a structured factor graph or dependency model rather than assume a simple weighted sum.

## 12. Opponent modeling as constrained hypothesis generation

The opponent model should not attempt to predict every future action.

It should generate hypotheses constrained by:

`observed evidence + known mechanics + resource feasibility + production feasibility + timing + map geometry`

For each hypothesis:

- evidence;
- prior plausibility;
- feasibility;
- required future commitments;
- predicted observations;
- vulnerabilities;
- counter-transition;
- falsifying evidence.

This converts opponent modeling from speculative storytelling into constrained inference.

## 13. Strategic loop after Pass 5

The refined loop is:

```text
WORLD
  ↓
OBSERVATION
  ↓
STATE ESTIMATION
  ↓
BELIEF / HYPOTHESES
  ↓
OBJECTIVE PRIORITIZATION
  ↓
FEASIBILITY FILTER
  ↓
TRANSITION GENERATION
  ↓
COUNTERFACTUAL / BEST-ALTERNATIVE TEST
  ↓
ROBUST EVALUATION
  ↓
COMMITMENT
  ↓
AUTHORIZED EXECUTION
  ↓
VERIFICATION
  ↓
OUTCOME / FAILURE SIGNATURE
  ↓
DIAGNOSTIC UPDATE
  ↓
NEW OBSERVATION
```

This is the current strategic control model.

## 14. What Pass 5 does NOT establish

Pass 5 does not yet establish calibrated values for:

- capability strength;
- resource marginal values;
- exact conversion-tax weights;
- optimal scouting thresholds;
- universal timing-window durations;
- combat exchange coefficients;
- production throughput coefficients;
- map-control valuation;
- uncertainty penalties;
- robust-risk coefficients;
- Byzantine-specific strategic weights.

These require empirical work, replay analysis, game-state extraction, and eventually controlled bot experiments.

## 15. Required empirical program

The next research stage should build datasets around **decision opportunities**, not merely match outcomes.

Each sample should contain:

- state snapshot;
- observations available at decision time;
- belief distribution;
- objective;
- feasible transitions;
- chosen action;
- alternatives;
- predicted outcome;
- actual outcome;
- failure signature if applicable;
- opponent response;
- resource delta;
- capability delta;
- map/position delta;
- timing delta;
- subsequent state.

This makes strategic learning causal rather than merely statistical.

## 16. Publication and provenance boundary

The uploaded `AiBuilder.per` is recognized as stock tooling intended to help users construct AI scripts. It is valuable as **historical/tooling context**, especially for understanding how stock authors exposed configurable phases, resource allocations, caps, prerequisites, infrastructure limits, and strategy parameters. It is not a source to copy wholesale into AEGIS.

The publication rule remains:

`small attributed exhibit -> explanation -> independent abstraction -> validation`

Never substitute copied stock implementation for understanding.

The same rule applies to Promisory and other historical/vendor-derived material. Failed experimental derivatives are not strategic evidence merely because they contain familiar names or concepts.

## 17. Six-month return standard

A future engineer returning to this project should be able to reconstruct the entire argument without relying on memory.

At minimum, they must be able to answer:

1. Why did Pass 5 exist?
2. What did Pass 4 claim?
3. Which claims survived and under what conditions?
4. Which claims were weakened?
5. Which counterexamples were deliberately constructed?
6. What concepts were added?
7. Which concepts remain hypotheses?
8. What evidence would falsify each major claim?
9. What measurements are required?
10. What empirical work comes next?
11. What source material is evidence and what material is excluded?
12. What should AEGIS eventually implement—and what is deliberately not justified yet?

If those questions cannot be answered from the repository, Pass 5 is incomplete.

## 18. Current adjudication

Pass 5 materially strengthens the ontology. The strongest conclusions are not that every Pass-4 statement is a universal law, but that a coherent family of conditional strategic relationships exists:

`partial observability + constrained resources + production capacity + spatial geometry + temporal deadlines + opponent adaptation -> state-dependent strategic decision making`

The most important AEGIS consequence is therefore methodological:

> **Do not build the bot from strategic slogans. Build a measurable state model whose hypotheses can be challenged, whose commitments have explicit alternatives and failure signatures, and whose strategic laws carry their domains of validity.**

Pass 5 should be considered the boundary between **ontology construction** and **empirical strategic science**.

The next stage is not another round of increasingly elaborate prose. It is to operationalize the validated ontology into measurable variables, replay-derived datasets, causal experiments, and decision records—while preserving the historical reasoning that motivated each abstraction.
