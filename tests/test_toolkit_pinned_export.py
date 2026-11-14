"""Source provenance, safety, strict input and deterministic export tests.

Synthetic repositories are created locally. No network or course rewriting is
required; this is not a conformance or learner-achievement test.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "ot_i02"
from tooling.oee_toolkit.core import export_course, inspect, canonical_json, ExportBlocked
from tooling.oee_toolkit.source import GitSource, SourceError


def git(root, *args):
    result = subprocess.run(["git", "-C", str(root), *args],
                            capture_output=True, text=True, check=False)
    if result.returncode:
        raise AssertionError(f"git {' '.join(args)}: {result.stderr}")
    return result.stdout.strip()


class PinnedToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "synthetic-oee"
        self.repo.mkdir()
        git(self.repo, "init", "-q")
        git(self.repo, "config", "user.name", "OEE synthetic test")
        git(self.repo, "config", "user.email", "synthetic@example.invalid")
        self.course = self.repo / "curriculum" / "FXT" / "FXT1.md"
        self.course.parent.mkdir(parents=True)
        self.course.write_text(
            (FIXTURES / "valid_v020_course.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        self.revision = self.commit("valid synthetic outcome fixture")

    def commit(self, message="fixture"):
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", message)
        revision = git(self.repo, "rev-parse", "HEAD")
        self.assertEqual(len(revision), 40)
        return revision

    def snapshot(self, revision=None):
        return GitSource(self.repo, revision or self.revision)

    def cli(self, command, *options):
        return subprocess.run(
            [sys.executable, "-m", "tooling.oee_toolkit", command,
             "--repo", str(self.repo), "--revision", self.revision, *options],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )

    def test_valid_course_export_shape_and_structural_disclosure(self):
        result = export_course(self.snapshot(), "FXT1")
        self.assertEqual(result["exportVersion"], 1)
        self.assertEqual(result["source"]["revision"], self.revision)
        self.assertEqual(result["source"]["specification"], "v0.2.0")
        self.assertEqual(result["course"]["code"], "FXT1")
        self.assertEqual(result["course"]["prerequisites"], [])
        self.assertEqual(result["validation"],
                         {"structural": "passed", "manualReviewRequired": True})
        self.assertEqual({o["id"] for o in result["outcomes"]},
                         {"FXT1-O1", "FXT1-O2"})
        self.assertEqual(result["coverage"],
                         {"FXT1-O1": ["FXT1-AS1"], "FXT1-O2": ["FXT1-AS1"]})
        self.assertEqual(result["assessments"][0]["work"],
                         "diagnose a supplied failure and explain a correction.")
        self.assertEqual(result["modules"][0]["number"], 1)
        self.assertEqual(result["modules"][0]["lessons"][0]["title"],
                         "Inspect a given failure trace")

    def test_repeated_exports_have_identical_bytes(self):
        source = self.snapshot()
        first = canonical_json(export_course(source, "FXT1"))
        second = canonical_json(export_course(source, "FXT1"))
        self.assertEqual(first, second)
        self.assertTrue(first.endswith(b"\n"))
        self.assertNotIn(str(self.repo).encode(), first)

    def test_dirty_worktree_and_new_head_do_not_change_pinned_revision(self):
        old = canonical_json(export_course(self.snapshot(), "FXT1"))
        self.course.write_text(
            self.course.read_text(encoding="utf-8").replace(
                "Diagnose an unfamiliar request failure using observations.",
                "Diagnose a DIFFERENT observed request failure.",
            ), encoding="utf-8",
        )
        self.assertEqual(old, canonical_json(export_course(self.snapshot(), "FXT1")))
        current = self.commit("change HEAD after the pinned version")
        self.assertEqual(old, canonical_json(export_course(self.snapshot(), "FXT1")))
        self.assertNotEqual(old, canonical_json(export_course(self.snapshot(current), "FXT1")))

    def test_direct_checkout_does_not_supply_missing_commit_blob(self):
        self.course.unlink()
        self.assertEqual(inspect(self.snapshot(), "FXT1")[0]["structuralOutcome"],
                         "passed")
        with self.assertRaisesRegex(SourceError, "not present"):
            self.snapshot("f" * 40)

    def test_reject_short_sha_and_unknown_course(self):
        with self.assertRaisesRegex(SourceError, "40-character"):
            self.snapshot("HEAD")
        result, content = inspect(self.snapshot(), "FXT2")
        self.assertEqual(result["structuralOutcome"], "incomplete")
        self.assertIsNone(content)
        self.assertEqual(result["findings"][0]["category"], "missing_input")

    def test_invalid_course_status_cannot_produce_an_export(self):
        self.course.write_text(
            self.course.read_text(encoding="utf-8").replace(
                "**Status:** `draft`", "**Status:** `accredited`"
            ), encoding="utf-8",
        )
        revision = self.commit("invalid unsupported course status")
        report, _ = inspect(self.snapshot(revision), "FXT1")
        self.assertEqual(report["structuralOutcome"], "failed")
        self.assertTrue(any(f["code"] == "OEE036" for f in report["findings"]))
        with self.assertRaises(ExportBlocked):
            export_course(self.snapshot(revision), "FXT1")

    def test_ordered_prerequisite_range_and_duplicate_course_ids(self):
        from tooling.oee_toolkit.core import prerequisites
        self.assertEqual(
            prerequisites("[FXT4](FXT4.md), FXT1–FXT3, [FXT4](FXT4.md)"),
            ["FXT4", "FXT1", "FXT2", "FXT3"],
        )
        with self.assertRaisesRegex(SourceError, "invalid prerequisite"):
            prerequisites("FXT1–APP3")
        with self.assertRaisesRegex(SourceError, "no resolvable"):
            prerequisites("an unresolvable requirement")

    def test_old_format_rejected_and_not_exported(self):
        self.course.write_text(
            (FIXTURES / "legacy_v010_course.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        version = self.commit("unsupported old format")
        report, capture = inspect(self.snapshot(version), "FXT1")
        self.assertEqual(report["structuralOutcome"], "incomplete")
        self.assertIsNone(capture)
        with self.assertRaises(ExportBlocked):
            export_course(self.snapshot(version), "FXT1")

    def test_linked_brief_resolves_from_same_git_revision(self):
        self.course.write_text(
            (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        brief = self.course.parent / "linked_brief.md"
        brief.write_text(
            (FIXTURES / "linked_brief.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        version = self.commit("linked public brief")
        before = canonical_json(export_course(self.snapshot(version), "FXT1"))
        brief.write_text("uncommitted conflicting assessment content", encoding="utf-8")
        after = canonical_json(export_course(self.snapshot(version), "FXT1"))
        self.assertEqual(before, after)
        result = json.loads(before)
        self.assertEqual(result["assessments"][0]["location"]["path"],
                         "curriculum/FXT/linked_brief.md")
        self.assertIn("traceable cause", result["assessments"][0]["criteria"])

    def test_missing_linked_brief_never_exports_partial_assessment(self):
        self.course.write_text(
            (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        version = self.commit("missing referenced brief")
        report, _ = inspect(self.snapshot(version), "FXT1")
        self.assertEqual(report["structuralOutcome"], "incomplete")
        self.assertTrue(any(item["category"] == "missing_input"
                            for item in report["findings"]))
        with self.assertRaises(ExportBlocked):
            export_course(self.snapshot(version), "FXT1")

    def test_escape_outside_repo_is_rejected(self):
        self.course.write_text(
            (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8").replace(
                "linked_brief.md", "../../../outside.md",
            ), encoding="utf-8",
        )
        version = self.commit("unsafe reference")
        report, _ = inspect(self.snapshot(version), "FXT1")
        self.assertEqual(report["structuralOutcome"], "failed")
        self.assertTrue(any(item["category"] == "unsafe_reference"
                            for item in report["findings"]))

    def test_git_symlink_input_is_not_followed(self):
        target = self.course.parent / "other.md"
        target.write_text(self.course.read_text(encoding="utf-8"), encoding="utf-8")
        self.course.unlink()
        try:
            self.course.symlink_to(target.name)
        except OSError:
            self.skipTest("symlink creation unavailable on this platform")
        version = self.commit("symlink course is unsafe")
        report, _ = inspect(self.snapshot(version), "FXT1")
        self.assertEqual(report["structuralOutcome"], "failed")
        self.assertEqual(report["findings"][0]["category"], "unsafe_reference")

    def test_cli_output_is_atomic_and_preserves_existing_file_on_error(self):
        output = self.repo / "result.json"
        ok = self.cli("export", "--course", "FXT1", "--output", str(output))
        self.assertEqual(ok.returncode, 0, ok.stderr)
        self.assertEqual(json.loads(output.read_text())["source"]["revision"],
                         self.revision)
        output.write_text("do not erase", encoding="utf-8")
        failed = self.cli("export", "--course", "FXT2", "--output", str(output))
        self.assertEqual(failed.returncode, 3, failed.stderr)
        self.assertEqual(output.read_text(), "do not erase")

    def test_cli_check_all_reports_unsupported_course_as_incomplete(self):
        other = self.repo / "curriculum" / "FXT" / "FXT2.md"
        other.write_text((FIXTURES / "legacy_v010_course.md").read_text(),
                         encoding="utf-8")
        self.revision = self.commit("add unsupported active course")
        scan = self.cli("check", "--all", "--json")
        self.assertEqual(scan.returncode, 3, scan.stderr)
        body = json.loads(scan.stdout)
        self.assertEqual(body["structuralOutcome"], "incomplete")
        self.assertTrue(body["manualReviewRequired"])
        self.assertEqual(len(body["courses"]), 2)
        self.assertEqual([item["structuralOutcome"] for item in body["courses"]],
                         ["passed", "incomplete"])

    def test_cli_json_is_stable_and_discloses_revision(self):
        first = self.cli("check", "--course", "FXT1", "--json")
        again = self.cli("check", "--course", "FXT1", "--json")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, again.stdout)
        self.assertEqual(json.loads(first.stdout)["source"]["revision"], self.revision)
        self.assertNotIn(str(self.repo), first.stdout)

    def test_cli_invalid_revision_is_incomplete(self):
        result = subprocess.run(
            [sys.executable, "-m", "tooling.oee_toolkit", "export",
             "--repo", str(self.repo), "--revision", "1" * 40,
             "--course", "FXT1", "--output", "-"],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 3)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
