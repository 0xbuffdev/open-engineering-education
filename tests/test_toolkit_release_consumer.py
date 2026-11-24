"""REL-I03 Git-free consumer, current-only export-v2 and adversarial cache tests.

Temporary source repos are Git-backed *only to build a test archive*. Once
installed, consumer operations use solely the verified bytes and a reviewed
release lock. Disposable keys are never official steward release authority.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

import test_curriculum_release_manifest as fixtures
from tooling.oee_toolkit.core import canonical_json
from tooling.oee_toolkit.assessment_context import export_assessment_context
from tooling.oee_toolkit.release_archive import (
    build_archive, install_verified_archive, sign_candidate,
)
from tooling.oee_toolkit.release_manifest import ReleaseManifestError, digest_manifest
from tooling.oee_toolkit.release_source import (
    ReleaseSource, export_release_course, read_lock, resolve_release,
)
from tooling.oee_toolkit.source import GitSource

ROOT = Path(__file__).resolve().parents[1]


class OfflineReleaseConsumerTests(unittest.TestCase):
    commit = fixtures.ReleaseManifestTests.commit
    source = fixtures.ReleaseManifestTests.source

    def setUp(self):
        fixtures.ReleaseManifestTests.setUp(self)
        self.directory = self.repo.parent
        self.store = self.directory / "trusted-cache"
        self.store.mkdir()
        manifest, archive = build_archive(self.source(), "2026.11.1")
        self.manifest = manifest
        self.digest = digest_manifest(manifest)
        key = Ed25519PrivateKey.generate()
        private = key.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
        public = key.public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        claims, signature = sign_candidate(archive, self.digest, private)
        self.installed = install_verified_archive(
            archive, self.digest, claims, signature, public, self.store,
        )
        self.lock = self.directory / "oee-curriculum.lock.json"
        self.lock.write_bytes(canonical_json({
            "formatVersion": 1,
            "releaseId": manifest["releaseId"],
            "manifestSha256": self.digest,
        }))

    def cli(self, *args, default_lock=False):
        env = {**os.environ, "PYTHONPATH": str(ROOT)}
        return subprocess.run(
            [sys.executable, "-m", "tooling.oee_toolkit", *args],
            cwd=self.directory if default_lock else ROOT,
            env=env, capture_output=True, check=False, text=True,
        )

    def explicit(self, action, *args):
        return self.cli(action, *args, "--lock", str(self.lock),
                        "--store", str(self.store))

    def test_installed_release_has_only_export_version_two(self):
        source = resolve_release(self.lock, self.store)
        self.assertIsInstance(source, ReleaseSource)
        with patch.object(ReleaseSource, "_git", side_effect=AssertionError(
                "Git must never execute for a consumer")):
            first = export_release_course(source, "FXT1")
            second = export_release_course(source, "FXT1")
        self.assertEqual(canonical_json(first), canonical_json(second))
        self.assertEqual(first["exportVersion"], 2)
        self.assertNotIn("revision", first["source"])
        self.assertEqual(first["source"]["releaseId"], "2026.11.1")
        self.assertEqual(first["source"]["manifestSha256"], self.digest)
        self.assertEqual(first["source"]["originCommit"], self.revision)
        self.assertEqual(first["source"]["coursePath"], "curriculum/FXT/FXT1.md")
        self.assertEqual(first["source"]["courseSha256"],
                         hashlib.sha256(self.source().read_file(
                             "curriculum/FXT/FXT1.md").encode()).hexdigest())
        self.assertEqual(first["toolkit"]["ruleSetVersion"], "v0.2.0-ot-i04")
        self.assertEqual([x["id"] for x in first["outcomes"]], ["FXT1-O1", "FXT1-O2"])
        self.assertEqual([x["id"] for x in first["assessments"]], ["FXT1-AS1"])
        self.assertEqual(first["coverage"], {
            "FXT1-O1": ["FXT1-AS1"], "FXT1-O2": ["FXT1-AS1"]
        })
        self.assertEqual(first["course"]["status"], "draft")
        self.assertEqual(first["validation"],
                         {"structural": "passed", "manualReviewRequired": True})

    def test_context_is_exact_source_bound_and_does_not_infer_mandatory_practice(self):
        source = resolve_release(self.lock, self.store)
        with patch.object(ReleaseSource, "_git", side_effect=AssertionError("Git forbidden")):
            context = export_assessment_context(source, "FXT1")
            self.assertEqual(context, export_assessment_context(source, "FXT1"))
        self.assertEqual(context["contextVersion"], 1)
        self.assertEqual(context["applicability"], "manual-resolution-required")
        self.assertEqual(context["reviewedRanges"], [])
        self.assertTrue(context["manualReviewRequired"])
        self.assertEqual(context["assessments"], [{
            "assessmentId": "FXT1-AS1",
            "sourcePaths": ["curriculum/FXT/FXT1.md"],
        }])
        document = context["documents"][0]
        self.assertEqual(document["markdown"], source.read_file(document["path"]))
        self.assertEqual(document["sha256"], hashlib.sha256(
            document["markdown"].encode()).hexdigest())
        self.assertEqual(context["courseExportSha256"], hashlib.sha256(
            canonical_json(export_release_course(source, "FXT1"))).hexdigest())
        digest = context.pop("contextSha256")
        self.assertEqual(digest, hashlib.sha256(canonical_json(context)).hexdigest())
        context["documents"][0]["markdown"] += "\\nChanged shared requirement"
        self.assertNotEqual(digest, hashlib.sha256(canonical_json(context)).hexdigest())
        first = self.explicit("assessment-context", "FXT1", "--output", "-")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, self.explicit(
            "assessment-context", "FXT1", "--output", "-").stdout)
        self.assertEqual(json.loads(first.stdout)["contextSha256"], digest)

    def test_released_sef1_context_preserves_exact_shared_and_optional_rules(self):
        # Rebuild the exact released bytes with a disposable test-only
        # signature. The historical published manifest/archive hashes are
        # independently recorded in the steward's release decision.
        revision = "f2afed3e36f6ae0495e2b44a8d9337661defeda1"
        available = subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "-t", revision],
            capture_output=True, check=False,
        )
        if available.returncode:
            if os.environ.get("CI"):
                self.fail("released SEF1 fixture commit unavailable in CI")
            self.skipTest("full OEE Git history required for released-source fixture")
        manifest, archive = build_archive(GitSource(ROOT, revision), "2026.11.1")
        digest = digest_manifest(manifest)
        self.assertEqual(digest,
            "57441494eb69c2ff9cb3f6029c8adc3c6a56f8c6ecabc43196c9b686e5959a6c")
        self.assertEqual(hashlib.sha256(archive).hexdigest(),
            "931b30209a2727717af331f4fd46bfc8e637c94c4d1d95d08d6ffeee753c78d2")
        key = Ed25519PrivateKey.generate()
        private = key.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption())
        public = key.public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        claims, signature = sign_candidate(archive, digest, private)
        store = self.directory / "released-fixture"
        store.mkdir()
        install_verified_archive(archive, digest, claims, signature, public, store)
        lock = self.directory / "released-lock.json"
        lock.write_bytes(canonical_json({
            "formatVersion": 1, "releaseId": "2026.11.1", "manifestSha256": digest,
        }))
        source = resolve_release(lock, store)
        context = export_assessment_context(source, "SEF1")
        self.assertEqual(context["applicability"], "source-indexed")
        self.assertTrue(context["manualReviewRequired"])
        self.assertEqual(context["source"]["originCommit"], revision)
        course = context["documents"][0]
        self.assertEqual(course["sha256"], context["source"]["courseSha256"])
        lines = course["markdown"].splitlines(keepends=True)
        shared = {}
        optional = []
        for item in context["reviewedRanges"]:
            loc = item["location"]
            excerpt = "".join(lines[loc["startLine"]-1:loc["endLine"]])
            self.assertEqual(hashlib.sha256(excerpt.encode()).hexdigest(), item["sha256"])
            if item["kind"] == "shared-rules":
                shared[tuple(item["assessmentIds"])] = excerpt
            elif item["kind"] == "optional-practice":
                self.assertEqual(item["assessmentIds"], [])
                optional.append(excerpt)
        environment = shared[("SEF1-AS1", "SEF1-AS2", "SEF1-AS3")]
        self.assertIn("inspectable simulator circuits", environment)
        self.assertIn("minimum steps another learner needs to", environment)
        self.assertIn("fully gate-implemented CPU is **not required**", environment)
        machine = shared[("SEF1-AS3",)]
        for phrase in ("reset `Z=0`", "**untaken** `JZ`", "without changing `PC`",
                       "LOAD F1", "STORE F0", "latch starts **unset**"):
            self.assertIn(phrase, machine)
        self.assertEqual(len(optional), 1)
        self.assertIn("not additional summative submissions", optional[0])
        self.assertEqual({a["assessmentId"] for a in context["assessments"]},
                         {"SEF1-AS1", "SEF1-AS2", "SEF1-AS3"})

        # Model a newly verified source revision at the parser boundary.
        # No claim of signing or installing this modified in-memory fixture.
        changed = copy.deepcopy(source)
        path = course["path"]
        modified = course["markdown"].replace(
            "Record the actual tool and version", "Record the exact tool and version")
        self.assertNotEqual(modified, course["markdown"])
        changed._files[path] = modified.encode()
        changed._hashes[path] = hashlib.sha256(modified.encode()).hexdigest()
        changed.manifest_sha256 = "f" * 64
        next_context = export_assessment_context(changed, "SEF1")
        self.assertEqual(next_context["applicability"], "manual-resolution-required")
        self.assertEqual(next_context["reviewedRanges"], [])
        self.assertNotEqual(next_context["contextSha256"], context["contextSha256"])
        self.assertIn("Record the exact tool and version",
                      next_context["documents"][0]["markdown"])

    def test_context_rejects_wrong_lock_without_replacing_existing_output(self):
        output = self.directory / "context.json"
        output.write_bytes(b"previous review")
        self.lock.write_bytes(canonical_json({
            "formatVersion": 1, "releaseId": "2026.11.1", "manifestSha256": "a" * 64,
        }))
        result = self.explicit("assessment-context", "FXT1", "--output", str(output))
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output.read_bytes(), b"previous review")

    def test_pure_offline_cli_without_git_checkout_or_default_network(self):
        # Change and remove publisher-side source: installed bytes remain fixed.
        source_dir = self.repo
        self.course.unlink()
        first = self.explicit("export", "FXT1", "--output", "-")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(json.loads(first.stdout)["exportVersion"], 2)
        again = self.explicit("export", "FXT1", "--output", "-")
        self.assertEqual(first.stdout, again.stdout)
        self.assertNotIn(str(source_dir), first.stdout)
        all_courses = self.explicit("check", "--all", "--json")
        self.assertEqual(all_courses.returncode, 0, all_courses.stderr)
        self.assertEqual(json.loads(all_courses.stdout)["structuralOutcome"], "passed")
        self.assertEqual(json.loads(all_courses.stdout)["source"]["manifestSha256"],
                         self.digest)

    def test_release_lock_is_required_with_no_parent_or_git_fallback(self):
        missing = self.cli("export", "FXT1", "--store", str(self.store),
                           "--output", "-")
        self.assertEqual(missing.returncode, 3)
        self.assertEqual(missing.stdout, "")
        self.assertIn("release lock", missing.stderr)
        rejected = self.cli("export", "FXT1", "--repo", str(self.repo),
                            "--revision", self.revision, "--output", "-")
        self.assertEqual(rejected.returncode, 2)
        self.assertEqual(rejected.stdout, "")
        default = self.cli("export", "FXT1", "--store", str(self.store),
                           "--output", "-", default_lock=True)
        self.assertEqual(default.returncode, 0, default.stderr)
        self.assertEqual(json.loads(default.stdout)["source"]["manifestSha256"],
                         self.digest)

    def test_manifest_digest_and_release_label_must_match_lock(self):
        original = self.lock.read_bytes()
        for change in (
            {"releaseId": "2026.11.2"},
            {"manifestSha256": "a" * 64},
            {"manifestSha256": "main"},
            {"formatVersion": 2},
            {"formatVersion": True},
            {"additional": "unsupported"},
        ):
            self.lock.write_bytes(canonical_json({**json.loads(original), **change}))
            with self.subTest(change=change), self.assertRaises(ReleaseManifestError):
                resolve_release(self.lock, self.store)
        self.lock.write_bytes(b'{"formatVersion":1,"formatVersion":1,"releaseId":"2026.11.1","manifestSha256":"' +
                              self.digest.encode() + b'"}\n')
        with self.assertRaises(ReleaseManifestError):
            read_lock(self.lock)

    def test_tampered_course_unlisted_file_and_symlink_in_store_rejected(self):
        course = self.installed / "curriculum/FXT/FXT1.md"
        original = course.read_bytes()
        course.chmod(0o644)  # installer creates read-only POSIX files
        course.write_bytes(original + b"\nUnreviewed academic requirement")
        with self.assertRaises(ReleaseManifestError):
            resolve_release(self.lock, self.store)
        course.write_bytes(original)
        extra = self.installed / "curriculum/FXT/hidden.md"
        extra.write_text("shadow course", encoding="utf-8")
        with self.assertRaises(ReleaseManifestError):
            resolve_release(self.lock, self.store)
        extra.unlink()
        outside = self.directory / "outside.md"
        outside.write_text("arbitrary file", encoding="utf-8")
        link = self.installed / "curriculum/FXT/shortcut.md"
        try:
            link.symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("filesystem has no symlinks")
        with self.assertRaises(ReleaseManifestError):
            resolve_release(self.lock, self.store)

    def test_untrusted_store_path_or_malformed_manifest_does_not_modify_lock(self):
        original = self.lock.read_bytes()
        with self.assertRaises(ReleaseManifestError):
            resolve_release(self.lock, self.directory / "no-cache")
        damaged = self.installed / "release.json"
        damaged.chmod(0o644)  # simulate an actor with trusted-store write access
        damaged.write_bytes(damaged.read_bytes() + b"x")
        with self.assertRaises(ReleaseManifestError):
            resolve_release(self.lock, self.store)
        self.assertEqual(self.lock.read_bytes(), original)

    def test_failure_does_not_overwrite_existing_export(self):
        output = self.directory / "existing.json"
        output.write_text("preserve learner data", encoding="utf-8")
        failed = self.explicit("export", "FXT99", "--output", str(output))
        self.assertNotEqual(failed.returncode, 0)
        self.assertEqual(output.read_text(encoding="utf-8"), "preserve learner data")

    def test_linked_public_brief_uses_same_verified_release_parser(self):
        fixture_dir = ROOT / "tests/fixtures/ot_i02"
        self.course.write_bytes((fixture_dir / "linked_brief_v020.md").read_bytes())
        brief = self.course.parent / "linked_brief.md"
        brief.write_bytes((fixture_dir / "linked_brief.md").read_bytes())
        latest = self.commit("new linked public brief included in immutable source")
        manifest, archive = build_archive(self.source(latest), "2026.11.2")
        digest = digest_manifest(manifest)
        key = Ed25519PrivateKey.generate()
        private = key.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption())
        public = key.public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        claims, signature = sign_candidate(archive, digest, private)
        linked_store = self.directory / "linked-trusted-cache"
        linked_store.mkdir()
        install_verified_archive(archive, digest, claims, signature, public, linked_store)
        linked_lock = self.directory / "linked-curriculum.lock.json"
        linked_lock.write_bytes(canonical_json({
            "formatVersion": 1, "releaseId": "2026.11.2",
            "manifestSha256": digest,
        }))
        source = resolve_release(linked_lock, linked_store)
        body = export_release_course(source, "FXT1")
        self.assertEqual(body["exportVersion"], 2)
        self.assertEqual(body["assessments"][0]["location"]["path"],
                         "curriculum/FXT/linked_brief.md")
        self.assertIn("traceable cause", body["assessments"][0]["criteria"])
        self.assertEqual(body["source"]["originCommit"], latest)
        self.assertEqual(body["source"]["manifestSha256"], digest)
        context = export_assessment_context(source, "FXT1")
        self.assertEqual(context["assessments"][0]["sourcePaths"], [
            "curriculum/FXT/FXT1.md", "curriculum/FXT/linked_brief.md",
        ])
        self.assertEqual(context["documents"][1]["markdown"], source.read_file(
            "curriculum/FXT/linked_brief.md"))

    def test_nested_project_never_inherits_parent_lock(self):
        nested = self.directory / "unreviewed-subproject"
        nested.mkdir()
        runner = subprocess.run(
            [sys.executable, "-m", "tooling.oee_toolkit", "export", "FXT1",
             "--store", str(self.store), "--output", "-"],
            cwd=nested,
            env={**os.environ, "PYTHONPATH": str(ROOT)},
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(runner.returncode, 3)
        self.assertIn("release lock", runner.stderr)
        self.assertEqual(runner.stdout, "")

    def test_public_schema_documents_current_only_export(self):
        file = ROOT / "tooling/oee_toolkit/schemas/course-export-v2.schema.json"
        schema = json.loads(file.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["exportVersion"]["const"], 2)
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(schema["properties"]["source"]["properties"]
                         ["manifestSha256"]["pattern"], "^[0-9a-f]{64}$")
        self.assertEqual(schema["properties"]["source"]["properties"]
                         ["specification"]["const"], "v0.2.0")
        self.assertIn("toolkit", schema["required"])


if __name__ == "__main__":
    unittest.main()
