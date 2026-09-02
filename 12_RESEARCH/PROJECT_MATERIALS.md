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

Promisory/ADPromisory and related experimental material. These artifacts are useful
for discovering possible engine capabilities and architectural ideas but are not
authoritative merely because they are sophisticated or newer. Complete source
remains quarantined outside the public repository.

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
materials. This class is actively expanded and is the principal long-term value
of the public repository.

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

`Promisory.zip` contains 37 ZIP entries, including the directory entry. The
complete per-file inventory and hashes are recorded in `SOURCE_MATERIAL_INVENTORY.json`.

- ZIP size: 492,581 bytes
- ZIP SHA-256: `a81785575ebe4715eeb3ab5feaf518ee4617a11b3f079b694ec668c8aa7baf29`
- Entries: 37 (including the directory entry)

## Public quarantine decision — 2026-09-02

The following material was present on the knowledge branch but is now removed from
the public tree because it is source-derived or otherwise unsuitable for public
redistribution:

- `ADPromisory/` — complete tree removed.
- `AiBuilder/` — complete tree removed.
- `ByzantineWarCouncil.per` — removed.
- `ByzantineWarCouncil.ai` — removed.

The private/local research specimens remain the evidence substrate where available.

**Important:** substantial editing does not, by itself, establish clean provenance.
If a file is derived from stock, historical, vendor, or restricted source, it remains
quarantined unless redistribution rights are established.

## Knowledge-first publication rule

We can publish the **knowledge about the code** at high density:

- rules and their purposes;
- facts/goals/strategic-number usage;
- control-flow patterns;
- state-machine reconstruction;
- strategic and tactical principles;
- economic reasoning;
- timer/hysteresis behavior;
- failure and recovery logic;
- engine limitations and workarounds;
- designer tradeoffs;
- historical evolution;
- experiments and negative results;
- generalized algorithms and schemas;
- small, isolated, attributed snippets when they materially explain an idea.

We do not need to publish the source implementation itself.

## Preferred evidence pattern

`small excerpt -> annotation -> observed behavior -> designer/problem interpretation -> general principle -> AEGIS abstraction -> independent implementation`

A reader should be able to understand the idea even if the excerpt is removed.

## History warning

Removal from the current branch tree does not erase previously committed Git blobs.
Historical source-object removal, if desired, requires an explicit history-rewrite
operation followed by verification.

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
