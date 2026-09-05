# AEGIS Layer 3 — Pass 94 Deterministic ABI Audit Harness Specification

Date: 2026-09-05  
Status: **PRE-IMPLEMENTATION / ACQUISITION + AUDIT HARNESS**  
Scope: `.per` namespace acquisition, normalization, collision audit, and ABI freeze. XS excluded.

## 1. Purpose

Pass 93 established the authoritative-input requirement but left an operational question: exactly how should the acquired AI package be converted into a reproducible namespace inventory without allowing parser convenience, filename order, or heuristic assumptions to silently become ABI decisions?

Pass 94 closes that operational gap.

The result is a deterministic, evidence-preserving audit pipeline:

`TARGET PACKAGE → IMMUTABLE SNAPSHOT → FILE MANIFEST → SYMBOL EXTRACTION → REFERENCE EXTRACTION → CHANNEL NORMALIZATION → COLLISION JOIN → WRITER/READER MATRIX → BUILD/VALIDATOR JOIN → ABI DECISION`

This pass does **not** allocate numeric identifiers and does **not** generate `.per` implementation code.

## 2. Non-negotiable invariants

1. The raw target package is never modified by the inventory process.
2. Every extracted fact retains source path, line/range, and source hash.
3. Parser failure is represented as an explicit uncertainty state; it is never silently treated as absence.
4. Numeric equality across channels never constitutes identity.
5. A symbol found only in references is not automatically a definition.
6. A definition found only in an inactive/unused file is not automatically imported runtime state.
7. A validator acceptance result never establishes engine semantics.
8. Engine documentation never establishes validator acceptance.
9. A5 inference can nominate a candidate but can never produce `CLEAR`.
10. Allocation output is generated only from an immutable inventory snapshot.
11. Every implementation-cleared allocation is reproducible from the recorded inputs.
12. No `.per` source is changed by this pass.

## 3. Acquisition boundary

### 3.1 Accepted evidence classes

The harness accepts exactly one primary snapshot class per run:

- `A1`: exact installed target package/build;
- `A2`: exact package snapshot with recorded provenance, hashes, and build identity;
- `A3`: byte/content-equivalent repository snapshot with equivalence evidence.

A4/A5 material may be attached as supporting evidence but cannot clear allocation.

### 3.2 Snapshot manifest

Before parsing, create a manifest containing:

`run_id | acquisition_time_utc | evidence_class | build_id | executable_version | ai_root | validator_version | validator_profile`

Then enumerate every relevant file:

`relative_path | byte_size | sha256 | file_type | parse_status`

The manifest itself receives a SHA-256 hash after serialization.

### 3.3 Immutability rule

The parser reads the snapshot. It does not normalize files in place, rewrite line endings, resolve includes by copying files, or otherwise mutate the evidence source.

If preprocessing is necessary, the derived artifact receives its own path, hash, transformation description, and parent hash.

## 4. Source extraction model

The extractor performs independent passes rather than one overloaded parser.

### Pass A — declarations

Extract:

- `defconst` declarations;
- symbolic aliases;
- goal-like declarations;
- strategic-number declarations;
- flags;
- timers;
- searches;
- imported/include relationships.

### Pass B — state writes

Extract every recognized state mutation, including:

- `set-goal`;
- `up-modify-goal`;
- strategic-number writes;
- flag setters/clearers;
- timer enable/disable/restart;
- search state mutation where statically identifiable.

### Pass C — state reads

Extract:

- direct state reads;
- goal comparisons;
- strategic-number comparisons;
- flag tests;
- timer tests/consumers;
- target/focus references;
- state used as command arguments.

### Pass D — control topology

Extract:

- rule names/locations;
- rule ordering;
- includes/import order;
- guards surrounding state mutation;
- mutually exclusive guards where mechanically evident;
- producer/consumer relationships.

The harness must preserve the distinction between syntactic evidence and semantic interpretation.

## 5. Normalized record schema

Every extracted symbol is normalized to:

`symbol | channel | numeric_id | source_file | source_line | source_hash | declaration_kind | reference_count | semantic_role | authority_class | owner | readers | writers | clearer | lifetime | sentinel | build_min | build_max_tested | engine_status | validator_status | aegis_status | evidence_grade | provenance_status | collision_status`

Unknown values are represented explicitly as `UNKNOWN`, not omitted.

### 5.1 Evidence grades

- `E0`: directly observed in authoritative source/snapshot;
- `E1`: strong deterministic derivation from E0 records;
- `E2`: AEGIS architectural generalization;
- `E3`: hypothesis/open question.

The harness never upgrades E2/E3 to E0 merely because a value is convenient.

## 6. Import closure

A declaration is runtime-relevant only when the package's actual import/include closure establishes that the declaration is reachable from the selected AI entrypoint.

The harness therefore emits two distinct statuses:

- `DECLARED`: symbol exists in the snapshot;
- `IMPORTED`: symbol is reachable from the target entrypoint through recorded inclusion/import relationships.

This prevents a stale backup file, archived module, or unrelated AI package from poisoning the ABI inventory.

If include semantics cannot be resolved with confidence, the symbol remains `IMPORT_STATUS=UNKNOWN` and cannot be used for a `CLEAR` allocation.

## 7. Channel normalization

The canonical channel set is:

- `GOAL`
- `STRATEGIC_NUMBER`
- `FLAG`
- `TIMER`
- `SEARCH`
- `ENGINE_STATE`
- `UNKNOWN`

The numeric identifier is always interpreted together with channel.

Canonical key:

`CHANNEL + NUMERIC_ID`

Therefore:

`GOAL:123 != STRATEGIC_NUMBER:123 != TIMER:123 != FLAG:123`

No cross-channel collision is recorded as an ABI collision unless the target engine explicitly couples the channels.

## 8. Numeric-domain audit

For each channel the harness creates an occupancy map:

`numeric_id → [all occupants]`

The audit then evaluates:

1. legacy occupancy;
2. engine-reserved occupancy;
3. project occupancy;
4. scratch/temporary occupancy;
5. validator constraints;
6. build maximum/minimum;
7. alias relationships;
8. duplicate writers;
9. sentinel conflicts;
10. representation feasibility.

A candidate receives `CLEAR` only if every applicable predicate succeeds.

## 9. Candidate allocation algorithm

The harness does **not** select the first unused integer.

For each symbolic AEGIS field:

```text
candidate_set = legal identifiers for the intended channel
remove engine-reserved identifiers
remove imported legacy identities unless explicit REUSE-LEGACY
remove project identities already owned by another field
remove scratch/temporary identities
remove validator-illegal identifiers
remove build-illegal identifiers
remove identifiers with unresolved ownership/writer conflicts
remove identifiers with sentinel ambiguity

if candidate_set is empty:
    status = UNRESOLVED
else:
    rank candidates deterministically
    emit ranked candidates
    require explicit allocation policy to choose one
```

The ranking function is informational only until the project declares its allocation policy.

The harness must never convert “lowest unused number” into an implicit project rule.

## 10. Legacy adapter decision

For each legacy symbol that overlaps the desired AEGIS concept, classify exactly one:

- `REUSE-LEGACY` — same semantics and identity intentionally preserved;
- `NEW-ALLOC` — separate AEGIS state intentionally created;
- `ADAPTER-MAP` — explicit translation between legacy and AEGIS state;
- `REJECT` — reuse is unsafe, ambiguous, or semantically incompatible.

Every `ADAPTER-MAP` requires source identity, destination identity, direction, conversion rule, lifetime, and invalidation behavior.

No silent aliasing is permitted.

## 11. Writer/reader analysis

For each state field the harness emits:

`FIELD → DEFINER → WRITERS → READERS → CLEARER → LIFETIME → INVALIDATION → GENERATION_SOURCE`

Writer classification:

- `SINGLE_CONSEQUENTIAL_WRITER`
- `MULTIPLE_STRUCTURALLY_EXCLUSIVE_WRITERS`
- `MULTIPLE_UNRESOLVED_WRITERS`
- `UNKNOWN`

Only the first two classes may proceed toward `CLEAR`.

Textual rule order is recorded as topology evidence, not automatically interpreted as ownership.

## 12. Generation audit

The harness validates the generation contract independently of numeric allocation.

Required fields:

`zero_state | increment_primitive | max_value | wrap_rule | equality_rule | init_rule | reset_rule | stale_action_rule`

The first slice should prefer equality matching:

`EXPECTED_GEN == COMMIT_GEN`

unless the target build and validator establish a safer alternative.

A generation field without a defined stale-operation rule is `ARCHITECTURALLY_INCOMPLETE` even if its numeric storage is collision-free.

## 13. Publication audit

The first-slice record protocol is represented as an ordered transition:

`INVALID → PAYLOAD_WRITTEN → METADATA_WRITTEN → VALID`

The audit must verify that the target primitives can express each transition.

The harness must flag any implementation plan that assumes hardware-style atomicity or transaction semantics not established by evidence.

A `VALID` flag with no documented invalidation path is a failure.

## 14. Validator separation

The harness stores validator findings as independent evidence:

`VALIDATOR_VERSION | PROFILE | FILE | LINE | SYMBOL | RULE | RESULT | MESSAGE`

A validator pass can establish only:

`VALIDATOR_STATUS=PASS`

It cannot establish:

`ENGINE_STATUS=YES`

Likewise, engine documentation or observed runtime behavior cannot silently establish validator acceptance.

## 15. Build compatibility

Every allocation receives a build scope:

`BUILD_ID | MIN_TESTED | MAX_TESTED | BUILD_DEPENDENT`

If a goal/SN limit, primitive signature, or parser behavior changes between builds, the allocation is partitioned by build profile rather than generalized across versions.

“Current” is not a valid build identifier.

## 16. Required machine-readable outputs

A complete run produces these artifacts:

1. `snapshot_manifest.json`
2. `symbol_inventory.jsonl`
3. `reference_inventory.jsonl`
4. `import_closure.json`
5. `channel_occupancy.json`
6. `writer_reader_matrix.jsonl`
7. `validator_findings.jsonl`
8. `build_profile.json`
9. `abi_candidates.jsonl`
10. `abi_decisions.jsonl`
11. `audit_report.md`
12. `RUN_MANIFEST.sha256`

The JSONL records are append-only for the run. The final decision file is derived from the earlier records and must contain their hashes.

## 17. Reproducibility requirements

A second execution over the same immutable snapshot, parser version, configuration, and validator profile must produce byte-equivalent normalized outputs except for explicitly documented nondeterministic metadata such as wall-clock execution time.

Sorting requirements:

- file paths: lexical normalized order;
- symbols: channel, numeric ID, symbol;
- references: source path, line, column, referenced symbol;
- findings: severity, file, line, rule.

No filesystem enumeration order may influence an ABI decision.

## 18. Failure states

The harness distinguishes:

- `ABSENT` — positively established absent;
- `UNPARSED` — parser could not inspect source;
- `AMBIGUOUS` — multiple interpretations remain;
- `UNRESOLVED` — required evidence unavailable;
- `CONFLICT` — independent evidence disagrees;
- `CLEAR` — all applicable gates passed.

Only `CLEAR` is implementation-eligible.

This distinction is critical: `UNPARSED` is never equivalent to `ABSENT`.

## 19. First-slice join target

The frozen symbolic Cavalry fields are joined against the inventory exactly as named in Pass 92/93:

`OBS.ENEMY_CAVALRY`
`OBS.ENEMY_CAVALRY_AGE`
`THREAT.CAVALRY_ACTIVE`
`CAP.CAMEL_CURRENT`
`CAP.CAMEL_REQUIRED`
`CAP.CAMEL_DEFICIT`
`CAND.PRODUCER`
`CAND.STATUS`
`COMMIT.VALID`
`COMMIT.OWNER`
`COMMIT.GEN`
`COMMIT.STAGE`
`EXEC.STAGE`
`EXEC.EXPECTED_GEN`
`RES.RESERVED`
`RES.DISCRETIONARY`
`ARB.EPOCH`
`ARB.DIRTY`
`VERIFY.LEVEL`

The join may reveal that one or more fields should use a different native channel than the provisional symbolic table assumed. Such a change is permitted only with an explicit ABI decision record and architectural rationale.

## 20. Exit criteria for numeric ABI clearance

The numeric ABI gate opens only when all of the following are true:

- A1/A2/A3 source snapshot identified;
- build identity recorded;
- snapshot manifest hashed;
- import closure resolved;
- declaration and reference extraction complete;
- channel occupancy complete;
- legacy overlap classified;
- engine-reserved identifiers accounted for;
- validator restrictions recorded;
- writer/reader matrix complete;
- generation semantics represented;
- publication/invalidation represented;
- all 19 first-slice fields have a candidate;
- every selected candidate is `CLEAR`;
- engine/validator/AEGIS statuses are independently positive;
- output hashes are internally consistent;
- the final allocation table is committed as the sole numeric ABI source of truth.

## 21. Current result

Pass 94 materially advances the project despite the unavailable workstation because it removes the remaining procedural ambiguity between “obtain the package” and “safely freeze the numeric ABI.”

The remaining blocker is now strictly evidentiary/infrastructural:

> **The target package/build must be acquired or an A2/A3-equivalent snapshot must be established.**

No further abstract state architecture is required before that event.

## 22. Hostile QC

### Rejected shortcuts

- Choosing a high unused goal number by inspection.
- Assuming goals and SNs share a namespace.
- Treating a missing declaration as proof of absence when parsing was incomplete.
- Treating an archived module as imported runtime state.
- Treating validator acceptance as semantic proof.
- Treating engine documentation as validator proof.
- Treating multiple writers as safe because they appear late/early in source order.
- Treating `VALID=1` as a transactional guarantee.
- Treating generation ordering as valid without proven comparison semantics.
- Treating a parser's first candidate as the project allocation policy.

### New safety property

The audit process itself is now deterministic, evidence-preserving, and replayable. That means the eventual numeric ABI can be reviewed as an auditable derivation rather than as a collection of hand-picked constants.

## 23. Verdict

**PASS — acquisition/audit procedure closed.**

**NUMERIC ABI: BLOCKED ONLY BY SOURCE/BUILD AVAILABILITY.**

**ARCHITECTURAL DESIGN: SUFFICIENT FOR FIRST-SLICE ALLOCATION.**

**`.per` IMPLEMENTATION: CORRECTLY BLOCKED UNTIL `CLEAR` ALLOCATIONS EXIST.**
