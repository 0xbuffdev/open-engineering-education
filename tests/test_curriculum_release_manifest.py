"""REL-I01 publisher-only regression suite using synthetic Git repositories.

Neither GitHub release publication nor learner records are touched.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/ot_i02"
SCRIPT = ROOT / "scripts/build-curriculum-release-manifest.py"

from tooling.oee_toolkit.core import canonical_json
from tooling.oee_toolkit.release_manifest import (
    ReleaseManifestError, build_manifest, digest_manifest, manifest_shape,
    read_canonical_manifest, verify_manifest,
)
from tooling.oee_toolkit.source import GitSource

RELEASE = "2026.11.1"


def git(root, *args):
    run = subprocess.run(["git", "-C", str(root), *args],
                         capture_output=True, text=True, check=False)
    if run.returncode:
        raise AssertionError("git failed: " + run.stderr)
    return run.stdout.strip()


class ReleaseManifestTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name) / "source"
        self.repo.mkdir()
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.name", "OEE synthetic test")
        git(self.repo, "config", "user.email", "fixture@example.invalid")
        self.course = self.repo / "curriculum/FXT/FXT1.md"
        self.catalog = self.repo / "curriculum/FXT/README.md"
        self.course.parent.mkdir(parents=True)
        self.course.write_bytes((FIXTURES / "valid_v020_course.md").read_bytes())
        self.catalog.write_text(
            "# FXT Program\n\n## Courses\n\n"
            "| Course | Title |\n| --- | --- |\n"
            "| [FXT1](FXT1.md) | Synthetic Outcome Course |\n",
            encoding="utf-8",
        )
        self.root_catalog = self.repo / "curriculum/README.md"
        self.root_catalog.write_text(
            "# Curriculum\n\n[Explore FXT](FXT/README.md)\n\n"
            "[Specification](../spec/README.md)\n", encoding="utf-8",
        )
        (self.repo / "spec").mkdir()
        (self.repo / "spec/README.md").write_text("# OEE specification\n", encoding="utf-8")
        (self.repo / "LICENSE").write_text("CC BY 4.0 license\n", encoding="utf-8")
        (self.repo / "NOTICE").write_text("OEE attribution\n", encoding="utf-8")
        (self.repo / "CITATION.cff").write_text("cff-version: 1.2.0\n", encoding="utf-8")
        self.revision = self.commit("valid source fixture")

    def commit(self, message):
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-qm", message)
        return git(self.repo, "rev-parse", "HEAD")

    def source(self, revision=None):
        return GitSource(self.repo, revision or self.revision)

    def manifest(self):
        return build_manifest(self.source(), RELEASE)

    def test_complete_deterministic_source_inventory(self):
        first, second = self.manifest(), self.manifest()
        self.assertEqual(canonical_json(first), canonical_json(second))
        self.assertEqual(first["source"]["commit"], self.revision)
        self.assertEqual(first["source"]["specification"], "v0.2.0")
        self.assertEqual(first["releaseId"], RELEASE)
        self.assertEqual(first["formatVersion"], 1)
        names = [e["path"] for e in first["files"]]
        self.assertEqual(len(names), 7)
        self.assertEqual(names, sorted(set(names)))
        self.assertTrue(set(names) >= {
            "curriculum/FXT/FXT1.md", "curriculum/FXT/README.md",
            "curriculum/README.md", "spec/README.md", "LICENSE", "NOTICE",
            "CITATION.cff",
        })
        course = next(e for e in first["files"] if e["path"] == "curriculum/FXT/FXT1.md")
        self.assertEqual(course["sha256"], hashlib.sha256(
            self.source().read_file("curriculum/FXT/FXT1.md").encode("utf-8")
        ).hexdigest())
        self.assertEqual(digest_manifest(first), hashlib.sha256(canonical_json(first)).hexdigest())
        self.assertEqual(verify_manifest(self.source(), first), first)

    def test_pinned_commit_unchanged_across_dirty_worktree_and_moving_head(self):
        original = canonical_json(self.manifest())
        self.course.write_text(self.course.read_text(encoding="utf-8").replace(
            "Diagnose an unfamiliar request failure using observations.",
            "Diagnose a newly changed failure using observations."), encoding="utf-8")
        self.assertEqual(canonical_json(self.manifest()), original)
        changed = self.commit("move HEAD")
        self.assertEqual(canonical_json(self.manifest()), original)
        other = build_manifest(self.source(changed), "2026.11.2")
        self.assertNotEqual(canonical_json(other), original)

    def test_cli_stdout_and_verification_do_not_publish(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--repo", str(self.repo),
             "--revision", self.revision, "--release-id", RELEASE, "--output", "-"],
            cwd=ROOT, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertEqual(result.stdout, canonical_json(self.manifest()))
        path = Path(self.repo.parent) / "candidate.json"
        path.write_bytes(result.stdout)
        verification = subprocess.run(
            [sys.executable, str(SCRIPT), "--repo", str(self.repo),
             "--revision", self.revision, "--check", str(path)],
            cwd=ROOT, capture_output=True, check=False,
        )
        self.assertEqual(verification.returncode, 0, verification.stderr.decode())
        self.assertIn(b"no release published", verification.stderr)

    def test_unknown_fields_versions_ids_and_file_types_rejected(self):
        good = self.manifest()
        invalid = [
            {"formatVersion": 2}, {"formatVersion": True},
            {"releaseId": "main"}, {"releaseId": "2026.00.1"},
            {"releaseId": "2026.13.1"}, {"releaseId": "2026.11.0"},
            {"releaseId": "v0.2.0"}, {"source": {**good["source"], "commit": "main"}},
            {"source": {**good["source"], "repository": "other/oee"}},
            {"source": {**good["source"], "specification": "v0.1.0"}},
            {"extra": True},
        ]
        for change in invalid:
            with self.subTest(change=change), self.assertRaises(ReleaseManifestError):
                manifest_shape({**good, **change})
        for key, value in (
            ("sha256", "a" * 40), ("sha256", "a" * 65),
            ("size", -1), ("size", True), ("size", 1_000_001),
            ("path", "../curriculum/FXT/FXT1.md"),
            ("path", "curriculum/FXT/../FXT1.md"),
            ("path", "/tmp/FXT1.md"),
            ("path", "curriculum/FXT/FXT1.bin"),
            ("path", "curriculum/FXT\\evil.md"),
        ):
            broken = copy.deepcopy(good)
            broken["files"][0][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ReleaseManifestError):
                manifest_shape(broken)

    def test_missing_duplicate_reordered_or_modified_file_rejected(self):
        good = self.manifest()
        missing = copy.deepcopy(good)
        missing["files"] = [e for e in missing["files"]
                            if e["path"] != "curriculum/FXT/FXT1.md"]
        duplicate = copy.deepcopy(good)
        duplicate["files"].insert(0, copy.deepcopy(duplicate["files"][0]))
        reverse = copy.deepcopy(good)
        reverse["files"].reverse()
        changed_sha = copy.deepcopy(good)
        changed_sha["files"][0]["sha256"] = "a" * 64
        changed_size = copy.deepcopy(good)
        changed_size["files"][0]["size"] += 1
        wrong_revision = copy.deepcopy(good)
        wrong_revision["source"]["commit"] = "f" * 40
        for broken in (missing, duplicate, reverse, changed_sha, changed_size, wrong_revision):
            with self.subTest(broken=broken), self.assertRaises(ReleaseManifestError):
                verify_manifest(self.source(), broken)

    def test_canonical_utf8_only_no_extra_whitespace_bom_or_bad_json(self):
        good = self.manifest()
        raw = canonical_json(good)
        self.assertEqual(read_canonical_manifest(raw), good)
        for text in (raw.rstrip(b"\n"), json.dumps(good, indent=2).encode(),
                     b"\xef\xbb\xbf" + raw, raw + b"\n", b"{bad", b"\xff\xfe"):
            with self.subTest(source=text[:12]), self.assertRaises(ReleaseManifestError):
                read_canonical_manifest(text)

    def test_missing_or_duplicated_program_course_catalog_fails(self):
        original = self.catalog.read_text(encoding="utf-8")
        variants = (
            original.replace("(FXT1.md)", "(FXT2.md)"),
            original.replace("[FXT1](FXT1.md)", "[FXT2](FXT2.md)"),
            original + "| [FXT1](FXT1.md) | Duplicate |\n",
            original.replace("| [FXT1](FXT1.md) | Synthetic Outcome Course |\n", ""),
        )
        for i, variant in enumerate(variants):
            self.catalog.write_text(variant, encoding="utf-8")
            revision = self.commit(f"catalog mismatch {i}")
            with self.subTest(i=i), self.assertRaises(ReleaseManifestError):
                build_manifest(self.source(revision), RELEASE)

    def test_root_catalog_references_program(self):
        self.root_catalog.write_text("# Curriculum with no FXT catalog\n", encoding="utf-8")
        revision = self.commit("omit program reference")
        with self.assertRaises(ReleaseManifestError):
            build_manifest(self.source(revision), RELEASE)

    def test_unsupported_course_or_missing_criteria_cannot_ship(self):
        source = self.course.read_text(encoding="utf-8")
        for i, altered in enumerate((
            source.replace("`v0.2.0`", "`v0.1.0`"),
            source.replace(
                "  - Criteria: demonstrate causal evidence and reproducible verification.\n",
                ""),
        )):
            self.course.write_text(altered, encoding="utf-8")
            revision = self.commit(f"invalid course {i}")
            with self.subTest(i=i), self.assertRaises(ReleaseManifestError):
                build_manifest(self.source(revision), RELEASE)

    def test_linked_public_assessment_brief_must_be_present(self):
        self.course.write_bytes((FIXTURES / "linked_brief_v020.md").read_bytes())
        brief = self.repo / "curriculum/FXT/linked_brief.md"
        brief.write_bytes((FIXTURES / "linked_brief.md").read_bytes())
        included = self.commit("linked public brief included")
        manifest = build_manifest(self.source(included), RELEASE)
        self.assertIn("curriculum/FXT/linked_brief.md",
                      {e["path"] for e in manifest["files"]})
        brief.unlink()
        missing = self.commit("remove linked brief")
        with self.assertRaises(ReleaseManifestError):
            build_manifest(self.source(missing), "2026.11.2")

    def test_non_markdown_extra_source_is_not_silently_omitted(self):
        (self.repo / "curriculum/FXT/hidden.bin").write_bytes(b"shadow content")
        revision = self.commit("unlisted academic content")
        with self.assertRaises(ReleaseManifestError):
            build_manifest(self.source(revision), RELEASE)

    def test_symlinks_under_public_source_rejected(self):
        link = self.repo / "spec/escape.md"
        try:
            link.symlink_to(self.course)
        except (OSError, NotImplementedError):
            self.skipTest("test platform cannot create symlinks")
        revision = self.commit("symlink under academic source")
        with self.assertRaises(ReleaseManifestError):
            build_manifest(self.source(revision), RELEASE)

    def test_oversized_source_is_rejected(self):
        (self.repo / "spec/huge.md").write_bytes(b"X" * 1_000_001)
        revision = self.commit("source size exceeded")
        with self.assertRaises(ReleaseManifestError):
            build_manifest(self.source(revision), RELEASE)

    def test_invalid_source_does_not_overwrite_manifest_output(self):
        dest = self.repo.parent / "candidate.json"
        dest.write_text("preserve existing bytes\n", encoding="utf-8")
        self.course.write_text("invalid OEE source\n", encoding="utf-8")
        revision = self.commit("invalid OEE content")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--repo", str(self.repo),
             "--revision", revision, "--release-id", RELEASE,
             "--output", str(dest)], cwd=ROOT, capture_output=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(dest.read_text(encoding="utf-8"), "preserve existing bytes\n")

    def test_public_schema_has_same_identity_and_strict_properties(self):
        schema = json.loads(
            (ROOT / "tooling/oee_toolkit/schemas/curriculum-release-manifest-v1.schema.json")
            .read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["formatVersion"]["const"], 1)
        self.assertEqual(schema["properties"]["source"]["properties"]
                         ["specification"]["const"], "v0.2.0")
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(set(schema["required"]),
                         {"formatVersion", "releaseId", "source", "files"})


if __name__ == "__main__":
    unittest.main()
