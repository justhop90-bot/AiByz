# Pass 52 — HD Resource / Escrow / Production / Sustainment Archaeology

**Date:** 2026-09-04  
**Layer:** Layer 2 — research / archaeology only  
**Implementation authority:** NONE  
**Status:** PASS WITH RESEARCH BOUNDARIES  
**Scope:** Historical HD AI resource allocation, escrow, production authorization, research authorization, and the implications for expensive late-game capability commitments such as Byzantine Cataphracts.

## 1. Mission

Pass 51 established a critical strategic correction: Cataphracts must be treated as late-game strategic capital rather than as a simple infantry counter. They consume substantial food and gold, require infrastructure and technology, and have downstream Elite and Logistica investments. The next archaeological question is therefore not merely whether the historical HD AI could produce an expensive unit, but how the historical control system protected, released, competed for, and consumed scarce resources when multiple strategic objectives were active.

This pass reconstructs that machinery from historical HD-style scripting semantics and public scripting references. It deliberately does **not** design a Layer-3 implementation.

## 2. Primary finding

The historical AI has a real resource-commitment mechanism, but it is not a general-purpose economic optimizer.

The strongest evidence supports this model:

```text
STRATEGIC PURPOSE
↓
RESOURCE CONTROL STATE
↓
ESCROW ACCUMULATION / PROTECTION
↓
AFFORDABILITY TEST INCLUDING ESCROW
↓
RELEASE ESCROW
↓
SIDE-EFFECT COMMAND
↓
RESOURCE CONTROL STATE RESET / TRANSITION
```

Escrow therefore acts as **protected purchasing power**. It lets a controller accumulate resources for a known future purpose while preventing ordinary affordability tests and ordinary spending from treating those resources as freely available.

This is substantially more powerful than a simple “save resources” flag, but it is still not evidence of a global optimizer that continuously scores every possible expenditure.

## 3. Escrow is a reservation mechanism

Public AI scripting documentation states that setting an escrow percentage diverts a percentage of newly received resources into escrow. Releasing escrow returns the saved amount to the normal resource pool. The documentation also demonstrates the key semantic distinction between ordinary affordability and escrow-inclusive affordability.

The engine therefore supports two materially different resource views:

```text
AVAILABLE RESOURCE
= current stockpile - protected escrow

ESCROW-INCLUSIVE RESOURCE
= current stockpile
```

The practical consequence is decisive:

```text
RESOURCE ARRIVES
→ PART IS PROTECTED
→ ORDINARY SPENDING CANNOT ASSUME IT IS AVAILABLE
→ TARGET CAPABILITY ACCUMULATES FUNDING
→ ESCROW-INCLUSIVE AFFORDABILITY BECOMES TRUE
→ ESCROW RELEASE
→ PURCHASE / RESEARCH / TRAIN / BUILD
```

The public command reference explicitly distinguishes `can-build-with-escrow`, `can-research-with-escrow`, and `can-train-with-escrow` from their non-escrow variants. citehttps://airef.github.io/commands/commands-index.html

## 4. Why this matters strategically

A conventional resource check asks:

> Can I afford this now?

Escrow introduces a second question:

> Have I protected enough resources that I can guarantee this capability later?

That is a major strategic distinction.

The resulting state is closer to:

```text
CURRENT RESOURCES
+
PROTECTED RESOURCES
+
PURPOSE / CONTROLLER STATE
=
FUTURE CAPABILITY COMMITMENT
```

However, escrow does not itself prove that the AI understands opportunity cost in a general human sense. It proves that the scripting system can reserve resources and use those reserved resources in explicit affordability/authorization paths.

**Evidence class:** DIRECT for escrow semantics; INFERRED for the strategic interpretation of “commitment.”

## 5. Resource control is a finite controller, not a utility optimizer

Historical AI patterns repeatedly use strategic-number state such as `sn-resource-control` to gate research, production, economy, and transition behavior. The state values can represent different economic-control modes.

The archaeological pattern is:

```text
NORMAL ECONOMIC CONTROL
        ↓
SPECIAL PURPOSE IDENTIFIED
        ↓
RESOURCE CONTROL STATE CHANGES
        ↓
ESCROW / SAVING BEGINS
        ↓
TARGET BECOMES AFFORDABLE
        ↓
RESOURCE RELEASE
        ↓
ACTION
        ↓
CONTROL STATE RESET
```

This is better described as a **distributed finite/control-state resource controller** than as an optimization engine.

The public scripting reference confirms that strategic numbers are persistent engine state channels and that the engine exposes 512 SN slots, although many are reserved/effective and must not be treated as arbitrary storage without verification. citehttps://airef.github.io/strategic-numbers/sn-index.htmlhttps://airef.github.io/resources/articles/data-limits.html

## 6. Escrow does not equal budgeting

A budget normally describes planned allocation across competing future uses.

Escrow, by itself, does not do that.

It provides a mechanism for protecting resources from competing spending.

Therefore:

```text
ESCROW
= RESOURCE PROTECTION

BUDGET
= RESOURCE ALLOCATION POLICY

OPTIMIZER
= COMPETITIVE EVALUATION AMONG ALLOCATIONS
```

Historical AI can combine escrow with state gates, threat conditions, unit counts, research status, age, and other predicates. That combination can approximate a budgeted commitment for a particular objective. It should not be mislabeled as a general budget optimizer.

## 7. The crucial asymmetry: escrow protects, but can also starve

Escrowing resources has an opportunity cost.

If food or gold is protected for a future technology or military investment, that resource is deliberately withheld from other actions.

Therefore:

```text
ESCROW BENEFIT
= INCREASED PROBABILITY OF TARGET CAPABILITY

ESCROW COST
= REDUCED FLEXIBILITY FOR COMPETING CAPABILITIES
```

This produces a genuine strategic tradeoff even if the historical script does not explicitly calculate that tradeoff numerically.

The historical mechanism can therefore be understood as an **implicit opportunity-cost controller**: the opportunity cost exists in the resource system, while the script encodes selected priorities through protection and release rules.

This is an AEGIS interpretation, not a claim about the original authors' formal design vocabulary.

## 8. Research is a capital expenditure

The command model distinguishes:

```text
can-research
can-research-with-escrow
research
research-completed
research-available
```

The historical pattern is frequently:

```text
STRATEGIC CONDITIONS
+
RESEARCH AVAILABLE
+
RESOURCE / ESCROW FEASIBILITY
+
UNIT / BUILDING / AGE CONTEXT
→
RESEARCH
```

The important archaeological distinction is between **research authorization** and **research completion**.

A rule firing `research` does not prove the technology is already completed. Likewise, an escrow threshold does not prove that the intended technology was eventually successful. The historical controller has to bridge intent, affordability, queueing, completion, and subsequent state.

The public command reference explicitly distinguishes `can-research` from `research` and `research-completed`. citehttps://airef.github.io/commands/commands-index.html

## 9. Production is also capital expenditure

Production has the analogous structure:

```text
CAN-TRAIN
→ TRAIN
→ QUEUE / EXECUTION
→ COMPLETION
→ FIELD CAPABILITY
```

The `can-train-with-escrow` mechanism means protected resources can be considered when authorizing training. This gives the historical AI a way to reserve resources for production without immediately spending them.

Again, however:

```text
TRAIN COMMAND
≠
COMPLETED UNIT
≠
SURVIVING UNIT
≠
EFFECTIVE ARMY
```

This distinction is consistent with the replay archaeology rule established earlier: queue/action evidence cannot automatically be promoted into world-state completion evidence.

## 10. Production throughput is the hidden denominator

For an expensive unit, affordability of one unit is strategically weak evidence.

A serious late-game capability requires:

```text
RESOURCE INCOME
↓
RESOURCE ALLOCATION
↓
PRODUCTION BUILDINGS
↓
QUEUE CAPACITY
↓
TRAINING THROUGHPUT
↓
ARMY MASS
↓
REINFORCEMENT RATE
↓
SURVIVABILITY
↓
SUSTAINED FIELD EFFECT
```

This is especially important for Cataphracts.

A single Cataphract can be affordable while a sustained Cataphract composition is economically impossible. Conversely, an expensive composition can become sustainable after the economy, infrastructure, and map conditions change.

Therefore the correct archaeological unit is not “unit affordability.” It is **capability sustainment**.

## 11. The Cataphract case exposes the difference

For Byzantines, the strategic sequence is better represented as three separate capital decisions:

```text
A. BEGIN CATAPHRACT PRODUCTION
B. INVEST IN ELITE CATAPHRACT
C. INVEST IN LOGISTICA
```

These decisions have different prerequisites, costs, timing, and expected benefits.

The Byzantine -25% discount does not apply to Cataphracts. It applies to the Spearman, Skirmisher, and Camel families. Thus the Byzantine economy can use discounted families to manipulate the food/gold bottleneck, but Cataphracts remain a full food+gold commitment.

Current public reference data lists Cataphract at 70 food / 75 gold and the Elite upgrade and Logistica as additional major investments. Official Update 39284 reduced the Elite Cataphract food cost from 1600 to 1200 and Logistica food from 1000 to 800 while retaining their major gold costs. These current values are reference data, not a substitute for installed `.dat` verification.

## 12. Gold is a portfolio resource

Gold should not be modeled as “the resource needed for Cataphracts.”

It is a competing capital pool.

Potential competing uses include:

```text
IMPERIAL AGE
ELITE CATAPHRACT
LOGISTICA
OTHER GOLD MILITARY UNITS
MONKS
KEY TECHNOLOGIES
SIEGE
GUNPOWDER
MARKET BALANCING
OTHER CIVILIZATION-SPECIFIC INVESTMENTS
```

Thus a Cataphract decision is partially a portfolio decision:

```text
WHAT CAPABILITY DOES THIS GOLD BUY?
```

The historical HD system can encode selected priorities through escrow and resource-control states, but the archaeology does not show a universal marginal-return calculation across every gold expenditure.

## 13. Resource control can be staged

Historical patterns show that the AI does not have to choose between “save everything” and “save nothing.” It can change escrow percentages and control states over time.

Conceptually:

```text
NORMAL
↓
ACCUMULATE
↓
PARTIAL PROTECTION
↓
TARGET THRESHOLD
↓
RELEASE
↓
SPEND
↓
NORMALIZE
```

This is important because strategic commitments have different urgency levels.

A technology that is useful eventually may justify gradual protection. An imminent military response may require immediate release. A crisis may force cancellation of the long-term reserve entirely.

Historical examples show this kind of staged behavior around research, economic upgrades, and civilization-specific investments.

## 14. Release is an authority event

Escrow release should be treated as more than bookkeeping.

The control sequence is often:

```text
RESOURCE PROTECTED
↓
TARGET CONDITION SATISFIED
↓
RELEASE ESCROW
↓
EXECUTE SIDE EFFECT
```

The release is therefore part of the authorization boundary between “resources reserved” and “resources available for immediate execution.”

This reinforces the Pass-48 invariant:

```text
INTENT
≠
AUTHORIZATION
≠
ACTION
≠
EXECUTION
≠
WORLD STATE
≠
OUTCOME
```

## 15. Historical example: unique-unit investment pattern

Publicly accessible HD-era AI material contains rules that set resource-control states, accumulate resources, test `can-research-with-escrow`, release escrow, and then research a civilization-specific technology. Other examples combine unit counts, research status, population, and economic state before allowing a unique technology to consume the reserve.

One especially useful pattern is effectively:

```text
TARGET UNIT / TECH CONTEXT
+
RESOURCE CONTROL STATE
+
RESEARCH AVAILABLE
+
CAN RESEARCH WITH ESCROW
→
RELEASE ESCROW
→
RESEARCH
```

This is strong evidence for **purpose-directed resource reservation**.

It is not evidence for a generalized optimizer.

The public scripting guide also explicitly presents escrow as a method for saving toward a future building and using `can-build-with-escrow` to trigger release and construction. citehttps://steamcommunity.com/sharedfiles/filedetails/?id=1238296169

## 16. Historical example: Byzantine technology

Public HD-style AI material contains a Byzantine-specific rule in which a military condition such as multiple Fire Ships gates a Greek Fire research action through `can-research-with-escrow`, followed by escrow release and research.

The archaeological chain is:

```text
BYZANTINE MILITARY STATE
↓
FIRE SHIP MASS THRESHOLD
↓
GREEK FIRE AVAILABLE
↓
ESCROW-INCLUSIVE RESEARCH FEASIBILITY
↓
RELEASE
↓
RESEARCH
```

This is a useful precedent because it demonstrates civilization-specific strategic research being coupled to military composition and protected resources.

It still does not establish a complete Byzantine strategic optimizer.

## 17. Emergency override is part of the model

A long-term reserve cannot be allowed to become an irreversible death sentence.

Historical patterns include release/reset behavior when the strategic context changes, such as population or military crisis conditions, missing prerequisites, or loss of the original target condition.

The generalized historical pattern is:

```text
LONG-TERM COMMITMENT
↓
WORLD STATE CHANGES
↓
ORIGINAL PURPOSE INVALIDATED
↓
RELEASE / RESET
↓
RETURN TO GENERAL RESOURCE CONTROL
```

This is the beginning of **commitment reversibility** in the archaeological model.

It is not full dynamic portfolio optimization, but it is much closer to adaptive control than a fixed build order.

## 18. Byzantine strategic capital lifecycle

Pass 51 can now be sharpened using the resource-control archaeology.

```text
THREAT / OPPORTUNITY
↓
REQUIRED CAPABILITY
↓
CATAPHRACT CANDIDATE
↓
RESOURCE COMPETITION
↓
RESERVATION / ESCROW DECISION
↓
INFRASTRUCTURE + TECH FEASIBILITY
↓
PRODUCTION AUTHORIZATION
↓
CATAPHRACT MASS
↓
ELITE THRESHOLD
↓
LOGISTICA THRESHOLD
↓
SUSTAINMENT
↓
BATTLEFIELD EFFECT
↓
REASSESS
```

The critical addition is **resource competition before production**.

## 19. Cheap Byzantine units as capital-preservation tools

The Byzantine discounts create an important interaction with Cataphract economics.

Because Spearmen, Skirmishers, and Camels receive a -25% cost discount, those families can sometimes solve a military requirement while preserving more Gold for a later high-value investment.

That yields a strategic substitution pattern:

```text
REQUIRED CAPABILITY
↓
CANDIDATE A: CHEAP DISCOUNTED FAMILY
CANDIDATE B: CATAPHRACT
↓
COMPARE
  RESOURCE BURDEN
  TIMING
  SUPPORT
  MOBILITY
  SURVIVABILITY
  FUTURE VALUE
  GOLD PRESERVATION
  TRANSITION COST
↓
SELECT / DELAY / MIX
```

This does **not** mean the discounted family is always superior. A cheap counter that cannot survive, reach the target, or solve the actual battlefield problem can be strategically inferior despite its price.

## 20. Imperial Age is a competing intertemporal investment

Byzantines receive a -33% Imperial Age cost.

That means a Cataphract investment competes not only with other units and technologies but with the timing value of Imperial Age.

The correct model is:

```text
SPEND GOLD/FOOD NOW
→ IMMEDIATE MILITARY CAPABILITY

OR

PRESERVE RESOURCES
→ IMPERIAL TRANSITION
→ ACCESS / UPGRADES / TECHNOLOGY / CAPABILITY
```

The cheaper Imperial transition changes the relative threshold at which waiting for Imperial becomes attractive. It does not guarantee a faster Imperial Age because military expenditure, economy, infrastructure, raids, map conditions, and idle time remain relevant.

## 21. The historical controller has three distinct resource questions

The archaeology suggests a useful distinction:

### Question A — Can I afford it?

```text
can-X
```

### Question B — Have I protected enough for it?

```text
can-X-with-escrow
```

### Question C — Should I spend it now?

This third question is usually encoded indirectly through surrounding conditions, controller state, threat state, age, unit counts, and strategic-number modes rather than through a universal utility function.

This is one of the most important findings of Pass 52.

## 22. Human strategy ↔ historical AI bridge

Human player reasoning:

```text
“I need to preserve 600 gold because my intended Imperial / Elite / military transition is more valuable than another marginal unit right now.”
```

Historical AI representation:

```text
STRATEGIC CONDITION
↓
RESOURCE-CONTROL STATE
↓
ESCROW PERCENTAGE
↓
ACCUMULATION
↓
CAN-RESEARCH-WITH-ESCROW / CAN-TRAIN-WITH-ESCROW
↓
RELEASE
↓
COMMAND
```

The semantic mapping is therefore:

```text
PLAYER CONCEPT
RESOURCE PRIORITY

HD REPRESENTATION
ESCROW + STATE + FEASIBILITY + COMMAND
```

The mapping is not one-to-one. A human semantic concept may be distributed across several rules and state channels.

## 23. Production sustainment and queue saturation

The training queue is itself a resource-capacity constraint. Public patch documentation records the training-queue mechanism and shows that training commands and affordability checks interact with the queue system.

Therefore a late-game capability must satisfy both:

```text
ECONOMIC FEASIBILITY
+
PRODUCTION CAPACITY
```

A fully funded Cataphract plan with insufficient production infrastructure still fails to generate sufficient field mass.

Conversely, production infrastructure without resource flow produces idle capacity.

Thus:

```text
SUSTAINABLE CAPABILITY
= RESOURCE FLOW × PRODUCTION THROUGHPUT × SURVIVAL
```

This is a conceptual dependency model, not a literal multiplication formula.

The UserPatch documentation confirms that training queue behavior changes the semantics of `can-train`, `can-train-with-escrow`, `train`, `up-can-train`, and `up-train`. citehttps://airef.github.io/tables/up-patch-notes.html

## 24. Resource-control failure modes

The archaeology exposes several failure classes that must remain distinct.

### A. Under-saving
Target capability never reaches affordability.

### B. Over-saving
Too much resource is protected while an urgent alternative capability is neglected.

### C. Stale commitment
Original strategic purpose is no longer valid.

### D. Infrastructure bottleneck
Resources exist but production/research cannot convert them into capability quickly enough.

### E. Gold starvation
Food and wood are sufficient while Gold becomes the binding constraint.

### F. Transition deadlock
Current army is committed while the next capability cannot be financed.

### G. Queue saturation
Production buildings exist but cannot create the required rate of reinforcement.

### H. False completion
Controller interprets authorization or queueing as successful world-state completion.

These should remain separate in all later archaeology and eventual implementation work.

## 25. New AEGIS concept: Capability Funding State

Pass 52 introduces a research concept for later Layer-3 consideration, but **not implementation authority**:

> **Capability Funding State** = the relationship between a desired future capability, protected resources, current free resources, competing resource claims, production capacity, and the conditions required to release the reserve.

Conceptually:

```text
CAPABILITY
+
CURRENT FUNDING
+
PROTECTED FUNDING
+
COMPETING CLAIMS
+
INFRASTRUCTURE
+
TECHNOLOGY
+
TIME HORIZON
+
CANCELLATION CONDITIONS
=
CAPABILITY FUNDING STATE
```

This is an AEGIS-generalization. It is not a historical variable name.

## 26. New AEGIS concept: Gold Portfolio Pressure

A second research concept is warranted.

> **Gold Portfolio Pressure** = the degree to which multiple strategically valuable future actions compete for the same scarce Gold pool.

For Byzantines this can become unusually important because the civilization has inexpensive non-Gold military families while several high-impact late-game investments remain Gold intensive.

Conceptually:

```text
GOLD INCOME
↓
CLAIMS
├─ Imperial
├─ Elite military
├─ Cataphract
├─ Logistica
├─ Monks
├─ Siege
└─ Other tech / military
↓
PORTFOLIO PRESSURE
```

Again, this is an AEGIS research construct, not a historical HD variable.

## 27. Evidence boundary

### DIRECT
- Escrow percentages protect resource income.
- Release commands return escrow to the common resource pool.
- Escrow-inclusive affordability checks exist for building, research, and training.
- Strategic-number state can control resource allocation behavior.
- Historical AI uses explicit state/condition/action chains around resource protection and research/production.
- Training queue state affects training commands and affordability checks.

### COMPOSED
- Historical AI can form purpose-directed resource commitments by combining state, escrow, affordability, and side-effect commands.
- Research and production are both resource-conversion pipelines with authorization gates.

### INFERRED
- Escrow functions as a commitment mechanism.
- Resource control approximates selected opportunity-cost management.
- Release is part of the authorization boundary.
- Late-game capability selection should be analyzed as capital allocation rather than simple unit production.

### AEGIS-GENERALIZATION
- Capability Funding State.
- Gold Portfolio Pressure.
- Strategic Capital Lifecycle.
- Intertemporal military-vs-Imperial investment framing.

### UNCERTAIN / OPEN
- Whether any historical subsystem globally compared all competing Gold claims.
- Whether historical AI calculated marginal return or expected battlefield value.
- Exact causal semantics of every `sn-resource-control` value.
- Whether resource reservations were coordinated across all independent controllers.
- Whether historical Byzantine Cataphract investment was ever dynamically chosen from a broad candidate set.

## 28. Research gaps created by this pass

The next archaeological work should target:

1. Exact historical `escrow.per` control-state transitions.
2. Every consumer of `sn-resource-control` and its state meanings.
3. Historical resource-control transitions around Imperial Age.
4. Historical unique-unit upgrade funding chains.
5. Production-specific escrow patterns.
6. Whether military production and research controllers can simultaneously reserve overlapping resources.
7. Release/cancellation paths under attack.
8. Evidence for resource-control handoff between controllers.
9. Cataphract-specific historical HD evidence, if any.
10. Whether resource control can be traced through a complete semantic closure from threat to sustained capability.

## 29. Pass-52 decision

**PASS WITH RESEARCH BOUNDARIES.**

The historical HD resource system is now sufficiently understood to establish the following archaeological invariant:

```text
RESOURCE CONTROL
≠
RESOURCE AMOUNT

ESCROW
≠
BUDGET

AFFORDABILITY
≠
AUTHORIZATION

AUTHORIZATION
≠
COMPLETION

COMPLETION
≠
SUSTAINMENT

SUSTAINMENT
≠
STRATEGIC SUCCESS
```

The strongest new strategic conclusion is:

> **The historical HD AI possessed a real mechanism for protecting resources for selected future capabilities, but its evidence supports a collection of explicit commitment controllers rather than a universal economic optimizer.**

For Byzantine late-game strategy, this means Cataphract analysis must begin **before** the train command: at the level of competing resource claims, protected funding, Imperial timing, production capacity, transition cost, and sustainable reinforcement.

## 30. Layer boundary confirmation

No `.per` implementation, controller, production policy, or runtime artifact was created by this pass.

This document is research/archaeology only and does not authorize Layer-3 implementation.

## Sources

- AoE2 AI Scripting Encyclopedia — command reference: https://airef.github.io/commands/commands-index.html
- AoE2 AI Scripting Encyclopedia — strategic-number reference: https://airef.github.io/strategic-numbers/sn-index.html
- AoE2 AI Scripting Encyclopedia — data limits: https://airef.github.io/resources/articles/data-limits.html
- AoE2 AI Scripting Encyclopedia — command semantics: https://airef.github.io/resources/articles/intro-to-commands.html
- UserPatch AI scripting notes: https://airef.github.io/tables/up-patch-notes.html
- Skelecat, AI Scripting guide: https://steamcommunity.com/sharedfiles/filedetails/?id=1238296169
- Eruner, Age-Of-Empires-AI-Scripts: https://github.com/Eruner/Age-Of-Empires-AI-Scripts
