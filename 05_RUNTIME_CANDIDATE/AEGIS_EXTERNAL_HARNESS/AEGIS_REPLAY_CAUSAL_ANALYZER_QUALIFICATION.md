# AEGIS Replay Causal Analyzer Qualification

Status: **IMPLEMENTED / NOT RUNTIME-QUALIFIED**

The analyzer correlates lifecycle ACTION records with later SYNC payload
identity presence. A matching identity is reported only as corroborating
observation; it is not promoted to creation, availability, or effectiveness.

## Evidence boundary

The analyzer can establish `COMMAND_ISSUED` from replay ACTION records. It
cannot independently establish acceptance, queueing, pending state, world
creation, availability, or combat/economic effectiveness.

This is intentional. The tool must expose missing observability as UNKNOWN
rather than manufacture causal certainty from temporal proximity.

## Next experiment

Run the analyzer against a controlled single-production-action replay and
compare its identity correlations against an independent world-state source.
The experiment should use the exact target build and preserve hashes for every
input artifact.
