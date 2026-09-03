# AEGIS External Project Qualification & Reuse Plan

**Date:** 2026-09-03  
**Project:** AEGIS / AiByz  
**Layer:** Layer 1 — Machine Understanding  
**Status:** Research integration plan; no external project is canonical runtime authority  
**Layer 1 position:** **89%**

---

## 1. Purpose

This document records the external open-source projects that materially improve the AEGIS investigation and defines exactly how they will be used, adapted, or deliberately kept outside the runtime architecture.

The central rule is:

> **Borrow capability, evidence, parsers, test ideas, and abstractions where useful; do not inherit undocumented runtime assumptions.**

AEGIS is a **pure `.per` AoE2DE AI**. External native-extension projects, DLL injection, detours, memory hooks, executable patching, or XS are not part of the AEGIS runtime architecture. They may still be valuable as archaeological evidence or offline research tooling.

External projects therefore have one of four dispositions:

1. **Tool dependency** — used offline to generate/inspect artifacts.
2. **Research specimen** — read for architecture, terminology, historical behavior, or implementation clues.
3. **Adapter candidate** — selected ideas may be reimplemented locally behind a controlled AEGIS interface.
4. **Do not import** — useful project, but its implementation model conflicts with AEGIS constraints.

---

## 2. External project registry

| Project | Role in AEGIS | Disposition |
|---|---|---|
| [AoE2 AI Module](https://github.com/FLWL/aoe2-ai-module) | Native AIExpert/run-list/fact/action archaeology | **Research specimen + source of discriminating hypotheses** |
| [AoE2ScenarioParser](https://github.com/KSneijders/AoE2ScenarioParser) | Deterministic scenario construction/inspection | **Offline test-fixture tool** |
| [mgz-fast](https://github.com/AoEInsights/mgz-fast) | Replay header/body extraction | **Offline observation tool** |
| [genieutils-py](https://github.com/SiegeEngineers/genieutils-py) | DAT parsing/data-model inspection | **Offline data tool** |
| [genieutils](https://github.com/sandsmark/genieutils) | Comparative Genie-format/data archaeology | **Research specimen** |
| [freeaoe](https://github.com/sandsmark/freeaoe) | Independent engine implementation comparison | **Comparative research specimen only** |
| [aoe2ai](https://github.com/lewisc64/aoe2ai) | High-level AI authoring/translation examples | **Historical/design specimen** |
| [aoe2-ai-fmt](https://github.com/ks07/aoe2-ai-fmt) | `.per` formatting/syntax tooling | **Tooling reference; not authoritative DE validator** |
| [aoe2-aiscript](https://github.com/Jvinniec/aoe2-aiscript) | Editor grammar/resource/signature knowledge | **Reference/tooling specimen; validator quarantined** |
| [SiegeEngineers/aoc-dev-resources](https://github.com/SiegeEngineers/aoc-dev-resources) | Discovery index for AoE development resources | **Research index** |

The registry is intentionally broader than the runtime dependency set. A research project can benefit from a tool without shipping that tool.

---

## 3. Priority project: FLWL/aoe2-ai-module

### 3.1 Why this project matters

The AoE2 AI Module is the most immediately valuable external source discovered in this pass because it exposes an implementation-facing model around the native `AIExpert` system rather than only `.per` vocabulary.

Its public source contains a DE-specific `SIG_FUNC_RUN_LIST` pattern and an `Expert::DetouredRunList` interface. The DE signature is defined as a function taking an `AIExpert*`, `listId`, and statistics output; the implementation then calls the resolved native `FuncRunList(aiExpert, listId, statsOutput)`. This is strong comparative evidence that a native run-list boundary exists in at least the historical DE build targeted by that project. It is **not** proof that the current AEGIS controlled build uses the same address, signature, ABI details, or implementation. See the project's `Configuration.h` and `Expert.cpp`.

The project also contains an explicit fact-loader model. Its `AIFact` structure includes `type`, `touched`, `lastResult`, argument metadata, and a native fact-function pointer. Its DE loader iterates `aiExpert->numFacts`, reads `aiExpert->fact[factId]`, and associates fact names with fact functions. This is particularly valuable for the AEGIS P0-A persistent-fact investigation because it gives us concrete competing hypotheses for what fact state may look like internally. It remains historical/source-derived evidence, not current-build truth.

### 3.2 What AEGIS will use

**Use directly as evidence:**

- the concept of a native run-list entry point;
- `AIExpert*` + `listId` as a candidate scheduling boundary;
- the distinction between fact metadata, fact function, `touched`, and `lastResult`;
- the existence of a fact-function registry keyed by native fact metadata;
- the possibility that facts have explicit mutable evaluation state;
- the project’s command/fact/action taxonomy as a hypothesis generator.

**Use as a hypothesis generator for P0-B:**

`run-list boundary → list selection → rule evaluation → command processing`

The project’s `DetouredRunList` is especially useful because it gives us a discriminating target: if current-build native recovery finds a run-list function with matching calling behavior, we gain a much stronger causal bridge than a string search alone.

**Use as a hypothesis generator for P0-A:**

`fact descriptor → touched/state → fact evaluation → lastResult → consumer`

We should explicitly test whether current DE behavior supports anything analogous to:

`unevaluated → evaluate → result → touched/dirty → consume → refresh`

rather than assuming the external structure is correct.

### 3.3 What AEGIS will NOT use

The project uses native detouring/memory integration. AEGIS will **not** import that runtime architecture.

Specifically, AEGIS will not:

- inject its DLL into AoE2DE;
- detour the current executable;
- patch the executable to expose AI internals;
- use the external project's hard-coded historical addresses as current-build addresses;
- treat its 2021 source as shipped source for the current 2026 build;
- use the project as a runtime dependency for the pure `.per` ByzBot.

The value is archaeological: it tells us **where to look and what competing implementation hypotheses to test**.

### 3.4 AEGIS adaptation plan

We will create local, offline-only equivalents of useful concepts where they improve research organization:

```text
External native concept
        ↓
AEGIS hypothesis / observation schema
        ↓
controlled executable evidence
        ↓
current-build causal proposition
        ↓
knowledge record
        ↓
.per architecture requirement
```

We will not copy native structures into production code merely because they are convenient.

### 3.5 Current evidence level

**Classification: high-value comparative evidence, not canonical runtime evidence.**

The repository is public and its current metadata identifies it as an LGPL-2.1 project. Its source is old relative to the controlled 2026 executable, so version drift is a first-class confounder.

---

## 4. AoE2ScenarioParser

Repository: https://github.com/KSneijders/AoE2ScenarioParser

### Use

This is our preferred **offline scenario-fixture generator and parser**. It can programmatically construct player state, units, triggers, map configuration, resources, and other scenario fields. Its current documentation states support through scenario version 1.58 (June 2026).

### AEGIS plan

Use it to create deterministic fixtures such as:

- one known unit vs. two known units;
- controlled unit creation/removal;
- resource changes;
- timing-triggered state transitions;
- embedded `.per` probes;
- identity/lifecycle fixtures;
- matched control/mutation scenarios.

The parser itself never becomes the authority for whether the game executed the scenario. The game remains the execution authority.

### Current qualification

AEGIS has already qualified the supplied parser source tree and a Python 3.13 environment, including bundled tests, DE 1.58 round-trip behavior, and a deterministic P0-A fixture. The parser boundary rejects XS for AEGIS fixtures.

### Modification plan

Do **not** fork the parser initially. Wrap it with an AEGIS provider that:

1. verifies the expected source digest;
2. pins the supported scenario version;
3. rejects XS execution paths;
4. emits fixture provenance and hashes;
5. writes only into the isolated laboratory area;
6. never claims runtime success from parser success.

If the upstream parser changes materially, requalify rather than silently upgrading.

---

## 5. mgz-fast

Repository: https://github.com/AoEInsights/mgz-fast

### Use

`mgz-fast` is the replay-observation pipeline. Its README identifies support for DE `.aoe2record` files and provides header/body parsing tools.

### AEGIS plan

Use it for:

- replay metadata extraction;
- player/civ/map/version identification;
- body-event extraction;
- candidate timeline construction;
- post-game behavioral measurement;
- replay-vs-native correlation.

### Hard boundary

A replay is an observation stream, not a direct dump of native AI state. AEGIS will never treat a parsed replay field as proof of an internal native variable without an explicit causal bridge.

### Modification plan

Keep upstream tooling external. Build an AEGIS normalization layer around its output rather than forking parser internals. Every replay-derived observation should carry replay file hash, parser version/source identity, and timestamp/tick provenance.

---

## 6. genieutils-py

Repository: https://github.com/SiegeEngineers/genieutils-py

### Use

Use it as an offline data extraction layer for DE DAT structures. Its public documentation states that it reads/writes recent AoE2DE DAT versions and provides JSON conversion tooling.

### AEGIS plan

Use it to validate and enrich:

- unit IDs;
- unit-line IDs;
- tech IDs;
- civilization data;
- task/action data;
- costs and prerequisites;
- data-version differences.

This directly supports the namespace discipline already established for concrete unit IDs, line IDs, class IDs, goal IDs, strategic numbers, and facts.

### Modification plan

Do not modify upstream initially. Produce immutable AEGIS data snapshots from a known DAT build and record their hashes. The AEGIS code should consume a normalized generated data layer rather than depending on mutable upstream internals.

---

## 7. genieutils

Repository: https://github.com/sandsmark/genieutils

### Use

Comparative format/data archaeology. It is useful for understanding the broader Genie file ecosystem and for cross-checking how community tooling models data structures.

### AEGIS plan

Use selectively when a DAT/scenario/replay question is ambiguous in one implementation. Never allow a generic Genie abstraction to override DE-specific evidence.

### Modification plan

No fork. If an AEGIS parser requires a missing DE field, implement a narrow adapter or normalization step and preserve the upstream project as the reference specimen.

---

## 8. freeaoe

Repository: https://github.com/sandsmark/freeaoe

### Use

FreeAoE is valuable because it is an independent engine implementation. It provides comparative implementations for scenario loading, units, actions, tasking, and partial AI scripting.

### What it can tell us

It can help distinguish:

- concepts that are natural consequences of the Genie/AoE2 domain;
- concepts that are implementation choices of one engine;
- places where our interpretation of vocabulary is too strong.

Its AI rule implementation shows a simple condition-satisfaction then action-execution architecture in `AiRule.cpp`, while its `AiScript::update` contains an explicit TODO around looping through rules. That is useful comparative evidence precisely because it is **not** the AoE2DE implementation.

### AEGIS plan

Use it to generate competing hypotheses and negative controls. Never copy its scheduler into AEGIS.

---

## 9. aoe2ai

Repository: https://github.com/lewisc64/aoe2ai

### Use

This project is useful for high-level AI authoring patterns and translation from a compact authoring language into `.per` rules.

### AEGIS plan

Study its abstraction choices for:

- repeated behavior;
- build/train macro abstractions;
- scouting and attack grouping;
- readable strategy expression.

Potentially borrow **authoring ergonomics** later, but not runtime semantics.

### Modification plan

If AEGIS eventually wants a higher-level authoring layer, it should compile to our own verified `.per` patterns and retain generated-source provenance. The production artifact remains `.per`.

---

## 10. aoe2-ai-fmt

Repository: https://github.com/ks07/aoe2-ai-fmt

### Use

Useful for formatting and basic syntax tooling around `.per` files.

### Critical limitation

Its public README explicitly warns that it is a work in progress and does not have full compatibility with DE/User Patch `.per` files.

Therefore it is **not** an authority for AEGIS syntax validity.

### AEGIS plan

Use only for developer ergonomics or comparative grammar ideas. AEGIS validation must be based on the actual controlled game's parser behavior plus our own static checks.

---

## 11. aoe2-aiscript

Repository: https://github.com/Jvinniec/aoe2-aiscript

### Use

This VS Code extension contains useful command signatures, parameter descriptions, snippets, resource files, and experimental error detection.

### Critical limitation

Its own documentation identifies limitations including missing rule-length/rule-closure checks and false positives around numeric IDs and identifier classes. Therefore its diagnostics cannot become our runtime truth.

### AEGIS plan

Use its resource/signature information as a secondary vocabulary cross-check and potentially mine useful human-facing descriptions. Do not install its validator into the causal promotion path.

A future AEGIS editor may reuse the *idea* of contextual signatures and namespace-aware completion, but should use the AEGIS qualified command/data registry.

---

## 12. SiegeEngineers/aoc-dev-resources

Repository: https://github.com/SiegeEngineers/aoc-dev-resources

### Use

This is a discovery/index source for AoE development resources. It helps find additional parsers, reimplementations, replay tools, and modding resources.

### AEGIS plan

Treat it as a **research index**, not an evidence source by itself. Every discovered project must be individually qualified before influencing architecture.

---

## 13. Planned AEGIS local adaptations

The goal is not to accumulate forks. The goal is to build a small set of stable local interfaces around proven external capabilities.

### Adapter A — Scenario provider

```text
AoE2ScenarioParser
        ↓
AEGIS scenario_provider
        ↓
qualified .aoe2scenario fixture
        ↓
native execution
```

### Adapter B — Replay provider

```text
mgz-fast
        ↓
AEGIS replay normalizer
        ↓
timestamped observation records
        ↓
causal/replay correlation layer
```

### Adapter C — Data provider

```text
DAT / genieutils-py
        ↓
AEGIS immutable data snapshot
        ↓
namespace registry
        ↓
static analysis + strategy layer
```

### Adapter D — Native archaeology ledger

```text
FLWL/aoe2-ai-module
FreeAoE
other public implementations
        ↓
competing implementation hypotheses
        ↓
controlled current-build test
        ↓
promotion / rejection
```

No external native-extension code enters the production ByzBot.

---

## 14. Proposed AEGIS toolchain

### Layer 1 research toolchain

1. **Controlled AoE2DE executable** — execution authority.
2. **Native PE/`.pdata` archaeology** — implementation geometry.
3. **ScenarioParser adapter** — deterministic fixture construction.
4. **mgz-fast adapter** — replay observation.
5. **genieutils-py data adapter** — authoritative-to-AEGIS data snapshot path.
6. **Static `.per` analyzer/validator** — AEGIS-owned, DE-scoped.
7. **Knowledge/evidence registry** — causal claims and provenance.
8. **Automated experiment harness** — orchestration only; no causal inference from launch success.

### Layer 4 production toolchain

The production bot should be much smaller:

```text
AEGIS doctrine/optimizer
        ↓
verified .per generation
        ↓
AoE2DE native AI parser
        ↓
AoE2DE AIExpert / scheduler / UnitAI
        ↓
gameplay
```

External tools remain outside this chain except for offline generation/validation of artifacts.

---

## 15. What I want to build from these projects

The eventual AEGIS stack should not be a Frankenstein of existing projects. It should be a **verified composition of narrow capabilities**:

### We borrow

- parser techniques;
- file-format knowledge;
- replay extraction;
- DAT modeling;
- scenario construction;
- historical native interface clues;
- human-friendly `.per` authoring concepts.

### We reimplement locally

- evidence normalization;
- build/version qualification;
- namespace registry;
- DE-specific static validator;
- experiment schema and promotion logic;
- replay/native correlation;
- causal knowledge graph;
- strategy-to-`.per` compiler/generator later in Layer 4.

### We explicitly reject

- DLL injection;
- detours/hooks as a runtime dependency;
- executable patching;
- memory modification;
- XS as a required production substrate;
- historical hard-coded addresses as current truth;
- third-party validators as final authority;
- third-party AI schedulers as models of the DE scheduler.

---

## 16. Immediate next engineering passes

### P0-B — Native scheduler recovery

Use the FLWL run-list model as a hypothesis source, then recover the current-build path independently:

`AIExpert creation → loadRules → rule/list representation → run-list entry → eligibility → ordering → selected rule → interval transition`

The first success criterion is an actual current-build executable edge, not another string cluster.

### P0-A — Persistent fact mutation

Use the external `AIFact` model to define competing hypotheses, then recover current-build evidence for:

`fact descriptor → evaluation → result storage → touched/dirty state → consumer → refresh/invalidation`

### P0-C — Rule to action

Track:

`selected rule → action representation → native action handler → accepted order/request`

### P0-D — UnitAI mutation

Close:

`accepted order → CurrentOrder → CurrentAction → execution/transition`

### P0-E — Failure/recovery

Close:

`failure/invalidation → notification → recovery/search → replacement order`

Only after these are sufficiently closed do external authoring projects become strategically important for production architecture.

---

## 17. Promotion rules for external evidence

An external project's implementation can generate a hypothesis, but it cannot by itself promote a current-build proposition.

Promotion requires:

1. exact source/version provenance;
2. explicit proposition;
3. competing hypotheses;
4. current-build evidence where the claim is about current AoE2DE;
5. controlled setup;
6. raw observation;
7. reproducibility;
8. conflict check against existing AEGIS evidence;
9. dated repository record;
10. explicit promotion/rejection decision.

If external evidence conflicts with current native evidence, the conflict becomes a research question. It is not silently reconciled.

---

## 18. Bottom line

The most important external project from this pass is **FLWL/aoe2-ai-module**, not because we should use its injection architecture, but because it gives AEGIS unusually concrete hypotheses around `AIExpert`, `RunList`, and fact state. Its DE run-list signature and `AIFact` representation are exactly the sort of evidence that can help us choose better native recovery targets.

The second pillar is **AoE2ScenarioParser**, which should remain an offline fixture-generation capability rather than a runtime dependency.

`mgz-fast` remains the replay observation layer; `genieutils-py` the data extraction layer; FreeAoE and the other AI projects remain comparative/historical specimens; and AEGIS itself becomes the integration, provenance, validation, and causal-knowledge layer.

The intended architecture is therefore:

> **External projects provide instruments and hypotheses. AEGIS provides qualification. AoE2DE provides runtime truth. The final bot remains pure `.per`.**

No Layer 1 percentage change is justified by this pass. **Layer 1 remains 89%.**
