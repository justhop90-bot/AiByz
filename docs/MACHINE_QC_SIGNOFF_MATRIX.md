# Layer 1 Preservation Signoff Matrix

| Domain | Required artifact | Current state | Remaining proof |
|---|---|---|---|
| Runtime identity | machine contract + fingerprint | documented | revalidate on executable change |
| Loader | loader graph | documented | native call graph closure |
| Script language | grammar model | documented as target | parser-level proof |
| Rules | lifecycle model | documented | native transition proof |
| Scheduler | scheduler model | documented | exact mathematics/fairness |
| Groups | group semantics | documented | activation synchronization proof |
| State | goals/SNs/timers/facts | documented | primitive-level semantics |
| UP | API ledger requirement | specified | complete primitive inventory |
| XS | capability boundary | specified | capability-by-capability qualification |
| Identifier typing | domain ledger | specified | exhaustive API mapping |
| Ranges | context matrix | specified | exhaustive boundary testing |
| Actions | command/postcondition model | specified | primitive-level execution evidence |
| Targets | lifetime model | specified | runtime invalidation tests |
| Pending state | lifecycle model | specified | controlled resource/build tests |
| Failure | fault taxonomy | specified | fault-to-recovery experiments |
| Validation | validator/runtime matrix | specified | systematic divergence corpus |
| Native RE | Ghidra protocol | documented | targeted call-graph closure |
| Provenance | source/binary boundary | documented | preserve new-build deltas |
| Evidence | epistemic statuses | documented | dependency graph integration |
| Reproduction | investigation bundles | specified | package representative cases |
| Replay | state alignment | specified | canonical alignment harness |
| Architecture | authority/verification | specified | implementation traceability |
| Re-entry | independent examination | created | future engineer execution |

## Signoff rule

This matrix is not a claim that every row is fully proven. It is a controlled distinction between preservation completeness and native research completeness. Layer 1 can remain operationally closed while individual evidence rows continue to improve. A row may be marked archival-complete only when the artifact is sufficient for independent re-entry and its unresolved questions are explicit.

## Adversarial review questions

- Is any conclusion stated more strongly than its evidence?
- Is any identifier treated as an untyped integer?
- Is any scheduler behavior inferred solely from naming?
- Is any source artifact being mistaken for shipped runtime implementation?
- Is any validator result being mistaken for runtime truth?
- Is any command treated as successful merely because it was issued?
- Is any stale observation treated as current state?
- Is any consequential state variable missing an owner?
- Is any failure mode missing a recovery interpretation?
- Is any major claim missing a reproducible evidence path?
- Can a contradictory result be represented without rewriting history?
- Can the machine model be regenerated for a new executable build?

A “yes” answer to any defect question means preservation review remains open for that domain.
