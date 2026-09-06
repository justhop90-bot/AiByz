# AEGIS Complete Architecture Build — 2026-09-06

## Build identity

Target: AoE2DE `101.103.48987.0` / Steam BuildID `24094652`.

This package is the complete AEGIS authority-pipeline skeleton for the first Cavalry Threat Containment vertical slice.

## Loaded architecture

```text
WORLD MODEL
  -> BELIEF
  -> SITUATION
  -> OBJECTIVES
  -> PLANNING
  -> DECISION
  -> COMMITMENT
  -> EXECUTION
  -> VERIFICATION
  -> RECOVERY
```

The entrypoint `AEGIS-BYZ.per` loads all ten AEGIS subordinate layers/adapters in producer-to-consumer order. No stock AI module is loaded.

## Production modules

1. `AEGIS-BYZ.per` — World Model / Architect coordinator
2. `AegisProm/AEGIS-BYZ-Engine-Carpenter-P2.per` — native sensor adapter
3. `AegisProm/Aegis-belief.per` — bounded belief transformation
4. `AegisProm/Aegis-situation.per` — situation classification
5. `AegisProm/Aegis-objectives.per` — objective authority
6. `AegisProm/Aegis-planning.per` — abstract means
7. `AegisProm/Aegis-decision.per` — bounded choice
8. `AegisProm/Aegis-commitment.per` — authorization boundary
9. `AegisProm/Aegis-execution.per` — execution boundary
10. `AegisProm/Aegis-verification.per` — outcome-evidence boundary
11. `AegisProm/Aegis-recovery.per` — bounded recovery boundary

The count is eleven physical `.per` files because the World Model entrypoint and the ten subordinate layers/adapters are distinct artifacts.

## Runtime ordering correction

The previous integrated ordering placed the Architect publication coordinator after all downstream modules. That created a one-generation lag: downstream layers consumed generation N while the coordinator then published N+1.

The entrypoint now loads Carpenter first, then runs the Architect bootstrap/publication/qualification rules, then loads Belief through Recovery. This makes the current published generation available to the downstream state machine in the same rule-evaluation pass.

The downstream observation marker contract is explicit:

```text
1 = native acquisition complete; not yet published
2 = current World Model generation published/qualified
```

Belief, Situation, Objectives, and Planning consume marker `2` only.

## Semantic QC corrections

A second source-level audit found an important goal-operand class of errors. In AoE2 AI scripting, `g:` operands refer to goal values, while `c:` operands refer to constants/literals. Therefore constructs such as `g:= 1` or `g:+ 1` do not mean literal one.

Decision and Commitment now use `set-goal` for literal stage/validity values. Situation, Objectives, and Planning now use `c:+ 1` for literal cycle increments. Goal-to-goal transfers continue to use `g:= <goal>`.

A reusable static semantic lint now exists at `tools/aegis_goal_operand_audit.py` to prevent regression of this class of error. It is a semantic lint, not a substitute for the target engine.

## Execution safety state

Production Execution remains inert at the native-command edge. It reaches `OPERATIONALIZED` but does not cross into `ISSUED`.

The reserved lifecycle is:

```text
AUTHORIZED
  -> OPERATIONALIZED
  -> ISSUED
  -> ACCEPTED/QUEUED
  -> PENDING
  -> CREATED
  -> AVAILABLE
  -> DEPLOYED
  -> EFFECTIVE
```

This is intentional. The completed architecture must not fabricate command issuance or world outcomes.

## First actuator candidate

A disposable qualification pair has now been added but is **not loaded by production**:

- `AegisProm/Aegis-actuator-train-candidate.per`
- `AegisProm/Aegis-verification-train-candidate.per`
- `AEGIS-BYZ-ACTUATOR-QUALIFICATION.per`

The candidate tests one native command contract: `train spearman-line`, with `can-train` and a pre-action `unit-type-count-total` baseline. The first verification boundary is a post-action count increase, explicitly classified as queue/count evidence rather than battlefield creation.

See `AEGIS_FIRST_ACTUATOR_QUALIFICATION_2026-09-06.md` for the promotion gate.

## Evidence status

The architecture is **CODE-COMPLETE AS A SKELETON** and **NOT RUNTIME-QUALIFIED AS A COMPLETE AUTONOMOUS BOT**.

Known evidence boundary:

- individual modules have machine-tested startup/load evidence;
- the reconciled eight-layer package has static structural evidence;
- publication ordering is now structurally corrected but still requires target-build runtime proof;
- generation propagation and stale-state rejection remain unqualified;
- sensor semantics remain partially unqualified;
- the first native actuator candidate exists but is not target-build qualified;
- no claim of autonomous-match semantic success is made.

## Promotion rule

Do not add an arbitrary native command merely to make the bot appear complete. The first Execution actuator must be one explicitly qualified command contract with:

- exact target build binding;
- immutable source/package hash;
- minimal controlled scenario;
- raw diagnostic evidence;
- observed command boundary;
- independent world-state corroboration where available;
- explicit UNKNOWN handling for unobservable lifecycle states.

Until that qualification exists, the production skeleton's inert Execution edge is the correct production behavior.
