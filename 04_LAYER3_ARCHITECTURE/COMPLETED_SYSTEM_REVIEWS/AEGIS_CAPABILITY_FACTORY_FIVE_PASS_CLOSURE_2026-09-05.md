# AEGIS Capability Factory — Five-Pass Architecture Closure

Date: 2026-09-05
Status: CLOSED — ARCHITECTURE
Phase: Layer 3A
Implementation status: NOT IMPLEMENTED
Runtime status: NOT AUTHORIZED / NOT EXECUTED
ABI status: NOT QUALIFIED

## Closure statement

Capability Factory is closed as an architectural subsystem after five-pass review by Architect, Carpenter, Adversary, Scientist, and Systems Assurance.

The subsystem exists to translate a currently relevant abstract capability requirement into a bounded set of concrete, qualified realizations using engine-derived and neighboring-subsystem evidence, without taking ownership of strategic choice, production capacity, resource policy, execution, or effectiveness.

Its minimal behavioral return is:

REQUIREMENT -> QUALIFY EXISTING CONTRIBUTION -> CONSTRUCT BOUNDED REALIZATION(S) -> QUALIFY MATERIAL DEPENDENCIES -> SUFFICIENT / PARTIAL-DEFICIENT / UNKNOWN -> PLANNING

Capability Factory is not a native AoE2DE capability primitive. It is an AEGIS semantic interpretation boundary built from lower-level engine evidence.

## Pass 1 — Architect

Architect established the subsystem boundary between abstract capability requirements and concrete realizable means.

Capability was explicitly separated from:
- unit identity;
- unit count;
- Force Composition;
- Production Capacity;
- Resource Portfolio;
- Technology;
- Infrastructure;
- strategic value;
- Planning;
- Decision;
- Commitment;
- Execution;
- Verification.

The initial model permitted capability decomposition, multiple realizations, existing contribution, material dependencies, timing, accessibility, civilization-specific realization, preservation of existing capability, and capability deficit.

The Architect established the core invariant that capability realization is not capability effectiveness and that a realization must not become a strategic selection merely because it is technically feasible.

Pass 1 verdict: PASS — PROVISIONAL.

## Pass 2 — Carpenter

Carpenter aggressively removed machinery that lacked independent behavioral return.

Rejected:
- Capability Factory Manager;
- Capability Manager;
- Capability Database;
- Capability Registry;
- Capability Ontology;
- Capability Lifecycle Manager;
- Capability Decomposition Engine;
- Capability Tree / universal graph;
- Capability Dependency Manager;
- Capability Simulator;
- Combat Simulator;
- Capability Optimizer;
- Universal Capability Score;
- Capability Completion Percentage;
- Universal Contribution Matrix;
- Realization Manager;
- Realization Registry;
- Deficit Manager;
- Reachability Manager;
- Timing Manager;
- Forecast Engine;
- Civilization Capability Registry;
- Capability Conflict Manager;
- universal Confidence Manager;
- universal History Manager.

The surviving semantic core is deliberately small:

1. Capability Requirement — what capability is currently requested.
2. Existing Contribution — what qualified current means already contribute.
3. Realization — what bounded concrete means could establish the requested capability.
4. Material Dependency — what prerequisite changes realization feasibility.
5. Deficit — what remains after qualified existing contribution.
6. Sufficiency — whether the realization meets the requirement at the relevant scope.
7. Unknown — whether evidence is insufficient to establish the conclusion.
8. Identity / generation / scope — retained only where their absence changes behavior or permits stale state to cross a semantic boundary.

Carpenter principle:

Retain state only where removing it creates a demonstrable behavioral failure.

Pass 2 verdict: PASS.

## Pass 3 — Adversary

Adversary attacked the reduced core for strategically dangerous false conclusions.

The attack surface included:
- unit-count reductionism;
- overcrediting existing contributors;
- scope leakage;
- false sufficiency;
- partial capability collapse;
- unknown-to-zero collapse;
- zero-to-unknown collapse;
- possible-to-available collapse;
- future-to-current collapse;
- production/resource duplication;
- technology/infrastructure duplication;
- hidden Planning;
- hidden Decision;
- hidden Force Composition;
- hidden strategic substitution;
- production bias;
- universal optimization;
- capability simulation;
- capability ontology explosion;
- recursive dependency explosion;
- shared-contributor double credit;
- stale capability generation;
- concurrent generation collision;
- cancellation/supersession corruption;
- search-state contamination;
- engine-data error propagation;
- runtime explosion;
- effectiveness laundering.

Five load-bearing adversarial failures were promoted:

A. False capability — means exist but do not satisfy the requested capability scope.
B. False sufficiency — means constitute part of the capability but are incorrectly declared sufficient.
C. Silent strategic substitution — an infeasible requested capability is replaced by another capability without upstream authorization.
D. Stale realization — a realization associated with obsolete requirement context remains actionable.
E. Capability explosion — realization/dependency generation becomes combinatorial and destroys runtime feasibility.

Promoted invariants include:
- capability contribution must be capability-specific;
- existing contribution must be scope-qualified;
- existence is not availability;
- availability is not sufficiency;
- partial capability cannot silently become complete;
- UNKNOWN cannot become ZERO merely because evidence acquisition failed;
- future realization cannot masquerade as current capability;
- shared contributors cannot be infinitely credited to independent demands;
- Capability Factory cannot select strategic preference;
- Capability Factory cannot substitute a different capability;
- Capability Factory cannot duplicate Resource Portfolio or Production Capacity;
- Capability Factory cannot become Planning or Decision;
- realization generation must remain bounded;
- identity and generation/context must survive consequential upstream changes;
- numeric ABI identity cannot define semantic ownership.

Pass 3 verdict: PASS WITH TARGETED CORRECTIONS.

## Pass 4 — Scientist

Scientist separated direct engine evidence, AEGIS derivation, and unresolved machine protocol.

The AoE2 AI Scripting Encyclopedia documents the engine-facing substrate, including facts, object data, search operations, production feasibility, research feasibility/status, training readiness, pending objects, resource access, cost data, goal comparison/arithmetic, and timing mechanisms. Many search/object operations have material runtime costs, making bounded evaluation a correctness concern as well as an optimization concern.

Relevant documented facilities include:
- up-get-fact;
- up-get-focus-fact;
- up-get-player-fact;
- up-get-object-data;
- up-get-object-target-data;
- up-get-object-type-data;
- up-pending-objects;
- up-can-build;
- up-can-train;
- up-can-research;
- up-train-site-ready;
- up-research-status;
- up-resource-amount;
- up-resource-percent;
- cost-data operations;
- up-get-precise-time;
- search/filter and spatial primitives.

Scientific classification:

SUPPORTED:
- concrete unit/object evidence;
- unit counts;
- relevant object data;
- specific production feasibility checks;
- training-site readiness;
- research feasibility/status;
- pending-work observation;
- resource observation;
- concrete cost construction/inspection;
- time observation;
- spatial/search evidence.

DERIVED / AEGIS SEMANTIC:
- generic capability;
- existing capability contribution;
- capability deficit;
- capability sufficiency;
- capability realization;
- capability scope;
- capability-specific partiality;
- capability availability as a composite conclusion.

ENCODABLE BUT PROTOCOL OPEN:
- capability identity;
- realization identity;
- generation linkage;
- multiple realization representation;
- scope representation;
- UNKNOWN representation;
- partial realization representation;
- upstream/downstream publication contract.

EMPIRICALLY OPEN:
- zero versus unknown;
- search isolation;
- contributor qualification;
- pending/current interaction;
- production/readiness transition behavior;
- technology transition latency;
- infrastructure transition latency;
- time-to-capability inference;
- concurrent capability isolation;
- publication atomicity;
- stale-generation rejection;
- shared contributor behavior;
- exact target-build line/type/class semantics;
- practical runtime budget.

The Scientist also established that documented engine behavior cannot automatically be treated as target-build truth. Official AoE2DE updates have repeatedly corrected AI scripting and object-data behavior. Update 177723, for example, documented fixes for false AI reports involving Enemy Gates, Town Centers, and object-data-next-attack. This directly supports build-scoped qualification rather than documentation-only certification.

Scientist principle:

USE DIRECT ENGINE EVIDENCE -> DERIVE ONLY WHAT IS NECESSARY -> STORE ONLY WHAT THE ENGINE CANNOT PROVIDE -> NEVER DUPLICATE ENGINE STATE WITHOUT BEHAVIORAL RETURN.

Pass 4 verdict: PASS WITH OPEN EMPIRICAL QUESTIONS.

## Pass 5 — Systems Assurance

Systems Assurance traced Capability Factory through its neighboring authoritative systems.

Primary trace:

WORLD MODEL
-> FORCE COMPOSITION / PLANNING
-> CAPABILITY FACTORY
-> PRODUCTION CAPACITY / RESOURCE PORTFOLIO / TECHNOLOGY / INFRASTRUCTURE INPUTS
-> PLANNING
-> DECISION
-> COMMITMENT
-> EXECUTION
-> VERIFICATION
-> RECOVERY
-> WORLD MODEL

Supporting trace:

CAPABILITY UNCERTAINTY
-> ATTENTION
-> SCHEDULER
-> OBSERVATION
-> WORLD MODEL
-> CAPABILITY FACTORY

Assurance confirmed:

World Model owns qualified world-state evidence.

Capability Factory owns capability interpretation, not raw world truth.

Force Composition supplies capability demand/context rather than receiving strategic selection authority from the factory.

Production Capacity owns production-capacity interpretation.

Resource Portfolio owns resource-side posture and feasibility.

Technology owns technology state and research policy.

Infrastructure owns infrastructure state and construction policy.

Planning owns course generation and feasibility at the strategic-course level.

Decision owns strategic selection.

Commitment owns accepted responsibility for attempting a selected course.

Execution owns operational realization.

Verification owns evidence-qualified operational outcome.

Recovery owns response to verified deviation/failure/uncertainty.

Capability Factory cannot issue commands, reserve resources, schedule work, select strategy, replace objectives, certify effectiveness, or rewrite world state.

## Final Capability Factory contract

Purpose:

Convert a currently relevant capability requirement into a bounded, qualified interpretation of how that capability can be realized from available civilization means, while preserving scope, uncertainty, identity, and upstream authority.

Owns:
- capability realization;
- capability-specific contribution;
- capability deficit;
- materially necessary capability decomposition;
- materially necessary realization dependencies;
- capability sufficiency assessment;
- capability-side UNKNOWN;
- capability scope where scope changes meaning;
- identity/generation linkage where needed for stale-state protection;
- bounded alternative realizations;
- capability realization publication.

Consumes:
- qualified World Model evidence;
- capability requirements from upstream systems;
- Force Composition context;
- relevant Production Capacity conclusions;
- Resource Portfolio feasibility;
- Technology state;
- Infrastructure state;
- Map/accessibility conclusions where relevant;
- existing Commitment context where it materially constrains available contribution.

Produces:
- bounded capability realizations;
- existing contribution;
- additional required means;
- material dependencies;
- sufficient / partial-deficient / unknown capability conclusions;
- capability-side information dependencies;
- planning-relevant realization alternatives.

Does not own:
- World Model truth;
- observation;
- Belief;
- Situation Analysis;
- Objectives;
- Planning;
- Decision;
- Commitment;
- Resource Portfolio;
- Production Capacity;
- Technology policy;
- Infrastructure policy;
- Force Composition policy;
- Map Control;
- Operations;
- Execution;
- Verification;
- Recovery;
- Attention;
- Scheduler;
- Memory;
- Risk;
- Doctrine;
- Opponent Model;
- strategic value;
- strategic preference;
- commands;
- strategic effectiveness.

## Load-bearing invariants

1. Capability is not a unit.
2. Capability is not a raw unit count.
3. Capability is not Force Composition.
4. Capability is not Production Capacity.
5. Capability is not Resource Portfolio state.
6. Capability is not strategic value.
7. Existing means do not automatically constitute usable contribution.
8. Contribution is scope-qualified where scope changes meaning.
9. Existing capability may satisfy a requirement without creating production demand.
10. Partial capability cannot silently become sufficient capability.
11. UNKNOWN cannot silently become ZERO.
12. Established ZERO cannot silently become UNKNOWN when negative evidence is material.
13. Possible realization is not current availability.
14. Current availability is not sufficiency.
15. Future realization is not current capability.
16. Shared contributors cannot be double-credited without qualified context.
17. Capability Factory cannot silently substitute a different capability.
18. Capability Factory cannot select among strategic alternatives.
19. Capability Factory cannot issue commands.
20. Capability Factory cannot reserve resources.
21. Capability Factory cannot duplicate production-capacity interpretation.
22. Capability Factory cannot duplicate resource-side feasibility interpretation.
23. Capability Factory cannot duplicate technology or infrastructure ownership.
24. Capability realization is not execution.
25. Capability realization is not verification.
26. Capability realization is not effectiveness.
27. Historical assessment is not current world truth.
28. Cancellation changes authority; it does not erase world history.
29. Supersession changes current authority; it does not rewrite prior evidence.
30. Upstream generation/context must survive consequential realization evaluation.
31. Concurrent scopes must not be conflated.
32. Realization generation must remain bounded.
33. Capability interpretation must not launder inference into observation.
34. Numeric identity is not semantic identity.
35. Documented engine semantics are not automatically target-build-qualified semantics.
36. Runtime cost is part of correctness.

## Scientific qualification gates retained for ABI/runtime phase

CF-S1: concrete contributor identity semantics.
CF-S2: contributor counting behavior.
CF-S3: existing-contribution qualification.
CF-S4: zero versus unknown.
CF-S5: search isolation.
CF-S6: production feasibility.
CF-S7: training-site readiness.
CF-S8: pending/current interaction.
CF-S9: technology transition.
CF-S10: infrastructure transition.
CF-S11: resource precision and failure behavior.
CF-S12: cost-data behavior.
CF-S13: temporal realization inference.
CF-S14: capability identity encoding.
CF-S15: generation isolation.
CF-S16: concurrent scope isolation.
CF-S17: multiple-realization representation.
CF-S18: publication coherence.
CF-S19: shared-contributor accounting.
CF-S20: runtime budget.

These gates remain open. Their existence does not reopen architecture closure.

## Closure conditions

Architect: PASS.

Carpenter: PASS.

Adversary: PASS WITH TARGETED CORRECTIONS; corrections incorporated into final contract.

Scientist: PASS WITH OPEN EMPIRICAL QUESTIONS; open questions preserved rather than hidden.

Systems Assurance: PASS.

No unresolved architectural ownership collision remains load-bearing.

No missing neighboring subsystem is required to define the architectural boundary.

No ABI channel has been allocated by this review.

No goal ID has been allocated by this review.

No strategic-number ID has been allocated by this review.

No runtime test has been executed by this review.

No production `.per` implementation has been authorized by this review.

## Final verdict

CAPABILITY FACTORY — CLOSED: ARCHITECTURE.

The subsystem is ready to leave Layer 3A architecture and enter the implementation-design / ABI-qualification pipeline when explicitly authorized.

The next engineering work must not begin by inventing a capability database or assigning arbitrary goals. It must begin by selecting one narrow capability contract, identifying the exact engine primitives needed, qualifying their target-build semantics, and proving that the resulting representation produces behavioral value without duplicating engine state.

## Evidence references

AoE2 AI Scripting Encyclopedia:
https://airef.github.io/

Commands Index:
https://airef.github.io/commands/commands-index.html

Parameter Index:
https://airef.github.io/parameters/parameters-index.html

AI Command Performance Benchmarks:
https://airef.github.io/resources/articles/command-performance.html

UserPatch AI/Scripting Patch Notes:
https://airef.github.io/tables/up-patch-notes.html

AoE2DE Update 177723:
https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/

These sources establish documented substrate and historical evidence only. The installed target build remains the qualification authority for production use.
