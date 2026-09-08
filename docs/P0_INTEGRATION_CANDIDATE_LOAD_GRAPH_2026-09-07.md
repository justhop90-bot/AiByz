# P0 Full Civilian Integration Candidate Load Graph

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Candidate only; NOT production-qualified; NOT loaded by production root.

## Purpose

This load graph puts the current AEGIS cognition, civilization-state, worker observation, economic demand, worker selection, source qualification, command, verification, recovery, and qualification instrumentation into one explicit candidate file on the machine.

## Safety boundary

The candidate is deliberately separate from `AEGIS-BYZ.per`. No production-root modification is made by this pass. The graph must not be treated as runtime-qualified merely because the files parse or load as text.

## Graph

Foundation → cognition stack → operations → civilian census → civilization state → worker-role census → worker-role vector → civilian demand → economic demand → arbitration → worker selection → source/dropsite serviceability → task command → task verification → productivity observation → recovery → dynamic qualification probes.

## Important unresolved dependency

The current worker-role vector uses zero-valued test targets in the archived candidate. That is intentional: it prevents an invented economic policy from silently becoming the bot's strategy. The final Byzantine role allocator must replace these with runtime-qualified demand policy derived from Byzantine state, resource needs, production commitments, infrastructure, map information, and opponent context.

## Qualification state

OBSERVED: stock civilization subsystems and engine-observable worker/resource mechanisms.
IMPLEMENTED: isolated AEGIS modules and explicit candidate load graph.
STATIC-QUALIFIED: files are separated from production root and intended dependency order is explicit.
UNQUALIFIED: complete candidate runtime load, target-build parser acceptance, pass ordering, mutation visibility, worker productivity, and long-horizon behavior.

## Gate decision

The candidate is ready to be used as an isolated qualification target, not as the production bot. Production integration waits for dynamic evidence.