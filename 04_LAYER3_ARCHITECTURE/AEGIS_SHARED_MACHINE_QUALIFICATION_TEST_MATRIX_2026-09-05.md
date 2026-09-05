# AEGIS — Shared Machine Qualification Test Matrix

**Date:** 2026-09-05  
**Layer:** Machine Qualification  
**Status:** ACTIVE — NO PRODUCTION IMPLEMENTATION IMPLIED  
**Target build:** AoE2DE `101.103.48987.0` / Steam BuildID `24094652`

## 1. Test philosophy

The objective is not to prove that a command exists. The objective is to prove the exact semantic transition AEGIS intends to rely upon.

Every test records:

`BUILD → INPUT → OPERATION → OBSERVABLE → TIMING → IDENTITY → SCOPE → RESULT → EVIDENCE GRADE`

A parser/validator PASS is necessary for implementation safety but is never sufficient to establish runtime truth.

## 2. Shared test matrix

| ID | Gate | Test | Required observation | Pass condition |
|---|---|---|---|---|
| T01 | Q-01 | Executable fingerprint | hash/version/Steam build | exact target identity recorded |
| T02 | Q-01 | Stock AI closure | recursive load graph | expected untouched stock closure reproduced |
| T03 | Q-02 | Goal low/high boundary | goal reads/writes/comparisons | operation-specific legal range established |
| T04 | Q-02 | SN boundary | strategic-number read/write | current legal range established |
| T05 | Q-02 | Typed identity | unit vs line vs class | invalid substitutions rejected or behavior documented |
| T06 | Q-02 | Fact signature | representative `up-get-*` facts | subject/output semantics match documentation |
| T07 | Q-03 | Stock collision scan | writer/reader map | no AEGIS channel collides with authoritative stock state |
| T08 | Q-03 | Writer uniqueness | repeated publication | exactly one semantic publisher |
| T09 | Q-04 | Generation propagation | successive versions | stale generation cannot authorize current work |
| T10 | Q-04 | Generation initialization | first publication | initial generation semantics deterministic |
| T11 | Q-04 | Generation wrap policy | boundary values | wrap/overflow cannot alias authority silently |
| T12 | Q-05 | Current observation | immediate repeat | current state distinguished from retained state |
| T13 | Q-05 | Stale observation | delayed change | stale evidence remains marked stale/last-known |
| T14 | Q-05 | Scope propagation | player/object/location scope | downstream cannot widen scope silently |
| T15 | Q-06 | Confirmed zero | known empty population | zero remains zero |
| T16 | Q-06 | Search no-result | no matching object | no-result is not silently treated as confirmed global absence |
| T17 | Q-06 | Unsupported query | invalid/unavailable query | unsupported/unknown distinct from zero |
| T18 | Q-06 | Observation gap | deliberately unobserved state | unknown survives publication |
| T19 | Q-07 | Filter isolation | sequential different filters | prior filter state cannot contaminate next query |
| T20 | Q-07 | Search reset | repeated search families | search state reset/qualification documented |
| T21 | Q-07 | Multiplicity | 0/1/many results | result cardinality is attributable |
| T22 | Q-07 | Identity continuity | same object across observations | object identity does not silently alias |
| T23 | Q-08 | Invalid-before-publish | multi-field record | partial record is not consumed as valid |
| T24 | Q-08 | Generation coherence | simultaneous field reads | all published fields belong to same generation |
| T25 | Q-08 | Interrupted publication | forced controller interruption | consumer sees invalid/old coherent record, never mixed record |
| T26 | Q-09 | Can-vs-issue | can-train/can-build/can-research then command | feasibility does not masquerade as acceptance |
| T27 | Q-09 | Queue acceptance | issued action | accepted/queued transition separately observed |
| T28 | Q-09 | Pending lifecycle | pending object | pending is distinct from created |
| T29 | Q-09 | Created lifecycle | completed object | created/available evidence distinct from pending |
| T30 | Q-09 | Availability | usable object | availability is separately evidenced |
| T31 | Q-10 | Cancellation | cancel active work | stale authority cannot resurrect cancelled work |
| T32 | Q-10 | Supersession | new generation | old generation rejected |
| T33 | Q-10 | Partial execution | action interrupted mid-course | partial result preserved without false completion |
| T34 | Q-10 | Retry bound | repeated failure | retry does not become infinite command loop |
| T35 | Q-11 | Shared resource race | two commitments | contention visible to correct authority |
| T36 | Q-11 | Producer race | two demands for one producer | no hidden reservation assumption |
| T37 | Q-11 | Shared contributor | one unit/capability supports multiple requirements | contribution cannot be double-counted silently |
| T38 | Q-11 | Commitment collision | simultaneous commitments | duplicate/contradictory commitments rejected or explicitly resolved |
| T39 | Q-12 | Primitive cost | representative expensive commands | measured runtime cost recorded |
| T40 | Q-12 | Search cost | bounded repeated search | worst-case cost remains within budget |
| T41 | Q-12 | Candidate bound | maximum candidate set | generation/evaluation work bounded |
| T42 | Q-12 | Fast/slow separation | fast loop under slow workload | slow qualification cannot starve control loop |
| T43 | Q-12 | Latency | command-to-observable timing | latency distribution recorded and budgeted |
| T44 | Q-12 | Regression | rerun critical tests after build/update | behavior drift detected before reuse |

## 3. Evidence grades

- **E0 — Direct engine evidence:** controlled observation from the target executable.
- **E1 — Official build/documentation evidence:** authoritative release or engine documentation.
- **E2 — Specialist reference:** high-quality external technical reference such as the AoE2 AI Scripting Encyclopedia.
- **E3 — Project inference:** reasoned architectural interpretation.
- **E4 — Hypothesis:** not safe for implementation.

A qualification gate may consume E1/E2 evidence for orientation, but any gate marked runtime-critical requires E0 before being promoted to implementation-qualified.

## 4. Test result vocabulary

`PASS` — evidence satisfies the criterion.  
`FAIL` — observed behavior contradicts the expected semantic.  
`UNKNOWN` — evidence insufficient.  
`BLOCKED` — test cannot yet be executed.  
`DRIFT` — behavior differs from the recorded build baseline.  
`REOPEN` — result falsifies a load-bearing architectural statement.

## 5. Required record for every executed test

Each result must preserve:

- exact executable/build identity;
- test ID;
- input setup;
- exact primitive/signature used;
- expected result;
- observed result;
- timing/latency where relevant;
- object/player/goal/SN identity;
- generation/scope if applicable;
- screenshots/logs/replay evidence where applicable;
- evidence grade;
- interpretation;
- disposition;
- whether architecture is affected.

## 6. Promotion rule

A primitive or semantic representation moves through:

`DOCUMENTED → STATICALLY SUPPORTED → TARGET-BUILD QUALIFIED → IMPLEMENTED → RUNTIME VALIDATED → REPLAY CORROBORATED → BATTLEFIELD VALIDATED`

No stage may be skipped by confidence, plausibility, or successful parsing.

## 7. Priority

**P1:** T01–T38 where they protect identity, authority, evidence, lifecycle, or cross-system correctness.  
**P2:** T39–T43 performance/latency qualification.  
**Regression:** T44 after every executable/build change affecting AI semantics.

## 8. Exit condition for shared qualification

The shared qualification program is not complete when every test passes. It is complete when every P1 semantic has either:

1. direct target-build evidence and a documented implementation contract; or
2. a formally accepted UNKNOWN/BLOCKED disposition with an explicit architectural consequence and owner.

The second condition prevents uncertainty from being silently converted into implementation truth.
