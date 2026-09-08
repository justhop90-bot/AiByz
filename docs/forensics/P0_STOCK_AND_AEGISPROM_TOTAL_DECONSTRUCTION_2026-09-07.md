# P0 Stock + AegisProm Total Deconstruction — 2026-09-07

## Scope

This is the first forensic pass of the total rework. It establishes the actual machine state before any major subsystem is rebuilt. Evidence comes from the installed AoE2DE AI directory, not from prior generated files or assumptions.

## 1. Stock main `.per`

Machine path:
`C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai\AI (HD version).per`

- 36,141 lines
- 1,167,238 bytes
- SHA-256: `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`
- 2,429 `defrule` blocks
- 4,222 `defconst` declarations
- 79 occurrences of `up-jump-rule`

The file is a flattened civilization OS. It begins with constants and conditional civilization definitions, then contains the runtime rule corpus, with a final conditional load of `Promisory\\finaling`.

### Major runtime regions

| Region | Approx. lines | Rules | Interpretation |
|---|---:|---:|---|
| Constant/preprocessor envelope | 1–4,983 | 0 | ABI constants, civ-specific constants, strategic numbers, IDs |
| Core civilization initialization/runtime | 4,984–6,267 | 79+ | foundational initialization and persistent state |
| Navy initialization | 6,268–6,584 | 26 | naval state/bootstrap |
| Superiority | 6,585–7,126 | 53 | military superiority / matchup state |
| Scouting | 7,127–7,521 | 31 | information acquisition and scout control |
| Strategy selection | 7,522–7,893 | 26 | strategy admission/selection |
| Civ-specific strategy | 7,894–15,900 | 620 | civilization-specific policy and build/army choices |
| Boar hunting | 15,901–16,001 | 5 | dedicated food acquisition |
| Resource management + age up | 16,002–19,622 | 272 | economic state, allocation, aging |
| Basics | 19,623–21,050 | 113 | general runtime support |
| Research | 21,051–22,561 | 131 | technology/research control |
| Siege | 22,562–23,226 | 43 | siege production/use |
| Trade | 23,227–23,361 | 12 | trade subsystem |
| Villagers | 23,362–23,777 | 32 | civilian production/task support |
| Buildings | 23,778–26,207 | 195 | construction system |
| Units | 26,208–26,402 | 14 | unit support |
| Navy | 26,403–29,128 | 190 | naval production/control |
| Other researches | 29,129–29,681 | 43 | additional research handling |
| Gatherer percentages | 29,682–32,470 | 230 | economic role/allocation state machine |
| Attack + retreat | 32,471–34,344 | 135 | military execution and retreat |
| Navy management | 34,345–34,586 | 22 | naval late/runtime management |
| Optional cheats | 34,587–34,645 | 6 | cheat/debug behavior |
| Human cooperation | 34,646–34,805 | 12 | co-op/taunt interaction |
| Increase TS | 34,806–36,141 | 112 | town-size / placement support |

These boundaries are forensic section markers, not yet proven module boundaries. They must not be blindly split into files until cross-section state dependencies are mapped.

## 2. Critical conclusion about the current AEGIS root

Machine comparison proves:

`AEGIS-BYZ.per == AI (HD version).per`

byte-for-byte.

Therefore the current root is a stock AI rehost, not the final AEGIS architecture.

Its active loads are:

```per
(load "Promisory\\defaultConstants")
(load "Promisory\\finalingConstants")
(load "Promisory\\finaling")
```

This is rejected as the final architecture.

## 3. AegisProm inventory

The current AegisProm directory contains 40 `.per` files. It includes:

- AEGIS foundation/state protocol
- cognition modules: belief, situation, objectives, planning, decision, commitment
- execution, verification, recovery
- economy and military services
- operations/carrier adapter
- civilian census/demand/lifecycle
- economic demand/arbitration
- worker role census/vector
- worker target selection/task command/productivity/recovery/verification
- worker-loop qualification/probe
- source/dropsite serviceability
- stock constant/finaling rehosts
- two stock-derived 36,141-line civilization corpora

### Current AEGIS-specific module sizes

| Module | Lines | Rules | Defconst |
|---|---:|---:|---:|
| Foundation | 208 | 1 | 155 |
| Carpenter | 31 | 1 | 0 |
| Belief | 55 | 5 | 0 |
| Situation | 75 | 6 | 0 |
| Objectives | 73 | 6 | 0 |
| Planning | 79 | 7 | 0 |
| Decision | 31 | 3 | 0 |
| Commitment | 38 | 4 | 0 |
| Execution | 104 | 8 | 0 |
| Verification | 89 | 7 | 2 |
| Recovery | 67 | 4 | 1 |
| Economy | 66 | 5 | 2 |
| Military | 59 | 5 | 0 |
| Operations | 119 | 9 | 3 |
| Civilian census | 60 | 4 | 12 |
| Civilian demand | 58 | 3 | 13 |
| Civilian lifecycle reconciler | 71 | 5 | 14 |
| Economic demand | 62 | 2 | 20 |
| Economic demand arbitration | 97 | 7 | 18 |
| Source/dropsite serviceability | 126 | 8 | 21 |
| Villager production | 77 | 5 | 13 |
| Worker role census | 58 | 2 | 19 |
| Worker role vector | 113 | 8 | 22 |
| Worker target selection | 79 | 4 | 17 |
| Worker task command | 120 | 5 | 14 |
| Worker productivity observer | 74 | 4 | 20 |
| Worker recovery | 77 | 5 | 18 |
| Worker task verification | 103 | 6 | 22 |
| Worker-loop qualification | 29 | 1 | 8 |
| Dynamic worker-loop probe | 41 | 3 | 8 |

## 4. Stock rehost audit

Three AegisProm stock rehosts are exact copies of their Promisory counterparts:

- `AEGIS-stock-defaultConstants.per` == `Promisory/defaultConstants.per`
- `AEGIS-stock-finalingConstants.per` == `Promisory/finalingConstants.per`
- `AEGIS-stock-finaling.per` == `Promisory/finaling.per`

Exact hashes:

- defaultConstants: `187980fd34f5a5626955b20dd97114dc2212c9e7e86356014a7976dd1ae310ad`
- finalingConstants: `ce7a804a9855742cf4329c0fa44e603a5d19655951bf8e6bc5cf689264e07455`
- finaling: `95e18eb8b765a7f87ea499c25ed944d0e04c9abf932b70d8821ef1154d872e52`

These are valid evidence of source material, but they are not by themselves an AEGIS civilization substrate.

## 5. Existing AEGIS ABI/state design

Foundation reserves:

- World Model: 300–318
- Carpenter: 319–321
- Belief: 322–330
- Situation: 331–338
- Objectives: 339–345
- Planning: 346–349
- Decision: 350–353
- Commitment: 354–358
- Execution: 359–366
- Verification: 367–371
- Recovery: 372–376
- Services: 377–378
- Raw sensor frame: 379–391
- Economy: 392–396
- Military: 397–401
- Operations scout point: 402

Additional worker/civilian/economic namespaces occupy 421–563, with a dynamic worker-loop probe at 560–563 and qualification at 555–559.

This namespace discipline is a useful architectural foundation, but every interface still requires ABI/static/runtime qualification when it becomes part of the final bot.

## 6. What the deconstruction tells us

The 36k stock corpus cannot be treated as one monolithic “brain.” Its effective behavior emerges from interacting services and state machines:

`strategy -> demand -> arbitration -> resource/service selection -> authorization -> physical command -> engine state -> observation -> verification -> recovery -> new strategy/demand`

The stock AI uses persistent goals, strategic numbers, timers, object searches, status fields, action/order metadata, jump control flow, escrow, research/age state, construction state, military state, and recovery rules. Therefore module boundaries must be defined by state ownership and interfaces, not by file length or comments alone.

## 7. Three mandatory reviews for each rebuilt subsystem

### ABI/compiler/reverse-engineering

Verify every primitive, operand type, constant, goal/SN mutation, rule-pass assumption, jump behavior, object-search semantic, and command side effect against target-build evidence where available. Do not promote inference to fact.

### Byzantine strategy/civilization

Verify that the service supports Byzantine-specific strengths, weaknesses, unit transitions, economic timings, defensive identity, monastery/religion interaction, and late-game behavior rather than becoming a generic AI with Byzantine constants.

### AI(HD)/behavioral regression

Compare against the stock civilization OS for the behaviors that are deliberately retained: worker continuity, construction, production, research, scouting, military control, threat response, resource logistics, water/trade, and recovery. Preserve proven behavior where it is useful while changing ownership and control boundaries to AEGIS.

## 8. Static QC gate

Every major subsystem must pass static QC before runtime qualification. At minimum:

- parse/preprocessor balance
- duplicate/conflicting AEGIS-owned definitions
- namespace collisions
- illegal or unqualified primitives
- operand-shape/type hazards
- forbidden Promisory runtime loads
- accidental stock-root replacement
- rule-state terminal completeness
- generation fencing
- stale-frame rejection
- bounded retry behavior
- command/observation separation
- verification/recovery handoff
- no hidden ownership of another subsystem's state

Static QC is a gate, not a substitute for runtime testing.

## 9. Rebuild order established by this pass

1. Preserve the untouched stock corpus as the reference civilization OS.
2. Finish deconstructing the stock rule/state dependency graph.
3. Finish deconstructing the AegisProm ABI and existing AEGIS module interfaces.
4. Define final ownership boundaries and namespace contract.
5. Rebuild the civilization substrate service-by-service under AEGIS control.
6. Integrate cognition only through certified interfaces.
7. Remove all final-runtime dependence on `Promisory\\`.
8. Run static QC after each major subsystem.
9. Run target-build runtime qualification.
10. Run adversarial qualification and regression comparison.

## Status

**P0 DECONSTRUCTION: IN PROGRESS / BASELINE VERIFIED**

No major final implementation is authorized from this report alone. The next phase is dependency and interface reconstruction from the full stock corpus and the full AegisProm corpus.
