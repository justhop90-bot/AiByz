# Layer 1 — Predictive Machine Understanding Standard

**Date:** 2026-09-02  
**Status:** Governing research standard  
**Scope:** Native AoE2DE machine understanding only  
**Excluded:** XS and XS qualification are not part of this project scope.

## 1. Objective

Layer 1 is not complete when the executable can be described, when APIs have been catalogued, or when a plausible architecture diagram exists.

Layer 1 is complete only when the machine is understood sufficiently to construct an AI framework whose behavior can be reasoned about from the machine's own mechanisms without unacknowledged semantic assumptions.

The target is **predictive machine understanding**: for a sufficiently specified state and input, the investigator should be able to trace the causal path through the relevant machine layers and predict the next meaningful machine behavior before the AI framework is implemented.

## 2. Three levels of understanding

### 2.1 Machine

Determine what the executable actually does:

- execution model
- simulation/update loop
- AI invocation and scheduling
- rule interpreter
- facts and goals
- state representation
- object/unit/entity model
- identity and lifecycle
- command generation and execution
- production and construction
- player state
- visibility and knowledge
- timing and ordering
- replay recording
- data-driven definitions
- error/failure behavior

### 2.2 Programmer

Determine why important mechanisms are structured as they are, using evidence rather than intuition.

For each significant mechanism, distinguish:

1. observation
2. implementation mechanism
3. constraint
4. supported design rationale
5. resulting behavior
6. implication for an AI built above it

A symbol name, source-like string, or decompiler label is not sufficient evidence of programmer intent.

### 2.3 Predictive interaction

The final test is not isolated subsystem knowledge. It is interaction knowledge.

For every critical AI path, establish:

- trigger
- scheduler/order
- input state
- representation crossing the boundary
- transformation
- internal state mutation
- side effect
- postcondition
- subsequent observation
- failure path
- timing
- persistence

## 3. Causal-spine requirement

Layer 1 must reconstruct the critical causal spines, including at minimum:

### Simulation

`initialization → update/tick → state mutation → next update`

### AI

`AI initialization → scheduler/dispatch → evaluation → fact/goal state → action selection → command emission`

### Object lifecycle

`definition → creation → insertion → active state → mutation → transformation/removal`

### Command execution

`AI request → command representation → validation → dispatch → execution → result`

### Replay

`simulation event → recorder → encoded replay event → parser observation`

Each spine must be supported by native evidence where possible. Replay/parser evidence is corroboration and observation, not a replacement for native implementation evidence.

## 4. Prediction test

For a critical mechanism, the investigator should eventually be able to specify:

`PRECONDITION → TRIGGER → DISPATCH → PROCESSING → STATE TRANSITION → POSTCONDITION`

and identify any hidden or asynchronous intermediate states.

A mechanism remains incomplete if an unknown boundary can materially alter the AI's behavior and that boundary has not been characterized.

## 5. Evidence discipline

Evidence classes remain hierarchical:

1. RUNTIME-IDENTITY
2. SCRIPT-CONSUMED
3. NATIVE-VOCABULARY
4. SOURCE-CONTRACT
5. NATIVE-IMPLEMENTATION
6. RUNTIME-EXPERIMENT
7. INFERENCE
8. HYPOTHESIS
9. HISTORICAL

Rules:

- symbol name is vocabulary, not semantics
- declaration is contract surface, not implementation
- string reference is not a call graph
- decompiler rendering is not automatically correct source
- replay field is observation, not complete internal state
- absence is not destruction
- command issuance is not execution success
- execution success is not strategic postcondition success
- intuition does not promote evidence

A claim is promoted only when the evidence demonstrates the proposition itself.

## 6. Tooling policy

Ghidra is the primary native archaeology instrument.

The controlled headless analysis is the reproducible baseline. Historical Pass33 remains preserved as evidence and must not be modified during the controlled investigation.

mgz-fast is the replay observation instrument. Its output must be treated according to what the parser actually decodes and preserves. Parser assumptions, discarded fields, guessed decoders, and encoding transformations must remain visible in the evidence chain.

Additional tools are justified only by a concrete unanswered Layer 1 question. The project should prefer targeted instrumentation over accumulating redundant tools.

## 7. Native archaeology automation

The investigation is authorized to create scripts for:

- PE/runtime inventory
- memory and section inventory
- imports/exports/TLS
- function inventory
- callers/callees
- call graph topology
- strongly connected components
- thunks/wrappers
- constructors/destructors
- strings and xrefs
- globals and data references
- structure candidates and field offsets
- vtables/RTTI where available
- semantic clusters
- candidate AI/object/unit/player/simulation/command/replay regions
- reproducible evidence reports

Automation is a discovery and measurement layer. It does not automatically promote semantic claims.

## 8. Object and identity standard

Object/unit identity is a critical Layer 1 dependency.

The investigation must resolve, with implementation evidence where possible, the relationships among:

- unit ID
- object ID
- copy ID
- game ID
- unique ID
- object fields such as `obj->id`
- ownership
- type/class
- lifecycle state
- transformation
- garrison
- creation/removal

The existence of native vocabulary such as `xsGetUnitObjectId`, `xsGetObjectType`, `xsGetObjectClass`, and related queries establishes important vocabulary but does not by itself establish complete identity semantics.

## 9. Programmer-mind reconstruction

Programmer intent must be reconstructed from converging evidence:

- implementation structure
- callers and callees
- data ownership
- repeated patterns
- boundary placement
- state lifetime
- error handling
- performance-oriented structures
- naming/source remnants
- runtime experiments
- replay consequences

When intent cannot be demonstrated, record competing hypotheses rather than choosing the most attractive explanation.

## 10. Framework-readiness gate

Layer 1 cannot be marked 100% until the following are true for the critical AI execution paths:

- exact executable identified and hashed
- native analysis reproducible
- analysis configuration recorded
- major machine subsystems mapped
- simulation timing characterized
- AI dispatch/scheduling characterized
- rule evaluation mechanism characterized
- facts/goals state model characterized
- command path characterized
- object/unit identity topology characterized
- lifecycle transitions characterized
- relevant data structures characterized
- important cross-layer state boundaries characterized
- failure/rejection behavior characterized
- replay boundaries characterized
- native and observational evidence separated
- programmer-intent claims graded
- unknowns explicitly catalogued
- critical causal paths traced end-to-end
- predictive tests exist for critical paths
- no material unacknowledged black boxes remain on those paths

## 11. Definition of 100%

100% does not mean omniscience over every instruction in the executable.

100% means that there are no **unacknowledged** black boxes on the machine paths that materially determine the behavior of the AI framework we intend to build.

The final standard is therefore:

> Given a sufficiently specified machine state and input, we can explain and, where experimentally practical, predict what the machine will perceive, evaluate, attempt, execute, mutate, expose, and do next across the relevant layers.

Only after that gate is satisfied should the project proceed to higher-level code/programmer archaeology, general AoE2DE strategy, Byzantine strategy, and finally ByzBot architecture and implementation.
