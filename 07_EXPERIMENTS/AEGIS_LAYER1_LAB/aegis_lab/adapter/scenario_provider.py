"""Qualified AoE2ScenarioParser fixture provider.

Laboratory tooling only. It never ships inside the .per bot and never invokes
XS facilities. The parser source is an external pinned capability.
"""
from __future__ import annotations

import hashlib
import importlib
import sys
from pathlib import Path

QUALIFIED_TREE_SHA256 = (
    "1F3B47E916C296EFF4A18E809B5B2D392D8382B4FD2680B04784BD1E57ED0652"
)
EXPECTED_SCENARIO_VERSION = "1.58"


def _tree_sha256(root: Path) -> str:
    rows = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()
                       and "__pycache__" not in p.parts and p.suffix != ".pyc"):
        digest = hashlib.sha256(path.read_bytes()).hexdigest().upper()
        rel = path.relative_to(root).as_posix()
        rows.append(f"{digest}  {path.stat().st_size}  {rel}")
    return hashlib.sha256(("\n".join(rows) + "\n").encode()).hexdigest().upper()


def load_qualified_parser(parser_root: str):
    root = Path(parser_root).resolve()
    package = root / "AoE2ScenarioParser"
    if not package.is_dir():
        raise FileNotFoundError(f"AoE2ScenarioParser package not found: {package}")
    observed = _tree_sha256(root)
    if observed != QUALIFIED_TREE_SHA256:
        raise RuntimeError(
            "Unqualified AoE2ScenarioParser source tree: "
            f"expected {QUALIFIED_TREE_SHA256}, observed {observed}"
        )
    package_init = (package / "__init__.py").resolve()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, str(root))
    try:
        module = importlib.import_module("AoE2ScenarioParser")
        if Path(module.__file__).resolve() != package_init:
            raise RuntimeError("Imported parser is not the qualified source tree")
        return module
    finally:
        sys.path.pop(0)


def _parser_classes(parser_root: str):
    load_qualified_parser(parser_root)
    scenario_mod = importlib.import_module(
        "AoE2ScenarioParser.scenarios.aoe2_de_scenario"
    )
    players_mod = importlib.import_module("AoE2ScenarioParser.datasets.players")
    units_mod = importlib.import_module("AoE2ScenarioParser.datasets.units")
    civ_mod = importlib.import_module("AoE2ScenarioParser.datasets.object_support")
    conditions_mod = importlib.import_module("AoE2ScenarioParser.datasets.conditions")
    effects_mod = importlib.import_module("AoE2ScenarioParser.datasets.effects")
    return (scenario_mod.AoE2DEScenario, players_mod.PlayerId,
            units_mod.UnitInfo, civ_mod.Civilization,
            conditions_mod.ConditionId, effects_mod.EffectId)


def build_p0a_calibration_fixture(parser_root: str, template_path: str,
                                  output_path: str) -> dict[str, object]:
    (AoE2DEScenario, PlayerId, UnitInfo, Civilization,
     _ConditionId, _EffectId) = _parser_classes(parser_root)
    source = Path(template_path).resolve()
    output = Path(output_path).resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    scenario = AoE2DEScenario.from_file(str(source))
    if scenario.scenario_version != EXPECTED_SCENARIO_VERSION:
        raise RuntimeError(f"Unsupported fixture version: {scenario.scenario_version}")
    player = scenario.player_manager.players[PlayerId.ONE]
    opponent = scenario.player_manager.players[PlayerId.TWO]
    player.civilization = Civilization.BYZANTINES
    player.human = False
    player.food = player.wood = player.gold = player.stone = 1000
    opponent.civilization = Civilization.BYZANTINES
    opponent.human = True
    scenario.unit_manager.add_unit(
        player=PlayerId.ONE, unit_const=UnitInfo.VILLAGER_MALE.ID,
        x=40, y=40
    )
    trigger = scenario.trigger_manager.add_trigger("P0A_CREATE_ONE_VILLAGER")
    trigger.new_condition.timer(timer=5)
    trigger.new_effect.create_object(
        object_list_unit_id=UnitInfo.VILLAGER_MALE.ID,
        source_player=PlayerId.ONE, location_x=41, location_y=40,
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    scenario.write_to_file(str(output))
    return validate_p0a_fixture(parser_root, str(output))


def validate_p0a_fixture(parser_root: str, scenario_path: str) -> dict[str, object]:
    (AoE2DEScenario, _PlayerId, _UnitInfo, _Civ,
     ConditionId, EffectId) = _parser_classes(parser_root)
    scenario = AoE2DEScenario.from_file(str(Path(scenario_path).resolve()))
    xs_effects = []
    xs_conditions = []
    for trigger in scenario.trigger_manager.triggers:
        xs_effects.extend(e for e in trigger.effects
                          if e.effect_type == EffectId.SCRIPT_CALL)
        xs_conditions.extend(c for c in trigger.conditions
                             if c.condition_type == ConditionId.SCRIPT_CALL)
    if scenario.scenario_version != EXPECTED_SCENARIO_VERSION:
        raise RuntimeError("Fixture scenario version is not 1.58")
    if xs_effects or xs_conditions:
        raise RuntimeError("Fixture contains an XS script-call element")
    names = [trigger.name for trigger in scenario.trigger_manager.triggers]
    if names != ["P0A_CREATE_ONE_VILLAGER"]:
        raise RuntimeError(f"Unexpected fixture triggers: {names}")
    p1_count = len(scenario.unit_manager.units[1])
    if p1_count != 1:
        raise RuntimeError(f"Expected one initial P1 unit, observed {p1_count}")
    return {
        "scenario_version": scenario.scenario_version,
        "map_size": scenario.map_manager.map_size,
        "active_players": scenario.player_manager.active_players,
        "initial_p1_unit_count": p1_count,
        "trigger_count": len(names),
        "xs_script_calls": 0,
        "pure_per_fixture": True,
    }
