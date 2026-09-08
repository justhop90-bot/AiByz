# AEGIS / ByzBot — Final Build Readiness Gate

**Date:** 2026-09-08  
**Target:** AoE2DE 101.103.48987.0 / Steam BuildID 24094652  
**Base commit:** `c3bd849f0cfaf9a18103d5a0064fdab47fda3d4f`  
**Scope:** static archaeology, ABI reconciliation, architecture, implementation preflight. No AoE2DE launch or runtime experiment is part of this pass.

## Executive decision

**READY TO BEGIN FINAL BOT IMPLEMENTATION — WITH ONE EXPLICIT QUALIFICATION BOUNDARY.**

The project has crossed the point where another broad architecture rewrite would add less value than implementation. The final bot can now be constructed as a coherent `.per` expert-system implementation using the established contracts, stock-derived service topology, target-build ABI baseline, evidence ladder, and external static/replay tooling.

The one area that must remain behind an explicit adapter boundary is **Construction OS timing**. Static evidence is sufficient to define its state machine and interfaces, but four target-build temporal questions remain runtime-unqualified: placement-token persistence, jump/placement evaluation timing, builder-assignment latency, and placement reinitialization after failure. The final bot must therefore avoid depending on any unqualified timing assumption. Construction can be implemented as a conservative command/observation/recovery service whose timing-sensitive transitions are isolated for later qualification.

This is an implementation-readiness decision, not a claim that every runtime semantic has been experimentally proven.

## What is now closed

### 1. Target build and stock substrate

The target executable/build identity is fixed to AoE2DE `101.103.48987.0`, Steam BuildID `24094652`.

The untouched retail HD AI executable closure is established as:

1. `AI (HD version).per`
2. `Promisory\\defaultConstants.per`
3. `Promisory\\finalingConstants.per`
4. `Promisory\\finaling.per`

The stock corpus has been inventoried at the symbol/state-operation level. The project therefore has a concrete stock substrate rather than a documentation-derived approximation.

### 2. Typed ABI model

The project has established that numeric equality is not semantic identity. Goals, strategic numbers, flags, timers, unit IDs, unit-line IDs, classes, buildings, technologies, search state, and other operands remain separate typed domains.

The implementation rule is frozen:

> A numeric value is implementation-safe only when its type, operation context, ownership, build scope, validator representation, and intended postcondition are known.

### 3. State architecture

The permanent state envelope is:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

Consequential state has an explicit owner/writer contract. Derived state is not allowed to become an accidental authority. Engine-authoritative observations are not silently replaced by cached estimates.

### 4. Temporal/evidence architecture

The bot is designed around two clocks:

- controller clock: rules, goals, strategic numbers, timers, searches;
- world clock: queues, training, construction, research, object creation, movement, combat.

The execution evidence ladder is frozen:

`INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`

No implementation module may silently promote one level to another.

### 5. Economic control plane

Static stock forensics now establishes the civilian/economic chain:

`DEMAND → AUTHORIZATION → ESCROW/RESERVATION → INTEGER WORKER TARGETS → SOURCE/SITE SEARCH → TASKING → WORLD OBSERVATION → VERIFICATION → RECOVERY`

Stock does not provide evidence for one universal civilian scheduler. Priority is distributed through conditional policy, rule ordering, jumps, escrow state, worker eligibility, source serviceability, and specialized retasking. AEGIS therefore implements an explicit arbitration boundary instead of copying the stock rule tree or inventing a universal priority ladder.

### 6. Civilian lifecycle

The distinction between:

- production desire/authorization,
- resource/production feasibility,
- physical production command,
- pending production,
- completion evidence

is now an explicit contract.

`trainvillager` is policy/authorization; `up-can-train escrow-state villager` is feasibility; `up-train escrow-state villager` is physical production service behavior.

### 7. Worker model

The worker model is no longer a four-bucket abstraction. Static evidence requires at least:

- food specialists;
- wood workers;
- gold workers;
- stone workers;
- builders;
- specialized food roles;
- idle/unassigned;
- protected/preemptable/reassigning task states.

Worker allocation and worker tasking remain separate services.

### 8. Resource/serviceability model

Source selection is spatial, stateful, and infrastructure-aware. The bot must preserve candidate identity, source status, dropsite/serviceability, worker eligibility, task load, and observation freshness rather than reducing resource gathering to a scalar shortage controller.

### 9. External tooling map

The supplied external projects have now been assigned explicit roles:

| Asset | Final role |
|---|---|
| `aoe2-ai-parser` | static syntax/command/package preflight and registry differential |
| `aoe2-ai-module` | native fact/action/temporal research reference; not an unqualified DE oracle |
| `aoc-mgz` | replay parser + regression fixture corpus |
| `aoe2rec` | independent replay parser / differential oracle |
| `pyage2` | experiment/orchestration architecture reference only; not DE runtime substrate |
| `openage-engine` | independent engine architecture reference only |
| x96dbg snapshot | targeted native ABI investigation tool; no blind reverse engineering |

The evidence hierarchy is frozen as:

`STOCK → TARGET-BUILD MACHINE EVIDENCE → REPLAY EVIDENCE → PARSER/REGISTRY → EXTERNAL IMPLEMENTATION → INFERENCE`

External documentation never silently upgrades to stock runtime truth.

## Static implementation preflight result

The current `implementation/` tree contains 19 `.per` modules totaling approximately 1,400 source lines.

A fresh local run of the supplied `aoe2-ai-parser` validator found six modules with findings. These are **prototype/preflight defects, not final-bot blockers**, because the files are explicitly `v0` implementation artifacts and are not yet the final package. The findings are nevertheless recorded so they cannot be carried forward accidentally:

- `AEGIS-civilian-lifecycle-reconciler-v0.per`: undocumented `g:-=` math form.
- `AEGIS-source-dropsite-serviceability-v0.per`: `up-get-search-state` called with two arguments at three sites; parser expects one.
- `AEGIS-worker-productivity-observer-v0.per`: `up-get-search-state` called with two arguments.
- `AEGIS-worker-role-vector-v0.per`: five uses of undocumented `g:-=` math form.
- `AEGIS-worker-target-selection-v0.per`: `up-get-search-state` called with two arguments.
- `AEGIS-worker-task-verification-v0.per`: `up-get-search-state` called with two arguments at two sites.

**Rule:** no `v0` implementation file is promoted into the final bot merely because its architecture is correct. Every final module must pass a clean static preflight or carry an explicit, evidence-backed compatibility exception.

## Numeric ABI correction

The older Pass 92 proposal used low numeric storage such as `403–562`. That proposal is **superseded** for final implementation. The stock goal-operation inventory shows no referenced goal channels in `403–562`, but the installed stock corpus also uses those numeric values heavily in other typed domains, and stock documentation contains extended-goal constraints. Therefore the old numbers are not automatically safe simply because the goal-reference inventory does not reference them.

The first Cavalry slice's high-goal candidates `10000–10015` are also **not automatically declared final** merely because the stock referenced-goal inventory does not use them. They remain candidate storage pending the project's final engine-reserved/target-build allocation record.

No implementation constant is cleared by numerical emptiness alone.

## Final implementation architecture

The final bot should be assembled in this order:

```text
FOUNDATION / BUILD PROFILE
        ↓
MACHINE-TRUTH + STATE ENVELOPE
        ↓
WORLD OBSERVATION
        ↓
BELIEF / SITUATION
        ↓
OBJECTIVES
        ↓
CAPABILITY / FORCE DEMAND
        ↓
ECONOMIC DEMAND
        ↓
ARBITRATION / ESCROW
        ↓
PRODUCTION / CONSTRUCTION / WORKER SERVICES
        ↓
EXECUTION AUTHORITY
        ↓
VERIFICATION
        ↓
RECOVERY / REASSESSMENT
```

No module is permitted to jump directly from strategic intent to physical command when an authorization, commitment, or verification boundary is required.

## Final bot vertical-slice strategy

The first production slice remains **Cavalry Threat Containment**, because it exercises the greatest number of cross-system contracts without requiring the entire game to be implemented first:

```text
Enemy cavalry observation
        ↓
Threat assessment
        ↓
Containment objective
        ↓
Camel capability requirement
        ↓
Current-vs-required deficit
        ↓
Producer/candidate selection
        ↓
Economic reservation / arbitration
        ↓
Training authority
        ↓
Queue/pending evidence
        ↓
Creation/availability evidence
        ↓
Deployment/effectiveness verification
        ↓
Objective reassessment
```

This slice should be implemented as a complete vertical system before broad civilization behavior is added. It is the smallest architecture that exercises observation, state, belief, objective, capability, economy, arbitration, execution, verification, and recovery together.

## What remains intentionally outside the final implementation guarantee

### Construction temporal ABI

Still runtime-unqualified:

1. placement-token persistence after failed authorization;
2. jump evaluation boundary relative to construction registration/observation;
3. builder-assignment visibility latency;
4. placement reinitialization semantics after failure.

These questions are now isolated behind Construction OS interfaces. They do **not** justify another architecture rewrite.

### Runtime generation semantics

The representation and lifecycle of generation state must be implemented conservatively. No final design may depend on wraparound, same-pass visibility, or mutation ordering that has not been established.

### Final numeric allocation

The symbolic ABI is ready. Numeric allocation must be generated from the final package's complete typed inventory rather than copied from prototype constants.

### Final package closure

The final `.ai` root and reachable `.per` closure have not yet been emitted. This is a build task, not an unresolved architectural question.

## Final build gate

The final implementation is authorized to begin when the implementation branch obeys these rules:

- no XS;
- no undocumented primitive introduced solely from memory;
- every command/fact has a parser/reference status;
- every persistent field has one owner;
- every consequential field has validity/generation semantics where needed;
- every numeric allocation has a collision record;
- every command has an evidence transition;
- every failure path has a recovery disposition;
- construction timing assumptions remain localized;
- final package closure is mechanically checked;
- final `.ai` entry is intentionally minimal/empty if that is the selected package form;
- the target build profile is recorded in the package manifest.

## Verdict

**The research phase has reached diminishing returns for broad architecture. We are ready to build the final bot.**

The next engineering operation should be **implementation of the final Cavalry Threat Containment vertical slice from the frozen contracts**, not another general-purpose research pass.

The only prohibited claim is that the resulting bot is already runtime-certified. Runtime certification remains a separate future gate, with Construction OS timing as the known unresolved semantic boundary.
