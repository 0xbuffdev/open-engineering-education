#!/usr/bin/env python3
"""Verify committed OT-I06 golden exports against one immutable Git revision.

Golden JSON is generated from the public OEE Toolkit parser and pinned OEE
source blobs. It is derived educational material, not an authoring format,
OEE conformance certificate or course-status promotion.

The '--emit' mode prints candidates for an initial human-reviewed commit.
Once golden files exist, normal CI MUST byte-compare them without updating.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tooling.oee_toolkit.core import canonical_json, export_course, ExportBlocked
from tooling.oee_toolkit.source import GitSource, SourceError

FIXTURE_ROOT = Path(__file__).resolve().parent
DEFAULT_MANIFEST = FIXTURE_ROOT / "fixtures" / "pins.json"
DEFAULT_GOLDENS = FIXTURE_ROOT / "golden"
SHA = re.compile(r"[0-9a-f]{40}\Z")
CODE = re.compile(r"[A-Z]{2,6}[1-9][0-9]*\Z")


def manifest(path: Path) -> dict:
    values = json.loads(path.read_text(encoding="utf-8"))
    info = values["source"]
    assert info["repository"] == "0xbuffdev/open-engineering-education"
    assert info["specification"] == "v0.2.0"
    assert values["exportVersion"] == 1
    assert SHA.fullmatch(info["revision"])
    assert len(values["courses"]) == len(set(values["courses"]))
    assert all(CODE.fullmatch(item) for item in values["courses"])
    assert SHA.fullmatch(values["workspaceConsumer"]["revision"])
    return values


def snapshots(repo: Path, manifest_path: Path) -> list[tuple[str, bytes]]:
    """Load selected Git objects, not HEAD/worktree or current network content."""
    pinned = manifest(manifest_path)
    source = GitSource(repo, pinned["source"]["revision"])
    records = []
    for code in pinned["courses"]:
        value = export_course(source, code)
        assert value["source"]["revision"] == source.revision
        assert value["source"]["specification"] == "v0.2.0"
        assert value["source"]["coursePath"].endswith(f"/{code}.md")
        assert value["validation"] == {
            "structural": "passed", "manualReviewRequired": True
        }
        encoded = canonical_json(value)
        assert encoded == canonical_json(export_course(source, code))
        records.append((code, encoded))
    return records


def verify(repo: Path, manifest_path: Path, golden_dir: Path) -> list[tuple[str, str]]:
    records = snapshots(repo, manifest_path)
    expected_files = {f"{code}.json" for code, _ in records}
    actual_files = {item.name for item in golden_dir.glob("*.json")}
    if expected_files != actual_files:
        raise ValueError(
            f"missing/unexpected golden files: expected {sorted(expected_files)}, "
            f"found {sorted(actual_files)}"
        )
    result = []
    for code, fresh in records:
        path = golden_dir / f"{code}.json"
        if path.is_symlink():
            raise ValueError(f"{path.name}: golden symlinks are not trusted")
        committed = path.read_bytes()
        if committed != fresh:
            raise ValueError(
                f"{path.name}: committed export differs from the exact pinned source "
                f"(expected {hashlib.sha256(fresh).hexdigest()}, "
                f"found {hashlib.sha256(committed).hexdigest()}); "
                "do not auto-regenerate during validation"
            )
        parsed = json.loads(committed)
        if canonical_json(parsed) != committed:
            raise ValueError(f"{path.name}: noncanonical JSON bytes")
        result.append((code, hashlib.sha256(committed).hexdigest()))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--golden-dir", type=Path, default=DEFAULT_GOLDENS)
    parser.add_argument("--emit", action="store_true",
                        help="print initial candidate JSON for human review; never writes files")
    args = parser.parse_args()
    try:
        if args.emit:
            for code, encoded in snapshots(args.repo, args.manifest):
                # One JSON-escaped line per golden, suitable for a reviewed commit.
                print("OEE_GOLDEN_" + code + "=" +
                      json.dumps(encoded.decode("utf-8"), ensure_ascii=True))
            return 0
        for code, digest in verify(args.repo, args.manifest, args.golden_dir):
            print(f"{code}: SHA-256 {digest} (pinned and byte-identical)")
        print("Manual review of educational meaning and learner outcomes remains required.")
        return 0
    except (KeyError, OSError, AssertionError, ValueError, SourceError, ExportBlocked) as exc:
        print(f"OT-I06 golden contract failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
