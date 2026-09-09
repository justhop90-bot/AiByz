# AEGIS / ByzBot — Final HD Basic-Capability Red-Team Addendum

**Date:** 2026-09-09
**Status:** Authoritative addendum to the final-bot blueprint and HD Capability Coverage Audit
**Purpose:** perform one final adversarial pass assuming the existing blueprint has missed basic RTS capabilities.

## 1. Result

The 20-slice blueprint remains structurally sound, but the previous coverage ledger was too high-level to be considered closed.

The most important correction is this:

> **A capability domain is not covered merely because a slice has a matching name. The historical AI must be audited for the mundane operational machinery underneath the strategic label.**

The verified HD/Promisory source family is not just a strategy layer. Its shipped source inventory includes dedicated machinery for initialization, construction, economy, hunting, gatherer control, interaction, research, scouting, threats, trade, resignation, water behavior, technology/upgrade processing, and extensive general-purpose state/search support. The current Steam depot inventory independently exposes modules including `boarhunting.per`, `buildings.per`, `escrow.per`, `gatherers.per`, `general.per`, `interaction.per`, `orb.per`, `researches.per`, `resign.per`, `scoutcontrol.per`, `threats.per`, `trade.per`, `tsa.per`, `ugp.per`, `init.per`, and water/phase-related support. This module inventory is evidence of capability areas requiring inspection; it is **not**, by itself, proof of the exact behavior of every module.

## 2. Basic capability families that must not be forgotten

### A. Civilian production and continuity

Explicitly audit:

- villager creation;
- villager queue continuity;
- housing forecasting;
- population-cap avoidance;
- idle-villager detection and recovery;
- worker death accounting;
- worker replacement;
- builder selection;
- builder release/reassignment;
- repair-capable workers;
- emergency worker reassignment;
- worker role switching;
- task completion and return-to-work behavior.

These are not implementation details. They determine whether the economy has continuous throughput.

### B. Food-source lifecycle

Do not reduce food to `food income`.

Audit separately:

- sheep/other herdable acquisition and handling;
- boar hunting;
- deer/huntable-source handling where present;
- farming transition;
- fishing transition;
- source depletion;
- dropsite replacement;
- source safety;
- worker travel;
- saturation;
- transition timing.

The existence of a dedicated `boarhunting.per` module is a direct warning that early food acquisition contains specialized operational logic.

### C. Economy infrastructure

Audit:

- lumber/wood dropsites;
- mining camps;
- mills;
- farms;
- docks;
- market access;
- replacement of destroyed/obsolete economic infrastructure;
- infrastructure placement constraints;
- builder allocation;
- economic recovery after harassment.

The final bot must know the difference between owning resources and having a sustainable physical mechanism for collecting them.

### D. Construction itself

The previous blueprint correctly treats construction as an ABI boundary, but the capability inventory must still include the whole problem:

- what should be built;
- when it becomes required;
- prerequisite satisfaction;
- placement search;
- builder selection;
- build authorization;
- placement failure;
- alternate placement;
- rebuild;
- defensive construction;
- walling/containment;
- production infrastructure;
- economic infrastructure;
- technology infrastructure;
- completion verification.

Construction is therefore both a strategic capability and a machine-semantic qualification problem.

### E. Military basics beneath "military strategy"

Explicitly audit:

- unit creation;
- unit replacement;
- upgrade selection;
- military production continuity;
- queue saturation;
- group creation;
- regrouping;
- movement;
- attack;
- attack-move;
- patrol;
- formation;
- target selection;
- target invalidation;
- pursuit;
- disengagement;
- retreat;
- re-engagement;
- garrison;
- ungarrison;
- escort;
- defense of economic units;
- emergency response.

A strategy controller without these operational primitives is not a complete RTS controller.

### F. Technology is broader than age-up

Audit all distinct technology roles:

- age advancement;
- economic upgrades;
- military upgrades;
- unit-line upgrades;
- civilization-specific technologies;
- monastery technologies;
- technology prerequisites;
- technology opportunity cost;
- research queue conflicts;
- completion verification;
- post-research capability changes.

The existing escrow archaeology establishes protected research commitments, but that does not mean age-up is the whole research system.

### G. Monks are a complete operational system

The previous blueprint correctly promoted monks to their own slice. The red-team pass adds the requirement to audit the mundane details explicitly:

- monastery construction;
- monk production;
- monk queue continuity;
- healing target selection;
- healing positioning;
- relic discovery;
- relic assignment;
- relic pickup;
- relic transport;
- relic deposit;
- conversion target selection;
- conversion timing/cooldown behavior;
- monk retreat/survival;
- escort;
- monastery technology dependencies;
- reserve monks;
- relic-economy strategic value.

Do not assume these are all historically implemented by HD merely because the game supports them. The audit must distinguish **game capability** from **historical AI behavior**.

### H. Siege is not just another unit class

Audit:

- siege production;
- siege prerequisites;
- siege escort;
- siege target selection;
- siege vulnerability;
- anti-siege response;
- defensive-structure pressure;
- siege timing;
- retreat/recovery;
- siege replacement.

### I. Water has two economies, not one

Audit separately:

- fishing economy;
- naval military;
- transport;
- dock production;
- naval grouping;
- naval movement;
- naval retreat;
- transport unloading/army delivery;
- water-map economic transition;
- amphibious logistics.

A bot that can fight on land but cannot maintain a water economy is incomplete for the game's map space.

### J. Market, trade, and conversion

Audit:

- market construction/access;
- buy/sell conversion;
- emergency resource conversion;
- trade-route infrastructure;
- trade-unit production;
- trade-route safety;
- late-game resource regime;
- opportunity cost of conversion.

### K. Social / team behavior

Audit:

- ally detection;
- ally/enemy classification;
- cooperation state;
- tribute/resource transfer;
- requests/taunts/operator controls where historically present;
- assistance logic;
- team military interactions;
- team economy interactions.

Do not silently turn historical operator interfaces into core strategic authority. They are separate control surfaces.

### L. Terminal behavior

Audit:

- defeat/terminal recognition;
- resignation policy;
- hopeless-state evaluation;
- leniency/timing;
- final resource/military state;
- whether terminal decisions are strategic policy or execution behavior.

The existence of a dedicated resignation subsystem means terminal behavior cannot be treated as an afterthought.

### M. Difficulty/execution scaling

Audit whether the historical source separates:

- strategic intent;
- execution speed/frequency;
- execution capability;
- search depth;
- rule/timing aggressiveness;
- difficulty-specific restrictions.

The final bot should preserve this distinction rather than embedding difficulty into strategic doctrine.

## 3. Hidden basic capability: state-machine hygiene

The most dangerous category of missed "basic" behavior is not a game feature. It is the machinery that keeps asynchronous rules from fighting one another.

The HD archaeology repeatedly points toward:

- pending checks;
- timers;
- reset state;
- self-disable/re-entry;
- generation changes;
- temporary goals;
- scratch search state;
- target invalidation;
- stale-state recovery;
- fallback paths;
- rule-budget/performance awareness.

Therefore every AEGIS capability must include a lifecycle contract, not merely a command.

## 4. Newly elevated cross-cutting requirements

The final blueprint must explicitly treat these as universal requirements:

1. **Idle-time management** — idle workers, idle production, idle military groups, and unused information assets.
2. **Death/replacement management** — civilians, military units, scouts, monks, ships, siege.
3. **Repair/maintenance** — damaged units, buildings, economic infrastructure, siege, ships where applicable.
4. **Housing/population continuity** — forecast capacity rather than reacting only after blockage.
5. **Queue continuity** — villagers, military, monks, ships, research.
6. **Upgrade continuity** — unit and technology transitions.
7. **Target invalidation** — target disappears, dies, becomes unreachable, or ceases to satisfy the objective.
8. **Command deduplication** — never treat repeated eligibility as permission to issue duplicate asynchronous actions.
9. **Temporal hysteresis** — timers, cooldowns, and reset/re-entry prevent oscillation.
10. **Performance budgeting** — search depth and rule cost are strategic constraints in a bounded rule engine.
11. **Emergency mode** — economic/military policy must be able to change under acute threat.
12. **Recovery mode** — failed execution must return to arbitration rather than silently remain committed.

## 5. What this red-team pass changes

It does **not** increase the blueprint to an arbitrary number of slices.

Instead, it strengthens the definition of completion for the existing 20 slices. Each slice now requires a **basic operational inventory** beneath its strategic headline.

For example:

`Civilian Lifecycle` is not complete when worker roles exist. It requires production, housing, assignment, task execution, idle recovery, reassignment, death, replacement, builder lifecycle, repair, and verification.

`Monastic Operations` is not complete when monk production exists. It requires relic and healing/conversion lifecycles and survival/positioning.

`Naval Operations` is not complete when warships exist. It requires fishing economy, transport, docks, naval groups, retreat, and water-map transitions.

`Military` is not complete when counters exist. It requires production, upgrades, composition, command, target lifecycle, engagement lifecycle, defense, retreat, regrouping, replacement, and recovery.

## 6. Audit verdict

**The 20-slice architecture survives the red-team pass, but the previous capability-coverage ledger remains OPEN.**

No additional top-level slice is justified yet. The correct next step is to populate the ledger with exact source anchors for these basic operational families.

If a direct source trace reveals a capability that cannot be cleanly owned by one of the 20 slices, the blueprint must be amended before production implementation.

## 7. Implementation gate

This red-team pass authorizes **no runtime code**.

Required order remains:

`HD SOURCE TRACE`
→ `CAPABILITY COVERAGE CLOSURE`
→ `MACHINE ABI CLEARANCE`
→ `SYMBOLIC CONTRACT FREEZE`
→ `FIRST PRODUCTION .PER`
→ `VERTICAL-SLICE QUALIFICATION`
→ `INTEGRATION`

The project must not substitute architectural confidence for source evidence.