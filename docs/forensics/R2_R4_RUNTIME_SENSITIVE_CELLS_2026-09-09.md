# AEGIS / AiByz — R2/R4 Runtime-Sensitive Cell Extraction

**Date:** 2026-09-09
**Status:** OPEN — probe design only; no runtime claims

## Purpose

Convert the static lifecycle join into the smallest set of observations that can discriminate competing lifecycle hypotheses. This artifact does not claim that a rule fires, that a write persists, or that a downstream consequence occurred.

## Probe A — cavalry threat scalar

| Cell | Static evidence | Competing hypotheses | Measurement required |
|---|---|---|---|
| Initial value | line 5167 writes 0 under `(true)` | reset once / reset repeatedly / overwritten before observation | observe value across repeated control cycles |
| Threshold ladder | lines 6927/6939/6951/6963 | monotonic ladder / overwrite race / unreachable branch | controlled enemy cavalry counts with timestamps |
| Contextual writers | 7006/7016/7031/7045 | modifiers / alternative detector / race with ladder | isolate time, stable, strategy, age, civ predicates |
| Persistence | many downstream readers | persistent state / transient scratch | sample before and after source condition disappears |
| Consequence | readers span production/research/military | causal downstream response / correlation only | pair scalar transition with first downstream state transition |

## Probe B — attack retreat cluster

| Cell | Static evidence | Measurement |
|---|---|---|
| `retreat-now-goal` 0→1 | seven assertion families | record exact precondition, transition, and duration |
| `retreat-now-goal` 1/2→0 | five clear writers | identify exact clearing rule and whether reassertion follows |
| `attack-status-goal` → `retreat` | paired writers with retreat policy | determine whether transition is same evaluation window or delayed |
| `attack-status-goal` → `tsa/groups` | late attack-control region | identify precedence/order when multiple predicates overlap |
| `restart-attack-goal` 0→1→0 | one assertion/two clears | establish one-shot persistence and re-entry conditions |

## Probe C — anomaly

Preserve `up-compare-goal attack-goal >= 29876` exactly. Test parser/compiler acceptance separately from runtime reachability. A successful compile does not prove the literal is semantically meaningful; failure does not justify source correction without identifying the actual grammar/validator boundary.

## Observation schema

Every sample should record: `run_id`, `build_identity`, `scenario_state`, `game_time`, `channel`, `observed_value`, `source_trigger_candidate`, `precondition_state`, `postcondition_state`, `evidence_level`, `confidence`, `notes`.

Required evidence ladder: `INTENTION → AUTHORIZED → ISSUED → ACCEPTED/QUEUED → PENDING → CREATED → AVAILABLE → DEPLOYED → EFFECTIVE`.

## Disqualifiers

- Do not infer execution from source order.
- Do not infer one-time initialization from `(true)`.
- Do not treat numeric equality as channel identity.
- Do not use replay command records as proof of world-state completion.
- Do not promote the stock channels into AEGIS-owned state.

## Next gate

Runtime-sensitive cells → controlled probe implementation → observed transition table → R2/R4 closure decisions.

