# Harness

The harness tree is reserved for **qualification**, not current implementation.

## Layout

- `scenarios/` — future controlled scenarios and only scenarios explicitly promoted for qualification.
- `manifests/` — machine/build/input identity records for each qualification run.
- `logs/` — raw runtime/validator output.
- `expected/` — explicit expected observations and verdict criteria.

## Current status

Scenario-loader automation/testing is retired as the primary development route. Existing historical experiments remain preserved under their original locations and authority labels.

This directory does not authorize a new runtime probe. Runtime qualification begins only after the corresponding subsystem has been deconstructed and its ABI/test contract is frozen.

## Required run contract

Every future qualification artifact must record:

`BUILD + INPUT_HASHES + SCRIPT_HASHES + SCENARIO_ID + TEST_PURPOSE + OBSERVED_OUTPUT + EXPECTED_OUTPUT + VERDICT + INTERPRETATION + LIMITATIONS`

Never record only PASS/FAIL. The observation that produced the verdict must remain recoverable.
