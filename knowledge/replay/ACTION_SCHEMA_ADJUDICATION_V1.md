# ACTION Schema Adjudication v1

## Purpose
Establish the first validated command taxonomy from the eight-game calibration corpus. This is an empirical schema, not a claim that every parser field is semantically authoritative.

## Corpus
Eight parsed DE recordings; all body streams contained zero malformed JSON lines and reached POSTGAME. Observed ACTION commands: 30 distinct command names. Total ACTION records: 20,583.

## Command frequency
MOVE 6811; DE_QUEUE 4991; ORDER 2944; BUILD 2206; GATHER_POINT 1083; RESEARCH 601; UNGARRISON 402; SPECIAL 355; SELL 232; DELETE 222; DE_ATTACK_MOVE 147; STOP 82; DE_TRANSFORM 75; WALL 68; PATROL 67; GAME 44; FORMATION 39; STANCE 38; DE_MULTI_GATHERPOINT 38; TOWN_BELL 33; BUY 30; DE_AUTOSCOUT 12; RESIGN 10; FLARE 10; FOLLOW 9; REPAIR 9; DE_107_B 8; GATE 7; DE_107_A 6; BACK_TO_WORK 4.

## Envelope invariant
Every sampled ACTION record uses the two-part payload envelope: command name followed by command payload. The prior analyzer that treated payload as a dictionary was invalid and has been quarantined.

## Semantic confidence policy
A command name is OBSERVED. Its payload keys are OBSERVED. Their gameplay meaning is promoted only when supported by parser implementation, repeated corpus behavior, and/or independent engine evidence.

## Initial normalization families
Movement/order: player/object/target/location fields where consistently present.
Production: DE_QUEUE and GATHER_POINT require lifecycle reconstruction before strategic interpretation.
Research: RESEARCH establishes command occurrence and technology payload; completion remains separate.
Building: BUILD establishes command occurrence and construction payload; completion must not be inferred from command alone.
Military: DE_ATTACK_MOVE, PATROL, STANCE, FORMATION, FOLLOW, STOP are commands, not outcome events.
Economy: BUY/SELL are explicit market actions; resource consequences require state evidence.
Lifecycle: DELETE, UNGARRISON, DE_TRANSFORM require specialized disappearance/transition adjudication.

## Parser-warning boundary
Parser source explicitly marks some decoding paths as best guesses or unknown. Such records remain parser-derived and uncertain until independently validated.

## Reproducibility
The registry must be regenerated from parsed JSONL, never hand-edited. Derived counts must be recomputable from preserved source streams.

## Negative evidence
Absence of a command is not evidence that the command was unavailable; it may simply not have been selected. Absence of a payload field may indicate command-specific optionality, parser omission, or a genuinely absent value.

## Version boundary
The eight calibration recordings are labeled version 101.103.48987.0. This supports within-version comparison only; it does not establish invariance across versions.

## Scaling decision
The taxonomy is stable enough for controlled normalization, but not sufficient to certify universal field semantics. Continue object lifecycle and time adjudication before full 156-game strategic extraction.
