# Layer 1 Automated Experiment Harness — Bootstrap

**Date:** 2026-09-03
**Status:** BOOTSTRAP VALIDATED / RUNTIME ADAPTER INCOMPLETE

## Question
How can AEGIS scale Layer 1 causal investigation without requiring the operator to manually launch, watch, and record hundreds of AoE2DE runs?

## Decision
Build an automated laboratory. An experiment is a machine-readable controlled case, not a manually observed game.

## Current implementation
- machine-readable experiment generation;
- explicit competing hypotheses;
- controlled-variable and timing dimensions;
- per-experiment run directories;
- append-only JSONL observation ledger;
- dry-run default;
- opt-in runtime process adapter;
- executable build identity recorded in the lab manifest.

## Local validation
The supplied AoE2DE executable was located at the expected Steam installation path and its SHA-256 matched the controlled identity already recorded for build `101.103.48987.0`.

The P0-A generator has a Cartesian capacity of 1,152 cases before adaptive pruning. A local harness smoke run generated and recorded 1,000 cases in approximately 2.71 seconds in dry-run mode. This validates orchestration throughput only; it is **not** 1,000 AoE2DE causal experiments.

## Epistemic boundary
The runtime adapter can execute an explicitly supplied command, but the AoE2DE scenario/control/observation contract is not yet assumed. No runtime causal result is promoted by this bootstrap.

## Next engineering gate
Implement the AoE2DE-specific setup and observation adapter, then run a tiny calibration campaign before enabling large automated runtime batches. The first target remains P0-A persistent-fact freshness.

## Governing standard
`question -> prior evidence -> competing hypotheses -> discriminating test -> exact setup/build -> raw observation -> interpretation -> confidence -> promotion/rejection -> repository artifact -> next test`
