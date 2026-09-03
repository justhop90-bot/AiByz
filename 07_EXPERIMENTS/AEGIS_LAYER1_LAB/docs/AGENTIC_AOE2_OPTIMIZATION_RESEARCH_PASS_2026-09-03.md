# AEGIS Research Pass — Agentic AoE2 AI Optimization

**Date:** 2026-09-03  
**Layer 1 status:** 89% — unchanged  
**Scope:** external video + public implementation evidence; architecture implications only  
**Evidence class:** comparative / external engineering evidence, not native-machine proof

## 1. Source

Primary source supplied for review:

- Emergent Garden, *AI agents play Age of Empires II* (2026-08-15), video ID `ZBdAe3ZwKds`.

The supplied source summary describes an agentic loop in which LLMs generate AoE2 AI scripts, scripts are run against executable game matches, results are measured, and subsequent agents refine the scripts. It emphasizes repeated feedback, tournament variance control, small/faster battle scenarios, and LLM-directed mutations rather than purely random genetic mutations.

Public implementation evidence reviewed alongside the video:

- `MaxRobinsonTheGreat/AgentsOfEmpires` — an automated AoE2DE runner used for the video. Its README documents round-robin tournaments, strategy archival, machine-readable status/heartbeat state, minimized/background-compatible operation of the tournament/smoke runner, and recording parsing. It explicitly states that the project is screen-capture driven and was uploaded as an improvised video-production tool, not as a polished engine integration.
- `mboop127/AlphaScripter` — an older AoE2 genetic-script system. Its README describes FFA selection/crossover for early training, adversarial winner selection for later training, score-based selection, seven mutations of a parent, and persistence of the best script.

## 2. Confirmed external engineering pattern

The strongest reusable pattern is:

`candidate generation → controlled execution → objective measurement → variance-aware evaluation → selection → mutation/refinement → archival → repeat`

This is an optimization architecture, not a reconstruction of the AoE2 AI machine.

The video and public implementations independently support the value of closing the loop between executable performance and code revision. They do **not** establish how the native AoE2DE scheduler, persistent facts, rule dispatcher, UnitAI, or failure/recovery machinery works internally.

## 3. What AEGIS should adopt

### 3.1 Tournament-as-evaluation, not single-game fitness

A candidate must not be promoted from one stochastic game. Evaluation should be a tournament or replicate set with fixed experimental controls. Record:

- build fingerprint
- scenario/map identity
- civs
- starting conditions
- opponent set
- random seeds where controllable
- candidate hash
- opponent hash
- game count
- win/loss/result
- duration
- resignation time
- age-up timing
- queue/build/research command counts
- replay artifact hash
- parser version
- evaluator version
- confidence/variance statistics

A single-game win is an observation. A promotion requires statistical evidence against the incumbent and relevant opponents.

### 3.2 Separate early, middle, and late optimization regimes

The external evidence suggests different selection pressures are useful at different maturity levels:

- **Exploration:** many cheap, small, controlled battles; maximize information per unit time.
- **Adversarial improvement:** candidate versus strong incumbent or targeted counter-strategy.
- **Generalization:** candidate versus a diverse opponent suite and multiple maps/scenarios.
- **Regression:** every promoted candidate reruns a fixed benchmark suite.

AEGIS should not copy the exact FFA/7-mutation numbers as constants. They are implementation choices from external projects, not universal optima.

### 3.3 Archive every generation

Each optimization generation should be immutable and reproducible:

`generation → parent(s) → mutation rationale → candidate hash → test matrix → raw results → aggregate fitness → promotion decision`

The existing Layer 1 epistemic standard already requires provenance and explicit promotion/rejection decisions. The optimizer should inherit the same discipline.

### 3.4 Use LLMs as structured mutation operators

An LLM should not receive only “make it better.” A mutation request should contain:

- parent script
- relevant source/rule neighborhood
- current architecture constraints
- observed failure signatures
- quantitative regression data
- known engine semantics
- prohibited constructs
- target objective
- required preservation invariants

The output should be a candidate patch plus machine-readable rationale. The evaluator remains authoritative: the LLM proposes; the executable environment decides fitness.

## 4. What AEGIS should explicitly reject

### 4.1 Optimizing before Layer 1 causal closure

External projects demonstrate that useful scripts can be evolved without a complete model of the engine. That is valuable engineering evidence, but it is not our epistemic standard.

AEGIS will continue to reconstruct the native machine first. Optimization can exploit the machine after its relevant causal contracts are known; it must not be used to silently convert correlations into engine semantics.

### 4.2 Treating replay-derived metrics as native state

Recording parsers are excellent evaluators. They are not authoritative access to the live AI state. Queue/build/research commands, resignation events, and inferred winners must remain labeled as observations/derived metrics unless independently validated.

The AgentsOfEmpires recording reader explicitly warns that queue/building commands are attempts rather than confirmed completed/surviving objects and that an inferred winner is not an official result field. This distinction matches AEGIS's existing replay epistemology.

### 4.3 Screen automation as the long-term Layer 1 mechanism

The external runner proves that screen-driven automation can close a practical optimization loop. Its own README states that it depends on screen capture and the real cursor. AEGIS should treat this as a fallback evaluation adapter, not as the preferred native causal instrument.

Our current fail-closed runtime adapter remains preferable for infrastructure control, while Scenario Editor automation remains shelved unless separately reopened.

## 5. New AEGIS optimizer architecture

Proposed eventual Layer 4 system:

```text
                 ┌─────────────────────┐
                 │ Strategy Genome     │
                 │ (.per + metadata)   │
                 └──────────┬──────────┘
                            │
                     mutation proposal
                            │
                 ┌──────────▼──────────┐
                 │ LLM / deterministic │
                 │ mutation operators  │
                 └──────────┬──────────┘
                            │
                      candidate gate
                            │
                 ┌──────────▼──────────┐
                 │ Static validator    │
                 │ + semantic checks   │
                 └──────────┬──────────┘
                            │
                   controlled execution
                            │
                 ┌──────────▼──────────┐
                 │ Tournament runner   │
                 │ / benchmark matrix  │
                 └──────────┬──────────┘
                            │
                     replay + telemetry
                            │
                 ┌──────────▼──────────┐
                 │ Evaluator           │
                 │ fitness + variance  │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │ Promotion gate      │
                 │ regressions + CI    │
                 └──────────┬──────────┘
                            │
                    archive / next gen
                            └───────────────►
```

The evaluator must support multi-objective fitness. Win rate alone is insufficient for a professional bot project. Candidate metrics should eventually include economic efficiency, military effectiveness, timing, resource float, idle production, strategic adaptation, and robustness, with scenario-specific weighting.

## 6. Mutation taxonomy

The optimizer should classify mutations instead of treating all LLM edits equally:

1. **Parameter mutation** — thresholds, target counts, timing constants.
2. **Rule mutation** — condition/action changes within an existing rule.
3. **Rule insertion/deletion** — add or remove behavior.
4. **Priority mutation** — alter competing rule interactions after scheduler semantics are established.
5. **Economic-policy mutation** — gather/production allocation.
6. **Military-policy mutation** — composition, attack, defense, reinforcement.
7. **Information-policy mutation** — scouting/intelligence rules.
8. **Recovery mutation** — explicit handling of failed or stale states once failure semantics are known.
9. **Structural mutation** — refactor duplicated logic without intended behavioral change.

Every mutation records its intended causal mechanism and the observations that would falsify it.

## 7. Benchmark design

Three benchmark classes should eventually exist:

### A. Micro-benchmarks

Short, low-variance scenarios targeting one capability. Examples: production timing, resource transition, military response, rule conflict, or a single known failure mode.

### B. Tactical battles

Small scenarios designed to expose decision quality while permitting many replicates per hour.

### C. Full games

Arabia/random-map or equivalent general-purpose benchmarks. Expensive and high variance; use for promotion/generalization, not for every mutation.

This is compatible with the video's observation that small/faster battles can accelerate optimization, but AEGIS should validate benchmark transfer rather than assuming it.

## 8. Connection to current Layer 1 work

This research changes **Layer 4 planning**, not Layer 1 confidence.

The highest-value Layer 1 work remains native causal recovery:

1. P0-B scheduler recovery
2. P0-A persistent-fact lifecycle
3. P0-C rule-to-action dispatch
4. P0-D UnitAI mutation/execution
5. P0-E failure/recovery
6. identity lifecycle
7. temporal/determinism model

The optimizer should be built against explicit interfaces for these contracts rather than embedding guesses about them.

## 9. Immediate engineering consequence

Do **not** begin a large-scale evolutionary tournament yet.

Instead, prepare the optimizer contract in parallel with Layer 1 recovery:

- candidate manifest schema
- immutable candidate hashing
- benchmark manifest schema
- tournament matrix schema
- raw result schema
- fitness/evaluation schema
- promotion/rejection record
- mutation provenance schema
- regression-suite manifest

These are static engineering artifacts and can be validated without launching hundreds of games.

Once P0 causal contracts are sufficiently closed, the same harness can be connected to native evaluation with substantially less redesign.

## 10. External source notes

`AgentsOfEmpires` README: practical DE tournament runner, strategy archival, machine-readable heartbeat/status, replay recording and parsing, and screen-capture constraints.

`AgentsOfEmpires/tournament.py`: pairwise combinations, configurable rounds, fixed civ, run archival, strategy copying, and per-game status recording.

`AgentsOfEmpires/tools/recording-tools/read-recording.mjs`: derives duration, resignations, age-up times, queue/build/research commands, market activity, and cautious winner inference from parsed recordings; explicitly records limitations.

`AlphaScripter/README.md`: FFA early training, score-based selection, adversarial selection, seven parent mutations, and best-script persistence.

## 11. Epistemic decision

**Promotion:** comparative optimization methodology only.

**Not promoted:** any claim about native AoE2DE scheduler semantics, fact freshness, rule ordering, rule-to-action dispatch, or UnitAI execution.

**Layer 1:** remains **89%**.

**Next Layer 1 pass:** P0-B native scheduler recovery.
