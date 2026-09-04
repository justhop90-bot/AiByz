# AoE2DE Observation / Replay Information-Boundary Archaeology — Pass 19

**Date:** 2026-09-04
**Layer:** 2 — HD / Promisory strategic-code archaeology
**Status:** Working canon — parser boundary identified

## Mission
Determine whether the missing runtime W2 bridge is caused by an information-loss problem in the normalized replay parser, or by the recorded-game representation itself.

## External parser evidence
The maintained `aoc-mgz` project explicitly distinguishes a fast parser from a fuller parser. The fast parser skips data considered rarely needed; the full parser attempts to parse substantially more. Its current support table also shows full-body support is version-dependent, while newer DE builds may lack full-body support.

The full model parses initial player/gaia objects from the replay header and constructs object records containing dataset object type, class, object id, instance id, index, and position. During body processing it records actions and SYNC-derived aggregate player time-series values. It does not reconstruct a continuously mutated per-object world model from the action stream.

## Critical distinction
The replay parser's `get_objects()` surface is derived from header objects. Those are objects that exist at the start of the recorded game. This is not equivalent to a chronological object-lifecycle database.

The body parser records commands such as DE_QUEUE, RESEARCH, BUILD, and DE_ATTACK_MOVE. These commands contain identifiers useful for command interpretation, but they do not themselves supply a complete post-command object-state snapshot.

Therefore upgrading from `mgz-fast` to the full parser is valuable for richer header/object metadata and model enrichment, but it should not be assumed to solve dynamic W2 lifecycle attribution.

## Object-state archaeology
The parser's historical object structure demonstrates that replay/header object records can contain fields corresponding to the kinds of state the AI's `object-data-*` vocabulary reasons about: object identity, hitpoints, object state, owner context, position, under-attack state, movement/path data, target IDs, action/order state, AI state, building `built`, `build_points`, unique build ID, production queue, and research/action structures.

This is powerful evidence that the replay format/parser ecosystem knows substantially more about object state than the normalized ACTION JSONL exposes. However, the source inspected places these rich structures in the header object parser. It does not establish that equivalent snapshots are emitted throughout the replay body.

## W2 hypothesis adjudication
Three hypotheses were tested conceptually:

### H1 — mgz-fast normalization is the only limitation
**DISPROVEN / too strong.** The fuller parser exposes substantially richer initial-object structures than mgz-fast.

### H2 — switching to full mgz may expose enough dynamic state to close W2
**NOT SUPPORTED.** Full parsing enriches initial object structures and parses more body information, but the inspected architecture still processes the body as operations/actions rather than replaying a continuously mutable object database.

### H3 — the recording itself is primarily an action log plus initial state, requiring replay execution to reconstruct arbitrary dynamic state
**SUPPORTED by available parser documentation and implementation architecture.** The recorded-game description explicitly characterizes the header as an initial-state snapshot and the body as moves that the game applies to mutate state. The parser can parse those moves, but arbitrary world-state reconstruction requires applying game semantics to those moves.

## New strategic conclusion
The W2 problem is therefore not simply “we haven't found the right JSON field.” The correct conceptual model is:

`INITIAL WORLD SNAPSHOT + ACTION STREAM + GAME SEMANTICS = RECONSTRUCTED WORLD STATE`

A static parser can expose inputs. A replay engine can reconstruct state by executing those inputs.

This explains why the historical AI has access to live `object-data-*` observations while our replay JSONL does not: the AI runs inside the game engine against live objects; the replay parser is primarily decoding recorded inputs and selected snapshots/aggregates.

## Architecture implication for AEGIS
Do not design the forensic replay layer as if it were inherently a world-state database.

Use two distinct layers:

1. **Replay evidence layer:** immutable commands, timestamps, initial objects, available sync aggregates, and parser-derived facts.
2. **Replay simulation layer:** a stateful interpreter that applies recorded commands against a validated game model and produces object/world postconditions.

Only the second layer can legitimately attempt broad W2/W3 reconstruction.

## What remains open
A full replay simulator remains an engineering project and is not justified merely by the need to close one evidence gap. Before building one, we should determine whether existing engine-compatible replay playback, genie-rs/recage-style implementations, or another authoritative runtime surface can provide state observations more efficiently.

The immediate next investigation should therefore inventory existing replay-playback/state-reconstruction implementations and compare their actual object-lifecycle coverage against the AEGIS W0-W4 evidence ladder.

## Evidence grades
- Fast/full parser distinction: **DIRECT — EXTERNAL SECONDARY**.
- Rich object fields in parser source: **DIRECT — EXTERNAL SECONDARY**.
- Header initial objects vs body actions architecture: **DIRECT — EXTERNAL SECONDARY**.
- H1 adjudication: **COMPOSED**.
- H2 adjudication: **COMPOSED / UNCERTAIN**.
- H3: **COMPOSED / PROBABLE**.
- AEGIS two-layer replay architecture: **AEGIS-GENERALIZATION**.

## Disposition
**Pass 19: ACCEPT WITH CORRECTIONS — W2 remains open, but the information boundary is now materially better characterized.**
