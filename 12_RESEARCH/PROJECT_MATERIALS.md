# Project Materials & Source Provenance

## Purpose

This section records the materials that constitute the AEGIS research substrate.
It is deliberately broader than the runtime source tree: source artifacts,
research artifacts, replay evidence, native-engine evidence, generated analyses,
and historical fossils all matter to institutional memory.

The repository is the durable record of what we learned from those materials,
not merely a copy of the files used to build the current bot.

## Material classes

### 1. Canonical project source

Project-owned source that is authorized to define current implementation or
architecture. These materials receive explicit authority labels and hashes.

### 2. Strategy source / fossils

Historical AI implementations used to recover strategic knowledge. V3 is a
strategy fossil; the HD/2013 AI is the principal archaeology specimen. Historical
source is evidence for reasoning, not automatic implementation authority.

### 3. Research substrate

Promisory/ADPromisory and related experimental material. These artifacts are
useful for discovering possible engine capabilities and architectural ideas but
are not authoritative merely because they are sophisticated or newer.

### 4. Machine evidence

Native executable metadata, hashes, strings, extracted signatures, Ghidra
projects/reports, diagnostics, loader evidence, scheduler evidence, and other
engine-forensics artifacts.

### 5. Empirical evidence

Replay files, parsed replay data, test results, validator reports, controlled
experiments, and observed runtime behavior.

### 6. Derived knowledge

Ledgers, control maps, archaeology reports, state graphs, quantitative profiles,
hypotheses, lessons, and cross-validation records produced from the source
materials.

## Newly supplied materials — 2026-09-02

### HD AI source packages

`AI (HD version).zip` and `AI (HD version) (2).zip` each contain the same logical
source file, `AI (HD version).per`, but the ZIP containers themselves have
different hashes. The extracted source SHA-256 is the identity used for research.

- `AI (HD version).per`
- Size: 1,167,238 bytes
- SHA-256: `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`
- Source identity: official HD/2013 Edition AI; source comment attributes it to
  Promiskuitiv and Archon.

ZIP container hashes:

- `AI (HD version).zip`: `a3687ba15ce1e069ec91c617f7486b8b42773becad06806dfe9414456542f796`
- `AI (HD version) (2).zip`: `dab1682d387741700ee3820202ff719f62ddc2dd320612f8fe723dc7e0e9b44f`

### Promisory package

`Promisory.zip` contains 37 ZIP entries, including the Promisory `.per` research
modules used by the HD source and AEGIS archaeology. The complete per-file
inventory and hashes are recorded in `SOURCE_MATERIAL_INVENTORY.json`.

- ZIP size: 492,581 bytes
- ZIP SHA-256: `a81785575ebe4715eeb3ab5feaf518ee4617a11b3f079b694ec668c8aa7baf29`
- Entries: 37 (including the directory entry)

## Public-repository handling

Some supplied materials are historical/vendor-derived AoE2 AI source rather than
new AEGIS-owned implementation. Because this repository is public, raw stock or
third-party source is not mirrored here merely for convenience. Instead, this
repository preserves cryptographic identity, provenance, structural facts,
research outputs, methodology, and references sufficient to connect the public
knowledge record to the locally preserved artifact.

If raw source ever needs to be versioned, that should occur only in an explicitly
authorized private repository or other controlled store.

## Authority rule

A material's presence in this registry does not make it canonical. Authority is
assigned separately by the project constitution and layer-specific contracts.

`material -> provenance -> evidence -> interpretation -> validation -> authority`

## Returnability standard

A future engineer must be able to determine:

- what material was used;
- which exact artifact/version was used;
- how its identity was verified;
- what was learned from it;
- what was inferred rather than observed;
- what remains uncertain;
- where the raw artifact is preserved;
- and how to reproduce the analysis.
