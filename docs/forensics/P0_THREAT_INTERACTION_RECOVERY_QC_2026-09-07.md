# P0 Threat Interaction / Recovery QC — 2026-09-07

**Project:** AEGIS-BYZ
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Authoritative corpus:** untouched stock `resources\\_common\\ai\\Promisory` on Weebo
**Status:** forensic evidence; no AEGIS runtime changes.

## Executive result

Reinspection of `interaction.per` confirms that stock threat handling is a distributed, policy-specific control system. Threat state can trigger unit-control reset, retreat state, defense-unit gathering, altered economy/building policy, and communication. It does **not** establish a universal civilian evacuation transaction.

The most important correction is that `underattack` is a broad policy predicate, while `gl-threat-time/player/source/target` are explicit threat-data outputs refreshed by `init.per`. These should not be collapsed into one AEGIS boolean.

## 1. Threat data is explicitly refreshed

`init.per:691-704` contains a recurrent initialization/state-acquisition rule that executes:

```per
(up-get-threat-data gl-threat-time gl-threat-player gl-threat-source gl-threat-target)
(up-find-player enemy find-attacker attacking-enemy)
(up-get-fact population 0 my-pop)
(up-get-fact civilian-population 0 my-cpop)
(up-get-fact military-population 0 my-mpop)
(up-get-fact unit-type-count villager villagercount)
(up-get-fact unit-type-count-total villager villagercounttotal)
```

This establishes an explicit threat snapshot alongside population accounting.

## 2. Threat response is operation-specific

`gatherers.per` uses `underattack`, `goal defend`, `gl-threat-player`, and `gl-threat-time` to alter economic policy. Examples include changing gatherer percentages and changing acceptable hunt/drop distances.

A particularly important path requires `gl-threat-player >= 1` and `gl-threat-time < 16000` before jumping to a different economic branch. Another path reduces maximum hunt drop distance when defense/underattack conditions are active.

This demonstrates that threat modifies **economic serviceability policy**, not merely military state.

## 3. Threat can terminate/suppress specific civilian operations

`gatherers.per` contains rules using `underattack` and `up-enemy-units-in-town` in livestock/food-management control. These conditions alter or suppress specific food-management branches.

`buildings.per` similarly uses threat-related predicates to alter construction decisions.

Therefore the correct abstraction is:

```text
THREAT OBSERVATION
      ↓
AFFECTED SUBSYSTEM
      ↓
LOCAL POLICY RESPONSE
```

not:

```text
THREAT = TRUE → STOP ALL CIVILIANS
```

## 4. Interaction controller has explicit threat-triggered control reset

`interaction.per:1065-1074` contains a rule requiring `underattack` plus an active unit-control timer and restrictive defense/gathering strategic numbers. Its actions include:

```per
(disable-timer unit-control-flare-timer2)
(up-reset-unit c: -1)
(set-strategic-number sn-disable-defend-groups 0)
(set-strategic-number sn-gather-defense-units 1)
(enable-timer spread 180)
(set-goal retreat yes)
```

This is a genuine threat-driven control reset, but its target is the unit-control/defense subsystem. It is not proof of worker evacuation.

## 5. Interaction controller uses enemy-in-town as a distinct trigger

`interaction.per:2351-2390` uses an OR condition containing:

- military inferiority,
- `up-enemy-units-in-town`,
- `underattack`,
- a defense-chat goal.

It then searches for nearby enemy/all-unit objects and sends defensive communication/position information.

This proves `up-enemy-units-in-town` is a meaningful spatial threat trigger independent of the generic `underattack` predicate.

## 6. Threat has temporal memory

Stock stores `gl-threat-time` and compares it against explicit windows such as `< 16000` and `>= 60000`. This means threat response is not necessarily a zero-duration instantaneous Boolean event; the AI consumes a remembered threat timestamp.

Exact units/semantics of the stored time value should remain documented as engine-native time data until independently characterized.

## 7. Important distinction: `underattack` vs threat snapshot

Evidence supports at least three threat concepts:

```text
UNDERATTACK
  broad policy predicate

THREAT SNAPSHOT
  gl-threat-time
  gl-threat-player
  gl-threat-source
  gl-threat-target

ENEMY-IN-TOWN
  spatial enemy-presence predicate
```

These have overlapping but non-identical uses. AEGIS should preserve them separately.

## 8. Threat does not prove global worker evacuation

The inspected interaction and gatherer paths do not establish a universal sequence:

```text
threat detected
→ enumerate all villagers
→ stop/evacuate villagers
→ mark assignments invalid
→ reassign after safety clears
```

Some civilian operations are suppressed or redirected, while other threat logic controls military/interaction behavior.

Therefore a centralized AEGIS safety service would be an architectural enhancement, not a direct transcription of stock behavior.

## 9. Timing result

The corpus proves that threat state can be stored and later consumed by rules. It does **not** provide enough evidence to calculate exact detection-to-retask latency. The `.per` language/rule scheduling model and engine-side threat update cadence still require runtime instrumentation or additional ABI evidence.

Do not assign a fixed number of rule cycles or milliseconds to threat recovery yet.

## 10. Revised AEGIS threat contract

AEGIS should expose threat state approximately as:

```text
threat-generation
observed-at
underattack
threat-player
threat-source
threat-target
threat-age
enemy-in-town
local-threat-severity
```

Subsystem requests should then classify themselves:

```text
REQUEST EXISTS
REQUEST EXECUTABLE
REQUEST THREAT-BLOCKED
REQUEST INVALIDATED
```

A blocked request should remain distinguishable from a failed request.

## 11. New failure distinction

This pass establishes a critical distinction:

```text
TASK FAILURE
    command/task became invalid

THREAT BLOCK
    task may remain semantically desirable but is temporarily unsafe

SOURCE FAILURE
    economic target cannot service the task
```

These should not converge prematurely into one `TASK_INVALID` code.

## 12. Confirmed

- `up-get-threat-data` populates four threat state values.
- Threat data is acquired alongside population/civilian/military census data.
- `underattack` gates economic and civilian-policy rules.
- `up-enemy-units-in-town` is independently used as a threat trigger.
- Interaction has explicit threat-triggered unit-control reset logic.
- Threat state has temporal memory through `gl-threat-time`.
- Threat can modify economic serviceability parameters.
- Threat response is distributed and subsystem-specific.

## 13. Not proven

- Universal civilian evacuation.
- Exact threat detection cadence.
- Exact threat-to-retask latency.
- Universal worker reassignment after threat clears.
- One centralized stock threat manager.
- Exact numeric semantics/units of `gl-threat-time` beyond its use in comparisons.

## Architectural verdict

The civilian substrate should not wait for a hypothetical universal evacuation primitive. AEGIS should instead implement a typed **Threat/Safety Service** that publishes threat facts and lets Economy, Construction, Worker Assignment, Scouting, and Military services independently decide whether a request is executable, blocked, or invalidated.

The next forensic target is now **source-status enum semantics and cross-resource failure convergence**. That is the final major evidence gate before drafting the Civilization Substrate ABI specification.