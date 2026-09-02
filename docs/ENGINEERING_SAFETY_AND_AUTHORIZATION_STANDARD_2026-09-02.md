# AEGIS Engineering Safety & Authorization Standard — 2026-09-02

## Purpose

This standard is a mandatory project-control layer for AEGIS native archaeology, reverse engineering, replay research, and repository publication.

The project must be useful **without becoming careless**. Technical capability does not establish authorization. An analysis result does not automatically establish a publication right.

The governing rule is:

> **Do not perform, retain, publish, or operationalize an action unless its technical purpose, authorization basis, and publication boundary are understood. When uncertain, stop the risky path and preserve only the minimum safe research record.**

## 1. Scope

This standard applies to:

- Ghidra and other native-analysis work;
- locally obtained game executables and supporting binaries;
- disassembly, decompilation, strings, metadata, symbols, and memory maps;
- replay extraction and parser research;
- runtime experiments;
- scripts that inspect or transform local artifacts;
- GitHub commits and repository history;
- derived documentation, measurements, and datasets;
- any future tool or connector introduced into the project.

## 2. Authorization boundary

The project assumes only the authority actually established by the available facts.

Possession of an executable is not treated as blanket permission to redistribute it, publish extracted proprietary code, disclose private material, or bypass access controls.

The investigation may analyze a locally obtained artifact when that analysis is within the user's authorized environment and applicable rules. If authorization becomes uncertain, the operation is paused rather than rationalized.

No project document may state or imply that reverse engineering, copying, publication, or redistribution is legally permitted merely because a tool can technically perform it.

## 3. Ghidra safety rule

Ghidra is an analysis instrument, not a source of automatically publishable material.

Native-analysis output is classified before entering project documentation:

1. **Safe derived observation** — original description, measurement, hash, address/range, or methodology that does not reproduce substantial proprietary material.
2. **Restricted evidence** — executable-derived content retained locally because it is useful for investigation but not suitable for public publication.
3. **Unresolved** — rights or sensitivity cannot presently be established; publication is prohibited until resolved.

The preferred public representation of proprietary native archaeology is:

`LOCAL EXECUTABLE -> CONTROLLED ANALYSIS -> ORIGINAL OBSERVATION -> ORIGINAL TECHNICAL DESCRIPTION`

not:

`LOCAL EXECUTABLE -> BULK EXTRACTION -> PUBLIC REDISTRIBUTION`

## 4. Prohibited default publication

Without an established publication basis, do not publish:

- copies of the game executable or DLLs;
- bulk binary dumps;
- substantial decompiled or disassembled proprietary code;
- private symbols or proprietary source recovered through analysis;
- game assets or other redistributable files extracted from the installation;
- credentials, tokens, keys, account information, or private identifiers;
- private correspondence or unrelated personal information;
- raw replay collections where ownership/privacy/publication status is unclear.

A useful engineering conclusion should instead be preserved as an original summary, measurement, hash, provenance record, or appropriately scoped reference whenever that preserves the research value.

## 5. Evidence and rights are independent

Every publication decision requires two gates:

**Evidence gate:** Is the technical claim actually demonstrated?

**Rights gate:** Is the proposed representation authorized and appropriate to publish?

Passing one gate never substitutes for passing the other.

A technically certain result can remain private. A legally publishable artifact can remain scientifically weak.

## 6. Native-analysis evidence discipline

The following distinctions are mandatory:

- native vocabulary is not implementation proof;
- a decompiler rendering is not verified source;
- a string reference is not a call graph;
- a recovered address is not automatically a public identifier;
- a parser field is not automatically native state;
- a failed search is not proof of absence;
- a technical capability is not authorization;
- local access is not redistribution permission.

Critical conclusions require the evidence ladder defined by the Layer 1 completion controls.

## 7. Tool-operation safety

Before a new invasive or destructive operation, establish:

1. exact target;
2. purpose;
3. authorization basis;
4. expected side effects;
5. rollback or preservation method;
6. publication classification;
7. independent verification method.

Never overwrite the only copy of a source artifact or historical analysis project. Preserve hashes and provenance before transformation. Use disposable analysis projects where practical.

Destructive repository operations require a verified backup/provenance record and a post-operation independent check.

## 8. Repository publication gate

The existing `PUBLICATION_AND_RIGHTS_CONTROL_STANDARD_2026-09-02.md` remains authoritative for publication classes P0–P6.

This standard adds the operational requirement that **uncertainty itself is a blocking condition** for publication of sensitive material.

When rights are unclear, publish the research conclusion in original wording without the restricted underlying artifact, if the conclusion can safely and legitimately be communicated that way.

## 9. Reverse-engineering output retention

Restricted native artifacts may be retained in the controlled local investigation environment when needed for reproducible analysis and authorized handling.

They should not be copied into the public repository merely to make the investigation convenient.

Public documentation should record enough provenance for another engineer to understand what was examined without requiring redistribution of the examined proprietary artifact.

## 10. Runtime experiments

Runtime experimentation must remain within the authorized local environment and must avoid unnecessary interaction with third-party services, accounts, or systems.

Experiments must identify:

- build identity;
- experiment purpose;
- controlled inputs;
- observed outputs;
- side effects;
- safety constraints;
- evidence classification.

No experiment is justified solely because it might reveal an interesting mechanism.

## 11. Personal and third-party data

Replay files, logs, screenshots, and diagnostics are treated as potentially sensitive until inspected.

Before publication, check for:

- player/account identifiers;
- chat;
- local filesystem paths;
- machine names or identifiers;
- timestamps that are unnecessarily identifying;
- private metadata;
- third-party recordings or fixtures.

Sanitize or withhold material when the research objective does not require disclosure.

## 12. Professional stop conditions

The engineer must stop and reassess when:

- authorization is unclear;
- publication rights are unclear;
- the operation could expose secrets or personal information;
- the only available evidence would require publishing restricted material;
- an analysis method risks modifying the authoritative source artifact;
- a destructive Git operation lacks a verified recovery path;
- a conclusion depends on an unsupported semantic assumption;
- tool output is being mistaken for proof.

Stopping is a successful engineering control, not a project failure.

## 13. Documentation requirement

Every significant native investigation record must state:

- what artifact was examined;
- how it was obtained, at the level safely recordable;
- exact build/hash where appropriate;
- tool and analysis configuration;
- what was observed;
- what was inferred;
- what remains unknown;
- whether the resulting artifact is public, restricted, or withheld;
- why the public representation is appropriate.

Corrections must amend the record rather than conceal prior uncertainty or failed experiments.

## 14. Legal-review boundary

This document is an engineering control, not legal advice and not a determination of legal rights.

Questions involving copyright, license terms, contracts, reverse-engineering exceptions, interoperability, privacy, jurisdiction, or redistribution rights may require qualified legal review.

Where such a question is material and unresolved, the conservative project action is to withhold the disputed material and preserve only a safe provenance/technical record.

## 15. Final engineering principle

The project's standard is deliberately higher than "technically possible."

The engineer is responsible for three separate questions:

1. **Can we do it?**
2. **Are we authorized to do it?**
3. **Is it responsible to retain or publish the result in this form?**

Only when the applicable answers support the action should the action proceed.

> **Capability is not permission. Evidence is not ownership. Usefulness is not justification. Responsible engineering requires all three boundaries to be respected.**
