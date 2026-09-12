# AEGIS Competency 5 — Production Authority v0.2 Cross-Reference

**Date:** 2026-09-12  
**Scope:** AIByzBuild runtime corpus + AEGIS uploaded AegisProm + AoE2DE AIBuilder + AoE2 AI Scripting Encyclopedia  
**Targets:** spearmen, skirmishers, archers, camelriders, monks, bombardcannons, fireships, uniqueunits

## Executive finding

Production Authority v0.2 is directionally correct, but the cross-reference changes one important implementation rule: **do not replace the AiBuilder training executor and do not import the AegisProm production executor wholesale.**

The native AIByzBuild boundary is already sound:

```text
composition authority
  -> desired-number-X
  -> militaryUnits.per
  -> unit-type-count-total X < desired-number-X
  -> can-train X
  -> train X
```

AoE2 AIBuilder is explicitly a basic build/train/attack generator whose generated `.per` files are intended to use common library behavior. Its training model is therefore the correct physical-execution substrate for AEGIS rather than something to bypass. The AI Scripting Encyclopedia independently documents `set-goal`, `can-train`, `train`, and `unit-type-count-total` as native scripting primitives.

The defect remains upstream: `phaseUpdate.per` and `byzPolicy.per` both write the same `desired-number-*` goals. The final composition target therefore needs one authority layer.

## Evidence classes

| Finding | Evidence |
|---|---|
| `militaryUnits.per` is the physical training executor | DIRECT — installed AIByzBuild |
| `phaseUpdate.per` writes generic production caps | DIRECT — installed AIByzBuild |
| `byzPolicy.per` writes Byzantine baselines and responses | DIRECT — installed AIByzBuild |
| goals can be used as mutable state/variables | DIRECT/COMPOSED — AI Scripting Encyclopedia |
| `can-train` is the native training-feasibility gate | DIRECT — AI Scripting Encyclopedia |
| `unit-type-count-total` is the count interface used by the executor | DIRECT — AIByzBuild + Encyclopedia |
| goal updates can be used as intermediate state | DIRECT — Encyclopedia |
| textual ordering can matter in some AI scripts because different facts update at different times | DIRECT historical scripting evidence; not promoted to a universal DE rule |
| AEGIS should own policy/authorization while AiBuilder owns physical training | AEGIS architectural rule derived from the cross-reference |

## 1. AIBuilder cross-reference

### Native executor

Installed `AIByzBuild/militaryUnits.per` contains the canonical executor for all eight targets.

```text
spearman-line       -> desired-number-spearmen
skirmisher-line     -> desired-number-skirmishers
archer-line         -> desired-number-archers
camel-line          -> desired-number-camelriders
monk-set / monk     -> desired-number-monks
bombard-cannon      -> desired-number-bombardcannons
fire-ship-line      -> desired-number-fireships
my-unique-unit-line -> desired-number-uniqueunits
```

Each uses the same native pattern:

```text
unit-type-count-total ...
g:< desired-number-X
can-train X
-> train X
```

This is exactly the abstraction AEGIS should consume, not duplicate.

### AIBuilder upgrade coupling

The AIBuilder upgrade library also consumes the same unit-line counts to gate research. Examples include spearman -> pikeman -> halberdier, archer -> crossbow -> arbalest, and skirmisher -> elite skirmisher. It uses `can-research-with-escrow` and releases escrow before research.

Therefore the composition authority must not treat the production target as the entire lifecycle. A target must coexist with the existing upgrade pipeline.

## 2. AI Scripting Encyclopedia cross-reference

The Encyclopedia confirms:

1. `set-goal` writes a goal value.
2. Goal operators use `g:` when comparing a goal to another goal.
3. `can-train` checks whether training can start.
4. `can-train-with-escrow` is a separate feasibility interface.
5. `train` is the physical training action.
6. `unit-type-count-total` is the native count interface.
7. Training-queue behavior can affect `can-train` and `train` when the relevant strategic number is enabled.

### Consequence for AEGIS

`can-train` is **not** a strategic authorization mechanism. It is an execution-feasibility fact.

Therefore:

```text
AEGIS authorization != can-train
AEGIS authorization -> desired-number-X
can-train -> physical feasibility
train -> physical command
```

This preserves the authority boundary.

## 3. AEGISProm cross-reference

The uploaded `AegisProm` contains two relevant candidate modules:

- `AEGIS-military-production-v0.per`
- `AEGIS-production-reservation-authority-v0.per`

The military-production candidate is deliberately bounded to a **spearman/cavalry-response slice**. It models an explicit lifecycle:

```text
idle
-> authorized
-> issued
-> pending
-> world-observed
-> causally-confirmed
or failed
-> reassessment
```

The reservation module adds:

```text
FREE
-> RESERVED
-> IN_FLIGHT
-> RELEASE_PENDING
-> RELEASED
```

with generation, request ID, authorization ID, owner, resource key, unit line, validity, expiry and release reason.

### Critical boundary

Those AegisProm modules are candidate architecture, not the current AIByzBuild executor. The reservation authority currently models only the `spearman-line` conflict resource and is explicitly marked candidate/not loaded. It therefore cannot be promoted as the eight-target production implementation without additional qualification.

### What should be ported functionally

Port the **authority concepts**, not the executor code:

- request identity
- authorization identity
- generation fencing
- explicit expiry
- exclusive ownership where resource contention requires it
- pending state
- world-state verification
- failure
- release
- reassessment

Do not replace the native `militaryUnits.per` executor merely to reproduce those concepts.

## 4. AIByzBuild cross-reference

Current installed root structure loads the Byzantine policy around the existing native modules. `constantsUP.per` provides the AEGIS private threat-state goals, while `byzPolicy.per` consumes them to raise production floors.

The current policy contains direct writes such as:

```text
cavalry threat -> spearmen 18 + camels 8
archer threat  -> skirmishers 18
infantry threat -> archers 18
warship threat -> fireships 6 + docks 2
under attack -> spearmen 12 + skirmishers 12
```

These are legitimate policy decisions, but they currently write final `desired-number-*` goals directly.

At the same time `phaseUpdate.per` writes phase/difficulty values for the same goals.

That is the authority defect v0.2 must remove.

## 5. Correct v0.2 architecture

Do not create another training executor.

Use four layers:

```text
PHASE REQUIREMENT
        |
BYZANTINE BASELINE REQUIREMENT
        |
COUNTER REQUIREMENT
        |
THREAT / DEFENSE REQUIREMENT
        v
COMPOSITION AUTHORITY
        |
        v
FINAL desired-number-X
        |
        v
AIBuilder militaryUnits.per
        |
        v
can-train / train
```

The policy layers must stop writing the final target directly.

## 6. How to implement precedence without accidental file-order authority

A literal `max()` function is not available as a normal `.per` abstraction. Use **requirement goals plus a final resolver**.

Each target gets private requirement goals, for example:

```text
req-phase-spearmen
req-byz-spearmen
req-counter-spearmen
req-threat-spearmen
req-defense-spearmen
final-spearmen
```

The source modules write only their requirement goals.

The resolver is the only writer of `desired-number-spearmen`.

### Resolver rule

The resolver selects the highest active authority tier:

```text
DEFENSE > THREAT > COUNTER > BYZANTINE BASELINE > PHASE BASELINE
```

Within a tier, use the largest requested value.

The resolver must also be written so that a lower tier cannot clear a higher tier merely because its rule is later in the file.

## 7. Expiry contract

Persistent requirements:

- phase baseline
- Byzantine age baseline

Conditional requirements:

- local counter
- fresh threat
- immediate defense

Every conditional requirement must explicitly clear when its source condition is no longer valid.

Threat requirements additionally require an evidence-validity boundary. The current AEGIS threat window remains an AEGIS policy value, not an engine semantic.

No temporary requirement may silently renew itself after its evidence expires.

## 8. Verification contract

Every target must be qualified through the same chain:

```text
V0 policy condition
-> V1 requirement state
-> V2 final desired-number-X
-> V3 count deficit + can-train
-> V4 train command accepted
-> V5 pending/world-state transition
-> V6 persistence
-> V7 expiry/release
-> V8 reassessment
```

Command acceptance is never sufficient evidence of world-state completion.

For the AEGISProm causal-production slice, the stronger attribution contract additionally requires request identity, authorization identity, generation identity, pending observation, pending resolution, world transition and alternative-producer exclusion before causal confirmation.

## 9. Eight-target authority cross-reference

| Target | Native executor | Byzantine requirements | Adaptive requirements | AEGISProm status | v0.2 action |
|---|---|---|---|---|---|
| Spearmen | `spearman-line` | Feudal 6 / Castle 8 / Imperial 20 | local cavalry, AEGIS cavalry, defense | Candidate lifecycle + reservation exists | First full authority implementation |
| Skirmishers | `skirmisher-line` | 8 / 10 / 20 | archers, local defense | No dedicated production lifecycle | Port authority pattern only |
| Archers | `archer-line` | 10 / 12 / 16 | skirmishers, infantry | No dedicated production lifecycle | Port authority pattern only |
| Camel Riders | `camel-line` | Castle 10 / Imperial 4 | knights/cavalry | No dedicated production lifecycle | Port authority pattern only |
| Monks | `monk` / `monk-set` | Castle 3 / Imperial 5 | none currently | No dedicated lifecycle | Baseline authority only |
| Bombard Cannons | `bombard-cannon` | Imperial 3 | none currently | No dedicated lifecycle | Baseline + workshop dependency |
| Fireships | `fire-ship-line` | no permanent Byzantine floor | warship threat 6 | No dedicated lifecycle | Threat authority + dock dependency |
| Unique Units | `my-unique-unit-line` | Castle 6 / Imperial 10 | none currently | Cataphract mapping not independently qualified | Authority + explicit identity qualification |

## 10. New finding: resource reservation is not required for every target

The AegisProm reservation authority is valuable where two policy producers compete for an exclusive resource/production request. It should not automatically be attached to every `desired-number-*` target.

For v0.2, composition arbitration and resource reservation remain separate contracts:

```text
composition authority
!=
resource reservation authority
```

Reservation becomes necessary only when competing producers require an exclusive claim that native `can-train` does not express.

## 11. Competency-5 promotion gate

Competency 5 remains incomplete until all eight targets have:

1. persistent baseline requirement;
2. adaptive requirement where evidence exists;
3. explicit precedence;
4. explicit expiry;
5. one final composition writer;
6. unchanged native executor;
7. production-capacity dependency where required;
8. upgrade continuity;
9. pending/world verification;
10. reassessment after release.

### Immediate implementation order

1. Implement the authority pattern on **spearmen** first because AegisProm already provides a bounded production/reservation lifecycle for that unit.
2. Keep `militaryUnits.per` unchanged.
3. Convert phase and Byzantine spearman writers into requirement writers.
4. Make the final resolver the only writer of `desired-number-spearmen`.
5. Verify expiry and baseline recovery.
6. Generalize the same pattern to skirmishers, archers, camels, monks, bombard cannons, fireships and unique units.
7. Only after the authority graph is clean should additional composition sophistication be added.

## Status

**Production Authority v0.2 design: QUALIFIED as an architectural design.**  
**Runtime implementation: NOT YET QUALIFIED.**  
**Eight-target final ownership: NOT YET QUALIFIED.**
