# HD AI Forensic Method

## 1. Purpose

The recovered HD AI is treated as a historical engineered control system. The
research question is stronger than "what rules exist?": it is "what model of
AoE2 did the designers hold in their heads, and how did they encode that model
under the constraints of the rule engine?"

The analysis therefore separates implementation from intent while preserving
the relationship between them.

## 2. Levels of reconstruction

### Level A — Mechanical description

Record exact predicates, operators, identifiers, constants, goals, strategic
numbers, timers, actions, loads, rule enable/disable behavior, and source
location.

### Level B — Functional description

State what the rule family accomplishes in game terms: detects a rush, protects
a resource, creates military mass, delays an attack, changes gatherer allocation,
chooses a transition, etc.

### Level C — Control description

Identify inputs, state registers, outputs, feedback, hysteresis, authority,
reset behavior, timing, and interactions with other controllers.

### Level D — Strategic description

Infer the underlying game-theoretic principle: opportunity cost, resource tax,
commitment recognition, capability preservation, tempo management, denial,
information value, transition timing, or risk control.

### Level E — Designer-model description

Ask what simplifying assumptions, practical experience, failure observations,
and engine constraints likely caused the designers to choose this particular
encoding. This is inference and must never be mislabeled as direct author intent.

## 3. Forensic record schema

Each major mechanism should eventually have:

`artifact_id`
`source_hash`
`source_section`
`source_file`
`line_start`
`line_end`
`authors_attribution`
`module_family`
`inputs`
`state_reads`
`state_writes`
`actions`
`timers`
`resource_effects`
`target_effects`
`preconditions`
`postconditions`
`failure_signature`
`reset_path`
`competing_writers`
`downstream_consumers`
`functional_interpretation`
`strategic_interpretation`
`designer_model_hypothesis`
`evidence_strength`
`counterevidence`
`independent_validation`
`AEGIS_generalization`
`implementation_consequence`

## 4. Counterfactual analysis

For every important rule family, ask:

1. What state exists before it fires?
2. What state exists after it fires?
3. What if one predicate is removed?
4. What if the action fails?
5. What if the enemy does the opposite?
6. What other rule now becomes active?
7. What assumption would be violated?
8. Why might the original designer have accepted that tradeoff?

Counterfactuals are especially important for discovering implicit knowledge.

## 5. Human-logic reconstruction

Do not infer intent from a single threshold. Look for repeated choices across
contexts. A principle becomes stronger when the same design pattern appears in
multiple independent subsystems.

Examples of strong recurring motifs include:

- classify enemy state once, then reuse the classification;
- reserve resources for strategically important conversions;
- rate-limit oscillating commands with timers;
- preserve military capability rather than accepting locally favorable trades;
- alter economic allocation when the strategic mode changes;
- distinguish attack permission from attack execution;
- distinguish retreat state from permanent strategic failure;
- use map position as an upstream strategic variable;
- use feasibility/pending-state gates before asynchronous actions.

These are candidate principles, not assumed author statements.

## 6. Negative evidence

Absence matters. If a supposedly central concept has no persistent state, no
writer ownership, no downstream consumer, or no recovery path, document that.
Likewise preserve commented-out experiments, obsolete code, duplicated writers,
and contradictory branches. They reveal development history and constraints.

## 7. Practical reconstruction standard

A future engineer should be able to answer, for any important behavior:

> What activates it? What state does it consume? What state does it create?
> What resources does it protect or spend? What action follows? What timer or
> reset controls it? What other rules compete with it? What happens when it
> fails? What strategic problem was it solving? What evidence supports the
> inferred rationale? And what remains unknown?

If the repository cannot answer those questions, the archaeology is incomplete.
