# AEGIS-Lite Final Engineering Handoff — 2026-09-06

## Mission

AEGIS-BYZ is a serious AoE2DE AI engineering program. This document is the handoff to the next project lead / ChatGPT instance. Treat it as an active engineering program, not a toy bot and not a green-field exercise.

The architecture is:

```text
WORLD MODEL
  -> BELIEF MODEL
  -> SITUATION ANALYSIS
  -> OBJECTIVES
  -> PLANNING
  -> DECISION
  -> COMMITMENT
  -> EXECUTION
  -> VERIFICATION
  -> RECOVERY
```

The first vertical slice is **Cavalry Threat Containment**.

The current objective is NOT to make the bot look complete. The objective is to prove that the architecture survives contact with the actual AoE2DE engine, then grow execution from qualified primitives.

## Evidence doctrine

Never collapse these distinctions:

```text
representation != reality
replay != game state
command != outcome
validator != engine
number != channel
architecture != runtime proof
startup != rule execution
rule execution != semantic correctness
external observation != architectural authority
```

Use exactly these evidence classes:

- PROVEN — directly demonstrated on the target machine/build.
- STOCK-EVIDENCED — directly found in the target stock package, but not necessarily runtime-qualified by AEGIS.
- DOCUMENTED — supported by authoritative external documentation/source.
- INFERRED — reasoned but not machine-demonstrated.
- UNKNOWN — not established.
- REJECTED — explicitly ruled out by evidence.

The most dangerous failure mode is silently converting UNKNOWN into PROVEN because a file parses, a process starts, or a validator accepts syntax.

## Target build

- AoE2DE: `101.103.48987.0`
- Steam BuildID: `24094652`
- executable: `AoE2DE_s.exe`
- executable SHA-256: `6378CA6F1BFD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- stock AI root: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai`

The stock AI root was restored and remains the reference installation. Do not contaminate it with experiments.

## Repository

Canonical repository: `justhop90-bot/AiByz`  
Active branch: `aegis/external-harness-v1-2026-09-05`  
Current branch HEAD at handoff: `cfc271b627815bf83a24564868343f41c2cc484c`

PR #43 remains open and unmerged. Its purpose is the retail-safe external harness. It is **not** the AEGIS runtime authority and is deliberately not runtime-qualified.

GitHub Issue #46 is the structural reconciliation gate.

## What has actually been built

The published AEGIS-Lite chain contains eight production `.per` files:

```text
AEGIS-BYZ.per
AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per
AegisProm/Aegis-belief.per
AegisProm/Aegis-situation.per
AegisProm/Aegis-objectives.per
AegisProm/Aegis-planning.per
AegisProm/Aegis-decision.per
AegisProm/Aegis-commitment.per
```

Generation probe:
`AegisProm/Aegis-generation-probe.per`

The probe is experimental instrumentation and is intentionally NOT loaded by the production entrypoint.

The individual modules were sequentially machine-tested during development. Reported results:

- Architect: started successfully.
- Carpenter modular load: started successfully.
- Belief: worked after correcting native `up-modify-goal` copy syntax.
- Situation: worked after correcting C-style comments to native `.per` comments.
- Objectives: worked.
- Planning: worked after correcting an undefined urgency identifier.
- Decision: worked.
- Commitment: worked.

Those tests establish useful runtime evidence, but they do not prove complete end-to-end propagation or sensor semantics.

## Structural reconciliation completed

The earlier modular package contained 27 duplicate World Model declarations in the loaded closure. They were caused by the Carpenter P2 artifact carrying its own copy of the World Model.

The reconciliation established:

- **Architect owns World Model semantics/state/qualification.**
- **Carpenter owns native sensor expression.**
- **Downstream modules own semantic transformation only.**
- **Only one Carpenter is loaded.**
- The obsolete unloaded `Aegis-carpenter.per` was removed after its SHA was recorded; Git history preserves it.

Fresh target-machine audit after reconciliation:

- 8 closure files
- 129 declaration rows
- 129 unique symbols
- 237 resolved goal operands
- 0 high-goal operands
- 0 duplicate declarations

The historical audit artifact at `audit_reconciled_2026-09-06/audit_report.md` reports the pre-reconciliation state (`156/129/356/0/27`). It is evidence of the defect, not the current closure authority.

The current reconciliation/source-hash documents are the authoritative structural records.

## IMPORTANT: one architectural inconsistency remains

Do not miss this.

The intended ownership model says the Architect owns generation semantics. However, the reconciled Carpenter currently contains:

```text
(up-modify-goal aegis-wm-generation c:+ 1)
(up-modify-goal aegis-wm-cycle c:+ 1)
```

Therefore the **declared ownership and implemented mutation path are not yet perfectly aligned**.

This is not a reason to panic or restart. It is a reason to stop and repair the ownership boundary before treating generation propagation as qualified.

The next lead should decide whether:

1. the Carpenter emits only sensor facts and a separate Architect-owned coordinator advances generation/cycle; or
2. generation is explicitly reclassified as an adapter-owned publication counter.

The architecture currently says option 1. Preserve that unless experiments prove a better boundary.

Do NOT “fix” this blindly. First understand native rule ordering/timer behavior and then make the smallest auditable change.

## Sensor truth remains UNKNOWN

Current probe details are intentionally conservative:

- `aegis-knight = 38` is a concrete Knight unit ID, not `knight-line`.
- `up-get-fact-max any-enemy unit-type-count aegis-knight` is not yet qualified as a complete enemy cavalry aggregate.
- `aegis-wm-observed-at = 1` is a marker, not a timestamp.
- `aegis-wm-time` is an advancing game-time channel, but exact unit correspondence remains separately unqualified.
- `aegis-wm-valid = 1` is an architectural qualification state, not independent truth certification.

Do not replace Knight 38 with an assumed `knight-line` alias merely to make the architecture look generalized. Qualify the actual primitive first.

## Generation experiment

The highest-value next experiment is already designed:

`AEGIS_GENERATION_PROPAGATION_EXPERIMENT_2026-09-06.md`

Probe:
`AegisProm/Aegis-generation-probe.per`

Required experiment:

```text
World Model generation N
        |
        v
Belief N -> Situation N -> Objective N -> Planning N
        -> Decision N -> Commitment N
        |
        v
World Model generation N+1
        |
        v
all downstream layers must publish N+1
```

Then separately test stale N after N+1.

Then separately test UNKNOWN/zero/absence.

Do not merge these experiments into one ambiguous test.

Every result must bind:

- executable hash
- build ID/version
- package/source hash
- probe hash
- raw diagnostic output
- generation sequence
- verdict
- evidence class

## External runtime observation

CA:DE has already been deeply investigated and is useful as an **independent observation/corroboration backend**, not as the AEGIS architectural dependency.

Established facts include:

- local CA:DE gRPC endpoint at `127.0.0.1:4341`
- authenticated TLS 1.3 / HTTP2 channel
- API version 20
- game version 180059
- structured world-state patches are observable
- advancing world-time signal exists
- entity records expose fields such as entity ID, owner, action, production queue, construction progress, position, visibility/fog

But exact world-time units, patch-ID semantics, entity lineage, command acceptance/completion semantics, and DE_QUEUE→CREATED correspondence remain unqualified.

The CA:DE observer should be used when it can independently corroborate an AEGIS transition. Do not make private CA:DE IPC a core `.per` dependency.

## Replay infrastructure

The replay work is valuable supporting infrastructure, not a prerequisite to proving the AEGIS skeleton.

The canonical replay parser work established:

- ACTION records can prove observed command issuance in the replay representation.
- SYNC time is accumulated from payload increments.
- Replay does not directly provide a live world-object snapshot.
- Accepted / queued / pending / created / available / effective are not automatically proven by replay alone.

Do not let replay archaeology consume the project while the native state machine remains unqualified.

## Stock AI archaeology: the important lesson

The stock `/ai` directory is much larger than the actual runtime import closure.

For ABI reasoning, the important untouched stock closure is the four-file HD runtime package:

```text
AI (HD version).per
Promisory/defaultConstants.per
Promisory/finaling.per
Promisory/finalingConstants.per
```

Physical files outside that closure are not automatically runtime dependencies.

This distinction saved us from a major false conclusion earlier. Always ask: **what is physically present, what is loaded, and what is actually executed?**

## Native scripting lessons

AoE2 `.per` is a constrained native rule/state-machine language, not C/C++.

Use native `.per` comment syntax (`;`). C-style `/* ... */` comments caused a real invalid-preprocessor-directive failure.

Be extremely careful with symbol names. One incorrect identifier can kill an otherwise coherent module. The Planning failure was caused by using `aegis-objective-urgency-high`, which was never declared; the correct urgency constants belonged to Situation Analysis.

For goal copies, use the native form that has actually survived machine testing:

```text
(up-modify-goal target g:= source)
```

Do not infer syntax from C-like languages.

For native facts, distinguish:

- `up-get-fact`
- `up-get-fact-max`
- `up-find-player`
- ordinary conditions/actions

A validator can tell you that syntax is recognized. It cannot tell you that the target engine interprets the value the way your architecture assumes.

## The knight-line trap

This is one of the most important historical lessons.

`knight-line` is a unit-line identifier. It is not simply the concrete Knight unit ID `38`.

The stock HD package conditionally redefines `knight-line` depending on civilization. Therefore a universal replacement of `knight-line` with `38` is not a valid architectural generalization.

At most, Knight 38 is a deliberately narrow calibration probe.

The earlier “Invalid Identifier” incident at `ADPromisory/ADByzantineIntelligence.per:345` taught another crucial lesson: a validator's corpus may disagree with what the engine can accept in a specific fact context. Never “repair” a valid engine construct solely to satisfy a weak validator without proving the engine behavior.

## Runtime launch reality

Direct retail launch surfaces were investigated extensively.

No reliable autonomous AI-match launch path has yet been established through the tested SCRIPT/SCRIPTREPORT/RUNNING_AUTOTEST/AIDEBUGGING/AISCRIPTDEBUGGING/RANDOMGAME/RANDOMMAP/GAM paths.

Therefore:

**Do not claim that AEGIS has been proven in a controlled autonomous match. It has not.**

A successful module startup is still valuable evidence, but it is not a complete runtime qualification.

## What NOT to do

Do not:

- restart the project from theory;
- immediately add real execution commands;
- use stock Promisory as an accidental architectural dependency;
- turn CA:DE into a hard dependency;
- equate replay commands with engine outcomes;
- equate process survival with semantic success;
- treat validator success as engine truth;
- change Knight 38 to Knight-line without calibration;
- claim the seven-layer chain is end-to-end proven;
- silently edit the stock AI tree;
- overwrite the machine-tested package without preserving a hash/diff;
- mix stale-generation, missing-observation, and zero-value experiments;
- inflate `valid` semantics beyond the evidence.

## What to do next — exact order

### Gate 1 — reconcile generation ownership

Inspect the current root/P2 interaction and remove the generation mutation from the Carpenter only after designing the Architect-side publication edge correctly.

Do not assume rule ordering. Test it.

### Gate 2 — machine-load the exact reconciled package

Use the disposable package prepared at:

`C:\Users\justh\Games\Age of Empires 2 DE\76561198093432383\mods\local\AEGIS-P0-Reconciled`

Verify its eight files against GitHub before launch.

Do not touch stock `/ai`.

### Gate 3 — prove generation propagation

Load the generation probe in a disposable experimental package only.

Require N across all seven layers, then N+1 across all seven layers.

### Gate 4 — prove stale rejection

Create a controlled N → N+1 transition and deliberately test whether stale N can authorize current state.

If the engine cannot expose the distinction, record UNKNOWN. Do not manufacture PASS.

### Gate 5 — qualify sensor semantics

Run narrow calibration experiments for each sensor independently.

Start with time, population, age, player search, own camel count, and enemy Knight count.

Then tackle the generalized cavalry-line problem.

### Gate 6 — only then add Execution skeleton

Execution initially records:

```text
AUTHORIZED
  -> ISSUED
  -> ACCEPTED/QUEUED
  -> PENDING
  -> CREATED
  -> AVAILABLE
  -> DEPLOYED
  -> EFFECTIVE
```

Do not skip states merely because the engine makes them difficult to observe.

### Gate 7 — qualify one command end-to-end

Only one command. One controlled scenario. One immutable source/package/build binding. One independent observation path where possible.

That single vertical slice is worth more than 500 lines of unqualified execution code.

## Engineering style for the next lead

Act like a systems engineer and experimental scientist simultaneously.

When something fails, ask:

1. Did the source parse?
2. Did the package load?
3. Did the rule execute?
4. Did the value change?
5. Did the value mean what we think it means?
6. Did the downstream layer consume the same generation?
7. Did the engine accept the eventual command?
8. Did the world change?
9. Can an independent observer corroborate that change?

Never jump from step 1 to step 9.

Keep a ledger of assumptions. Every time you write “obviously,” stop and ask what evidence would falsify it.

## The deeper design principle

The strength of AEGIS is not clever `.per` syntax.

It is the separation of authority:

```text
WORLD MODEL
  owns state

BELIEF
  owns bounded interpretation

SITUATION
  owns classification

OBJECTIVE
  owns what must be achieved

PLANNING
  owns abstract means

DECISION
  owns selected bounded choice

COMMITMENT
  owns authorization

EXECUTION
  owns issuance

VERIFICATION
  owns outcome evidence

RECOVERY
  owns what happens when reality disagrees
```

If a module starts owning two of these without an explicit architectural reason, investigate it.

## Final instruction

You are not inheriting a pile of `.per` files. You are inheriting an evidence-controlled attempt to build a genuinely autonomous Byzantine AI architecture inside a hostile, constrained native scripting environment.

Do not be impressed by the amount of code. Be impressed only by what has survived experiment.

Preserve what was tested. Challenge what was assumed. Record what was learned. Make every promotion in evidence level earned.

The project is ready for the next empirical step. It is **not** ready for execution authority yet.

Finish the skeleton. Prove generation. Prove stale rejection. Qualify the sensors. Then earn Execution.

That is the path.
