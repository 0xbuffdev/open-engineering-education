#!/usr/bin/env python3
"""Reject internal planning-repository links from public OEE documentation.

The checker is intentionally narrow: it detects links to the steward's
non-public planning repositories. It does not enforce a writing style,
check external URLs, or make educational/conformance judgments.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re


PRIVATE_PLAN_LINK = re.compile(
    r"https?://(?:www\.)?github\.com/0xbuffdev/"
    r"(?:context|internal-context)(?=[/#?\s)>]|$)",
    flags=re.IGNORECASE,
)

DOCUMENT_GLOBS = (
    "README.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "spec/*.md",
    "rfcs/*.md",
    "curriculum/*.md",
    "curriculum/*/*.md",
    ".github/ISSUE_TEMPLATE/*.md",
    "scripts/README.md",
    "tooling/*.md",
    "tooling/interop/*.md",
)


def public_documents(root: Path) -> list[Path]:
    """Collect public documents without including generated or test fixtures."""
    return sorted(
        {file for pattern in DOCUMENT_GLOBS for file in root.glob(pattern)
         if file.is_file()}
    )


def check_public_documents(root: Path) -> list[str]:
    """Return path-and-line findings for disallowed internal planning links."""
    problems: list[str] = []
    for file in public_documents(root):
        for number, line in enumerate(
            file.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if PRIVATE_PLAN_LINK.search(line):
                problems.append(
                    f"{file.relative_to(root).as_posix()}:{number}: "
                    "remove link to an internal planning repository"
                )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path,
        default=Path(__file__).resolve().parents[1],
        help="OEE repository root (defaults to the script's parent repository)",
    )
    args = parser.parse_args()
    problems = check_public_documents(args.root.resolve())
    for problem in problems:
        print(problem)
    if problems:
        print(f"FAIL: {len(problems)} internal planning link(s) found")
        return 1
    print("OK: public documentation contains no internal planning links")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
