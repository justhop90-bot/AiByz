# AEGIS Knowledge Preservation Standard

## Purpose

This document defines the minimum standard for turning research into durable institutional knowledge.

The project does not measure research quality by source-code volume. It measures it by **recoverable reasoning**.

## The atomic research object

The preferred unit is a **decision/control event**:

`observation -> interpretation -> state change -> authority consequence -> action -> expected world change -> observation`

A source line is evidence. A defrule is an implementation unit. The control event is the reasoning unit.

## Required record

Every important recovered behavior should record:

- `id`
- `source`
- `source_location`
- `evidence_type`
- `observed_inputs`
- `observed_reads`
- `observed_writes`
- `observed_actions`
- `temporal_guards`
- `state_transition`
- `functional_role`
- `strategic_role`
- `designer_logic`
- `alternative_explanations`
- `counterevidence`
- `failure_signature`
- `engine_constraints`
- `generalization`
- `AEGIS_abstraction`
- `implementation_requirement`
- `confidence`
- `status`

## Five reconstruction levels

### Level 1 — Mechanical
What does the machine do?

### Level 2 — Functional
What subsystem behavior does the event implement?

### Level 3 — Control
What state transition and authority relationship does it create?

### Level 4 — Strategic
What game-theoretic or economic purpose does the behavior serve?

### Level 5 — Designer model
What problem was the programmer apparently solving, what constraints shaped the solution, and what tradeoff did the implementation accept?

A mature record should reach Level 5 for high-value behaviors.

## Counterfactual requirement

For major findings, ask:

> If this rule/event did not exist, what decision would become impossible, unstable, delayed, or less robust?

This distinguishes meaningful architecture from incidental code.

## Negative evidence

Absence matters. Record when:

- an expected writer does not exist,
- a subsystem reads state but does not own it,
- a timer is present where continuous reaction would seem possible,
- a command is issued without completion verification,
- a historical implementation contains an abandoned experiment,
- or a seemingly obvious capability is never attempted.

Negative evidence can reveal the boundaries of the original design.

## Source-derived versus generalized knowledge

The repository may preserve **knowledge about code** without becoming a public mirror of the code.

Preferred publication order:

1. identify source and provenance;
2. publish only the smallest useful evidence exhibit;
3. explain the behavior in original words;
4. generalize the principle;
5. express the AEGIS abstraction independently;
6. derive an implementation requirement;
7. validate independently.

## Snippet discipline

A snippet should be short enough that its purpose is obvious. Surround it with explanation. Never publish a large contiguous historical implementation merely because it is educationally interesting.

A strong exhibit has the form:

**Claim → tiny excerpt → annotation → interpretation → general principle → AEGIS design consequence.**

## Knowledge graph rule

Important records should eventually connect:

`historical observation -> repeated pattern -> implicit principle -> strategic principle -> general AoE2 law -> AEGIS abstraction -> native constraint -> implementation requirement -> empirical test`

## Completion test

A knowledge item is complete only when a future engineer can use it to answer:

- What happened?
- Why do we believe it?
- Why did the original designer likely do it?
- What else could explain it?
- When does it fail?
- What does AEGIS keep?
- What does AEGIS deliberately reject?
- How can the claim be tested?
