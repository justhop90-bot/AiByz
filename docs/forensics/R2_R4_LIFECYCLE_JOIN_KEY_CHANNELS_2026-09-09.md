# AEGIS / AiByz — R2/R4 Lifecycle Join: Key Active State Channels

**Date:** 2026-09-09  
**Target:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652` / Update `#180059`  
**Status:** OPEN — static lifecycle join complete for the four key channels; runtime qualification remains required.

## 1. Purpose

This pass advances R2/R4 from mutation-site discovery to a concrete lifecycle ledger for the first active control cluster. It uses the corrected structural mutation parser and the existing canonical inventories. It does not create a replacement symbol inventory.

The four channels are:

- `sn-cavalry-threat`
- `retreat-now-goal`
- `attack-status-goal`
- `restart-attack-goal`

The historical-only `cavarchers` and `temporary-goal2` channels remain excluded from active-stock ownership conclusions.

## 2. Machine evidence boundary

The exact installed four-file closure was re-read from the target machine. The structural rule-scope parser reproduced:

- 14,000 recognized mutation rows across the complete 37-file HD/Promisory corpus;
- 6,182 enclosing rules;
- 0 missing rule joins;
- 0 empty condition scopes;
- 4,202 recognized mutations in the four-file active closure.

For the four key channels, the structural join returned:

| Channel | Declaration | Active mutation rows | Reader occurrences | Static status |
|---|---:|---:|---:|---|
| `sn-cavalry-threat` | line 24 | 9 | 93 | active SN control channel |
| `retreat-now-goal` | line 52 | 13 | 9 | active GOAL control channel |
| `attack-status-goal` | line 56 | 19 | 2 | active GOAL control channel |
| `restart-attack-goal` | line 59 | 3 | 2 | active GOAL control channel |

Reader counts are lexical counts after excluding declaration and recognized mutation heads; they are not semantic consumer counts.

## 3. `sn-cavalry-threat` — lifecycle

Declaration:

`AI (HD version).per:24` → `(defconst sn-cavalry-threat 65)`.

Static mutation sequence:

- `5167` → `0`, unconditional `(true)` rule beginning at `5161`.
- `6927` → `1`, cavalry-line threshold family.
- `6939` → `2`, higher cavalry-line threshold family.
- `6951` → `3`, higher cavalry-line threshold family.
- `6963` → `4`, highest threshold family.
- `7006` → `1`, time/stable/cavalry contextual rule.
- `7016` → `2`, stronger cavalry/time/stable contextual rule.
- `7031` → `1`, early flush-specific contextual rule.
- `7045` → `1`, early Castle-Age/civilization contextual rule.

The threshold family reads enemy cavalry-line counts for magyar-huszar, boyar, knight, scout-cavalry, tarkan, war-elephant, camel, and cataphract lines. The four thresholds are strictly stepped by increasing composition requirements.

The later writers are not simple threshold duplicates: they add time windows, stable presence, strategy, military population, age, and civilization constraints.

### R2 interpretation

The evidence supports a **distributed stock strategic-control channel** rather than a single-producer variable. Multiple rules write the channel, while many downstream rules read it. The safest owner candidate is the stock strategic-control policy network in `AI (HD version).per`, not any individual writer rule.

This is a static ownership candidate only. It does not prove scheduler priority, overwrite ordering, or whether the unconditional reset executes once, repeatedly, or under another engine rule-scheduling regime.

### R4 interpretation

The declaration supplies the numeric channel identity. The `(true)` rule is a runtime mutation site with reset-like semantics, but its execution frequency is unresolved. Therefore the initializer classification remains `RUNTIME_REQUIRED`, not `UNCONDITIONAL_RUNTIME_INIT_PROVEN`.

The threshold and contextual writers are subsequent mutations until runtime evidence establishes an earlier/later lifecycle boundary.

## 4. `retreat-now-goal` — lifecycle

Declaration:

`AI (HD version).per:52` → `(defconst retreat-now-goal 20)`.

The source comment explicitly documents three policy values: `1=always`, `2=when attacking`, `3=attack conditions false`. This is source evidence about the programmer's intended value encoding, not an independent engine ABI proof.

Active writers:

- `32591` → `1`
- `32611` → `1`
- `32633` → `1`
- `32653` → `1`
- `32678` → `1`
- `32697` → `1`
- `32718` → `1`
- `33154` → `2`
- `34033` → `0`
- `34053` → `0`
- `34075` → `0`
- `34093` → `0`
- `34104` → `0`

The seven early escalation rules cover combinations of attack coordination, age, tower/TC/castle-arrow threats, siege availability, military level, population, and monk threat. The `33154` writer produces the distinct `2` state under Feudal/flush conditions. The five later zero writers form the recovery/reset region and are guarded by water-body, victory-time, town-size, attack-group, and retreat-timer conditions.

### R2 interpretation

The channel behaves as a **retreat-policy state machine** with distributed triggers and distributed clearing. No single writer is the semantic owner. The owner candidate is the attack/retreat control policy region, subject to runtime confirmation.

### R4 interpretation

`0` is demonstrably written by multiple active rules, so it cannot be labeled a one-time initializer from source inspection. The lifecycle is therefore:

`declared → policy asserted (1/2) → recovery/reset candidates (0) → possible reassertion`.

Whether this forms a recurring state machine in live execution requires runtime observation.
## 5. `attack-status-goal` — lifecycle

Declaration:

`AI (HD version).per:56` → `(defconst attack-status-goal 24)`.

Active writers encode four observed state families:

- `retreat`
- `tsa`
- `groups`
- `0`

The retreat writers at `32592`, `32612`, `32634`, `32654`, `32698` are paired with the corresponding `retreat-now-goal` escalation rules. This establishes a direct static coupling between retreat-policy assertion and attack-status transition.

The later control region contains:

- `33881`, `33957` → `tsa`
- `34054`, `34076` → `retreat`
- `34166`, `34180`, `34204` → `groups`
- `34214`, `34227` → `tsa`
- `34240`, `34261`, `34273`, `34285`, `34296` → `0`

The conditions span victory-time, wonder/relic state, maximum town size, retreat state, attack-goal state, target-player state, attack timers, attack-group counts, military level, and population thresholds.

### R2 interpretation

`attack-status-goal` is not merely a Boolean retreat flag. Static source evidence shows a **multi-state attack-control channel** whose values select distinct attack-management modes. Its semantic owner candidate is the stock attack-control policy network.

### R4 interpretation

The `0` writes are distributed over several independently guarded rules. They therefore represent reset/re-entry candidates, not a single initializer. The lifecycle boundary between `retreat`, `tsa`, `groups`, and `0` remains runtime-sensitive.

### Anomaly requiring separate qualification

Rule `AI (HD version).per:34189` contains the condition `(up-compare-goal attack-goal >= 29876)`. This literal is unusually large relative to the nearby attack-goal state values and must be preserved exactly as source evidence. It must **not** be normalized, corrected, or interpreted as a typo without independent compiler/engine evidence.

This anomaly is now a qualification item rather than silently treated as impossible.

## 6. `restart-attack-goal` — lifecycle

Declaration:

`AI (HD version).per:59` → `(defconst restart-attack-goal 27)`.

Active mutations:

- `35153` → `1` when `increase-town-size-goal == 2` and `sn-maximum-town-size >= 40`, with the water-body condition also present.
- `35165` → `0` when the restart flag is set and ally-proximity, attack-group count, minimum attack-group size, and maximum town size satisfy the reset condition.
- `35171` → `0` when the restart flag is set and ally-proximity is below the required threshold.

The source comment states that this channel restarts an attack in team games when TSA was reduced to place a building. The comment is programmer-intent evidence; the conditions provide the direct control-flow evidence.

### R2 interpretation

This is a compact **one-shot/re-entry request channel** with one assertion site and two clearing sites. It is materially different from `attack-status-goal`: it records a restart request rather than the current attack mode.

### R4 interpretation

The static lifecycle is:

`0 → 1 (restart request) → 0 (clear on qualifying postcondition)`.

Whether a rule can reassert `1` before or after clearing, and whether the value persists across rule cycles, requires runtime qualification.

## 7. Cross-channel control topology

The four channels form a coherent static control cluster:

`enemy composition / world conditions`
`→ sn-cavalry-threat`
`→ production/research/military readers

and separately:

`attack conditions / threat conditions`
`→ retreat-now-goal`
`→ attack-status-goal`
`→ retreat / TSA / groups behavior
`→ restart-attack-goal`
`→ attack re-entry after town-size/TSA disruption

The important architectural point is that these are **state channels**, not isolated constants. The same state is written in one rule family and consumed elsewhere, creating delayed and cross-subsystem effects.

## 8. Ownership and lifetime matrix

| Channel | Owner candidate | Writer topology | Reset topology | Lifetime status | Disposition |
|---|---|---|---|---|---|
| `sn-cavalry-threat` | stock strategic-control policy network | 9 writers, threshold + contextual | unconditional zero writer plus contextual overwrites | runtime frequency/order open | RUNTIME_REQUIRED |
| `retreat-now-goal` | stock attack/retreat control | 13 writers, assertion + clearing | 5 active zero writers | recurring state-machine behavior probable, execution unproven | RUNTIME_REQUIRED |
| `attack-status-goal` | stock attack-control policy | 19 writers, four state families | 5 active zero writers | recurring multi-state controller probable, execution unproven | RUNTIME_REQUIRED |
| `restart-attack-goal` | stock attack re-entry controller | 1 assertion + 2 clear writers | 2 clear paths | request lifecycle statically bounded, runtime persistence open | RUNTIME_REQUIRED |

No row is classified `AEGIS_AUTHORITATIVE`. These are stock engine-script channels and are being characterized as evidence, not adopted as AEGIS state.

## 9. Evidence grades

`sn-cavalry-threat`: **DIRECT + COMPOSED / PROBABLE** for channel role; **UNCERTAIN** for runtime ordering/frequency.

`retreat-now-goal`: **DIRECT + COMPOSED / PROBABLE** for multi-rule retreat state; **UNCERTAIN** for runtime lifetime.

`attack-status-goal`: **DIRECT + COMPOSED / PROBABLE** for multi-state attack control; **UNCERTAIN** for runtime ordering/lifetime.

`restart-attack-goal`: **DIRECT + COMPOSED / PROBABLE** for restart-request semantics; **UNCERTAIN** for runtime persistence and re-entry timing.
## 10. Runtime qualification queue

The static join now identifies what must be measured rather than assumed.

### Probe A — `sn-cavalry-threat`

Observe a controlled enemy-cavalry transition and establish:

1. initial observed value;
2. first threshold crossing;
3. subsequent values 1→2→3→4;
4. whether values decrease without an explicit zero writer;
5. reset timing relative to the `(true)` rule;
6. downstream production/research consequences;
7. whether competing writers overwrite within one evaluation interval.

### Probe B — attack retreat cluster

Observe controlled transitions among `retreat-now-goal 0/1/2`, `attack-status-goal 0/retreat/tsa/groups`, and `restart-attack-goal 0/1`.

The probe must distinguish command issuance from state realization and preserve unknown transitions.
### Probe C — anomalous literals

The `attack-goal >= 29876` condition and other unusually large literals must be preserved exactly and separately checked against compiler/validator behavior. Do not rewrite them because they look implausible.

## 11. Gate status after this pass

- R2 mutable-state ownership: **OPEN**, materially advanced.
- R4 lifecycle/reset classification: **OPEN**, materially advanced.
- Structural mutation → rule-scope join: **COMPLETE** for recognized mutation classes.
- Key-channel declaration/mutation/reader join: **COMPLETE statically**.
- Runtime lifecycle: **NOT QUALIFIED**.
- R3 numeric allocation: **BLOCKED**.
- First production `.per`: **BLOCKED until ABI/runtime gates close**.

## 12. Non-negotiable boundaries

1. Source text is not runtime proof.
2. A `(true)` condition is not proof of one-time execution.
3. Multiple writers do not automatically imply multiple owners.
4. A reader does not become an owner.
5. Historical Promisory presence does not imply active retail load.
6. Numeric similarity does not establish semantic identity.
7. No AEGIS channel is cleared for reuse from this pass.
8. No source anomaly is silently corrected.

## 13. Next exact operation

`KEY-CHANNEL STATIC JOIN`
`→ RUNTIME-SENSITIVE CELL EXTRACTION`
`→ CONTROLLED ABI PROBE DESIGN`
`→ CAVALRY THREAT CONTAINMENT QUALIFICATION`
`→ ABI FREEZE`
`→ ONLY THEN production `.per` implementation.

## 14. Source artifacts

Primary machine artifact:
`R2_R4_JOIN_WORK/semantic_mutation_rule_scope.jsonl`

Reproducible structural parser:
`docs/forensics/tools/r2_r4_rule_scope_join.py`

Canonical raw inventories remain authoritative; this document is a reconciliation/interpretation layer and must not replace them.
