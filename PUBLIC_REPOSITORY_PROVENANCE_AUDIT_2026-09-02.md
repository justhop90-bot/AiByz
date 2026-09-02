# Public Repository Provenance Audit — 2026-09-02

## Decision

The public AEGIS repository is a **knowledge and project repository, not a repository of stock or source-derived game AI files**.

The following material was removed from the public `aegis/knowledge-foundation` branch because it was identified by project authority as stock-derived, source-derived, or otherwise unsuitable for public redistribution:

- `ADPromisory/` — removed in full.
- `AiBuilder/` — removed in full.
- `ByzantineWarCouncil.per` — removed.
- `ByzantineWarCouncil.ai` — removed.

The historical specimens remain part of the private/local research archive where available. They are research evidence, not public project source.

## Why modified source is still quarantined

Heavy editing does not automatically transform a source-derived tree into clean project-owned publication material. The safe boundary is therefore based on provenance, not on how many lines were changed.

The project learns from historical implementations by reconstructing their behavior, logic, constraints, and design patterns. It does not need to redistribute the implementation itself.

## What the public repository should contain

### KEEP — project-owned

- AEGIS architecture and contracts.
- Project-owned runtime code.
- Project-owned tests and tooling.
- Original strategic models and abstractions.
- Original documentation.

### DERIVED — strongly encouraged

- Machine facts.
- Engine interface ledgers.
- Reconstructed state models.
- Strategic principles.
- Meta-knowledge.
- Quantitative analyses.
- Failure analyses.
- Experimental conclusions.
- Knowledge graphs.
- Schemas and methodologies.

### EXCERPT — permitted when appropriate

Small, isolated, attributed historical snippets used as evidence exhibits, surrounded by original explanation and analysis.

### PRIVATE — never publish wholesale

- Stock game AI source.
- Complete historical/vendor-derived source trees.
- Proprietary binaries.
- Complete source packages copied from external artifacts.
- Other restricted material whose redistribution rights are not established.

## Required publication transformation

`source identity -> tiny evidence exhibit -> forensic interpretation -> general principle -> AEGIS abstraction -> implementation requirement -> validation`

This is the project's central publication discipline.

## Important Git-history warning

File deletion removes the material from the current branch tree; it does **not** erase previously committed blobs from Git history.

Because the repository is public, historical source blobs may remain reachable through prior commits until history is deliberately rewritten. This audit therefore records **tree cleanup**, not a claim that historical Git objects have been purged.

History rewriting is a separate consequential operation and must be explicitly authorized and verified before execution.

## Knowledge-directory policy

The `knowledge/` directory is now treated as a first-class institutional-memory system. Its purpose is to preserve nearly everything learned from the source material without reproducing the source material itself.

The expected density is high: strategic, mechanical, functional, control, economic, tactical, transition, meta, failure, and engineering knowledge should be captured as atomic records and connected into a knowledge graph.

## Audit standard

Future additions should be classified before publication:

`KEEP | DERIVED | EXCERPT | PRIVATE | QUARANTINE`

No uncertain source should enter the public tree merely because it is useful.
