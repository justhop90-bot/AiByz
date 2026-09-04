# AoE2DE Observation / Replay Information-Boundary Archaeology — Pass 19 (AMENDED)

**Date:** 2026-09-04
**Layer:** 2 — HD / Promisory strategic-code archaeology
**Status:** Working canon — parser boundary characterized; raw-format lifecycle archaeology remains open

## Amendment reason
Deep QC found that the original pass correctly identified the parser/state boundary but used language that could be read as proving more about the raw `.aoe2record` format than the inspected evidence establishes. This amendment separates four layers: raw recording bytes, parser decoding, normalized replay representation, and state reconstruction.

## Mission
Determine whether the missing runtime W2 bridge is caused by information loss in the normalized replay parser, by limitations of the inspected parser/model, or by the recorded-game representation itself.

## Four-layer forensic model
1. **L0 — Raw recording:** bytes and encoded operations actually present in the `.aoe2record`.
2. **L1 — Parser decoding:** structures and events understood by a parser implementation.
3. **L2 — Normalized representation:** the JSONL/action/SYNC surface exposed to our forensic pipeline.
4. **L3 — Stateful reconstruction:** a validated interpreter that applies recorded events through game semantics and produces world state at time T.

The strongest established boundary is **L2 != L3**. The inspected parser implementations also do not establish that L1 automatically supplies L3. L0 has not yet been exhaustively exhausted.

## External parser evidence
The maintained `aoc-mgz` project explicitly distinguishes a fast parser from a fuller parser. The fast parser is intentionally stripped down; the fuller parser parses materially richer information. The fuller model includes initial player/gaia object records and substantially richer object metadata than the normalized ACTION JSONL.

The fuller implementation processes body operations/actions and SYNC-derived aggregate values. The inspected implementation does not provide a continuously mutated per-object world-state database equivalent to the live object observation surface available to `.per` AI code.

These are **external secondary technical evidence**, not Layer-2 historical authority.

## Critical distinction
Header object records are not equivalent to a chronological object-lifecycle database. Likewise, body commands such as DE_QUEUE, RESEARCH, BUILD, and DE_ATTACK_MOVE contain identifiers useful for command interpretation but do not themselves constitute complete post-command object-state snapshots.

Therefore switching from `mgz-fast` to a fuller parser is valuable for richer initial-object metadata and model enrichment, but it is not demonstrated to close dynamic W2 lifecycle attribution.

## Object-state archaeology
The inspected fuller parser/model contains fields corresponding to many categories relevant to the AI's `object-data-*` vocabulary: identity, type, ownership context, position, hitpoints/state, movement/path information, target/action state, and building production/construction/research structures.

This establishes that the parser ecosystem understands substantially more object metadata than the normalized ACTION JSONL exposes. It does **not** establish that equivalent dynamic snapshots are emitted throughout the replay body.

## Hypothesis adjudication
### H1 — mgz-fast normalization is the only limitation
**REJECTED AS A SUFFICIENT EXPLANATION.** The fuller parser exposes substantially richer initial-object structures than mgz-fast. This does not prove mgz-fast is never responsible for information loss; it proves only that it is not the whole explanation.

### H2 — switching to full mgz may expose enough dynamic state to close W2
**NOT SUPPORTED by the inspected implementation.** Full parsing enriches initial-object structures and parses more body information, but the inspected architecture does not itself provide a continuously reconstructed dynamic object database. This remains an implementation finding, not a proof about every possible parser/runtime.

### H3 — arbitrary dynamic state requires state reconstruction from initial state, recorded events, and game semantics
**COMPOSED / PROBABLE.** Available parser documentation describes the recording as an initial state followed by recorded moves/events that the game applies to mutate state. A parser can decode those inputs; reconstructing arbitrary world state requires applying validated game semantics or an equivalent authoritative runtime.

## CREATE and unknown-opcode boundary
The local `mgz-fast` enum contains CREATE and multiple `DE_UNKNOWN_*` action IDs. CREATE is decoded by the inspected implementation only into limited fields such as player and coordinates; this does not prove that CREATE is an object-birth event for the reference DE recording.

Unknown DE opcodes are therefore legitimate raw-format reverse-engineering targets. Their presence in parser code proves parser recognition, not semantic closure. Their absence/presence in a particular recording must be measured independently.

## Correct conceptual model
`INITIAL WORLD SNAPSHOT + RECORDED EVENT STREAM + VALIDATED GAME SEMANTICS = RECONSTRUCTED WORLD STATE`

This is an engineering model supported by the inspected architecture, not a claim that the raw recording has been exhaustively specified.

## Architecture implication for AEGIS
Maintain two explicit forensic layers:

1. **Replay evidence layer:** immutable commands/events, raw/decoded temporal order, initial objects, available SYNC aggregates, and parser-derived facts.
2. **Replay reconstruction layer:** a stateful interpreter/runtime surface that applies recorded events and exposes postconditions.

Do not treat inferred pending state as W1 unless the recording/parser provides authoritative evidence for that pending state. Likewise, aggregate SYNC fields whose semantics remain parser-level guesses must retain that uncertainty.

## Evidence discipline
Use the following distinctions permanently:

`PARSER CAPABILITY != RECORDING EVIDENCE != SEMANTIC INTERPRETATION != RECONSTRUCTED WORLD STATE`

Never write “the replay contains no object state.” State instead that the **tested normalized body surface does not expose sufficient dynamic object-state lineage for the requested W2 claims**.

Never write “full mgz cannot reconstruct state.” State only that the **inspected full parser/model does not itself provide a continuously reconstructed dynamic world-state database**.

Never promote external parser implementation details to Layer-2 historical authority.

## What remains open
Raw `.aoe2record` opcode/lifecycle archaeology has not yet exhausted the possibility of additional undocumented or poorly decoded lifecycle signals. In particular, CREATE and unknown DE opcodes require systematic occurrence, payload, temporal-neighborhood, SYNC-delta, and object-ID correlation analysis.

If raw-format archaeology fails to reveal sufficient lifecycle evidence, the next escalation is to inventory existing replay playback/state-reconstruction implementations before considering a bespoke interpreter.

## Evidence grades
- Fast/full parser distinction: **DIRECT — EXTERNAL SECONDARY**.
- Rich object fields in parser source: **DIRECT — EXTERNAL SECONDARY**.
- Header initial objects vs body operations: **DIRECT — EXTERNAL SECONDARY**.
- L2 != L3: **COMPOSED / CONFIRMED for the tested pipeline**.
- H1: **REJECTED AS SUFFICIENT EXPLANATION**.
- H2: **NOT SUPPORTED / UNCERTAIN beyond inspected implementation**.
- H3: **COMPOSED / PROBABLE**.
- AEGIS two-layer replay architecture: **AEGIS-GENERALIZATION**.

## Disposition
**Pass 19 amended: ACCEPT WITH CORRECTIONS — WORKING CANON.**
The amendment narrows the claims without weakening the central finding: the current normalized replay surface does not close W2, the inspected parser does not automatically supply L3 state reconstruction, and raw-format lifecycle archaeology remains the proper next experiment.
