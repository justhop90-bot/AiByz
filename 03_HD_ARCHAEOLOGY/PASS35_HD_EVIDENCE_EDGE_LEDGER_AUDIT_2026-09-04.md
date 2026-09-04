# AEGIS Layer 2 — Pass 35
## HD Evidence-Edge Ledger / Causal Provenance Audit

**Date:** 2026-09-04  
**Historical source:** verified `AI (HD version).per` + verified Promisory modules  
**Historical source SHA-256:** `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`  
**Layer-1 boundary:** frozen at 89%; no Layer-1 reopening  
**Scenario-loader:** permanently retired  
**Disposition:** WORKING CANON — evidence-edge ledger established

## 1. Mission

Passes 3–6 recovered the programmer model, state channels, causal chains, and strategic transitions. Pass 6 QC identified the remaining epistemic risk: a valid historical edge can acquire unsupported strategic meaning when several edges are compressed into one sentence.

This pass restores edge-level provenance.

Canonical transition:

`GAME PROBLEM -> OBSERVATION -> CLASSIFICATION -> STATE -> REQUIREMENT -> COMMITMENT -> AUTHORITY -> ACTION -> WORLD POSTCONDITION -> STRATEGIC POSTCONDITION`

Every arrow is independently graded.

## 2. Evidence contract

- **DIRECT:** exact executable source supports the edge.
- **COMPOSED:** multiple DIRECT edges establish the relationship.
- **INFERRED:** strategic meaning reconstructed from repeated behavior.
- **AEGIS-GENERALIZATION:** new architecture derived from historical evidence.
- **UNCERTAIN:** insufficient evidence.

Closure is independent:

- **CONTROL:** state reaches a command/control consequence.
- **WORLD:** game-state change is independently observed/proven.
- **STRATEGIC:** intended game relationship improves and is demonstrated.

A CONTROL edge never automatically upgrades to WORLD or STRATEGIC.

## 3. Edge ledger

| ID | Transition | Source anchor | Edge mechanism | Grade | Closure | Alternative explanation / falsifier | AEGIS treatment |
|---|---|---|---|---|---|---|---|
| E01 | enemy cavalry -> threat aggregate | `threats.per`, cavalry/cavalry-archer measurement branches | enemy measurement accumulated into threat state | DIRECT | CONTROL | aggregate may be a count rather than normalized threat score | preserve as typed observation/aggregate |
| E02 | threat aggregate -> camel response | `threats.per` cavalry aggregate consumers; `units.per` `traincamel` branches | threshold/context enables camel production state | DIRECT/COMPOSED | CONTROL | response may address only a subset of conditions | preserve; do not call universal optimizer |
| E03 | camel response -> production | `units.per` `traincamel yes`; stable search; `can-train` guards; training action | requirement -> production search -> feasibility -> train | DIRECT | CONTROL | command proves invocation, not completed unit | preserve as capability pipeline |
| E04 | research escrow -> Castle/Imperial research | `escrow.per`: `escrow-flag` + `can-research-with-escrow` -> `research` | protected resource state gates research command | DIRECT | CONTROL | strategic-number age write may be controller state only | preserve reservation/feasibility separation |
| E05 | research command -> age controller state | `escrow.per` Castle/Imperial blocks | research action followed by `sn-current-age` write | DIRECT | CONTROL | controller may anticipate completion | treat as controller state, not world proof |
| E06 | age state -> changed production/economy options | distributed age readers | downstream eligibility changes with age state | COMPOSED | CONTROL | exact post-age capability depends on prerequisites | preserve transition graph |
| E07 | fortification observation -> retreat state | HD attack/retreat rules, approx. 32578–32718 | defensive conditions write retreat/attack state | DIRECT | CONTROL | retreat may be temporary controller response | preserve attack lifecycle |
| E08 | retreat state -> retreat command | HD attack/retreat consumer, approx. 34013 | retreat state enables `up-retreat-now`; state then clears | DIRECT | CONTROL | command may fail or be delayed | require world verification |
| E09 | retreat -> restart state | HD restart case, approx. 35153 onward | restart state resets attack-group controls under guards | DIRECT | CONTROL | reset may not yield renewed attack | separate tactical reset from strategic success |
| E10 | restart state -> renewed attack | restart/attack consumer chain | reset permits later attack eligibility | COMPOSED | CONTROL | renewed attack may never become favorable | require operational postcondition |
| E11 | 504/505 search -> movement point | `general.per`; `temporary-goal2=-1`; `temporary-goal > temporary-goal2` | argmax pair -> midpoint -> centerward shift -> move | DIRECT | CONTROL | higher strategic purpose unresolved | preserve algorithm; purpose remains inferred |
| E12 | scout danger -> pivot | `scoutcontrol.per` path-quarterstep / pivot geometry | candidate pivot evaluated against local danger/path state | DIRECT | CONTROL | objective may be safety/distance/other | separate geometry from information-value claim |
| E13 | pivot -> scout movement | `scoutcontrol.per` target-point/action chain | selected point becomes movement action | DIRECT | CONTROL | arrival requires world evidence | preserve candidate-search architecture |
| E14 | scouting -> strategic belief | scout observations consumed by strategic/threat state | observations affect later classifications | COMPOSED | CONTROL | some scans may be tactical-only | typed information evidence |
| E15 | gatherer allocation -> resource throughput | `gatherers.per` contextual percentage writers | SN changes alter worker allocation | COMPOSED | CONTROL | throughput depends on task/map conditions | demand-driven allocation model |
| E16 | reservation -> production/research competition | `escrow.per` + resource-control | reservation protects one conversion from competing spend | COMPOSED | CONTROL | priority policy varies by subsystem | explicit reservation ledger |
| E17 | unit-goal -> train authorization | `unit-goal` consumers in `units.per` | persistent requirement enables production branches | COMPOSED | CONTROL | unit-goal may represent broader mode | model as requirement, not queue entry |
| E18 | position -> strategy/unit/control | HD position casebook, approx. 5252–5262 | position writer co-writes strategic channels | DIRECT | CONTROL | classification may be map-role-specific | preserve upstream map-role state |
| E19 | building failure -> fallback | building/rebuild branches | failure routes to alternate construction path | DIRECT/COMPOSED | CONTROL | exact detector varies | explicit failure/recovery policy |
| E20 | timer entry -> reassessment | attack/scout/restart timer patterns | timer changes future eligibility | DIRECT | CONTROL | purpose differs by timer | attach timer to named transition |

## 4. Critical findings

### 4.1 Historical source is strongest at the control layer

The source reliably establishes observations, state writes, guards, searches, commands, resets, and downstream eligibility. It is substantially weaker at proving that a commanded world transition occurred and weaker still at proving strategic success.

### 4.2 Threat -> capability is the strongest strategic chain

The cavalry/cavalry-archer path is unusually complete: enemy measurement is compressed into reusable state, that state participates in camel-response conditions, and `units.per` contains the downstream production mechanism.

This supports a context-sensitive counter-capability interpretation. It does not establish a general-purpose counter-composition optimizer.

### 4.3 Attack -> retreat -> reset/restart is the strongest lifecycle chain

Distinct attack, retreat, and restart state plus temporal controls establish a real lifecycle rather than a boolean attack flag. They do not prove that every retreat preserved military mass or every restart produced successful renewed pressure.

### 4.4 504/505 is the strongest algorithmic micro-case

The `-1` sentinel and greater-than comparison establish maximum-distance selection, not generic minimum/best-distance selection. The midpoint and centerward shift then convert the result into movement. The strategic purpose remains unresolved.

### 4.5 Resource control is a network property

No single escrow rule proves a universal resource-allocation doctrine. The opportunity-cost interpretation emerges from repeated interactions among escrow, gatherer allocation, production, technology, and strategic state.

## 5. Transition conservation law

Every strategic transition must consume at least one scarce budget:

`RESOURCE | PRODUCTION CAPACITY | MILITARY MASS | TIME | MAP ACCESS | INFORMATION | OPTIONALITY`

If an AEGIS proposal appears to improve every dimension simultaneously, identify the conversion paying for that improvement or reject the model.

Examples:

- Age-up converts resources/time into future capability.
- Siege converts resources/production into a changed fortification relationship.
- Retreat converts immediate position/initiative into preserved optionality.
- Scouting converts scout time/risk into information.
- Farms convert wood into future food throughput.

These are AEGIS strategic models, not claims that the historical source computes explicit equations.

## 6. AEGIS ownership model

The historical distributed channels imply seven explicit ownership roles for AEGIS:

1. **Observation owner** — establishes what is evidenced.
2. **Belief owner** — maintains interpretation and confidence.
3. **Objective owner** — owns strategic purpose.
4. **Commitment owner** — reserves resources/capacity.
5. **Authority owner** — grants side-effect permission.
6. **Execution owner** — issues concrete action.
7. **Verification/recovery owner** — decides whether the result occurred and what happens next.

This is an AEGIS architecture, not a claim that these were explicit historical modules.

## 7. Highest-value implementation chains

### C1 — Threat to capability
`OBSERVE ENEMY -> CLASSIFY THREAT -> DEFINE REQUIRED CAPABILITY -> RESERVE -> PRODUCE -> VERIFY -> REASSESS`

### C2 — Strategic transition
`DESIRE AGE/TECH -> PROTECT RESOURCES -> CHECK FEASIBILITY -> RESEARCH -> VERIFY NEW CAPABILITY -> REALLOCATE`

### C3 — Military lifecycle
`CAPABILITY -> ATTACK COMMITMENT -> ENGAGE -> ASSESS -> RETREAT/CONTINUE -> REGROUP -> RESTART/ABANDON`

### C4 — Information to action
`INFORMATION GAP -> SCOUT CANDIDATES -> SAFETY/UTILITY EVALUATION -> MOVE -> OBSERVE -> UPDATE BELIEF`

These chains span most strategic subsystems and are more valuable than isolated `.per` rules.

## 8. Deliberately open edges

- individual production completion/spawn identity in the reference replay;
- physical retreat success from controller-state writes;
- strategic success of renewed attacks;
- exact information-value objective of scouting;
- exact strategic purpose of the 504/505 maximum-distance point;
- universal optimality of historical resource allocation;
- predictive opponent modeling as an explicit historical object;
- current-build semantics beyond frozen Layer-1 evidence.

## 9. Pass disposition

**PASS 35: ACCEPT — EVIDENCE-EDGE LEDGER ESTABLISHED.**

The methodological result is more important than another list of mechanisms: strategic claims must now be assembled from individually graded causal edges. This sharply reduces accidental promotion from control evidence to claims about author intent or game outcome.

**Next target:** formalize C1 — Threat -> Capability into the first AEGIS strategic transition specification, using the historically strongest closed chain as the implementation template.
