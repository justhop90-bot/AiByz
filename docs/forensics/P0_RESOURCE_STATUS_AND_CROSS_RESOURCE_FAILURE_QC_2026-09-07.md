# P0 Resource Status and Cross-Resource Failure QC — 2026-09-07

Target: AoE2DE 101.103.48987.0 / BuildID 24094652
Corpus: untouched stock `resources/_common/ai/Promisory` on Weebo.
Status: forensic evidence; implementation deferred.

## Executive finding

Stock exposes a common object-status vocabulary, but it does NOT implement one universal resource controller. The common substrate is a search/filter/selection ABI; resource-specific controllers add different capacity, distance, cargo, threat, and fallback policies.

The correct AEGIS abstraction is therefore a **common Resource Acquisition Service contract with resource-specific policy adapters**, not one generic gather rule.

## 1. Status semantics: what is actually proven

`defaultConstants.per` defines:

- `status-pending = 0`
- `status-ready = 2`
- `status-resource = 3`
- `status-down = 4`
- `status-gather = 5`
- `object-data-status = 19`
- `object-data-tasks-count = 32`

The stock comment for `object-data-status` states:

- 0: incomplete
- 2: active
- 3: resource
- >=4: inactive

This must not be converted into a universal ordinal lifecycle. In particular, `status-gather = 5` is used contextually as an active/search state, while the generic comment describes values >=4 as inactive. The safe semantic interpretation is **call-site/context dependent**, not numeric ordering.

`status-ready` is repeatedly used to select usable active objects. `status-resource` is repeatedly used before `up-find-resource`. `status-gather` is used for objects currently participating in gather/fishing/hunting-style operations. `status-pending` is used extensively for foundations and pending construction.

## 2. Object status is a search qualification, not a resource amount

Stock frequently combines status with other predicates:

```text
status
+ distance
+ resource type/class
+ task load
+ hitpoints/carry
+ dropsite relationship
+ strategic constraints
```

Therefore `status-resource` cannot be treated as proof that a source is usable by itself. A resource can be structurally present but unsuitable because it is too far away, overloaded, or lacks serviceable infrastructure.

## 3. Wood: strongest common allocation pattern

`gatherers.per` contains the concrete sequence:

```text
reset search
→ filter distance
→ status-resource
→ find wood
→ remove object-data-tasks-count >= 2
```

A later retry path uses `status-ready` before another wood search and again removes candidates with `object-data-tasks-count >= 2`.

This establishes:

```text
SOURCE STATUS != SOURCE CAPACITY
```

The engine exposes workload through `object-data-tasks-count`; stock uses it as a candidate filter. The exact threshold is controller-specific and must not be universalized.

## 4. Forage: same substrate, different capacity policy

The forage controller uses:

```text
status-resource
→ find forage-bush-class
→ remove tasks-count >= 3
```

The threshold differs from the wood path. This is direct evidence that task-load limits are **resource/controller policy**, not an engine-wide capacity constant.

## 5. Hunting: status plus biological state

`boarhunting.per` searches boar with `status-ready`, then filters on:

- hitpoints
- max hitpoints
- carry
- distance

The deer controller similarly selects `status-ready` animals and searches multiple huntable classes.

Thus hunting eligibility is not simply `status-ready`; it is a composite biological/task-state predicate.

## 6. Fishing: active task state plus source selection

`watercontrol.per` uses `status-gather` for fishing ships and searches ocean fish. It also checks ship carry and distance, ranks candidates by distance, and issues `action-default`.

Fishing therefore demonstrates an important distinction:

```text
WORKER/BOAT TASK STATE = status-gather
SOURCE STATE = resource search
```

The status of the worker and the status of the resource are not interchangeable.

## 7. Gold and stone: same spatial/resource-selection substrate

`buildings.per` repeatedly uses `status-resource` followed by gold and stone searches. It also ranks by precise distance and varies the allowed service radius using `sn-camp-max-distance`.

This reinforces the source/dropsite model established in the previous logistics forensic: resource acquisition depends on both resource validity and spatial serviceability.

## 8. Cross-resource convergence

Despite different controllers, the common operational pattern is:

```text
DISCOVER
  ↓
STATUS QUALIFY
  ↓
RESOURCE/OBJECT TYPE QUALIFY
  ↓
SPATIAL QUALIFY
  ↓
TASK-LOAD QUALIFY
  ↓
RESOURCE-SPECIFIC QUALIFIERS
  ↓
RANK / SELECT
  ↓
ISSUE COMMAND
  ↓
OBSERVE RESULT
  ↓
RETRY / RETASK / FALLBACK
```

This is the strongest common ABI candidate.

The branches differ at the policy layer:

- wood: tree availability + task load + lumber-camp topology
- gold: mine availability + mining-camp topology + strategic demand
- stone: mine availability + mining-camp topology + strategic demand
- forage: bush availability + smaller task-load policy
- boar/deer: animal state + hunt distance + carry/health predicates
- fishing: ship task state + fish source + dock/water topology
- farms/sheep/livestock: worker-role state + source lifecycle + local threat/food policy

## 9. Failure taxonomy refinement

Cross-resource evidence supports these normalized AEGIS failure classes:

```text
SOURCE_NOT_PRESENT
SOURCE_NOT_USABLE
SOURCE_OVERLOADED
SERVICE_DISTANCE_EXCEEDED
DROPSITE_UNAVAILABLE
INFRASTRUCTURE_PENDING
INFRASTRUCTURE_FAILED
WORKER_INCOMPATIBLE
WORKER_TASK_INVALID
THREAT_BLOCK
STRATEGIC_DEMAND_CHANGED
```

`TASK_INVALID` remains a derived condition. The underlying cause should be preserved.

## 10. Critical architecture correction

Do NOT encode:

```text
resource-status = good/bad
```

Instead represent at least:

```text
source-status
source-load
service-distance
serviceability
worker-eligibility
strategic-demand
freshness
```

A source may simultaneously be:

```text
status-resource = true
serviceable = false
```

or:

```text
status-resource = true
serviceable = true
capacity = exhausted
```

These are materially different failure causes and require different recovery actions.

## 11. Recommended AEGIS Resource Acquisition contract

```text
RESOURCE_REQUEST
  generation
  resource-type
  required-workers
  priority
  urgency
  reason
  source constraints
  dropsite constraints

SOURCE_CANDIDATE
  source-id
  source-type
  source-status
  task-load
  location
  service-distance
  dropsite-id
  serviceable
  observed-at
  generation

RESOURCE_RESULT
  generation
  source-id
  dropsite-id
  worker-set
  command-stage
  productive-stage
  failure-class
  failure-detail
```

The common service owns discovery, qualification, ranking, issuance, and observation. Resource-specific adapters own thresholds and special rules.

## 12. Important negative findings

Not proven:

- exact universal meaning of every numeric status outside its documented/call-site context
- a universal task-load threshold
- `object-data-tasks-count` as literal worker count
- identical source failure behavior across resources
- identical replacement timing across resources
- one centralized stock resource manager
- exact path-distance semantics for every distance predicate

## 13. Engineering consequence

The civilization substrate should be built around **orthogonal state vectors**, not a single resource state enum:

```text
OBJECT STATE
TASK STATE
SERVICEABILITY STATE
POLICY STATE
```

This preserves the distinction between what exists, what is being done, whether it can physically be done, and whether it is still strategically justified.

That distinction is now sufficiently supported by the stock corpus to become a foundational AEGIS substrate principle.

## Qualification status

Static forensic confidence: HIGH for the common search/filter substrate.

Runtime confidence: NOT ESTABLISHED.

No live AEGIS runtime files were modified in this pass.
