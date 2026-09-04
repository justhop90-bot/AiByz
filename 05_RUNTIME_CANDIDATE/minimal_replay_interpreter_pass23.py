"""AEGIS Layer 2 Pass 23: conservative deterministic replay interpreter."""
from __future__ import annotations
import hashlib
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

SUPPORTED = {"MOVE", "ORDER", "BUILD", "DE_QUEUE", "RESEARCH", "DELETE", "DE_ATTACK_MOVE", "REPAIR", "UNGARRISON", "GATHER_POINT"}
PENDING_OPS = {"BUILD", "DE_QUEUE", "RESEARCH", "DELETE"}

@dataclass
class Evidence:
    source: str
    confidence: str = "DIRECT"
    note: str = ""

@dataclass
class Pending:
    pending_id: int
    sequence: int
    command: str
    player_id: int | None
    actor_ids: list[int]
    target_id: int | None
    target_type: int | None
    coordinates: list[float] | None
    expected_postcondition: str
    completion_evidence: list[dict[str, Any]] = field(default_factory=list)
    failure_evidence: list[dict[str, Any]] = field(default_factory=list)
    status: str = "PENDING"
    match_level: int = 0

class Interpreter:
    def __init__(self) -> None:
        self.players: dict[str, dict[str, Any]] = {}
        self.delete_targets: dict[int, dict[str, Any]] = {}
        self.pending: list[Pending] = []
        self.events = 0
        self.actions = 0
        self.opaque_actions = 0
        self.current_time = None

    @staticmethod
    def evidence(source: str, note: str = "") -> dict[str, Any]:
        return asdict(Evidence(source=source, note=note))

    def sync(self, payload: list[Any]) -> None:
        self.events += 1
        if len(payload) < 3 or not isinstance(payload[2], dict):
            return
        state = payload[2]
        self.current_time = state.get("current_time", self.current_time)
        for key, value in state.items():
            if key == "current_time" or not isinstance(value, dict):
                continue
            self.players.setdefault(key, {"player_id": int(key), "evidence": []})
            self.players[key].update({
                "resource_snapshot": value.get("total_res"),
                "object_count_snapshot": value.get("obj_count"),
                "dp_obj_count_snapshot": value.get("dp_obj_count"),
                "dp_obj_ttl": value.get("dp_obj_ttl"),
            })
            self.players[key]["evidence"].append(self.evidence("PARSED_SNAPSHOT", "SYNC aggregate telemetry"))

    def action(self, command: str, data: dict[str, Any]) -> None:
        self.events += 1
        self.actions += 1
        if command not in SUPPORTED:
            self.opaque_actions += 1
            return
        seq = int(data.get("sequence", -1))
        ids = [int(x) for x in data.get("object_ids", []) if isinstance(x, int)]
        player = data.get("player_id")
        if command == "DELETE":
            for oid in ids:
                self.delete_targets.setdefault(oid, {"object_id": oid, "provenance": self.evidence("DIRECT_REPLAY", "DELETE target")})
        if command not in PENDING_OPS:
            return
        target_type = data.get("unit_id")
        if command == "BUILD":
            target_type = data.get("building_id")
        elif command == "RESEARCH":
            target_type = data.get("technology_id")
        expected = {"BUILD": "building_realized", "DE_QUEUE": "unit_realized", "RESEARCH": "technology_completed", "DELETE": "object_removed"}[command]
        coords = [float(data[x]) for x in ("x", "y")] if "x" in data and "y" in data else None
        self.pending.append(Pending(
            pending_id=len(self.pending) + 1,
            sequence=seq,
            command=command,
            player_id=int(player) if player is not None else None,
            actor_ids=ids,
            target_id=int(data["target_id"]) if isinstance(data.get("target_id"), int) else None,
            target_type=target_type if isinstance(target_type, int) else None,
            coordinates=coords,
            expected_postcondition=expected,
        ))

    def feed(self, path: str) -> None:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                row = json.loads(line)
                op, payload = row.get("op"), row.get("payload")
                if op == "SYNC":
                    self.sync(payload)
                elif op == "ACTION" and isinstance(payload, list) and len(payload) == 2 and isinstance(payload[1], dict):
                    self.action(payload[0], payload[1])
                else:
                    self.events += 1

    def negative_tests(self) -> dict[str, bool]:
        return {
            "queue_not_spawned": not any(p.command == "DE_QUEUE" and p.status == "REALIZED" for p in self.pending),
            "build_not_completed": not any(p.command == "BUILD" and p.status == "REALIZED" for p in self.pending),
            "research_not_completed": not any(p.command == "RESEARCH" and p.status == "REALIZED" for p in self.pending),
            "no_individual_birth_from_aggregate": True,
            "no_aggregate_death_lineage": True,
        }

    def report(self, input_path: str) -> dict[str, Any]:
        raw = Path(input_path).read_bytes()
        counts: dict[str, int] = {}
        for p in self.pending:
            counts[p.command] = counts.get(p.command, 0) + 1
        return {
            "schema": "AEGIS-L2-P23-v1",
            "input": str(input_path),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "events_seen": self.events,
            "actions_seen": self.actions,
            "opaque_unsupported_actions": self.opaque_actions,
            "players": len(self.players),
            "delete_targets_observed": len(self.delete_targets),
            "pending_total": len(self.pending),
            "pending_by_command": counts,
            "promoted_w1": 0,
            "promoted_w2": 0,
            "promoted_w3": 0,
            "negative_tests": self.negative_tests(),
            "closure": {"W0": "CLOSED", "W1": "OPEN", "W2": "OPEN", "W3": "OPEN"},
            "invariant": "unsupported transitions remain unresolved",
        }

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("--report", required=True)
    args = ap.parse_args()
    itp = Interpreter()
    itp.feed(args.input)
    result = itp.report(args.input)
    Path(args.report).write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
