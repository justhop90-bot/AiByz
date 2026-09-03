# AiByz — Whole-Repository Quality Control

**Date:** 2026-09-03
**Scope:** main repository plus current Layer 1 adapter PR #12 branch
**Formal Layer 1 position:** **89% — unchanged**
**Disposition:** PASS with targeted corrections

## 1. Purpose

This pass audits the repository as an engineering knowledge base rather than reviewing only the newest document. It checks structural integrity, stale claims, internal references, evidence boundaries, current-build scope, the latest adapter branch, and external corroboration relevant to the native scheduler question.

The goal is to find mistakes worth fixing, not to manufacture a higher completion percentage.

## 2. Main-branch integrity result

The current `main` head is `3ecaa2bc3ff4c35b9d42d8068d8fd0369e295d89`.

Static inventory:

- 108 tracked files in the checked-out repository tree.
- 88 Markdown files.
- 10 JSON files.
- 10 JSONL files.
- All 10 JSON files parsed successfully.
- All 211 JSONL records parsed successfully.
- 51 relative Markdown links were checked; 0 were missing.
- No `TODO`, `FIXME`, or `XXX` markers were found in the checked textual corpus.
- No stale `91%` or retired `7,715` claim was found in the checked main tree.

These are repository-integrity measurements, not Layer 1 evidence measurements.

## 3. Adapter PR #12 integrity result

The current PR #12 remains open and unmerged. It has 54 commits and 56 changed files at head `181c23aa3e69ad84311b662b17a51cac3a17847c`.

The branch contains substantially more Layer 1 adapter and native investigation material than `main`, including the scheduler recovery pass, native scenario-entry work, parser qualification, security gates, and the professional handoff.

The branch was audited separately because it is active engineering work and therefore can contain facts or paths not yet present in `main`.

## 4. Concrete defect found and fixed

`07_EXPERIMENTS/AEGIS_LAYER1_LAB/PROFESSIONAL_HANDOFF_2026-09-03.md` on PR #12 referenced:

`07_EXPERIMENTS/AEGIS_LAYER1_LAB/MACHINE_EXPERIMENT_SCHEMA.json`

That path does not exist. The canonical experiment schema is:

`knowledge/MACHINE_EXPERIMENT_SCHEMA.json`

The handoff was corrected on the PR #12 branch. The correction does not change any scientific conclusion.

## 5. Historical RunList signature — QC re-verification

The public historical `FLWL/aoe2-ai-module` project provides an independent architectural lead. Its DE configuration contains a byte signature intended to locate a RunList function, and its `Expert` implementation models the DE call as:

`DetouredRunList(AIExpert* aiExpert, int listId, void* statsOutput)`

The detour invokes the original `FuncRunList(aiExpert, listId, statsOutput)` before processing the project's own command queue. Its DE `AIExpert` model also exposes string, fact, and action tables; its fact model includes type, touched, last-result, argument-count, native function pointer, and argument-type metadata.

This source is historical: its repository source was last pushed in 2021. It is therefore comparative evidence, not 2026 runtime authority.

The RunList signature was re-tested against the exact controlled `AoE2DE_s.exe` using the actual hexadecimal bytes rather than escaped textual byte tokens. The full wildcard signature produced **0 matches**. The earlier intermediate probe that displayed tokens such as `b'\\x40...'` was not a valid byte-pattern test and is not evidence; the corrected test is the one retained here.

Conclusion:

`historical RunList signature -> current executable = no match`

No current-build RunList address is promoted.

## 6. Stronger rule-set evidence from the public scripting reference

The AoE2 AI Scripting Encyclopedia documents two useful runtime-visible commands:

- `up-get-rule-id` returns the zero-based ID for the current rule within the rule set.
- `up-jump-rule` jumps forward or backward within the current rule set.

This independently strengthens the existence of a rule-set execution context and makes the scheduler investigation more concrete. It still does not prove the native scheduler comparator, sorted-list implementation, cursor mutation, or interval transition algorithm.

The same reference documents `chat-trace` as a testing action used to check when a rule executes, and `up-log-data` as a formatted AI log action. These are especially valuable because they suggest a pure-`.per` observation route that does not require XS and may reduce dependence on Scenario Editor automation once a reliable custom-AI load path is established.

## 7. Important methodological correction

The project previously treated the historical RunList signature as a promising current-build scan target. The correct formulation is narrower:

- the historical source establishes that an independent DE AI integration project identified a RunList boundary and associated it with `listId`;
- the historical signature does not survive unchanged into the controlled 2026 executable;
- therefore the signature is a hypothesis generator for structural recovery, not a locator for the current function.

Future scheduler recovery should combine current-build `.pdata` intervals, instruction-level field access, caller/callee topology, and execution evidence rather than signature nostalgia.

## 8. `.ai` terminology cleanup

The repository frequently uses `.ai/.per` as shorthand for the AI substrate. This is understandable in the context of historical material, but it can blur three different things:

1. AI bootstrap/profile or scenario-selection metadata;
2. `.per` / `.per2` rule-program material;
3. native parser/engine state after loading.

The evidence supports the existence of `.per` / `.per2` parsing and rule loading, while native diagnostic material also contains `.ai2` terminology. Future documentation should prefer **“AI bootstrap/profile + `.per`/`.per2` rule material”** when discussing the pipeline, unless a specific `.ai` artifact is the subject.

This is terminology precision, not a new runtime claim.

## 9. Claims that survive QC unchanged

The following remain sound under the evidence discipline:

- exact executable identity is build-scoped;
- `.pdata` is structural function-coordinate evidence, not semantic naming;
- direct string-xref absence is bounded negative evidence;
- persistent-fact evaluation is a named native phase, but freshness/storage semantics remain open;
- native UnitAI exposes order/action/target/notification/search/recovery vocabulary, but exact state ownership remains open;
- historical source is comparative evidence only;
- replay is an observation instrument, not complete native state;
- validator behavior is not runtime proof;
- Scenario Editor automation was a rejected tooling route, not a rejected game feature;
- 7,831 is the qualified reachable-rule corpus statistic and 7,715 is retired;
- Layer 1 remains 89%.

## 10. New engineering implication

The strongest immediate opportunity created by the external cross-reference is a two-stage scheduler strategy:

### Static stage
Recover the current-build rule execution boundary using `.pdata` partitions and candidate object/call relationships. The target is:

`RunList context -> current rule -> eligibility -> ordering -> selection -> interval transition`

### Runtime stage
Once a reliable pure-`.per` loading route is established, use a deliberately instrumented rule set with `chat-trace`, `up-log-data`, and `up-get-rule-id` to make rule execution externally observable without introducing XS.

The runtime probe must still be treated as calibration until the observation channel itself is validated. A trace message proves an action reached the observable command layer; it does not by itself prove every internal scheduler state transition.

## 11. Recommended documentation changes

1. Keep the root README as the stable front door and add this QC record to its navigation list.
2. Add this record to `RESEARCH_INDEX.md` under Layer 1 QC.
3. Keep PR #12's professional handoff path corrected to the canonical experiment schema.
4. When the next native scheduler pass begins, record the historical RunList evidence as comparative provenance rather than current address evidence.
5. Prefer the phrase “rule-set execution context” over stronger claims about a particular scheduler data structure until current-build state ownership is recovered.

## 12. Promotion decision

**No Layer 1 causal proposition is promoted by this QC.**

The repository passes integrity review. One concrete path defect was corrected. One flawed intermediate byte-pattern probe was identified and replaced by a valid re-test. External evidence adds a useful rule-set/run-list lead and a promising pure-`.per` observation strategy, but none closes a P0 causal edge.

**Layer 1 remains 89%.**

## 13. Next pass

The next native pass should remain P0-B:

`current executable -> .pdata function intervals -> AIExpert object evidence -> RunList/loadRules candidate -> rule iteration -> eligibility -> ordering -> selected rule`

Do not reopen broad Scenario Editor automation unless it becomes more discriminating than the pure-`.per` observation route.
