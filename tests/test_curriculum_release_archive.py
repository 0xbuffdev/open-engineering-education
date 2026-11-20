"""REL-I02 deterministic USTAR, signed-provenance and offline no-clobber tests.

Uses temporary, synthetic Git source and disposable test-only Ed25519 keys.
Never creates or uploads a real release, key, learner record, or package.
"""
from __future__ import annotations

import copy
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

import test_curriculum_release_manifest as fixtures
from tooling.oee_toolkit.core import canonical_json
from tooling.oee_toolkit.release_archive import (
    MANIFEST_NAME, attestation_claims, build_archive, canonical_archive,
    inspect_archive, install_verified_archive, sha256, sign_candidate,
    verify_attestation,
)
from tooling.oee_toolkit.release_manifest import (
    ReleaseManifestError, digest_manifest,
)

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts/build-curriculum-release-archive.py"
RELEASE_ID = "2026.11.1"


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        fixtures.ReleaseManifestTests.setUp(self)
        self.store = self.repo.parent / "installed-releases"
        self.store.mkdir()
        self.manifest, self.archive = build_archive(self.source(), RELEASE_ID)
        self.digest = digest_manifest(self.manifest)
        self.secret = Ed25519PrivateKey.generate()
        self.private = self.secret.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        self.public = self.secret.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        self.attestation, self.signature = sign_candidate(
            self.archive, self.digest, self.private,
        )

    # Share fixture source operations without importing a second test class.
    commit = fixtures.ReleaseManifestTests.commit
    source = fixtures.ReleaseManifestTests.source

    def installed(self, archive=None, digest=None, attestation=None,
                  signature=None, public=None, store=None):
        return install_verified_archive(
            self.archive if archive is None else archive,
            self.digest if digest is None else digest,
            self.attestation if attestation is None else attestation,
            self.signature if signature is None else signature,
            self.public if public is None else public,
            self.store if store is None else store,
        )

    def assert_rejected(self, archive=None, digest=None, attestation=None,
                        signature=None, public=None):
        with self.assertRaises(ReleaseManifestError):
            verify_attestation(
                self.archive if archive is None else archive,
                self.digest if digest is None else digest,
                self.attestation if attestation is None else attestation,
                self.signature if signature is None else signature,
                self.public if public is None else public,
            )

    def rewrite_tar(self, transform):
        with tarfile.open(fileobj=io.BytesIO(self.archive), mode="r:") as origin:
            collected = [(copy.copy(item), origin.extractfile(item).read())
                         for item in origin.getmembers()]
        collected = transform(collected)
        target = io.BytesIO()
        with tarfile.open(fileobj=target, mode="w:", format=tarfile.USTAR_FORMAT) as archive:
            for info, data in collected:
                archive.addfile(info, io.BytesIO(data) if info.isfile() else None)
        return target.getvalue()

    def test_canonical_archive_manifest_and_source_hashes(self):
        second_manifest, second_archive = build_archive(self.source(), RELEASE_ID)
        self.assertEqual(self.manifest, second_manifest)
        self.assertEqual(self.archive, second_archive)
        decoded, files = inspect_archive(self.archive, self.digest)
        self.assertEqual(decoded, self.manifest)
        self.assertEqual(canonical_archive(decoded, files), self.archive)
        self.assertEqual(files["curriculum/FXT/FXT1.md"],
                         self.source().read_file("curriculum/FXT/FXT1.md").encode())
        self.assertEqual(self.digest, hashlib.sha256(canonical_json(decoded)).hexdigest())
        self.assertEqual(len(files), len(self.manifest["files"]))
        self.assertEqual(decoded["source"]["commit"], self.revision)
        self.assertEqual(decoded["source"]["specification"], "v0.2.0")

    def test_pinned_archive_ignores_dirty_worktree_and_later_head(self):
        first = self.archive
        self.course.write_text(
            self.course.read_text(encoding="utf-8").replace(
                "Diagnose an unfamiliar request failure using observations.",
                "Diagnose another previously unreported failure."),
            encoding="utf-8",
        )
        self.assertEqual(build_archive(self.source(), RELEASE_ID)[1], first)
        changed = self.commit("change current HEAD")
        self.assertEqual(build_archive(self.source(), RELEASE_ID)[1], first)
        newer = build_archive(self.source(changed), "2026.11.2")[1]
        self.assertNotEqual(newer, first)

    def test_test_only_trust_signature_and_offline_no_clobber_install(self):
        self.assertEqual(verify_attestation(
            self.archive, self.digest, self.attestation, self.signature, self.public,
        ), self.manifest)
        expected_claims = attestation_claims(self.archive, self.manifest)
        self.assertEqual(json.loads(self.attestation), expected_claims)
        location = self.installed()
        self.assertEqual(location, self.store / self.digest)
        self.assertEqual((location / "release.json").read_bytes(),
                         canonical_json(self.manifest))
        self.assertEqual(
            (location / "curriculum/FXT/FXT1.md").read_bytes(),
            self.source().read_file("curriculum/FXT/FXT1.md").encode(),
        )
        self.assertFalse((self.store / ".oee-install.lock").exists())
        with self.assertRaisesRegex(ReleaseManifestError, "already installed"):
            self.installed()
        self.assertEqual((location / "release.json").read_bytes(),
                         canonical_json(self.manifest))
        self.assertEqual(list(self.store.iterdir()), [location])

    def test_invalid_signature_wrong_key_changed_attestation_or_digest(self):
        other = Ed25519PrivateKey.generate().public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        flipped = self.signature[:-1] + bytes([self.signature[-1] ^ 1])
        self.assert_rejected(signature=flipped)
        self.assert_rejected(signature=b"")
        self.assert_rejected(public=other)
        self.assert_rejected(digest="0" * 64)
        self.assert_rejected(attestation=self.attestation + b"\n")
        swapped = json.loads(self.attestation)
        swapped["releaseId"] = "2026.11.2"
        self.assert_rejected(attestation=canonical_json(swapped))
        corrupted = self.archive[:-1] + bytes([self.archive[-1] ^ 1])
        self.assert_rejected(archive=corrupted)
        self.assertEqual(list(self.store.iterdir()), [])

    def test_untrusted_tar_entries_cannot_escape_or_hide(self):
        def replace_name(name):
            return self.rewrite_tar(lambda xs: [
                (self.rename(info, name) if info.name == "curriculum/FXT/FXT1.md"
                 else info, data) for info, data in xs
            ])
        for path in (
            "../../escape.md", "/absolute.md", "curriculum/FXT/../FXT1.md",
            "other/secret.md", "curriculum\\FXT\\FXT1.md",
        ):
            with self.subTest(name=path), self.assertRaises(ReleaseManifestError):
                inspect_archive(replace_name(path), self.digest)

    @staticmethod
    def rename(info, name):
        info.name = name
        return info

    def test_symlink_duplicate_extra_entry_and_noncanonical_metadata_rejected(self):
        def duplicate(xs):
            xs.insert(0, (copy.copy(xs[0][0]), xs[0][1]))
            return xs
        def additional(xs):
            info = tarfile.TarInfo("extra/private.md")
            info.size = 1
            info.mode = 0o644
            xs.append((info, b"x"))
            return xs
        def symlink(xs):
            for info, data in xs:
                if info.name == "curriculum/FXT/FXT1.md":
                    info.type = tarfile.SYMTYPE
                    info.linkname = "../../etc/passwd"
                    info.size = 0
                    return xs
            return xs
        def changed_mode(xs):
            xs[0][0].mode = 0o777
            return xs
        def changed_mtime(xs):
            xs[0][0].mtime = 10
            return xs
        def changed_order(xs):
            xs.reverse()
            return xs
        def corrupt_contents(xs):
            for info, data in xs:
                if info.name == "curriculum/FXT/FXT1.md":
                    xs[xs.index((info, data))] = (info, data[:-1] + b"X")
                    break
            return xs
        for mutate in (duplicate, additional, symlink, changed_mode,
                       changed_mtime, changed_order, corrupt_contents):
            with self.subTest(case=mutate.__name__), self.assertRaises(ReleaseManifestError):
                inspect_archive(self.rewrite_tar(mutate), self.digest)
        with self.assertRaises(ReleaseManifestError):
            inspect_archive(self.archive + b"unlisted bytes", self.digest)
        with self.assertRaises(ReleaseManifestError):
            inspect_archive(b"not a tar", self.digest)

    def test_release_id_collision_does_not_replace_existing_snapshot(self):
        first = self.installed()
        old = (first / "curriculum/FXT/FXT1.md").read_bytes()
        self.course.write_text(
            self.course.read_text(encoding="utf-8").replace(
                "Diagnose an unfamiliar request failure using observations.",
                "Diagnose an independently reported failure using observations."),
            encoding="utf-8",
        )
        changed = self.commit("same release ID with different bytes")
        manifest, archive = build_archive(self.source(changed), RELEASE_ID)
        second_sha = digest_manifest(manifest)
        self.assertNotEqual(self.digest, second_sha)
        claim, signature = sign_candidate(archive, second_sha, self.private)
        with self.assertRaisesRegex(ReleaseManifestError, "releaseId is already installed"):
            self.installed(archive=archive, digest=second_sha,
                           attestation=claim, signature=signature)
        self.assertEqual((first / "curriculum/FXT/FXT1.md").read_bytes(), old)
        self.assertFalse((self.store / second_sha).exists())

    def test_symlink_store_and_corrupted_existing_entry_rejected(self):
        alternate = self.store.parent / "redirected-store"
        alternate.mkdir()
        link = self.store.parent / "linked-store"
        try:
            link.symlink_to(self.store, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation is unavailable")
        with self.assertRaises(ReleaseManifestError):
            self.installed(store=link)
        corrupted = self.store / ("f" * 64)
        corrupted.mkdir()
        (corrupted / "release.json").write_text("not JSON", encoding="utf-8")
        with self.assertRaises(ReleaseManifestError):
            self.installed()
        self.assertFalse((self.store / self.digest).exists())

    def test_existing_cache_digest_must_match_its_on_disk_manifest(self):
        forged = self.store / ("f" * 64)
        forged.mkdir()
        (forged / "release.json").write_bytes(canonical_json(self.manifest))
        with self.assertRaisesRegex(ReleaseManifestError, "digest disagrees"):
            self.installed()
        self.assertFalse((self.store / self.digest).exists())

    def test_cli_build_sign_verify_install_without_publication(self):
        working = self.store.parent
        archive = working / "candidate.tar"
        pem = working / "test-only-secret.pem"
        public = working / "trusted-test-only-public.pem"
        pem.write_bytes(self.private)
        public.write_bytes(self.public)
        claim = working / "candidate.attestation.json"
        signature = working / "candidate.sig"
        commands = [
            ["build", "--repo", str(self.repo), "--revision", self.revision,
             "--release-id", RELEASE_ID, "--output", str(archive)],
            ["sign", "--archive", str(archive), "--expected-manifest-sha256",
             self.digest, "--private-key", str(pem),
             "--attestation", str(claim), "--signature", str(signature)],
            ["verify", "--archive", str(archive), "--expected-manifest-sha256",
             self.digest, "--attestation", str(claim),
             "--signature", str(signature), "--trusted-public-key", str(public)],
            ["install", "--archive", str(archive), "--expected-manifest-sha256",
             self.digest, "--attestation", str(claim),
             "--signature", str(signature), "--trusted-public-key", str(public),
             "--store", str(self.store)],
        ]
        for command in commands:
            result = subprocess.run([sys.executable, str(CLI), *command],
                                    cwd=ROOT, capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0,
                             f"failed {' '.join(command[:1])}: {result.stderr}")
        self.assertEqual(archive.read_bytes(), self.archive)
        self.assertTrue((self.store / self.digest / "release.json").is_file())
        # Refuse overwriting existing candidate archive or store installation.
        repeated = subprocess.run([sys.executable, str(CLI), *commands[0]],
                                  cwd=ROOT, capture_output=True, text=True)
        self.assertNotEqual(repeated.returncode, 0)
        self.assertEqual(archive.read_bytes(), self.archive)


if __name__ == "__main__":
    unittest.main()
