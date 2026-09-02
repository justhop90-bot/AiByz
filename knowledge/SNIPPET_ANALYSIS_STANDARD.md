# Historical Snippet Analysis Standard

Small historical excerpts are permitted as **evidence exhibits** when they materially clarify a reconstructed idea. They must never become a substitute for the original source or a disguised source dump.

## Exhibit format

### Claim
State the exact engineering or strategic claim.

### Source
Identify historical implementation and approximate source location.

### Excerpt
Use only the smallest contiguous fragment necessary to make the behavior intelligible.

### Annotation
Explain the important predicates, state writes, timers, self-disable behavior, or actions.

### Control interpretation
Describe:

`observation -> classification -> state -> authority -> action -> expected consequence`

### Strategic interpretation
Explain what game problem the behavior appears to solve.

### Designer interpretation
Explain what substrate constraint or engineering tradeoff may have shaped the implementation.

### Generalization
Rewrite the insight independently of the historical syntax.

### AEGIS consequence
State what the project should preserve, generalize, replace, or reject.

### Confidence
Use an explicit epistemic status and evidence strength.

## Example pattern

A tiny historical rule that changes an internal strategy state after observing an enemy commitment can demonstrate a general principle such as:

> **Enemy observations become persistent state before downstream action.**

The important knowledge is not the copied syntax. It is the control architecture:

`enemy evidence -> classification -> persistent state -> downstream strategic response`

The excerpt exists only to prove that the historical implementation actually used that pattern.

## Anti-patterns

Do not publish:

- whole historical modules;
- long contiguous rule families when a small representative example suffices;
- complete constant tables;
- copied stock infrastructure renamed as AEGIS;
- source dumps whose explanation is thinner than the code;
- excerpts without provenance;
- excerpts presented as universal truth when they are heuristics.

## Preferred depth

A strong exhibit spends more words on **why** than on **what the syntax says**.

The reader should finish knowing the decision logic even if the historical source itself is removed from the page.
