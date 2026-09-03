# LAYER 1 — NATIVE PASS: `.PER`-FIRST CAUSAL RECOVERY

Date: 2026-09-03
Status: ACTIVE / NOT COMPLETE
Working completion estimate: 89%

## Scope correction

ByzBot is a pure `.per` project. XS is outside the implementation scope and is not a Layer 1 completion dependency. Native XS observations may remain as machine archaeology, but they must not drive implementation priorities or be represented as ByzBot requirements.

The governing predictive standard already states that XS and XS qualification are excluded from project scope. This pass therefore treats the `.per` AI path as the sole implementation-facing frontier.

## Controlled executable baseline

SHA-256: `6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4`.
Image base: `0x140000000`.

Section mapping was independently re-read from the PE header during this pass:

- `.text`: RVA `0x1000`, raw `0x400`, raw size `0x313A000`.
- `.rdata`: RVA `0x313C000`, raw `0x313AC00`, raw size `0xBF6A00`.
- `.pdata`: RVA `0x4C30000`, raw `0x41DCC00`, raw size `0x1E8800`.

All future raw/VA conversion must be section-aware.

## Targeted reference experiment

The native source/debug strings for `loadRules`, `Defining Fact`, `Defining Action`, `Evaluating Persistent Facts`, `Next Rule:`, `CurrentAction`, `CurrentOrder`, `processNotify`, and `Action %d has failed` were located in `.rdata`.

A fresh executable-wide scan tested the most likely direct RIP-relative forms used for references to these strings. The tested representation produced zero direct RIP-relative consumers for all selected targets.

This is a valid negative result only for the tested representation. It does not prove the strings are unused, nor does it prove that the corresponding code is indirect. Possible alternatives include indexed/relocated tables, indirect diagnostic infrastructure, folded/dead diagnostic strings, or other reference encodings.

## Consequence for native archaeology

The source-path/debug-string corpus is strong semantic vocabulary but is no longer treated as a reliable function-address locator by itself.

The investigation must therefore move from string anchoring to structural anchors:

1. verified `.pdata` function boundaries;
2. data structures that contain rule state;
3. constants/IDs used by rule operations;
4. native control-flow patterns surrounding state reads/writes;
5. calls into known AI modules;
6. runtime experiments that distinguish competing causal models.

## `.per` causal spine

The implementation-facing model is:

`.per source`
→ lexical/preprocessor handling
→ rule construction
→ rule storage
→ scheduling
→ fact evaluation
→ rule selection/firing
→ handler/action
→ native AI control
→ UnitAI
→ simulation
→ observable feedback.

The arrows remain individually graded. Vocabulary adjacency does not promote an arrow to implementation evidence.

## High-value discovery in the native corpus

The AIExpert region contains a broad semantic vocabulary that is useful for locating state boundaries even when direct string references are unavailable. It includes:

- `loadRules` and explicit parsing-success/failure diagnostics;
- `Defining Constant`, `Defining Fact`, and `Defining Action`;
- `ruleElementsPtr`, indexed `rule[j].element`, and `ruleDebugInfo[j]`;
- persistent-fact evaluation start/completion diagnostics;
- `Next Rule`, rule-jump bounds checks, and breakpoint/debugger vocabulary;
- explicit invalid goal, point-goal, comparison, unit-type, building-type, timer, player, resource, and search-source failures.

This establishes a useful semantic map of the native rule engine but not its complete implementation graph.

## Practical `.per` implication

The native interface exposes derived predicates such as `can-build`, `can-research`, and `can-train`, alongside resource, population, research, player, timer, unit, building, and strategic-number state.

ByzBot should not duplicate native mechanisms merely because they are easy to reimplement. The eventual design should explicitly classify each machine capability as one of:

- trusted observation;
- trusted native control surface;
- compensating wrapper;
- strategic logic that must live in `.per`;
- unresolved capability requiring experiment.

## UnitAI frontier

The native UnitAI corpus contains a separate vocabulary for orders, actions, targets, notifications, search, pathing, retry, retargeting, and completion/failure. The strongest remaining promotion target is an actual native mutation chain:

`CurrentOrder/CurrentAction read`
→ condition or transition
→ state write
→ downstream consumer
→ observable result.

Until this is recovered, the order/action distinction remains strong architectural evidence rather than a complete class/ownership reconstruction.

## QC result

No new implementation-level `.per` causal edge was promoted in this pass. That is intentional. The pass produced stronger negative evidence against the current direct-string-xref method and a cleaner structural research strategy.

The working completion estimate remains 89%. No percentage increase is justified merely by additional negative evidence.

## Next discriminating experiments

### Experiment A — rule-state structural anchor
Recover `.pdata` function ranges around candidate AI code regions and identify functions that repeatedly access compact rule-state fields or rule-index-like values. Promote only when a coherent read/branch/write chain is established.

### Experiment B — persistent-fact boundary
Search for the native state transition that produces the persistent-fact result, using the fact ID/value diagnostic region only as semantic corroboration rather than an address anchor.

### Experiment C — UnitAI mutation
Use native diagnostics and known UnitAI field vocabulary to locate a verified mutation of `CurrentAction` or `CurrentOrder`, then follow its consumer.

### Experiment D — runtime falsification
Construct the smallest `.per` rule whose observable behavior distinguishes two competing hypotheses about evaluation order, persistence, or action conflict. Use runtime output/replay evidence to falsify one model.

## Evidence policy

Promoted: section-aware PE mapping; `.pdata` membership for verified function boundaries; coherent disassembly of independently validated functions; native AIExpert and UnitAI vocabulary; negative direct-RIP-reference results for the tested string-reference representation.

Quarantined: source-string adjacency as execution order; string address as function address; broad naming-based call-graph claims; malformed targeted disassembly; XS dispatch hypotheses as ByzBot implementation requirements.

## Next pass target

The next pass should be a structural `.per` archaeology pass, not an XS pass: recover one verified AIExpert rule-state function or one UnitAI state mutation chain. The preferred outcome is a single causal edge with a demonstrable read → decision → write → consumer sequence.
