# Layer 1 QC Pass — 2026-09-03 — `.per` Scope and Native Metadata Correction

## Executive finding

This pass corrects an important scope distinction and one important native-archaeology interpretation from the immediately preceding pass.

The ByzBot implementation target is a **pure `.per` AI project**. XS is not part of the bot architecture or implementation contract. XS/native scripting infrastructure may still be investigated because it is part of the machine we are trying to understand, but XS discoveries must remain in the **machine-understanding layer** and must not leak into the ByzBot design as an implementation dependency.

The practical Layer 1 priority therefore remains the native machinery that consumes `.per` AI files: AI file loading, lexical/preprocessor handling, rule construction, fact/action registration, rule scheduling, persistent-fact evaluation, strategic-number and goal state, action/order issuance, UnitAI execution, search, and result/recovery feedback.

## Correction 1 — section classification

The previous pass and subsequent discussion contained an address-space classification error. The AIExpert/UnitAI and XS metadata strings around addresses such as `0x1431ea3dd` and `0x1432af648` are in the PE `.rdata` virtual-address range, not `.text`.

For the controlled executable:

- `.text` RVA: `0x1000`, raw pointer `0x400`;
- `.rodata` RVA: `0x313b000`, raw pointer `0x313a400`;
- `.rdata` RVA: `0x313c000`, raw pointer `0x313ac00`;
- `.data` RVA: `0x3d33000`.

The relevant AI/XS string RVAs lie between `.rdata` start and `.data` start. They must therefore be treated as readonly data/debug/source metadata unless implementation evidence proves otherwise.

This correction is significant because it explains why direct instruction/xref recovery from those addresses has repeatedly been weak. A string being near important AI metadata does not make the string itself executable code.

## Correction 2 — candidate `0x1417FF3E0`

The 8-byte value `0x1417ff3e0` found in the inspected metadata record is real executable-address data: it occurs once as an exact 64-bit value in the executable and falls at the beginning of a valid PE unwind (`.pdata`) function range.

The function boundary is:

`0x1417ff3e0` → `0x1417ff4c6`

Independent decoding from the executable produces a coherent function body. It:

- saves nonvolatile registers;
- takes object-like state through `RCX`;
- writes a readonly-data address into the object at offset zero;
- iterates an 8-byte-pointer array at an object-relative location;
- conditionally invokes cleanup-like calls on array members;
- clears/releases pointer storage;
- conditionally invokes another cleanup/deallocation path;
- returns the object pointer.

This is **destructor/cleanup-like behavior**, not evidence of an XS API handler.

The earlier interpretation that the candidate was merely an arbitrary `.text` address was therefore too weak. The stronger and safer statement is:

> The metadata field contains a pointer to a real native function boundary, but the recovered function's behavior is cleanup/destructor-like and does not presently support identification as the `xsGetTechAttribute` implementation.

No direct `CALL rel32` references to this function were found in the tested executable `.text` representation. Its exact role remains unresolved.

## Correction 3 — metadata record interpretation

The inspected record tail has the observable form:

`API signature → zero/metadata field → readonly-data address → executable-address field → source/debug path`

The field immediately before the source path that contains `0x1417ff3e0` is therefore not random bytes. It is structured metadata.

However, the record's semantic field meanings remain unproven. In particular, the executable-address field could be:

- a cleanup/destructor routine associated with a metadata object;
- a constructor/destructor support pointer;
- a registration helper;
- a callable implementation pointer unrelated to the API named immediately before it;
- another runtime object-management reference.

The observed function behavior strongly demotes the final interpretation for this specific candidate, but only a verified consumer of the record can settle the field semantics.

## New native observation — `.pdata` is now an archaeological filter

The PE unwind table can be used as an independent function-boundary validator.

For a candidate executable address, the following promotion test is now available:

1. address lies in `.text`;
2. address is contained in a `.pdata` function interval or otherwise independently established as code;
3. bytes decode coherently from the proposed boundary;
4. function body has a plausible control-flow/ABI structure;
5. caller/consumer evidence connects the function to the target subsystem.

The candidate `0x1417ff3e0` passes steps 1–3 but fails the subsystem-identity test. It therefore remains **QUARANTINED / role unresolved**, not promoted as an API handler.

## `.per` implementation scope

The ByzBot does not require XS knowledge to execute its design. The machine-facing contract we need to close is:

```text
.per file
  ↓
file acquisition / selection
  ↓
preprocessor + lexical analysis
  ↓
semantic rule construction
  ↓
constant / fact / action registration
  ↓
rule storage
  ↓
rule scheduling
  ↓
persistent fact evaluation
  ↓
trigger evaluation
  ↓
handler execution
  ↓
script-visible state mutation
  ↓
action/order request
  ↓
UnitAI
  ↓
simulation
  ↓
next AI evaluation
```

This is the primary causal spine for the bot.

XS investigations may illuminate generic runtime architecture, but they are secondary to closing this `.per` spine.

## What the existing AIExpert corpus gives us

The native corpus already exposes a surprisingly complete semantic vocabulary for the `.per` substrate:

- `loadRules`;
- `Defining Constant`;
- `Defining Fact`;
- `Defining Action`;
- `ruleElementsPtr`;
- indexed `rule[j].element`;
- `ruleDebugInfo[j]`;
- `Evaluating Persistent Facts`;
- `Finished Evaluating Persistent Facts`;
- `Fact[%d] evaluated persistently to %s`;
- `Next Rule`;
- rule-jump bounds diagnostics;
- parser/preprocessor errors;
- rule-length and list-capacity errors;
- string-table capacity errors;
- missing identifier/keyword/arrow/LHS/RHS errors;
- file-open/read failures;
- lexical-analysis failures.

The native semantic surface also contains a large stock vocabulary of strategic numbers and facts covering:

- population and housing;
- resources and resource percentages;
- buildings and building types;
- units and unit types;
- military population;
- research availability/completion;
- feasibility (`can-build`, `can-research`, `can-train`);
- player relationships and stances;
- current age and age time;
- game time and timers;
- searches and target state;
- attack/defend groups;
- exploration;
- target evaluation;
- gathering distributions;
- retasking;
- attack timing;
- cooperation;
- defense distances;
- production/build frequencies.

This is directly relevant to ByzBot because the native `.per` machine contract is already exposing many of the primitives required for a high-level Byzantine decision system.

## Important practical inference — the strategic-number surface is an implicit control plane

The SN corpus is not merely a list of tuning constants.

It contains variables for attack-group size, defense-group size, exploration, target evaluation, gathering percentages, retasking, attack timing, cooperation, and build behavior.

That means a pure `.per` bot can potentially influence substantial portions of the native AI behavior indirectly by changing machine-consumed state rather than attempting to micromanage every unit directly.

This should become a major design question for the eventual bot:

> Which behaviors should ByzBot implement as explicit rule logic, and which should it steer by manipulating the machine's existing strategic-number control surfaces?

That question is more important than any XS API detail.

## New practical architecture for the bot

The machine-facing ByzBot architecture should eventually distinguish three layers of control:

### Layer A — Explicit `.per` reasoning

Rules encode doctrine, priorities, economic conditions, military thresholds, technology choices, emergency responses, and strategic transitions.

### Layer B — Native AI control surfaces

Goals, strategic numbers, timers, groups, facts, and actions are used as the machine's existing control vocabulary.

### Layer C — Native execution/recovery

UnitAI, pathfinding, target search, queues, notifications, action state, and simulation execute the requests and determine the actual result.

This produces the practical model:

`DOCTRINE → RULE DECISION → MACHINE STATE/REQUEST → NATIVE EXECUTION → OBSERVED RESULT → REASSESSMENT`

The `.per` bot should be designed around this feedback loop rather than assuming that issuing an action is equivalent to accomplishing its strategic objective.

## New high-value research targets

The next investigation should prioritize:

1. **`.per` loader boundary:** recover the native function boundary surrounding `loadRules`.
2. **Rule record construction:** recover how one parsed `defrule` becomes the indexed rule representation.
3. **Fact/action ID registration:** determine when IDs are assigned and how they are stored.
4. **Persistent-fact evaluation:** recover the actual evaluation loop and cadence.
5. **Scheduler:** recover priority, interval, sorted-rule traversal, and eligibility behavior.
6. **Handler execution:** recover the transition from a satisfied rule to its action/handler semantics.
7. **Action/order bridge:** identify the native boundary that converts script-level action requests into UnitAI work.
8. **UnitAI mutation:** recover one concrete `CurrentOrder` or `CurrentAction` state write and its subsequent consumer.
9. **Failure feedback:** trace one action from issuance through failure/invalidation/completion into the next AI decision opportunity.
10. **SN/goal control:** determine which machine state changes are immediate, deferred, cached, or sampled on the next evaluation cycle.

## Falsification-first experiments

### Experiment A — rule conflict

Create two otherwise eligible rules that request incompatible machine actions. Determine whether the machine resolves the conflict by priority, source order, scheduler state, action rejection, or UnitAI replacement.

### Experiment B — persistent fact timing

Change a world-state variable immediately before an AI evaluation boundary and determine whether the persistent fact observes the new state, the previous snapshot, or cached state.

### Experiment C — action failure feedback

Issue an action whose execution can deterministically fail. Observe which script-visible or scheduler-visible state changes on the following evaluation.

### Experiment D — SN steering

Alter one native strategic-number control surface while holding rule logic constant. Measure the downstream behavioral change. This tests whether the SN is a genuine control surface rather than a diagnostic/tuning-only variable.

### Experiment E — queue semantics

Issue repeated actions/orders in controlled sequence and determine whether the second request replaces, queues behind, invalidates, or is rejected by the native controller.

## Evidence policy

The following distinctions are mandatory:

- native source-path string ≠ recovered function;
- source/debug metadata ≠ executable implementation;
- executable pointer ≠ API handler;
- `.pdata` function interval ≠ semantic identity;
- action request ≠ execution success;
- execution success ≠ strategic success;
- strategic-number name ≠ proven causal effect;
- replay observation ≠ hidden native state;
- `.per` syntax ≠ native parser implementation.

## Status

Layer 1 remains active and incomplete.

The project should **not** increase its completion estimate merely because the XS metadata investigation became richer. The relevant completion metric is closure of the machine paths that materially determine pure `.per` AI behavior.

The XS findings remain valuable machine archaeology, but they are now explicitly classified as **secondary infrastructure knowledge** for this project.

The highest-leverage frontier is the `.per → AIExpert → UnitAI → simulation → feedback` causal spine.
