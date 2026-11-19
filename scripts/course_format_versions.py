"""Classify supported OEE v0.2.0 sources and run structural validation.

An explicit unsupported version fails closed. Unmarked sources with recognizable
current outcome or assessment identifiers are still checked for completeness.
"""

from pathlib import Path
import re
import subprocess
import sys

SPEC_RE = re.compile(
    r"^\*\*(?:Specification|OEE specification):\*\*\s*`?(v\d+\.\d+\.\d+)`?\s*$",
    re.IGNORECASE | re.MULTILINE,
)
ID_HINT_RE = re.compile(
    r"^\s*-\s+\*\*[A-Z]{2,6}[1-9]\d*-(?:O|AS)[1-9]\d*",
    re.MULTILINE,
)
OUTCOME_VERSION = "v0.2.0"


def is_outcome_course(content: str) -> bool:
    """Reject unsupported declared versions; detect the current format."""
    metadata = content.split("\n## ", 1)[0]
    match = SPEC_RE.search(metadata)
    if match:
        version = match.group(1)
        if version != OUTCOME_VERSION:
            raise ValueError(f"unsupported OEE course specification {version}")
        return True
    return bool(ID_HINT_RE.search(content))


def validate_outcome_course(path: Path) -> list[str]:
    """Run the canonical v0.2.0 structural checker for a course file."""
    script = Path(__file__).with_name("check-outcome-curriculum.py")
    result = subprocess.run(
        [sys.executable, str(script), "--course", str(path)],
        capture_output=True, text=True, check=False,
    )
    if result.returncode == 0:
        return []
    failures = [
        line.removeprefix("ERROR: ")
        for line in result.stderr.splitlines() if line.strip()
    ]
    if not failures:
        failures = [result.stdout.strip() or "outcome structural check failed"]
    return failures
