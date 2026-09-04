# AoE2DE Raw Replay Opcode / Lifecycle Archaeology — Pass 21

**Date:** 2026-09-04
**Layer:** 2 — HD / Promisory strategic-code archaeology
**Status:** Working canon — raw opcode boundary tested; W2 remains open
**Reference replay:** `C:\Users\justh\Desktop\AEGIS-AI-LAB\06_REPLAYS\08_FORENSIC_RUNS\2026-09-02_REFERENCE\body.bin`
**Reference normalized replay:** `C:\Users\justh\Desktop\AEGIS-AI-LAB\06_REPLAYS\08_FORENSIC_RUNS\2026-09-02_REFERENCE\body_fresh.jsonl`

## Mission
Test whether the reference `.aoe2record` body contains decoded or unknown action opcodes that could provide an unexploited object-lifecycle bridge between commands and W2 world-state evidence.

## Method
The reference body was inspected using the local `mgz-fast` source and a raw action-frame scanner. The scanner respected the parser's body meta preamble, ACTION length field, action ID, payload bytes, and sequence field. Known parser action IDs were compared against the complete `mgz.fast.Action` enum. The normalized JSONL was independently inspected for operation counts and action payloads.

## Reference recording operation census
The normalized reference contains:
- SYNC: 295,407
- VIEWLOCK: 295,407
- ACTION: 6,858
- CHAT: 8
- POSTGAME: 1

The raw action-frame scan recovered exactly **6,858 ACTION frames**, matching the normalized ACTION count.

## Raw ACTION opcode census
Recovered action IDs and counts:
- MOVE (3): 2,640
- DE_QUEUE (129): 1,493
- ORDER (0): 904
- BUILD (102): 471
- UNGARRISON (111): 280
- GATHER_POINT (120): 226
- SELL (122): 194
- SPECIAL (117): 157
- RESEARCH (101): 118
- DE_ATTACK_MOVE (33): 72
- STOP (1): 47
- PATROL (21): 44
- FORMATION (23): 36
- STANCE (18): 36
- DELETE (106): 33
- WALL (105): 29
- BUY (123): 19
- DE_MULTI_GATHERPOINT (45): 13
- TOWN_BELL (127): 13
- DE_107_B (140): 7
- FOLLOW (20): 6
- DE_107_A (44): 6
- REPAIR (110): 5
- GAME (103): 4
- DE_AUTOSCOUT (38): 4
- RESIGN (11): 1

**Unknown action IDs:** 0 occurrences among the reference ACTION frames.
In particular, no reference occurrences were found for the local enum's `DE_UNKNOWN_34`, `DE_UNKNOWN_37`, `DE_UNKNOWN_39`, `DE_UNKNOWN_40`, `DE_UNKNOWN_80`, `DE_UNKNOWN_109`, `DE_UNKNOWN_130`, `DE_UNKNOWN_131`, `DE_UNKNOWN_134`, `DE_UNKNOWN_135`, `DE_UNKNOWN_136`, `DE_UNKNOWN_137`, or `DE_UNKNOWN_138` entries.

## CREATE finding
The local parser enum recognizes `CREATE`, but the reference recording contains **no CREATE ACTION frame**. Therefore CREATE cannot presently be promoted as an object-birth bridge for this specimen. Its parser presence establishes capability to recognize an opcode, not emission or semantic identity in the reference recording.

## Lifecycle correlation test
The reference contains 590 rich SYNC records with `current_time` values spanning approximately 16,170 to 10,886,319. SYNC exposes aggregate values including parser-labeled `obj_count` for players, but the source itself marks several SYNC field meanings as guesses.

Representative production/build/research/delete actions were correlated with neighboring SYNC samples using action sequence as a temporal candidate. Aggregate object counts frequently changed across intervals containing these actions, but the changes are not one-to-one with individual commands. For example, DE_QUEUE events are followed by intervals showing increases, decreases, or no change in `obj_count`; BUILD and DELETE show similarly mixed aggregate deltas. This is expected for a population aggregate and cannot establish object identity or command-to-object completion lineage.

## Strong negative finding
No hidden unknown-action lifecycle channel was exposed by the reference recording's decoded ACTION stream. The reference's 6,858 action frames are fully covered by known local enum IDs, and CREATE is absent.

This materially reduces the probability that a simple “unknown opcode” discovery will close W2 for this specimen.

## Important limitation
This pass does **not** prove that the raw `.aoe2record` contains no additional lifecycle information. It proves only that the inspected ACTION frame stream of the reference body contains no unknown action IDs and no CREATE frames, and that the currently exposed SYNC aggregates do not provide object identity lineage.

The raw body still contains non-ACTION operation structures and payload semantics that have not been exhaustively reverse-engineered at byte level. A full state reconstruction remains possible in principle through a validated interpreter if sufficient game semantics are established.

## W2 adjudication
For the tested reference replay surface:
- W0 command evidence: **CLOSED / strong**.
- W1 authoritative pending state: **OPEN** unless separately exposed by a validated state source.
- W2 object-level realization: **OPEN**.
- W3 operational capability: **OPEN at command-lineage level; individual realization requires state evidence**.
- W4 strategic effect: **OPEN**.

## Architecture conclusion
The forensic boundary is now better specified:

`L0 RAW RECORDING → L1 PARSER DECODING → L2 NORMALIZED EVIDENCE → L3 STATEFUL RECONSTRUCTION`

The reference experiment establishes that L2 is not L3 and that no obvious unknown-action shortcut bridges the gap. It does not justify claiming that L0 is exhausted.

## Next escalation
Do not reopen the scenario-loader. Before considering a bespoke simulator, inspect existing replay playback/state-reconstruction implementations and determine whether they can expose the same object-level observations available to historical `.per` code. If no practical runtime surface exists, design a minimal deterministic state interpreter rather than assuming a full game simulator is required.

## Evidence grades
- Raw reference ACTION count = normalized ACTION count: **DIRECT — LOCAL EXPERIMENT**.
- Complete known-ID coverage of reference ACTION frames: **DIRECT — LOCAL EXPERIMENT**.
- CREATE absent from reference: **DIRECT — LOCAL EXPERIMENT**.
- Unknown DE action IDs absent from reference: **DIRECT — LOCAL EXPERIMENT**.
- Aggregate SYNC changes around lifecycle commands: **DIRECT observation, non-causal**.
- Aggregate changes cannot establish individual lifecycle lineage: **COMPOSED / CONFIRMED by data shape and command ambiguity**.
- Raw format contains no further lifecycle information: **NOT PROVEN**.
- Need for stateful reconstruction to obtain arbitrary W2: **COMPOSED / PROBABLE**.

## Disposition
**Pass 21: ACCEPT WITH CORRECTIONS — WORKING CANON.**
The unknown-opcode/object-birth shortcut is not present in the reference ACTION stream. W2 remains open, but the next investigation should move from “find a missing normalized action” toward existing playback/state reconstruction surfaces and, only if necessary, a minimal validated state interpreter.