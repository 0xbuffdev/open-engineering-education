"""Regression tests for the derived, non-normative migration inventory."""

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "curriculum_inventory.py"
spec = importlib.util.spec_from_file_location("curriculum_inventory", SCRIPT)
inventory = importlib.util.module_from_spec(spec)
spec.loader.exec_module(inventory)
SHA = "a" * 40


def course(code, prereqs="none", version="v0.2.0", assessment=True):
    declared = f"**Specification:** `{version}`\n" if version else ""
    evaluation = (f"- **{code}-AS1** (required investigation)\n"
                  f"  - Outcomes: {code}-O1\n"
                  "  - Work: construct and investigate a model.\n"
                  "  - Criteria: explain the observed behavior.\n"
                  "  - Evidence: reproducible notes and trace.\n") if assessment else ""
    return (f"# {code} — Sample\n\n**Type:** `course`\n**Prerequisites:** {prereqs}\n"
            f"**Duration:** 1 week\n**Status:** `draft`\n{declared}\n"
            f"## Overview\n\nA sample.\n\n## Learning outcomes\n\n"
            f"- **{code}-O1:** Explain a measurable result.\n\n## Modules\n\n"
            f"### Module 1 — Model\n\n#### Outcomes\n\n- {code}-O1\n\n"
            "#### Lessons\n\n1. Trace an example\n\n## Completion requirements\n\n"
            f"{evaluation}")


def legacy_course(code, prereqs="none"):
    return (f"# {code} — Legacy\n\n**Type:** `course`\n"
            f"**Prerequisites:** {prereqs}\n**Duration:** 1 week\n**Status:** `draft`\n\n"
            "## Overview\n\nA sample.\n\n## Learning outcomes\n\n"
            "- Explain a concept without a stable ID.\n\n## Modules\n\n"
            "### Module 1 — Basics\n\n#### Outcomes\n\n- Explain a concept.\n\n"
            "#### Lessons\n\n1. A lesson — `lesson`\n")


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "scripts").mkdir()
        for filename in ("course_format_versions.py", "check-outcome-curriculum.py"):
            shutil.copyfile(ROOT / "scripts" / filename, self.root / "scripts" / filename)
        (self.root / "curriculum").mkdir()
        (self.root / "curriculum" / "README.md").write_text(
            "| Code | Program | Courses | Directory |\n"
            "| --- | --- | --- | --- |\n"
            "| `SEF` | Foundations | 2 | [SEF/](SEF/) |\n"
            "| `APP` | Apps | 1 core | [APP/](APP/) |\n"
            "| `SYS` | Systems | 9 | [SYS/](SYS/) |\n"
            "| `AI` | AI | 9 | [AI/](AI/) |\n"
            "| `SEC` | Security | 9 | [SEC/](SEC/) |\n", encoding="utf-8")
        folder = self.root / "curriculum" / "SEF"
        folder.mkdir()
        (folder / "README.md").write_text(
            "# SEF\n\n## Courses\n\n"
            "| Course | Title | Duration | Prerequisite | Kind |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| [SEF1](SEF1.md) | Sample | 1 week | — | `course` |\n"
            "| [SEF2](SEF2.md) | Second | 1 week | SEF1 | `course` |\n", encoding="utf-8")
        (folder / "SEF1.md").write_text(course("SEF1"), encoding="utf-8")
        (folder / "SEF2.md").write_text(legacy_course("SEF2", "SEF1"), encoding="utf-8")

    def report(self, prs=None):
        return inventory.build_inventory(self.root, SHA, prs)

    def test_derived_counts_and_missing_programs(self):
        report = self.report()
        courses = {c["code"]: c for c in report["courses"]}
        self.assertEqual(report["source_commit"], SHA)
        self.assertEqual(courses["SEF1"]["format"], "v0.2.0")
        self.assertEqual(courses["SEF1"]["structural_validation"], "passed")
        self.assertEqual(courses["SEF1"]["covered_outcome_count"], 1)
        self.assertEqual(courses["SEF1"]["assessment_count"], 1)
        self.assertEqual(courses["SEF1"]["learner_validation"], "not_established")
        self.assertEqual(courses["SEF2"]["prerequisites"], ["SEF1"])
        self.assertEqual(courses["SEF2"]["format"], "legacy_unsupported")
        self.assertIsNone(courses["SEF2"]["outcome_count"])
        self.assertEqual(next(p for p in report["programs"] if p["program"] == "SYS")["missing_catalog_entries"], 9)

    def test_pending_pr_is_not_adopted_curriculum(self):
        prs = [{"number": 51, "url": "https://github.com/0xbuffdev/open-engineering-education/pull/51",
                "head_sha": "b" * 40, "files": ["curriculum/SYS/SYS1.md", "curriculum/SYS/README.md"]}]
        rows = {row["code"]: row for row in self.report(prs)["courses"]}
        self.assertEqual(rows["SYS1"]["format"], "pending_pr_unreviewed")
        self.assertIsNone(rows["SYS1"]["source_sha"])
        self.assertEqual(rows["SYS1"]["source_prs"][0]["head_sha"], "b" * 40)
        self.assertEqual(rows["SYS1"]["learner_validation"], "not_established")

    def test_conflicting_spec_and_uncovered_outcome_cannot_pass(self):
        path = self.root / "curriculum" / "SEF" / "SEF1.md"
        path.write_text(course("SEF1", version="v9.9.9"), encoding="utf-8")
        row = next(r for r in self.report()["courses"] if r["code"] == "SEF1")
        self.assertEqual(row["format"], "unsupported")
        self.assertEqual(row["structural_validation"], "not_applicable")
        path.write_text(course("SEF1", assessment=False), encoding="utf-8")
        row = next(r for r in self.report()["courses"] if r["code"] == "SEF1")
        self.assertEqual(row["structural_validation"], "failed")
        self.assertEqual(row["uncovered_outcomes"], ["SEF1-O1"])

    def test_missing_prerequisite_and_catalog_mismatch_visible(self):
        path = self.root / "curriculum" / "SEF" / "SEF2.md"
        path.write_text(legacy_course("SEF2", "SEF3"), encoding="utf-8")
        row = next(r for r in self.report()["courses"] if r["code"] == "SEF2")
        self.assertIn("course prerequisites differ from catalog", row["prerequisite_issues"])
        self.assertIn("missing prerequisite course: SEF3", row["prerequisite_issues"])

    def test_catalog_missing_file_is_visible(self):
        (self.root / "curriculum" / "SEF" / "SEF2.md").unlink()
        row = next(r for r in self.report()["courses"] if r["code"] == "SEF2")
        self.assertEqual(row["format"], "missing")
        self.assertIsNone(row["source_sha"])

    def test_linked_ranges_are_normalized(self):
        codes, errors = inventory.prerequisites("[SEF1](SEF1.md)–[SEF3](SEF3.md)")
        self.assertEqual(codes, ["SEF1", "SEF2", "SEF3"])
        self.assertEqual(errors, [])

    def test_declared_total_drift_is_reported(self):
        index = self.root / "curriculum" / "README.md"
        index.write_text(index.read_text(encoding="utf-8").replace("Foundations | 2 |", "Foundations | 1 |"), encoding="utf-8")
        issues = next(p for p in self.report()["programs"] if p["program"] == "SEF")["issues"]
        self.assertTrue(any("overview declares 1 courses but catalog lists 2" in issue for issue in issues))

    def test_cli_outputs_deterministic_json_without_network(self):
        process = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root),
                                  "--source-sha", SHA, "--format", "json"],
                                 text=True, capture_output=True, check=False)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)["pr_scan"], "not_requested")
        self.assertNotIn("github.com", process.stderr)


if __name__ == "__main__":
    unittest.main()
