# Letter to the Engineer Who Takes AEGIS From Here

**September 5, 2026**

To the engineer — human or AI — who inherits this project after this conversation:

You are not inheriting a finished bot. You are inheriting something more important at this stage: a deliberately constrained body of research, architecture, evidence, failed experiments, and engineering decisions that has been brought to the point where implementation can begin — but only after one final factual gate is closed.

I have treated the repository as the durable memory of the project. The conversation is now disposable. **GitHub is the authority.** If you remember something that is not in the repository, assume it is suspect until you can reproduce it from committed evidence.

## What I did

I took the project from broad AoE2DE machine archaeology and HD/Promisory source archaeology toward an explicit AEGIS architecture.

The major work was not simply collecting commands or writing down interesting `.per` tricks. The important work was reconstructing the control problem underneath them.

The historical AI was studied as a constrained strategic controller. Its recurring pattern is roughly:

`PROBLEM → OBSERVE → CLASSIFY → STATE → REQUIREMENT → COMMIT → AUTHORIZE → ACT → OBSERVE RESULT → RECOVER / REASSESS`

That reconstruction led to a more ambitious AEGIS model:

`WORLD → OBSERVE → CLASSIFY → BELIEVE → DETECT TRANSITION → OBJECTIVE → REQUIREMENTS → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXECUTE → VERIFY → RECOVER / RE-ARBITRATE → REASSESS`

I deliberately did **not** assume that the historical AI literally contains these abstractions. They are AEGIS architectural abstractions derived from observed mechanisms and explicitly graded as such.

I also established a hard distinction between three kinds of closure:

`CONTROL → WORLD → STRATEGIC`

Issuing a command is not proof that the engine accepted it. Acceptance is not proof that the intended object exists. Object existence is not proof that the strategic objective succeeded.

That distinction is one of the most important pieces of the entire project.

## Where I left the project

The project is at the boundary between **architecture and implementation**.

Layer 1 is frozen at 89%. Broad machine archaeology is no longer the priority. Scenario-loader automation was retired because it became an unreliable engineering path; do not resurrect it merely because the old conversation mentioned it.

Layer 2 — HD/Promisory strategic archaeology — is effectively closed. The important strategic mechanisms have been recovered. Additional research should now be targeted and justified by its ability to change the architecture or implementation.

Layer 3 is the active workstream. The architecture has been subjected to hostile QC and has survived with important corrections.

Layer 4 runtime implementation is still intentionally blocked.

The first vertical slice is:

**Cavalry Threat Containment**

The intended loop is:

`OBSERVE ENEMY CAVALRY → CLASSIFY THREAT → DEFINE CAMEL CAPABILITY REQUIREMENT → MEASURE CURRENT CAPABILITY → COMPUTE DEFICIT → CHECK RESOURCES / FEASIBILITY → SELECT PRODUCER → COMMIT → EXECUTE → VERIFY → RECOVER / RE-ARBITRATE → REASSESS`

The architecture is ready for the next factual step. The numeric ABI is not.

## The single most important next step

**Acquire the exact installed target AI package and executable identity from Weebo, freeze it as an immutable evidence snapshot, and run the deterministic ABI audit described in Pass 94.**

Do not start writing `.per` because a goal number looks free.

Do not choose an SN because it seems unused.

Do not assume flags, goals, strategic numbers, timers, and searches form one namespace.

Do not trust a validator to tell you what the engine means.

Do not trust a parser to tell you that something does not exist merely because it failed to parse it.

The correct sequence is:

`INSTALLED BUILD → IMMUTABLE AI SNAPSHOT → IMPORT CLOSURE → SYMBOL INVENTORY → REFERENCE INVENTORY → CHANNEL NORMALIZATION → COLLISION AUDIT → WRITER/READER MATRIX → ENGINE/VALIDATOR/AEGIS JOIN → NUMERIC ABI DECISION`

The exact output contract is already specified in:

`04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`

That is where I would begin the next engineering session.

## What we currently believe about the build

The project evidence fingerprints the target as:

`AoE2DE 101.103.48987.0 / Update #180059`

This is the current engineering target and is consistent with the replay evidence and public update chronology.

But there is an important qualification: **do not promote that to A1 installed-machine truth until the executable has actually been read from Weebo and hashed.**

The distinction matters because this project has spent considerable effort learning not to confuse corroboration with authority.

The desired A1 record is:

`executable path + FileVersion + ProductVersion + SHA-256 + acquisition timestamp + exact AI root + package manifest`

Once that exists, the package itself becomes the evidence substrate for the ABI audit.

## The architectural breakthrough

The most important architectural conclusion is that AEGIS should not be designed as a giant rule list.

It should be designed as a **bounded state-and-commitment system operating through a constrained runtime language**.

The `.per` layer is not the whole intelligence. It is the execution substrate.

AEGIS therefore needs a translation discipline:

`STRATEGIC NEED → CAPABILITY → FEASIBLE PLAN → VERIFIED RUNTIME PRIMITIVES → EXECUTION → POSTCONDITION → REASSESSMENT`

Every high-level abstraction must eventually have a verified realization path in the actual AoE2DE environment.

If you invent a beautiful concept that cannot be represented by the verified runtime, it is architecture fiction.

Conversely, if you find an ugly native primitive that solves a real control problem reliably, do not reject it merely because it is ugly. The objective is a capable system, not architectural aesthetics.

## The second most important lesson: state is dangerous

The project has repeatedly encountered the temptation to treat shared state as if it were a normal programming-language variable with ownership and atomic transactions.

Do not do that.

Goals, strategic numbers, flags, timers, searches, target points, and other state channels have different semantics. Same-pass visibility does not automatically prove atomic handoff. Rule order can create arbitration effects without constituting a universal scheduler. `sn-resource-control` is useful stateful admission machinery, but it is not proven to be a universal mutex.

The first AEGIS state envelope is therefore deliberately explicit:

`VALID + OWNER + GENERATION + STAGE + PAYLOAD + EVIDENCE_LEVEL`

The publication protocol is deliberately described as a protocol, not as an atomic transaction:

`VALID=0 → populate payload → generation/owner/stage → VALID=1`

Readers must guard validity, ownership, generation, and legal stage as appropriate.

Generation exists because delayed actions and changing world observations create stale-state hazards. The generation mechanism itself still needs to be realized against verified native primitives before implementation.

## The ABI is the current dragon

Passes 92–94 froze the **symbolic** ABI for the first slice. The symbolic fields are:

- `OBS.ENEMY_CAVALRY`
- `OBS.ENEMY_CAVALRY_AGE`
- `THREAT.CAVALRY_ACTIVE`
- `CAP.CAMEL_CURRENT`
- `CAP.CAMEL_REQUIRED`
- `CAP.CAMEL_DEFICIT`
- `CAND.PRODUCER`
- `CAND.STATUS`
- `COMMIT.VALID`
- `COMMIT.OWNER`
- `COMMIT.GEN`
- `COMMIT.STAGE`
- `EXEC.STAGE`
- `EXEC.EXPECTED_GEN`
- `RES.RESERVED`
- `RES.DISCRETIONARY`
- `ARB.EPOCH`
- `ARB.DIRTY`
- `VERIFY.LEVEL`

The count is provisionally 16 goal-like fields plus 3 flags. That representation is allowed to change if the authoritative inventory demonstrates that another representation is safer.

What is **not** frozen is the numeric allocation.

This is intentional.

The project already learned from the `knight-line` / `temporary-goal` validator incident that an identifier can be semantically correct for the engine while being represented differently in a validator corpus, and that a high-numbered scratch goal can be valid in one primitive context while invalid in another. The correct response was not to blindly change semantics to satisfy a linter. The correct response was to establish the engine/validator distinction and then audit the target build.

Carry that lesson forward everywhere.

## What the HD archaeology actually taught us

Do not make the mistake of thinking the old AI was strategically empty because it is rule-based.

The historical HD/Promisory AI is a capable bot with meaningful strategic structure, although materially below a decent human player.

Its sophistication comes from distributing a controller across primitive state channels and rule eligibility.

The important recurring mechanisms are:

- measurement compressed into reusable state;
- guards before side effects;
- search before commitment;
- contextual resource allocation;
- protected strategic transitions / escrow;
- production treated as a capability pipeline;
- threat classification feeding counter-capability production;
- attack / retreat / restart lifecycle;
- timers as temporal control;
- scouting as constrained geometric information acquisition;
- persistent state and rule eligibility as a distributed controller;
- explicit fallback and recovery behavior.

The historical implementation is therefore worth mining for **control patterns**, not copying line-for-line.

## The cavalry/camel slice is not arbitrary

The strongest historically supported counter chain found in the archaeology is:

`ENEMY MOUNTED PRESSURE → CAVALRY THREAT STATE → CAMEL PRODUCTION CONDITIONS → FEASIBILITY GATES → TRAIN CAMEL`

Replay evidence independently corroborated that Byzantine camel production and enemy knight production occur in the relevant sequences, including cases where knight production precedes camel production.

But the project deliberately did **not** claim that replay ordering proves causality.

That distinction is essential.

The first AEGIS slice should therefore prove the architecture's ability to represent a defensible causal/control loop, not retrofit a causal story onto replay chronology.

## Do not collapse mechanical identity into strategic identity

One of the useful corrections from the Byzantine archaeology is the Cataphract example.

Mechanically:

`Cataphract = cavalry / mounted`

Strategically:

`Cataphract = anti-infantry capability`

Those statements can both be true.

The AEGIS capability model must therefore separate:

`MECHANICAL FAMILY`
`COMBAT PROPERTIES`
`TARGET-SPECIFIC EFFECT`
`STRATEGIC ROLE`

A unit's engine category is not its strategic purpose.

This is more important than it sounds because a future optimizer that uses raw unit classes as strategic roles will systematically make bad capability substitutions.

## The evidence discipline you must preserve

Every important claim should answer two questions:

**What is the evidence?**

**What kind of claim did we make from it?**

The current evidence ladder is:

`E0 / DIRECT → E1 / COMPOSED → E2 / AEGIS-GENERALIZATION → E3 / HYPOTHESIS`

And closure remains:

`CONTROL → WORLD → STRATEGIC`

The most dangerous failure mode in this project is **composition inflation**: several true observations get chained together until the final sentence sounds directly proven even though only the first pieces were observed.

Pass 87 exists specifically to make that failure harder.

Read it carefully.

## Where you should look first

If you have only one hour, read these in order:

### 1. `docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`

This is the current clean-room recovery point. It tells you what the project is, the current layer status, the current architecture, the ABI gate, the build qualification, and the immediate sequence.

### 2. `docs/CANONICAL_QC_2026-09-05.md`

This is the hostile review. Read it even if you think the architecture is obvious. It records what was challenged and what remains deliberately blocked.

### 3. `04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`

This is the next-action document. It tells you exactly how to turn the live target package into an auditable ABI inventory.

### 4. `04_LAYER3_ARCHITECTURE/PASS93_AUTHORITATIVE_ABI_INVENTORY_SPEC_2026-09-05.md`

This explains what the inventory must contain and how numeric allocation decisions are supposed to be made.

### 5. `04_LAYER3_ARCHITECTURE/PASS92_ABI_FINALIZATION_AND_ALLOCATION_GATE_2026-09-05.md`

This gives the symbolic first-slice contract and the explicit reasons numeric allocation was not cleared.

### 6. `04_LAYER3_ARCHITECTURE/PASS91_CROSS_MODULE_CONTRACT_MATRIX_2026-09-05.md`

This is where the subsystem boundaries become concrete: Intelligence, Assessment, Objective, Force, Production, Arbitration, Execution, Verification, and their contracts.

### 7. `04_LAYER3_ARCHITECTURE/PASS91_FAILURE_TOPOLOGY_AND_INTEGRATION_TEST_PLAN_2026-09-05.md`

Read this to understand how the system is expected to fail, recover, wait, release, replace, re-arbitrate, and abandon rather than simply issuing commands.

### 8. `03_HD_ARCHAEOLOGY/PASS87_END_TO_END_EVIDENCE_GRAPH_2026-09-05.md`

This is where the epistemology of the project becomes explicit. It is one of the best documents for understanding why some apparently obvious claims remain unproven.

## Where to dive for the full complexity

If you want to **understand the project rather than merely operate it**, do not read the repository as a pile of documents.

Read it as four increasingly concrete layers.

### Dive A — Why the architecture exists

Start with Pass 87 and work backward through the late HD archaeology passes, especially the commitment, arbitration, recovery, production-observability, and identity work.

You are looking for repeated control patterns, not isolated tricks.

### Dive B — How the architecture was constructed

Read Passes 88–94 sequentially.

This is the transition from archaeological findings to AEGIS engineering. You will see the project progressively discover that strategic concepts need runtime realization, that state needs contracts, that contracts need failure semantics, and that state contracts ultimately require an audited ABI.

### Dive C — Why implementation is currently blocked

Study the hostile QC and ABI documents together.

The central question is not "can I make this run?"

It is:

**Can I prove that the state channels I am about to use are legal, non-colliding, correctly scoped, and semantically compatible with the exact target build?**

If the answer is no, implementation is premature.

### Dive D — The historical source itself

Only after understanding the architecture should you return to the HD/Promisory source artifacts and the practical coding knowledge base.

At that point you will read the old `.per` differently. You will see why apparently crude rules form a distributed state machine and where the historical programmer was compensating for missing language/runtime features.

## What not to waste time on

Do not reopen broad Layer-1 archaeology.

Do not restart scenario-loader automation.

Do not make CADE the center of the project.

Do not chase XS. It is outside AEGIS.

Do not turn the replay interpreter into the bot runtime.

Do not create a giant optimizer before the state/commitment substrate is proven.

Do not write hundreds of `.per` rules to discover whether the architecture works.

Build one vertical slice.

Make it survive hostile tests.

Then expand.

## The intended engineering order from here

`1. VERIFY BUILD`

`2. SNAPSHOT TARGET AI`

`3. AUDIT ABI`

`4. FREEZE NUMERIC CONTRACT`

`5. IMPLEMENT MINIMAL CAVALRY/CAMEL SLICE`

`6. STATIC VALIDATION`

`7. CONTROLLED ENGINE TEST`

`8. REPLAY CORROBORATION`

`9. FAILURE-INJECTION TESTS`

`10. BATTLEFIELD TEST`

`11. ONLY THEN GENERALIZE`

Do not reverse this order merely because writing code feels more productive than proving the substrate.

## My final warning

The project is now complex enough that the greatest danger is no longer ignorance.

It is **false confidence**.

There are enough real facts in the repository to construct a convincing but subtly incorrect AI. There are enough inferred mechanisms to make a beautiful architecture that does not actually map onto AoE2DE. There are enough validator quirks to produce code that passes a linter while relying on the wrong engine semantics. There are enough replay events to construct causal narratives that the replay cannot actually prove.

Fight that tendency relentlessly.

When something is unknown, mark it unknown.

When something is inferred, mark it inferred.

When a mechanism is proven only at the control layer, do not promote it to strategic success.

When an implementation works once, do not call it an architecture until it survives failure.

When a number appears unused, do not allocate it until the collision audit says it is safe.

And when the old AI does something clever, understand **why the mechanism works** before deciding that AEGIS should reproduce it.

## Where I would personally start

If I were waking up tomorrow with no conversational memory, I would open:

`docs/CANONICAL_PROJECT_HANDOFF_2026-09-05.md`

then:

`docs/CANONICAL_QC_2026-09-05.md`

then:

`04_LAYER3_ARCHITECTURE/PASS94_DETERMINISTIC_ABI_AUDIT_HARNESS_SPEC_2026-09-05.md`

Then I would connect to Weebo and obtain the A1 build/package evidence.

I would **not write a line of `.per` first**.

Once the ABI is cleared, I would implement the smallest possible Cavalry Threat Containment slice and make the failure-topology tests pass before adding intelligence, optimization, or breadth.

That is where I left you.

The archaeology has done its job.

The architecture has earned the right to be tested.

Now prove the substrate — and then build the bot.

— **Project handoff**
