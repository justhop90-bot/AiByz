# AEGIS — Typed Fact Static Evidence

**Date:** 2026-09-05  
**Status:** STATIC EVIDENCE — RUNTIME SIGNATURE TEST STILL OPEN  
**Target:** AoE2DE `101.103.48987.0`

## 1. Direct stock evidence

The exact normal HD stock AI contains the following executable rule pattern in `AI (HD version).per` around lines 6465–6474:

`(up-get-focus-fact unit-type-count galley-line math-goal)`

followed by analogous calls for:

- `fire-ship-line`
- `longboat-line`
- `turtle-ship-line`
- `cannon-galleon-line`

The result is then stored/manipulated through `math-goal` and `enemy-focus-navy`.

This is direct evidence that the stock HD closure uses:

`up-get-focus-fact + unit-type-count + unit-line identifier + goal output`

as a real engine-facing pattern.

## 2. Why this matters to the historical knight-line question

The historical AEGIS experiment used:

`up-get-focus-fact + unit-type-count + knight-line + temporary-goal`

The exact stock closure does not establish that exact `knight-line` compound, but it does establish the broader typed signature with unit-line identifiers as the subject and a goal as output.

The stock closure additionally shows that `knight-line` is a conditionally defined symbolic alias rather than one universal numeric identity. Examples include:

- `knight-line → steppe-lancer-line` under `JURCHENS-CIV`;
- `knight-line → hei-guang-cavalry-line` under multiple later civilization blocks.

Therefore replacing `knight-line` with concrete `knight 38` merely to satisfy a historical validator failure would be semantically unjustified.

## 3. `temporary-goal` evidence

The stock closure contains a comment near line 35211 stating that two scratch goals are used without being defconst-defined and then uses literal goals `60` and `61` for related temporary data.

This proves that “not locally defconsted” and “engine-invalid” are not equivalent propositions.

It does **not** prove that an arbitrary symbolic `temporary-goal` is legal. The exact target validator/engine behavior remains an empirical gate.

## 4. Specialist reference alignment

The AoE2 AI Scripting Encyclopedia explicitly distinguishes parameter types and explains that commands interpret identifiers according to the parameter type expected at that position. citeturn3search5turn3search6

Its command index identifies `up-get-focus-fact` as a High-cost Fact/Action and `up-get-object-data` as Very High cost, reinforcing that signature correctness and runtime-cost qualification are separate concerns. citeturn2search1

## 5. Disposition

**Static typed-signature evidence:** strengthened.  
**Historical `knight-line` replacement with `knight 38`:** rejected as an unjustified semantic change.  
**Exact `knight-line` compound runtime legality:** OPEN P1.  
**Temporary scratch-goal semantics:** OPEN P1.  
**No production implementation promoted.**
