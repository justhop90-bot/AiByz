# Replay Knowledge — Second-Order Six-Month QC

## Scope
Audit the GitHub replay knowledge layer for omissions, weak claims, missing provenance, measurement hazards, and opportunities for deeper generalization.

## Current inventory
The replay knowledge branch currently contains the event model, calibration triple-pass record, ACTION schema registry, and ACTION schema adjudication. The branch is therefore a documented research foundation, not yet a complete empirical replay corpus.

## Findings

### 1. Version the ontology itself
Event families and semantics need explicit schema versions. A future parser change must not silently alter historical interpretations.

### 2. Separate parser schema from AEGIS schema
`mgz-fast` payload structure is an instrument-level representation. AEGIS normalized events should be a separate contract with explicit transforms.

### 3. Preserve parser source location
Each promoted field should identify the parser function/module responsible for decoding it.

### 4. Add raw-record locators
Normalized events need record sequence and source-file locator so a researcher can jump back to the original evidence.

### 5. Hash every calibration artifact
The calibration corpus needs replay SHA-256, parsed-body SHA-256, header SHA-256, and parser snapshot hash.

### 6. Add corpus membership manifest
The eight-game calibration set should have one machine-readable manifest defining exact membership and inclusion rationale.

### 7. Distinguish calibration from validation
The same replay must not silently serve as both schema-discovery evidence and unbiased validation evidence.

### 8. Add held-out validation
Reserve recordings that were not used to formulate a schema, then test the schema against them.

### 9. Add command rarity handling
Rare commands require different confidence treatment from high-frequency commands; absence is not evidence of impossibility.

### 10. Add payload optionality statistics
For every command, measure field presence frequency, null/default frequency, and co-occurrence patterns.

### 11. Add malformed/unknown preservation
Unknown command or payload forms must survive normalization unchanged and enter a quarantine stream rather than disappear.

### 12. Add semantic field confidence
Confidence belongs at field level, not only event level. A command can be known while one field remains uncertain.

### 13. Add dependency graph
Document which normalized fields depend on which raw fields and parser assumptions.

### 14. Add invariant testing
Candidate invariants such as SYNC/VIEWLOCK relationships should become executable tests, with counterexamples retained.

### 15. Add metamorphic tests
Where replay semantics imply relationships, test transformations such as reordering independent events, repeated observation, or equivalent command encodings.

### 16. Add temporal uncertainty intervals
When exact simulation time is unavailable, represent bounds rather than inventing a timestamp.

### 17. Add clock-domain documentation
Explicitly distinguish replay sequence, simulation tick, synchronization cadence, recording time, and wall-clock timestamps.

### 18. Add causality confidence
Causal edges should carry evidence strength and alternative explanations.

### 19. Add negative controls
Early termination, anomalous, observer-only, and low-information recordings should be retained as tests of uncertainty handling.

### 20. Add positive controls
Use recordings with independently obvious events to verify that reconstruction detects what it should.

### 21. Add lifecycle state machine
Object lifecycle reconstruction should be an explicit finite-state model with legal and illegal transitions.

### 22. Add production state machine
Production should distinguish command, queue admission, cancellation, completion, and battlefield availability.

### 23. Add resource conservation checks
Where resource observations permit, test conservation-style equations and report residual error rather than forcing equality.

### 24. Add map-coordinate normalization
Spatial analysis must be map-aware and must not treat raw coordinates as portable strategic locations.

### 25. Add visibility masks
An observed absence must be classified against what the observing player could actually see.

### 26. Add player-perspective reconstruction
Strategic analysis should be performed from each player's information set, not only omniscient replay state.

### 27. Add decision opportunity sampling protocol
Define exactly how candidate decision points are selected to avoid cherry-picking dramatic moments.

### 28. Add action-set reconstruction
At each decision point, reconstruct feasible alternatives separately from the chosen action.

### 29. Add outcome windows
Define short-, medium-, and long-horizon outcome windows before looking at results.

### 30. Add attribution protocol
Separate temporal correlation, mechanical consequence, strategic consequence, and causal attribution.

### 31. Add counterfactual limits
Record when alternative-action evaluation is identifiable, partially identifiable, or speculative.

### 32. Add calibration metrics
Prediction systems should eventually report Brier score, log loss, reliability/calibration curves, and confidence-stratified accuracy where probabilities are emitted.

### 33. Add distribution-shift detection
Game version, map, civilization, player count, skill, and game mode can change event distributions and strategic meaning.

### 34. Add civ-specific overlays
General AoE2 event semantics should remain separate from civilization-specific strategic interpretation.

### 35. Add player-skill stratification
Observed human choices should not automatically become optimal-policy labels.

### 36. Add decision-quality vs outcome-quality distinction
Winning does not prove the decision was optimal; losing does not prove it was irrational. Evaluation must use the information set available at decision time.

### 37. Add regret and robustness
A decision should be evaluated against plausible alternatives and uncertainty intervals, not only the realized path.

### 38. Add commitment/optionality accounting
Strategic actions should record resource cost, time cost, production lock-in, and reversibility where measurable.

### 39. Add initiative-transfer detection
Identify actions that force an opponent response and quantify response latency.

### 40. Add conversion-tax measurement
Eventually quantify the resources, production capacity, time, map control, and attention imposed on an opponent by a commitment. This is the empirical bridge to Byzantine doctrine.

### 41. Add transition-denial measurement
Measure whether an action actually delayed, weakened, redirected, or prevented an opponent transition.

### 42. Add parser regression corpus
Every discovered parser edge case should become a permanent regression fixture.

### 43. Add source-to-knowledge traceability
Each strategic principle derived from replay evidence should link backward to events and ultimately to raw recordings.

### 44. Add claim status lifecycle
Claims should move through: OBSERVED → REPLICATED → CROSS-VALIDATED → GENERALIZED → CALIBRATED, with explicit demotion paths.

### 45. Add reproducibility recipe
A future researcher should be able to regenerate every published replay-derived table from the preserved raw artifacts, parser snapshot, and deterministic scripts.

### 46. Add computational environment capture
Record Python version, operating system, dependencies, parser commit/hash, locale, and relevant configuration.

### 47. Add schema migration policy
Never mutate an old interpretation in place. Create a new schema/version and record the migration transform.

### 48. Add uncertainty budget
Every reconstructed strategic variable should expose uncertainty contributed by parser ambiguity, missing observations, time ambiguity, identity ambiguity, and model assumptions.

### 49. Add cross-replay replication thresholds
Define how many independent recordings and how much diversity are required before a semantic rule is promoted.

### 50. Add six-month return test
A future researcher must be able to answer: What was observed? How was it decoded? What was assumed? What was unknown? Why was this interpretation chosen? What would falsify it? How can I regenerate it?

## QC verdict
The GitHub replay layer is structurally sound but should be treated as **research-foundation / pre-authoritative** until the held-out validation, object lifecycle, temporal adjudication, corpus manifest, and reproducibility machinery are implemented.

The most important architectural extrapolation is that replay analysis should become a **measurement science subsystem** rather than a collection of summaries. The replay corpus will eventually support runtime regression, strategic-policy evaluation, belief calibration, transition prediction, and empirical measurement of conversion tax.

## Immediate next implementation gate
1. Build canonical corpus manifest and hashes.
2. Freeze calibration/held-out split.
3. Generate corrected ACTION schema statistics from the preserved parsed streams.
4. Build temporal adjudication report.
5. Build object lifecycle ledger.
6. Build production lifecycle ledger.
7. Add executable validation/invariant tests.
8. Only then begin full 156-game normalization.
