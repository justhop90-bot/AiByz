# Resource Preservation — Six-Month Recovery Inventory

## Canonical local resources
- AoE2DE executable: `C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe`
- Current replay/savegame root: `C:\Users\justh\Games\Age of Empires 2 DE\76561198093432383\savegame`
- Calibration corpus: `...\savegame\AEGIS_CALIBRATION_DATA`
- Project lab: `C:\Users\justh\Desktop\AEGIS-AI-LAB`
- Ghidra: `C:\Ai tool requests\ghidra_12.1.3_PUBLIC_20260817\ghidra_12.1.3_PUBLIC`
- Java runtime: `C:\Program Files\Eclipse Adoptium\jdk-25.0.4.101-hotspot\bin\java.exe`

## Critical replay artifacts
Preserve the eight-game calibration headers, bodies, and parsed JSONL streams. Preserve the complete replay corpus and the mgz-fast snapshot. Do not rely solely on derived summaries when raw evidence can be recovered from the PC.

## Critical project artifacts
Preserve:
- PORPHYRA_V2_2_2 control baseline and independent hash manifest;
- canonical V3 source tree;
- V4 experimental tree separately;
- native-engine extraction and Ghidra project/logs;
- HD source and SHA-256;
- HD archaeology corpus;
- Layer-2 ontology/generalization/operationalization ledgers;
- replay action registry/adjudication;
- temporal semantics documents;
- object lifecycle documents;
- production lifecycle documents;
- validation and quarantine ledgers;
- provenance manifests.

## PC-to-GitHub rule
GitHub is institutional memory, not the sole raw-data store. Binary or large source artifacts should remain on controlled local storage where licensing/provenance requires it, with hashes, manifests, and reconstruction instructions in GitHub.

## Recovery rule
If conversation context disappears, recover from PC first. Use GitHub for derived knowledge, provenance, schema, conclusions, and instructions. Recompute derived artifacts from raw evidence when necessary rather than trusting stale generated files.

## Missing/expired conversation attachments
Some earlier conversation attachments have expired from the ChatGPT file context. This is not a loss of project state because the replay corpus and many source artifacts were recovered from the user's PC and the knowledge record is being preserved in GitHub. Any artifact not recoverable from PC/GitHub must be explicitly marked missing; never silently reconstruct it from memory.

## Preservation checksum policy
Every important raw artifact should have SHA-256. Every derived artifact should state source hashes, parser version, analysis date, and methodology. Experimental artifacts must retain their status and must never silently become canonical.

## Branch policy
The project has accumulated many experimental AEGIS branches. Do not create another branch merely to store a note. The six-month handoff branch is the designated handoff consolidation point. Branch cleanup should be performed only after inventory and without deleting the authoritative branch or PR history.

## Six-month test
A clean machine with only this repository, the documented PC paths, and recovered raw artifacts should be sufficient to reconstruct the research state, reproduce calibration, identify unknowns, and determine the next experiment.