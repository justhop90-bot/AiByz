# Layer 1 Native Archaeology — QC Addendum

## Six-Month Recovery Standard

This addendum is intentionally written as an archival quality-control layer over the native archaeology log. Its purpose is to ensure that the repository can reconstruct the state of knowledge without relying on conversational memory.

A future engineer returning after six months must be able to answer five questions without asking the original investigator:

1. **What do we know?**
2. **How do we know it?**
3. **What did we try that failed?**
4. **What do we still not know?**
5. **What exact experiment should happen next, and what result would change our model?**

A document is considered insufficient if it records conclusions without recording the evidentiary route to those conclusions.

---

## 1. QC finding: preserve the distinction between discovery and interpretation

The native executable contains a rich vocabulary for unit, object, copy, ownership, validity, availability, garrison, enumeration, creation, and unit-AI concepts. This is a substantial discovery.

However, the discovery is not yet an implementation map.

The repository must therefore maintain three separate layers:

**Layer A — Physical observation**

Exact bytes, addresses, strings, symbols, instruction references, structures, and decompiled operations.

**Layer B — Semantic interpretation**

What those observations most likely mean, including explicit uncertainty.

**Layer C — Engineering abstraction**

The stable API/model that ByzBot may safely depend upon.

Promotion from A to B requires an argument. Promotion from B to C requires stronger evidence, normally implementation tracing and/or controlled runtime validation.

This prevents a future engineer from reading a polished abstraction and incorrectly assuming that every component of it was directly demonstrated by the executable.

---

## 2. QC finding: the negative pointer scan is informative but bounded

The completed direct-pointer experiment returned zero exact little-endian 64-bit occurrences for all selected targets, including API signatures and source/debug strings.

The correct conclusion is:

> No tested target was observed as an exact embedded absolute 64-bit pointer in the scanned representation.

The incorrect conclusion would be:

> Nothing references these strings.

The latter does not follow because x86-64 code can reference static data through RIP-relative addressing, indirect tables, computed addresses, hashes, or other structures.

The experiment therefore removes one representation hypothesis while increasing the priority of instruction-level reference recovery.

This distinction must remain permanently attached to the artifact so that the same exhaustive search is not repeated later merely because “the pointer search found nothing.”

---

## 3. QC finding: the signature region itself is now a research object

The API names should no longer be treated as independent strings.

Their co-location and repeated signature format make the surrounding region the more informative archaeological object. The next investigation should characterize:

- boundaries;
- alignment;
- record stride;
- repeated fields;
- nearby constants;
- candidate pointers;
- candidate hashes/ordinals;
- references from executable instructions;
- initialization consumers;
- lookup consumers;
- and dispatch consumers.

The key question is not merely “where is `xsGetUnitObjectId`?” but:

**What native structure contains this entry, who consumes that structure, and how does consumption produce executable behavior?**

That question has a much higher probability of reaching the implementation.

---

## 4. QC finding: use discriminating experiments, not accumulation

Future archaeology should prefer experiments whose possible outcomes imply different architectural conclusions.

For example:

| Experiment | Outcome A | Outcome B | Meaning |
|---|---|---|---|
| RIP-relative scan | References enter signature region | No references | Direct instruction consumer likely / alternative representation required |
| Region stride analysis | Repeating records | Flat byte pool | Structured registry candidate / likely string pool |
| Candidate record inspection | Function-like pointers | No pointer-like fields | Registration structure strengthened / weakened |
| Consumer decompilation | Name-to-function lookup | Diagnostics/introspection only | Dispatch hypothesis strengthened / weakened |
| API trace | Object lookup and field access | Generic wrapper/other subsystem | Identity semantics become concrete / remain unresolved |
| Controlled runtime identity test | Stable conversion | Context-dependent conversion | Namespace relationship characterized |

This is the standard for subsequent work: every experiment should have a stated discriminating purpose before execution.

---

## 5. QC finding: identity must be modeled as a topology, not a field

The term “ID” is dangerously underspecified.

The future world model should assume separate namespaces until evidence proves otherwise. Candidate namespaces include:

- script-visible unit identifier;
- native unit identifier;
- native object identifier;
- object copy identifier;
- game/resource identifier;
- `obj->id`;
- `uniqueID`;
- replay numeric reference;
- strategic identity assigned by the bot.

For each namespace, the research record should answer:

**Domain:** What objects can possess this identifier?  
**Scope:** Is it global, player-local, game-local, object-local, or subsystem-local?  
**Allocation:** Where does the value originate?  
**Lifetime:** When does it become valid and invalid?  
**Reuse:** Can a later object receive the same value?  
**Conversion:** How is it mapped to other identifiers?  
**Persistence:** Does it survive transformation, garrisoning, save/load, or serialization?  
**Observation:** Which interfaces expose it?  
**Failure:** What happens when it is invalid?

This schema turns “object identity research” into a finite set of testable propositions.

---

## 6. QC finding: lifecycle is part of identity semantics

An identifier cannot be understood without understanding the lifetime of the entity to which it refers.

A future implementation must distinguish at least:

`created -> active -> mutated -> transformed/garrisoned/removed`

and must not collapse all non-observation into destruction.

A robust evidence model should distinguish:

- observed alive/active;
- observed transformed;
- observed garrisoned;
- observed removed/destroyed;
- observed ownership change;
- invalid handle/reference;
- not currently observable;
- parser did not decode the event;
- genuinely unknown.

This directly prevents false military accounting and false command recovery.

---

## 7. QC finding: command semantics require a postcondition boundary

The eventual AI architecture must not treat a command as a completed action.

The machine-level contract should eventually be reconstructed as:

`request -> encode -> validate -> dispatch -> execute -> mutate -> expose result`

The bot should then maintain distinct evidence for:

- command issued;
- command accepted;
- command executed;
- state changed;
- intended postcondition achieved.

This is particularly important for object-targeted commands. A command may be syntactically accepted while its intended object has transformed, died, become unavailable, or otherwise changed before execution.

Native identity research is therefore a prerequisite for reliable postcondition adjudication.

---

## 8. QC finding: production is a state machine, not a counter

The native creation vocabulary and replay queue observations imply an important future modeling discipline.

A production event should not be represented as one scalar fact such as “one knight exists in production.” The research model should preserve the possible transitions:

`intent -> command -> admission -> queue -> start -> completion -> object creation -> availability -> deployment -> operational capability`

Not every transition will necessarily be directly observable through every interface. The point is to prevent unsupported collapse of distinct machine states.

This matters later to the Production Director, Force Planner, and evaluation framework because strategic capability should be based on actual machine state rather than optimistic intent accounting.

---

## 9. QC finding: replay provenance must remain lossless upstream

Replay parsing should preserve the raw event before normalization whenever practical.

The preferred pipeline is:

`raw replay bytes -> lossless decoded event -> normalized event -> derived fact -> interpretation -> strategic label`

Each transformation should be attributable to a parser version and methodology.

This is especially important because the current parser intentionally discards some fields and uses best-guess decoding in selected action families. Such output is useful observational evidence but must not silently become machine ground truth.

A future replay corpus should therefore preserve enough provenance to answer:

- Which replay file?
- Which exact bytes?
- Which parser version/source snapshot?
- Which decoder path?
- Which fields were discarded?
- Which fields were inferred?
- Which labels were derived afterward?

This is essential if replay data later becomes a training or evaluation substrate.

---

## 10. Programmer-mind reconstruction protocol

The project objective includes understanding the design logic of the programmer/system builder, but this must not become speculative biography.

Intent should be reconstructed from engineering evidence:

1. implementation structure;
2. callers and callees;
3. data ownership;
4. state lifetime;
5. repeated architectural patterns;
6. error handling;
7. performance-oriented structures;
8. source-name remnants;
9. boundary placement;
10. runtime behavior.

A statement such as “the programmer intended this as an identity abstraction” should therefore be accompanied by the implementation evidence that makes that interpretation stronger than competing explanations.

The repository should prefer:

**“The implementation does X; this constrains Y; therefore interpretation Z is supported.”**

over:

**“The programmer obviously intended Z.”**

That difference is central to maintaining scientific discipline during reverse engineering.

---

## 11. Practical architecture consequences

The Layer 1 findings imply several constraints on later ByzBot architecture.

### World state

The world model should retain evidence provenance and confidence rather than only normalized values.

### Belief state

Beliefs should reference observations and preserve uncertainty. A belief that an enemy army unit is “dead” should identify the evidence that produced that belief and the alternative explanation if identity/lifecycle remains ambiguous.

### Targeting

Target persistence should distinguish stable machine identity from strategic identity. “The enemy knight I was tracking” is a strategic referent; it must not automatically be treated as an immutable native object handle.

### Force composition

Composition accounting should distinguish commanded, existing, available, and operational units.

### Command authority

A high-level decision should not receive implicit authority merely because the corresponding command was emitted. Execution and postcondition evidence must close the loop.

### Recovery

Recovery logic should branch on diagnosed machine state rather than generic failure. Identity/lifecycle semantics are what make this possible.

---

## 12. Six-month reconstruction procedure

A future engineer should be able to reconstruct the project in this order:

### Step 1 — Read the Layer 1 predictive standard

Understand the completion definition, evidence ladder, causal-spine requirement, and black-box rule.

### Step 2 — Read this archaeology log

Understand what the native investigation discovered and what it deliberately refused to claim.

### Step 3 — Inspect the controlled investigation artifacts

Review the generated inventories, negative xref results, native-region evidence, and pointer-scan result.

### Step 4 — Reconstruct the hypothesis register

Know which propositions are established, supported, plausible, or unresolved.

### Step 5 — Reproduce the next experiment

Run instruction-level RIP-relative reference recovery against the known native signature region.

### Step 6 — Promote only demonstrated semantics

Once a candidate consumer is found, trace it through registration/dispatch and into implementation before changing the authoritative identity model.

### Step 7 — Build runtime experiments around unresolved propositions

Especially test identity conversion, lifecycle, transformation, garrisoning, invalidation, and replay correspondence.

### Step 8 — Update the ledger

Every promotion or falsification must update the hypothesis register and the evidence ledger.

The repository should thereby function as a cumulative research instrument rather than a collection of disconnected notes.

---

## 13. Quality-control acceptance criteria

This archaeology record passes QC only if a future reader can determine:

- what executable was investigated;
- which analysis environment was used;
- which methods were attempted;
- which methods failed;
- what each successful method actually demonstrated;
- what the native vocabulary contains;
- why the current interpretation is stronger than alternatives;
- what remains unknown;
- what evidence would promote each unknown;
- how the findings affect future bot architecture;
- and exactly where investigation resumes.

The record must remain useful even if the original conversational context disappears completely.

---

## 14. Final QC assessment

The native investigation is at a productive transition point: vocabulary discovery is substantially established, while implementation semantics remain the principal unresolved layer.

The direct pointer experiment has now been completed and preserved as a bounded negative result. It should not trigger another broad search. The next high-value operation is instruction-level reference recovery into the known signature region, followed by structural reconstruction and one complete API implementation trace.

The central engineering objective remains unchanged:

> **Do not ask the machine what we hope its abstractions mean. Recover what the machine actually does, identify why the architecture is structured that way where evidence permits, and only then build the bot's abstractions on top of it.**

That is the standard required for Layer 1 completion and for a repository capable of restoring the investigator's knowledge after a long absence.
