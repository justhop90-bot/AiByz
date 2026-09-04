# PASS 39 — C1-C Decision Envelope Reconstruction

Date: 2026-09-04  
Layer: 2 — HD/Promisory archaeology  
Mission: C1 Threat → Capability  
Status: **PASS — decision envelope reconstructed; replay compatibility remains underdetermined, so no causal closure is claimed.**

## 1. Purpose

The project recommendation is to stop treating archaeology as an end in itself. This pass therefore asks the practical question:

> Can the historical camel controller be reduced to a reusable decision envelope that AEGIS can implement and improve?

The answer is **yes**. The available evidence is sufficient to recover the controller's major inputs, gates, and commitment shape. The replay corpus is not sufficient to prove that the hidden controller fired in either observed game.

## 2. Historical decision envelope

The strongest reconstructed form is:

`FOCUS-PLAYER MOUNTED OBSERVATION`
→ `THREAT AGGREGATION`
→ `PHASE-SCOPED CAVALRY NORMALIZATION`
→ `CONTEXT / CIVILIZATION GATES`
→ `RESOURCE / MILITARY FEASIBILITY`
→ `CAVALRY / CAVARCHER PRESSURE THRESHOLD`
→ `OWN CAMEL-SET CEILING`
→ `TRAINCAMEL AUTHORIZATION`
→ `PRODUCTION FEASIBILITY`
→ `CAMEL QUEUE`

This is a composed controller model. Individual edges are supported by historical source; the complete causal chain is a reconstruction rather than a directly observed runtime trace.

## 3. Pressure ladder

The historical camel-production logic contains threshold/ceiling pairs including:

| Pressure input | Own camel-set ceiling | Response |
|---:|---:|---|
| 4 | < 6 | traincamel |
| 5 | < 8 | traincamel |
| 7 | < 11 | traincamel |
| 10 | < 16 | traincamel |
| 15 | < 24 | traincamel |
| 25 | < 40 | traincamel |
| 40 | < 58 | traincamel |

Additional contextual/civilization branches contain different pressure/ceiling pairs, including approximately 3→10, 7→20, 15→40, 25→35, and 35→45. These must remain branch-specific; they are not a universal camel formula.

The practical design pattern is therefore not `camel_count = f(cavalry)`. It is a **piecewise response envelope** in which perceived pressure raises the permitted counter-capability ceiling, subject to contextual gates.

## 4. Hard constraints

Observed historical gates include combinations of:

- military-production state (`milunits`);
- food buffer / resource availability;
- own `camel-set` ceiling;
- enemy `cavalry` and `cavarchers` state;
- research status and technology prerequisites;
- unit availability;
- population constraints;
- civilization/preprocessor branches;
- military-superiority and monk-count conditions.

Therefore the historical controller is better represented as:

`DESIRED COUNTER-CAPABILITY`
`+ HARD FEASIBILITY CONSTRAINTS`
`→ `AUTHORIZATION`

rather than as a direct threat-to-unit mapping.

## 5. The normalization finding matters

Pass 37 established that `camels` is a focus-player threat component while `camel-set` is an own-capability inventory. `cavalry` is a mutable aggregate that is temporarily decremented by `camels` and later restored.

This means the historical controller contains a phase-scoped derived state transformation:

`component observation`
→ `aggregate`
→ `normalize`
→ `decision`
→ `restore`

The exact strategic reason for subtraction remains uncertain. We therefore do **not** encode the stronger hypothesis that it definitely removes enemy camel pressure from the generic cavalry threshold.

## 6. Replay compatibility test

Pass 38 established two Byzantine-player replay cases in which enemy knight production preceded the first Byzantine camel queue.

Replay A:
- first Byzantine camel queue: sequence 2,945,313;
- enemy knight queue history before it: 35 recorded actions;
- latest preceding enemy knight queue: 2,536,974.

Replay B:
- first Byzantine camel queue: sequence 2,918,785;
- enemy knight queue history before it: 10 recorded actions;
- latest preceding enemy knight queue: 1,855,078.

These facts establish temporal compatibility with the broad historical direction `enemy mounted activity → camel production`, but they do not expose the internal `cavalry`, `cavarchers`, `camel-set`, `traincamel`, or research-state values at the decision instant.

Therefore the strict compatibility result is:

**BROAD COMPATIBILITY: CONFIRMED.**

**THRESHOLD COMPATIBILITY: UNDETERMINED.**

**CAUSAL AUTHORIZATION: UNOBSERVABLE.**

This distinction is deliberate.

## 7. Why we stop here

The remaining missing evidence is not merely another instance of the same question. To close threshold compatibility we would need reliable reconstruction of the enemy mounted inventory and the relevant technology/production state at the exact decision boundary, plus confidence that those reconstructed values correspond to the same state consumed by the historical controller.

The current replay representation does not expose the historical strategic-number state or rule firing. Additional camel-transition examples would improve statistical corroboration but would not, by themselves, expose that hidden authorization edge.

Consequently, further forensic effort on this exact transition has diminishing capability return.

## 8. AEGIS extraction

The reusable AEGIS pattern is:

`OBSERVE`
→ `CLASSIFY THREAT`
→ `ESTIMATE REQUIRED CAPABILITY`
→ `APPLY HARD CONSTRAINTS`
→ `GENERATE / SCORE RESPONSE LEVEL`
→ `COMMIT`
→ `AUTHORIZE`
→ `EXECUTE`
→ `VERIFY`
→ `REASSESS`

The key improvement over the historical mechanism is that AEGIS should keep the quantities conceptually separate:

- observed enemy capability;
- derived threat pressure;
- required counter-capability;
- existing friendly capability;
- feasibility;
- commitment;
- execution status;
- verification result.

A single mutable aggregate should not be allowed to obscure these distinctions in the architecture, even if `.per` implementation later requires compact state channels.

## 9. Capability target

The purpose of C1 is not to reproduce `traincamel`. It is to create a general adaptive composition controller.

Target abstraction:

`THREAT VECTOR`
→ `REQUIRED CAPABILITY`
→ `TARGET CAPABILITY LEVEL`
→ `DEFICIT`
→ `RESOURCE / TIMING FEASIBILITY`
→ `PRODUCTION COMMITMENT`
→ `POSTCONDITION`
→ `REASSESSMENT`

The camel case becomes one calibration instance of that controller.

## 10. Evidence disposition

| Element | Status | Evidence class |
|---|---|---|
| enemy mounted observation | CONFIRMED | DIRECT historical source |
| cavalry/cavarcher aggregation | CONFIRMED | DIRECT historical source |
| phase-scoped cavalry normalization | CONFIRMED | DIRECT historical source |
| camel-set as own capability inventory | CONFIRMED | DIRECT historical source |
| pressure/ceiling ladder | CONFIRMED | DIRECT historical source |
| production feasibility gating | CONFIRMED | DIRECT historical source |
| enemy knight → camel temporal ordering | CONFIRMED | DIRECT replay actions / COMPOSED relation |
| exact replay-time threshold crossing | UNDETERMINED | replay state insufficient |
| historical traincamel firing in replay | UNOBSERVABLE | replay state insufficient |
| knight production caused camel decision | UNPROVEN | alternative explanations remain |
| AEGIS deficit-based generalization | AEGIS-GENERALIZATION | derived design |

## 11. Engineering decision

**C1-C is complete enough to graduate.**

Do not spend additional passes attempting to prove hidden `traincamel` authorization from the current replay corpus unless a new evidence source exposes controller state.

The historical evidence is now sufficient to justify implementation of a generalized **Threat → Capability → Deficit → Commitment** subsystem.

The implementation must preserve the evidence boundary: historical behavior supplies the design primitives; the generalized deficit/commitment machinery is explicitly an AEGIS invention.

## 12. Next target

Move from archaeology to capability engineering.

First implementation target: define the AEGIS adaptive composition controller as a `.per`-implementable state machine, with explicit:

`THREAT VECTOR → CAPABILITY REQUIREMENT → DEFICIT → HARD CONSTRAINTS → RESPONSE LEVEL → COMMITMENT → AUTHORIZATION → VERIFICATION → RELEASE / ESCALATE / REDIRECT`.

The first concrete calibration case should remain cavalry pressure → camel capability, because its historical envelope is now sufficiently characterized to serve as the reference implementation without pretending the implementation itself is historical code.
