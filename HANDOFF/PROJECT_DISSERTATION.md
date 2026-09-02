# AEGIS-BYZ — Project Dissertation

## Abstract
AEGIS-BYZ is an attempt to construct a genuinely strategic Byzantine AI for Age of Empires II DE by solving the problem in the correct order. The central thesis is that a strong bot cannot be safely produced by stacking heuristics on an incompletely understood execution substrate. The project therefore proceeds from machine knowledge to strategic knowledge to Byzantine doctrine and only then to runtime implementation.

The intended chain is:

`ENGINE MODEL -> INTERPRETER MODEL -> STRATEGIC MODEL -> BYZANTINE MODEL -> BOT`

The project treats the game engine as a machine to be learned, existing AI as an archaeological record of human strategic engineering, replays as causal measurement instruments, and the eventual bot as a controlled decision system rather than a pile of rules.

## I. The machine must be understood first
The first intellectual problem was not “what build order is strongest?” It was “what machine will execute the bot?” AoE2DE AI is constrained by a native rule engine, facts, goals, strategic numbers, timers, command interfaces, loading boundaries, and execution behavior. A strategy that cannot be expressed and reliably executed by the actual interpreter is not an architecture; it is a wish.

Native investigation therefore distinguishes embedded vocabulary, parser behavior, script usage, diagnostics, native function signatures, callgraph evidence, and behavioral tests. Strings alone are not semantics. A native interface becomes stronger evidence when independently supported by signatures, call sites, script consumption, diagnostics, and runtime behavior.

## II. The historical AI is an archaeological fossil
The HD/2013 AI is valuable because it contains strategic knowledge encoded by its designers. Its importance is not that its implementation should be copied. Its importance is that its rules reveal what experienced programmers considered strategically relevant.

The proper research unit is not a source line. It is a control event:

`observation -> classification -> state write -> authority effect -> action/resource consequence -> temporal guard -> reassessment`

From this we can recover explicit knowledge, implicit strategic principles, and meta-knowledge about why a rule system requires timers, hysteresis, state compression, reset mechanisms, and distributed control.

## III. The designer's recurring mental model
The recovered design repeatedly converts high-dimensional observations into reusable state. Strategy, unit choice, control state, resource control, military level, current age, focus player, target player, attack status, retreat status, threat state, position, and timers form a distributed finite-state/control system.

This system is ugly in places because it is historical engineering. Duplicate writers, obsolete rules, commented experiments, debugging controls, and workarounds are evidence of design evolution. They must be classified before being discarded.

## IV. The strategic abstraction missing from the fossil
The historical system contains strategic knowledge without a clean strategic ontology. AEGIS should extract that ontology rather than inherit the implementation.

The strategic state should include at least:

Economy, Production, Military, Technology, Map, Position, Information, Timing, Infrastructure, Logistics, Reserves, Threats, Commitments, Opportunities, Confidence, Initiative, and Objective.

Units are not the final representation. Capabilities are. Resources are not merely quantities. They have state-dependent marginal value and opportunity cost. Production is not merely a queue. It is a capability pipeline.

## V. Competitive causality
The game is modeled as a causal chain:

`economy -> production -> capability -> map -> resources -> transition -> timing -> initiative -> opponent response`

A decision must therefore be evaluated against both its immediate result and the state it makes possible or impossible later.

## VI. Information and uncertainty
The AI must never know tomorrow's state while pretending it knew it yesterday. Replay reconstruction therefore separates:

KNOWN THEN
BELIEVED THEN
UNKNOWN THEN
KNOWN NOW

Observed state, reconstructed state, and counterfactual state must never be silently merged. Every inference carries evidence, method, confidence, and falsifiers.

## VII. Temporal reasoning
Temporal semantics are a foundational part of strategy. ACTION sequence is strongly correlated with terminal world time across the eight-game calibration corpus and is therefore a probable command-associated temporal coordinate, but its exact native unit remains unproven. SYNC current_time has an explicit parser interpretation as milliseconds from beginning. POSTGAME world_time is a terminal simulation-time observation.

Equal ACTION sequence values form temporal clusters. JSONL serialization order must not be mistaken for causality.

## VIII. Production as strategic capability
Production must be reconstructed as intent, queue command, admission, queue state, start, completion, object birth, availability, deployment, and reinforcement. `DE_QUEUE` is evidence of a queue command, not proof of completion.

The `amount` field exposes commitment magnitude. `object_ids` exposes producer identity. This makes queue capacity, congestion, parallelism, production latency, and bottlenecks measurable.

## IX. The Byzantine doctrine
The Byzantine strategic objective is not simply “counter the enemy.” It is:

**Make every enemy commitment pay a conversion tax.**

The tax can include resources, production capacity, time, map displacement, response latency, transition delay, attention, and lost optionality. The best Byzantine action is therefore not necessarily the one that wins the local exchange. It is the one that converts the opponent's commitment into disproportionate strategic burden.

## X. Decision theory
The eventual decision function should be expressible as:

`STATE + UNCERTAINTY + OBJECTIVE + AVAILABLE ACTIONS -> BEST ACTION + EXPECTED CONSEQUENCE + RISK + FAILURE SIGNATURE + RECOVERY`

Strategic value should account for military, economic, map, technology, production, information, timing, initiative, reserve, exposure, transition cost, replacement cost, economic damage, and uncertainty.

## XI. Learning
Strategic memory should preserve four epistemic layers:

FACT
PATTERN
HYPOTHESIS
OUTCOME / LESSON

Learning is not “change a threshold because we lost.” It is evidence-backed model revision. Failed actions are useful because their failure signatures constrain the model.

## XII. Engineering doctrine
Authority must be explicit. Sensors should be read-only. Planning must not secretly execute. Commands require authorization. Execution must be observable. Completion requires acknowledgment. Failed execution requires recovery or explicit unresolved state.

The architecture should prefer one authoritative writer for critical state over fragmented competing writers. Existing V3 behavior is a strategy fossil, not a template for reproducing distributed ambiguity.

## XIII. Six-month return test
A future engineer must be able to answer:

- What did we know?
- Why did we believe it?
- What evidence supported it?
- What remained unknown?
- What did we reject and why?
- Which artifacts are authoritative?
- Which experiments failed?
- What can be rerun?
- What can be falsified?
- What should be built next?

If those answers cannot be recovered without the original conversation, the handoff has failed.

## Final thesis
The project is not ultimately about writing more rules. It is about building an AI that understands the relationship between state, uncertainty, commitment, capability, timing, initiative, and consequence—and that can exploit those relationships under the exact constraints of the machine on which it runs.