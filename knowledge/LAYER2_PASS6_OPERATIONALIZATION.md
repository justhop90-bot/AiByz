# Layer 2 — Pass 6: Strategic Operationalization

## 0. Purpose

Pass 5 established that the Layer-2 ontology is useful only if its claims can be measured, falsified, and eventually implemented. Pass 6 converts the surviving strategic concepts into **operational variables** without prematurely turning them into hard-coded heuristics.

The governing transformation is:

`strategic concept -> construct definition -> observable proxies -> derived variable -> uncertainty -> decision horizon -> measurement event -> validation target -> runtime requirement`

Pass 6 is therefore the bridge from **strategic theory to empirical strategic science**.

It is not a bot rewrite. It is not parameter tuning. It is not permission to encode every concept as a threshold.

## 1. Six-month requirement

A future engineer must be able to determine:

1. what each strategic variable means;
2. why it exists;
3. which observations feed it;
4. which observations cannot establish it;
5. how stale or contradictory observations affect it;
6. what time horizon it belongs to;
7. what uncertainty it carries;
8. how it changes a decision;
9. what experiment can validate it;
10. what evidence would invalidate it;
11. what runtime capability is required to measure it;
12. which parts remain deliberately unimplemented.

If a variable cannot pass those tests, it is not operationally mature.

# 2. Measurement philosophy

The central distinction is:

`observable != measurable construct != decision variable`

An observation may be directly available while the strategic quantity of interest is latent.

Example:

`observed cavalry count -> estimated mobility capability -> estimated raid threat -> objective-specific response demand`

The controller must preserve this chain rather than pretending the final estimate is a raw fact.

Every derived variable therefore requires provenance.

## Provenance chain

```text
RAW OBSERVATION
   ↓
NORMALIZATION
   ↓
DERIVED FACT
   ↓
ESTIMATE
   ↓
BELIEF / CONFIDENCE
   ↓
DECISION VARIABLE
```

# 3. Canonical operational state

The first operational state vector is:

```text
TIME
PHASE
RESOURCES
ECONOMIC_FLOW
PRODUCTION_CAPACITY
TECHNOLOGY
MILITARY_COMPOSITION
MILITARY_READINESS
MILITARY_POSITION
MAP_CONTROL
INFORMATION_STATE
OPPONENT_BELIEFS
OBJECTIVE_PRIORITY
ACTIVE_COMMITMENTS
THREATS
TIMING_WINDOWS
INITIATIVE
OPTIONALITY
CONSTRAINTS
DECISION_BUDGET
UNCERTAINTY
```

These are domains, not yet numerical coefficients.

# 4. Resource operationalization

Resource state must be decomposed into:

- stock;
- income rate;
- expenditure rate;
- reserved amount;
- committed amount;
- free amount;
- projected stock at horizon H;
- expected demand;
- feasible conversions;
- best alternative conversion;
- scarcity;
- acquisition difficulty;
- uncertainty.

## 4.1 Resource deficit

For a desired conversion C over horizon H:

`deficit(C,H) = required_resources(C,H) - projected_available_resources(H)`

Positive deficit indicates a shortfall. Negative deficit indicates surplus relative to that conversion.

The important point is that deficit is **objective-relative**. There is no universal food deficit independent of what the actor intends to do.

## 4.2 Shadow value

Conceptually:

`shadow_value(resource,H) = marginal strategic value of one additional unit of resource at horizon H`

This must not initially be hard-coded. Early implementation should expose the variable and gather empirical evidence before assigning stable coefficients.

## 4.3 Reservation

A reservation is not simply “saved resource.” It is:

`resource protected because a future commitment has sufficiently high priority or timing sensitivity.`

Operational fields:

- purpose;
- amount;
- release condition;
- priority;
- expiration;
- confidence;
- competing claim.

# 5. Capability operationalization

Capability must become measurable without collapsing back into unit count.

A capability record should contain:

```text
CAPABILITY_ID
OBJECTIVE
REQUIRED_COMPONENTS
CURRENT_MAGNITUDE
READINESS
AVAILABILITY
RELIABILITY
REACH
POSITION_DEPENDENCE
SUSTAINABILITY
REINFORCEMENT_RATE
REPLACEMENT_RATE
PREREQUISITES
COUNTERS
COUNTER_VULNERABILITIES
PREPARATION_TIME
EFFECTIVE_HORIZON
CONFIDENCE
```

## 5.1 Magnitude

How much relevant capability exists?

Magnitude may be represented by composition, production capacity, resource throughput, or other domain-specific measures.

## 5.2 Readiness

How soon can the capability produce its intended effect?

Readiness is distinct from magnitude.

## 5.3 Availability

Nominal capability can be unavailable because units are displaced, damaged, committed elsewhere, blocked, or otherwise unable to contribute to the current objective.

## 5.4 Reliability

Estimated probability of accomplishing the intended task under current conditions.

This should incorporate known counters, position, timing, and uncertainty.

## 5.5 Sustainability

How long can the capability be maintained under current resource and production flow?

A force that can fight for thirty seconds and a force that can sustain pressure for five minutes are not strategically equivalent.

# 6. Production operationalization

Production becomes measurable as throughput and latency.

Required variables:

- production structures;
- active queues;
- available queues;
- production rate;
- resource feed rate;
- prerequisite readiness;
- reinforcement distance;
- reinforcement time;
- replacement rate;
- bottleneck identity;
- queue saturation;
- expected completion time.

## 6.1 Production latency

`production_latency = time from strategic demand declaration to usable capability availability`

This is more strategically useful than train time alone because it includes prerequisites, resource acquisition, infrastructure, training, movement, and readiness.

## 6.2 Bottleneck

A bottleneck is the limiting factor preventing a desired capability from increasing at the required rate.

Potential bottlenecks:

`resources | production slots | prerequisites | technology | population | geography | time`

# 7. Technology operationalization

Technology should be recorded as a transition investment.

Variables:

- acquisition cost;
- research latency;
- prerequisites;
- immediate capability delta;
- future capability delta;
- composition dependency;
- production dependency;
- counter impact;
- timing-window creation;
- alternative investment displaced;
- reversibility.

The measurement target is not “technology researched.”

It is:

`technology -> capability change -> objective impact`.

# 8. Position operationalization

Position must be represented relative to an objective.

Useful measurements include:

- distance to objective;
- distance to reinforcement;
- retreat distance;
- access routes;
- choke value;
- exposure;
- defensive modifiers;
- resource proximity;
- enemy access;
- vision/control contribution.

Position is therefore a **relational state**, not simply `(x,y)`.

# 9. Information operationalization

Information state should track:

```text
OBSERVATION
SOURCE
TIMESTAMP
VISIBILITY
CONFIDENCE
RELEVANCE
EXPECTED DECISION IMPACT
CONTRADICTIONS
AGE
EXPECTED EXPIRATION
```

## 9.1 Value of information

For a decision D:

`VOI(D,I) = E[value(best action after I)] - E[value(best action without I)] - acquisition_cost(I)`

The expression is conceptual until calibrated.

The crucial operational test is whether information changes the feasible or preferred action set.

# 10. Belief operationalization

Beliefs should not be represented as one opaque “enemy strategy” variable.

Minimum belief structure:

```text
HYPOTHESIS
PRIOR_CONFIDENCE
SUPPORTING_EVIDENCE
CONTRADICTORY_EVIDENCE
LAST_UPDATE
AGE
EXPECTED_NEXT_EVENT
REQUIRED_PREREQUISITES
EXPECTED_RESOURCES
EXPECTED_TIMING
EXPECTED_CAPABILITY
VULNERABILITIES
ALTERNATIVE_HYPOTHESES
```

## 10.1 Belief update

A future implementation may use Bayesian or Bayesian-like updating, but the ontology does not require one mathematical estimator yet.

The invariant requirement is:

`new evidence -> confidence revision`,

with update magnitude dependent on evidence quality and diagnosticity.

# 11. Opponent transition operationalization

The opponent model should predict **requirements**, not merely labels.

Example:

```text
OBSERVED INFRASTRUCTURE
      ↓
POSSIBLE CAPABILITY
      ↓
REQUIRED RESOURCES
      ↓
REQUIRED PRODUCTION
      ↓
LIKELY TIMING
      ↓
LIKELY OBJECTIVE
      ↓
VULNERABLE DEPENDENCIES
```

The resulting record should contain:

- current visible capability;
- inferred intended capability;
- candidate transitions;
- probability/confidence;
- required resources;
- required infrastructure;
- preparation time;
- likely commitment;
- vulnerable dependencies;
- alternative interpretations.

# 12. Threat operationalization

Threat is an objective-relative, temporal construct.

```text
THREAT
├── target objective/capability
├── mechanism
├── magnitude
├── probability
├── time-to-impact
├── required enemy capability
├── evidence
├── confidence
├── mitigation options
├── mitigation cost
└── consequence
```

A scalar danger number may still be used for convenience, but it must be derived from typed threats rather than replacing them.

# 13. Timing-window operationalization

A timing window exists when the expected value of an action is materially higher within an interval than outside it.

Fields:

- opening estimate;
- closing condition;
- preparation latency;
- enemy reaction latency;
- capability differential;
- commitment cost;
- miss cost;
- confidence.

The window should be represented as a range, not an unjustified exact timestamp.

# 14. Initiative operationalization

Initiative is measured through **decision pressure**.

Candidate observables:

- opponent response demand;
- response deadline;
- number of viable responses;
- response cost;
- actor's retained alternatives;
- ability to change direction;
- opponent transition delay.

Conceptually:

`initiative_value ≈ opponent decision burden + action-set restriction + tempo advantage - cost of maintaining pressure`

This is deliberately not a final formula.

# 15. Optionality operationalization

Optionality is the value of feasible future choices.

A useful proxy is:

`option_set = {materially feasible future transitions}`

Then:

`optionality ≈ weighted value of feasible alternatives`

The count of options alone is insufficient. Ten worthless options do not equal one decisive option.

Operational fields:

- feasible alternatives;
- expected values;
- resource requirements;
- timing windows;
- reversibility;
- confidence;
- dependencies.

# 16. Commitment operationalization

Every consequential commitment should be recorded as an object:

```text
COMMITMENT
├── actor
├── objective
├── transition
├── start_time
├── expected_duration
├── resources_consumed
├── production_capacity_consumed
├── position_exposure
├── option_set_before
├── option_set_after
├── expected_gain
├── expected_risk
├── exit_condition
├── warning_signature
├── failure_signature
└── recovery_plan
```

This allows post-game analysis of not only whether a commitment succeeded, but whether it was rational **at the time it was made**.

# 17. Counterfactual decision measurement

The central empirical question is:

> Was the selected action better than the strongest feasible alternative given the information available at the decision time?

Therefore every decision-opportunity record should preserve:

`decision_state + information_state + feasible_alternatives + selected_action + outcome`.

Do not evaluate historical decisions using information that was only discovered later unless explicitly performing hindsight analysis.

This distinction is essential for avoiding hindsight bias.

# 18. Decision event schema

The canonical empirical unit is:

```text
DECISION_EVENT
├── event_id
├── replay/game identifier
├── timestamp
├── actor
├── phase
├── observable_state
├── derived_state
├── beliefs
├── objectives
├── threats
├── constraints
├── feasible_actions
├── selected_action
├── expected_transition
├── commitment
├── predicted_outcome
├── actual_outcome
├── opponent_response
├── capability_delta
├── resource_delta
├── production_delta
├── position_delta
├── timing_delta
├── information_delta
├── failure_signature
├── recovery
├── post_state
└── adjudication
```

## 18.1 Decision opportunity versus action

A crucial distinction:

`decision opportunity != executed action`.

The empirical corpus must include cases where an actor **could have chosen differently**.

Otherwise we cannot estimate regret, alternative value, or policy quality.

# 19. Outcome measurement

Outcome should be measured on multiple horizons.

### Immediate
Seconds/minutes:

- units lost;
- damage;
- position change;
- resources consumed.

### Short-term
Next transition:

- production state;
- economy;
- reinforcement;
- technology;
- map control.

### Strategic
Later phase:

- capability advantage;
- transition access;
- denial achieved;
- economic trajectory;
- initiative.

### Terminal
Game-level:

- victory/loss;
- timing of decisive conversion;
- strategic cause if attributable.

A decision may be locally negative and globally correct.

# 20. Attribution discipline

Observed outcome must not automatically be attributed to the immediately preceding action.

Potential confounders:

- concurrent opponent action;
- random map state;
- hidden information;
- execution error;
- unrelated resource event;
- prior commitment;
- delayed effects from earlier decisions.

The corpus should therefore distinguish:

`temporal association` from `causal attribution`.

# 21. Calibration ladder

Operational variables should mature through stages:

```text
L0 — CONCEPT
L1 — NAMED VARIABLE
L2 — OBSERVABLE PROXY
L3 — DERIVED MEASURE
L4 — REPLAY-MEASURABLE
L5 — PREDICTIVE
L6 — CALIBRATED
L7 — POLICY-USEFUL
L8 — RUNTIME-TRUSTED
```

A variable should not jump from L1 to L8 because it “sounds right.”

# 22. Measurement error and uncertainty

Every derived variable has uncertainty.

The corpus should eventually record:

- measurement error;
- missing observations;
- stale observations;
- inference uncertainty;
- model uncertainty;
- execution uncertainty.

This allows AEGIS to distinguish:

`we don't know` from `we know the state is bad`.

# 23. Minimal empirical metrics

The first metrics to implement should be:

1. resource deficit accuracy;
2. production latency prediction error;
3. opponent transition prediction accuracy;
4. belief calibration;
5. timing-window hit/miss rate;
6. initiative/action-set restriction;
7. capability prediction error;
8. decision regret;
9. conversion efficiency;
10. failure-signature detection latency.

These are more valuable than immediately optimizing a large weighted strategic score.

# 24. Experimental design

Experiments should isolate one construct wherever possible.

Bad experiment:

> “Build a smarter bot and see if it wins more.”

Good experiment:

> “Given equivalent starting states, does transition-aware counter selection reduce opponent access to its target capability at equal or lower total commitment cost?”

The latter produces interpretable evidence.

## Required experimental controls

Where feasible:

- matched maps;
- matched civilizations;
- matched starting conditions;
- repeated trials;
- controlled perturbation;
- one primary independent variable;
- predefined success metric;
- predefined falsifier.

# 25. Hindsight control

Replay analysis must preserve the information actually available at the decision point.

A later-observed enemy technology must not be silently inserted into the earlier belief state.

Therefore every empirical decision record has two epistemic views:

`AS-KNOWN-THEN`

and optionally:

`AS-KNOWN-NOW`.

They must never be conflated.

# 26. Runtime measurement contract

Eventually every strategic construct that enters AEGIS requires:

```text
SOURCE OBSERVATIONS
      ↓
VALIDATION
      ↓
DERIVATION
      ↓
CONFIDENCE
      ↓
CONSUMERS
      ↓
DECISION IMPACT
      ↓
POST-ACTION VERIFICATION
```

A measurement without a consumer is instrumentation.

A decision variable without provenance is an undocumented heuristic.

A decision variable without validation is a hypothesis masquerading as architecture.

# 27. What Pass 6 deliberately does NOT do

Pass 6 does not establish:

- universal numerical weights;
- exact strategic utility coefficients;
- universal resource prices;
- universal combat values;
- universal timing windows;
- a single opponent-prediction algorithm;
- a final Bayesian implementation;
- Byzantine-specific policy;
- final runtime thresholds;
- final production logic.

Those require empirical calibration and later doctrine-specific work.

# 28. Resulting research architecture

The strongest current Layer-2 model is now:

```text
WORLD
 ↓
OBSERVATIONS
 ↓
DERIVED FACTS
 ↓
BELIEFS / UNCERTAINTY
 ↓
OBJECTIVE PRIORITY
 ↓
CONSTRAINTS
 ↓
FEASIBLE TRANSITION SET
 ↓
ALTERNATIVE COMPARISON
 ↓
ROBUST STRATEGIC EVALUATION
 ↓
COMMITMENT
 ↓
EXECUTION
 ↓
VERIFICATION
 ↓
OUTCOME
 ↓
CAUSAL ATTRIBUTION
 ↓
BELIEF UPDATE
 ↓
LEARNING
```

This is the operational research loop.

# 29. Pass-6 completion criterion

Pass 6 is complete only when the project possesses a replay-measurable representation for the principal surviving strategic constructs and can answer, for a real decision point:

> What did the actor know, what did it believe, what did it want, what could it actually do, what alternatives existed, what did it choose, what did it commit, what did it expect, what happened, what changed, and what should the evidence teach us?

Until that can be answered repeatedly from actual game records, Layer 2 remains a theory under development.
