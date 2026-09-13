# AEGIS Bot Upgrade Roadmap — 2026-09-13

## Purpose

This document is the shared planning surface for bringing the live `AIByzBuild` Byzantine bot from a technically sophisticated `.per` system into a demonstrably competent RTS opponent.

The governing principle is **functional capability over architectural complexity**. AEGIS should reproduce the useful tactical/strategic behavior demonstrated by the stock HD/Promisory corpus, using the native AoE2DE `.per` machine available to the target runtime. Historical code is evidence, not automatic runtime authority.

## Immediate rule: do not contaminate the running test

The current `foodTransition53.per` deployment is an active experiment. No additional live changes should be made until the game finishes and the co-scripter's observations are available.

The experiment is intended to answer one causal question:

`hunt depletion → transition authority → farm production → farmer assignment → sustained food → villager production`

A failed result will be diagnosed against that chain before any replacement is designed.

---

# 1. Research conclusion: what a competent `.per` RTS bot actually needs

Review of the AoE2 scripting corpus and public scripting references reinforces a key point: strong bots are not necessarily large collections of policy layers. Their competence comes from reliable closed loops around the engine's existing executors.

The scripting reference explicitly describes `.per` as a rule/fact/action expert system, with strategic numbers controlling major engine behavior. citeturn0search5turn0search29

Public working scripts show the same pattern: economy scripts continuously maintain gatherer percentages, build required drop sites, and change economic parameters over time rather than attempting to replace the native economy allocator. citeturn0search3

Therefore AEGIS should prioritize:

1. **Reliable observation** — know what the world and engine currently say.
2. **Correct classification** — distinguish shortage, threat, opportunity, transition, and failure.
3. **Single clear authority** — one subsystem owns each important decision variable.
4. **Existing executor reuse** — policy should feed native training, construction, economy, research, and attack machinery whenever possible.
5. **Verification** — prove that an accepted command produced the intended state change.
6. **Expiry/reassessment** — temporary decisions must stop controlling the system when their evidence becomes stale.

This is consistent with the AEGIS architecture already established in the repository: `WORLD → OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → RESULT → RECOVER/RE-ARBITRATE → REASSESS`.

---

# 2. The competency ladder

The bot should be developed as a sequence of **closed vertical capabilities**, not as a simultaneous rewrite.

| Competency | Capability | Current assessment | Next gate |
|---|---|---|---|
| 1 | **Civilian / economy survival** | Partially functional; food transition under live qualification | Sustain villager production and age progression |
| 2 | **Infrastructure / construction** | Existing executor is substantial | Prove infrastructure keeps economic and military production supplied |
| 3 | **Technology / age progression** | Policy exists; causal economy coupling remains important | Age transitions occur on competitive timings without economic collapse |
| 4 | **Information / scouting** | Stock-derived primitives and threat work exist | Information changes policy rather than merely being recorded |
| 5 | **Production / composition** | **Current milestone**; desired-number executor exists, composition demand layer is live | Threat/objective → composition demand → executor → physical army |
| 6 | **Military readiness / defense** | Partial | Army protects economy and responds to credible threats |
| 7 | **Military action / attack** | Partial/historical controls available | Readiness → attack authorization → execution → verification → reassessment |
| 8 | **Counter-response / adaptation** | Anti-cavalry and related slices exist as evidence/architecture | Enemy transition produces timely counter-capability |
| 9 | **Strategic objectives / expansion** | Not yet a primary live competency | Objectives change infrastructure, economy, production, and military behavior coherently |
| 10 | **Late-game / strategic continuity** | Not yet qualified | Bot continues making useful decisions after the opening plan expires |

The exact implementation order may change when runtime evidence exposes a dependency, but the competency model remains the organizing framework.

---

# 3. The most important architectural decision

AEGIS should not create a second executor every time a policy requirement appears.

The preferred pattern is:

```text
OBSERVE
  ↓
CLASSIFY
  ↓
OBJECTIVE / REQUIREMENT
  ↓
AUTHORITATIVE GOAL OR STRATEGIC NUMBER
  ↓
EXISTING ENGINE EXECUTOR
  ↓
PHYSICAL STATE
  ↓
VERIFY
  ↓
REASSESS
```

For production, this currently means:

```text
composition/threat policy
        ↓
desired-number-* authority
        ↓
AIByzBuild militaryUnits executor
        ↓
train <unit>
        ↓
unit exists / count changes
        ↓
verification
```

The same principle applies to farms, houses, military buildings, technology, and eventually attacks.

This avoids the failure mode of building a sophisticated policy layer that has no reliable path to physical execution.

---

# 4. Competency 1 — Economy survival

### Objective

Establish a self-sustaining economic loop that keeps villagers producing, advances ages, and supplies the production layer.

### Required closed loops

**Food:**

`food demand → gatherer allocation → dropsite/farm infrastructure → food income → villager production → reassessment`

**Wood:**

`wood demand → allocation → lumber infrastructure → wood income → farms/houses/military infrastructure → reassessment`

**Gold:**

`gold demand → allocation → mining infrastructure → gold income → age-up/technology/military production → reassessment`

### Current test

`foodTransition53.per` is the immediate qualification slice.

### Success criteria

- Hunt-to-farm transition occurs before catastrophic food starvation.
- Farms physically appear when required.
- Farmers actually appear.
- Food income recovers.
- Villager production remains continuous.
- Age progression is not crippled by the transition.

### Failure handling

Do not patch all possible causes simultaneously. Identify the first broken link in the chain and modify only that authority/executor boundary.

---

# 5. Competency 2 — Infrastructure

The existing construction system should be treated as a major asset, not replaced.

Required infrastructure classes:

- houses / population headroom
- farms
- lumber camps
- mining camps
- mills / economic drop sites
- barracks
- ranges
- stables
- siege workshops
- monasteries / universities / castles as appropriate

The qualification question is not merely "does the rule exist?" It is:

> Does the bot construct the right infrastructure early enough that the next required capability can actually execute?

A building rule that never receives demand is not an effective capability. A demand rule whose executor cannot place the building is not an effective capability.

---

# 6. Competency 3 — Technology and age progression

The bot needs a coherent resource-to-age/technology pipeline.

Target loop:

```text
economic state
  ↓
age/technology requirement
  ↓
resource feasibility
  ↓
authorization
  ↓
research / age-up command
  ↓
state transition
  ↓
new-age policy activation
  ↓
reassessment
```

Historical escrow behavior is particularly important here. `can-research-with-escrow` and `can-train-with-escrow` demonstrate a useful pattern: reserve resources for a high-priority action rather than allowing lower-priority spending to consume them.

AEGIS should eventually use this concept where the runtime semantics are sufficiently established, but should not promote historical behavior to confirmed target-runtime semantics without evidence.

---

# 7. Competency 4 — Information becomes policy

Scouting is only strategically useful if it changes decisions.

The required loop is:

`observe enemy → classify → update belief/state → change requirement → change authority → executor`

Examples:

- cavalry observed → anti-cavalry requirement increases
- enemy ranged mass observed → skirmisher/appropriate counter requirement increases
- enemy siege observed → siege response requirement increases
- forward military infrastructure observed → defensive readiness requirement increases
- enemy expansion observed → strategic objective changes

The current anti-cavalry work is a strong candidate for proving this transition because the historical corpus contains substantial evidence for threat observation and camel production.

---

# 8. Competency 5 — Production / composition

This is the current AEGIS milestone.

The existing executor already provides the crucial physical layer: it reads desired-number goals and trains the corresponding units.

The milestone is therefore **not** "write a better trainer." It is:

> Build a reliable policy-to-composition authority that produces useful army composition without fighting the existing executor.

### Target loop

```text
enemy / strategic state
        ↓
classification
        ↓
composition requirement
        ↓
production authority
        ↓
desired-number-* goal
        ↓
existing AiBuilder training executor
        ↓
physical unit production
        ↓
composition verification
        ↓
reassessment
```

### Eight production targets

The production authority matrix should govern each target explicitly, with:

- writer
- trigger
- precedence
- owner
- executor
- verification
- expiry
- failure behavior

The immediate targets are the Byzantine military production classes already represented by the live executor, including spearmen, skirmishers, camel riders, and the remaining existing production targets.

### Key design constraint

Do not let multiple generations write the same production authority without an explicit precedence contract.

CompositionDemand 55–59 can remain experimental while qualification determines whether its demand signal improves the executor's output or merely increases economic pressure.

---

# 9. Competency 6 — Military readiness and defense

Once production works, the next question is whether the army exists **before** the threat becomes lethal.

Required loop:

`threat → readiness requirement → production/building authorization → army accumulation → defensive posture → threat reassessment`

The bot should distinguish:

- harmless observation
- harassment
- genuine attack
- siege threat
- base breach
- economic raid
- army transition

A competent bot should not respond to every observation by blindly changing composition.

---

# 10. Competency 7 — Military action

Attack behavior should be treated as another lifecycle, not as a single `(attack-now)` command.

Historical constants already provide evidence of distinct attack states:

- retreat-now goal 20
- attack-status goal 24
- restart-attack goal 27

The AEGIS version should eventually express:

```text
readiness
  ↓
attack objective
  ↓
authorization
  ↓
attack execution
  ↓
contact / movement / target state
  ↓
result classification
  ↓
continue / retreat / restart / re-form
```

The key qualification rule is that an accepted attack command is not itself proof of strategic success.

---

# 11. Competency 8 — Adaptation and counter-response

The bot must eventually respond to **transitions**, not merely static threats.

Example:

```text
enemy scouts / cavalry observed
        ↓
threat aggregate rises
        ↓
anti-cavalry requirement
        ↓
camel/spear production authority
        ↓
production
        ↓
army composition changes
        ↓
threat reassessment
```

This is the AEGIS THREAT → CAPABILITY chain.

The same framework should support multiple response classes:

- counter unit
- fortification
- mobility
- denial
- relocation
- retreat
- counterattack
- siege
- technology
- delay

The bot should choose among these based on requirements and feasibility rather than hard-coding every threat to a single unit.

---

# 12. Competency 9 — Strategic objectives and expansion

After the bot can survive and fight, it needs objectives that change over time.

Examples:

- secure additional resources
- establish forward military infrastructure
- take a second/third Town Center
- protect a critical economic area
- deny enemy expansion
- secure relics
- establish trade
- transition to late-game composition

These should be expressed as requirements that downstream systems can consume rather than as isolated scripts.

---

# 13. Competency 10 — Late-game continuity

A strong opening is not enough.

The bot must survive the expiration of its early-game assumptions.

Required properties:

- stale objectives expire
- old composition demands stop dominating
- resource allocation adapts
- technology continues
- infrastructure scales
- military composition evolves
- attacks can be abandoned and restarted
- economic/military authority remains internally consistent

This is where AEGIS's generation/expiry/reassessment model becomes especially valuable.

---

# 14. What we should NOT do

Until the current qualification evidence says otherwise:

1. Do not add multiple competing economy systems.
2. Do not replace the native villager allocator unnecessarily.
3. Do not build duplicate construction executors when `construction.per` already supplies one.
4. Do not replace the existing training executor with another training layer.
5. Do not treat command acceptance as world-state completion.
6. Do not promote historical HD/Promisory behavior to target-runtime fact without evidence.
7. Do not reopen the retired scenario-loader automation.
8. Do not resurrect `ADProm` or `ByzantineWarCouncil` as production architecture.
9. Do not change a running experiment merely because another possible failure mode has been identified.
10. Do not optimize code size or architectural elegance ahead of measurable gameplay competence.

---

# 15. Qualification method

Every competency should pass through the same four gates.

### Gate A — Static integrity

- parser-valid
- load-valid
- symbol ownership known
- no duplicate authority
- no known ABI collision

### Gate B — Control evidence

- trigger fires
- authority changes
- executor receives the demand

### Gate C — World evidence

- physical state changes
- intended object/unit/building/research exists
- no false inference from command acceptance

### Gate D — Strategic effect

- resource throughput improves
- army composition changes appropriately
- threat is actually mitigated
- age progression improves
- attack/defense outcome improves

A competency is not "done" merely because Gate A or B passes.

---

# 16. Development cadence

The project should move in this order:

```text
CURRENT FOOD TEST
      ↓
DIAGNOSE FIRST BROKEN LINK
      ↓
ONE TARGETED CORRECTION
      ↓
REQUALIFY
      ↓
PRODUCTION / COMPOSITION QUALIFICATION
      ↓
MILITARY READINESS
      ↓
THREAT → CAPABILITY
      ↓
ATTACK / DEFENSE LIFECYCLE
      ↓
STRATEGIC OBJECTIVES
      ↓
LATE-GAME CONTINUITY
```

Each step should leave behind a reusable contract, evidence record, and known failure modes.

---

# 17. Immediate work queue after the current game

### P0 — Current food-transition result

**Owner:** current test / co-scripter observation

Determine:

- whether transition activated
- when it activated
- farm count before/after
- farmer count before/after
- food throughput before/after
- villager production continuity
- age-up timing

### P1 — Economy bottleneck closure

Only after P0 identifies the broken link:

- repair the smallest failing authority/executor boundary
- re-run the same 30-minute comparison
- compare against the current baseline

### P2 — Production authority qualification

For each of the eight production targets:

- enumerate all writers
- define precedence
- define final owner
- connect to existing executor
- define verification
- define expiry
- prove physical production

### P3 — Production effectiveness

Move beyond "units were produced":

- compare desired vs actual composition
- compare composition against threat
- measure resource pressure
- ensure production does not destroy villager production

### P4 — Threat → capability vertical slice

Complete one full anti-cavalry slice from observation through physical counter-capability and reassessment.

### P5 — Military lifecycle

Build readiness → attack → result → retreat/reform/restart as a qualified lifecycle.

### P6 — Strategic continuity

Add objective transitions, expansion, and late-game reassessment only after the lower-level executors are reliable.

---

# 18. External research notes

The public AoE2 scripting ecosystem supports the same engineering direction:

- AIREf documents DE-compatible AI commands, facts, parameters, strategic numbers, and DUC behavior. citeturn0search5
- The original CPSB documentation describes the AI as a rule/fact/action expert system, which is the correct mental model for `.per`. citeturn0search29
- Working public scripts demonstrate continuous strategic-number economy control and construction triggers rather than replacing the engine's underlying allocation system. citeturn0search3
- Microsoft's DE updates explicitly describe improvements to AI age advancement and economic preservation, reinforcing that economic continuity and age progression are fundamental AI competencies rather than incidental optimizations. citeturn0search1
- Public AI projects also demonstrate that substantial competence can be expressed entirely through declarative AI scripts, including economic allocation, buildings, military production, technology, defense, and attack behavior. citeturn0search0turn0search7

These sources are **comparative evidence**, not authority over the target runtime. Repository evidence and direct runtime evidence remain higher priority.

---

# 19. Definition of success

The goal is not to make AEGIS contain more rules than the stock AI.

The goal is to make the bot reliably perform the following transformation:

```text
SEE SOMETHING
    ↓
UNDERSTAND WHAT IT MEANS
    ↓
DECIDE WHAT CAPABILITY IS REQUIRED
    ↓
AUTHORIZE THAT CAPABILITY
    ↓
MAKE THE ENGINE EXECUTE IT
    ↓
VERIFY THAT IT HAPPENED
    ↓
MEASURE WHETHER IT HELPED
    ↓
CHANGE COURSE WHEN IT DID NOT
```

When AEGIS can do that across economy, production, defense, military action, adaptation, and strategic objectives, it becomes a competent RTS bot rather than merely a sophisticated `.per` codebase.

---

## Current status

**2026-09-13 — PLANNING / NO LIVE CODE CHANGE**

Current live experiment: `foodTransition53.per`.

Next decision is deliberately blocked on the completed game and the co-scripter's screenshot/replay observations.
