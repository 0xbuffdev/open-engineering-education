#!/usr/bin/env python3
"""REL-I02 explicit candidate archive / detached signature / offline install.

No GitHub release uploads, registry publication, tag creation, implicit
network access or entitlement/learner writes. Git is used ONLY by build.
A release's human name is not proof of identity or authenticity.
"""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tooling.oee_toolkit.release_archive import (  # noqa: E402
    build_archive, digest_manifest, inspect_archive, install_verified_archive,
    sign_candidate, verify_attestation,
)
from tooling.oee_toolkit.release_manifest import ReleaseManifestError  # noqa: E402
from tooling.oee_toolkit.source import GitSource, SourceError  # noqa: E402


def create_only(target: Path, content: bytes) -> None:
    """Stage and atomically link a new file without replacing old bytes."""
    target = target.expanduser().absolute()
    if not target.parent.is_dir() or target.parent.is_symlink():
        raise ReleaseManifestError("output parent must be an existing real directory")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".oee-candidate-", suffix=".tmp",
                                         dir=target.parent, delete=False) as writer:
            temporary = Path(writer.name)
            writer.write(content)
            writer.flush()
            os.fsync(writer.fileno())
        # Exclusive hard-link commit: unlike os.replace/os.rename, it cannot
        # destroy existing user files or published source artifacts.
        os.link(temporary, target)
    except (FileExistsError, OSError) as exc:
        raise ReleaseManifestError("output destination already exists or is not writable") from exc
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest="command", required=True)

    build = modes.add_parser("build", help="publisher-only source candidate TAR")
    build.add_argument("--repo", required=True, type=Path)
    build.add_argument("--revision", required=True, help="publisher's full immutable Git SHA")
    build.add_argument("--release-id", required=True, help="candidate YYYY.MM.N")
    build.add_argument("--output", required=True, type=Path, help="new .tar; no overwrite")

    sign = modes.add_parser("sign", help="explicitly sign candidate with external key")
    sign.add_argument("--archive", required=True, type=Path)
    sign.add_argument("--expected-manifest-sha256", required=True)
    sign.add_argument("--private-key", required=True, type=Path,
                      help="maintainer-controlled PEM Ed25519 key; never in source control")
    sign.add_argument("--attestation", required=True, type=Path, help="new .json sidecar")
    sign.add_argument("--signature", required=True, type=Path, help="new raw 64-byte .sig")

    for mode in ("verify", "install"):
        command = modes.add_parser(mode, help="offline trusted-archive " + mode)
        command.add_argument("--archive", required=True, type=Path)
        command.add_argument("--expected-manifest-sha256", required=True)
        command.add_argument("--attestation", required=True, type=Path)
        command.add_argument("--signature", required=True, type=Path)
        command.add_argument("--trusted-public-key", required=True, type=Path,
                             help="separately approved steward PEM Ed25519 public key")
        if mode == "install":
            command.add_argument("--store", required=True, type=Path,
                                 help="existing trusted cache directory; no-clobber")

    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            source = GitSource(args.repo, args.revision)
            manifest, candidate = build_archive(source, args.release_id)
            create_only(args.output, candidate)
            print("REL-I02 unpublished candidate built; releaseId=" +
                  manifest["releaseId"] + "; manifestSha256=" +
                  digest_manifest(manifest) + "; archiveSha256=" +
                  hashlib.sha256(candidate).hexdigest(), file=sys.stderr)
            return 0

        archive = args.archive.read_bytes()
        if args.command == "sign":
            attestation, signature = sign_candidate(
                archive, args.expected_manifest_sha256,
                args.private_key.read_bytes(),
            )
            if args.attestation.resolve() == args.signature.resolve():
                raise ReleaseManifestError("attestation and signature paths must be distinct")
            # A signature is not release approval, user authentication or a
            # GitHub Release. Both outputs must be newly allocated paths.
            if args.attestation.exists() or args.attestation.is_symlink() or \
                    args.signature.exists() or args.signature.is_symlink():
                raise ReleaseManifestError("refusing to replace existing signing sidecars")
            create_only(args.attestation, attestation)
            create_only(args.signature, signature)
            print("REL-I02 candidate signed locally; not published", file=sys.stderr)
            return 0

        attestation = args.attestation.read_bytes()
        signature = args.signature.read_bytes()
        trusted_key = args.trusted_public_key.read_bytes()
        if args.command == "verify":
            manifest = verify_attestation(archive, args.expected_manifest_sha256,
                                          attestation, signature, trusted_key)
            print("REL-I02 trusted candidate verified; releaseId=" +
                  manifest["releaseId"] + "; no publication", file=sys.stderr)
        else:
            result = install_verified_archive(
                archive, args.expected_manifest_sha256, attestation,
                signature, trusted_key, args.store,
            )
            print("REL-I02 offline immutable candidate installed at " +
                  str(result) + "; no publication or lockfile changes",
                  file=sys.stderr)
        return 0
    except (ReleaseManifestError, SourceError, OSError) as exc:
        print("REL-I02 rejected: " + str(exc), file=sys.stderr)
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
