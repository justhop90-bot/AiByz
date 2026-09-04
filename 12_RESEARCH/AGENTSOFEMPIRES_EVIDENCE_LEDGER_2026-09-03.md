# AgentsOfEmpires — AEGIS Evidence Ledger

**Date:** 2026-09-03  
**Scope:** `MaxRobinsonTheGreat/AgentsOfEmpires`  
**Authority:** External behavioral/research evidence; current executable remains authoritative for native implementation  
**Layer-1 status:** 89%

## Provenance

The repository was treated as an archaeological specimen. Local inventory and comparison were performed against the controlled Weebo environment. The `docs/Promisory` corpus was compared with the installed Promisory directory: **36 files checked, 0 mismatches**.

This establishes file identity for those 36 files only. It does not establish correctness of the repository's native-engine interpretations or experimental attribution without separate evidence.

## High-value observations

### AOEA-001 — Current Promisory source bridge

**Observation:** Repository Promisory files match the installed Promisory files on Weebo for all 36 checked files.

**Evidence:** direct file-content comparison.

**Grade:** A+ for file identity.

**Use:** current-build behavioral corpus.

**Restriction:** no inference that repository source comments or historical implementation assumptions are current native truth.

### AOEA-002 — Promisory is a distributed stateful system

**Observation:** Major modules combine facts, actions, goals, strategic numbers, timers, DUC/search state, group state, target selection, and explicit control transitions.

**Grade:** A/B+.

**Use:** architecture model and experiment design.

### AOEA-003 — Search state is explicit state

**Observation:** DUC workflows repeatedly reset, populate, filter, sort, inspect, select, and consume search state.

**Grade:** A/B+.

**Use:** prioritize native DUC state-machine archaeology.

### AOEA-004 — Search state can outlive a single rule

**Observation:** Repository experiments report cross-rule accumulation unless a full search reset is performed.

**Grade:** B+ behavioral.

**Use:** state-lifetime hypothesis.

**Not proven:** exact native scheduler/pass boundary.

### AOEA-005 — Class/type namespaces differ

**Observation:** A concrete object-type search failed in an experimental scenario while class-based searches successfully located intended targets; the corrected experiment produced an explicit runtime marker.

**Grade:** A behavioral.

**Use:** namespace registry and DUC validation.

### AOEA-006 — Target-object operations are compound

**Observation:** Targeting combines local search state, remote search state, target selection, grouping, formation, stance, and native order submission.

**Grade:** B+.

**Use:** high-priority native bridge target.

### AOEA-007 — Competing order mutations are order-sensitive

**Observation:** Repository experiments found that a later tactical order could supersede an earlier order in the same effective execution context.

**Grade:** B+ behavioral.

**Use:** scheduler/action-queue constraint.

**Not proven:** lexical ordering as the universal scheduler algorithm.

### AOEA-008 — Rule jumps matter to reachability

**Observation:** Promisory uses rule-jump constructs extensively, and experiments found that appended rules can be bypassed by internal control flow.

**Grade:** B+.

**Use:** probe-placement and control-flow modeling.

### AOEA-009 — Timer state has lifecycle semantics

**Observation:** Experiments and reference material distinguish enabled/running, triggered, and disabled timer behavior and show interactions between baseline and experimental timer allocations.

**Grade:** B+.

**Use:** native timer state-machine archaeology.

### AOEA-010 — Extended goals can encode structured state

**Observation:** Search-state operations populate contiguous goal slots; strategies use high-numbered goal blocks for structured scratch/state data.

**Grade:** A/B+.

**Use:** goal-store and result-mutation archaeology.

### AOEA-011 — Focus-player context is operational

**Observation:** Scripts save, replace, use, and restore focus-player state around context-sensitive remote searches and related operations.

**Grade:** B+.

**Use:** context ownership/lifetime model.

### AOEA-012 — Pure Promisory can outperform invasive tactical overlays

**Observation:** The repository's final A/B experiment records a 14–1 result for a minimal Promisory configuration versus 9–5 for a more interventionist tactical variant in the tested configuration.

**Grade:** A experimental.

**Use:** architectural principle: correct high-leverage context before replacing established control subsystems.

### AOEA-013 — Siege controller failure was attributable to search semantics

**Observation:** An intended controller initially lacked its expected runtime marker because its target search did not identify the intended objects; a class-based implementation subsequently produced the marker.

**Grade:** A experimental.

**Use:** require observable subsystem confirmation before attributing gameplay outcomes.

### AOEA-014 — Production policies can interfere with baseline objectives

**Observation:** Older experiments showed Feudal training demand consuming resources needed by the baseline age-up/economic system.

**Grade:** B+ experimental.

**Use:** supports deficit/opportunity-cost production architecture.

### AOEA-015 — Strategy packaging exposes load-resolution constraints

**Observation:** Strategy packaging duplicates and namespaces dependency trees, rewriting internal loads to avoid ambiguous resolution under the game's AI-root search environment.

**Grade:** B+ behavioral/tooling.

**Use:** generated `.per` packaging design.

### AOEA-016 — GUI automation is not causal evidence

**Observation:** The harness must maintain foreground game interaction and contains platform-specific window management.

**Grade:** A for harness behavior.

**Use:** adapter engineering only.

### AOEA-017 — Harness backup implementation requires correction before reuse

**Observation:** The documented AI backup path does not preserve original file contents; it creates a placeholder before deleting the source.

**Grade:** A code inspection.

**Use:** quarantine current backup routine; never reuse unchanged for destructive operations.

## Native archaeology consequences

The specimen changes the priority order of current-build native investigation.

### Highest-value targets

1. `up-full-reset-search` -> search object/state.
2. `up-find-local` / `up-find-remote` -> candidate-list construction.
3. `up-get-search-state` -> state serialization/result write.
4. `up-set-target-object` -> target-selection state.
5. `up-target-objects` -> DUC-to-native-order bridge.
6. timer enable/trigger/rearm -> timer lifecycle.
7. goal writes/readers -> script-visible state storage.
8. rule-jump/control position -> scheduler/control-flow bridge.
9. target/order mutation -> `CurrentOrder` / `CurrentAction` transition.

## Cross-source triangulation

The strongest current AEGIS model is now:

```text
AgentsOfEmpires behavioral corpus
          |
          v
behavioral constraints
          |
          +---- historical AIExpert/run-list evidence
          |
          +---- AIRef command semantics
          |
          v
candidate current-native architecture
          |
          v
controlled AoE2DE executable
          |
          v
promotion / rejection
```

The historical native project can suggest internal structures; the current Promisory corpus can constrain what those structures must accomplish; only the controlled executable can promote a native implementation claim.

## Explicit non-promotions

Do not promote the following from this specimen:

- exact current `AIExpert` layout;
- exact current `RunList` address or ABI;
- exact current fact-cache implementation;
- exact persistent-fact refresh cadence;
- exact scheduler comparator;
- exact rule-to-action dispatcher;
- exact action-to-UnitAI mutation;
- exact failure/recovery dispatcher;
- any hard-coded native address from an external project.

## Layer-1 accounting

This pass **strengthens evidence but does not close a completion-gate edge**. The 89% position therefore remains frozen.

The reason is methodological: Layer 1 completion is defined by causal reconstruction, not evidence volume. The newly established Promisory provenance and behavioral constraints improve the quality of hypotheses and experimental design, but the missing native transitions remain missing.

## Fair-use statement

This ledger is original AEGIS analysis. It summarizes public project behavior and records independently generated measurements and deductions without reproducing substantial source text or proprietary binaries. External projects remain credited research specimens and are not treated as AEGIS-owned source code or canonical runtime authority.
