# AEGIS A1 State Lifecycle Trace — 2026-09-05

## Scope
Forensic trace of the verified untouched stock HD AI closure on AoE2DE build 101.103.48987.0. This pass traces writers, readers, initialization/reset, value domain, and semantic ownership for the strongest stock analogues relevant to the AEGIS Layer-3 state ABI.

## Findings

### `sn-cavalry-threat` — stock threat classifier
- Definition: `sn-cavalry-threat = 65`.
- Initialization: line 5167 sets it to `0`.
- Primary classifier writes: lines 6917–6963 set levels `1`, `2`, `3`, `4` from enemy composition thresholds.
- Recovery/poor-scouting writes: lines 6997–7006, 7008–7016, 7018–7031, and the DEATH-MATCH block at 7034–7045 can raise the signal when scouting evidence is weak or contextual heuristics apply.
- Readers include downstream strategy/production rules; the channel is therefore persistent strategic state, not a transient scratch value.
- Semantic domain is ordinal threat severity, not a unit count and not an AEGIS transaction record.
- **Disposition: stock input/analogue only. Do not reuse.**

### `anti-cavalry-threat-goal` — stock response latch
- Definition: `anti-cavalry-threat-goal = 7`.
- Initialization: line 5168 sets it to `0`.
- Writer: line 6973 sets it to `1` under explicit anti-cavalry conditions involving enemy cavalry/camel/mameluke/spearman populations and time context.
- Readers include lines 7947, 8859, 8875, 8901, 8917, 8927, 9148, 9171, and 9662, among others.
- It is therefore a stock response-policy latch with cross-module consumers.
- **Disposition: historical analogue/input only. Do not reuse.**

### `unit-goal` — stock production selector
- Definition: `unit-goal = 4`.
- Extremely high traffic: 432 `set-goal` writes, 722 ordinary goal reads, and 122 `up-compare-goal` reads in the current closure census.
- It carries many unrelated production selections and values, including unit lines, unique units, wonder-related choices, and other production decisions.
- **Disposition: reject as AEGIS producer/candidate state. Existing stock ownership is too broad.**

### `attack-status-goal` — stock attack FSM
- Definition: `attack-status-goal = 24`, explicitly documented as indicating whether an attack stops or regroups.
- Initialization/reset behavior is embedded in the attack subsystem rather than serving as generic storage.
- Writes include `retreat` and `tsa`; readers consume those attack-state meanings.
- **Disposition: reject. Low traffic does not imply free capacity; semantics are incompatible with AEGIS execution state.**

### `sn-resource-control` — stock global resource policy
- Definition: `sn-resource-control = 191`.
- High cross-module traffic: 91 writes and approximately 501 reads in the closure census.
- A reset rule at lines 5962–5968 forces it to `0` when its policy conditions permit, while other rules use values `0`, `2`, and `3` to gate resource/production behavior.
- This is global stock resource policy, not reservation ownership or discretionary-resource accounting for an AEGIS transaction.
- **Disposition: input/analogue only. Do not reuse.**

## Critical ABI conclusion
Numeric availability is not sufficient for allocation. The trace establishes that a candidate state channel must be free of conflicting stock ownership *and* have compatible lifecycle, value domain, reader/writer topology, and reset semantics.

The strongest stock cavalry chain is:

`enemy observations → ordinal threat classification → persistent strategic signal → response-policy latch → downstream production/strategy`

This is useful as a reference implementation for AEGIS observation/classification, but it is not an AEGIS-owned transaction envelope.

## Layer-2 gate status
Layer 2 remains **90/100**.

Closed:
- stock runtime closure identified
- machine evidence captured
- typed state census completed
- numeric collision map completed
- principal stock analogue ownership traced
- writer/reader/reset semantics established for the principal analogues
- stock-vs-AEGIS ownership boundary established

Remaining gates:
1. dedicated AEGIS namespace candidate audit
2. target-build runtime legality validation of candidate state primitives
3. persistence/transition smoke test proving the selected AEGIS state representation survives the real interpreter lifecycle
4. final ABI freeze

**No numeric channel allocation is authorized by this document.**
