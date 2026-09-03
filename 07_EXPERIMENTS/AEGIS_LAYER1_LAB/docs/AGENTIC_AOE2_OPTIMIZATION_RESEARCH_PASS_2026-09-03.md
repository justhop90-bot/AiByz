# AEGIS Research Pass — Agentic AoE2 AI Optimization

**Date:** 2026-09-03  
**Layer 1:** 89% — unchanged  
**Evidence class:** comparative external engineering evidence; not native-machine proof

## Source synthesis

The supplied Emergent Garden video describes an agentic loop: LLMs generate AoE2 scripts, executable matches provide performance feedback, and later agents refine the scripts. The practical lessons are iterative refinement, tournament/replicate evaluation to reduce stochastic variance, and using smaller/faster battles when the objective is rapid optimization.

Public implementations reviewed:

- `MaxRobinsonTheGreat/AgentsOfEmpires`: AoE2DE screen-driven tournament runner. Its README documents round-robin evaluation, strategy/run archival, machine-readable status/heartbeat state, recordings, and replay parsing. It explicitly says the implementation is screen-capture driven and was assembled for video production rather than as a polished engine integration.
- `mboop127/AlphaScripter`: older genetic AoE scripting system. Its README documents FFA/crossover for early training, score-based and adversarial selection modes, seven mutations of a parent, and persistence of the best script.

## Reusable architecture

```text
candidate → static gate → controlled execution → measurement
         → replicate/tournament evaluation → selection
         → mutation/refinement → archive → next generation
```

This is an optimization architecture, not evidence about the internal AoE2DE AI machine.

## AEGIS decisions

### Adopt

1. **No single-game promotion.** Candidate fitness must be based on controlled replicates/tournaments with build, map/scenario, civs, seeds where controllable, candidate/opponent hashes, result, duration, resignation, age-up, queue/build/research observations, replay hash, parser/evaluator versions, and variance/confidence metadata.
2. **Use staged evaluation.** Exploration uses cheap micro/tactical benchmarks; adversarial evaluation tests against strong incumbents/counters; generalization uses diverse opponents/maps; promoted candidates run a fixed regression suite.
3. **Archive immutable generations.** `parents → mutation rationale → candidate hash → test matrix → raw results → aggregate fitness → promotion decision`.
4. **Treat LLMs as mutation operators, not authorities.** Mutation prompts should include the parent, relevant rule neighborhood, constraints, observed failures, quantitative regressions, known engine semantics, prohibited constructs, target objective, and preservation invariants. The executable evaluator decides whether the mutation worked.
5. **Use multi-objective fitness.** Eventually include economic efficiency, military effectiveness, timing, resource float, production utilization, adaptation, and robustness rather than win rate alone.

### Reject

1. Do not use optimization results to infer native scheduler/fact/UnitAI semantics before Layer 1 causal closure.
2. Do not treat replay-derived commands or inferred winners as live native state. The reviewed AgentsOfEmpires recording reader explicitly labels queue/building commands as attempts and winner inference as non-official.
3. Do not make screen automation the preferred Layer 1 causal instrument. It is a practical evaluation fallback; native causal recovery remains the primary research route.
4. Do not copy external constants such as seven mutations or particular tournament sizes as AEGIS invariants. They are implementation choices, not proven optima.

## Mutation taxonomy for eventual AEGIS optimizer

- parameter/threshold/timing mutation
- existing-rule condition/action mutation
- rule insertion/deletion
- priority mutation (only after scheduler semantics are established)
- economic-policy mutation
- military-policy mutation
- information/scouting mutation
- recovery/failure-handling mutation (only after failure semantics are established)
- structural/refactoring mutation

Each mutation must state its intended causal mechanism and falsification criterion.

## Benchmark hierarchy

**Micro:** one capability, short and low variance.  
**Tactical:** small battles, high iteration rate.  
**Full:** general games for promotion/generalization, not every mutation.

Benchmark transfer must be tested rather than assumed.

## Immediate engineering consequence

Do **not** launch a large evolutionary tournament yet. Build the optimizer contract in parallel with Layer 1:

- candidate manifest and immutable hashing
- benchmark manifest
- tournament matrix
- raw-result schema
- fitness/evaluation schema
- mutation provenance
- promotion/rejection record
- regression-suite manifest

These are static artifacts and can be validated without hundreds of game launches.

## Layer 1 boundary

This pass changes Layer 4 planning only. It does **not** promote any claim about native AoE2DE scheduling, persistent-fact freshness, rule ordering, rule-to-action dispatch, UnitAI execution, or failure/recovery.

**Promotion:** comparative optimization methodology only.  
**Layer 1:** 89%, unchanged.  
**Next Layer 1 pass:** P0-B native scheduler recovery.

## External implementation evidence

The AgentsOfEmpires tournament implementation uses pairwise strategy combinations, configurable rounds, fixed civ settings, per-run archives, and per-game status. Its recording reader derives duration, resignation/age-up timing, queue/build/research/market observations, and cautious winner inference while documenting limitations. AlphaScripter separates FFA exploration from adversarial/score-based selection and retains the best script.
