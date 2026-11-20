#!/usr/bin/env python3
"""Repository maintenance entrypoint for OEE's single packaged parser.

Keep source structural checking, Toolkit export and diagnostic rules on one
implementation: tooling/oee_toolkit/_outcome_parser.py. This wrapper exists
for the repository's CI and maintenance commands, not as a legacy format
reader, compatibility mode, or a second course parser.
"""

from pathlib import Path
import sys

# Direct execution (python scripts/check-outcome-curriculum.py) places only
# scripts/ on sys.path, so expose the source checkout's package explicitly.
_REPO = Path(__file__).resolve().parents[1]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from tooling.oee_toolkit._outcome_parser import *  # noqa: F401,F403,E402

if __name__ == "__main__":
    raise SystemExit(main())
