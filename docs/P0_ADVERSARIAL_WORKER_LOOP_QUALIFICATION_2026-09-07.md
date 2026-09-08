# P0 Adversarial Worker Loop Qualification

Target: AoE2DE 101.103.48987.0 / BuildID 24094652.
Status: Static architectural audit; no runtime qualification claimed.

## Scope

Audit the current civilian economic vertical slice for dependency integrity, goal-range collisions, generation propagation, terminal-state behavior, and uncontrolled feedback loops before any production-root integration.

## Result

The vertical slice is conceptually closed but is NOT integration-ready. The audit identified a critical arbitration terminal-state defect: the final qualification rule could mark a no-demand frame valid because `stage == arbitrated` was sufficient. That could allow downstream selection to consume a zero-resource arbitration frame. The arbitration file was corrected so only a positive selected-resource result becomes qualified/valid. New commit: 441f928be6179cccc7972ab472c197cee5352519.

## Cross-module chain

Civilization State → Civilian Demand → Economic Demand → Economic Arbitration → Worker Target Selection → Source/Dropsite Serviceability → Worker Task Command → Worker Task Verification → Worker Recovery.

The intended generation chain is monotonic. Each downstream module fences on an upstream generation and publishes its own generation rather than relying on same-pass mutation visibility.

## Findings

1. GENERATION FENCING: present across the major candidate modules. This is an architectural mitigation for uncertain interpreter pass semantics, not proof of runtime ordering.
2. TERMINAL VALIDITY: arbitration required an explicit positive-selection condition. Without it, no-demand could become valid.
3. WORKER RETASKING: worker selection searches `villager-class`, not current economic role, preserving the ability to reallocate existing workers.
4. SOURCE QUALIFICATION: source existence and selected-source serviceability remain distinct from worker selection.
5. COMMAND BOUNDARY: command issuance is separated from verification.
6. VERIFICATION BOUNDARY: worker/target observation remains weaker than proof of productive gathering.
7. RECOVERY BOUNDARY: recovery does not directly issue replacement commands; it returns to retry/upstream disposition.
8. FOOD GAP: food remains unimplemented as a complete service because the stock food system is a portfolio of sources and dedicated subsystems.
9. CONCURRENCY: individual worker attribution is not proven when multiple simultaneous production/task commands exist.
10. RUNTIME ABI: exact pass boundaries, mutation visibility, command side effects, and search-state refresh remain unqualified.

## Loop analysis

The intended retry path is bounded by generation and attempt count. However, static boundedness is not sufficient to prove absence of runtime churn. Dynamic qualification must observe whether failure → recovery → re-arbitration advances generation and changes state rather than repeatedly reproducing the same command.

## Qualification state

OBSERVED: stock search/filter and distributed recovery mechanisms.
CORRELATED: current AEGIS module boundaries form a coherent closed-loop architecture.
IMPLEMENTED: candidate modules and generation-fenced interfaces.
STATIC-QUALIFIED: no production-root load; isolated goal ranges; explicit terminal conditions after correction.
UNQUALIFIED: target-build execution order, same-pass mutation visibility, search-state freshness, task attribution, productivity, and dynamic loop termination.

## Gate decision

DO NOT load the full vertical slice into production yet. The correct next step is a controlled ABI/dynamic probe harness or isolated integration candidate that can measure one generation through the entire worker loop. Integration must not proceed from static confidence alone.