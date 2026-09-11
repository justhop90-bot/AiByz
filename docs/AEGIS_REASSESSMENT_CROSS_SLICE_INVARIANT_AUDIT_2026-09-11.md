# AEGIS Seven-Vertical REASSESSMENT Cross-Slice Invariant Audit — 2026-09-11

## Scope

This audit covers the complete seven-vertical REASSESSMENT chain:

1. Worker Economy
2. Villager Production
3. Housing
4. Age Transition
5. Anti-Cavalry
6. Tactical Micro
7. Military Production candidate

The audit checks generation ownership, exact terminal-generation identity, one-shot publication/consumption, stale-outcome rejection, active-request protection, semantic ownership, namespace separation, strategy-boundary separation, and absence of a central reassessment controller.

Source under `main/AegisProm` is authoritative. Runtime copies are not used as architecture authority.

## Executive finding

The seven-vertical REASSESSMENT graph is now structurally closed at the source-contract level.

One cross-slice semantic-owner violation was found and repaired in Tactical Micro:

- `AEGIS-micro-verification-v0.per` was directly clearing `aegis-mc-valid`, a Micro Control-owned lifecycle field.
- Verification must report the terminal result; Micro Control must close its own lifecycle.
- The write was removed from Micro Verification.
- Micro Control now closes `aegis-mc-valid` as part of consuming the exact MV REASSESS publication.

No other equivalent direct lifecycle-owner violation was identified in the seven REASSESS consumers audited.

## Canonical graph

```text
Worker Economy
WTV terminal generation N
  -> WTV REASSESS N
  -> Worker Role Vector acknowledges N
  -> fresh Worker Census generation

Villager Production
VR terminal generation N
  -> VR REASSESS N
  -> Civilian Demand acknowledges N
  -> fresh Civilization State generation

Housing
HC terminal generation N
  -> HC REASSESS N
  -> Civilian Demand acknowledges N
  -> fresh Civilization State generation

Age Transition
RA terminal generation N
  -> RA REASSESS N
  -> Civilization State acknowledges N
  -> fresh World Model generation

Anti-Cavalry
CR terminal generation N
  -> CR REASSESS N
  -> Scouting/Threat acknowledges N
  -> fresh World Model generation

Tactical Micro
MV terminal generation N
  -> MV REASSESS N
  -> Micro Control acknowledges N and closes its lifecycle
  -> fresh World Model generation

Military Production candidate
MP terminal generation N
  -> MP REASSESS N
  -> Scouting/Threat acknowledges N
  -> fresh World Model generation
```

No arrow labelled REASSESS creates the next observation generation.

## Invariant results

| Invariant | Result |
|---|---|
| Seven publishers present | PASS |
| Seven downstream consumption boundaries present | PASS |
| Publisher generation is tied to terminal lifecycle generation | PASS — source level |
| Consumer requires exact published generation identity | PASS — source level |
| Same terminal publication cannot be acknowledged twice | PASS — generation identity + one-shot token |
| REASSESS cannot manufacture the next observation generation | PASS |
| Stale terminal generation cannot be accepted after a newer upstream frame | PASS where consumer has an explicit upstream-generation identity gate; see notes below |
| Active request cannot be silently replaced | PASS for audited production/request verticals; MP remains candidate/incomplete |
| REASSESS does not select strategy | PASS |
| REASSESS does not authorize physical action | PASS |
| UNKNOWN/FAILED is not credited as success | PASS at registry/vertical boundaries |
| Namespace allocations are unique through 787 | PASS at recorded namespace level |
| No central reassessment controller | PASS |
| Runtime qualification | NOT EXECUTED |

## Generation ownership audit

### Worker Economy

WTV publishes the terminal worker-task lifecycle generation. Worker Role Vector acknowledges the exact WTV generation. WRV does not increment its own generation from REASSESS; its generation remains derived from a fresh Worker Role Census observation.

Result: PASS.

### Villager Production

The villager reconciler publishes its lifecycle generation. Civilian Demand records that exact generation. Civilian Demand's next demand generation remains Civilization-State-owned rather than REASSESS-owned.

Result: PASS.

### Housing

Housing publishes its lifecycle generation. Civilian Demand has a separate housing acknowledgement namespace and therefore cannot conflate a housing outcome with the villager-production acknowledgement. New demand still requires a newer Civilization State frame.

Result: PASS.

### Age Transition

Civilization State consumes the exact Age Transition lifecycle generation only when that lifecycle generation still equals the current Civilization State generation. This is an explicit stale-token barrier.

Result: PASS.

### Anti-Cavalry

Scouting/Threat consumes the exact Anti-Cavalry lifecycle generation. A new ST generation remains World Model-owned. The same consumer also has an independent acknowledgement namespace for Military Production, preventing MP and CR publications from sharing a token.

Result: PASS.

### Tactical Micro

Micro Control is the upstream lifecycle owner and owns the stable request identity. Micro Verification reports the terminal tactical outcome and publishes REASSESS.

A violation was found: MV directly wrote `aegis-mc-valid 0`. That allowed a verifier to mutate Micro Control lifecycle state outside the owner boundary.

Repair:

- removed `set-goal aegis-mc-valid 0` from MV;
- added lifecycle closure to the MC REASSESS consumer;
- MC now owns both the acknowledgement and closure of its own lifecycle.

Result after repair: PASS.

### Military Production

Scouting/Threat consumes the MP REASSESS token. This does not promote Military Production. The MP selector-initialization blocker remains in force, and the vertical remains `CANDIDATE_BLOCKED` / `NOT_QUALIFIED`.

Result: PASS for reassessment boundary; qualification remains blocked.

## Stale-outcome analysis

The required stale-outcome pattern is:

```text
terminal N
 -> REASSESS N
 -> acknowledge N
 -> wait
 -> upstream observation N+1
 -> derive next lifecycle
```

The forbidden pattern is:

```text
terminal N
 -> REASSESS N
 -> create lifecycle N+1 without new upstream evidence
```

The audited consumers do not advance their authoritative upstream generation from REASSESS. They only copy the terminal generation into acknowledgement fields.

Age Transition is the strongest explicit stale-token barrier because Civilization State requires the RA generation to still equal the current CS generation before acknowledgement.

Tactical Micro similarly records the exact MV lifecycle generation and requires the publisher token to match the current MV lifecycle generation.

## Duplicate-request analysis

Generation-keyed lifecycle admission and `valid == 0` protection remain the primary active-request barrier in the qualified request-producing slices.

The REASSESS consumers do not reset a live upstream request into a new physical request. A new request requires the upstream observation/demand boundary to advance first.

Military Production is intentionally excluded from promotion-level duplicate-request conclusions because its selector and complete authorization lifecycle remain incomplete.

## Authorization boundary

REASSESS consumption does not create authorization.

The established rule remains:

```text
REASSESS
 !=
AUTHORIZATION
```

A consumer may acknowledge that reconsideration is permitted, but physical execution still requires the vertical's normal authorization/feasibility chain.

## Semantic ownership finding

The important cross-slice rule is:

```text
one semantic state field -> one owner
```

A REASSESS publisher's event token is a protocol boundary and may be consumed by its designated downstream consumer. That protocol coupling is intentional and separately namespaced.

A consumer must not directly mutate an unrelated lifecycle owner's substantive state.

The Tactical Micro MV→MC `valid` write violated that rule and was repaired.

The resulting ownership is:

```text
MV owns MV result/stage/reassessment publication.
MC owns MC lifecycle validity/closure/request identity.
MC consumes MV's publication token.
```

## Namespace audit

Current reassessment allocations:

- 760–761 WTV publisher
- 762–763 VR publisher
- 764–765 HC publisher
- 766–767 RA publisher
- 768–769 CR publisher
- 770–771 MV publisher
- 772–773 MP publisher
- 774–775 CIV acknowledgement of VR
- 776–777 CIV acknowledgement of HC
- 778–779 WRV acknowledgement of WTV
- 780–781 CS acknowledgement of RA
- 782–783 ST acknowledgement of CR
- 784–785 MC acknowledgement of MV
- 786–787 ST acknowledgement of MP

These allocations are disjoint and are registered in the authoritative namespace map.

## Central-controller audit

No monolithic REASSESS controller was introduced.

Each downstream owner consumes the event appropriate to its upstream boundary:

```text
WTV -> WRV
VR  -> CIV
HC  -> CIV
RA  -> CS
CR  -> ST
MV  -> MC
MP  -> ST
```

This is distributed event consumption, not a hidden central scheduler.

## Promotion boundaries preserved

This audit does not promote any vertical.

Remaining independent blockers include:

- causal evidence writers are not proven for several verticals;
- target-build runtime evidence has not been executed;
- Tactical Micro command-to-world-effect qualification remains open;
- Military Production selector initialization remains unresolved;
- authoritative engine-age observation remains a World Model issue;
- reassessment consumption is source-contract complete but not runtime-qualified.

## Tests added

`tests/vertical_slices/test_reassessment_cross_slice_invariants.py` checks the seven publisher allocations, seven consumer allocations, strategy separation, Tactical Micro ownership repair, no REASSESS-generated consumer generation, and absence of a monolithic reassessment controller.

These are static source tests. They are not target-build runtime qualification.

## Final disposition

**SEVEN-VERTICAL REASSESSMENT CHAIN: SOURCE-CONTRACT CLOSED.**

**CROSS-SLICE OWNER VIOLATION FOUND: Tactical Micro MV -> MC valid write.**

**REPAIR: COMPLETED.**

**NAMESPACE: REGISTERED THROUGH 787.**

**CENTRAL CONTROLLER: NONE.**

**QUALIFICATION: NOT PROMOTED.**

The next engineering gate should be a repository-wide audit of lifecycle ownership and physical-action authorization, followed by runtime qualification only where the evidence gates permit it.
