# Byzantine Policy Activation Index — 2026-09-08

**Target:** AoE2DE `101.103.48987.0` / BuildID `24094652`
**Source:** restored target-build `AI (HD version).per` on Weebo

This index identifies every non-commented `#load-if* BYZANTINE-CIV` activation directive in the flattened stock AI. It is the starting point for reconstructing Byzantine-specific policy as a graph of activated rules and state effects rather than as a list of civilization bonuses.

## Activation sites

There are **23 non-commented Byzantine activation directives** in the source:

```text
  611   #load-if-not-defined BYZANTINE-CIV
 1271   #load-if-defined BYZANTINE-CIV
 3884   #load-if-defined BYZANTINE-CIV
 9275   #load-if-defined BYZANTINE-CIV
14646   #load-if-not-defined BYZANTINE-CIV
14671   #load-if-not-defined BYZANTINE-CIV
14969   #load-if-defined BYZANTINE-CIV
16232   #load-if-not-defined BYZANTINE-CIV
23100   #load-if-not-defined BYZANTINE-CIV
24663   #load-if-not-defined BYZANTINE-CIV
25109   #load-if-defined BYZANTINE-CIV
25142   #load-if-not-defined BYZANTINE-CIV
25847   #load-if-not-defined BYZANTINE-CIV
26832   #load-if-defined BYZANTINE-CIV
27397   #load-if-defined BYZANTINE-CIV
27709   #load-if-not-defined BYZANTINE-CIV
27910   #load-if-not-defined BYZANTINE-CIV
27979   #load-if-not-defined BYZANTINE-CIV
28784   #load-if-not-defined BYZANTINE-CIV
28885   #load-if-defined BYZANTINE-CIV
31193   #load-if-not-defined BYZANTINE-CIV
31443   #load-if-defined BYZANTINE-CIV
35829   #load-if-not-defined BYZANTINE-CIV
```

## Why this matters

The stock AI does not express civilization policy in one isolated Byzantine module. Byzantine behavior is distributed through multiple physical regions of the flattened program.

The activation index therefore creates the correct extraction target:

```text
BYZANTINE-CIV activation
        ↓
activated rule block
        ↓
conditions / prerequisites
        ↓
read state
        ↓
write state
        ↓
engine side effect
        ↓
downstream subsystem
```

## Preliminary high-value anchors

Static inspection already identifies several important Byzantine-specific anchors:

- **Line 1,271 region:** Byzantine-specific constants for villager/starting-state behavior.
- **Line 3,884 region:** Byzantine-specific Imperial resource/transition constants.
- **Line 9,275 region:** Byzantine strategy rule(s), including unit-goal interaction.
- **Line 14,969 region:** Byzantine-specific policy inside the strategy/civ-policy area.
- **Line 25,109 region:** Byzantine construction/economic policy around town-size/building decisions.
- **Line 26,832 region:** Byzantine unit-production policy.
- **Line 27,397 region:** Byzantine production/composition policy.
- **Line 28,885 region:** Byzantine unit/research policy.
- **Line 31,443 region:** Byzantine military/attack-side policy.

These anchors are deliberately described as extraction targets rather than conclusions about final AEGIS behavior.

## Required next static extraction

For each of the 23 activation sites, extract:

1. matching `#end-if` boundary;
2. nested activation predicates;
3. rule count;
4. goals read/written;
5. strategic numbers read/written;
6. timers touched;
7. facts/object-data queried;
8. production/build/research actions;
9. communication/interaction effects;
10. cross-region state dependencies;
11. historical purpose;
12. AEGIS generalization candidate;
13. evidence strength.

The output should become a **Byzantine policy graph** with explicit source provenance and no implicit promotion into the AEGIS runtime ABI.

## Boundary

This is static deconstruction only. No runtime probe is required or authorized by this index.
