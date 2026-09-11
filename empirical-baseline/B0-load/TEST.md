# B0 — Empirical Runtime Load/Execution Probe

## Question
Can the target AoE2DE runtime load and execute a minimal custom `.per` without AEGIS/AegisProm dependencies?

## Files
- `MiniBot.ai` — empty AI entry file.
- `MiniBot.per` — one rule, one strategic-number write, then self-disable.

## Controlled variable
The only behavioral mutation is:

`sn-percent-civilian-explorers = 0`

## Manual procedure
1. Copy `MiniBot.ai` and `MiniBot.per` to the manually selected test AI location.
2. Do not modify the untouched stock `resources\\_common\\ai` baseline.
3. Start one ordinary single-player test match and select `MiniBot` as the AI.
4. Observe whether the AI loads, whether the match remains responsive, and whether the intended behavioral change is visible.
5. Record the exact game build, map/mode, AI slot/difficulty, elapsed game time, and observed result.
6. Do not infer execution from file presence or selection-list presence alone.

## Pass condition
Runtime loads the AI and there is positive runtime evidence that the rule executed.

## Fail condition
Parser/load error, AI does not start, runtime instability attributable to the probe, or no evidence of execution.

## Current status
NOT EXECUTED — requires manual in-game stimulus/observation.
