# AEGIS Replay Event Model v1

This document defines the empirical event layer between parsed AoE2DE recordings and strategic interpretation.

## Evidence discipline
RAW `.aoe2record` -> parser/toolchain -> parsed data -> normalized events -> reconstructed state -> strategic interpretation.

Evidence classes: OBSERVED, DERIVED, RECONSTRUCTED, INFERRED, UNKNOWN, CONFLICT.

## Canonical envelope
Each event retains replay identity, raw sequence, simulation time when established, operation, actor, raw payload, normalized payload, evidence class, confidence, parser version, and source offset when available.

## Families
- MOVEMENT: MOVE, PATROL, DE_ATTACK_MOVE, ORDER, FOLLOW
- PRODUCTION: DE_QUEUE, BUILD, DE_TRANSFORM, BACK_TO_WORK, DELETE
- TECHNOLOGY: RESEARCH
- ECONOMY: BUY, SELL, DE_TRIBUTE
- CONTROL: STANCE, FORMATION, GATHER_POINT, TOWN_BELL, STOP
- MILITARY/SPECIAL: SPECIAL, REPAIR, UNGARRISON, GATE, FLARE
- SYSTEM: GAME, CHAT, RESIGN, POSTGAME, VIEWLOCK, SYNC

## Calibration findings
The eight-game calibration corpus contains 1,234,086 SYNC records and 20,583 ACTION records. Every sampled ACTION payload includes a sequence field. MOVE exposes coordinates and object IDs; ORDER adds target ID; BUILD adds building ID; DE_QUEUE adds unit ID and amount; RESEARCH adds technology ID.

The parser source explicitly marks DE_MULTI_GATHERPOINT as a best guess and contains unknown/partially decoded command families. Binary fields that are skipped or unnamed remain raw evidence rather than being silently interpreted.

## Rules
Object IDs are preserved exactly. Resource identifiers are not given semantic names until independently validated. Sequence is retained as ordering evidence and is not assumed to equal simulation time. Strategic decision events must preserve the information cutoff at the moment of decision; later events adjudicate outcomes only.

## Scaling gate
Full-corpus strategic interpretation begins only after event taxonomy, sequence/time mapping, object identity, resource identifiers, and parser caveats have been cross-validated on the calibration corpus.
