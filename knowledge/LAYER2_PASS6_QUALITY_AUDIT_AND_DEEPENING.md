# Layer 2 Pass 6 — Second-Order Quality Audit and Deepening

## Purpose

The first Pass-6 draft converted strategic concepts into operational constructs. This audit deliberately assumes that first pass is insufficient.

The question is not whether variables have names and formulas. The question is whether those variables are **valid scientific measurements** that a future engineer can compute from real games without hindsight leakage, construct confusion, selection bias, or unjustified causal attribution.

The six-month standard is:

> A returning researcher must be able to understand not only what was measured, but why the measurement should represent the intended construct, what could corrupt it, and how to discover that corruption.

## 1. Defects found in first-pass operationalization

### 1.1 Proxy validity was under-specified

An observable proxy is not automatically a valid measurement of a latent strategic construct.

For example:

`army count -> capability`

is useful but incomplete.

A valid construct requires an explicit mapping:

`proxy -> construct hypothesis -> assumptions -> known failure modes -> validation test`.

### 1.2 Temporal aggregation can destroy causality

A measurement computed over a long interval can hide the sequence that produced the outcome.

Strategic variables therefore require a declared temporal resolution:

`instantaneous | event-window | transition-window | phase | game`.

### 1.3 Hindsight leakage is a major threat

Any variable derived using information observed after a decision can contaminate evaluation of that decision.

The corpus must maintain strict temporal cutoffs.

### 1.4 Selection bias can manufacture strategic laws

If the corpus contains mostly decisive or successful events, measured relationships can appear stronger than they are.

Failed, ambiguous, interrupted, and non-decisive opportunities are required.

### 1.5 Causal attribution remains harder than correlation

An action occurring immediately before an outcome is not sufficient evidence that it caused the outcome.

Concurrent actions, delayed effects, prior commitments, opponent actions, and map conditions must be represented.

### 1.6 Measurement scale was missing

A variable must declare whether it is:

- nominal;
- ordinal;
- count;
- rate;
- duration;
- probability;
- interval;
- ratio;
- latent estimate.

This affects permissible mathematical operations and statistical interpretation.

### 1.7 Calibration target was under-specified

A prediction is not calibrated merely because its average error is low. Probability estimates must be compared with empirical frequencies; continuous estimates require appropriate error and discrimination metrics.

# 2. Construct validity protocol

Every operational variable now requires four forms of validity.

## 2.1 Face validity

Does the measurement plausibly represent the intended concept?

Useful but weak.

## 2.2 Content validity

Does the variable include the important dimensions of the construct rather than one convenient proxy?

Example: capability should not reduce to army count when readiness, position, reinforcement, and counters materially matter.

## 2.3 Criterion validity

Does the variable predict or explain an independently measured outcome?

Example:

`predicted production latency -> observed usable-capability arrival time`.

## 2.4 Construct validity

Does the variable behave as theory predicts across related and contrasting situations?

Example:

initiative should correlate with response demand but should not necessarily correlate with raw attack frequency.

# 3. Measurement invariance

A strategic construct should not silently change meaning between contexts.

Before comparing values across:

- civilizations;
- maps;
- game phases;
- unit classes;
- matchups;
- players;

verify that the construct has the same semantic interpretation.

If it does not, use a context-conditioned variable rather than falsely comparing unlike quantities.

# 4. Temporal contract

Every measurement must declare its horizon.

```text
T0        decision instant
T1        immediate outcome
T2        short-term transition
T3        strategic horizon
T4        terminal/game horizon
```

A decision may be:

`bad at T1, neutral at T2, strongly positive at T3`.

Therefore no single outcome horizon should be treated as the universal ground truth.

# 5. Information cutoff contract

For each decision event define:

`information_cutoff = all information legitimately available before action selection`.

Any feature whose timestamp exceeds the cutoff is prohibited from `AS_KNOWN_THEN` evaluation.

Derived quantities must inherit the latest source timestamp.

This prevents subtle leakage through derived state.

# 6. Missingness is information

Missing observations have multiple causes:

- not visible;
- not recorded;
- not measurable;
- destroyed evidence;
- parser limitation;
- genuinely absent object.

These must not be collapsed into zero.

Required missingness states:

`KNOWN_ZERO | OBSERVED_POSITIVE | UNKNOWN | NOT_VISIBLE | NOT_APPLICABLE | PARSER_MISSING`.

This is particularly important for opponent modeling.

# 7. Observation quality

Every observation should carry:

```text
SOURCE
TIMESTAMP
VISIBILITY
PRECISION
CONFIDENCE
FRESHNESS
CORROBORATION
```

A low-quality observation should not have the same update weight as a direct, fresh, corroborated observation.

# 8. Causal graph discipline

For important measurements, preserve a causal graph rather than only a feature list.

Example:

```text
MAP
 ↓
RESOURCE_ACCESS
 ↓
ECONOMIC_FLOW
 ↓
PRODUCTION_CAPACITY
 ↓
CAPABILITY
 ↓
OBJECTIVE_PROGRESS
```

But the graph may also contain:

```text
OPPONENT_ACTION -> RESOURCE_ACCESS
OPPONENT_ACTION -> CAPABILITY
```

If both paths exist, naive attribution of objective progress to our action may be wrong.

# 9. Intervention versus observation

A replay gives observational evidence.

A controlled bot experiment gives intervention evidence.

These answer different questions.

Observational evidence can establish:

`X commonly precedes Y`.

Intervention can better test:

`changing X causes Y to change`.

The repository must preserve this distinction.

# 10. Counterfactual identifiability

Decision regret requires a counterfactual:

> What would have happened under the best feasible alternative?

That outcome is usually unobserved.

Therefore regret is initially a **model-based estimate**, not a direct fact.

The record must include:

- alternative;
- assumptions;
- model used;
- uncertainty range;
- confidence;
- sensitivity to assumptions.

A future AEGIS system must not treat estimated regret as historical truth.

# 11. Sensitivity analysis

When a conclusion depends on uncertain quantities, vary them.

Example:

If an attack is judged superior only when enemy reinforcement time is assumed to be 22 seconds rather than 27 seconds, the decision should be marked sensitive.

Required classifications:

`ROBUST | MODERATELY_SENSITIVE | HIGHLY_SENSITIVE | INDETERMINATE`.

# 12. Calibration science

Probability-bearing constructs require calibration tests.

Examples:

- opponent-transition probability;
- capability success probability;
- timing-window probability;
- belief confidence.

Useful eventual metrics include:

- Brier score;
- log loss;
- reliability diagrams;
- calibration error;
- discrimination/precision-recall where appropriate.

Continuous predictions require domain-appropriate metrics such as:

- MAE;
- RMSE;
- median absolute error;
- interval coverage;
- rank correlation when ordering rather than magnitude is the target.

No single metric should become universal.

# 13. Baselines are mandatory

Every new strategic construct requires a baseline.

Examples:

`dynamic resource allocation vs fixed ratio`

`transition-aware counter vs unit-reactive counter`

`probabilistic opponent model vs deterministic label`

`capability estimate vs unit count`

`VOI-guided scouting vs fixed scouting schedule`.

Without a baseline, “improvement” is undefined.

# 14. Ablation protocol

A mature strategic experiment should remove one construct while holding the remainder as constant as practical.

Examples:

- remove timing from capability valuation;
- remove position;
- remove belief alternatives;
- remove resource reservations;
- remove transition prediction;
- remove failure diagnostics.

If removing a construct produces no meaningful degradation under its declared domain, its runtime complexity requires reconsideration.

# 15. Negative controls

Experiments need cases where a construct should have little or no effect.

Examples:

- VOI when all actions are equivalent;
- position valuation in a locally homogeneous combat region;
- transition prediction when the opponent's state is fully observable;
- optionality cost when all future alternatives are dominated.

A model that predicts strong effects where theory predicts none is suspect.

# 16. Distribution shift

A model calibrated on one corpus can fail elsewhere.

Track:

- map distribution;
- civilization distribution;
- skill distribution;
- game length;
- strategic style;
- patch/version;
- opening distribution.

Future empirical claims should declare their training/evaluation domain.

# 17. Confounder register

The empirical corpus should explicitly record major confounders:

- civilization advantage;
- map advantage;
- starting resource variance;
- execution quality;
- scouting quality;
- opponent skill;
- prior damage;
- simultaneous engagements;
- hidden technology;
- random events/mechanics;
- game-state selection effects.

# 18. Decision quality is not outcome quality

A rational decision can lose.

An irrational decision can win.

Therefore the research corpus should distinguish:

`decision quality`

from:

`realized outcome`.

The first asks whether the action was justified given available information and feasible alternatives.

The second asks what actually happened.

This is one of the most important protections against learning the wrong lesson from replay results.

# 19. Strategic construct families

Pass 6 now groups measurements into six families.

### A. State estimation

- resource deficit;
- production capacity;
- capability state;
- position;
- information freshness;
- belief confidence.

### B. Prediction

- opponent transition;
- production latency;
- timing window;
- capability reliability;
- sustainability.

### C. Choice quality

- feasible alternatives;
- decision regret;
- opportunity cost;
- optionality;
- robustness.

### D. Interaction

- initiative;
- conversion tax;
- response demand;
- transition denial.

### E. Learning

- failure diagnosticity;
- belief update;
- calibration;
- causal attribution.

### F. Control health

- commitment conflicts;
- decision budget;
- execution delay;
- verification delay;
- recovery success.

# 20. Operational maturity gate

A construct may enter experimental runtime only when it reaches at least:

`L4 replay-measurable + explicit uncertainty + declared horizon + known failure modes + baseline + validation target`.

It should not enter trusted runtime until it also demonstrates:

`predictive validity + calibration/accuracy + robustness + reproducibility + no material hindsight leakage`.

# 21. Six-month reconstruction map

A returning engineer should be able to navigate:

```text
PASS 4
  what concepts exist
       ↓
PASS 5
  which concepts survived challenge
       ↓
PASS 6
  how each surviving concept can be measured
       ↓
REPLAY CORPUS
  whether measurements predict reality
       ↓
CALIBRATION
  numerical reliability
       ↓
CONTROLLED EXPERIMENTS
  causal confidence
       ↓
POLICY
  decision usefulness
       ↓
RUNTIME
  trusted autonomous use
```

## Final determination

Pass 6 is materially stronger after this second-order review because it now treats operationalization as **measurement science**, not merely instrumentation.

The most important new constraints are:

1. construct validity;
2. temporal contracts;
3. information cutoffs;
4. explicit missingness;
5. observation quality;
6. causal graphs;
7. intervention/observation separation;
8. counterfactual uncertainty;
9. sensitivity analysis;
10. probability calibration;
11. baselines;
12. ablations;
13. negative controls;
14. distribution-shift tracking;
15. confounder accounting;
16. separation of decision quality from outcome quality.

These should be treated as permanent methodological requirements for subsequent Layer-2 empirical work.
