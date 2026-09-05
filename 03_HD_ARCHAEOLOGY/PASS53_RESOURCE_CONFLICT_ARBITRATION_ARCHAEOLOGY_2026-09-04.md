# Pass 53 — Resource Conflict / Arbitration / Commitment-State Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation authority:** NONE  
**Status:** PASS WITH EXPLICIT HISTORICAL / AEGIS BOUNDARIES  
**Predecessors:** Pass 52 + Pass 52 Deep QC  

## 1. Mission

Pass 52 established that historical HD AI scripting contains concrete resource-protection / escrow mechanisms that can participate in purpose-directed capability commitments. Pass 52 Deep QC identified the deeper unresolved question: not merely how the AI saves resources, but how multiple strategic demands interact when they compete for the same scarce resource.

This pass therefore investigates the concept of **resource arbitration** at the historical-control level.

The research target is:

```text
STRATEGIC DEMANDS
↓
RESOURCE CLAIMS
↓
PROTECTION / ESCROW
↓
FEASIBILITY
↓
AUTHORIZATION
↓
EXPENDITURE
↓
REASSESSMENT
```

The pass does not claim that the historical AI contained a centralized portfolio manager. It asks what evidence exists for distributed priority, suppression, release, reset, and competing claims.

No `.per` implementation is created.

## 2. Deep-QC correction to Pass 52

The most important correction is terminological.

**Escrow is a mechanism. Resource control is a controller. Arbitration is a property that emerges only when multiple demands interact.**

Therefore:

```text
ESCROW ≠ BUDGET
ESCROW ≠ PRIORITY
ESCROW ≠ OPTIMIZER

ESCROW + CONTROL STATE + CONDITIONS
can implement a PURPOSE-DIRECTED COMMITMENT.
```

Only when competing commitments are observed can we legitimately discuss arbitration.

## 3. Engine-level semantics that matter

The public AI scripting reference confirms that `set-escrow-percentage` controls the computer player's escrow percentage for a resource and that escrow-aware commands include `can-research-with-escrow`, `can-train-with-escrow`, and `can-build-with-escrow`. The engine also exposes release and direct escrow-modification mechanisms.

The public UserPatch documentation explains the crucial affordability distinction: ordinary affordability excludes protected escrow, while escrow-inclusive checks can consider it. Escrow therefore changes the resource view supplied to authorization predicates.

**Evidence:** DIRECT for engine semantics; historical applicability remains version-scoped.

## 4. The real economic object: spendable vs committed capital

The stockpile alone is insufficient.

```text
TOTAL RESOURCE
=
SPENDABLE RESOURCE
+
PROTECTED / COMMITTED RESOURCE
```

For strategic analysis, a commitment also has:

```text
PURPOSE
TARGET
REQUIRED AMOUNT
URGENCY
TIME HORIZON
FEASIBILITY
RELEASE CONDITION
CANCELLATION CONDITION
```

Historical code does not necessarily store these as one object. They can be distributed across goals, strategic numbers, timers, escrow state, research availability, unit counts, and other predicates.

**Key insight:** semantic state can be distributed even when no explicit semantic object exists.

## 5. Resource claims

An AEGIS analytical resource claim can be represented as:

```text
CLAIM = {
    resource,
    purpose,
    required_amount,
    current_protection,
    urgency,
    feasibility,
    expiration,
    reversibility,
    competing_value
}
```

This is an AEGIS abstraction, not a historical variable declaration.

It gives us vocabulary for describing the collective behavior of historical mechanisms from a player-strategy perspective.

## 6. Conflict is the real test

The meaningful arbitration state is:

```text
SUM OF DESIRED SPENDING > AVAILABLE RESOURCE
```

Possible responses include:

```text
DELAY
PROTECT
RELEASE
SUPPRESS
OVERRIDE
CANCEL
SUBSTITUTE
```

A rule-driven AI can encode priority without a numeric utility function. Rule ordering, strategic-number modes, escrow percentages, and prerequisite gates can make some actions eligible while making others effectively unavailable.

Therefore:

> **Priority can be operationally real without being numerically explicit.**

This is a critical distinction between historical control logic and formal optimization.

## 7. `sn-resource-control` as a control-mode channel

Historical usage repeatedly treats `sn-resource-control` as a mode that gates downstream behavior. The exact meaning of a numeric value must always be recovered from its writers and readers in context.

The safe model is:

```text
CONTROL MODE
↓
LOCAL POLICY GATES
↓
ELIGIBLE / INELIGIBLE ACTIONS
```

This explains how one compact state channel can coordinate many subsystems without requiring a centralized planner.

## 8. Priority without optimization

Three concepts must remain separate:

```text
UTILITY OPTIMIZATION
= compare candidate values

PRIORITY ENCODING
= establish ordered eligibility

ESCROW
= protect purchasing power
```

Historical evidence is strongest for the latter two mechanisms in selected paths. It does not prove a global utility optimizer.

This is highly relevant to the eventual bot because a useful baseline can be achieved with stable priority arbitration before sophisticated scoring is added.

## 9. Temporal commitment

Escrow changes not only what can be spent but when it can be spent.

```text
NORMAL SPENDING
↓
COMMITMENT ACTIVATED
↓
RESOURCE INFLOW PROTECTED
↓
TARGET FUNDING ACCUMULATES
↓
TARGET FEASIBLE
↓
RELEASE
↓
ACTION
```

This connects resource control to the existing AEGIS temporal model:

```text
STATE + TIMER + RESOURCE STATE
→ DELAYED ELIGIBILITY
```

## 10. Hysteresis: plausible, important, not yet proven

A naïve controller can thrash:

```text
COMMIT
→ CANCEL
→ RECOMMIT
→ CANCEL
```

The presence of persistent state, timers, escrow, and reset logic makes hysteresis an important archaeological hypothesis, but not a universal historical conclusion.

The decisive test is whether entry and exit conditions differ:

```text
ENTRY THRESHOLD
vs
EXIT THRESHOLD
```

If systematically present, historical hysteresis is directly supported.

## 11. Release and cancellation are first-class transitions

Potential commitment lifecycles include:

```text
COMMIT → SUCCESS → RELEASE
COMMIT → FAILURE → RELEASE
COMMIT → INVALIDATED → RELEASE
COMMIT → TIMEOUT → RELEASE
COMMIT → OVERRIDDEN → RELEASE
```

Selected release/reset behavior is evidenced; the complete taxonomy remains open.

Therefore every future archaeological record of resource commitment should include **release provenance**.

Never infer cancellation solely because a later rule resets a variable.

## 12. Authorization boundary

The canonical chain remains:

```text
DESIRE
↓
RESOURCE POLICY
↓
AFFORDABILITY
↓
AUTHORIZATION
↓
SIDE EFFECT
↓
WORLD STATE
```

Therefore:

```text
can-X-with-escrow ≠ action
release-escrow ≠ completion
train ≠ surviving unit
research ≠ completed technology
```

This is a hard AEGIS evidence invariant.

## 13. Production arbitration

Production is not a purchase event; it is a continuing demand rate.

```text
CAPABILITY DEMAND
↓
RESOURCE DEMAND RATE
↓
PRODUCTION THROUGHPUT
↓
REINFORCEMENT REQUIREMENT
```

A unit affordable once can still be economically invalid as a sustained composition.

An AEGIS analytical approximation is:

```text
SUSTAINABLE PRODUCTION RATE
≈
NET RESOURCE SURPLUS
÷
RESOURCE COST PER UNIT
```

This is not claimed as a historical formula.

## 14. Byzantine application: Camel vs Cataphract vs Imperial

Byzantines expose the conflict problem clearly:

```text
CAVALRY THREAT
→ CAMEL DEMAND

INFANTRY THREAT
→ CATAPHRACT DEMAND

LATE-GAME POWER WINDOW
→ IMPERIAL DEMAND
```

The -25% Byzantine discount applies to Spearman, Skirmisher, and Camel families, not Cataphracts. Cataphracts therefore remain a major food+gold commitment. The -33% Imperial discount changes the intertemporal value of preserving resources for age transition.

The correct player question is not:

> Which unit is strongest?

It is:

> **Which capability deserves the next scarce resource commitment given threat, timing, infrastructure, sustainment, and future demand?**

## 15. Capital-preservation substitution

A discounted Byzantine capability can have strategic value because it may satisfy a requirement while preserving resources for another commitment.

```text
REQUIRED CAPABILITY
↓
CHEAPER BYZANTINE OPTION
↓
LOWER FOOD BURDEN
↓
RESOURCE PRESERVED
↓
ALTERNATIVE CAPABILITY REMAINS FUNDABLE
```

The AEGIS generalized effective strategic cost is:

```text
DIRECT COST
+
DISPLACED CAPABILITY VALUE
+
TRANSITION COST
+
TIMING COST
+
RISK
```

This is an AEGIS model, not a recovered HD formula.

## 16. Emergency override

Long-term resource protection must be defeasible if survival requires immediate expenditure.

```text
LONG-TERM RESERVE
↓
CRISIS
↓
SURVIVAL PRIORITY
↓
RELEASE / OVERRIDE
↓
IMMEDIATE CAPABILITY
```

Selected historical release/reset behavior exists, but universal crisis arbitration is not yet closed.

This is a major discriminator between a saving controller and an adaptive controller.

## 17. Economic thrashing

Poor arbitration can produce:

```text
PLAN A
→ PARTIAL FUNDING
→ PLAN B
→ RELEASE A
→ PARTIAL FUNDING B
→ PLAN A AGAIN
```

This can waste both resources and strategic time while every local rule remains technically valid.

AEGIS therefore gains a future metric:

**Commitment Stability** — frequency and cost of reversing strategic resource commitments before intended capability delivery.

This is an AEGIS metric, not historical evidence.

## 18. Economic integrity invariant

The research-derived design invariant is:

```text
A RESOURCE COMMITMENT SHOULD NOT BE
CREATED, BROKEN, OR REDIRECTED
WITHOUT AN EXPLICIT STATE TRANSITION.
```

This is Layer-3 design guidance derived from the archaeology, not a claim that HD perfectly enforced it.

## 19. Minimum economic state model

For future AEGIS research, the minimum conceptual state is:

```text
RESOURCE STOCK
RESOURCE ESCROW
RESOURCE FLOW
ACTIVE CLAIM
CLAIM PURPOSE
CLAIM PRIORITY
CLAIM AGE
CLAIM FEASIBILITY
CLAIM EXPIRY
COMPETING DEMANDS
COMMITMENT STRENGTH
RELEASE CONDITION
FAILURE CONDITION
```

The historical system may distribute these semantics across many state channels rather than materialize them together.

## 20. Historical architecture vs AEGIS abstraction

Historical HD substrate:

```text
GOALS
+
STRATEGIC NUMBERS
+
FLAGS
+
TIMERS
+
RULE GATES
+
ESCROW
+
CAN-* PREDICATES
+
SIDE-EFFECT COMMANDS
```

AEGIS research abstraction:

```text
BELIEF / STATE
↓
DEMANDS
↓
CLAIMS
↓
ARBITRATION
↓
COMMITMENT
↓
AUTHORIZATION
↓
ACTION
↓
VERIFICATION
↓
UPDATE
```

The second must never be represented as recovered historical architecture.

## 21. Closure criteria for the economic pillar

Before declaring the resource-control pillar closed, archaeology should establish from executable source evidence:

1. Every writer of `sn-resource-control`.
2. Every major reader.
3. Meaning of every observed mode in local context.
4. Every relevant escrow-percentage writer.
5. Every release path.
6. Every escrow-inclusive affordability path.
7. Every reset/cancellation path.
8. Evidence for or against competing claims.
9. Evidence for or against hysteresis.
10. Evidence for or against emergency override.
11. Resource-control ↔ gatherer allocation.
12. Resource-control ↔ production authorization.
13. Resource-control ↔ research authorization.
14. Resource-control ↔ military crisis.
15. At least one end-to-end chain in which resource protection materially changes downstream capability authorization.

Until these are closed, the pillar remains research-active.

## 22. Practical significance for the eventual bot — still Layer 2

The archaeology now strongly suggests that a future implementation should not reduce economic control to villager percentages or raw affordability checks.

The eventual conceptual pipeline is more powerful:

```text
RESOURCE OBSERVATION
↓
DEMAND REGISTRY
↓
CLAIM / PRIORITY MODEL
↓
COMMITMENT CONTROL
↓
FEASIBILITY GATES
↓
PRODUCTION / RESEARCH AUTHORITY
↓
POSTCONDITION VERIFICATION
↓
REASSESSMENT
```

The practical objective is **economic integrity**: avoid locally legal actions that collectively destroy the bot's next strategically necessary capability.

No implementation is authorized in Layer 2.

## 23. Deep conclusion

Pass 53 changes the definition of the pillar.

The pillar is not “escrow.”

It is:

> **ECONOMIC COMMITMENT CONTROL.**

Escrow is one historical mechanism inside that larger problem.

Historical evidence supports pieces of the problem:

```text
RESOURCE PROTECTION
+
PURPOSE-DIRECTED SAVING
+
ESCROW-AWARE FEASIBILITY
+
RELEASE
+
RESOURCE-CONTROL STATES
+
RESEARCH / PRODUCTION GATES
+
RESET / REASSESSMENT
```

The decisive unresolved question is whether cross-consumer priority is explicitly encoded or emerges from distributed rule ordering and state gates.

That is now the central archaeological target.

**Pass 53 status: PASS WITH OPEN ARCHAEOLOGICAL QUESTIONS.**

Layer 2 remains strictly research-only.