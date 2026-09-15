# AEGIS Blueprint — AI(HD)+Promisory Adversarial Review — 2026-09-09

## Reviewer persona

This review treats the stock `AI (HD version).per` plus the complete original `Promisory` corpus as the adversarial senior engineer. Its job is to find omissions in the authoritative AEGIS Bot Blueprint, not to approve it.

## Verdict

**The blueprint is materially more complete than the previous vertical-slice list, but it is not allowed to claim behavioral equivalence with stock.** It now explicitly covers the major stock operating domains identified in the P0 substrate reconstruction: economy/workers, construction, research, production, scouting, military, threat, trade, water, boar, and interaction, plus their shared state and feedback topology.

## Stock-AI objections that the blueprint must retain

1. **Civilization continuity is foundational.** Villager production, housing, idle recovery, resource acquisition, worker allocation, dropsites and food transitions cannot be treated as optional economy polish.
2. **Construction is a state machine.** Placement, builder assignment, foundation/progress, completion, failure, retry and rebuilding are separate lifecycle stages.
3. **Food is a portfolio.** Herdables, forage, boar, deer/hunt, farms and fishing where applicable require source selection and transitions, not a single food counter.
4. **Economy is discrete and strategy-dependent.** Worker percentages are policy inputs, not the final control representation. Resource demand, escrow, affordability, competing claims and opportunity cost must be represented.
5. **Research changes the economy and military.** Age and technology state are coupled to gathering, construction and production.
6. **Scouting is an information service.** Discovery, geometry, path/threat analysis, enemy-strength estimation, task continuity and information freshness belong in the blueprint.
7. **Threat is interpreted.** Raw enemy counts are insufficient; stock aggregates military classes and weighted strength signals.
8. **Military is an operating system.** Production, grouping, tasking, targeting, movement, attack, retreat, reinforcement, siege and recovery must all exist.
9. **Water, trade, boar and interaction are real operating domains.** They cannot disappear merely because the first strategy slice is land cavalry.
10. **Late-game and transition behavior matter.** Population saturation, resource exhaustion, technology/production transitions and ending-state behavior must be integrated.
11. **Cross-system feedback is mandatory.** Economy ↔ production ↔ construction ↔ research ↔ military ↔ threat ↔ scouting must remain connected after AEGIS reorganizes ownership.
12. **Persistent state and control topology are part of behavior.** Timers, goals, strategic numbers, flags, groups, queues, state lifetimes and rule ordering cannot be abstracted away without proving the replacement semantics.
13. **Failure behavior is part of the capability.** Stock's practical competence includes recovery from blocked or changing conditions; AEGIS must explicitly model failure, retry, fallback and reassessment.

## Coverage check

The authoritative blueprint now contains explicit construction coverage for each objection above. The P0 reconstruction independently establishes that these domains exist in the stock source and interact as a distributed control system.

## Remaining adversarial warning

Coverage on paper is not coverage in code. A listed capability remains **UNIMPLEMENTED** until its stock contract has been forensically extracted, its AEGIS ownership defined, its ABI usage justified, its implementation written, and its runtime behavior qualified.

The adversarial reviewer therefore accepts the blueprint as the governing construction inventory while rejecting any claim that the bot is complete or stock-equivalent merely because every category has a row.

## Required review cadence

Before every implementation slice:

`BLUEPRINT → RELEVANT STOCK SOURCES → EXISTING AEGIS DOCUMENTATION/CODE → ABI/OWNERSHIP → IMPLEMENTATION → STATIC QC → RUNTIME QUALIFICATION → ADVERSARIAL STOCK REVIEW → ACCEPT/REVISE`

Any newly discovered stock capability must be added to the authoritative blueprint before it can be considered outside scope.
