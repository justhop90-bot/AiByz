#!/usr/bin/env python3
"""Build a disposable target-build goal ABI smoke-test package.

The installed AI tree is read-only. The generated package is never copied back
into the retail tree. Runtime verdicts require a separately controlled match.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

CLOSURE = [
    "AI (HD version).per",
    "Promisory/defaultConstants.per",
    "Promisory/finaling.per",
    "Promisory/finalingConstants.per",
]

TEST_LOAD = '(load "AEGIS_P0_GOAL_SMOKE")'
TEST_SOURCE = '''; AEGIS P0 goal ABI smoke test — disposable only.
(defconst aegis-p0-goal 10000)
(defconst aegis-p0-result 10001)

(defrule
    (true)
=>
    (set-goal aegis-p0-goal 12345)
    (up-modify-goal aegis-p0-result c:= 0)
    (disable-self))

(defrule
    (goal aegis-p0-result = 0)
=>
    (up-chat-data-to-self "AEGIS_P0_WRITE_READ %d" g: aegis-p0-goal)
    (set-goal aegis-p0-result 1))

(defrule
    (goal aegis-p0-result = 1)
    (up-compare-goal aegis-p0-goal = 12345)
=>
    (up-chat-data-to-self "AEGIS_P0_COMPARE PASS %d" g: aegis-p0-goal)
    (set-goal aegis-p0-result 2))
'''


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ai-root", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    root = args.ai_root.resolve()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    copied = []
    for rel in CLOSURE:
        src = root / rel
        if not src.is_file():
            raise FileNotFoundError(src)
        dst = out / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append({"path": rel, "sha256": sha256(src)})

    entry = out / CLOSURE[0]
    text = entry.read_text(encoding="utf-8")
    if TEST_LOAD in text:
        raise RuntimeError("test load already present")
    entry.write_text(text + "\n" + TEST_LOAD + "\n", encoding="utf-8")
    test = out / "AEGIS_P0_GOAL_SMOKE.per"
    test.write_text(TEST_SOURCE, encoding="utf-8")

    manifest = {
        "schema": "AEGIS-P0-GOAL-SMOKE-v1",
        "source_ai_root": str(root),
        "entrypoint": CLOSURE[0],
        "test_file": "AEGIS_P0_GOAL_SMOKE.per",
        "candidate_goals": {"aegis-p0-goal": 10000, "aegis-p0-result": 10001},
        "source_closure": copied,
        "retail_tree_modified": False,
        "runtime_verdict": "UNKNOWN",
    }
    (out / "EXPERIMENT_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8"
    )
    print(json.dumps(manifest, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
