# P0 Dynamic Worker Loop Probe — Implementation Pass

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Probe implemented and archived; runtime execution evidence NOT YET CAPTURED; production root untouched.

## Objective

Provide an isolated instrument for measuring whether a goal mutation becomes visible to a later rule evaluation. This is the first ABI qualification instrument for the worker-loop architecture.

## Probe design

A timer establishes a repeatable observation boundary. One rule writes a trigger goal and stage marker. A later rule, on a subsequent timer evaluation, tests those markers and records an observed marker. No economy command, worker task, source selection, or production-root load is involved.

The instrument therefore tests one narrow proposition: whether goal state written by one evaluation is observable by a later evaluation. It does not prove same-pass visibility, command side-effect visibility, search mutation visibility, or rule re-entry behavior.

## Evidence status

OBSERVED: target build and stock engine diagnostics are available; stock source uses persistent goal state extensively.
CORRELATED: persistent goal publication is the appropriate substrate for generation-fenced AEGIS state.
IMPLEMENTED: isolated goal-visibility probe.
STATIC-QUALIFIED: candidate has isolated IDs 560–563 and is not loaded by AEGIS-BYZ.per.
RUNTIME-QUALIFIED: NO — the probe has not yet been executed through the target-build AI interpreter with captured debugger/log evidence.

## Important limitation

The probe deliberately uses a timer boundary. A successful result establishes pass-to-pass visibility only. It cannot be used to infer that a goal written earlier in the same rule pass is immediately visible to another rule, nor that engine commands have immediate observable side effects.

## Required runtime experiment

Execute the probe on the exact target build with AI script debugging/logging enabled. Record:

1. target executable/build identity;
2. candidate script hash;
3. probe activation time;
4. trigger/stage writes;
5. observation marker;
6. rule/script position evidence;
7. whether the observation occurs on the expected subsequent timer boundary;
8. any interpreter warnings/errors.

Repeat enough times to detect nondeterministic behavior. Archive the raw observation before promoting any ABI claim.

## Gate decision

No production integration follows from this probe alone. The next qualification sequence should add isolated probes for strategic-number mutation, search-state mutation, and command side-effect visibility, using the same evidence discipline.