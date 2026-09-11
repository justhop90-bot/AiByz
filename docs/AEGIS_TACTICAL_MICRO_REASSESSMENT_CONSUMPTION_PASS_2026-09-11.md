# AEGIS Tactical Micro REASSESSMENT Consumption Pass — 2026-09-11

## Decision

Tactical Micro REASSESS consumption is implemented at the source-contract level.

The correct downstream consumer is **Micro Control (MC)**. Micro Verification (MV) owns the terminal tactical lifecycle and publishes the REASSESS event; Micro Control owns the stable tactical request identity and is therefore the correct owner to acknowledge that terminal lifecycle before a newer World Model frame can create another tactical request.

## Evidence direction

The accepted lifecycle is:

```text
World Model generation N
    -> Micro Control lifecycle/request N
    -> tactical execution/verification
    -> Micro Verification terminal outcome N
    -> MV REASSESS N
    -> MC acknowledges exact N once
    -> MV publication token consumed
    -> newer World Model generation N+1
    -> MC generation N+1
    -> new tactical lifecycle
```

The forbidden lifecycle is:

```text
MV REASSESS N
    -> MC generation N+1
    -> duplicate tactical request without a new world observation
```

The implementation does not provide that shortcut.

## Consumer implementation

`AegisProm/AEGIS-micro-control-v0.per` now owns:

- `aegis-mc-reassess-generation = 784`
- `aegis-mc-reassess-valid = 785`

The acknowledgement requires:

1. `aegis-mv-reassess-valid == 1`;
2. the published REASSESS generation equals `aegis-mv-generation`;
3. the MC acknowledgement generation differs from the published generation.

The consumer then:

1. records the exact MV lifecycle generation;
2. sets the local MC acknowledgement bit;
3. consumes the MV publisher token by clearing `aegis-mv-reassess-valid`.

No MC lifecycle generation is modified by the acknowledgement.

## New-generation ownership

Micro Control can create a new lifecycle only from a valid World Model frame:

```text
World Model valid
AND
MC generation != World Model generation
AND
MC valid == 0
```

The new MC generation is copied from `aegis-wm-generation`.

Therefore REASSESS is not a generation source. A new tactical lifecycle requires a new upstream world observation.

## Idempotency

The consumer is generation-keyed. Once generation N has been acknowledged, the condition:

```text
MC reassess generation != MV reassess generation
```

is false for that same event. Clearing the MV publication token also prevents repeated consumption of the same publication event.

A later World Model generation resets MC's local acknowledgement-valid state as part of opening the next lifecycle.

## Strategy boundary

The REASSESS acknowledgement contains no strategy selection. It does not set:

- engage;
- retreat;
- regroup;
- tactical stage;
- physical command;
- authorization.

Those remain separate decision/execution responsibilities. This prevents REASSESS from becoming a hidden central tactical controller.

## Evidence preservation

The existing MV verification boundary remains intact. MV can observe an applied/partial/failed/unknown tactical outcome, but REASSESS itself does not upgrade that evidence into strategic success or causal success.

In particular, the existing tactical verification source requires world evidence and explicit causal evidence for stronger outcome claims. Unknown/partial/failed states remain distinguishable.

The implementation therefore preserves the distinction between:

```text
command issued
    !=
world effect observed
    !=
causal attribution proven
    !=
strategic success
```

## Important existing Tactical Micro limitations

This pass does not promote Tactical Micro to full qualification.

Known independent gates remain:

1. physical command-to-world-effect qualification is incomplete;
2. causal evidence is not established by REASSESS;
3. the execution bridge references broader strategic authority fields that require continued cross-file integration audit;
4. pursuit remains a governor-level intent without a separately qualified physical pursuit adapter;
5. target-build runtime qualification has not been executed here.

These are intentionally left visible rather than being hidden by the reassessment implementation.

## Namespace

The new acknowledgement fields are allocated as:

```text
784  aegis-mc-reassess-generation
785  aegis-mc-reassess-valid
```

They are registered in `docs/AEGIS_GOAL_NAMESPACE_MAP_2026-09-11.md`.

## Validation

Added:

`tests/vertical_slices/test_tactical_micro_reassessment_consumption.py`

The static contract suite checks:

- MV publisher identity;
- MC consumer ownership;
- exact generation matching;
- one-shot publisher-token consumption;
- upstream-only MC generation advancement;
- active-request protection;
- absence of strategy selection at the REASSESS boundary;
- preservation of tactical evidence uncertainty;
- absence of a central reassessment controller.

These are source-contract tests. They do **not** constitute AoE2DE target-build runtime qualification.

## Promotion decision

**Tactical Micro REASSESS consumption: IMPLEMENTED — source-contract level.**

**Stale-generation shortcut: BLOCKED.**

**Duplicate acknowledgement: BLOCKED.**

**REASSESS → new generation shortcut: BLOCKED.**

**Central reassessment controller: NONE.**

**Tactical Micro vertical: NOT FULLY QUALIFIED.** Existing tactical execution/world-effect and causal-verification gates remain independent.
