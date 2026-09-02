# HD Source Snippet Casebook — Pass 4

## Purpose

This casebook defines how historical source excerpts may be used to explain generalized strategic concepts without publishing or reconstructing the historical source tree.

The source is an exhibit. The generalized idea is the knowledge.

## Case 1 — State compression

### Pattern

A complex observation is converted into a compact state variable and later rules consume that state.

### Why the pattern matters

The programmer is creating a reusable symbolic vocabulary. Hundreds of downstream decisions can reason about a classification instead of repeating the complete observation predicate.

### Generalized ontology

`OBSERVATION -> DERIVED_STATE -> BELIEF/STRATEGIC_STATE`

### AEGIS requirement

Every derived state should have provenance, owner, update policy, confidence, and legal consumers.

## Case 2 — Resource reservation

### Pattern

A resource-control state protects resources for a future strategic conversion.

### Strategic interpretation

The resource is not economically equivalent to every other possible expenditure. Its value depends on what it can enable next.

### Generalized ontology

`RESOURCE -> RESERVATION -> COMMITMENT -> CAPABILITY`

### AEGIS requirement

Represent resource demand and reservation explicitly. A unit being affordable does not mean buying it is strategically optimal.

## Case 3 — Timer-governed state

### Pattern

A strategic or tactical state is paired with delayed or periodic reassessment.

### Strategic interpretation

The controller needs temporal hysteresis because immediate observations do not always reveal the consequences of a commitment.

### Generalized ontology

`COMMITMENT -> TIMING_WINDOW -> REASSESSMENT`

### AEGIS requirement

Timing should be semantic: preparation time, reaction time, persistence, expiry, and reassessment condition.

## Case 4 — One-shot transition

### Pattern

A rule performs a state-changing event and disables itself.

### Strategic interpretation

A persistent predicate has been turned into an event with implicit completion semantics.

### Generalized ontology

`TRIGGER -> TRANSITION -> COMPLETION`

### AEGIS requirement

Represent lifecycle explicitly: pending, authorized, executing, acknowledged, failed/recovered.

## Case 5 — Attack/retreat state

### Pattern

Offensive state, retreat state, reset behavior, and later restart are represented separately.

### Strategic interpretation

Tactical contact is not identical to strategic success/failure. Preserving surviving capability can preserve future options.

### Generalized ontology

`CAPABILITY -> COMMITMENT -> ENGAGEMENT -> FAILURE/SUCCESS -> RECOVERY`

### AEGIS requirement

Track force preservation, objective validity, retreat reason, and re-entry conditions separately.

## Case 6 — Enemy commitment inference

### Pattern

Observed enemy infrastructure/composition/technology contributes to an enemy strategy classification.

### Strategic interpretation

The controller is attempting to infer what the opponent can afford and is likely to require next.

### Generalized ontology

`OBSERVATION -> BELIEF -> EXPECTED_TRANSITION -> COUNTER`

### AEGIS requirement

Opponent modeling must include alternatives and confidence rather than a single irreversible label.

## Publication rule

When a source snippet is used in public documentation:

1. keep it short and isolated;
2. identify the historical source and context;
3. explain the excerpt's purpose;
4. do not publish surrounding implementation unnecessarily;
5. do not publish large contiguous source sections;
6. spend more documentation space on analysis than quotation;
7. derive a general concept independent of the excerpt;
8. clearly label inference versus mechanical fact;
9. connect the concept to AEGIS architecture;
10. never use a snippet as a substitute for the full historical artifact.

The objective is educational and analytical preservation of ideas, not redistribution of the source implementation.
