#!/usr/bin/env python3
"""REL-I01 publisher-only offline candidate manifest builder / verifier.

This is NOT an OEE curriculum release command for learners, and does not
create a release archive, GitHub Release, Git tag, upload or installation.
The publisher selects a full immutable Git SHA; later consumers will not.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tooling.oee_toolkit._publisher_cli import atomic_write  # noqa: E402
from tooling.oee_toolkit.core import canonical_json  # noqa: E402
from tooling.oee_toolkit.release_manifest import (  # noqa: E402
    ReleaseManifestError, build_manifest, digest_manifest, read_canonical_manifest,
    verify_manifest,
)
from tooling.oee_toolkit.source import GitSource, SourceError  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--repo", type=Path, required=True,
                     help="trusted local OEE Git checkout")
    cli.add_argument("--revision", required=True,
                     help="exact publisher-selected 40-character Git commit")
    modes = cli.add_mutually_exclusive_group(required=True)
    modes.add_argument("--output", metavar="FILE|-",
                       help="write an unpublished, deterministic manifest to file or stdout")
    modes.add_argument("--check", type=Path, metavar="MANIFEST",
                       help="verify existing canonical manifest against the full source tree")
    cli.add_argument("--release-id",
                     help="explicit proposed YYYY.MM.N identifier; required for --output")
    args = cli.parse_args(argv)
    if args.output is not None and args.release_id is None:
        cli.error("--output requires --release-id")
    if args.check is not None and args.release_id is not None:
        cli.error("--release-id is taken from the candidate during --check")

    try:
        source = GitSource(args.repo, args.revision)
        if args.check is not None:
            raw = args.check.read_bytes()
            candidate = read_canonical_manifest(raw)
            verify_manifest(source, candidate)
        else:
            candidate = build_manifest(source, args.release_id)
            # All source checks complete before touching a destination.
            atomic_write(args.output, canonical_json(candidate))
        digest = digest_manifest(candidate)
        count = len(candidate["files"])
        if args.output != "-":
            print(f"REL-I01 source-only manifest {'verified' if args.check else 'built'}; "
                  f"{count} files, SHA-256 {digest}; no release published",
                  file=sys.stderr)
        return 0
    except (ReleaseManifestError, SourceError, OSError) as exc:
        print(f"REL-I01 rejected source/manifest: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
