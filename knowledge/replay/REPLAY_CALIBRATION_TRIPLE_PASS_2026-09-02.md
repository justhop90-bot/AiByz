# Replay Calibration Triple Pass — 2026-09-02

## Pass A — structural reconstruction
Eight calibration bodies were profiled. Operation classes are consistently SYNC, VIEWLOCK, ACTION, CHAT, POSTGAME. Across the set: 1,234,086 SYNC and 20,583 ACTION records. SYNC and VIEWLOCK counts match in every calibration recording.

ACTION taxonomy is materially richer than a click log: MOVE, DE_QUEUE, ORDER, BUILD, GATHER_POINT, RESEARCH, SPECIAL, UNGARRISON, SELL, DELETE, DE_ATTACK_MOVE, STOP, WALL, PATROL, FORMATION, STANCE, BUY, TOWN_BELL, DE_MULTI_GATHERPOINT, FOLLOW, REPAIR, GAME, DE_AUTOSCOUT, RESIGN, and additional DE-specific commands occur.

## Pass B — semantic reconstruction
The installed mgz-fast source was inspected directly. `parse_body.py` drives `fast.meta()` and repeated `fast.operation()` calls. The DE action parser decodes player IDs and operation-specific fields. MOVE decodes coordinates/object IDs; ORDER adds target ID; BUILD adds building ID; DE_QUEUE adds unit ID/amount; RESEARCH adds technology ID. The parser itself marks DE_MULTI_GATHERPOINT as a best guess and contains skipped/unknown binary fields.

## Pass C — six-month returnability audit
No field is promoted solely because its name appears authoritative. Raw payloads remain preserved. Sequence remains ordering evidence until time semantics are independently established. Resource IDs remain unmapped until validated. Object IDs remain exact, including sentinel-like values. Conflicting header representations remain CONFLICT.

The Aug. 29 11:10 replay remains the reference specimen because binary and parsed artifacts already exist. The Aug. 20 ~3.35-second replay remains a negative-control early termination specimen. The Aug. 23 220x220 multi-player recording is retained as a structural-variation specimen.

## Research consequence
The replay corpus should be treated as an empirical measurement instrument and later as a runtime regression corpus. Strategic interpretation must operate above a validated event/state layer, never directly on parser convenience fields.

## Next gate
Validate sequence-to-time mapping, object lifecycle reconstruction, resource identifier semantics, queue/completion reconstruction, and cross-replay event invariants before scaling strategic derivation to all 156 raw recordings.
