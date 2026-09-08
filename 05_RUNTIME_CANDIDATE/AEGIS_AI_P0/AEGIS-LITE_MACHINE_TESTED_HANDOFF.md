# AEGIS-Lite Machine-Tested Handoff

Status date: 2026-09-06
Target: AoE2DE 101.103.48987.0 / Steam BuildID 24094652
Branch: `aegis/external-harness-v1-2026-09-05`

## Purpose

This artifact records the AEGIS-Lite modules that were developed and individually runtime-tested on the target machine before being published to GitHub. They were intentionally held back from GitHub while iterative testing was underway. They are now published so the repository contains the tested architectural continuation rather than only the earlier research checkpoint.

## Published tested chain

```text
WORLD MODEL
    ↓
BELIEF MODEL
    ↓
SITUATION ANALYSIS
    ↓
OBJECTIVES
    ↓
PLANNING
    ↓
DECISION
    ↓
COMMITMENT
```

Published paths:

- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AEGIS-BYZ.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/Aegis-belief.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/Aegis-situation.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/Aegis-objectives.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/Aegis-planning.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/Aegis-decision.per`
- `05_RUNTIME_CANDIDATE/AEGIS_AI_P0/AegisProm/Aegis-commitment.per`

## Runtime-test record

The user tested the modular layers sequentially against the target installation. Reported results were:

- Architect / World Model: started successfully.
- Carpenter modular load: started successfully.
- Belief Model: worked after correcting native `up-modify-goal` copy syntax.
- Situation Analysis: worked after correcting an invalid C-style comment block to AoE2 `.per` comments.
- Objectives: worked without a problem.
- Planning: worked after correcting an undefined urgency identifier to the Situation-layer urgency constants.
- Decision: worked.
- Commitment: worked.

These are runtime startup/execution observations from the development/test sequence. They do **not** constitute full semantic qualification of every sensor, goal channel, command surface, or engine outcome.

## Critical evidence distinction

Do not upgrade these modules from `machine-tested candidate` to `PROVEN engine semantics` merely because they load or execute.

In particular:

- `aegis-knight = 38` currently represents a concrete Knight unit ID, not a qualified `knight-line` sensor.
- `up-get-fact` / `up-get-fact-max` return values still require semantic calibration.
- `aegis-wm-valid = 1` is an architectural state transition, not independent proof that every observation has been semantically corroborated.
- Commitment is authorization/intent, not proof of execution.
- Execution, Verification, and Recovery are not yet part of the tested AEGIS-Lite chain.

## Source-of-truth rule

The live machine and GitHub had diverged because the modules were being tested directly on the machine. That was intentional during development, but it must not continue indefinitely.

From this point forward:

1. Preserve the machine-tested artifacts.
2. Treat GitHub as the canonical project memory.
3. Do not silently overwrite the machine package with a different repository version.
4. When machine code differs from GitHub, perform an explicit reconciliation diff.
5. Record build, source path, evidence class, and test result for meaningful changes.

## Do not do this next

Do **not** immediately replace the tested chain with a newly generated Execution module simply because Commitment is the current architectural endpoint.

First verify the published tree against the live machine and ensure the entrypoint/load graph is the exact intended modular package.

Then continue with Execution as a semantic skeleton, keeping:

```text
AUTHORIZED != ISSUED != ACCEPTED != PENDING != CREATED != EFFECTIVE
```

and defer concrete command adapters until their native surfaces are separately qualified.

## Highest-value next experiment

The most valuable empirical experiment is one complete, tightly bound state transition:

```text
exact .per source
    ↓
exact package
    ↓
package hash
    ↓
exact AoE2 executable/build
    ↓
engine execution
    ↓
one controlled AEGIS state transition
    ↓
external observation (CA:DE or equivalent)
    ↓
independent corroboration where available
    ↓
verdict
```

The goal is not to prove the whole bot. The goal is to prove one source-to-engine-to-observation transition with immutable provenance.

## Known qualification priorities

1. Reconcile GitHub and live machine closures.
2. Verify the eight-file load graph exactly.
3. Qualify concrete Knight ID `38` versus `knight-line`.
4. Separate observation execution from semantic evidence validity.
5. Repair/normalize the external-harness manifest dialect mismatch.
6. Bind experiment results to executable/package/source hashes.
7. Only then expand into native execution adapters.

## Engineering instruction to the next project lead

You are inheriting an active engineering program, not starting a green-field bot.

Preserve the tested artifacts. Challenge assumptions with experiments. Do not treat validators as the engine. Do not treat a parser success as semantic proof. Do not treat replay representation as direct engine state. Do not turn an external observer into an architectural dependency merely because it is useful.

The architecture is intentionally being built from meaning toward execution:

```text
WORLD MODEL → BELIEF → SITUATION → OBJECTIVES → PLANNING → DECISION → COMMITMENT → EXECUTION → VERIFICATION → RECOVERY
```

The first seven layers are now represented in the repository as the machine-tested AEGIS-Lite continuation. The next lead should reconcile, qualify, and then advance the system—not discard the work and restart from theory.
