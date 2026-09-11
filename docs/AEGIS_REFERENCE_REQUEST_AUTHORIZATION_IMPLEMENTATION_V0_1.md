# AEGIS Reference Request/Authorization Implementation V0.1

**Status:** NORMATIVE IMPLEMENTATION TEMPLATE
**Reference slice:** Worker Economic Tasking
**Scope:** `main/AegisProm` pure `.per` source
**Purpose:** Define the implementation pattern that the remaining registered vertical slices must adopt without weakening their capability-specific semantics.

## 1. Implemented reference boundary

The Worker Economic slice now carries one request identity from economic arbitration through worker selection, physical task authorization, physical dispatch, and verification.

```text
civilian/economic observation
    ↓
economic demand arbitration
    ↓
REQUEST_ID
    ↓
worker target selection
    ↓
REQUEST_ID preserved
    ↓
worker task command
    ↓
AUTHORIZATION_ID + AUTHORIZATION_GENERATION + AUTHORIZATION_VALID
    ↓
physical target-objects command
    ↓
authorization consumed
    ↓
worker task verification
    ↓
REQUEST_ID / AUTHORIZATION_ID preserved
    ↓
world-state observation
```

## 2. Ownership

| Concern | Authoritative owner | Reference symbol |
|---|---|---|
| Economic request identity | Economic demand arbitration | `aegis-eda-request-id` |
| Worker request identity | Worker target selection | `aegis-wts-request-id` |
| Execution request identity | Worker task command | `aegis-wtc-request-id` |
| Authorization identity | Worker task command | `aegis-wtc-authorization-id` |
| Authorization generation | Worker task command | `aegis-wtc-authorization-generation` |
| Authorization validity | Worker task command | `aegis-wtc-authorization-valid` |
| Authorization expiry marker | Worker task command | `aegis-wtc-authorization-expiry` |
| World-state verification identity | Worker task verification | `aegis-wtv-request-id`, `aegis-wtv-authorization-id` |

No downstream module generates a replacement request identity.

## 3. Request identity rule

The reference implementation uses the originating arbitrated demand generation as the request identity.

This is a deliberate V0 identity strategy:

```text
REQUEST_ID := ARBITRATION_GENERATION
```

It is valid only because the request is admitted once per fresh generation and downstream modules preserve the identity.

This does **not** prove that generation is the final universal AEGIS request-ID mechanism. A future stronger identity mechanism may replace it if engine-safe and evidence-backed.

## 4. Authorization rule

Authorization is explicitly represented rather than inferred from feasibility alone.

A physical action requires:

```text
valid request
AND
current request generation
AND
valid authorization
AND
authorization generation == request generation
AND
capability-specific physical preconditions
```

The physical command consumes the authorization. Verification therefore cannot reuse the authorization to issue another command.

## 5. Expiry rule

V0 uses generation-bounded authorization expiry.

An authorization is stale when its authorization generation no longer matches the active request generation.

Leaving the authorized state also consumes the authorization.

This establishes a safe fail-closed boundary without claiming a wall-clock timer semantic that has not been proven for this lifecycle.

## 6. Idempotency rule

A request generation may issue at most one physical worker task command in V0.

The existing `attempts < 1` guard remains the physical duplicate-command barrier.

A retry requires a new lifecycle generation or an explicit future recovery mechanism. Verification cannot itself authorize another physical request.

## 7. Evidence rule

The reference verifier continues to distinguish:

```text
COMMAND_ISSUED
≠
WORLD_STATE_OBSERVED
≠
CAUSALLY_VERIFIED
```

The current worker verifier establishes observable worker/task/target state but does not claim resource-income causality. Therefore this change does **not** promote worker productivity to proven causal effectiveness.

## 8. Remaining six slices — adoption template

Each remaining slice SHALL adopt the same semantic fields while preserving its own capability-specific state machine.

| Slice | Request owner | Physical owner | Verification boundary | Special blocker/condition |
|---|---|---|---|---|
| `villager_production` | civilian demand | villager production | lifecycle reconciler/census | command→completion causality remains unproven |
| `housing` | civilian demand | housing construction | census/world observation | build→completion causality remains unproven |
| `age_transition` | age requirement | research-age | age/world observation | initial engine age must be observed, not assumed |
| `anti_cavalry` | cavalry response | military production/response boundary | production/world observation | authorization chain must remain explicit |
| `tactical_micro` | micro controller/governor | execution/physical adapter | micro verification | command→tactical effect remains unproven |
| `military_production` | military requirement | military production | production/world observation | source selector `aegis-mp-unit` remains blocked |

## 9. Required adoption fields

Each slice's authoritative physical-action owner SHALL eventually expose equivalents of:

```text
request_id
authorization_id
authorization_generation
authorization_valid
authorization_expiry
```

The slice SHALL preserve:

```text
request identity
→ authorization identity
→ physical action
→ pending identity
→ verification identity
→ reassessment
```

## 10. Promotion gate

Adding these fields does not itself qualify a slice.

Qualification still requires the existing registry contract, runtime evidence, world-state verification, promotion eligibility, and absence of active blockers.

In particular:

```text
synthetic trace
≠
engine proof
≠
qualification
```

## 11. Forbidden implementation shortcut

The remaining slices SHALL NOT be modified by blindly copying the Worker Economic `.per` code.

Only the **functional lifecycle boundary** is reusable:

```text
REQUEST
→ AUTHORIZE
→ PHYSICAL_ACTION
→ PENDING
→ WORLD_STATE_VERIFIED
→ REASSESS
```

Capability-specific strategy, selectors, physical commands, evidence requirements, and recovery semantics remain owned by their respective slices.

## 12. Current state

**Reference slice:** request identity + explicit authorization boundary implemented in source.

**Remaining six:** contract template established; implementation must proceed one slice at a time and preserve existing evidence gates.

The next implementation target should be `villager_production`, because it is the closest civilian analogue and directly exercises the distinction between queue admission, pending state, completion observation, causal attribution, and reassessment.
