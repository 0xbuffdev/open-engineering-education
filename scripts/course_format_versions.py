"""Shared OEE curriculum revision classification and validation dispatch.

This is a validator integration utility, not a normative serialization schema.
A v0.2.0 marker opts a course into the outcome validator; a course that
starts adopting stable outcome/assessment IDs is also treated as migrating.
Unknown explicitly declared versions fail closed instead of being ignored.
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
LEGACY_VERSIONS = frozenset(("v0.0.1", "v0.1.0"))
OUTCOME_VERSION = "v0.2.0"


def is_outcome_course(content: str) -> bool:
    """Classify a course without silently downgrading partially migrated work.

    Only a metadata declaration near the beginning of a course counts
    as a specification version. Incidental citations inside lesson
    material should not select a parser.
    """
    metadata = content.split("\n## ", 1)[0]
    match = SPEC_RE.search(metadata)
    has_ids = bool(ID_HINT_RE.search(content))
    if match:
        version = match.group(1)
        if version == OUTCOME_VERSION:
            return True
        if version in LEGACY_VERSIONS:
            if has_ids:
                raise ValueError(
                    f"explicit legacy specification {version} conflicts with "
                    "v0.2.0-style outcome/assessment identifiers"
                )
            return False
        raise ValueError(f"unsupported OEE course specification {version}")
    return has_ids


def validate_outcome_course(path: Path) -> list[str]:
    """Run the canonical structural checker for a v0.2.0 course file.

    The legacy program scripts call this so a newly migrated course
    cannot bypass validation just because its older lab checks are skipped.
    """
    script = Path(__file__).with_name("check-outcome-curriculum.py")
    result = subprocess.run(
        [sys.executable, str(script), "--course", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode == 0:
        return []
    failures = [
        line.removeprefix("ERROR: ")
        for line in result.stderr.splitlines()
        if line.strip()
    ]
    if not failures:
        failures = [result.stdout.strip() or "outcome structural check failed"]
    return failures
