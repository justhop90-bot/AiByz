# AEGIS Layer 3 — Pass 90 Support Matrix + Minimal Cavalry Slice ABI

Date: 2026-09-04
Status: architecture gate

## 1. Support matrix

| Capability | Engine/documentation | Historical archaeology | Validator | AEGIS project | Runtime test |
|---|---|---|---|---|---|
| Goal state | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Strategic-number state | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Flag state | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Timer state | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Focus-player fact query | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Unit-line counting | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Queued-object counting | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| `can-train` | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| `train` | SUPPORTED | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Producer search | SUPPORTED/SEMANTICS NEED EXACT SIGNATURE | SUPPORTED | MUST AUDIT | DESIGN-APPROVED | BLOCKED |
| Generation guard | AEGIS abstraction | NOT HISTORICAL PRIMITIVE | project-owned | DESIGN-APPROVED | BLOCKED |
| Ownership guard | AEGIS abstraction | not proven historical | project-owned | DESIGN-APPROVED | BLOCKED |
| Record publication protocol | AEGIS abstraction | not proven historical | project-owned | DESIGN-APPROVED | BLOCKED |
| Best-so-far candidate selection | AEGIS abstraction | not proven universal historical | project-owned | DESIGN-APPROVED | BLOCKED |

Official Update 36202 confirms queue-aware `unit-type-count-total` and `up-pending-objects`. citeturn0search0 Official Update 47820 confirms train/can-train command behavior and research-queue control. citeturn1search1

## 2. Minimal Cavalry Threat Containment vertical slice

### Inputs

1. Enemy mounted-pressure observation.
2. Own camel capability count.
3. Camel requirement policy.
4. Candidate producer set.
5. Resource/queue feasibility.

### Processing

`OBSERVE → CLASSIFY → REQUIRE → DEFICIT → SELECT → AUTHORIZE → ISSUE → OBSERVE QUEUE → OBSERVE CREATION → OBSERVE AVAILABILITY → VERIFY → REASSESS`

### Hard gates

A camel train operation is command-eligible only when:

- threat observation is valid and not stale;
- objective remains valid;
- deficit > 0;
- candidate producer is valid;
- producer can train the intended unit/line;
- resource reservation is satisfied;
- queue capacity permits the operation;
- commitment is valid;
- owner and generation match;
- execution stage is command-eligible.

### Deficit

`DEFICIT = max(0, REQUIRED - CURRENT)`

Surplus is tracked separately; deficit zero is not objective success.

### Verification

Minimum proof chain:

- V1: commitment authorized;
- V2: command issued;
- V3: queue/pending evidence;
- V4: creation evidence;
- V5: availability evidence;
- V6: deployment evidence;
- V7: battlefield interaction evidence;
- V8: objective-specific effect.

A replay aggregate can corroborate production timing but cannot by itself establish causal intent.

## 3. Byzantine-specific evidence boundary

The historical Byzantine chain is sufficiently supported to serve as the first vertical-slice target:

`enemy mounted pressure → cavalry threat state → camel production conditions → feasibility gates → train camel`

However, the current slice must not hard-code a claim that the historical `traincamel` rule is causally responsible for replay camel queues. Replay evidence establishes temporal production correlation, not causal closure.

## 4. Current build boundary

The latest major official update located is build 177723 (June 2, 2026). It contains AI-engine fixes, including corrections involving `players-unit-type-count`, object-data behavior, and scout commands. The workstation's actual installed build remains unverified. citeturn1search0

## 5. Implementation gate

This pass authorizes **architecture completion for the minimal Cavalry Slice**, not `.per` coding. Coding starts only after the Namespace Collision Audit is concretely cleared and the primitive signatures are validator-verified.
