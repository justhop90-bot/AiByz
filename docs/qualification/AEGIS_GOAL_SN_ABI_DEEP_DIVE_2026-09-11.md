# AEGIS Goal / Strategic-Number ABI Deep Dive — 2026-09-11

## Executive result

The full AEGIS source tree does **not** currently have a cleared numeric ABI. The previous high-number allocation scheme was experimental and must not be treated as production-safe.

The immediate runtime error in `AEGIS-worker-target-selection-v0.per` is **not caused by goal 514**. In the installed file, line 61 is:

`(up-get-search-state local-total)`

`local-total` is not defined in the installed module. `up-get-search-state` requires an output goal and writes four consecutive extended goals. The current module therefore has an actual undefined-identifier defect.

The GitHub version additionally contains `aegis-wts-request-id 551`, while the installed copy inspected on 2026-09-11 does not contain that definition. The installed copy is therefore not source-identical to current GitHub.

## Authority cross-reference

1. Exact installed target package and local source files.
2. Current GitHub `main` source.
3. AoE2 AI Scripting Encyclopedia / SN Index.
4. UserPatch patch-history documentation for extended-goal and DUC semantics.
5. Historical HD/Promisory source examples.
6. Project ABI policy and prior qualification documents.

No historical number is promoted merely because it appears unused.

## Goal model

The current Encyclopedia's detailed Goals section defines 512 standard goal storage locations, numbered 1–512. It also distinguishes **extended goals** used by UserPatch/DUC commands. Goals 1–40 are unsuitable for commands that write multiple consecutive goals. Extended-output operations should use a start goal in the documented safe extended range.

The UserPatch records explicitly constrain multi-goal cost operations to extended goals 41–508, and point operations historically use extended goals beginning above 40. `up-get-search-state` writes four consecutive extended goals. Therefore AEGIS should treat:

- **1–40:** scalar-only reserve; do not use for point/cost/search-state outputs.
- **41–508:** primary AEGIS working allocation range for state and extended outputs.
- **509–512:** scalar-only reserve; do not use for four-goal outputs or other operations that consume consecutive goal slots.

The exact target-build runtime still controls final qualification.

## Existing AEGIS allocation problem

The installed AegisProm source contains 152 AEGIS state-like numeric channels in 300–507 and another 164 above 512, excluding timer definitions. The high blocks extend through the 700s. Those values are not valid as a general production GoalId namespace merely because `defconst` accepts the integer.

Two timers are also outside the documented timer range:

- `aegis-dp-timer = 60`
- `aegis-wm-timer = 300`

The timer range is 1–50. These are separate ABI defects.

## Proposed goal reclamation model

A compact reallocation can fit the currently counted AEGIS state channels inside the valid working range instead of inventing a larger numeric namespace.

Recommended first-pass reservation:

- **116–431:** 316 AEGIS scalar/state channels, after typed review of every channel.
- **432–508:** reserved headroom for future AEGIS state, point pairs, search-state blocks, cost data, and other multi-goal operations.
- **41–97:** untouched safety reserve unless a specific extended operation requires it.
- **98–115:** preserve the stock/finaling working definitions currently present in the AEGIS stock substrate.
- **1–40 and 509–512:** preserve as scalar-only engine space; do not allocate multi-goal outputs there.

This is a **candidate allocation**, not a cleared production allocation. Every channel must still be typed and checked against all writers/readers before promotion.

## Why 116–431

The installed stock finaling constants occupy goal-like working identifiers 98–115 (`gl-population-cap`, `temp-goal`, `found-gaia`, point/search state variables, etc.). The AEGIS state channels currently begin at 300 and therefore collide conceptually with the need for a bounded namespace but not with those stock values directly.

Repacking the AEGIS state channels into 116–431 gives 316 consecutive slots and leaves 432–508 as a substantial contiguous extended-goal reserve. This is preferable to continuing the 510+ experimental pattern.

The allocation must be generated from a machine-readable manifest rather than hand-edited independently in 49 files.

## Strategic-number model

Strategic numbers are a separate ABI namespace: **0–511**. They must not be confused with goals.

The current Encyclopedia SN index identifies roughly 300 active/listed SNs and says the unlisted high range can be used as extra goal-like storage, while specifically recommending **SN 510 downward** and warning that **SN 511 has DE bugs**. The index also notes that DE can add SNs, so high-number custom SNs require target-build qualification.

For AEGIS:

- **SN 511:** do not use.
- **SN 510:** first candidate custom SN.
- **SN 509 downward:** candidate custom SN pool only after checking the current target-build SN index and source usage.
- Known active/listed SN IDs such as 313, 314, 316, 318 and the documented 0–312 range must not be treated as free merely because AEGIS does not define them.
- Named engine SNs such as `sn-focus-player-number`, `sn-target-point-adjustment`, `sn-maximum-gold-drop-distance`, etc. remain engine behavior controls, not AEGIS scratch storage.

AEGIS currently does not define its own numeric `sn-*` scratch block; most `sn-*` names in AegisProm are engine-defined strategic numbers. This is good and should remain the default architecture.

## Recommended custom-SN policy

If AEGIS truly needs scratch SN state, use a descending block beginning at 510, excluding 511, and record each ID in the ABI manifest. Do not allocate a large block until the exact target build's SN index has been reconciled.

Prefer goals for AEGIS internal state. Use SNs only where the state must pass through a command whose operand is explicitly an SN or where a proven engine behavior is intentionally being controlled.

## Worker-target-selection correction

Installed file line 61:

`(up-get-search-state local-total)`

is invalid because `local-total` is not defined in that module.

The established stock/Promisory pattern defines four consecutive output goals, for example `gl-local-total`, `gl-local-last`, `gl-remote-total`, and `gl-remote-last`, and passes the first of those to `up-get-search-state`.

The AEGIS module should instead use a dedicated four-goal block, e.g. a future ABI-assigned quartet, rather than inventing `local-total` locally.

This is a **symbol-definition defect**, not evidence that goal 514 itself caused the error.

## Source discrepancy: installed vs GitHub

Current GitHub `AegisProm/AEGIS-worker-target-selection-v0.per` contains an additional:

`(defconst aegis-wts-request-id 551)`

The installed copy inspected on Weebo does not contain that definition and instead reaches `up-get-search-state local-total` at line 61.

Therefore runtime qualification must always record a source hash/manifest and must not assume that the machine-local tree is the current GitHub tree.

## Non-negotiable rules going forward

1. No numeric channel is cleared from vacancy alone.
2. Every numeric symbol gets a type: Goal, extended Goal, SN, Timer, Flag, or non-storage constant.
3. Every multi-goal operation reserves its full consecutive span, not merely the first ID.
4. No goal allocation above the proven target-engine GoalId range.
5. No timer allocation outside 1–50.
6. SN 511 is excluded; high custom SN candidates begin at 510 and descend only after target-build reconciliation.
7. Engine SNs are not scratch variables merely because their current behavior is undesirable or undocumented.
8. Installed runtime files and GitHub source must be hash-manifested separately.
9. Static validation must reject undefined output identifiers such as `local-total`.
10. Runtime testing resumes only after the ABI manifest is internally consistent.

## Qualification disposition

This deep dive **does not clear any production allocation yet**. It establishes the corrected engineering model and a candidate reclamation plan.

The next required artifact is a generated typed ABI manifest mapping every AEGIS numeric channel to: symbol, numeric ID, type, module, writer, readers, multi-goal span, stock collision status, target-build evidence, and qualification state.
