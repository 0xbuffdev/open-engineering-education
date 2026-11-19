"""OT-I06: pinned golden bytes and advisory cross-repository source drift.

These synthetic tests never fetch a remote repository or modify a public
course. No old OEE course or resource-map v1 compatibility is introduced.
"""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from tooling.oee_toolkit.core import export_course, canonical_json
from tooling.oee_toolkit.source import GitSource
from tooling.interop.drift import compare
from tooling.interop.verify_golden import verify, snapshots

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "ot_i02" / "valid_v020_course.md"


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo), *args],
                       capture_output=True, text=True, check=False)
    if p.returncode:
        raise AssertionError(p.stderr)
    return p.stdout.strip()


class PinnedGoldenAndDriftTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.repo = Path(folder.name) / "source"
        self.repo.mkdir()
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.name", "Synthetic test")
        git(self.repo, "config", "user.email", "synthetic@example.invalid")
        self.course = self.repo / "curriculum" / "FXT" / "FXT1.md"
        self.course.parent.mkdir(parents=True)
        self.course.write_text(FIXTURE.read_text(encoding="utf-8"),
                               encoding="utf-8")
        self.original = self.commit("initial source")
        self.base = export_course(GitSource(self.repo, self.original), "FXT1")
        self.pins = Path(folder.name) / "pins.json"
        self.goldens = Path(folder.name) / "golden"
        self.goldens.mkdir()
        self.pins.write_text(json.dumps({
            "source": {"repository": "0xbuffdev/open-engineering-education",
                       "revision": self.original, "specification": "v0.2.0"},
            "exportVersion": 1,
            "courses": ["FXT1"],
            "workspaceConsumer": {
                "repository": "0xbuffdev/oee-workspace",
                "revision": "a" * 40,
            },
        }), encoding="utf-8")
        (self.goldens / "FXT1.json").write_bytes(canonical_json(self.base))

    def commit(self, message):
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-qm", message)
        return git(self.repo, "rev-parse", "HEAD")

    def revised(self, original, modified):
        body = self.course.read_text(encoding="utf-8")
        self.assertIn(original, body)
        self.course.write_text(body.replace(original, modified),
                               encoding="utf-8")
        return self.commit("new source revision")

    def test_golden_is_byte_identical_after_main_changes(self):
        first = verify(self.repo, self.pins, self.goldens)
        new = self.revised(
            "Diagnose an unfamiliar request failure using observations.",
            "Diagnose an unexpected behavior using alternate observations.",
        )
        self.assertNotEqual(new, self.original)
        self.assertEqual(first, verify(self.repo, self.pins, self.goldens))
        self.assertEqual(snapshots(self.repo, self.pins)[0][1],
                         canonical_json(self.base))

    def test_committed_golden_tampering_fails_without_auto_rewrite(self):
        wrong = self.goldens / "FXT1.json"
        wrong.write_text('{"course":"forged"}\n', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs from the exact pinned source"):
            verify(self.repo, self.pins, self.goldens)
        self.assertEqual(wrong.read_text(), '{"course":"forged"}\n')

    def test_unrelated_head_cannot_override_requested_source(self):
        self.revised(
            "diagnose a supplied failure and explain a correction.",
            "diagnose a different supplied failure and explain a correction.",
        )
        # A caller can only select the full SHA passed in; no implicit HEAD.
        self.assertEqual(
            compare(self.repo, self.base, self.original, self.original)["status"],
            "compatible",
        )

    def test_same_outcome_id_with_changed_description_requires_review(self):
        new = self.revised(
            "Diagnose an unfamiliar request failure using observations.",
            "Diagnose unfamiliar behavior with a different evaluation basis.",
        )
        report = compare(self.repo, self.base, self.original, new)
        self.assertEqual(report["status"], "needs_mapping_review")
        self.assertEqual(report["deltas"]["outcomes"]["changed"], ["FXT1-O1"])
        self.assertEqual(report["deltas"]["modules"]["changed"], [])
        self.assertTrue(report["manualReviewRequired"])

    def test_same_assessment_id_changed_criteria_requires_review(self):
        new = self.revised(
            "demonstrate causal evidence and reproducible verification.",
            "demonstrate a different measurement and justify its limits.",
        )
        report = compare(self.repo, self.base, self.original, new)
        self.assertEqual(report["status"], "needs_mapping_review")
        self.assertEqual(report["deltas"]["assessments"]["changed"], ["FXT1-AS1"])

    def test_missing_target_commit_does_not_fallback_to_head(self):
        report = compare(self.repo, self.base, self.original, "f" * 40)
        self.assertEqual(report["status"], "source_missing")
        self.assertEqual(report["targetRevision"], "f" * 40)

    def test_old_course_format_is_not_advisory_compatible(self):
        new = self.revised("`v0.2.0`", "`v0.1.0`")
        report = compare(self.repo, self.base, self.original, new)
        self.assertEqual(report["status"], "unsupported_version")

    def test_unsupported_workspace_map_is_not_reinterpreted(self):
        wrong_map = self.pins.parent / "old-map.json"
        wrong_map.write_text(json.dumps({
            "schemaVersion": 1,
            "curriculum": {"revision": self.original},
            "modules": [{"number": 1, "resources": [{"resource": "R89"}]}],
        }), encoding="utf-8")
        report = compare(self.repo, self.base, self.original,
                         self.original, wrong_map)
        self.assertEqual(report["mapping"]["status"], "unsupported_map_schema")
        self.assertEqual(report["mapping"]["affectedResourceIds"], [])

    def test_reviewed_source_pin_but_changed_outcome_marks_resource_affected(self):
        map_path = self.pins.parent / "map-v2.json"
        map_path.write_text(json.dumps({
            "schemaVersion": 2,
            "status": "reviewed",
            "curriculum": {
                "repository": "0xbuffdev/open-engineering-education",
                "revision": self.original,
                "specification": "v0.2.0",
                "course": "FXT1",
                "path": "curriculum/FXT/FXT1.md",
            },
            "modules": [{"number": 1, "resources": [{
                "resource": "R89", "outcomeIds": ["FXT1-O1"],
            }]}],
        }), encoding="utf-8")
        new = self.revised(
            "Diagnose an unfamiliar request failure using observations.",
            "Diagnose one different observed malfunction.",
        )
        report = compare(self.repo, self.base, self.original, new, map_path)
        self.assertEqual(report["mapping"]["status"], "needs_mapping_review")
        self.assertEqual(report["mapping"]["affectedResourceIds"], ["R89"])

    def test_draft_v2_map_cannot_claim_reviewed_resource_impact(self):
        map_path = self.pins.parent / "unreviewed-v2.json"
        map_path.write_text(json.dumps({
            "schemaVersion": 2,
            "status": "draft",
            "curriculum": {
                "repository": "0xbuffdev/open-engineering-education",
                "revision": self.original,
                "specification": "v0.2.0",
                "course": "FXT1",
                "path": "curriculum/FXT/FXT1.md",
            },
            "modules": [{"number": 1, "resources": [{
                "resource": "R89", "outcomeIds": ["FXT1-O1"],
            }]}],
        }), encoding="utf-8")
        new = self.revised(
            "Diagnose an unfamiliar request failure using observations.",
            "Diagnose a changed malfunction with supporting reasoning.",
        )
        report = compare(self.repo, self.base, self.original, new, map_path)
        self.assertEqual(report["mapping"]["status"], "unreviewed_map")
        self.assertEqual(report["mapping"]["affectedResourceIds"], [])

    def test_wrong_workspace_map_revision_is_source_mismatch(self):
        map_path = self.pins.parent / "map-v2.json"
        map_path.write_text(json.dumps({
            "schemaVersion": 2,
            "curriculum": {
                "repository": "0xbuffdev/open-engineering-education",
                "revision": "a" * 40,
                "specification": "v0.2.0",
                "path": "curriculum/FXT/FXT1.md",
            },
            "modules": [],
        }), encoding="utf-8")
        report = compare(self.repo, self.base, self.original,
                         self.original, map_path)
        self.assertEqual(report["mapping"]["status"], "source_mismatch")


if __name__ == "__main__":
    unittest.main()
