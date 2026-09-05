# AEGIS Layer 2 — Static ABI Closure

Date: 2026-09-05
Status: CLOSED — STATIC / PRE-RUNTIME
Build baseline: AoE2DE 101.103.48987.0

## Decision
Layer 2 is now closed as a static architecture and ABI gate. No runtime test, bot implementation, or production `.per` code is authorized by this document.

The remaining empirical questions are deliberately transferred to the first Layer 3 validation gate. This preserves the project rule that runtime begins only after Layer 2 is closed.

## 1. Machine namespace evidence
The official DE update expanded available goals from 512 to 16,000. The current stock installation was independently captured and the normal HD entrypoint was resolved to a four-file recursive source closure.

The closure contains zero resolved references to goal IDs 512–16,000. A broader scan of all 50 stock `.per` files found 85 high goal IDs, ranging from 623 through 8404. Therefore the entire high range cannot be treated as globally empty merely because it is outside the HD closure.

Crucially, the broader stock scan found zero resolved stock goal references in 10000–15999. This is stronger evidence for a candidate namespace than the earlier closure-only result.

## 2. AEGIS namespace policy
AEGIS receives a reserved candidate scalar-goal namespace of:

    10000–15999 inclusive

Capacity: 6000 goal slots.

Goal 16000 is deliberately excluded from the normal namespace as a boundary sentinel. Goals below 10000 are not AEGIS-owned by this policy.

No numeric channel outside this range may be assigned an AEGIS semantic merely because it appears unused in one file.

## 3. Ownership rule
Namespace ownership is defined by symbolic AEGIS ownership plus the static allocation registry, not by numeric emptiness alone.

A stock symbol or stock lifecycle may not be repurposed. Stock goals 1–9999 remain stock/non-AEGIS territory even where individual values appear unused.

The AEGIS namespace is reserved at the architecture level before any implementation uses it.

## 4. Scalar-only ABI rule
The Layer 2 state ABI may use the reserved goals only as scalar state channels through operations whose documented semantics address one goal at a time, including:

- set-goal
- up-modify-goal
- goal reads/comparisons
- up-compare-goal
- scalar fact-to-goal operations such as up-get-fact and its player/focus/target variants

Point, cost, search-state, guard-state, victory-data, and other operations that consume multiple consecutive extended goals are not part of the scalar state ABI unless separately qualified.

This prevents an apparently free goal from becoming an accidental base address for a multi-goal structure.

## 5. Extended-goal boundary policy
The scripting reference documents command-specific restrictions for multi-goal operations. Historical restrictions around consecutive goal ranges remain relevant as a design hazard even after the global goal-count expansion.

Therefore AEGIS does not infer “all 16,000 goals are interchangeable.” Each multi-goal command family requires its own qualification before use.

The core 19-field AEGIS state envelope is intentionally designed as scalar records first.

## 6. ABI ownership model
Every AEGIS state field must have:

- symbolic name
- numeric goal allocation
- type/channel kind
- owner
- writer set
- reader set
- lifecycle/reset rule
- generation semantics where applicable
- permitted operations
- prohibited operations
- evidence level

Numeric allocation without this metadata is invalid.

## 7. Existing stock analogues remain off-limits
The following remain inputs/analogues, not AEGIS-owned state:

- sn-cavalry-threat
- anti-cavalry-threat-goal
- unit-goal
- attack-status-goal
- sn-resource-control

Their writer/reader/lifecycle traces established existing stock ownership. AEGIS will observe or derive from them where appropriate rather than hijacking their channels.

## 8. What is proven
Static evidence now proves:

1. Goal capacity is 1–16,000 in the documented DE scripting model.
2. The normal stock HD closure is only four loaded `.per` files.
3. That closure has no resolved high-goal state references.
4. The wider stock `.per` tree does use high goals, but its observed maximum resolved goal ID is 8404.
5. No resolved stock goal reference was found in 10000–15999 across the complete stock `.per` tree scanned.
6. Existing stock state channels have identifiable ownership/lifecycle semantics and are not to be reused.
7. AEGIS therefore has a statically justified six-thousand-slot candidate namespace that is materially separated from observed stock goal usage.

## 9. What is intentionally NOT claimed
This closure does not claim that a runtime write/read to 10000–15999 has already been executed. None has.

It does not claim that every engine command accepts every high goal as an argument.

It does not claim that future game updates will preserve the same stock namespace.

Those are runtime/build-regression concerns and belong to the first Layer 3 validation gate, after Layer 2 closure.

## 10. Layer 2 acceptance
Layer 2 acceptance criteria are now satisfied at the static architecture level:

- stock ownership boundary: CLOSED
- stock load-closure audit: CLOSED
- high-goal namespace reconnaissance: CLOSED
- global stock collision scan: CLOSED
- dedicated AEGIS namespace policy: CLOSED
- scalar-vs-extended operation policy: CLOSED
- ABI metadata/ownership contract: CLOSED
- implementation allocation: NOT STARTED
- runtime validation: DEFERRED TO LAYER 3

## Final status

**LAYER 2: 100 / 100 — CLOSED (STATIC / PRE-RUNTIME)**

**Runtime remains forbidden until Layer 3 begins.**

The first Layer 3 task is not bot construction. It is controlled ABI validation of the already-frozen static contract against the exact captured build, followed by evidence capture and regression criteria.
