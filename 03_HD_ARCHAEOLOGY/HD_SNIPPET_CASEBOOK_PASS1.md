# HD/2013 Snippet Casebook — Pass 1

**Purpose:** publish small, isolated excerpts that demonstrate reconstructed semantics without reproducing the historical source tree.

**Source identity:** `AI (HD version).per`  
**Source SHA-256:** `8a554a90a18f7983a949f7bef3b767e09732bce87dca3b9546fe782f098de51c`

## 1. Position becomes strategic state

Approx. source lines 5252–5262:

```lisp
(up-compare-goal position-goal != pocket)
=>
(set-goal position-goal pocket)
(set-goal strategy-goal pocket-strategy)
(set-goal unit-goal pocket-unit)
(set-goal control-goal 0)
```

**Demonstrates:** spatial classification is an upstream strategic control input. It can immediately select both strategic mode and military capability.

**Evidence:** CONFIRMED / ENGINE-SPECIFIC.

## 2. Retreat is a coordinated lifecycle transition

Approx. source lines 32578–32595:

```lisp
(set-goal retreat-now-goal 1)
(set-goal attack-status-goal retreat)
(set-goal attack-goal 0)
(enable-timer attack-timer 60)
(set-goal reset 1)
```

**Demonstrates:** retreat modifies several control registers and installs temporal hysteresis. It is not equivalent to a single “enemy stronger” predicate.

**Evidence:** CONFIRMED.

## 3. Resource reservation

Approx. source lines 14765–14775:

```lisp
(set-strategic-number sn-resource-control 2)
```

**Demonstrates:** resource control is represented as an explicit reservation/priority channel that later rules consume.

**Evidence:** CONFIRMED / ENGINE-SPECIFIC.

## 4. Feasibility before construction

Approx. source lines 16006–16014:

```lisp
(up-pending-objects c: dock < 6)
(can-build dock)
=>
(build dock)
```

**Demonstrates:** construction is gated by pending-object state and engine feasibility rather than assuming an issued command is immediately completed.

**Evidence:** CONFIRMED / ENGINE-SPECIFIC.

## 5. Failed infrastructure changes the plan

Approx. source lines 16016–16026:

```lisp
(not (can-build dock))
...
(can-build barracks)
=>
(build barracks)
(set-strategic-number sn-number-explore-groups 3)
```

**Demonstrates:** failure of one infrastructure path can redirect production while simultaneously changing information-gathering capacity.

**Evidence:** CONFIRMED.

## Publication rule

These excerpts are evidence exhibits. They must never be expanded into a substitute copy of the historical source. The public repository preserves derived understanding, provenance, and minimal demonstrations; complete historical/vendor-derived source remains outside the public repository.
