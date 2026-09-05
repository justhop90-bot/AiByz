# AEGIS Research Pass — Agentic AoE2 AI Optimization

**Date:** 2026-09-03
**Evidence class:** comparative external engineering evidence; not native-machine proof
**Promotion status:** retained research; not runtime authority

## Source synthesis

The reviewed external work describes an iterative loop in which agents generate AoE2 scripts, executable matches provide performance feedback, and later agents refine candidates. Reusable lessons are iterative refinement, replicate/tournament evaluation to reduce stochastic variance, and cheap benchmarks for rapid optimization.

Public implementations reviewed included screen-driven tournament evaluation and genetic AoE scripting. Their methods are useful comparative evidence but are not AoE2DE native-machine proof.

## Reusable architecture

```text
candidate → static gate → controlled execution → measurement
         → replicate/tournament evaluation → selection
         → mutation/refinement → archive → next generation
```

## AEGIS decisions

1. Do not promote a candidate from one game. Use controlled replicates/tournaments with build, map/scenario, civs, candidate/opponent hashes, result, duration, replay/evaluator provenance, and variance metadata.
2. Use staged evaluation: micro/tactical exploration, adversarial evaluation, generalization, then a fixed regression suite for promotion.
3. Archive immutable generations: parent → mutation rationale → candidate hash → test matrix → raw results → aggregate fitness → promotion decision.
4. Treat LLMs as mutation operators, not authorities. The executable evaluator determines whether a mutation worked.
5. Prefer multi-objective evaluation eventually: economic efficiency, military effectiveness, timing, resource float, production utilization, adaptation, and robustness rather than win rate alone.

## Explicit rejections

- Optimization results must not be used to infer native scheduler/fact/UnitAI semantics before Layer-1 causal closure.
- Replay-derived commands must not be treated as completed native state without evidence.
- Screen automation is an evaluation fallback, not the preferred Layer-1 causal instrument.
- External mutation counts, tournament sizes, or other implementation constants are not AEGIS invariants.

## Eventual optimizer contract

Before large evolutionary runs, define:

- candidate manifest and immutable hashing;
- benchmark manifest;
- tournament matrix;
- raw-result schema;
- fitness/evaluation schema;
- mutation provenance;
- promotion/rejection record;
- regression-suite manifest.

## Boundary

This research does not change the current Layer-1 89% position, does not establish native scheduler semantics, and does not clear Layer-4 implementation. It is retained because it informs the eventual optimization/evaluation subsystem.
