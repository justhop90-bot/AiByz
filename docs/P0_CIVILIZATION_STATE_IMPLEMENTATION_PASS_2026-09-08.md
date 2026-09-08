# AEGIS-BYZ — P0 CIVILIZATION STATE IMPLEMENTATION PASS

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Status:** STATIC-QUALIFIED CANDIDATE / NOT RUNTIME-QUALIFIED
**Implementation:** `implementation/AEGIS-civilization-state-v0.per`

## Implementation decision

The first production substrate candidate is a Civilization State reconciliation layer. It does not acquire native facts itself. It consumes the Architect-owned, published World Model and converts that publication into a separate state snapshot.

This deliberately avoids the duplicate-consumer race identified in the historical AEGIS-Lite P2 package, where both Foundation publication and a downstream module could consume the Carpenter completion marker.

## State fields

The candidate allocates goals 403-420 for generation, validity, stage, observation marker, cycle, time, population, population-cap, age, food, wood, gold, spear count, camel count, skirmisher count, enemy cavalry count, enemy archer count, and focus player.

Stage values are INIT=0, OBSERVE=1, QUALIFIED=2.

## Reconciliation contract

The sole state transition is fenced by:

```text
World Model valid == 1
AND
Civilization State generation != World Model generation
```

The rule copies the complete published snapshot, sets its own generation equal to the World Model generation, and marks the state qualified.

No raw Carpenter marker is consumed.
No native command is issued.
No same-pass propagation is required by the state module.

## Static qualification

Direct target-machine audit of the candidate and its Foundation/Carpenter dependencies produced:

- 56 lines in the candidate;
- balanced parentheses: delta 0;
- 21 candidate `defconst` declarations;
- all referenced external AEGIS symbols defined by Foundation/Carpenter;
- new goal IDs 403-420;
- no collision with existing numeric AEGIS IDs 300-402.

The candidate is therefore **STATIC-QUALIFIED** under the current static gate.

## Important limitation

The candidate has not been inserted into the live root or called runtime-qualified. Target-build same-pass visibility, publication timing, and long-horizon reconciliation remain unqualified.

The module is intentionally designed so that if downstream visibility is delayed by one or more interpreter boundaries, correctness does not depend on immediate propagation.

## Next implementation dependency

The next code pass must add the minimum civilization-state facts required by the first vertical slice that are not currently present in the World Model:

1. discrete villager census;
2. housing/building census;
3. pending production state;
4. worker-role census;
5. idle/interrupted worker state;
6. source/dropsite serviceability state.

Those facts must be added at the Carpenter/State boundary without collapsing native acquisition and semantic ownership.

## Three-personality verdict

**Archaeologist:** approved static structure; runtime timing remains a qualification question.

**Byzantine Architect:** approved as the common substrate boundary; Byzantine demand can consume this state without owning engine acquisition.

**AI(HD)+Promisory:** approved provided worker continuity, pending state, source/dropsite qualification, and recovery are added rather than replaced by scalar resource counts.

## Promotion rule

Do not load this module into the production root until a disposable target-build runtime package demonstrates that the current Foundation -> Carpenter -> Civilization State closure parses, starts, publishes and reconciles without ownership collisions.
