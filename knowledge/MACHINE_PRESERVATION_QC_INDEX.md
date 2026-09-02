# Machine Preservation QC Index

## Purpose

This index makes the Layer-1 preservation packet discoverable and prevents the project from treating individual documents as independent silos.

## Core chain

`MACHINE_ONTOLOGY.jsonl`
→ `MACHINE_KNOWLEDGE_MONOGRAPH_2026-09-02.md`
→ `MACHINE_EVIDENCE_MATRIX_2026-09-02.md`
→ `MACHINE_ARCHITECTURAL_CONSEQUENCES_2026-09-02.md`
→ `MACHINE_RECONSTRUCTION_PROCEDURE.md`
→ `MACHINE_INVESTIGATION_HISTORY.jsonl`
→ `MACHINE_QC_EXPANSION_2026-09-02.md`
→ `MACHINE_QC_SECOND_ORDER_2026-09-02.md`
→ `LAYER1_REENTRY_EXAMINATION.md`
→ `MACHINE_QC_SIGNOFF_MATRIX.md`

## Preservation layers

### Descriptive
What the machine appears to contain.

### Evidentiary
Why each claim is believed and what class of evidence supports it.

### Causal
How machine components interact and how state transitions propagate.

### Operational
How an engineer uses the machine safely and reproducibly.

### Architectural
What constraints the machine imposes on AEGIS design.

### Epistemic
What is known, inferred, contradicted, obsolete, or unresolved.

### Re-entry
Whether an independent engineer can reconstruct the above without conversational context.

## Current conclusion

The Layer-1 packet is now substantially more complete than the initial preservation pass. The remaining work is primarily integration and proof closure: exhaustive UP ledger population, targeted native call-graph verification, controlled scheduler experiments, replay/state alignment, and cross-linking evidence dependencies.

The project should not confuse “preservation-complete enough to continue” with “every native implementation detail reverse engineered.” Those are different milestones.
