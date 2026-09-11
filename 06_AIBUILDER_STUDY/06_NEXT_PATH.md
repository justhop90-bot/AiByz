# AiBuilder Study — Forward Path

**Status:** ACTIVE — governing work plan

**Repository:** `justhop90-bot/AiByz`

**Scope:** `06_AIBUILDER_STUDY/` and the current `AiBuilder.per` + `AiBuilder/` source corpus.

## 1. Objective

The purpose of this study is not to improve AiBuilder. It is to determine, with source-backed evidence, whether AiBuilder provides a safe and sufficiently understood execution substrate on which AEGIS can eventually place Byzantine policy.

No Byzantine policy implementation is authorized merely because a Goal, timer, rule, or command appears usable.

The governing contract is:

`SOURCE → ABI → OWNERSHIP → LIVENESS → AUTHORITY → RUNTIME QUALIFICATION → VERTICAL SLICE → AEGIS POLICY`

A later stage cannot be used to silently establish a fact that an earlier stage failed to prove.

## 2. Immediate work: finish the static substrate audit

### 2.1 Reconcile the ABI matrix against source

The existing ABI matrix is the working inventory, not an engine guarantee. Recheck it against the actual root and loaded modules.

Required outputs:

- every explicitly allocated Goal 1–121;
- every unallocated interval, especially 122–479;
- complete 480–510 working/register characterization;
- every explicit timer allocation;
- every operation that may span more than one Goal;
- every point/search-state register alias;
- every Strategic Number symbol used by the corpus;
- declaration-order or loader-order questions that remain unresolved.

**Important:** `122–479 unallocated by AiBuilder` must remain distinct from `122–479 engine-safe.`

### 2.2 Resolve operation width and alias hazards

For each non-scalar Goal operation, determine the actual source-level span and all symbols participating in it.

Particular attention:

- coordinate pairs 480–491;
- search-state 495–498;
- shared scratch 501–510;
- `temporary-goal2` / Goal 509;
- `temporary-goal` / Goal 510;
- any multi-Goal read/write operation in construction, general, or military behavior.

Do not describe scratch lifetime as runtime-safe. The source establishes reuse; it does not by itself establish temporal isolation.

### 2.3 Complete ownership/liveness tracing

For each policy channel, record:

`declaration → all writers → all readers → predicates/comparisons → feasibility gate → action request → downstream consumer → reassessment`

Classify each channel as:

- single-writer/single-consumer;
- controlled multi-writer;
- multi-reader;
- write-without-reader;
- read-without-writer;
- alias-sensitive;
- authority-ambiguous;
- runtime-unknown.

The existing traces for Goals 48, 49, and 57 are evidence-backed starting points. They do not justify generalizing the pattern to the rest of the Goal bank without tracing each channel.

The next military channel to trace is Goal 54 only after recovering its actual source occurrences; its presence in an inventory table is not sufficient evidence.

## 3. UC-04' resolution

The earlier interpretation of UC-04 as a failure to establish symbolic-to-numeric binding is corrected.

The composition root directly establishes symbolic Goal names and numeric assignments. The unresolved question is narrower:

> Is declaring additional Goal slots legal and safe for the target engine/runtime, and are apparently unallocated slots actually available to AEGIS?

The study must therefore separate:

1. **binding mechanism — DIRECT**;
2. **existing allocation — DIRECT**;
3. **unallocated repository range — DIRECT**;
4. **extension syntax legality — UNKNOWN until established**;
5. **engine slot availability/safety — UNKNOWN until established**;
6. **declaration-order effects — UNKNOWN until established**;
7. **duplicate/alias behavior — UNKNOWN until established**.

Until items 4–7 are resolved, no new Byzantine Goal declaration is authorized.

## 4. Ownership decision

The first design decision is not "which new Goals should AEGIS allocate?"

It is:

> Can AEGIS safely control an already-existing AiBuilder policy channel without corrupting its owner, consumer, or lifecycle?

This is the existing-channel authority question.

For an existing channel, preserve the distinction between:

- **current owner** — who presently writes it;
- **consumer** — who presently reads it;
- **proposed authority** — who AEGIS would like to control it;
- **runtime precedence** — which writer wins when multiple writers execute;
- **authorization boundary** — when AEGIS may write;
- **expiry/reversion** — when AEGIS must relinquish control;
- **reassessment** — how ownership is re-evaluated.

No existing channel becomes "Byzantine-owned" merely because it looks convenient.

## 5. Runtime qualification comes after static closure

Runtime tests will answer narrow questions that static source cannot answer. They will not be used as exploratory debugging by the tester.

The first runtime qualification should establish the smallest possible existing-channel authority contract:

`known condition → existing policy Goal → existing consumer → existing feasibility gate → existing action request`

The test must distinguish at minimum:

- policy value written;
- policy value read by the consumer;
- action request issued;
- physical/world transition;
- downstream reassessment.

An action request is not completion evidence.

A unit count observed later is not automatically proof of causal ownership because resource availability, queues, population limits, timing, and other rules can intervene.

## 6. Vertical-slice promotion

After an existing-channel authority path is runtime-qualified, promote one complete vertical slice.

The governing slice is the **Civilian Production Loop**:

`condition → policy → desired civilian count → economy consumer → feasibility → train request → engine transition → confirmation → reassessment`

The slice must be small enough that every state transition has an identifiable owner and evidence boundary.

No broad Byzantine intelligence layer should be built around an unqualified substrate.

## 7. Only then build AEGIS policy

Once the substrate contract is qualified, AEGIS can begin replacing policy rather than reinventing execution.

The eventual pattern is:

`WORLD → OBSERVE → CLASSIFY → BELIEVE → TRANSITION → OBJECTIVE → REQUIREMENTS → CONSTRAINTS → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE → EXISTING EXECUTION SUBSTRATE → VERIFY → UPDATE → REASSESS`

AiBuilder supplies execution machinery only where its behavior has been established. AEGIS supplies Byzantine strategic policy only where ownership and authority are explicitly defined.

## 8. Gates

### Gate A — Static ABI

**Pass condition:** the relevant ABI, widths, aliases, declarations, and unresolved engine boundaries are explicitly documented.

### Gate B — Ownership/Liveness

**Pass condition:** the selected existing channel has a complete source-level writer/reader/execution graph and no unresolved ownership contradiction.

### Gate C — Runtime Authority

**Pass condition:** a deliberately minimal qualification establishes whether the proposed writer can affect the existing consumer under controlled conditions.

### Gate D — Vertical Slice

**Pass condition:** one complete production lifecycle is evidenced from policy through execution and reassessment.

### Gate E — AEGIS Policy

**Pass condition:** AEGIS can express policy without requiring unqualified Goal/timer allocation or undocumented engine semantics.

## 9. Current prohibitions

Until the corresponding gate passes:

- no new Goal declarations;
- no new timer declarations;
- no use of 122–479 as if they were free ABI;
- no use of 480–510 as Byzantine state storage;
- no Byzantine ownership claim over an existing Goal;
- no broad override layer;
- no XS;
- no ADProm/byzwarcouncil architecture imported as a template;
- no scenario-loader automation revival;
- no tester-driven discovery campaign.

## 10. Immediate next deliverables

1. Reconcile the ABI matrix against the current source corpus.
2. Complete operation-width and alias audit.
3. Finish source-backed ownership/liveness traces for the selected policy channels.
4. Resolve UC-04' as far as source evidence permits and isolate the remaining engine question.
5. Select exactly one existing-channel runtime authority qualification.
6. Execute that qualification only after its expected observations and failure interpretations are frozen.
7. Promote the Civilian Production Loop only after runtime authority is established.

**Current state:** static study remains active. Byzantine implementation remains blocked.
