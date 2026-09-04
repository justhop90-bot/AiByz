# PASS 37 — C1-A Cavalry Normalization Trace

Date: 2026-09-04
Layer: 2 — HD/Promisory archaeology
Mission: C1 Threat → Capability
Status: PASS — normalization mechanism materially resolved; semantic scope still requires replay/order proof.

## 1. Question
Determine whether `cavalry` is raw enemy mounted pressure, normalized pressure, or a mixed channel; trace `camels` writes and reads.

## 2. Direct evidence
Source: live Promisory `threats.per`, `init.per`, `units.per`.

`init.per` initializes `cavalry = 0` and `camels = 0`.

`threats.per` first resets both channels. It then reads the focus player's `imperial-camel` and `camel-line` counts into `camels`, and adds those values to `cavalry`. It also adds many other mounted categories to `cavalry`, including knight-line, scout-cavalry-line, cataphract-line and war-elephant-line, with explicit weighting on some categories.

Therefore `camels` is populated from the focus player's mounted state; it is not an own-capability inventory in this phase.

## 3. Critical normalization
Immediately after the threat measurement section, `units.per` contains:

    (strategic-number camels >= 1)
    =>
    (up-modify-sn cavalry s:- camels)

This is a direct subtraction of the camel component from the aggregate cavalry channel.

Later in the camel-production section, the source again contains:

    (strategic-number camels >= 1)
    =>
    (up-modify-sn cavalry s:+ camels)

This establishes that `cavalry` is not a permanently raw channel. Its value is deliberately transformed across controller phases.

## 4. Consequence
The camel production ladder evaluates `strategic-number cavalry` while also separately testing `cavarchers` and civilization-specific unit counts. Because the subtraction occurs before the camel ladder, the exact effective meaning is phase/order dependent.

The strongest current interpretation is:

    enemy mounted observations
        → aggregate cavalry
        → camel component isolated in `camels`
        → temporary cavalry normalization
        → camel-production decision logic
        → later restoration of cavalry aggregate

This is stronger than the earlier claim that `cavalry` was simply enemy-only pressure.

## 5. Important correction to Pass 36
Pass 36 correctly established that `camel-set` is an own-capability inventory channel. However, `camels` is a different variable and is populated by the focus-player camel observations in `threats.per`.

Do not conflate:
- `camels` = threat-side camel component used during threat aggregation/normalization;
- `camel-set` = own camel capability inventory used by production thresholds.

## 6. What is proven
DIRECT / CONFIRMED:
- `cavalry` is reset before threat aggregation.
- `camels` is reset before threat aggregation.
- focus-player camel counts feed `camels`.
- `camels` contributes to `cavalry` during threat aggregation.
- `cavalry` is later decremented by `camels`.
- `camel-set` remains a separate own-capability state channel.
- camel production rules compare `cavalry` against `camel-set` thresholds.

## 7. What remains uncertain
UNCERTAIN / ENGINE-ORDER DEPENDENT:
- exact rule-file execution order and whether every normalization/restoration rule executes in the same controller pass;
- whether the temporary subtraction exists specifically to prevent enemy camels from satisfying the generic cavalry threshold while camel-specific conditions are evaluated;
- whether `cavalry` is restored before every downstream consumer or only before selected consumers;
- whether any later director consumes the normalized or restored value.

## 8. Strategic interpretation
The historical programmer is using one strategic number as a mutable aggregate rather than a single immutable semantic fact. Component extraction and reinsertion are part of the controller's computation.

This is significant for AEGIS: strategic state should distinguish immutable observations from derived decision channels. A derived channel may be intentionally normalized for one decision and restored for another.

Conceptual model:

    OBSERVED COMPONENTS
        ↓
    AGGREGATE STATE
        ↓
    TEMPORARY NORMALIZATION
        ↓
    DECISION
        ↓
    RESTORE / REUSE

This is historical evidence for phase-scoped derived state, not evidence for a modern object-oriented state model.

## 9. Falsifiers
The interpretation would weaken if runtime tracing shows that subtraction/restoration never brackets the camel decision phase, or if `cavalry` is overwritten by another source between these operations in a way that makes the subtraction irrelevant.

## 10. Next target
C1-B: establish temporal/replay evidence for a real transition. Search the replay corpus for enemy mounted pressure, production authorization proxies, camel queue events, and subsequent camel capability. Do not infer causal authorization merely from a camel appearing.
