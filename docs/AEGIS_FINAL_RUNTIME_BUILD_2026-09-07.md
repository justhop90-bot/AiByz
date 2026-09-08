# AEGIS-BYZ Final Runtime Build

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.

## Decision

The project now has a single final integrated runtime entry point on the machine:
`resources/_common/ai/AEGIS-BYZ.per`.

This build intentionally does not use the word candidate in its root identity. It is the bot intended to be loaded for real-game testing and improvement.

## Runtime graph

The final root loads the established AEGIS cognitive stack plus the civilian control stack:

World Model → Civilization State → Worker Role Census → Worker Role Vector → Civilian/Economic Demand → Arbitration → Worker Selection → Source/Dropsite Serviceability → Worker Task Command → Task Verification → Productivity Observation → Recovery → Villager Production → Civilian Lifecycle Reconciliation.

The existing AEGIS economy, military, verification, recovery, and operations services remain in the graph.

Dynamic probe/qualification instruments are deliberately excluded from the production graph.

## Finalization changes

1. Installed the previously archived villager-production and civilian-lifecycle modules onto the machine.
2. Converted economic arbitration to a complete final module and restored its wood/gold/stone/terminal-selection rules.
3. Added the missing explicit high-priority arbitration constant.
4. Gave the worker-role vector concrete initial civilian targets: food 7, wood 4, gold 3, stone 0, builder 1. These are starting behavior targets, not claimed optimums.
5. Integrated the civilian stack directly into the production root.

## Static machine verification

Production root load targets: 29.
Missing load targets: 0.
Parenthesis delta across loaded graph: 0.
Undefined AEGIS symbols across loaded graph: 0.
Numeric AEGIS goal definitions at 300+: 252.

Final root SHA-256:
8184E9504F4D1B163EB3840DEF6890B3D8B08FFD6646651E4119237DCF9638B5

## Qualification status

This is the final bot build for live testing. It is NOT being represented as proven-successful runtime behavior yet. The next evidence comes from running this exact build in AoE2DE and observing what happens.

If the bot behaves incorrectly, the next work is repair of the actual failure observed in-game—not creation of another parallel integration candidate.