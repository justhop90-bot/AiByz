# PASS 40 — AEGIS Adaptive Composition Controller Specification

Date: 2026-09-04  
Layer: 2 → capability engineering  
Mission: Convert C1 historical evidence into an implementable AEGIS controller.

## 1. Engineering objective

C1 is graduated from archaeology. The objective is now to build a generalized adaptive composition controller that can operate within AoE2DE `.per` constraints while preserving explicit evidence boundaries.

The cavalry → camel case is the calibration instance, not the architecture itself.

## 2. Governing model

`THREAT VECTOR → CAPABILITY REQUIREMENT → TARGET LEVEL → DEFICIT → HARD CONSTRAINTS → RESPONSE LEVEL → COMMITMENT → AUTHORIZATION → EXECUTION → VERIFICATION → REASSESSMENT`

Historical source establishes the useful decision pattern. The generalized deficit/commitment architecture is an AEGIS invention.

## 3. State separation

AEGIS should conceptually maintain separate channels for:

- observed enemy capability;
- derived threat pressure;
- required counter-capability;
- friendly existing capability;
- capability deficit;
- resource feasibility;
- timing feasibility;
- production commitment;
- execution status;
- verification result;
- confidence / uncertainty.

Do not collapse these into one mutable aggregate merely because `.per` makes compact state attractive.

## 4. State machine

### S0 — OBSERVE
Acquire enemy and friendly measurements.

Output: observation snapshot plus freshness/coverage metadata.

### S1 — CLASSIFY
Map observations into threat vectors.

Example: enemy knight-line pressure contributes to a mounted-threat vector.

Output: threat classification and confidence.

### S2 — REQUIRE
Translate threat into a required counter-capability level.

The requirement is piecewise and contextual, not necessarily linear.

### S3 — DEFICIT
Compute required capability minus verified friendly capability.

`DEFICIT = MAX(0, TARGET - VERIFIED_CAPABILITY)`

The deficit is a planning quantity; it is not itself an order to produce.

### S4 — CONSTRAIN
Apply hard gates before authorization:

- technology availability;
- resource floor / escrow;
- population capacity;
- production availability;
- unit availability;
- military-state restrictions;
- civilization-specific rules;
- existing commitment conflicts.

A failed hard constraint blocks or defers authorization.

### S5 — SCORE / RESPONSE
Select a response level from feasible candidates.

Candidate score should consider:

- deficit reduction;
- resource cost;
- production time;
- timing urgency;
- tactical usefulness;
- strategic risk;
- opportunity cost;
- optionality;
- confidence in threat assessment.

### S6 — COMMIT
Create a bounded production commitment.

Commitment must record conceptually:

- target capability;
- minimum useful persistence;
- activation time;
- invalidation conditions;
- replacement conditions;
- expected completion;
- failure signature.

### S7 — AUTHORIZE
Convert a valid commitment into executable production intent.

Authorization must remain distinct from desire.

### S8 — EXECUTE
Issue or permit the production action through existing AoE2DE production machinery.

### S9 — VERIFY
Confirm world-side postconditions where observable.

Examples: production queue activity, capability increase, technology completion, or other reliable state change.

A requested action is not equivalent to successful completion.

### S10 — REASSESS
Recompute threat, deficit, feasibility, and commitment validity.

Possible transitions:

`MAINTAIN`, `ESCALATE`, `RELEASE`, `REDIRECT`, `RECOVER`.

## 5. Commitment rules

### Activation
Commit only when a candidate clears hard constraints and exceeds the minimum decision threshold.

### Persistence
Do not reverse a commitment solely because the next observation fluctuates within tolerance.

### Invalidation
Invalidate when the threat disappears, prerequisite capability becomes unavailable, the strategic objective changes, or the commitment becomes materially inferior.

### Replacement
A new commitment may supersede an old one only when the new response clears a stronger replacement threshold.

### Recovery
A failed commitment enters recovery rather than immediately oscillating into its opposite.

## 6. Calibration: cavalry → camel

Historical calibration envelope:

`mounted pressure → camel-set ceiling → traincamel authorization → production`

Representative historical pressure/ceiling pairs include:

`4 → <6`, `5 → <8`, `7 → <11`, `10 → <16`, `15 → <24`, `25 → <40`, `40 → <58`.

These values are calibration evidence, not universal AEGIS constants.

AEGIS should convert the historical pattern into:

`enemy mounted threat → required anti-mounted capability → verified camel capability → deficit → feasible camel response → commitment`.

## 7. Anti-oscillation policy

The controller must prevent rapid composition thrashing.

Required mechanisms:

- commitment persistence window;
- hysteresis between activation and release thresholds;
- minimum deficit before escalation;
- confidence decay rather than instant threat deletion;
- replacement threshold above ordinary activation threshold;
- recovery state after execution failure.

Target behavior:

`camel commitment → temporary knight observation loss → maintain commitment`

rather than:

`camel → knight → camel → knight`.

## 8. `.per` implementation strategy

Implement the architecture as compact state channels rather than attempting to create an object-oriented runtime model.

Candidate channel families:

- strategic numbers for measured/derived numeric state;
- goals for discrete state and authority;
- flags for orthogonal boolean conditions;
- timers for persistence, cooldown, and delayed reassessment;
- search state for candidate generation.

Keep semantic roles documented even when physical channels are reused.

Derived channels should be explicitly normalized and restored when a historical-style computation requires phase-scoped transformation.

## 9. Authority boundary

Required lifecycle:

`DESIRE → CAN-FACT → COMMITMENT → AUTHORITY → ACTION → POSTCONDITION`

A desire cannot directly cause a side effect.

A production authorization must be invalidated when its prerequisites cease to hold, subject to commitment persistence rules.

## 10. Verification model

Verification has three levels:

1. Tactical — did the requested capability/action occur?
2. Operational — did the capability change the local military/economic state as expected?
3. Strategic — did the threat/plan state improve?

Failure at any level feeds the reassessment loop.

## 11. Evidence boundary

Historical claims remain tagged as historical/direct/composed/inferred where appropriate.

The following are explicitly AEGIS inventions:

- generalized threat vectors;
- deficit computation as a universal controller quantity;
- explicit commitment object/state semantics;
- hysteresis/replacement policy;
- multi-level verification;
- generalized candidate scoring.

These are engineering improvements inspired by historical mechanisms, not claims about Promisory internals.

## 12. Acceptance criteria

The controller specification is ready for implementation when a `.per` mapping can answer all of these without ambiguity:

- What threat is active?
- How confident are we?
- What capability is required?
- How much verified capability already exists?
- What is the deficit?
- Which hard constraints block action?
- Which response levels are feasible?
- Why is the selected response preferred?
- What commitment is active?
- What authorizes production?
- What observable event verifies execution?
- What invalidates or releases the commitment?
- What happens after failure?

## 13. Engineering disposition

**PASS — architecture specified for implementation.**

The project has crossed the archaeology → capability-engineering boundary for C1.

No further C1 forensic expansion is justified unless new evidence becomes available that materially changes implementation design.

## 14. Next target

Implement the controller's smallest executable vertical slice using cavalry-pressure → camel-capability as the calibration case.

The vertical slice should contain state definition, threat measurement, requirement/deficit calculation, hard feasibility gates, commitment hysteresis, authorization, and a conservative verification/reassessment loop.

Do not build the entire military director at once. Prove one complete adaptive loop, then generalize it.