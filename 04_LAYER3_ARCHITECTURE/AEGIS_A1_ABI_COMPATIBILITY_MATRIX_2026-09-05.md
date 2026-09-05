# A1 ABI Compatibility Matrix — Cavalry Threat Containment

**Date:** 2026-09-05  
**Build:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Evidence basis:** committed A1 stock manifest, typed state census, collision map, and C1 threat→camel specification.  
**Status:** ABI-GATE / allocation not authorized.

## Purpose

This matrix tests the planned 19-field AEGIS Cavalry Threat Containment state envelope against the verified stock runtime before any numeric goal/SN/timer allocation or production implementation.

The governing test is **semantic compatibility**, not numeric vacancy. A stock channel is reusable only if its primitive type, meaning, writer set, reader set, lifecycle, ownership, and update cadence are compatible with the AEGIS field. A matching number alone is insufficient.

## Verdict

**No stock state channel is currently cleared for direct reuse as a core AEGIS control-envelope field.** Several stock channels are valuable observation inputs or historical analogues, but they are already owned by stock semantics. The matrix therefore separates **usable as input evidence** from **safe as AEGIS-owned state**.

## Matrix

| AEGIS field | Intended semantic role | Stock analogue / evidence | Reuse status | Reason / next proof |
|---|---|---|---|---|
| `OBS.ENEMY_CAVALRY` | observed enemy cavalry quantity/classification | `sn-cavalry-threat` = 65; stock cavalry/threat definitions; unit-count facts | **INPUT ONLY** | Stock threat SN is an existing strategic signal, not an AEGIS-owned observation register. Exact freshness/count semantics require runtime trace. |
| `OBS.ENEMY_CAVALRY_AGE` | age/context at which enemy cavalry observation applies | `sn-current-age` = 190 | **REJECT** | `sn-current-age` is the AI's own current age, not enemy age. Same primitive does not imply same meaning. |
| `THREAT.CAVALRY_ACTIVE` | normalized threat-active state | `anti-cavalry-threat-goal` = 7; `enemy-sighted-goal` = 23; `attack-status-goal` = 24 | **INPUT/ANALOGUE ONLY** | These channels have existing stock meanings and writers. None is proven equivalent to an AEGIS lifecycle-safe threat-active latch. |
| `CAP.CAMEL_CURRENT` | current available camel capability/mass | camel-line unit IDs and stock unit-count facts | **DERIVED** | Best represented by engine facts/counts rather than hijacking a persistent stock goal/SN. Need exact chosen fact and cadence test. |
| `CAP.CAMEL_REQUIRED` | computed required counter mass | no semantically dedicated stock channel | **NO CLEARANCE** | Must be AEGIS-owned derived state or recomputable value; no stock field has compatible ownership/lifecycle evidence. |
| `CAP.CAMEL_DEFICIT` | required minus current capability | no dedicated stock channel | **NO CLEARANCE** | Arithmetic result should not be stored in an unrelated stock channel. Candidate scratch storage needs explicit lifecycle proof. |
| `CAND.PRODUCER` | selected producer/building candidate | `unit-goal` = 554; stock production logic | **REJECT** | `unit-goal` is heavily multiplexed stock production state. It cannot be assumed safe as a stable AEGIS candidate register. |
| `CAND.STATUS` | candidate lifecycle state | `status-pending`, `status-ready`, `status-resource`, etc.; `object-data-status` = 19 | **REJECT** | These are existing status vocabularies/data fields, not an AEGIS candidate-state namespace. |
| `COMMIT.VALID` | coherent publication/commit latch | no dedicated stock analogue | **NO CLEARANCE** | `VALID` must mean publication coherence; stock threat/attack flags do not establish that contract. |
| `COMMIT.OWNER` | owner identity of committed work | `object-data-ownership` exists as an object-data concept | **REJECT** | Object ownership is not state-record ownership. Different semantic domain. |
| `COMMIT.GEN` | generation/version of committed state | stock generation-related names exist, but no proven AEGIS transaction generation | **NO CLEARANCE** | Numeric coincidence with generation constants is insufficient. Requires explicit generation lifecycle. |
| `COMMIT.STAGE` | commit lifecycle stage | no dedicated compatible stock field | **NO CLEARANCE** | Existing stock stages/statuses are subsystem-specific. |
| `EXEC.STAGE` | execution lifecycle stage | stock production commands and statuses | **REJECT** | `train`/`can-train` establish commands/feasibility, not a persistent AEGIS execution-stage register. |
| `EXEC.EXPECTED_GEN` | generation expected by execution verifier | no dedicated stock analogue | **NO CLEARANCE** | Requires cross-event correlation between authorization and observed execution. |
| `RES.RESERVED` | resources committed/reserved to this objective | stock escrow/resource-control machinery | **INPUT/ANALOGUE ONLY** | Existing escrow is strategically meaningful but cannot be claimed as AEGIS reservation ownership without exact path proof. |
| `RES.DISCRETIONARY` | resources not reserved and available for allocation | stock resource-control/gather percentages | **INPUT/ANALOGUE ONLY** | Resource-control state is global stock policy, not AEGIS reservation accounting. |
| `ARB.EPOCH` | arbitration epoch/version | no dedicated stock analogue | **NO CLEARANCE** | Requires explicit monotonic lifecycle semantics. |
| `ARB.DIRTY` | arbitration invalidation/recompute latch | no dedicated stock analogue | **NO CLEARANCE** | Existing timers/goals may trigger work but do not establish the required dirty-bit contract. |
| `VERIFY.LEVEL` | evidence level reached after execution | `sn-military-level` = 190 and other level/status concepts | **REJECT** | Existing levels describe other stock concepts; verification evidence is a distinct AEGIS semantic domain. |

## Important stock observations

The machine census reports 87 referenced goal channels, 143 strategic-number channels, and 29 timer channels in the captured stock closure. It also records 4,893 numeric `defconst` declarations across 1,480 unique declared symbols. These counts are inventories, not available ABI capacity.

The collision evidence demonstrates why numeric allocation cannot be done from gaps alone: multiple symbolic names can legitimately share a numeric value across different semantic domains or contexts. For example, numeric values used by `sn-cavalry-threat`, `request`, and unrelated stock constants are not thereby interchangeable.

The stock runtime also contains high-frequency writers such as the four gatherer-percentage SNs and substantial writes to `unit-goal`, `control-goal`, and `strategy-goal`. High-frequency, heavily multiplexed channels are particularly poor candidates for AEGIS transaction state.

## C1-specific conclusion

The historical C1 evidence establishes a concrete mechanism from enemy cavalry/cavalry-archer observation through contextual response logic toward camel production, with production feasibility gates. It does **not** establish a reusable historical transaction ABI for AEGIS.

Therefore AEGIS should reuse the **engine facts and historically demonstrated signals as observations where appropriate**, while maintaining its own explicitly owned state for commitment, generation, arbitration, reservation, execution correlation, and verification.

## Allocation gate

The following remain **blocked** until additional evidence exists:

1. numeric goal allocation;
2. numeric SN allocation;
3. timer allocation;
4. flag allocation;
5. production `.per` implementation of the 19-field envelope.

## Required next evidence pass

1. Build exact writer→reader edges for each candidate stock analogue from the committed census.
2. Trace lifecycle and reset conditions for `sn-cavalry-threat`, `anti-cavalry-threat-goal`, `unit-goal`, `attack-status-goal`, `sn-resource-control`, and related channels.
3. Establish exact runtime freshness behavior for the relevant threat facts/SNs.
4. Determine whether any scratch goal/state mechanism can be isolated without aliasing stock ownership.
5. Only then evaluate a **dedicated AEGIS goal namespace** or other state representation, with build-scoped empirical validation.

**Decision:** A1 ABI remains unallocated; evidence work continues.