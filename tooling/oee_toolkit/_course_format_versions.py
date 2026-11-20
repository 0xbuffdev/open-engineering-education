"""Single OEE v0.2.0 course format detector used by the canonical parser."""

import re

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
