# AEGIS Traceability Model

Every important implementation decision should be traceable in both directions.

## Backward trace

`implementation -> architecture requirement -> strategic principle -> evidence pattern -> source artifact`

This answers: **why does this code exist?**

## Forward trace

`source observation -> interpretation -> knowledge record -> strategic model -> architecture requirement -> machine interface -> validation -> runtime evidence`

This answers: **what did we learn, and where did it go?**

## Evidence classes

- Runtime observation
- Native verified behavior
- Native signature/cross-reference
- Native diagnostics
- Target-build script behavior
- Source archaeology
- Documentation/comments
- Model inference
- Hypothesis

## Promotion gates

Historical code is not automatically architecture. Architecture is not automatically runtime. Runtime is not automatically canonical. Each promotion requires evidence appropriate to the claim.

## Contradiction handling

When sources disagree, preserve both observations. Record the disagreement, identify the evidence class of each, and state the current resolution or uncertainty. Never silently reconcile contradictory evidence.

## Reproducibility requirement

Experiments that materially change project direction should preserve inputs, commands, version/build identity, output, interpretation, and conclusion. A negative result is valuable evidence and should remain searchable.

## Layer boundary

Layer 1 constrains what can be executed. Layer 2 determines what should be attempted. Byzantine doctrine specializes the general strategy. Implementation translates validated doctrine into Layer-1-compatible actions.

## Review question

Before merging a major design change, an engineer should be able to answer: What evidence justified it? What assumption does it introduce? What would falsify it? What machine capability executes it? How will runtime success or failure be observed?
