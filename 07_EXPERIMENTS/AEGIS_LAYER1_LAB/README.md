# AEGIS Layer 1 Experimental Laboratory

Bootstrap implementation of an automated causal-experiment harness for Layer 1.

The harness is designed to remove manual AoE2DE operation from routine experimentation. It generates machine-readable experiments, records controlled variables and timing, launches an explicitly configured runtime command when execution is enabled, captures observations, and writes append-only JSONL evidence.

## Current status

- Version: 0.1.0-bootstrap
- Default mode: dry-run
- Runtime adapter: present, but no AoE2DE launch contract is assumed yet
- First campaign: P0-A persistent-fact freshness
- Current campaign capacity: 1,152 generated cases before any adaptive pruning

## Pipeline

`question -> hypotheses -> generator -> setup -> runtime -> observation -> adjudication -> evidence ledger`

Execution success is not causal proof. Promotion remains governed by the Layer 1 evidence ladder and requires discrimination between competing machine models.
