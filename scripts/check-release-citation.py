#!/usr/bin/env python3
"""Verify OEE release citation metadata against an announced release.

Read the CITATION.cff committed at the exact release tag, never an unrelated
main-branch file. This is a release-consistency check, not a CFF/YAML parser
or a normative specification validator.

Usage:
  python3 scripts/check-release-citation.py --tag v0.3.0 --published-at 2026-12-01
  python3 scripts/check-release-citation.py --tag v0.3.0 --published-at 2026-12-01T11:30:00Z --citation CITATION.cff
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
from pathlib import Path
import re
import sys

RELEASE_TAG = re.compile(r"^v(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z][0-9A-Za-z.-]*))?$")
PLAIN = re.compile(r"^[^\s\"'#][^#]*$")


def cff_scalar(text: str, name: str) -> str:
    """Read one unindented scalar, rejecting duplicates and unsupported syntax."""
    values = re.findall(rf"^{re.escape(name)}:\s*(.*?)\s*$", text, flags=re.MULTILINE)
    if len(values) != 1:
        raise ValueError(f"CITATION.cff must declare one top-level {name} scalar (found {len(values)})")
    value = values[0].strip()
    if not value:
        raise ValueError(f"{name} must not be empty")
    if value.startswith('"'):
        if len(value) < 2 or not value.endswith('"'):
            raise ValueError(f"{name} has an unterminated quoted scalar")
        import json
        try:
            parsed = json.loads(value)
        except ValueError as exc:
            raise ValueError(f"{name} has invalid double-quoted value") from exc
        if not isinstance(parsed, str):
            raise ValueError(f"{name} must be a string scalar")
        return parsed
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise ValueError(f"{name} has an unterminated quoted scalar")
        return value[1:-1].replace("''", "'")
    if not PLAIN.fullmatch(value) or value.rstrip().endswith(":"):
        raise ValueError(f"{name} must be a simple scalar")
    return value


def release_date(value: str) -> date:
    """Compare against the GitHub publication date in UTC, not local time."""
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return date.fromisoformat(value)
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        timestamp = datetime.fromisoformat(value)
        if timestamp.tzinfo is None or timestamp.utcoffset() is None:
            raise ValueError("timestamp needs an explicit UTC offset")
        return timestamp.astimezone(timezone.utc).date()
    except (ValueError, TypeError) as exc:
        raise ValueError(f"invalid release publication date: {value}") from exc


def validate(text: str, tag: str, published_at: str) -> list[str]:
    """Return actionable mismatches. Archived releases are never rewritten."""
    match = RELEASE_TAG.fullmatch(tag)
    if not match:
        return [f"invalid release tag {tag!r}; expected vMAJOR.MINOR.PATCH (optional prerelease)"]
    version = tag[1:]
    errors = []
    for key in ("version", "date-released"):
        try:
            actual = cff_scalar(text, key)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if key == "version":
            if actual != version:
                errors.append(f"CITATION.cff version {actual!r} does not match tag {tag!r} (expected {version!r})")
        else:
            try:
                when = date.fromisoformat(actual)
            except ValueError:
                errors.append(f"CITATION.cff date-released {actual!r} is not a valid ISO date")
                continue
            if actual != when.isoformat():
                errors.append(f"CITATION.cff date-released {actual!r} must use YYYY-MM-DD")
                continue
            try:
                expected = release_date(published_at)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if when != expected:
                errors.append(f"CITATION.cff date-released {actual!r} does not match UTC release publication date {expected}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True, help="published tag (e.g. v0.3.0)")
    parser.add_argument("--published-at", required=True, help="expected release date YYYY-MM-DD or GitHub ISO timestamp")
    parser.add_argument("--citation", type=Path,
                        default=Path(__file__).resolve().parents[1] / "CITATION.cff")
    args = parser.parse_args()
    try:
        source = args.citation.read_text(encoding="utf-8")
    except OSError as exc:
        parser.exit(2, f"citation metadata unavailable: {exc}\n")
    errors = validate(source, args.tag, args.published_at)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Release citation metadata check FAILED ({len(errors)} problem(s)).", file=sys.stderr)
        return 1
    print(f"Release citation metadata consistent with {args.tag} at {release_date(args.published_at)} (UTC).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
