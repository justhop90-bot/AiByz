# AEGIS-BYZ — P0 BYZANTINE ARCHITECT PASS
## Civilization-Operating-System Contract — 2026-09-08

**Target:** AoE2DE 101.103.48987.0 / BuildID 24094652
**Persona:** Byzantine Architect — Civilization Doctrine
**Verdict:** The first substrate must be a Byzantine demand-and-state system, not a generic economy with Byzantine strategy bolted on.

## 1. Architectural principle

The Byzantine advantage is adaptability. Therefore adaptability must propagate through the service architecture:

```text
OPPONENT OBSERVATION
→ BELIEF / CONFIDENCE
→ BYZANTINE RESPONSE MODEL
→ STRATEGIC DEMAND
→ RESOURCE DEMAND
→ WORKER DEMAND
→ INFRASTRUCTURE / PRODUCTION DEMAND
→ PHYSICAL EXECUTION
→ OBSERVED RESULT
→ NEW INFORMATION
```

A tactical counter is not automatically a strategic answer. Counter selection must consider confidence, timing, resources, infrastructure, production throughput, map access, counter-counter risk, and opportunity cost.

## 2. Byzantine-specific knowledge requirements

The Architect must maintain version-aware data for civilization bonuses, team bonus, unit availability, technology availability, costs, prerequisites, unique units/technologies, upgrade paths, production endpoints, counter relationships, defensive modifiers, Imperial timing/economic implications, and map-dependent options.

External strategy material is strategic context only. Target-build unit/technology facts must ultimately be checked against authoritative target data.

## 3. Byzantine operating principles

### Counter elasticity

Prefer responses that preserve the ability to change composition when the opponent changes.

### Defensive compounding

Defensive durability buys time for information acquisition, worker preservation, infrastructure completion, and counter production.

### Gold preservation

The scheduler must understand when discounted trash counters allow gold to be conserved for higher-value strategic expenditures.

### Imperial conversion

The cheaper Imperial transition is a timing/resource allocation option. It must not become a universal fast-Imperial trigger.

### Information economics

Incorrect information can cause incorrect production, technology and worker allocation. Scouting freshness and confidence therefore affect economic demand.

## 4. Byzantine demand contract

The cognition layer should eventually emit typed intent rather than raw engine commands.

```text
BYZ_DEMAND
  generation
  reason
  urgency
  priority
  confidence
  threat-family
  desired-counter-family
  quantity
  resource-burden
  deadline
  infrastructure-requirement
  information-requirement
  fallback
```

The service layer converts this into resource, worker, construction, production, information and military requests.

## 5. First civilian slice

The first implementation remains civilian but must accept future Byzantine strategic demand without rewriting the substrate.

```text
BYZ STRATEGIC DEMAND
→ ECON DEMAND
→ TARGET WORKER VECTOR
→ SOURCE QUALIFICATION
→ TASK COMMAND
→ MEASURED RESOURCE RESULT
→ RECONCILIATION
```

Initial concrete demand is villager continuity plus housing and sustainable food/wood service.

## 6. Byzantine economic state

Static worker percentages are not the final controller. Worker targets derive from base civilization needs, strategic demand, construction demand, production demand, technology reservations, emergency liquidity, source serviceability, and risk.

Allocation requires hysteresis and bounded retasking so the bot does not oscillate workers between resources.

## 7. Counter matrix contract

For each opponent threat family maintain:

```text
threat family
observed amount
confidence
likely continuation
immediate counter
sustainable counter
transition counter
resource burden
production endpoint
technology requirement
infrastructure requirement
counter-counter risk
information required
fallback
```

This matrix belongs to Byzantine doctrine. Physical unit production belongs to Production/Military services.

## 8. Map doctrine

Priorities vary by map class and resource topology. Open, closed, water/hybrid, and resource-poor states alter the value of defense, scouting, production timing, and resource access. Map awareness therefore enters demand arbitration rather than a fixed opening script.

## 9. Ownership

The Byzantine Architect owns strategic demand semantics, Byzantine priorities, counter doctrine, timing policy, flexibility policy, information requirements, and economic opportunity-cost policy.

It does not own engine facts, raw command legality, worker object mutation, queue commands, direct building commands, or engine authority.

## 10. First implementation rule

Do not write a Byzantine opening script. Write a Byzantine civilization control substrate capable of receiving changing demand.

The first proof is:

> Can a Byzantine strategic requirement propagate into physical civilization state, survive disruption, and return measured evidence to cognition?

## 11. Architect verdict

Proceed from archaeological reconciliation into behavioral preservation and contract synthesis. The first production implementation should be a small Civilization State + demand interface capable of driving villager, housing, and worker services without ownership collisions.
