"""Static AEGIS goal-operand audit.

This is an AEGIS semantic lint, not an AoE2 parser or engine validator.
It catches the specific class of bug where a goal operator receives a
numeric literal through a g: operand even though the author intended a
constant value.

Examples:
    BAD:  (up-modify-goal flag g:= 1)
    GOOD: (set-goal flag 1)
    BAD:  (up-modify-goal cycle g:+ 1)
    GOOD: (up-modify-goal cycle c:+ 1)

Goal references intentionally remain legal:
    (up-modify-goal dst g:= source-goal)
    (up-modify-goal dst g:+ source-goal)

Usage:
    python tools/aegis_goal_operand_audit.py path/to/file.per [more.per ...]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PATTERN = re.compile(
    r"\(up-modify-goal\s+[^\s()]+\s+g:(?:=|\+|-|\*|/)\s+(-?\d+)\b"
)


def audit(path: Path) -> list[str]:
    findings: list[str] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if PATTERN.search(line):
            findings.append(f"{path}:{number}: numeric literal used as g: operand: {line.strip()}")
    return findings


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: python tools/aegis_goal_operand_audit.py FILE.per [...]")
        return 2

    findings: list[str] = []
    for raw in argv:
        path = Path(raw)
        if not path.is_file():
            print(f"NOT_FOUND: {path}")
            return 2
        findings.extend(audit(path))

    if findings:
        print("FAIL")
        print("\n".join(findings))
        return 1

    print(f"PASS: audited {len(argv)} file(s); no numeric g: operands found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
