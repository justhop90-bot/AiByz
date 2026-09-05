# AEGIS Layer 3 — Pass 93 Authoritative ABI Inventory Specification

Date: 2026-09-05
Status: **PRE-IMPLEMENTATION / INVENTORY GATE**
Scope: `.per` architecture and ABI evidence. XS excluded.

## 1. Objective

Pass 92 froze the symbolic Cavalry Threat Containment ABI but correctly refused to invent numeric identifiers. Pass 93 converts that remaining blocker into a concrete acquisition and audit specification.

The required artifact is an authoritative namespace inventory from the exact target AI package/build, followed by a deterministic join against the frozen symbolic ABI.

No implementation constant is valid merely because a number appears unused in a partial source file.

## 2. Authority hierarchy

Numeric ABI evidence is ranked:

1. **A1 — exact installed target package/build**, extracted directly from the authorized workstation;
2. **A2 — exact package snapshot whose provenance, hashes, and build identity are recorded**;
3. **A3 — repository snapshot known to be byte/content equivalent to the target package**;
4. **A4 — historical/source documentation or community material**;
5. **A5 — inference**.

Only A1–A3 may establish a numeric allocation as implementation-cleared. A4/A5 can identify candidates but cannot establish `CLEAR` status.

## 3. Required source inventory

The acquisition pass must enumerate, at minimum:

### Goal domain

- every imported `defconst` whose value is used as a goal;
- every goal explicitly initialized;
- every goal written by `set-goal`, `up-modify-goal`, or equivalent state mutation;
- every temporary/scratch goal;
- every legacy AEGIS/PORPHYRA goal actually imported;
- every project-owned goal;
- build-reserved goal ranges/symbols if documented.

### Strategic-number domain

- every strategic-number constant;
- every SN read;
- every SN write;
- every engine-reserved SN;
- target-build maximum and any documented special ranges.

### Flag domain

- every flag definition/reference;
- initial state;
- writers and clearers;
- semantic aliases;
- imported legacy flags.

### Timer domain

- every timer ID;
- enable/disable consumers;
- owner;
- generation association;
- initial state.

### Search/state domain

- every search definition;
- search state variables;
- nested/stacked search assumptions;
- target/focus state channels.

## 4. Deterministic inventory record

Every discovered state symbol must be normalized to:

`symbol | channel | numeric_id | source_file | source_line | source_hash | semantic_role | authority_class | owner | readers | writers | clearer | lifetime | sentinel | build_min | build_max_tested | validator_status | evidence_grade | collision_status`

`source_line` may be a range when the definition is multi-line.

`source_hash` must identify the source artifact used for the assignment, not merely the repository commit.

## 5. Collision algorithm

For each proposed AEGIS field:

1. resolve its symbolic name;
2. resolve its intended channel;
3. enumerate all numeric occupants in that channel;
4. compare against imported legacy state;
5. compare against engine-reserved identifiers;
6. compare against validator restrictions;
7. compare against build-specific limits;
8. compare against scratch/temporary state;
9. verify owner/writer uniqueness;
10. verify sentinel does not collide with legal data;
11. record the result.

The collision decision is:

`CLEAR` only if every applicable comparison is clean.

Otherwise the field remains `COLLIDES_LEGACY`, `COLLIDES_ENGINE`, `COLLIDES_VALIDATOR`, `BUILD_DEPENDENT`, or `UNRESOLVED`.

## 6. Cross-channel non-equivalence

The inventory must never merge identifiers merely because the same integer is available in multiple channels.

Examples:

- goal `123` is not SN `123`;
- flag identity is not goal identity;
- timer `7` is not goal `7`;
- search state is not automatically persistent memory.

Channel identity is part of the ABI key.

## 7. Legacy preservation rule

A legacy state symbol keeps its identity when imported unless an explicit adapter intentionally remaps it.

The audit must therefore distinguish:

`REUSE-LEGACY` — intentionally preserved;

`NEW-ALLOC` — newly allocated project state;

`ADAPTER-MAP` — deliberate translation from legacy to AEGIS state;

`REJECT` — unsafe or ambiguous reuse.

No silent remapping is permitted.

## 8. Minimum Cavalry allocation demand

The inventory must find safe concrete storage for these symbolic fields and no more:

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

This is **16 goal-like fields + 3 flags**, with the caveat that the final representation may change if the inventory reveals a safer native-compatible representation. The symbolic contract, not the assumed channel, is authoritative.

## 9. Generation encoding requirement

Before allocation, define:

- generation zero state;
- increment primitive;
- maximum value;
- wraparound behavior;
- equality comparison representation;
- initialization;
- reset/invalidation;
- stale-operation handling.

The safest first-slice implementation is equality-based generation matching rather than ordering comparisons, unless the target validator/engine proves a better primitive.

## 10. Publication encoding requirement

The record protocol must remain:

`VALID=0 → populate → generation → owner → stage → metadata → VALID=1`

A reader must reject records that are invalid or whose expected owner/generation does not match.

The audit must verify that the chosen primitives can actually express these operations in the target build and validator profile.

## 11. Writer matrix requirement

For every allocated field produce:

`FIELD → OWNER → WRITERS → READERS → CLEARER → LIFETIME → INVALIDATION → GENERATION SOURCE`

A field with multiple consequential writers is not `CLEAR` until those writers are shown to be structurally exclusive or governed by an explicit arbitration contract.

## 12. Validator/source-of-truth requirement

Validator acceptance is not evidence of engine semantics. Engine documentation is not evidence that the project's validator accepts a representation.

The final inventory must therefore carry independent:

- `ENGINE_STATUS`;
- `VALIDATOR_STATUS`;
- `AEGIS_STATUS`.

A state allocation is implementation-cleared only when all three are compatible.

## 13. Build identity

The inventory must record:

`build_id | executable/version evidence | AI package path | package hash manifest | validator version/profile | inventory timestamp`

The project must not label the resulting ABI “current-build compatible” without this evidence.

The latest publicly identified major official update is 177723 (June 2, 2026), but public release identity is not a substitute for the exact installed build on the target workstation. citeturn0search5

## 14. Acquisition status

The authorized workstation is currently reachable by ping but unavailable at the filesystem/process layer. Therefore the authoritative A1 inventory cannot yet be generated from the installed package.

This is an infrastructure blocker, not an architecture ambiguity.

If the exact target AI package or a verified snapshot is supplied, it can immediately become A1/A2 evidence once its build identity and hashes are recorded.

## 15. Pass-93 verdict

**PASS — inventory specification complete.**

**NUMERIC ABI: STILL BLOCKED.**

**CODE GENERATION: STILL BLOCKED.**

The next useful action is now sharply defined: obtain the authoritative source inventory, execute the collision algorithm, assign concrete IDs, and freeze the resulting numeric ABI as the sole implementation allocation source.

No further abstract state design is required before that evidence arrives.
