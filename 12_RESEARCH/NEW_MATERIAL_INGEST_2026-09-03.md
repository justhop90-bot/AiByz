# New Material Ingestion — 2026-09-03

## Scope

This record captures the latest evidence set examined during the three-pass AiByz QC. The purpose is to preserve provenance and prevent future engineers from confusing supplied evidence with public-runtime authority.

## Supplied evidence classes

### Exact native runtime

- `AoE2DE_s.exe`
- Build/version: `101.103.48987.0`
- SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`
- PE32+, x86:LE:64
- Image base: `0x140000000`

### Stock AI/data material

- `gamedata_x2.zip`
- `ai (2).zip` / duplicate `ai.zip`
- `dat.zip`
- `xs.zip`

Important inspected components include:

- `gamedata_x2/PromiDE.per2`;
- `gamedata_x2/randomgame.per2`;
- `xs/ailib/Geometry.xs`;
- stock Promisory rule corpus;
- `dat/AIConsts.json`;
- `dat/unitlines.json`;
- Byzantine civilization/data references.

## Key measured result

Conservative recursive load/include analysis of the reachable stock AI graph produced:

- 28 reachable `.per/.per2/.xs` files;
- 7,831 syntactically reachable `defrule` definitions;
- conditional branches included conservatively;
- count is not an execution count for an individual game.

The older 7,715 figure is retired.

## Key semantic result

`PromiDE.per2` demonstrates a modular composition root that loads Promisory constants and rule modules and includes `ailib/Geometry.xs`. This strengthens the repository's model of the stock AI as a composed rule program with an XS capability surface.

## Data namespace result

`unitlines.json` establishes a line namespace distinct from concrete unit identifiers. The Knight Line is represented by line metadata and an ID chain. Therefore:

`unit ID != unit-line ID != unit class ID`

The prior `knight-line` validator dispute remains a runtime/validator contract question. It is not to be resolved by intuition alone.

## XS result

The supplied corpus and official World's Edge documentation independently establish AI XS support. XS can therefore be recorded as a real engine capability. It is not recorded as a mandatory AEGIS dependency.

## Public-source corroboration

Verified public sources used in QC include:

- World's Edge AoE2DE Update 87863 for AI XS support and XS goal/SN/persistence facilities;
- World's Edge AoE2DE Update 177723 for 2026 AI-engine and pathfinding fixes;
- World's Edge AoE2DE Update 42848 for strategic AI, targeting, and pathfinding fixes;
- World's Edge AoE2DE Update 58259 for AI garrison/retargeting behavior and scripting changes;
- AoE2 AI Scripting Encyclopedia for the broad command/fact/parameter/unit-line reference surface;
- Siege Engineers `aoc-reference-data` for structured reference-data corroboration;
- FreeAoE source as comparative evidence only.

## Publication boundary

Do not add the supplied executable, proprietary game binaries, or unrestricted source-derived artifacts to the public repository merely because they were inspected. Public records should contain reproducible findings, hashes, provenance, methodology, and permitted derived observations. Restricted artifacts remain in the controlled local lab.

## Authority rule

This ingestion record does not supersede the Layer 1 completion control, final handoff, or evidence matrix. It feeds them. Where the new material increases corroboration without closing a causal proposition, confidence may rise while the Layer 1 completion position remains unchanged.
