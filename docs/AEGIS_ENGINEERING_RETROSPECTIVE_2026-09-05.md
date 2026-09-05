# AEGIS — Final Engineering Retrospective

**Date:** 2026-09-05
**Project:** AiByz / AEGIS Byzantine AI
**Purpose:** durable record of the engineering experience and the most important lessons learned during the project phase represented by this handoff.

## 1. What this project was actually like

This was not primarily a programming project. It was a prolonged exercise in learning how not to fool ourselves.

At the beginning, the obvious temptation was to write a Byzantine bot: identify cavalry, count units, build camels, manage resources, attack, retreat, repeat. That sounds like an implementation problem.

It became clear that it was first a machine-semantics problem.

The difficult questions were things such as:

- What exactly does a `.per` command mean?
- When does a command become an engine action rather than an instruction issued by the controller?
- When does a queued object become a created object?
- When is a created object actually available for another decision?
- What does a zero mean?
- What does absence mean?
- What does an unknown observation mean?
- Which numeric values are actually free in the target build?
- Which values merely happen to be numerically equal across different typed namespaces?
- Which historical statements still apply to the current executable?
- What does a replay prove, and what does it merely suggest?

The project became progressively less about producing impressive-looking code and more about establishing claims that could survive hostile scrutiny.

## 2. The biggest change in perspective

The central realization was:

> **The hard part is not teaching an AI what to do. The hard part is proving what the machine actually did.**

That sentence became the practical boundary between architecture and implementation.

A rule can express an intention.

A command can establish that an instruction was issued.

An engine can accept or reject it.

A queue can hold work that has not yet become a world object.

A world object can exist without yet being strategically effective.

A replay can record the command while exposing only aggregate synchronization evidence for the resulting world.

Those are different facts.

The project became substantially stronger once those facts were no longer collapsed into one word such as `success`.

## 3. What I learned most

### 3.1 Evidence is an engineering dependency

Evidence is not documentation added after the code. In a reverse-engineering project, evidence is an input dependency of the code.

A primitive is not trustworthy merely because its syntax is documented. It becomes trustworthy when the target build, legal inputs, side effects, failure behavior, and observable postcondition are known well enough to support the claim the architecture needs.

That is why the project adopted the primitive progression:

`DOCUMENTED → ARCHAEOLOGICALLY_SUPPORTED → IMPLEMENTED → RUNTIME_VALIDATED → REPLAY_CORROBORATED → BATTLEFIELD_VALIDATED`

The distinction is uncomfortable but essential. A project can have thousands of lines of correct-looking code and still have no proof that its critical assumptions are correct.

### 3.2 Typed identity matters more than numeric coincidence

One of the most instructive ABI discoveries was that numeric equality does not imply semantic collision.

A value such as `10000` can appear in a declaration that is not a goal channel while the same numeric range can remain a candidate goal namespace. The correct question is not “is this number used?” but “what typed semantic channel owns this value in this context?”

The same lesson appeared with unit IDs, unit lines, classes, facts, goals, and strategic numbers.

Names that look interchangeable often are not.

The validator may reject something the engine accepts, or accept something that does not prove the desired runtime property. Conversely, replacing a semantically correct abstract identifier with a concrete identifier merely to satisfy a validator can destroy the intended behavior.

### 3.3 The validator is an instrument, not the machine

A validator answers questions about the validator's model of legal input.

The engine answers questions about the engine.

Those models overlap, but they are not identical.

The historical `knight-line` investigation was a particularly useful example: the identifier's meaning depends on typed context and engine semantics. The correct engineering response was to preserve the semantic distinction and seek target-build evidence rather than blindly rewrite the code around a static lint complaint.

### 3.4 A replay is an evidentiary record, not a perfect world-state database

The real `CAL_REPLAY_001` replay was one of the turning points.

It contained 444,591 body records, including 2,213 ACTION records and 221,174 SYNC records. It was rich enough to reconstruct a substantial command chronology.

But the same replay also demonstrated the limits of that evidence.

Only 442 SYNC records exposed a parsed `current_time`. Aggregate synchronization fields existed, but those observations did not automatically provide individual object lineage.

Therefore:

`DE_QUEUE ≠ created unit`

`BUILD ≠ realized building`

`RESEARCH ≠ completed technology`

unless independent evidence establishes the transition.

That is not a weakness of the project. It is a discovery about the evidence source.

### 3.5 Negative results are first-class engineering results

Several apparently promising paths were deliberately abandoned:

- automated scenario-loader testing;
- hidden native test-harness activation;
- treating injection-based runtime tooling as a harmless dependency;
- treating screen capture as primary semantic instrumentation;
- treating historical source as current runtime authority;
- allocating apparently unused state channels without ownership proof.

Every one of these dead ends reduced future uncertainty.

The project would be materially worse if those failed approaches had simply disappeared from the record.

## 4. The native test-harness lesson

Direct inspection of the retail executable revealed a surprisingly large amount of embedded test-harness terminology: `TEST_HARNESS_COMM`, `TEST_HARNESS_ADDRESS`, FTS parsing, event controllers, test-harness storage, and related AI commands.

The temptation was obvious: if the capability exists in the binary, activate it.

Controlled launches did not establish a working external retail harness path.

The resulting rule is one of the most important architectural lessons:

**Embedded capability ≠ enabled capability ≠ externally invocable capability.**

A binary can contain facilities that are intended for internal builds, QA infrastructure, development modes, or code paths that are not supported through normal retail invocation.

The professional response is to respect the evidence boundary rather than reverse-engineer a forbidden door simply because the lock is visible.

## 5. The external harness lesson

The external harness became valuable because it was deliberately boring.

It does not attempt to become the game.

It captures the build.

It launches the retail executable.

It records lifecycle state.

It acquires the replay.

It parses the replay.

It emits conservative evidence.

It refuses to claim more than the evidence establishes.

That architecture is less glamorous than an injected omniscient observer, but it creates a cleaner evidentiary chain and keeps the project aligned with its retail-safe constraints.

AoE2Control was still useful. Its exact-build compatibility evidence and live-state design exposed valuable ideas about external observability. But its injection/runtime-hooking architecture made it inappropriate as an unqualified AEGIS core dependency.

The right conclusion was not “AoE2Control is bad.” It was “AoE2Control answers a different class of question and therefore has a different evidence status.”

## 6. The architectural lesson

The project reviewed a large collection of AEGIS subsystems: world modeling, belief, situation analysis, objectives, planning, decision, commitment, execution, verification, recovery, resource portfolio, production capacity, capability factory, force composition, and production/economic conversion.

The important result was not that every subsystem became elaborate.

It was that repeated objections converged on a small set of cross-system machine-truth problems:

- identity and generation;
- UNKNOWN versus FALSE versus ZERO;
- publication atomicity;
- search isolation;
- zero-result semantics;
- pending/created/available lifecycle;
- command acceptance;
- feasibility versus desirability versus authorization versus commitment;
- controller time versus world time.

The answer was **not** a universal State Manager.

The better answer was a shared qualification discipline: define the ownership and evidence contract once, then let each subsystem retain its own responsibility.

## 7. The project became more rigorous as it became more specific

Early work naturally produced broad questions: “How do we make the bot smarter?”

The useful questions became narrower:

- Can this exact target executable accept this exact fact query?
- What typed identifier does this operand require?
- What is the earliest observable transition after this command?
- Is the resulting observation individual or aggregate?
- Can identity be followed across the transition?
- Can the result be reproduced?
- What alternative explanation remains possible?

That narrowing is progress.

A good reverse-engineering project does not end with fewer unknowns because it guessed more confidently. It ends with fewer unknowns because it converted them into experiments.

## 8. What I would tell the next project lead

Do not start by writing the Byzantine bot.

Start by proving the machine.

Do not trust the prettiest abstraction.

Trust the strongest evidence.

Do not ask whether a number looks unused.

Ask which typed channel owns it.

Do not ask whether a command appeared in a replay.

Ask what causal transition can actually be demonstrated afterward.

Do not treat an unknown observation as false.

Do not treat a zero as unknown.

Do not treat validator acceptance as runtime proof.

Do not treat historical code as current-build truth.

Do not erase failed experiments.

And most importantly: when the evidence says “I don't know,” preserve that answer. An explicit UNKNOWN is an engineering asset. A fabricated TRUE is technical debt with a fuse attached.

## 9. Final assessment

The project did not reach a finished Byzantine production bot in this phase.

That is the truth.

It did something more foundational: it transformed a large, ambiguous ambition into an evidence-controlled engineering program with a known target executable, a preserved stock baseline, a reconstructed historical architecture, a typed ABI discipline, a defined first vertical slice, an external replay-oriented harness, actual calibration against a real replay, and a sharply bounded list of remaining machine-semantic questions.

The next team should not interpret that as failure or as permission to rush implementation.

The remaining work is now tractable because the uncertainty has been named.

The next breakthrough is expected from controlled causal experiments around:

`COMMAND_ISSUED → ACCEPTED/REJECTED → PENDING/QUEUED → CREATED → AVAILABLE → EFFECTIVE`

Once those transitions are sufficiently observable and repeatable, the ABI can be frozen with confidence and the first production `.per` vertical slice can be implemented against real machine semantics.

## 10. Closing thought

The project taught me that serious engineering is often an exercise in refusing to be impressed by your own explanation.

A plausible theory is cheap.

A reproducible observation is expensive.

A clean distinction between the two is priceless.

AEGIS should be built on that distinction.
