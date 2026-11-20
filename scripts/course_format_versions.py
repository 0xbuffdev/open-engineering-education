"""Repository maintenance callers of the packaged OEE format detector."""

from pathlib import Path
import subprocess
import sys

_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from tooling.oee_toolkit._course_format_versions import is_outcome_course  # noqa: E402


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
