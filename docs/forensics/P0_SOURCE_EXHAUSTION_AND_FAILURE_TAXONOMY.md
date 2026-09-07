# P0 Source Exhaustion and Failure Taxonomy Forensics

**Project:** AEGIS-BYZ  
**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Corpus:** untouched stock `resources\_common\ai\Promisory` on the project machine  
**Status:** Forensic evidence; implementation deliberately deferred.

## Executive finding

The stock civilian system contains explicit source-exhaustion and source-unserviceability reactions. It does not rely exclusively on aggregate resource counts. Individual worker roles are stopped when their corresponding source portfolio becomes unavailable, too distant, or otherwise invalid.

This pass materially strengthens the failure taxonomy. The same broad recovery primitive appears across hunters, foragers, and fishers: identify workers whose source class has lost serviceability, filter out workers carrying incompatible loads, issue `action-stop`, then disable the local recovery rule so normal allocation can retask them.

## 1. Wood source capacity is explicitly filtered

In `gatherers.per` around lines 4300-4330, stock first searches eligible villagers and removes workers already targeting trees, carrying resources, or carrying an active task. It then searches wood resources with active/ready status and removes candidate resource objects whose `object-data-tasks-count >= 2`.

This establishes a concrete wood-source capacity gate in addition to the earlier observed task-load accounting.

The sequence is:

```text
eligible worker set
    ↓
wood resource discovery
    ↓
status = active/ready
    ↓
tasks-count < 2
    ↓
distance ordering
    ↓
action-default
```

The threshold is stock behavior for this path and should not be promoted into a universal AEGIS constant without further evidence.

## 2. Forage exhaustion has an explicit worker cleanup path

`gatherers.per` contains an active rule that fires when there are foragers but no viable forage portfolio. The observed conditions include:

```text
villager-forager >= 1
forage-count <= 0
forage-bush availability < 1
```

and, in the active condition set, Gaia forage availability is checked directly.

Stock then:

```text
reset search
find forage-role workers
remove workers carrying too much
stop selected workers
```

This is strong evidence that **source disappearance is converted into worker-task invalidation**, rather than waiting for a generic idle-worker mechanism.

## 3. Fishing exhaustion has its own failure reaction

The same region contains a dedicated fisherman recovery rule. It fires when:

```text
villager-fisherman >= 1
shore-count <= 0
shore-fish-class Gaia count < 1
dropsite-min-distance shore-fish-class > maximum food drop distance
shore-fish-class distance >= 17
```

The selected fishing workers are filtered to avoid incompatible states and then stopped.

Therefore fishing is not simply a variant of land-food tasking. It has source availability, delivery-distance, and worker cleanup semantics of its own.

## 4. Hunting failure is spatially coupled

The hunter cleanup rule fires when both boar-hunting and deer-hunting delivery distances exceed the configured maximum hunt drop distance, with additional hard distance gates. It finds hunter-role workers, excludes heavily loaded workers, stops them, and disables the rule.

This establishes a distinct failure class:

```text
source may exist
BUT
service distance is unacceptable
        ↓
hunting task invalid
        ↓
stop workers
        ↓
allow normal retasking
```

Therefore **source existence and source serviceability are separate facts**.

## 5. Deer has both identity invalidation and spatial invalidation

The deer controller previously established that `current-deer` is cleared when its object ID can no longer resolve to a valid status. This pass adds the broader spatial failure pattern: hunting workers can be stopped when both hunting portfolios exceed service-distance policy.

The two layers are distinct:

```text
Target identity failure
    → invalidate cached deer

Serviceability failure
    → stop hunter workers
    → permit reassignment
```

AEGIS should preserve that distinction.

## 6. Livestock failure is identity/state based

The livestock controller maintains `current-livestock` and `next-livestock`, validates object status, and explicitly switches livestock targets. A worker's role therefore depends on a currently valid resource object rather than a permanent role assignment.

This supports the operational model:

```text
worker role = current productive task state
```

not:

```text
worker role = immutable class
```

## 7. Fish boats have source switching plus exploratory fallback

`watercontrol.per` contains a three-second control loop for fishing ships. It:

1. locates a dock;
2. identifies fishing ships;
3. removes ships carrying too much;
4. identifies ships currently targeting shore fish;
5. measures the dock-to-shore-fish relationship;
6. searches for ocean/deep fish;
7. removes unsuitable ocean-fish candidates by carry state;
8. sorts by distance;
9. retargets ships with `action-default`.

If no deep fish is found, the system generates a random point near the dock and can move a fishing ship there when that point is unexplored.

This proves that fishing has a **source substitution / exploration fallback**, not merely a static shore-fish assignment.

## 8. Wood camp placement and source serviceability interact

`buildings.per` contains explicit lumber-camp rules that react to wood delivery distance. When wood is found beyond the preferred dropsite relationship, stock can enable adjacent dropsites, adjust `sn-camp-max-distance`, and request another lumber camp.

This connects three previously separate observations:

```text
source capacity
      +
source availability
      +
delivery serviceability
      ↓
resource task validity
      ↓
infrastructure migration when justified
```

## 9. Failed placement is not equivalent to completed infrastructure

`general.per` contains a placement reset path for a lumber camp while placement remains pending. It calls `up-reset-placement` and can release escrow under a later failure condition.

This means the logistics state machine must distinguish:

```text
requested
→ placement pending
→ foundation
→ completed
→ serviceable
```

and failure can occur before completion.

## 10. Worker failure taxonomy now supported by direct evidence

The evidence now supports at least these distinct failure classes:

```text
SOURCE_INVALID
  target identity no longer resolves

SOURCE_UNAVAILABLE
  no usable source objects remain

SOURCE_OVERLOADED
  object-data-tasks-count exceeds path threshold

DROPSITE_UNSERVICEABLE
  delivery/service distance exceeds policy

WORKER_INCOMPATIBLE
  worker is building, attacking, entering, carrying, or otherwise excluded

TASK_TARGET_LOST
  worker/source target relationship no longer exists

INFRASTRUCTURE_PENDING_OR_FAILED
  placement/foundation is not yet a usable dropsite

WORKER_THREATENED
  requires separate threat-system evidence

WORKER_DEAD
  accounting latency remains to be measured
```

The final two remain unproven in this pass.

## 11. Critical distinction: local cleanup versus global allocator

The stock rules show resource-specific cleanup controllers. A forager failure invokes a forager-specific worker search. Fisher failure invokes a fisher-specific search. Hunter failure invokes a hunter-specific search.

This is further evidence against assuming one centralized stock civilian recovery manager.

Stock architecture is better represented as:

```text
                 CIVILIAN SYSTEM
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     WOOD           FOOD/HUNT       FISH
        │              │              │
   local failure   local failure   local failure
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                generic retasking
```

AEGIS can centralize this behavior architecturally while preserving resource-specific failure causes.

## 12. Failure recovery is intentionally conservative around carried resources

Multiple cleanup paths remove workers carrying resources beyond a configured threshold before issuing `action-stop`.

This means:

```text
carrying resource != ordinary idle worker
```

The worker may be in a partially completed economic transaction. AEGIS should therefore track cargo state separately from assignment state and should not blindly stop/reassign every worker whose target becomes invalid.

## 13. `action-stop` is recovery, not successful reassignment

The failure paths use `up-target-point 0 action-stop -1 -1` to terminate the invalid task. They do not themselves constitute the new assignment.

The correct interpretation is:

```text
failure detected
    ↓
stop/clean task
    ↓
worker becomes eligible
    ↓
normal allocation discovers new task
    ↓
action-default issues new command
    ↓
engine state must be observed
```

This reinforces the previous finding:

```text
COMMAND ISSUED != TASK CONFIRMED
```

## 14. AEGIS failure taxonomy requirement

Every Worker Assignment / Resource Acquisition transaction should return a typed failure rather than a generic `false`.

Minimum proposed categories:

```text
NO_SOURCE
SOURCE_INVALID
SOURCE_EXHAUSTED
SOURCE_OVERLOADED
NO_DROPSITE
DROPSITE_TOO_FAR
DROPSITE_INVALID
NO_ELIGIBLE_WORKER
WORKER_BUSY
WORKER_CARRYING
WORKER_THREATENED
TARGET_LOST
COMMAND_NOT_ACCEPTED
TASK_NOT_CONFIRMED
TASK_NONPRODUCTIVE
INFRASTRUCTURE_PENDING
INFRASTRUCTURE_FAILED
WORKER_DEAD
```

Only categories directly evidenced by stock should be marked proven in the implementation ledger. The others remain architectural candidates until traced.

## 15. Timing remains an unresolved P0 issue

The stock rules demonstrate periodic evaluation using timers and repeated rule passes. They do not yet prove the exact latency between:

```text
source disappears
→ role count becomes stale
→ cleanup fires
→ worker stops
→ allocator retasks worker
```

That latency matters because AEGIS verification and recovery generations must tolerate transient stale state without creating command thrash.

## Verdict

This pass materially advances P0. We now have direct evidence for source-unavailability cleanup across forage, fishing, and hunting, explicit wood source task-load limits, fishing source substitution, and the separation between source invalidation and worker recovery.

The remaining high-value gaps are threat-driven evacuation, worker-death accounting latency, construction interruption/builder replacement, and the complete semantics of resource/object status values.

No runtime implementation should begin solely from these findings.
