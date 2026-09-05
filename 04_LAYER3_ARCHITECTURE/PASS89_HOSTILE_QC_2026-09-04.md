# PASS 89 HOSTILE QC — TYPED AEGIS STATE / `.PER` REALIZATION ARCHITECTURE

**Layer:** 3 — architecture QC  
**Subject:** `PASS89_TYPED_AEGIS_STATE_PER_REALIZATION_2026-09-04.md`  
**Subject commit:** `afee726a5e9ee53ffb581f8c828b28a5ad95066b`  
**QC status:** CONDITIONAL PASS — architecture is valuable and directionally sound, but several claims and implementation contracts must be tightened before the state ABI can become a coding authority.  
**Canonical branch:** `aegis/layer2-hd-methodology-coding-2026-09-04`  
**QC method:** repository inspection, predecessor comparison, official-engine cross-check, adversarial state-machine review, storage-model review, stale-state analysis, implementation-feasibility review, and workstation connectivity check.

---

## 0. Executive verdict

Pass 89 is a strong architectural document. It successfully moves the project from abstract cognitive objects toward a realizable scalar-state architecture without using XS. The central idea — a conceptual type system realized through explicit field schemas over goals, flags, SNs, timers, searches, and engine-owned observations — is sound as an AEGIS design direction.

However, hostile review identifies a critical distinction:

> **Pass 89 defines a state-schema philosophy more completely than it defines a safe `.per` ABI.**

The document is therefore **not yet safe to treat as the final implementation contract**.

The highest-risk defects are:

1. the proposed `G0–G511` compatibility allocation is not demonstrated to be collision-free against the actual project/runtime namespace;
2. “goals are the memory plane / SNs are the control plane” is too absolute and can become false when engine semantics or inherited AI conventions consume those channels;
3. the record-validity protocol does not fully specify how readers are prevented from observing partially populated records under actual rule evaluation semantics;
4. ownership and generation are architecturally specified but not yet given a mechanically enforceable writer protocol;
5. the candidate-selection design is underspecified — procedural candidate evaluation does not by itself produce a comparison/selection mechanism;
6. deficit arithmetic, saturation, overflow, and negative-value policy are deferred despite being foundational to the first vertical slice;
7. evidence-strength codes and execution stages are well separated conceptually but their promotion rules are still insufficiently formalized;
8. the document contains embedded transient tool-citation identifiers (`turn...`) that are unsuitable as durable repository citations;
9. current-build claims are carefully caveated in places, but the compatibility profile still risks being interpreted as a runtime-guaranteed substrate before validation;
10. several “must” statements are architecture policy, while others sound like engine facts; the document needs a sharper normative/evidentiary split.

**Disposition:** retain Pass 89 as an architecture milestone; do not rewrite history. Record corrective requirements here and incorporate them into Pass 90+ registries.

---

# 1. QC scorecard

| Area | Verdict | Severity | Action |
|---|---|---:|---|
| Cognitive/runtime separation | PASS | — | Preserve |
| No-XS boundary | PASS | — | Preserve |
| Evidence discipline | PASS with documentation defect | M | Replace transient citations with durable source records |
| State ABI concept | PASS | — | Preserve |
| Goal allocation | FAIL AS IMPLEMENTATION CONTRACT | C | Replace proposed numeric map with collision-audited allocation |
| SN policy | NEEDS CORRECTION | H | Relax absolute memory/control dichotomy |
| Flag policy | NEEDS SPECIFICATION | H | Establish actual flag semantics and namespace |
| Timer model | PASS CONCEPTUALLY | M | Add timer-to-generation protocol |
| Search identity | PASS | — | Preserve |
| Record atomicity | INCOMPLETE | C | Define write/read protocol formally |
| Generation model | STRONG DESIGN / UNPROVEN RUNTIME | H | Define wrap, comparison, and writer enforcement |
| Ownership model | STRONG DESIGN / UNENFORCED | H | Define actual writer gate |
| Objective model | PASS CONCEPTUALLY | M | Separate semantic fields from storage allocation |
| Capability deficit | INCOMPLETE | C | Define arithmetic/saturation before implementation |
| Candidate model | INCOMPLETE | C | Define best-so-far / comparison protocol |
| Feasibility gate | PASS CONCEPTUALLY | M | Map each predicate to verified primitive |
| Execution stage | PASS | — | Preserve |
| Evidence strength | PASS CONCEPTUALLY | M | Define promotion matrix |
| Recovery | PASS CONCEPTUALLY | M | Define bounded transition table |
| Arbitration | INCOMPLETE | H | Define dirty-bit ownership and consumption semantics |
| Reservation model | DESIGN-VALID | M | Avoid premature quantitative ledger |
| Compatibility profiles | GOOD IDEA / NOT YET OPERATIONAL | H | Make profile selection a validated artifact |
| Vertical slice | GOOD | — | Preserve as implementation target |
| Adversarial matrix | GOOD | M | Convert into executable/static tests |
| Implementation readiness | CONDITIONAL | C | Pass 90 required before coding beyond scaffolding |

---

# 2. Finding C-01 — `G0–G511` is not a proven compatibility allocation

**Severity:** CRITICAL  
**Disposition:** BLOCKS state-ABI allocation.

Pass 89 proposes:

```text
G0–G63       bootstrap / ABI / health
G64–G127     observation summaries
G128–G191    belief / confidence
G192–G255    assessment
G256–G319    objectives
G320–G383    capability requirements
G384–G447    candidate state
G448–G511    commitment / execution core
```

This is useful as a *logical partition sketch*, but it is not yet a safe numeric allocation.

The critical problem is that “goal exists” and “goal is free for AEGIS” are different propositions. The project already has inherited AI conventions and existing custom state, including low-numbered goal identifiers. A compatibility namespace must therefore be collision-audited against the complete loaded script graph, not merely against the engine's maximum.

The official 2024 Update Preview explicitly raised the available goal count from 512 to 16000, while the project also has historical/current scripts using goals for ordinary AI state. The larger engine range therefore solves capacity, not namespace ownership. citeturn3view0

### Required correction

Replace:

```text
L3-COMPAT = G0–G511
```

with:

```text
L3-COMPAT = lowest validated collision-free AEGIS allocation
```

The numeric allocation must be generated from an inventory containing:

```text
stock goals
custom constants
loaded goals
temporary/scratch goals
engine-reserved goals
validator-reserved ranges
AEGIS-owned ranges
```

No `.per` implementation should consume a proposed number merely because it appears in Pass 89.

---

# 3. Finding H-02 — “Goals are memory / SNs are control” is too absolute

**Severity:** HIGH.

The document correctly recognizes that SNs can affect engine behavior and therefore should not casually become a general-purpose database. However, the binary formulation:

```text
Goals = memory plane
SNs = control plane
```

is an architectural heuristic, not a universal runtime truth.

Historical AI scripts use goals for engine-facing strategy/control semantics, and SNs can carry persistent controller state. The correct abstraction is therefore:

```text
PREFERRED AEGIS ROLE
≠
EXCLUSIVE RUNTIME ROLE
```

### Correct rule

Use:

> Goals are the **preferred AEGIS scalar-state plane**, subject to collision and engine-consumer audits. SNs are the **preferred engine-facing control plane**, subject to explicit declarations when used for persistent controller state.

The registry, not the storage class name, determines authority.

---

# 4. Finding H-03 — Flag semantics are under-specified

**Severity:** HIGH.

Pass 89 treats flags as simple Boolean state. The available scripting references indicate that flag operations/comparisons can have engine-specific semantics, including bitwise-style flag tests. That means “flag = Boolean” is an architectural preference, not enough of a runtime contract.

### Required registry additions

The flag registry must specify:

```text
flag identifier
representation
bit/boolean semantics
set operation
clear operation
comparison operation
initial state
writer
reader
reset semantics
build profile
```

Until this exists, flags should not be used as authoritative AEGIS state.

---

# 5. Finding C-04 — Record validity does not yet establish safe multi-field publication

**Severity:** CRITICAL.

The document correctly recognizes that `.per` fields are not automatically atomic. The proposed protocol:

```text
VALID = 0
→ write fields
→ generation
→ VALID = 1
```

is directionally correct, but it needs a stronger contract.

The actual requirement is:

```text
NO CONSUMER MAY TREAT ANY FIELD IN THE RECORD AS AUTHORITATIVE
UNTIL VALID == 1 AND ALL REQUIRED GENERATION/OWNER CHECKS PASS.
```

The writer must also guarantee that `VALID` is the **last publication action**, and every consumer must test it before reading any dependent field.

### Required state protocol

```text
FREE
  ↓
INVALID / RESERVED
  ↓
WRITE STATIC FIELDS
  ↓
WRITE GENERATION
  ↓
WRITE OWNER
  ↓
WRITE DYNAMIC FIELDS
  ↓
PUBLISH VALID
  ↓
ACTIVE
```

For updates:

```text
ACTIVE
  ↓
INVALIDATE OR ENTER UPDATE-GUARDED STATE
  ↓
WRITE NEW FIELDS
  ↓
CHANGE GENERATION
  ↓
PUBLISH VALID
```

The exact order must be validated under the real rule-evaluation model before being called atomic.

The architecture should avoid the word **atomic** unless a runtime test proves atomicity. The safer phrase is **publication protocol**.

---

# 6. Finding H-05 — Generation protection is not yet mechanically enforceable

**Severity:** HIGH.

Generation is one of the strongest ideas in Pass 89. The weakness is enforcement.

The document says a stale writer should be rejected when:

```text
writer_generation != current_generation
```

But this is only useful if every delayed writer actually carries and compares its expected generation.

### Required implementation contract

Every delayed operation must have:

```text
expected_generation
```

and every mutation path must guard:

```text
VALID
AND
OWNER_MATCH
AND
GENERATION_MATCH
```

Timer-driven, recovery-driven, search-driven, and queued-command-driven mutations must all use this guard where reuse is possible.

### Additional unresolved issue

Generation wraparound is unspecified.

The registry must define:

```text
minimum generation
maximum generation
wrap policy
zero meaning
comparison policy
```

A wrap that allows an old generation to become numerically equal to a new generation is a stale-state hazard.

For the first implementation, the safest policy may be a bounded monotonically increasing generation with explicit reset/reinitialization semantics, rather than clever modular arithmetic.

---

# 7. Finding H-06 — Ownership exists conceptually but has no runtime enforcement mechanism

**Severity:** HIGH.

Pass 89 defines ownership as “the subsystem currently authorized ... to mutate the authoritative record.” That is a good AEGIS definition.

But authorization cannot remain documentation-only.

If two rules both execute:

```text
set-goal COMMIT-STAGE ...
```

the presence of an `OWNER` field does not itself stop either rule from writing.

### Required correction

Ownership must become a guardable runtime contract:

```text
writer identity
→ expected owner
→ owner guard
→ generation guard
→ validity guard
→ mutation
```

If `.per` cannot directly encode writer identity, use structural ownership:

```text
one authoritative writer rule-family
+
exclusive controller phase
+
explicit handoff state
```

This must be specified before the first multi-controller implementation.

---

# 8. Finding C-07 — Candidate selection is incomplete

**Severity:** CRITICAL.

Pass 89 correctly says:

```text
candidate
→ hard constraints
→ feasibility
→ soft evaluation
→ selection
```

But the proposed first implementation says candidates may be evaluated procedurally:

```text
camel
→ spear
→ static defense
→ reposition
→ select
```

That does not define selection.

If the first feasible candidate immediately wins, the architecture has recreated **first feasible wins**, not candidate evaluation.

If later candidates can replace earlier ones, the runtime needs:

```text
best_candidate
best_evaluation
candidate_rank / policy band
```

or an equivalent deterministic comparison mechanism.

### Required correction

Define one of these explicitly:

**A. Ordered policy selection**

```text
candidate order is the policy
first feasible candidate wins
```

or:

**B. Best-so-far selection**

```text
candidate → evaluate → compare with incumbent → retain winner
```

The second is more expressive but requires additional state.

The architecture must not call both “candidate evaluation” without distinguishing them.

---

# 9. Finding C-08 — Capability deficit arithmetic is not ready for implementation

**Severity:** CRITICAL.

The central equation is:

```text
DEFICIT = REQUIRED − CURRENT
```

but the document explicitly defers saturation/negative-value policy.

That is not safe for a first implementation because deficit state controls whether the AI invests.

Required semantics:

```text
CURRENT > REQUIRED
```

must have a defined result.

Possible policies:

```text
raw deficit may be negative
or
DEFICIT = max(0, REQUIRED - CURRENT)
```

The architecture should choose deliberately.

For the production controller, the second is probably safer:

```text
DEFICIT = MAX(0, REQUIRED - CURRENT)
```

while a separate surplus field can represent over-capability.

### Additional requirement

Define maximum values and arithmetic safety before writing `.per` code.

---

# 10. Finding H-09 — Evidence-strength classes need a promotion matrix

**Severity:** HIGH.

Pass 89 separates:

```text
execution stage
```

from:

```text
evidence strength
```

This is correct and important.

But it then allows examples such as:

```text
CREATED with E3 correlation
```

without specifying whether that is sufficient for promotion.

### Required promotion matrix

The registry must specify, per transition:

| Transition | Minimum evidence |
|---|---|
| INTENTION → AUTHORIZED | controller state |
| AUTHORIZED → ISSUED | command path executed |
| ISSUED → PENDING | accepted queue/pending evidence |
| PENDING → CREATED | validated completion evidence |
| CREATED → AVAILABLE | capability/object availability evidence |
| AVAILABLE → DEPLOYED | deployment evidence |
| DEPLOYED → INTERACTION | interaction evidence |
| INTERACTION → OBJECTIVE_EFFECT | objective evidence |

The exact evidence class may vary by primitive, but the rule must be explicit.

This is especially important because official AoE2DE updates changed queue/pending observability semantics over time. The architecture is right to treat those as distinct states; the registry must now formalize the evidence threshold. citeturn1search1turn1search2

---

# 11. Finding H-10 — Build-profile logic needs an actual profile artifact

**Severity:** HIGH.

The document correctly separates:

```text
L3-COMPAT
L3-DE-CURRENT
```

and cites the official goal expansion and SN expansion.

But “profile” currently means prose.

It needs a machine-readable contract eventually containing:

```text
profile_id
build_min
build_max_tested
goal_min
goal_max
SN_min
SN_max
flag capabilities
timer capabilities
primitive set
validator profile
known incompatibilities
```

The official sources establish that the scripting surface changed over time: strategic numbers reached 511 in Update 42848, while goals reached 16000 in Update 125283. citeturn1search1turn3view0

Therefore build profile is not documentation decoration; it is part of runtime compatibility.

---

# 12. Finding M-11 — Embedded transient web citations are not durable repository evidence

**Severity:** MEDIUM.

The committed Pass 89 contains references such as:

```text
turn0search4
turn0search0
turn1search0
```

Those identifiers belong to a specific tool session. They are not durable repository references.

This is a documentation-integrity defect, not a runtime defect.

### Required correction

Future canonical artifacts should use a durable source record containing at least:

```text
source title
publisher
publication/update identifier
date
canonical URL
relevant claim
accessed date
```

The repository can additionally maintain a source manifest so later QC can re-check the claim without relying on chat-local citation IDs.

---

# 13. Finding M-12 — “current build” language must remain explicitly unverified

**Severity:** MEDIUM.

The document generally handles this correctly, but the phrase:

```text
L3-DE-CURRENT
```

can be read as if the installed build has already been verified.

It has not.

The workstation currently responds to ping but the authorized filesystem is not accessible; a directory probe returned `Not connected`. Therefore no current-build validator or game-runtime proof was available during this QC.

The correct status is:

```text
DE-CURRENT = architecture profile target
installed-build conformance = OPEN
```

This distinction must remain permanent until the workstation can execute the relevant tests.

---

# 14. Finding H-13 — Arbitration dirty-bit can create lost-update and thrash hazards

**Severity:** HIGH.

The proposed:

```text
ARB-DIRTY = 1
```

is attractive as a lightweight event mechanism, but the consumption semantics are incomplete.

Potential race:

```text
Controller A: DIRTY = 1
Arbiter: reads DIRTY
Controller B: DIRTY = 1
Arbiter: clears DIRTY = 0
```

The B event can be lost if there is no epoch/change counter.

Pass 89 already proposes `ARB-EPOCH`; therefore the stronger design should be:

```text
ARB-EPOCH increments on material invalidation
ARB-DIRTY mirrors pending work
consumer records last_consumed_epoch
```

The epoch becomes authoritative; dirty is only an optimization.

This also solves repeated identical dirty writes.

---

# 15. Finding H-14 — Review timers need explicit ownership and generation association

**Severity:** HIGH.

The document correctly identifies the stale-timer hazard:

```text
commitment A starts timer
A releases
B reuses state
T fires
→ B accidentally modified
```

The proposed generation check is correct.

But the timer registry needs to make the association explicit:

```text
TIMER_ID
OWNER_RECORD
OWNER_GENERATION
PURPOSE
CONSUMER
ENABLED_STATE
RESTART_POLICY
```

If a timer cannot carry those fields natively, the consumer must use a shared generation channel.

A timer firing must never itself imply that the original commitment still exists.

---

# 16. Finding M-15 — Search result persistence needs a three-state identity contract

**Severity:** MEDIUM.

The document correctly refuses to equate search results with durable entity identity.

The implementation should formalize:

```text
IDENTITY =
    DURABLE
    PROVISIONAL
    UNKNOWN
```

Only `DURABLE` identities may be retained across long controller intervals without mandatory revalidation.

`PROVISIONAL` requires revalidation immediately before side effect.

`UNKNOWN` should not be stored as an authoritative target identity.

This aligns with the Layer-2 identity archaeology and avoids accidentally converting search/model IDs into world-object identity.

---

# 17. Finding C-16 — Resource reservations need an invariant against negative discretionary resources

**Severity:** CRITICAL.

Pass 89 gives:

```text
actual gold = 200
reserved gold = 150
available discretionary gold = 50
```

but does not define the invariant when reservations exceed actual resources.

The runtime policy must guarantee:

```text
RESERVED_RESOURCE >= 0
DISCRETIONARY_RESOURCE = max(0, ACTUAL - RESERVED)
```

and must define what happens if external engine spending causes:

```text
ACTUAL < RESERVED
```

Possible policy:

```text
reservation becomes underfunded
→ affected commitments become feasibility-invalid
→ arbitration dirty
```

Never allow an internal reservation to masquerade as actual resource availability.

---

# 18. Finding M-17 — Reset ordering is good but needs a side-effect barrier

**Severity:** MEDIUM.

Pass 89 proposes:

```text
1. disable side-effect permissions
2. invalidate record
3. clear transient fields
4. increment generation
5. release reservations
6. disable timers
7. clear derived flags
8. request re-arbitration
```

This is directionally strong.

However, “disable side-effect permissions” must become a concrete guard that command rules actually test.

Otherwise the first step is merely documentation.

Recommended invariant:

```text
NO COMMAND RULE MAY FIRE IF COMMIT.VALID != 1
```

and, where applicable:

```text
NO COMMAND RULE MAY FIRE IF COMMIT.STAGE IS NOT COMMAND-ELIGIBLE
```

---

# 19. Finding M-18 — Execution stage and commitment stage should not be duplicated without authority rules

**Severity:** MEDIUM.

The document uses:

```text
COMMIT-STAGE
EXEC-STAGE
controller_stage
world_stage
```

These concepts are useful, but duplication creates divergence risk.

Recommended model:

```text
COMMIT-STAGE = AEGIS controller lifecycle
WORLD-STAGE = observed engine lifecycle
```

Do not create both `COMMIT-STAGE` and `EXEC-STAGE` if they encode the same semantic domain.

If both remain, the registry must state which is authoritative and which is derived.

---

# 20. Finding M-19 — Objective taxonomy is useful but should be treated as versioned policy

**Severity:** MEDIUM.

The objective enumeration:

```text
SURVIVE
PROTECT
GAIN_CAPABILITY
DENY
ATTACK
TRANSITION
INFORMATION
RECOVER
```

is a good initial ontology.

It must not be treated as immutable.

The registry should version semantic enums because changing integer meanings in a live `.per` state plane can reinterpret persisted state.

Required:

```text
ENUM_VERSION
TYPE_ID
NAME
VALID_FROM
VALID_TO
MIGRATION_POLICY
```

For the first implementation, simpler is preferable: freeze the enum for the vertical slice and avoid runtime migration.

---

# 21. Finding H-20 — Capability measurement must be separated from capability policy

**Severity:** HIGH.

Pass 89 correctly warns that:

```text
CAPABILITY ≠ UNIT TYPE
```

and that weighted capability should not be implemented before constituent measurements are validated.

The architecture should go one step further:

```text
measurement function
```

and:

```text
policy requirement
```

must be separate.

Example:

```text
MEASURE_ANTI_MOUNTED()
→ current capability

REQUIRE_ANTI_MOUNTED()
→ required capability
```

Otherwise the requirement itself can become circular:

```text
we need 8 because our model says 8
```

The first vertical slice should use a transparent requirement rule with explicit provenance.

---

# 22. Finding C-21 — The first vertical slice should not claim objective-level verification from deficit zero alone

**Severity:** CRITICAL.

Pass 89's example advances:

```text
CURRENT = 8
DEFICIT = 0
```

then says the objective is reassessed.

That is acceptable as a trigger for reassessment, but not as proof of objective success.

For example, eight camel units may exist but:

```text
be un-deployed
be trapped
be dead shortly afterward
be insufficient against the actual threat
```

Therefore:

```text
DEFICIT = 0
```

means:

> measured capability requirement is currently satisfied.

It does **not** mean:

> strategic objective has been achieved.

Objective-level success remains V8 and requires its own postcondition.

---

# 23. Finding M-22 — “Every active commitment has an exit path” needs a watchdog definition

**Severity:** MEDIUM.

The invariant is excellent, but implementation needs a measurable definition.

A commitment is considered potentially immortal if:

```text
ACTIVE
AND
no progress evidence
AND
no review
AND
no release
```

for a bounded interval.

The review timer becomes the watchdog.

Required invariant:

```text
ACTIVE commitment
→ review deadline exists
```

except for explicitly declared non-timed states whose lifecycle is itself engine-bounded.

---

# 24. Finding H-23 — The architecture needs an explicit state-transition legality table

**Severity:** HIGH.

The prose state machine is useful but insufficient for coding.

Pass 90 should create a table:

| Current | Event/evidence | Guard | Next | Required writes | Forbidden writes |
|---|---|---|---|---|---|
| FREE | allocation | slot free | PROPOSED | gen, owner | world stage |
| PROPOSED | authorization | objective valid + feasible | AUTHORIZED | stage | completion |
| AUTHORIZED | command | command guard | ISSUED | action | completed |
| ISSUED | queue evidence | matching gen | PENDING | world stage | objective success |
| PENDING | completion | sufficient evidence | CREATED | stage | false battlefield effect |
| ... | ... | ... | ... | ... | ... |

This table should become the authoritative state-machine source for implementation and testing.

---

# 25. Finding H-24 — The ABI needs a distinction between authoritative, derived, and observational fields

**Severity:** HIGH.

Pass 89 has this distinction conceptually, but the field registry does not encode it explicitly.

Add:

```text
authority_class =
    ENGINE_AUTHORITATIVE
    AEGIS_AUTHORITATIVE
    DERIVED_CACHE
    OBSERVATIONAL
```

Then enforce:

```text
DERIVED_CACHE may be deleted/recomputed
ENGINE_AUTHORITATIVE may not be overwritten by AEGIS state
OBSERVATIONAL may not be treated as permanent truth
```

This would materially strengthen the ABI.

---

# 26. Finding H-25 — “Typed” should be renamed “schema-typed” where precision matters

**Severity:** MEDIUM.

The phrase “typed AEGIS state” is useful shorthand, but it risks implying actual language-level type enforcement.

The architecture itself acknowledges that `.per` has no native AEGIS type system.

Recommended precise term:

```text
schema-typed scalar state
```

or:

```text
contract-typed runtime state
```

The title can remain “Typed AEGIS State” for readability, but the glossary should define the term precisely.

---

# 27. Finding M-26 — The compatibility core is too large for the first vertical slice

**Severity:** MEDIUM.

Pass 89 itself says the first implementation should be smaller, which is correct.

The hostile recommendation is stronger:

> Do not allocate the entire conceptual ABI before the first slice proves that the storage model works.

First slice should allocate only the minimum collision-free fields for:

```text
threat observation
objective validity
required capability
current capability
deficit
candidate feasibility
commitment validity
commitment generation
commitment stage
attempt count
failure code
review state
arbitration epoch/dirty
```

Everything else remains unallocated until justified.

---

# 28. Finding H-27 — “Static validator” must itself have a source of truth

**Severity:** HIGH.

Pass 89 proposes excellent lint rules. But the validator cannot infer the registry from the `.per` source alone without a schema source.

Required architecture:

```text
STATE ABI REGISTRY
        ↓
VALIDATOR
        ↓
`.per` implementation
```

not:

```text
`.per`
  ↓
validator guesses intent
```

The registry must be authoritative for AEGIS-owned channels.

---

# 29. Finding H-28 — The first implementation needs a namespace collision audit before any code

**Severity:** HIGH.

This is the immediate practical gate.

The audit must enumerate all loaded symbols and classify:

```text
ENGINE_RESERVED
STOCK_AI
CUSTOM_AI
AEGIS_RESERVED
FREE
UNKNOWN
```

A symbol cannot enter `AEGIS_RESERVED` from “looks unused.” It requires evidence from the actual load graph and definitions.

Because the workstation is currently unreachable for filesystem inspection, this audit is presently OPEN.

---

# 30. Finding M-29 — Official update history supports build sensitivity, but does not prove project validator semantics

**Severity:** MEDIUM.

Official notes are authoritative for documented engine changes. They are not automatically authoritative for the behavior of the project's validator/corpus.

The prior `knight-line` / `temporary-goal` incident demonstrates that:

```text
engine semantics
≠
validator acceptance semantics
```

Therefore the primitive registry should have separate fields:

```text
ENGINE_SUPPORT
VALIDATOR_SUPPORT
PROJECT_IMPLEMENTATION_SUPPORT
```

Do not collapse them.

---

# 31. Corrected architecture after hostile review

The safest post-QC model is:

```text
                    AEGIS SEMANTIC OBJECT
                              │
                              ▼
                    SCHEMA-TYPED RECORD
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
             FIELD REGISTRY       TRANSITION TABLE
                    │                   │
                    └─────────┬─────────┘
                              ▼
                       RUNTIME ABI
                              │
        ┌───────────────┬─────┼─────┬──────────────┐
        ▼               ▼     ▼     ▼              ▼
      GOALS           FLAGS   SNs  TIMERS       SEARCHES
        │               │     │     │              │
        └───────────────┴─────┼─────┴──────────────┘
                              ▼
                    VALIDATED PRIMITIVES
                              │
                              ▼
                       ENGINE / WORLD
                              │
                              ▼
                         OBSERVATION
                              │
                              └──────→ REASSESSMENT
```

Three things are authoritative:

```text
FIELD REGISTRY
TRANSITION TABLE
PRIMITIVE REGISTRY
```

Everything else is generated or derived from those authorities.

---

# 32. Mandatory Pass-90 deliverables

Pass 90 should produce, at minimum:

## A. Runtime Primitive Registry

For each primitive:

```text
ID
name
engine syntax
inputs
preconditions
side effects
success evidence
failure evidence
validator support
engine support
build profile
known limitations
```

## B. State ABI Registry

For each field:

```text
field ID
semantic type
authority class
storage class
numeric allocation
encoding
range
sentinel
owner
writers
readers
validity guard
generation guard
reset policy
build profile
```

## C. State Transition Table

Every legal transition:

```text
source
trigger
guards
writes
next state
required evidence
failure path
```

## D. Namespace Collision Audit

Actual loaded project/runtime symbol inventory.

## E. Minimal Cavalry Slice ABI

Only the fields actually required by the first closed loop.

---

# 33. Acceptance criteria for Pass 90

Pass 90 should not be marked complete unless it can answer all of these without prose hand-waving:

```text
1. What exact channel stores this field?
2. Is that channel collision-free?
3. Who owns it?
4. Who writes it?
5. Who reads it?
6. What values are legal?
7. What is zero?
8. How is it initialized?
9. How is it invalidated?
10. How is stale state detected?
11. How is generation created?
12. How is generation compared?
13. What exact primitive writes it?
14. What exact primitive reads it?
15. What engine evidence validates it?
16. What validator evidence validates it?
17. What happens if the evidence is absent?
18. What happens if the objective disappears?
19. What happens if the producer disappears?
20. What happens if the queue blocks?
21. What happens if a timer fires late?
22. What happens if another controller competes?
23. What happens if the workstation build differs?
24. What happens when the field is reused?
25. What test proves the contract?
```

If any answer is “the architecture assumes,” the item remains OPEN.

---

# 34. Final QC disposition

## What survives

The following Pass-89 foundations are approved:

```text
AEGIS cognitive/runtime separation
schema-based state representation
no-XS architecture
minimum sufficient state
engine-owned world truth
explicit execution stages
objective ≠ feasibility
capability ≠ unit type
issued ≠ completed
generation as stale-state defense
ownership as AEGIS policy
explicit recovery
build-sensitive architecture
state ABI concept
vertical-slice-first implementation strategy
adversarial validation philosophy
```

## What must be corrected before coding

```text
numeric namespace allocation
flag semantics
record publication protocol
writer enforcement
generation wrap/comparison
candidate selection mechanism
deficit arithmetic
resource reservation invariants
evidence promotion rules
arbitration epoch semantics
durable source provenance
profile registry
state transition table
authority-class metadata
namespace collision audit
```

## Overall verdict

**CONDITIONAL PASS — ARCHITECTURE QUALITY: HIGH; IMPLEMENTATION READINESS: NOT YET CLEARED.**

Pass 89 is not a failed pass. It is a successful architectural pass that exposed the exact places where conceptual rigor must become executable contracts.

The most important QC conclusion is:

> **Do not start writing the bot from Pass 89's prose. Start writing the bot from the registries and transition tables that Pass 89 now requires.**

That is the difference between a sophisticated design document and a dependable runtime architecture.

---

# Appendix A — Hard invariants promoted by QC

```text
Q1  No AEGIS field without registry entry.
Q2  No numeric allocation without collision audit.
Q3  No authoritative read without validity guard.
Q4  No reusable record mutation without generation guard.
Q5  No authoritative mutation without owner/writer discipline.
Q6  No command promotion without declared evidence.
Q7  No objective success from capability sufficiency alone.
Q8  No candidate optimization before hard feasibility.
Q9  No stale timer/search result may mutate a new generation.
Q10 Engine-owned state cannot be overwritten by AEGIS expectations.
Q11 Derived caches must be recomputable.
Q12 Compatibility profile must be validated against actual build.
Q13 Validator support and engine support are separate claims.
Q14 Every active commitment has a bounded review/exit path.
Q15 Arbitration epoch is authoritative over a dirty-bit optimization.
```

---

# Appendix B — Evidence status

### Direct / official evidence

- Strategic-number maximum reached 511 in Update 42848.
- Available goals increased from 512 to 16000 in Update Preview 125283.
- Queue/pending semantics evolved through official AI scripting updates.
- Research-queue interaction changed through official updates.

### Repository archaeology

- Historical AI uses goals/SNs/flags/timers/search state as mutable controller substrate.
- Procedural arbitration and resource competition are directly evidenced.
- Recovery/release/reset patterns are directly evidenced.
- Identity namespaces must not be conflated.

### AEGIS design

- schema-typed records
- ownership
- generations
- objective/capability/candidate abstractions
- arbitration epoch
- recovery taxonomy
- evidence promotion policy
- compatibility profiles

### Open runtime claims

- exact installed-build goal allocation
- collision-free AEGIS namespace
- exact flag semantics for the target build
- exact publication ordering under all relevant `.per` evaluation behavior
- validator acceptance of the final ABI
- runtime behavior of the final state machine

---

**QC result:** PASS WITH REQUIRED CORRECTIONS  
**Production `.per` authorized by this QC:** NO  
**Layer 1 reopened:** NO  
**XS introduced:** NO  
**Workstation runtime validation:** BLOCKED — ping succeeds, filesystem access currently reports `Not connected`  
**Next engineering target:** Pass 90 — Runtime Primitive Registry + State ABI Registry + Transition Table + Namespace Collision Audit.