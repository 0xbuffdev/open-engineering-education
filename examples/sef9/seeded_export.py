"""Deliberately flawed ChatGPT-authored SEF9 CSV candidate.

Teaching case only. The proposal is recorded in assistant-proposal.md.
Do NOT run against private or production data, or accept its success result.
"""

from __future__ import annotations

from os import PathLike
from typing import Iterable, Mapping


def export_tasks(
    tasks: Iterable[Mapping[str, object]], destination: str | PathLike[str]
) -> bool:
    """Attempt CSV export. This is deliberately *not* a correct implementation."""
    try:
        with open(destination, "w", encoding="utf-8", newline="") as stream:
            stream.write("id,title\n")
            for task in tasks:
                stream.write(f"{task['id']},{task['title']}\n")
    except OSError:
        return True  # Deliberately wrong: hides failure.
    return True
