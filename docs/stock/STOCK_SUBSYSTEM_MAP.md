# Stock Subsystem Map

This is the living reconstruction index for the stock AI substrate. It is deliberately separate from the final AEGIS architecture.

| Stock subsystem | Primary evidence | Reconstructed responsibility | Cross-system consumers | Status |
|---|---|---|---|---|
| `gatherers` | stock source + machine topology | worker/economic state machine | economy, construction, resource control | DECONSTRUCTING |
| `dawn` | stock source | allocation/reconciliation of worker roles | gatherers/economy | DECONSTRUCTING |
| `buildings` | stock source + topology | construction/placement OS | economy, threat, production | DECONSTRUCTING |
| `researches` | stock source + topology | research/age policy and authorization | strategy, economy, military | DECONSTRUCTING |
| `boarhunting` | stock source | dedicated food acquisition lifecycle | economy, workers | DECONSTRUCTING |
| `scoutcontrol` | stock source | information/scouting control | threat, military, strategy | DECONSTRUCTING |
| `threats` | stock source | threat sensing/response signals | construction, military, economy | DECONSTRUCTING |
| `tsa` | stock source | tactical/military control | threat, production, scouting | DECONSTRUCTING |
| `trade` | stock source | trade economy | economy, strategy | DECONSTRUCTING |
| `watercontrol` | stock source | water/naval support | navy, economy | DECONSTRUCTING |
| `units` | stock source | unit production/role control | military, economy | DECONSTRUCTING |
| `general` | stock source | shared/general AI services | multiple | DECONSTRUCTING |
| `interaction` | stock source | cross-player/cooperation behavior | strategy, military | DECONSTRUCTING |
| `escrow` | stock source | protected resource reservation/control | production, research, economy | DECONSTRUCTING |

These labels are reconstruction hypotheses backed by source topology; exact execution semantics require evidence appropriate to the claim.
