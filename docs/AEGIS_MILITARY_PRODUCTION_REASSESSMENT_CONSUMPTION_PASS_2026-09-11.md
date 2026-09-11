# AEGIS Military Production REASSESSMENT Consumption Pass — 2026-09-11

## Decision

Military Production REASSESSMENT consumption is implemented at the **Scouting/Threat (ST) generation boundary**.

Military Production remains a **candidate seventh vertical** and remains **CANDIDATE_BLOCKED / NOT_QUALIFIED**. This pass implements lifecycle consumption only. It does not resolve selector initialization, causal verification, or runtime qualification.

## Why Scouting/Threat is the consumer

`AEGIS-military-production-v0.per` consumes Scouting/Threat state and begins its lifecycle when `aegis-mp-generation != aegis-st-generation`. Therefore ST owns the upstream observation-generation boundary for this candidate.

The correct cycle is:

```text
ST generation N
  -> Military Production lifecycle N
  -> terminal observed outcome
  -> MP REASSESS N
  -> ST acknowledges MP REASSESS N exactly once
  -> MP publication token is consumed
  -> wait for a newer World Model generation
  -> ST generation N+1
  -> possible new MP lifecycle
```

REASSESS does not create `aegis-st-generation`. Only the World Model observation boundary may advance ST generation.

## Source implementation

`AegisProm/AEGIS-scouting-threat-v0.per` now owns:

- `786` — `aegis-st-mp-reassess-generation`
- `787` — `aegis-st-mp-reassess-valid`

The consumer requires:

1. `aegis-mp-reassess-valid == 1`;
2. `aegis-mp-reassess-generation == aegis-mp-generation`;
3. the exact MP lifecycle generation has not already been acknowledged.

It then records the exact generation, sets its local acknowledgement state, and clears `aegis-mp-reassess-valid`.

The consumer does not modify `aegis-st-generation`.

## Invariants

### Exact identity

An old MP publication cannot be acknowledged as a different MP lifecycle generation.

### One-shot consumption

The MP publication token is cleared when consumed. The acknowledgement generation prevents the same publication from being accepted repeatedly.

### Upstream generation ownership

The consumer does not increment or assign ST generation. ST continues to consume World Model generations through its existing rule.

### No strategy selection

The acknowledgement does not select a military unit, threat response, or production strategy. It only records that the MP lifecycle reached a terminal observed outcome.

### Candidate isolation

Consuming REASSESS does not initialize `aegis-mp-unit`, change the candidate's qualification status, or promote the vertical.

## Evidence audit

The existing MP source still has the known selector blocker: `aegis-mp-unit` is declared and compared but has no source initializer. Runtime-only initialization is not treated as source authority.

The existing source also retains the explicit warning that an observed spearman-count increase is not sufficient by itself to establish qualified causal evidence. Accordingly, this pass does not manufacture causal evidence or upgrade the candidate to qualified status.

## Static contract coverage

`tests/vertical_slices/test_military_production_reassessment_consumption.py` verifies:

- MP reassessment publisher fields and terminal states;
- ST ownership of MP acknowledgement;
- exact lifecycle-generation identity;
- one-shot publication-token consumption;
- absence of ST-generation mutation from REASSESS;
- World Model ownership of new ST generations;
- preservation of the selector-initialization blocker;
- no strategy selection at the acknowledgement boundary;
- namespace registration;
- no central reassessment controller.

These are static source-contract tests. Target-build runtime qualification has not been executed in this pass.

## Promotion decision

**REASSESS CONSUMPTION: IMPLEMENTED at source-contract level.**

**MILITARY PRODUCTION QUALIFICATION: NOT PROMOTED.**

Remaining blockers are independent:

- selector initialization;
- causal verification;
- target-build runtime evidence;
- complete production lifecycle qualification.
