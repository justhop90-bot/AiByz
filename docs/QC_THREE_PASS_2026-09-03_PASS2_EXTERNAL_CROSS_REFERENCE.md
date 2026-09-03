# AiByz — Three-Pass Quality Control

## Pass 2 — Cross-Reference: New Material, GitHub, and Verified External Sources

**Date:** 2026-09-03  
**Disposition:** PASS with evidence promotions and retained uncertainty

## 1. Method

This pass compares the latest local evidence against three independent classes of material:

1. the current AiByz repository and its historical evidence record;
2. newly supplied AoE2DE data/AI/XS/replay/native material;
3. independently verified public sources, prioritizing official World's Edge documentation and established community reference projects.

The purpose is not to make three sources agree. The purpose is to identify where they converge, where they differ, and which propositions survive the strongest available evidence.

## 2. Cross-reference results

### 2.1 Stock AI composition — STRENGTHENED

The supplied `gamedata_x2/PromiDE.per2` is a compact composition root that loads the Promisory constants and rule modules and includes `ailib/Geometry.xs`. The recursive corpus analysis resolves a broad stock-AI graph and counts **7,831 syntactically reachable `defrule` definitions across 28 reachable `.per/.per2/.xs` files**, conservatively including conditional branches.

This agrees with the repository's existing model that the shipped AI is a modular rule program rather than a single flat script. It does not establish that all definitions execute in one game.

### 2.2 XS support — CONFIRMED, NOT ARCHITECTURALLY REQUIRED

The supplied stock composition uses XS, and the official World's Edge Update 87863 explicitly documents AI XS support, including `include "script.xs"`, `xs-script-call`, goal/SN accessors, and persistent XS storage. This independently corroborates the existence of an XS bridge into AI scripting. It does **not** prove that AEGIS requires XS; that remains an implementation choice subject to capability qualification.

### 2.3 AI/UnitAI distinction — STRENGTHENED

The native vocabulary reconstructed in the repository distinguishes AI rule/fact/action concepts from UnitAI concepts such as orders, actions, targets, notifications, search, and recovery. Official update history independently documents fixes to AI exploration commands, target reporting, invalid terrain placement, pathfinding, garrison behavior, retargeting, and SHIFT-queued control. These reports are consistent with a meaningful boundary between strategic AI decisions and downstream unit execution, while still not exposing the internal class/data-flow implementation.

### 2.4 Search/targeting machinery — STRENGTHENED

The repository's native-search model is consistent with public scripting documentation and official patch behavior showing target acquisition, retargeting, pathing, ownership/visibility effects, and AI command corrections. The correct conclusion remains that native tactical machinery is substantial and should be reused where possible rather than duplicated by the strategic bot.

### 2.5 Identity namespaces — RETAIN STRICT BOUNDARY

The newly supplied `dat` material distinguishes unit-line data from concrete unit identifiers. The Knight Line is represented by a line identifier and an ID chain rather than being semantically identical to a concrete Knight unit ID. This strengthens the repository rule that unit IDs, line IDs, and class IDs are separate namespaces.

The earlier `knight-line` validator issue must therefore remain classified as a validator/runtime contract question until reproduced against the exact controlled runtime. A validator complaint is not sufficient evidence to rewrite the runtime semantic model.

### 2.6 Runtime evolution — IMPORTANT QUALIFIER

Official Update 177723 (June 2, 2026) documents current AI-engine fixes including exploration-command targeting, object-data behavior, treaty-related target classification, invalid placement, and multiple pathfinding changes. Therefore, native conclusions must remain build-scoped. Historical public descriptions can corroborate mechanism categories but cannot silently substitute for the exact 101.103.48987.0 executable.

## 3. External-source hierarchy

The strongest public corroboration used in this pass is:

- World's Edge official update notes for AI, scripting, pathfinding, and UnitAI-adjacent behavior;
- AoE2 AI Scripting Encyclopedia for scripting vocabulary and command/parameter reference;
- Siege Engineers reference data for structured unit-line/data semantics;
- independent FreeAoE source for comparative evidence about an independently implemented AI rule model.

FreeAoE is explicitly comparative evidence. Its implementation must not be treated as the AoE2DE implementation.

## 4. Evidence promotions

The following claims may be strengthened in the repository's knowledge layer:

- exact stock composition root and its XS include;
- qualified 7,831 reachable rule-definition corpus statistic;
- existence of a real stock XS integration surface;
- separation of strategic AI vocabulary from UnitAI execution vocabulary;
- substantial native search/target/pathing capability;
- distinct unit/line/class identity namespaces;
- necessity of build-scoping native conclusions.

## 5. Claims deliberately NOT promoted

The following remain open despite cross-source agreement:

- exact scheduler comparator and interval mathematics;
- exact persistent-fact storage, cache lifetime, and invalidation;
- exact rule-handler → native-action mutation bridge;
- exact `CurrentOrder → CurrentAction` write path;
- exact failure/invalidation/completion propagation;
- complete native object identity lifecycle and reuse semantics;
- end-to-end predictive causal path through the shipped runtime.

## 6. Pass-2 conclusion

**PASS.** Independent sources increase confidence in the mechanism categories and boundaries already recorded, but none of them supplies the missing implementation-level causal edges. The repository should become more precise, not more confident merely because the sources are numerous.
