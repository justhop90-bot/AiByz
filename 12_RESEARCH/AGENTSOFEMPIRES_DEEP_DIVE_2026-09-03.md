# AgentsOfEmpires — AEGIS Archaeological Deep Dive

**Date:** 2026-09-03  
**Project:** AEGIS / AiByz  
**Layer:** Layer 1 — Machine Understanding  
**Source specimen:** `MaxRobinsonTheGreat/AgentsOfEmpires`  
**Disposition:** High-value external behavioral/reference corpus; not production runtime authority  
**Layer-1 position after this pass:** **89% — unchanged**

---

## 1. Executive assessment

`AgentsOfEmpires` is unusually valuable to AEGIS because it combines a large real-world `.per` corpus, an executable experimental harness, strategy variants, replay analysis, parser/reference data, and a written record of failed and successful experiments. Its principal value is therefore not hidden native code. Its value is the experimentally observed relationship between AoE2 AI-script constructs and gameplay outcomes.

The most important new provenance result is that the repository's `docs/Promisory` source was compared against the Promisory directory installed on the controlled Weebo machine and all **36 checked files matched with zero differences**. This creates a direct source-to-installed-corpus bridge for the controlled environment. It does not make the repository authoritative for native implementation, but it elevates its current-Promisory behavioral observations substantially above an ordinary historical script collection.

The repository should therefore be treated as a **behavioral specification and experiment corpus**. Its native-extension or GUI-automation mechanisms are not candidates for the AEGIS production runtime.

---

## 2. Corpus scale and composition

A local inventory of the specimen found approximately:

- 293 non-Git files;
- 198 `.per` files;
- approximately 18.8 MB of `.per` source;
- approximately 24.9 MB across the non-Git corpus;
- 32 duplicate-content groups;
- multiple Promisory-derived strategy trees.

The four principal strategy forks examined were `strat_pure_promi`, `strat_deep_hunter`, `strat_deep_fortress`, and `strat_backline_reaper`.

The duplicated dependency trees are not wasted duplication from an archaeological perspective. They create quasi-controlled variants: a common baseline can be held fixed while a narrow strategy layer is changed. That makes the repository useful for causal comparison of script behavior.

Major Promisory modules are large stateful rule systems. The most substantial include `units.per`, `tsa.per`, `buildings.per`, `init.per`, `general.per`, `researches.per`, `gatherers.per`, `customConstants.per`, `interaction.per`, and `orb.per`. Their combined scale demonstrates that practical `.per` AI is a distributed control system rather than a short collection of independent attack rules.

---

## 3. Current-build provenance bridge

### Observation

The repository's `docs/Promisory/*.per` corpus was compared against the installed Promisory source under the controlled AoE2DE AI directory on Weebo.

### Result

**36 files checked; 0 mismatches.**

### Interpretation

This is direct machine evidence that the examined Promisory source corpus is identical to the corresponding installed files on the controlled machine at the time of comparison.

### Boundary

This proves file identity for the compared files. It does not prove that repository comments, experimental conclusions, or inferred native mechanisms are correct. It also does not imply that the entire repository is current, nor that all native code represented by the executable corresponds to the repository's historical assumptions.

### AEGIS classification

**Evidence grade: A+ for file identity; B/B+ for semantic corroboration; not native implementation authority.**

---

## 4. Revised conceptual model of the `.per` substrate

The corpus supports a stateful model more accurately represented as:

```text
.per source
  -> loader / preprocessor environment
  -> rule and symbol representation
  -> facts and feasibility checks
  -> goals / strategic numbers / timers
  -> search and DUC state
  -> rule-control transitions
  -> native action handlers
  -> unit/group/game state
  -> subsequent evaluation
```

This is deliberately a behavioral abstraction. It does not assert the exact C++ class structure of the current executable.

The corpus repeatedly combines:

- facts;
- actions;
- goals;
- strategic numbers;
- timers;
- DUC search state;
- temporary context changes;
- rule jumps;
- group state;
- target selection;
- stance and formation changes.

Consequently, treating a `.per` program as a purely stateless `IF fact THEN action` list is an inadequate engineering abstraction for sophisticated AI behavior.

---

## 5. DUC/search is a first-class computational subsystem

The corpus contains thousands of uses of DUC operations, including search reset, local/remote search, search-state retrieval, target selection, object filtering, and target-object actions. The exact corpus counts are duplicated-source counts and should not be interpreted as unique semantic operations.

The important structural observation is the repeated pattern:

```text
reset search
  -> construct candidate set
  -> filter / sort
  -> inspect search state
  -> choose target
  -> construct or distribute an action
```

The reference data bundled with the specimen describes `up-get-search-state` as writing multiple search counters into consecutive goals. The corpus uses high-numbered goal blocks for this purpose. This demonstrates a practical technique for serializing DUC state into the AI goal namespace.

### AEGIS consequence

Search state should be modeled as explicit mutable engine state with a defined lifetime, not as an implementation detail that disappears at the end of a single command.

---

## 6. Cross-rule search-state lifetime

The repository's experimental notes report that search results can persist across rules within an effective pass unless explicitly reset. This is why the corpus repeatedly begins independent DUC operations with a full search reset.

This is important evidence for state-lifetime analysis:

```text
rule A
  modifies search state
       |
       v
rule B
  can observe or reuse that state
```

unless an explicit reset or replacement occurs.

### Evidence status

**Behavioral evidence: strong corroboration.**

It does not by itself establish the exact native scheduler boundary or the exact storage object. Those remain current-build native questions.

---

## 7. Search semantics: class versus concrete type

One of the most valuable controlled failures in the corpus concerns searches for siege units. A concrete type-based search did not behave as expected in the test scenario, while class-based searches successfully identified the intended objects.

The corrected experimental pattern used broader classes such as siege-weapon and archery classes. The experiment produced an explicit runtime marker indicating that the intended dive controller had acquired targets.

This gives AEGIS a useful namespace rule:

> A numeric object identifier, unit-line identifier, class identifier, and search semantic are distinct concepts even when their representations are all integers.

### Engineering consequence

Never infer equivalence from numeric representation. Validate the semantic namespace of every DUC parameter independently.

This aligns with AEGIS's existing distinction between concrete unit IDs, unit-line IDs, class IDs, facts, goals, and strategic numbers.

---

## 8. `up-target-objects` reveals a compound native boundary

The repository's scripts and reference material show that target-object actions can combine:

1. a local candidate set;
2. a remote candidate set;
3. a selected target or target distribution policy;
4. local-unit grouping;
5. formation selection;
6. stance selection;
7. native order submission.

Therefore the semantic boundary is not simply:

```text
find target -> issue order
```

but closer to:

```text
local search
  + remote search
  + target-selection state
  + grouping
  + tactical parameters
      -> native action construction
      -> unit order state
```

This makes `up-target-objects` a particularly valuable candidate for future native archaeology because it potentially crosses from DUC state into native unit-control state.

---

## 9. Rule ordering and order overwrite

The repository's experiments report that an earlier `attack-now` action can be overwritten by a later DUC order in the same effective execution context. This is not sufficient to prove lexical-order scheduling of all rules.

The defensible proposition is narrower:

> Competing unit-order mutations can be order-sensitive, and a later applicable action can replace an earlier native order in the observed execution context.

This is useful scheduler evidence because it constrains possible models without prematurely choosing one.

It is compatible with several possibilities, including sequential rule execution, multiple scheduler passes, action queue replacement, or other native mechanisms. Current-build native evidence is still required to distinguish them.

---

## 10. Rule jumps imply nontrivial control flow

The Promisory corpus uses rule-jump primitives extensively. Experimental notes also report that appending a rule to the end of a large module can fail to produce the expected behavior because internal control flow can bypass that region.

This means a `.per` module should not be modeled solely as a flat ordered list. A more useful abstraction is:

```text
rule/control position
       |
       +--> condition evaluation
       |
       +--> action/state mutation
       |
       +--> control transition
       |
       +--> another rule region
```

This is especially important for AEGIS because it explains why seemingly valid appended probes can produce negative results without proving that the command or subsystem is broken.

---

## 11. Timers are state, not merely time comparisons

The corpus uses timers as explicit control mechanisms and reports practical interaction between timers already consumed by Promisory and timers added by experimental strategy layers.

The bundled reference models timer operations around states such as enabled/running, triggered, and disabled. The experiments reinforce the need to treat timers as engine-managed state with lifecycle semantics.

### AEGIS consequence

Future native archaeology should seek:

```text
create/enable timer
  -> timer state
  -> trigger condition
  -> rule eligibility
  -> trigger consumption/rearm
```

rather than treating `(timer-triggered X)` as a simple pure fact.

---

## 12. Goals and extended state

The corpus uses high-numbered goals as structured scratch/state storage, including blocks used to receive multiple outputs from one command. The search-state example is especially clear: one starting goal can represent a contiguous state record whose neighboring goals receive related counters.

This suggests that the goal namespace is not merely a collection of strategic scalar variables. It can act as a compact script-visible state memory.

### AEGIS consequence

The persistent-state investigation should distinguish at least:

- ordinary strategic state;
- scratch goals;
- extended goal blocks;
- fact results;
- search-state outputs;
- timer state;
- native object state.

These may have different lifetimes even though `.per` exposes them through related primitives.

---

## 13. Focus-player context behaves like a temporary execution context

The corpus contains repeated patterns that save the current focus-player value, replace it with a target player, execute a remote search or related operation, and restore the previous value.

Abstractly:

```text
save context
  -> switch focus
  -> perform context-sensitive operation
  -> restore context
```

This is evidence that focus-player state is semantically significant to operations rather than merely descriptive metadata.

### AEGIS consequence

The machine model should represent focus/target player selection as mutable context with ownership and lifetime, and should not treat it as a passive label attached to a rule.

---

## 14. Pure Promisory experiment

One of the strongest strategy experiments compares a minimal top-level loader with increasingly specialized tactical overlays.

The minimal successful configuration essentially preserved Promisory and corrected the target/focus-player context. The repository records a final 15-game comparison in which the pure-Promisory configuration won **14–1**, while a more interventionist tactical variant won **9–5**.

The result is strategically interesting, but its engineering value is greater:

> Adding a controller can reduce system performance when the baseline native/script subsystem already contains effective control logic.

This supports a general AEGIS design principle:

> **Prefer observation, parameter correction, and narrow intervention over replacing an existing subsystem whose state ownership and interactions are not yet understood.**

The result is not proof that the same score will recur in another matchup or build. It is evidence about the tested experimental configuration.

---

## 15. Deep Hunter as a negative causal experiment

A more elaborate strategy attempted a cavalry/siege interaction. Its intended siege behavior did not actually execute because the target search mechanism was semantically mismatched to the scenario.

The important lesson is not the strategy result. It is the causal debugging sequence:

```text
intended behavior
  -> implementation
  -> no observable marker
  -> isolate search mechanism
  -> identify namespace mismatch
  -> replace with class-based search
  -> obtain explicit runtime marker
```

This is a model AEGIS should emulate for experimental engineering.

A favorable game result must never be attributed to a subsystem until the subsystem's critical behavior has been independently observed.

---

## 16. Production-layer interference

Older Arabia experiments in the corpus show another important systems phenomenon: adding a Feudal military-training layer could starve the baseline age-up/resource system.

This is a direct demonstration of resource-policy interference:

```text
new production demand
  -> resource consumption
  -> altered economic state
  -> age-up or baseline objective delayed
  -> downstream tactical plan never reaches intended state
```

This is strong support for an AEGIS Production Director based on deficits, opportunity cost, prerequisite chains, and baseline strategic obligations rather than simple unit quotas.

---

## 17. Strategy packaging exposes a loader semantic

The repository's packaging utility copies the Promisory dependency tree into a strategy-specific namespace and rewrites internal load references. The motivation is to prevent AoE2's AI-root loading behavior from resolving the package as if each included file had ordinary source-relative module semantics.

This yields a useful behavioral proposition:

> Script load resolution is sufficiently rooted in the game's AI search environment that package isolation requires explicit namespace rewriting.

The packaging code is not evidence of the parser's internal implementation, but it is a useful experiment-backed constraint for generated AEGIS `.per` packages.

---

## 18. Experimental harness assessment

The repository's GUI harness contains practical Windows foreground-window management because the game must remain interactable during automation. This confirms an important distinction for AEGIS:

> GUI automation is an adapter/harness concern, not a substitute for native causal evidence.

The harness also contains at least one material safety defect: its documented AI-file backup path writes a placeholder rather than preserving the original file contents. This means the harness should not be treated as production-safe file-management infrastructure without correction.

The harness's replay/result interpretation also correctly distinguishes between attempted commands and surviving game state. That separation is worth retaining in AEGIS experiment design.

---

## 19. Replay analysis value

The repository's recording analysis reconstructs observations such as game duration, players, civilizations, AI names, resignations, age transitions, queue/build/research/market commands, and chat. It explicitly treats many commands as attempts rather than proof of persistent state.

This reinforces AEGIS's replay rule:

```text
replay observation != complete native state
command event != guaranteed execution success
execution success != strategic success
```

The repository is therefore useful as an observation methodology specimen, but replay parsing remains below native executable evidence in the AEGIS hierarchy.

---

## 20. Current native archaeology implications

AgentsOfEmpires changes the order in which AEGIS should attack the executable.

Repeated broad searches for individual `UPGetFact*` names have diminishing returns because decorated names and lambda metadata do not directly identify the native fact body.

The behavioral corpus instead gives discriminating structures to search for:

### P0 candidate A — DUC state machine

```text
reset search
 -> local/remote search
 -> filtering/sorting
 -> search-state export
 -> target selection
 -> target-object action
```

### P0 candidate B — goal-state store

```text
set/read goal
 -> contiguous extended-goal state
 -> fact/search/timer consumers
```

### P0 candidate C — timer state machine

```text
enable
 -> running
 -> triggered
 -> consumed/rearmed/disabled
```

### P0 candidate D — rule-control/jump machinery

```text
current control position
 -> eligibility
 -> rule selection
 -> jump/continue
```

### P0 candidate E — DUC-to-UnitAI bridge

```text
search state
 -> target selection
 -> grouping/formation/stance
 -> native order mutation
 -> CurrentOrder / CurrentAction
```

These are now better-defined native targets than a generic search for fact names.

---

## 21. Relationship to historical AIExpert evidence

The historical `FLWL/aoe2-ai-module` specimen supplies an implementation-facing hypothesis involving an `AIExpert` object, fact/action collections, a run-list boundary, and fact-function metadata. AgentsOfEmpires supplies a large current-Promisory consumer corpus that exercises the semantic surfaces such a native architecture would have to support.

The two sources therefore complement one another:

```text
historical native specimen
  -> candidate internal architecture

AgentsOfEmpires
  -> behavioral constraints on what the architecture must accomplish

current AoE2DE executable
  -> authority for whether the proposed architecture actually exists now
```

This is the correct evidentiary direction. Neither external source should be promoted to current-native truth without an executable anchor.

---

## 22. Evidence matrix

| Proposition | Evidence | Grade | Current-native status |
|---|---|---|---|
| Promisory corpus is large and stateful | local source inventory | A | Corroborated |
| Repository Promisory matches installed Promisory | 36/36 exact file comparison | A+ | Direct current-machine evidence |
| DUC is central to practical AI behavior | source corpus + reference data | A/B+ | Semantics corroborated |
| Search state can persist across rules without reset | recorded experiments | B+ | Native boundary open |
| Class/type search semantics differ | controlled experiment | A | Current behavioral constraint |
| Target-object action crosses search and unit-control domains | source/reference semantics | B+ | Native bridge open |
| Competing orders can overwrite one another | recorded experiment | B+ | Scheduler mechanism open |
| Rule jumps create non-flat control flow | source + experiment | B+ | Native implementation open |
| Timers have lifecycle state | source/reference + experiments | B+ | Native implementation open |
| Extended goals can encode structured state | source/reference | A/B+ | Storage implementation open |
| Focus player is meaningful execution context | source corpus | B+ | Native implementation open |
| Pure Promisory + context correction outperformed custom controller in test | tournament record | A experimental | Strategy evidence only |
| Historical AIExpert/run-list model exists | external historical source | B+ | Not current-native authority |
| Current scheduler implementation recovered | none | D | **Open** |
| Current persistent-fact lifecycle recovered | none | D | **Open** |
| Current rule-to-action bridge recovered | none | D | **Open** |
| Current action-to-UnitAI mutation recovered | none | D | **Open** |
| Current failure/recovery propagation recovered | none | D | **Open** |

---

## 23. What this pass does not establish

This pass does not establish:

- the exact current scheduler comparator;
- whether lexical file order is the primary scheduler order;
- persistent-fact refresh cadence in the current executable;
- exact current `AIExpert` object layout;
- exact current `RunList` address or ABI;
- exact native fact-dispatch table;
- exact `CurrentOrder -> CurrentAction` mutation path;
- exact failure/invalidation propagation;
- exact ownership/lifetime of all search structures;
- an end-to-end predictive causal path through the current executable.

Those remain Layer-1 completion-gate items.

---

## 24. AEGIS architectural deductions

The strongest engineering deductions from the specimen are:

1. **Preserve native/script subsystems until their state ownership is understood.**
2. **Treat DUC as a computational subsystem, not a convenience API.**
3. **Treat search state, timers, goals, and focus context as state with explicit lifetime.**
4. **Keep identifier namespaces distinct even when their storage representation is numeric.**
5. **Use controlled A/B experiments rather than attributing wins to unobserved mechanisms.**
6. **Prefer narrow parameter correction before invasive tactical replacement.**
7. **Make experiment harnesses observable and fail loudly when an intended action does not execute.**
8. **Separate replay observations from native-state claims.**
9. **Use external implementations to generate discriminating hypotheses, never as automatic current-build authority.**
10. **Build AEGIS around a small verified `.per` runtime surface while keeping archaeological tooling offline.**

---

## 25. Final Layer-1 disposition

The AgentsOfEmpires investigation materially strengthens the evidence base, particularly around current Promisory provenance, DUC/search semantics, state lifetime, control-flow behavior, experimental methodology, and strategic-system interference.

It **does not close the implementation-level causal gaps** that define the remaining Layer-1 completion gate.

Therefore the official Layer-1 position remains:

> **89% — investigation closed for handoff; completion gate unsatisfied.**

The percentage is intentionally not increased merely because the evidence corpus became richer. The remaining work requires native causal closure, not additional documentation volume.

---

## 26. Recommended next native pass

Use the behavioral constraints from this specimen to search the current executable for:

```text
DUC reset
  -> search state
  -> target selection
  -> target-object dispatch
  -> native order mutation
```

in parallel with:

```text
timer lifecycle
  -> rule eligibility/control position
```

and:

```text
goal/fact result storage
  -> later rule consumer
```

The first verified current-build causal edge among these is worth substantially more than another broad vocabulary scan.

---

## 27. Fair-use and provenance policy

This document is an original AEGIS analysis. It paraphrases observations, summarizes public technical behavior, and records AEGIS-generated measurements and interpretations. It intentionally avoids reproducing source files, large code passages, proprietary executable contents, or repository prose verbatim.

External projects remain credited as research specimens. Their licenses and project-specific terms govern their own source distributions. AEGIS uses the ideas and experimentally relevant observations as research evidence while keeping production `.per` code independently authored and subject to the AEGIS evidence and licensing policy.
