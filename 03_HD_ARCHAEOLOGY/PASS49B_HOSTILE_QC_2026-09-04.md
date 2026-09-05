# Pass 49B Hostile QC — Byzantine Deep Dive

**Status: PASS**  
**Layer: 2 — research only**  
**Implementation: ZERO**

## Purpose

Attack the Byzantine mechanics/strategy cross-reference for overclaiming, stale mechanics, civ confusion, and accidental Layer-3 specification.

## Findings

1. **Current-version contamination:** PASS. Current official February 2026 naval overhaul and +25% Byzantine Fire Ship/Dromon attack-speed bonus are explicitly incorporated.
2. **AoE4 contamination:** PASS. AoE4 Byzantine material is not used as evidence for AoE2 mechanics.
3. **Discount overclaim:** PASS. -25% is treated as selective cost leverage, not a generic economic multiplier.
4. **Imperial overclaim:** PASS. -33% Imperial cost is not equated with guaranteed earlier Imperial timing.
5. **Cataphract ontology:** PASS. Cavalry mechanical family remains distinct from anti-infantry strategic role; anti-cavalry resilience is not treated as anti-cavalry offensive role.
6. **Counter ontology:** PASS. Nominal counter, effective counter, and strategic response are separated.
7. **Tech-tree feasibility:** PASS. Tree access is not treated as immediate feasibility.
8. **Vision overclaim:** PASS. Free Town Watch/Patrol is treated as information advantage, not automatic map control.
9. **Historical AI overclaim:** PASS. Historical HD mechanisms are separated from proof of Byzantine-specific strategic intent.
10. **Camel chain:** PASS. Threat→camel production is classified as a strong selected historical response chain, not universal optimization.
11. **Naval historical drift:** PASS. Current naval mechanics are not inferred from historical HD scripts.
12. **Monk overclaim:** PASS. Healing/conversion/relic economy are separate capability classes.
13. **Defense overclaim:** PASS. Building HP is a durability/tempo mechanism, not direct strategic victory value.
14. **Layer boundary:** PASS. No .per, runtime, controller, or production implementation was created.

## Deepening conclusions

The most important refinement is that Byzantine strategy is best modeled as a **capability-selection problem under changing constraints**. The civilization's bonuses interact: information can create response time; durable infrastructure can create delay; selective food discounts can change bottlenecks; broad technology access can enlarge the feasible response set; and discounted Imperial access can convert survival into a late-game transition advantage. None of these interactions should be treated as a single historical engine variable.

The strongest currently proven historical Byzantine-specific bridge remains:

```text
ENEMY MOUNTED PRESSURE
→ CAVALRY THREAT STATE
→ CAMEL PRODUCTION CONDITIONS
→ FEASIBILITY GATES
→ TRAIN CAMEL
```

The largest unresolved historical question is the degree to which the HD controller dynamically exploits other Byzantine-specific strategic advantages, especially Cataphract anti-infantry specialization, building durability, free vision, and discounted Imperial timing.

## Six-month re-entry test

A future reviewer should verify: current naval patch is used; AoE4 is excluded; all civ bonuses are correctly scoped; Cataphract role is preserved; historical evidence is not inflated into intent; current structured reference is not confused with installed .dat; and Layer-2 implementation remains zero.

## Verdict

**PASS — research foundation is safe to advance into Pass 50.**
