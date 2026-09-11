# AEGIS Anti-Cavalry REASSESSMENT Consumption Pass — 2026-09-11

## Finding

Anti-Cavalry already publishes a terminal lifecycle generation through `aegis-cr-reassess-generation = 768` and `aegis-cr-reassess-valid = 769`. The correct downstream consumer is the **Scouting/Threat** owner because it owns the upstream threat-observation generation consumed by Anti-Cavalry.

The consumer therefore follows:

```text
Anti-Cavalry terminal generation N
    -> CR REASSESS publication N
    -> Scouting/Threat acknowledges N once
    -> CR publication token consumed
    -> wait for newer World Model generation
    -> Scouting/Threat generation N+1
    -> new threat classification
    -> possible new Anti-Cavalry lifecycle
```

REASSESS does not create or increment the next threat generation.

## Consumer implementation

`AegisProm/AEGIS-scouting-threat-v0.per` now owns:

- `aegis-st-reassess-generation = 782`
- `aegis-st-reassess-valid = 783`

The acknowledgement requires:

1. `aegis-cr-reassess-valid == 1`;
2. published CR generation equals the current CR lifecycle generation;
3. the Scouting/Threat acknowledgement generation differs from that published generation.

The consumer then:

- records the exact CR lifecycle generation;
- marks the local acknowledgement state;
- clears the CR one-shot publication token.

It does not modify `aegis-st-generation`.

## Generation ownership

A new Scouting/Threat generation remains owned by the World Model observation boundary:

`aegis-wm-valid == 1` AND `aegis-st-generation != aegis-wm-generation`

The source then copies `aegis-wm-generation` into `aegis-st-generation`.

Therefore the forbidden path is blocked:

```text
CR REASSESS N
    -> ST generation N+1
    -> repeat stale observation/request
```

The permitted path is:

```text
CR REASSESS N
    -> ST acknowledges N
    -> wait
    -> World Model N+1
    -> ST consumes N+1
```

## Namespace audit

This pass exposed a pre-existing source namespace collision that the earlier namespace ledger had missed:

- Age Transition used `600–612`.
- Scouting/Threat used `610–617`.

Because all loaded `.per` goal identifiers share one numeric namespace, the overlap was unsafe. Scouting/Threat was relocated as a semantic block to `642–649`.

The pass also found `aegis-cr-failure` being referenced by Anti-Cavalry without a source `defconst`. It is now explicitly allocated at goal `650`.

These changes are namespace repairs only; symbol names and semantic ownership remain unchanged.

## Evidence audit

The Anti-Cavalry lifecycle still distinguishes:

- threat observation;
- request identity;
- authorization;
- physical `up-train escrow-state c: spearman-line` action;
- pending queue evidence;
- observed spearman-count increase;
- causal evidence;
- terminal outcome;
- REASSESS publication.

A pending queue entry is not treated as a completed unit. An observed count increase is not promoted to causal success without explicit causal evidence. The source still requires `aegis-cr-causal-evidence == 1` before confirmation, and the current source contains no proven writer establishing that evidence.

Therefore Anti-Cavalry remains fail-closed on causal attribution.

## Authorization audit

The active-request gate remains:

`aegis-cr-valid == 0` before a new Scouting/Threat generation is admitted.

Request and authorization identity remain tied to `aegis-st-generation`. Authorization is consumed on physical dispatch. A stale authorization is rejected when its authorization generation no longer matches the current threat generation.

REASSESS consumption does not bypass any of these gates.

## Reassessment invariants

| Invariant | Result |
|---|---|
| Exact CR lifecycle generation required | **PASS — source-level** |
| One-shot CR publication token | **PASS — source-level** |
| Duplicate acknowledgement blocked | **PASS — source-level** |
| REASSESS cannot manufacture ST generation | **PASS — source-level** |
| Next ST generation remains World Model-owned | **PASS — source-level** |
| Active CR request protection preserved | **PASS — source-level** |
| Authorization remains single-use | **PASS — source-level** |
| Pending ≠ completion | **PASS** |
| Causal evidence required for confirmation | **PASS — fail-closed** |
| Causal evidence writer proven | **NO — blocker remains** |
| Target-build runtime qualification | **NOT EXECUTED** |
| Central reassessment controller introduced | **NO** |

## Promotion decision

**Anti-Cavalry REASSESS consumption: IMPLEMENTED at source-contract level.**

**Anti-Cavalry reassessment loop: ARCHITECTURALLY CLOSED against stale-generation and duplicate-request shortcuts.**

**Anti-Cavalry vertical: NOT FULLY QUALIFIED.** The remaining evidence gates include causal attribution and target-build runtime qualification.

The newly discovered Scouting/Threat namespace collision has also been repaired and registered in the authoritative namespace ledger.
