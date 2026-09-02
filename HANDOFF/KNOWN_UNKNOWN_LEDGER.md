# AEGIS-BYZ Known / Unknown Ledger

Date: 2026-09-02

## CONFIRMED / HIGH-CONFIDENCE
- PORPHYRA_V2_2_2 is the control baseline by project authority.
- V3 canonical strategy source is user-designated.
- V3 is modular and contains a distributed rule/control system.
- HD source contains substantial strategic knowledge encoded as rules, state variables, timers, and transitions.
- Replay ACTION payload envelope is `[command_name, command_payload]`.
- Eight-game calibration corpus contains 20,583 ACTION records and 30 command names.
- DE_QUEUE schema is `amount, object_ids, player_id, sequence, unit_id`.
- Eight-game DE_QUEUE aggregate is 4,991 commands.
- ACTION sequence streams are non-decreasing in the calibration corpus.
- Sequence is non-unique.
- Seven of eight calibration recordings have last ACTION sequence equal to POSTGAME world_time.
- One recording has a 3,500-unit terminal interval after its final ACTION.
- SYNC current_time is explicitly described by preserved parser documentation as duration from beginning in ms.
- JSONL serialization order must not be treated as causal order.
- Object disappearance is not sufficient evidence of destruction.

## PROBABLE
- ACTION sequence is a command-associated replay/simulation temporal coordinate.
- Equal sequence values define temporal clusters.
- Production can be reconstructed through queue-to-object lineage when identity evidence is sufficient.
- Production capacity is a strategic resource.
- Timers in the historical AI implement hysteresis, memory, or rate limiting in addition to timing.
- The historical AI is best modeled as a distributed finite-state/control system.

## UNPROVEN
- Exact native unit of ACTION.sequence.
- Universal temporal semantics across all AoE2DE patches/save versions.
- Complete object identity semantics for every object type.
- Exact queue admission semantics from replay alone.
- Universal completion signatures for every production type.
- Exact resource reservation timing visible to replay reconstruction.
- Full native semantics of every ACTION command.
- Complete Ghidra callgraph proof of all AI scheduler/loader/execution interfaces.

## EXPLICITLY REJECTED
- ADPromisory as architecture/evidence substrate.
- WarCouncil as architecture/evidence substrate.
- Wholesale inheritance of V4.
- Treating V3's fragmented implementation as the target architecture.
- Treating queue commands as completed units.
- Treating missing objects as dead.
- Treating hindsight knowledge as player knowledge.
- Treating strings alone as native semantic proof.

## Required falsifiers
Every future promoted hypothesis must state what observation would disprove it. Unknowns must remain visible rather than being silently converted into constants.