# Repository Architecture

## Purpose

The repository is organized as a knowledge system, not a miscellaneous code dump.

## Domains

`00_CONSTITUTION` — project authority, safety, governance, definitions, non-negotiable rules.

`01_MACHINE` — AoE2DE AI machine contract, parser/runtime semantics, rule scheduler, facts/goals/SNs, XS, loader/execution research, native evidence.

`02_STRATEGY` — general AoE2 strategic knowledge, models, decision theory, competitive causality, and the Layer 2 curriculum.

`03_HD_ARCHAEOLOGY` — extracted HD source, rule corpus, explicit/implicit/meta reconstruction, and evidence records.

`04_PROMISORY` — Promisory/ADPromisory research substrate and qualification evidence; never assumed canonical.

`05_PORPHYRA` — canonical control baseline and subsequent controlled Porphyra implementation history.

`06_REPLAYS` — replay-derived empirical evidence and match analysis.

`07_NATIVE_ENGINE` — local/native reverse-engineering evidence, hashes, Ghidra artifacts, signatures, call graphs, and reports that may legally be preserved.

`08_AEGIS_ARCHITECTURE` — system architecture, interfaces, state models, execution contracts, verification and recovery design.

`09_BYZANTINE_DOCTRINE` — Byzantine-specific strategic doctrine after general Layer 2 knowledge is established.

`10_EXPERIMENTS` — controlled experiments, hypotheses, results, failures, and lessons.

`11_TOOLCHAIN` — validators, parsers, deployment tooling, scripts, and reproducibility procedures.

`12_RESEARCH` — external research and supporting references.

`99_ARCHIVE` — superseded or uncertain material retained for provenance rather than active design.

## Canonicality

Canonical source is explicitly designated. Experimental source is never promoted by proximity or recency. Historical material may explain design intent without becoming implementation authority.

## Knowledge graph

Knowledge records should link evidence to interpretation and implementation: `evidence -> observed pattern -> inferred principle -> generalized law -> AEGIS abstraction -> implementation requirement -> machine interface -> experiment -> outcome`.

## Change discipline

Major changes should be traceable to a rationale and evidence. Destructive cleanup is permitted only when provenance and irrelevance are established. Otherwise material belongs in archive/review.

## Long-term objective

A new engineer should be able to enter the repository at the current layer and reconstruct the project's intellectual and technical state without relying on the original conversation transcript.
