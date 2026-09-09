#!/usr/bin/env python3
"""Deterministic R2/R4 source occurrence joiner.

This tool is deliberately evidence-preserving. It does not infer engine semantics.
It scans the exact four-file stock load closure, joins lexical symbol occurrences
to the existing canonical symbol inventory, and retains raw source lines and
source hashes so later semantic parsers can refine the result without rescanning
or silently changing provenance.

Inputs
------
1. Exact installed stock closure:
   AI (HD version).per
   Promisory/defaultConstants.per
   Promisory/finalingConstants.per
   Promisory/finaling.per
2. Existing _local_stock_audit-2026-09-06/symbol_inventory.jsonl

Outputs
-------
A JSONL occurrence index. The output is intentionally reproducible and should
be regenerated when the source hash changes. Do not treat role_candidate as
engine semantics; mutation_context only means that a mutation primitive occurs
on the same source line.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

TOKEN_RE = re.compile(r"[A-Za-z0-9_?][A-Za-z0-9_?\-]*")
DEFCONST_RE = re.compile(r"\(defconst\s+([^\s\)]+)\s+([^\s\)]+)", re.I)
RULE_RE = re.compile(r"^\s*\(defrule\b", re.I)
OP_RE = re.compile(r"\(([A-Za-z0-9_-]+)\b")
MUTATION_OPS = {
    "set-goal", "up-modify-goal", "set-strategic-number",
    "up-modify-strategic-number", "set-flag", "clear-flag",
    "enable-timer", "disable-timer", "set-goal-now",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_inventory(path: Path):
    # utf-8-sig accepts both the canonical UTF-8 JSONL and Windows-exported
    # copies carrying a BOM, without altering the parsed records.
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    by_symbol = collections.defaultdict(list)
    for row in rows:
        by_symbol[row["symbol"].lower()].append(row)
    return rows, by_symbol


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stock-root", type=Path, required=True)
    ap.add_argument("--inventory", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    root = args.stock_root
    files = [
        root / "AI (HD version).per",
        root / "Promisory" / "defaultConstants.per",
        root / "Promisory" / "finalingConstants.per",
        root / "Promisory" / "finaling.per",
    ]
    inventory_rows, by_symbol = load_inventory(args.inventory)
    symbols = set(by_symbol)

    output_rows = []
    source_manifest = []
    for path in files:
        data = path.read_bytes()
        text = data.decode("utf-8")
        lines = text.splitlines()
        digest = sha256_bytes(data)
        source_manifest.append({
            "path": str(path),
            "bytes": len(data),
            "lines": len(lines),
            "sha256": digest,
        })
        current_rule = None
        current_rule_line = None
        for line_no, raw in enumerate(lines, 1):
            # Keep raw text verbatim. Semicolon/comment interpretation is NOT
            # silently applied here because that is itself a semantic question.
            tokens = TOKEN_RE.findall(raw.lower())
            hits = sorted(set(token for token in tokens if token in symbols))
            if RULE_RE.search(raw):
                current_rule = raw.strip()
                current_rule_line = line_no
            if not hits:
                continue
            ops = [m.group(1).lower() for m in OP_RE.finditer(raw)]
            mutations = [op for op in ops if op in MUTATION_OPS]
            for symbol in hits:
                if DEFCONST_RE.search(raw):
                    role = "DECLARATION_CONTEXT"
                elif mutations:
                    role = "MUTATION_CONTEXT"
                else:
                    role = "REFERENCE"
                output_rows.append({
                    "symbol": symbol,
                    "file": str(path),
                    "line": line_no,
                    "source_sha256": digest,
                    "role_candidate": role,
                    "mutation_ops": mutations,
                    "enclosing_rule_line": current_rule_line,
                    "enclosing_rule": current_rule,
                    "text": raw,
                    "declarations": by_symbol[symbol],
                })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="\n") as fh:
        for row in output_rows:
            fh.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    summary = collections.Counter(row["role_candidate"] for row in output_rows)
    print(json.dumps({
        "inventory_rows": len(inventory_rows),
        "unique_symbols": len(symbols),
        "occurrences": len(output_rows),
        "role_counts": dict(summary),
        "source_manifest": source_manifest,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
