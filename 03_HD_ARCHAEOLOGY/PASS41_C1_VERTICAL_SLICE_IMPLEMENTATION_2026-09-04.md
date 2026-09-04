# PASS 41 — C1 Vertical Slice Implementation

Date: 2026-09-04  
Layer: 2 → capability engineering  
Mission: Turn the Pass-40 C1 architecture into the smallest bounded runtime candidate.

## 1. Disposition

**PASS — syntax-qualified vertical-slice candidate; runtime qualification remains open.**

The candidate now implements one complete adaptive loop for the calibration case:

`ENEMY KNIGHT PRESSURE → CAMEL REQUIREMENT → VERIFIED CAMELS → DEFICIT → COMMITMENT → AUTHORITY → TRAINCAMEL → VERIFICATION → RECOVERY`

The implementation is intentionally isolated. It does not replace the existing production director, optimizer, or historical `units.per` production machinery.

## 2. Artifact

`05_RUNTIME_CANDIDATE/AEGIS_C1_VERTICAL_SLICE_PASS41.per`

The candidate uses a fresh goal block `3830–3839`. The local goal audit found the existing AD research stack reaching goal 3827, so this block was selected immediately after the known allocation range.

## 3. Measurement design

The calibration slice deliberately avoids the previously identified validator-sensitive combination:

`up-get-focus-fact unit-type-count knight-line`

Instead, enemy knight pressure is measured with the established `players-unit-type-count focus-player knight-line` predicate and compressed into five pressure buckets:

- 4+
- 7+
- 15+
- 25+
- 40+

Friendly camel capability is read with `unit-type-count-total camel-line` into controller state.

This is a conservative calibration adapter, not a claim that the final AEGIS threat model should only observe knights.

## 4. Requirement / deficit

The historical calibration envelope is preserved as target levels:

| Mounted-pressure bucket | Camel target |
|---:|---:|
| 4–6 | 6 |
| 7–14 | 11 |
| 15–24 | 24 |
| 25–39 | 40 |
| 40+ | 58 |

The controller computes:

`DEFICIT = TARGET - VERIFIED_CAMELS`

only when the target exceeds verified capability. Otherwise deficit is zero.

The historical numbers are calibration evidence, not universal AEGIS doctrine.

## 5. Authority boundary

The candidate separates:

`DEFICIT → COMMITMENT → AUTHORITY → traincamel`

Authorization requires:

- positive deficit;
- no active C1 commitment;
- `milunits yes`;
- `food-amount >= cm-buffer-f`.

The module does not directly issue a unit-training command. It sets the existing `traincamel` production-authority goal and leaves execution to the established production machinery.

## 6. Commitment / hysteresis

Once committed, pressure in the 2–3 range does not immediately cancel the response. Release occurs below pressure 2.

This creates the first executable anti-oscillation boundary:

`activate >= 4 → remain committed at 2–3 → release < 2`

The design deliberately does not alternate between camel and knight responses because the current slice has only one capability candidate.

## 7. Verification / failure handling

`traincamel yes` is not treated as proof of success.

The controller re-reads friendly camel capability after the action request. A no-growth observation increments a stall counter. Three consecutive no-growth observations enter the `STALLED` result state and clear C1 commitment/authority.

The three-cycle allowance is intentionally conservative relative to the approximately 22-second camel training interval established from the Byzantine unit data.

This is capability verification, not individual queue-to-spawn identity proof.

## 8. Static validation

The candidate was fetched from the committed GitHub branch and tested with the installed AoE2 AI parser/linter.

### Default profile

Result:

`finding_count: 0`  
`failed: false`

### Corpus profile

The same candidate also passed the corpus profile with exit code 0.

### Line-length check

Maximum observed line length: **81 characters**.  
No line exceeded the 255-character engineering limit.

Temporary validation copies were removed after testing; GitHub remains the canonical artifact store.

## 9. What is now proven

### DIRECT / IMPLEMENTATION

- A bounded C1 state machine can be expressed using current `.per` primitives.
- Enemy knight pressure can be bucketed without the known validator-sensitive `up-get-focus-fact ... knight-line` form.
- Friendly camel capability can be stored as controller state.
- Deficit can be represented separately from production authorization.
- Commitment can be represented separately from authority.
- Existing `traincamel` machinery can remain the execution bridge.
- Capability verification can be separated from command issuance.
- A bounded recovery state can be represented after repeated no-growth observations.

### HISTORICAL / CALIBRATION

The pressure/target pairs come from the recovered HD/Promisory camel-production envelope. Their reuse here is calibration, not proof that AEGIS should permanently reproduce the historical policy.

## 10. What is not proven

- That the current DE runtime will execute this candidate correctly when integrated into the full AI package.
- That the selected pressure buckets are optimal.
- That `players-unit-type-count focus-player knight-line` alone is sufficient for the final mounted-threat vector.
- That a camel-count increase was caused specifically by this controller rather than another production rule.
- That three no-growth observations are the optimal recovery horizon.
- That the historical target values are strategically optimal for Byzantines under current DE balance.

These remain runtime/strategic qualification questions.

## 11. Integration boundary

Do **not** immediately splice this file into the live AI.

The next engineering action is package-level integration analysis:

1. identify the exact load root and load order for the current AEGIS runtime candidate;
2. identify any existing writers of `traincamel` and any reset/priority machinery that can race this controller;
3. wire the C1 module at a controlled authority boundary;
4. run static package validation;
5. perform a minimal runtime experiment if and only if the package can be launched without resurrecting the retired scenario-loader workflow;
6. record observable results as CONTROL / WORLD / STRATEGIC separately.

## 12. Engineering conclusion

Pass 40 specified the controller. Pass 41 now gives that specification a concrete, syntax-qualified implementation candidate.

The important result is not the camel rule itself. It is the executable separation of:

`OBSERVE → REQUIRE → DEFICIT → COMMIT → AUTHORIZE → VERIFY → RECOVER`

That is the first complete AEGIS adaptive decision loop suitable for controlled integration and later generalization to additional capabilities.
