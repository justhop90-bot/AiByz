# AEGIS Coding Posture - Descriptivist Engine-First Constraint Exploration

Date: 2026-09-06
Status: Engineering standard

## 1. Rule

AEGIS treats the target AoE2:DE engine as the descriptive authority for what the machine actually accepts and does. Static validators, public references, style conventions, and historical scripting guidance are prescriptive evidence about expected usage, not proof of the complete target-build language.

The engineering question is not merely what should this script contain? It is what exact syntax, operands, state transitions, and side effects does the target machine accept and produce?

## 2. Constraint hierarchy

1. Target-build runtime observation
2. Reproducible machine-level evidence
3. Static parser/validator acceptance
4. Official/public documentation
5. Community convention and historical examples

Lower levels remain useful. None silently overrides higher-level evidence.

## 3. Push constraints, do not erase them

When a validator rejects a construct, AEGIS does not automatically rewrite the construct to satisfy the validator. First determine whether the validator is narrower than the engine. Build the smallest controlled experiment that can distinguish engine-invalid; validator-invalid but engine-valid; syntactically accepted but semantically different; accepted and semantically equivalent; or unresolved/UNKNOWN.

A validator failure is therefore a hypothesis about the machine, not the machine itself.

## 4. Native-language posture

`.per` is treated as a constrained native rule/state-machine language. Coding decisions must follow observed grammar, evaluation order, goal/fact typing, numeric domains, rule scheduling, and side effects. C/C++/Python intuitions are not imported unless experimentally justified.

Do not normalize unusual native constructs merely because they look inelegant. Preserve them when they are machine-valid and architecturally useful.

## 5. Evidence discipline

Pushing the limits does not mean promoting guesses. Every aggressive construct receives an evidence label: STATIC_ONLY, PARSER_ACCEPTED, LOADED, EXECUTED, SEMANTICALLY_PROVEN, or UNKNOWN.

Architecture may use a construct provisionally, but production promotion requires the evidence level required by that interface.

## 6. Practical consequence for AEGIS

For engine-facing adapters, prefer the narrowest experiment that exposes actual machine behavior. Keep the validator in the loop as a regression detector, but never let validator conformity become a substitute for target-build qualification.

The objective is maximum demonstrated capability inside the actual machine constraints.
