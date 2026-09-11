# AEGIS P0/P1 Remediation & Static Qualification Result — 2026-09-11

## Scope

This record supersedes the unresolved portions of the 2026-09-11 P0/P1 contradiction pass for the findings directly attacked in this remediation cycle. It does **not** promote any module to target-runtime S5 or strategic S6.

Target source contract: AoE2DE `101.103.48987.0` / BuildID `24094652`.

## 1. CR reservation capability binding — REMEDIATED STATICALLY

`AegisProm/AEGIS-production-reservation-authority-v0.per` now requires the CR requested unit to equal the reservation authority's certified spearman capability before the CR grant can enter `RESERVED`:

`aegis-cr-unit == aegis-pr-unit-spearman-line`

This predicate is upstream of the reservation state mutation. A downstream dispatch check is therefore no longer the first place at which the unit/resource relationship is enforced.

## 2. Reservation negative paths — COVERED STATICALLY

The dedicated negative-path suite covers:

- wrong-unit CR request;
- stale authorization generation for reserved and in-flight reservations;
- zero-expiry fail-closed behavior;
- duplicate reservation attempts while the resource is occupied;
- invalid release from active states;
- release identity/generation mismatch;
- repeated release/idempotency;
- reservation rule syntax guard.

The tests remain static contract tests. They do not claim engine rule-firing behavior.

## 3. Military-production selector initialization — REMEDIATED STATICALLY

`AEGIS-military-production-v0.per` now explicitly initializes `aegis-mp-unit` to `aegis-mp-unit-spearman` in its generation initialization rule, before authorization can be reached.

Rationale is bounded by the existing V0 contract: this module's physical production path is exclusively `spearman-line`, and the authorization rule already requires `aegis-mp-unit-spearman`. No camel selector is inferred or silently introduced into the V0 execution path.

The reassessment test was updated to distinguish selector initialization from reassessment ownership. Reassessment remains downstream acknowledgement; it does not select strategy.

## 4. Static-suite infrastructure defect discovered and repaired

The existing GitHub Actions validator workflow invoked `unittest discover`, but the repository's vertical-slice tests are pytest-style functions and were therefore not discovered. The workflow reported `NO TESTS RAN` with exit code 5.

The workflow now installs pytest and runs:

`python -m pytest tests -q`

This converts the workflow from a false-negative/no-discovery harness into the intended complete static qualification suite.

## 5. Additional contradiction exposed by the complete suite

The complete suite exposed an unrelated ACAP cross-record test contradiction: one test claimed that an interior claimed range qualified solely from outer observations, while the validator separately requires each claimed boundary to be directly demonstrated (`EVD-009`).

The test was reconciled to the validator's fail-closed boundary semantics rather than weakening the validator.

## 6. Complete static-suite result

Final GitHub Actions run after reconciliation:

- Workflow: `ACAP and Vertical Slice Validator Tests`
- Run: `#38`
- Run ID: `34638039803`
- Commit: `0bf04190ea2d199c32dee9a2ec719db87e0bcc7b`
- Result: **SUCCESS**
- Test result: **136 passed, 7 subtests passed**
- Runtime: approximately 0.31 s

The separate `AEGIS Policy Checks` workflow also passed on the corresponding commit.

## 7. Qualification interpretation

The static gate is now green for this remediation cycle.

That establishes:

`source contract + static negative-path coverage + repository policy + complete test discovery = PASS`

It does **not** establish:

`target engine loaded + engine accepted + pending lifecycle + world transition + causal attribution = PASS`

Therefore:

- CR reservation unit-binding: **S3/S4 static remediation complete; S5 unproven**.
- Reservation negative-path coverage: **static coverage complete; runtime behavior unproven**.
- Military selector initialization: **S3/S4 static remediation complete; first-load engine behavior unproven**.
- Target-runtime qualification: **BLOCKED**.
- Strategic qualification: **BLOCKED**.
- Production promotion: **NOT AUTHORIZED**.

## 8. Next qualification target

The remaining work should now move from these repaired static contradictions to the controlled **Civilian Production Loop** runtime evidence bundle, while preserving the same negative-path discipline and without promoting the military candidate merely because its static gate is green.
