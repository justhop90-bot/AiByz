# AEGIS — Next AI Engineering Handoff

**Date:** 2026-09-03 17:10 ET
**Project:** AiByz / AEGIS
**Role being handed off:** Lead engineer / Layer 1 machine-reconstruction engineer
**Current Layer 1 position:** **89%**
**Investigation phase:** closed; continuation is explicitly permitted
**Runtime architecture constraint:** pure `.per`; **XS is not part of ByzBot**
**Controlled build:** AoE2DE 101.103.48987.0 / #180059 / Steam 24094652
**Controlled executable SHA-256:** `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`

## 1. WHO

You are the next AEGIS engineer. Treat this as a professional reverse-engineering and causal-reconstruction project, not a bot-writing exercise. The objective is to learn the actual AoE2DE AI machine well enough that ByzBot can exploit it without depending on folklore, historical assumptions, validator behavior, or guessed engine semantics.

The previous engineer has deliberately stopped at 89% rather than manufacturing closure. Your job is to attack the remaining implementation-level causal gaps and promote claims only when evidence crosses the project promotion standard.

## 2. WHAT

Recover the native causal chain behind the `.per` AI runtime:

`AI file -> parser/loader -> rule representation -> facts -> scheduler -> rule selection -> action/handler -> UnitAI mutation -> execution -> failure/recovery -> next decision`

Priority order is P0-B scheduler, P0-A persistent facts, P0-C rule-to-action dispatch, P0-D UnitAI mutation, P0-E failure/recovery, then temporal/identity/determinism closure.

The end state is not merely descriptive. For critical mechanisms we need predictive state transitions: given a sufficiently specified precondition and input, predict the next meaningful machine state and then falsify that prediction.
## 3. WHEN / WHERE

All current native conclusions are scoped to the exact controlled executable above. Re-verify the executable hash before any new native conclusion. Local lab root:
`C:\Users\justh\Desktop\AEGIS-AI-LAB\_adapter_qc`

Primary evidence lives under:
- `docs/` — durable architecture, QC, and handoff records
- `knowledge/` — machine facts and investigation history
- `07_EXPERIMENTS/AEGIS_LAYER1_LAB/` — executable/scenario/harness experiments
- `03_HD_ARCHAEOLOGY/` — historical/HD comparative reconstruction

The GitHub repository is `justhop90-bot/AiByz`. Current working branch:
`lab/aoe2de-adapter-2026-09-03`

PR #12 is the adapter continuation and depends on PR #11's harness-bootstrap base. Do not merge either merely because it is mergeable; preserve the dependency and evidence review.

## 4. WHY

The project already has a strong semantic map but lacks causal closure at the exact places where a bot implementation would otherwise make dangerous assumptions. The remaining 11% is therefore disproportionately valuable: scheduler order, fact freshness, action dispatch, UnitAI state mutation, and failure/recovery determine whether an apparently brilliant `.per` design actually behaves as intended.

Do not increase 89% because you found more strings, commands, rules, or source references. Increase it only when a defined causal proposition closes under the Layer 1 promotion standard.

## 5. CURRENTLY ESTABLISHED

- Native `AIExpert` subsystem and game-load construction exist.
- Native `.per/.per2` loading grammar and rule-list concepts exist.
- Native persistent-fact evaluation phase exists.
- Native player AI identity and scenario AI-rule data structures exist.
- Native scenario AI resolution / embedded-vs-loose AI concepts exist.
- Native UnitAI vocabulary exposes order, action, target, notification, search, completion, failure, invalidation, and retry concepts.
- `.pdata` supplies a mechanically bounded current-build function-coordinate layer.
- Exact-build direct runtime startup, background operation, and AI diagnostic logging are established.
- Automated Scenario Editor interaction is shelved as a primary route.
- Internal test-harness activation is shelved; its existence is evidence, not permission to use undocumented interfaces.
## 6. CRITICAL NEGATIVE KNOWLEDGE

Never repeat these shortcuts:

1. Strings are not call-graph edges.
2. Raw `VA - imagebase` is not a universal file offset.
3. Ghidra repair-heavy functions are not automatically trustworthy.
4. A metadata pointer to a valid function is not semantic ownership.
5. Zero direct xrefs does not prove absence.
6. Replay object IDs do not automatically equal native identity IDs.
7. Validator acceptance/failure is not runtime semantics.
8. Historical source is comparative evidence, not current-build proof.
9. More rule counts do not prove scheduler execution counts.
10. A successful process launch is not a successful game-state experiment.

## 7. NEW COMPARATIVE LEAD — USE CAREFULLY

The public historical `FLWL/aoe2-ai-module` source is useful as a hypothesis generator. Its DE branch models a `RunList(AIExpert*, int listId, void* statsOutput)` boundary and dynamically resolves the DE RunList by signature. It also models AIExpert fact/action/string tables and an AIFact record containing `type`, `touched`, `lastResult`, `argc`, `factFn`, and argument-type fields.

This is valuable because it gives a concrete shape for candidate searches. It is **not** permission to transplant addresses or assume the 2021 structure is unchanged in build #180059.

The historical RunList signature was tested against the exact current executable and produced **zero matches**. Treat that as a rejected current-address hypothesis, not as evidence that RunList disappeared.

The historical source also shows a useful experimental seam: its wrapper calls the native RunList and then processes a command queue. That reinforces the priority of recovering the native rule-list boundary before designing an external scheduler model.

## 8. MOST IMPORTANT CURRENT-BUILD RESULT

Current executable string targets for `loadRules`, persistent-fact diagnostics, scenario AI identity, and scenario AI-rule data were located, but corrected `.text` RIP-relative scans and exact 64-bit pointer scans did not produce direct executable references to those raw string addresses.

Generic RCX-field patterns were also rejected as insufficient because candidate functions touched many unrelated offsets. Therefore **no current function address is promoted** for RunList, loadRules, or scheduler execution.

The current preferred method is:

`PE .pdata boundaries -> candidate function body -> object-field pattern -> call/callee structure -> state ownership -> runtime/log corroboration -> falsification`

Do not reverse this order by starting from a desired function name and forcing a candidate to fit.
## 9. FIRST MISSION

Start with **P0-B native scheduler recovery**.

Do not return to Scenario Editor automation unless a new independent reason appears. Do not activate the internal test harness. Use static PE-aware archaeology and ordinary supported runtime/logging first.

Immediate target chain:

`AIExpert construction -> loadRules -> rule-list storage -> rule metadata -> RunList/scheduler entry -> eligibility -> ordering/comparator -> selected rule -> interval transition`

For every candidate function, record: RVA/VA, `.pdata` interval, size, calling convention hypothesis, register/stack evidence, object pointer evidence, relevant field offsets, calls made, callers found, strings/data touched, confidence, and rejection reasons.

Build a reverse index from `.pdata` function starts to all known function-pointer storage sites. Prioritize dense pointer tables and clusters associated with AIExpert-related data, but require semantic corroboration before attribution.

## 10. SECOND MISSION

In parallel, attack **P0-A persistent facts** at the native mutation boundary:

`fact registration -> evaluator -> result write -> persistent storage -> later read -> invalidation/refresh -> rule consumer`

The native diagnostics `Evaluating Persistent Facts`, `Fact[%d] evaluated persistently to %s`, and `Finished Evaluating Persistent Facts` are orientation markers only. Find the actual instructions that write/read the result and tie them to the AIExpert object before claiming cache semantics.

The historical AIFact layout is a search lead, not a recovered current structure.

## 11. THIRD MISSION

Then recover **P0-C rule-to-action dispatch** and **P0-D UnitAI mutation**:

`selected rule -> action representation -> action handler -> native order request -> CurrentOrder -> CurrentAction -> execution`

Use existing native UnitAI vocabulary and `.pdata` boundaries. The decisive evidence is a real state mutation or an unambiguous call/data relationship, not another string cluster.
## 12. EXPERIMENTAL STANDARD

Use the project experiment schema:
`question -> prior evidence -> competing hypotheses -> discriminating test -> exact setup/build -> raw observation -> interpretation -> confidence -> promotion/rejection -> repository artifact -> next test`

A runtime experiment must specify independent variable, controls, dependent observations, expected outcomes, confounders, commands, artifacts, and falsification criteria. Infrastructure success never counts as causal proof.

For scheduler work, high-value controlled hypotheses include:
- lexical-order execution versus priority-order execution;
- stable sort versus dynamic resort after mutation;
- interval gate evaluated before or after rule eligibility;
- one rule/list pass versus multiple passes per AI update;
- persistent fact read-before-refresh versus refresh-before-read;
- rule disabling/removal mutating the active list immediately versus at a boundary.

Do not infer the answer from stock Promisory ordering. Design tests that make competing models predict different outcomes.

## 13. REPOSITORY DISCIPLINE

Every meaningful result gets a dated report and, where appropriate, an atomic record in `knowledge/`. Supersede old claims explicitly. Preserve failed approaches and their reason for rejection. Never overwrite historical evidence merely to make the repository look cleaner.

Before final handoff, verify:
- exact executable hash;
- clean Git status or explicitly documented intentional artifacts;
- all new reports committed;
- branch/PR head synchronized;
- no temporary probe files accidentally promoted;
- no unsupported Layer 1 percentage change;
- security standard still passes.

## 14. SECURITY / AUTHORIZATION

Operate only on the authorized machine and ordinary game/modding surfaces. No DLL injection, executable patching, hooks, debugger attachment, memory modification, arbitrary internal test-harness protocol use, or security bypass. Undocumented internal strings are archaeology evidence, not an authorization grant.

Keep game installation read-only during experiments where practical; write outputs under the isolated lab root. Fail closed on build mismatch, provenance mismatch, timeout ambiguity, or contaminated controls.

## 15. DEFINITION OF SUCCESS

Do not declare Layer 1 100% because the bot works well. Declare causal closure only when the evidence supports the machine proposition itself.

The remaining completion gate is satisfied when the major P0 chains are sufficiently reconstructed to make testable predictions and at least one critical `.per` path is predicted and experimentally falsified/confirmed end-to-end.

Until then: **Layer 1 = 89%.**

## 16. FINAL INSTRUCTION TO THE NEXT AI

Take initiative. If a better discriminating experiment, static-analysis route, source cross-reference, or evidence-preservation step appears, execute it rather than waiting for permission, provided it stays inside the security boundary. The goal is not to continue the previous engineer's exact plan; the goal is to close the machine's remaining causal gaps with the strongest evidence available.

Start by reading this handoff, `docs/LAYER1_FINAL_INVESTIGATION_HANDOFF_2026-09-03.md`, `docs/OPEN_NATIVE_QUESTIONS_LAYER1.md`, `docs/LAYER1_PREDICTIVE_MACHINE_STANDARD_2026-09-02.md`, the current scheduler pass, and the `.pdata`/AIExpert archaeology. Then produce a concrete evidence-ranked workboard and attack the highest-information unresolved edge.

Do not restart the project. Do not redesign ByzBot yet. Learn the machine first.
