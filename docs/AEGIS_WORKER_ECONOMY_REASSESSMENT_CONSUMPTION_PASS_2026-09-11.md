# AEGIS Worker Economy REASSESSMENT Consumption Pass — 2026-09-11

## Status

**IMPLEMENTED at source-contract level.**

This pass implements downstream consumption of the Worker Task Verification (WTV) REASSESS event without allowing the terminal worker-task result to manufacture a new worker-economy generation, replay a stale request, or create a central reassessment controller.

Target-build runtime qualification is not claimed by this document.

## 1. Correct consumer boundary

The WTV module owns publication of the worker-task terminal lifecycle event:

```text
WTV lifecycle generation
    -> WTV reassess-generation / reassess-valid
```

The correct downstream acknowledgement owner is **Worker Role Vector (WRV)**, not Worker Role Census (WRC).

Reason:

- WRC is the authoritative observer that publishes fresh engine role counts and advances the observation generation.
- WRV consumes that observation and converts it into the next role-vector frame.
- WRV is therefore the first semantic owner capable of acknowledging the prior task lifecycle while still respecting the requirement that the next generation must originate from a new WRC observation.
- Economic Demand (ED) consumes WRV, and the remainder of the worker-economy vertical follows downstream.

This keeps the architecture distributed and preserves the boundary between observation, reconciliation, demand, selection, execution, and verification.

## 2. New namespace allocation

Worker Role Vector now owns:

- `778` — `aegis-wrv-reassess-generation`
- `779` — `aegis-wrv-reassess-valid`

These slots were added to the repository-wide namespace ledger before promotion.

## 3. Acknowledgement contract

WRV consumes WTV REASSESS only when all of the following hold:

```text
WTV reassess-valid == 1
WTV reassess-generation == WTV lifecycle generation
WRV acknowledgement generation != WTV reassess-generation
```

On acknowledgement WRV:

1. records the exact WTV lifecycle generation;
2. sets its local acknowledgement-valid bit;
3. consumes the WTV publication token.

The acknowledgement does **not** increment `aegis-wrv-generation`.

## 4. New-generation gate

A new WRV generation remains owned by WRC:

```text
WRC valid == 1
AND
WRV generation != WRC generation
```

The WRV lifecycle then copies the WRC generation and observation timestamp.

Therefore:

```text
WTV REASSESS
    !=
new WRV generation
```

The former merely records that the previous worker task lifecycle reached a terminal observed outcome. The latter requires a fresh worker-role observation.

## 5. Full worker-economy chain

```text
WRC fresh engine observation
    ↓
WRV generation N
    ↓
ED generation N
    ↓
EDA arbitration generation N
    ↓
WTS candidate-selection generation N
    ↓
WTC authorized request N
    ↓
physical worker task command
    ↓
WTV verification generation N
    ↓
terminal observed result
    ↓
WTV REASSESS(N)
    ↓
WRV acknowledges N exactly once
    ↓
WAIT
    ↓
WRC publishes a fresh observation generation N+1
    ↓
WRV generation N+1
    ↓
new economic-demand lifecycle
```

The important property is that the cycle closes through a **new observation**, not through feedback from the terminal event itself.

## 6. Evidence preservation

The WTV module distinguishes:

- unknown result;
- observed task state;
- worker missing;
- target not observed;
- identity mismatch;
- terminal confirmation/failure.

The REASSESS consumer does not reinterpret these outcomes as strategic success, resource productivity, or causal proof. It only acknowledges that the prior lifecycle is terminal and permits the distributed system to reconsider after a new observation.

## 7. Duplicate-request protection

The downstream command layer already requires:

```text
aegis-wtc-valid == 0
```

before admitting a new execution lifecycle.

The WTC request generation must differ from WTS generation, and request identity is copied downstream rather than regenerated. Authorization is consumed at physical dispatch.

Thus REASSESS cannot directly authorize a second physical command.

## 8. No stale-generation shortcut

The following shortcut is explicitly forbidden:

```text
WTV terminal N
→ REASSESS N
→ WRV generation N again
→ ED generation N again
→ duplicate request
```

Instead:

```text
WTV terminal N
→ REASSESS N
→ WRV acknowledgement of N
→ WRC fresh observation N+1
→ WRV generation N+1
```

## 9. No central controller

No reassessment controller was added.

The ownership remains distributed:

- WTV — publishes terminal worker-task REASSESS;
- WRV — acknowledges WTV REASSESS;
- WRC — owns fresh worker-role observation generation;
- ED — derives economic demand from WRV;
- EDA — arbitrates demand;
- WTS — selects candidates;
- WTC — authorizes and dispatches physical action;
- WTV — verifies the resulting observable worker state.

## 10. Qualification boundary

This pass closes the **downstream REASSESS consumption contract** for the worker economy at source level.

It does not qualify the worker economy as a complete runtime vertical.

Independent limitations remain, including the current WRV policy targets being zero in source, which makes the economic demand path normally demand-starved until another policy writer changes those targets. The source explicitly defines those targets as conservative V0 policy inputs rather than the final Byzantine economy scheduler.

Target-build execution evidence remains a separate qualification gate.

## 11. Tests

Added:

`tests/vertical_slices/test_worker_economy_reassessment_consumption.py`

The tests verify:

- WTV publisher identity;
- WRV acknowledgement ownership;
- one-shot publication consumption;
- upstream-only generation creation;
- reset of acknowledgement state on a new WRC observation;
- end-to-end generation ordering;
- active-request protection;
- preservation of verification uncertainty;
- absence of a central reassessment controller.

These are static source-contract tests and do not constitute target-build runtime qualification.
