"""Regression tests for deterministic, source-located OEE structural findings.

All fixtures are synthetic. No learner work is graded and no curriculum is
rewritten. These are repository maintenance checks, not official Toolkit APIs.
"""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "ot_i02"
SCRIPT = ROOT / "scripts" / "check-outcome-curriculum.py"
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("oee_diagnostics", SCRIPT)
checker = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = checker
spec.loader.exec_module(checker)


def sample():
    return (FIXTURES / "valid_v020_course.md").read_text(encoding="utf-8")


class StructuralDiagnosticsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.course = self.root / "FXT1.md"
        self.course.write_text(sample(), encoding="utf-8")

    def inspect(self, content=None):
        if content is not None:
            self.course.write_text(content, encoding="utf-8")
        return checker.inspect_course(self.course)

    def find(self, report, code):
        return next(f for f in report["findings"] if f["code"] == code)

    def test_valid_source_passes_but_needs_human_review(self):
        result = self.inspect()
        self.assertEqual(result["structuralOutcome"], "passed", result["findings"])
        self.assertTrue(result["manualReviewRequired"])
        self.assertEqual(result["checksPerformed"], ["v0.2.0-structure"])
        self.assertEqual(result["findings"], [])

    def test_duplicate_outcome_points_to_its_actual_source_line(self):
        content = sample().replace("## Modules", "- **FXT1-O1:** Duplicate.\n\n## Modules")
        finding = self.find(self.inspect(content), "OEE007")
        line = content.splitlines().index("- **FXT1-O1:** Duplicate.") + 1
        self.assertEqual(finding["location"], {"path": "FXT1.md", "line": line})
        self.assertEqual(finding["category"], "structural_violation")
        self.assertEqual(self.inspect()["structuralOutcome"], "failed")

    def test_invalid_module_reference_points_to_the_actual_reference_line(self):
        content = sample().replace("- FXT1-O2\n", "- APP9-O9\n", 1)
        finding = self.find(self.inspect(content), "OEE014")
        self.assertEqual(finding["location"]["line"],
                         content.splitlines().index("- APP9-O9") + 1)

    def test_missing_criteria_reports_stable_rule_and_correct_assessment_line(self):
        content = sample().replace(
            "  - Criteria: demonstrate causal evidence and reproducible verification.\n", ""
        )
        finding = self.find(self.inspect(content), "OEE023")
        self.assertIn("missing or empty criteria", finding["message"])
        self.assertEqual(finding["location"]["line"],
                         content.splitlines().index(
                             "- **FXT1-AS1** (required investigation)") + 1)

    def test_linked_public_brief_passes_and_covers_required_outcomes(self):
        linked = (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8")
        brief = (FIXTURES / "linked_brief.md").read_text(encoding="utf-8")
        self.course.write_text(linked, encoding="utf-8")
        (self.root / "linked_brief.md").write_text(brief, encoding="utf-8")
        result = self.inspect()
        self.assertEqual(result["structuralOutcome"], "passed", result["findings"])

    def test_project_details_may_be_published_in_linked_brief(self):
        linked = (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8")
        linked = linked.replace("**Type:** `course`", "**Type:** `project`")
        brief = (FIXTURES / "linked_brief.md").read_text(encoding="utf-8")
        brief += "\nRequired deliverables: reproducible artifact.\n"
        brief += "Project defense: explain design and limitations.\n"
        self.course.write_text(linked, encoding="utf-8")
        (self.root / "linked_brief.md").write_text(brief, encoding="utf-8")
        report = self.inspect()
        self.assertEqual(report["structuralOutcome"], "passed", report["findings"])

    def test_empty_linked_brief_field_points_to_brief_source(self):
        linked = (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8")
        brief = (FIXTURES / "linked_brief.md").read_text(encoding="utf-8")
        brief = brief.replace(
            "- Criteria: establish a traceable cause and a testable correction.",
            "- Criteria: ",
        )
        self.course.write_text(linked, encoding="utf-8")
        (self.root / "linked_brief.md").write_text(brief, encoding="utf-8")
        report = self.inspect()
        self.assertEqual(report["structuralOutcome"], "failed")
        finding = self.find(report, "OEE023")
        self.assertEqual(finding["location"], {
            "path": "linked_brief.md",
            "line": brief.splitlines().index("- Criteria: ") + 1,
        })

    def test_missing_linked_brief_is_incomplete_not_false_violation(self):
        linked = (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8")
        result = self.inspect(linked)
        finding = self.find(result, "OEE020")
        self.assertEqual(result["structuralOutcome"], "incomplete")
        self.assertEqual(finding["category"], "missing_input")
        self.assertFalse(any(f["code"] == "OEE029" for f in result["findings"]))

    def test_unsafe_absolute_or_parent_escape_fails_closed(self):
        original = (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8")
        for path in ("/tmp/brief.md", "../outside.md", "subdir/../../outside.md"):
            with self.subTest(path=path):
                report = self.inspect(original.replace("linked_brief.md", path))
                self.assertEqual(report["structuralOutcome"], "failed")
                self.assertEqual(self.find(report, "OEE020")["category"], "unsafe_reference")

    def test_remote_brief_is_incomplete_parser_limitation_not_spec_violation(self):
        original = (FIXTURES / "linked_brief_v020.md").read_text(encoding="utf-8")
        report = self.inspect(original.replace(
            "linked_brief.md", "https://example.org/brief.md"
        ))
        self.assertEqual(report["structuralOutcome"], "incomplete")
        self.assertEqual(self.find(report, "OEE020")["category"], "parser_limitation")

    def test_unknown_explicit_specification_is_not_supported(self):
        report = self.inspect(sample().replace("`v0.2.0`", "`v0.1.0`"))
        self.assertEqual(report["structuralOutcome"], "incomplete")
        self.assertEqual(self.find(report, "OEE034")["category"], "unsupported_format")

    def test_missing_required_source_is_incomplete(self):
        missing = checker.inspect_course(self.root / "nonexistent.md")
        self.assertEqual(missing["structuralOutcome"], "incomplete")
        self.assertEqual(self.find(missing, "OEE032")["location"]["line"], 1)

    def test_json_is_deterministic_and_excludes_local_machine_path(self):
        command = [sys.executable, str(SCRIPT), "--course", str(self.course),
                   "--format", "json"]
        first = subprocess.run(command, capture_output=True, text=True, check=False)
        second = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual(payload["structuralOutcome"], "passed")
        self.assertEqual(payload["scope"], "course")
        self.assertNotIn(str(self.root), first.stdout)

    def test_json_failure_carries_structured_source_span_and_exit_code(self):
        self.course.write_text(sample().replace(
            "  - Evidence: annotated trace and written technical explanation.\n", ""
        ), encoding="utf-8")
        run = subprocess.run([sys.executable, str(SCRIPT), "--course", str(self.course),
                              "--format", "json"], capture_output=True,
                             text=True, check=False)
        self.assertEqual(run.returncode, 1, run.stderr)
        payload = json.loads(run.stdout)
        self.assertEqual(payload["structuralOutcome"], "failed")
        finding = next(f for f in payload["findings"] if f["code"] == "OEE023")
        self.assertEqual(finding["location"]["path"], "FXT1.md")
        self.assertGreater(finding["location"]["line"], 1)

    def test_noncanonical_assessment_layout_is_parser_limitation(self):
        source = sample().replace(
            "- **FXT1-AS1** (required investigation)",
            "### FXT1-AS1 — Required investigation",
        )
        result = self.inspect(source)
        self.assertEqual(result["structuralOutcome"], "incomplete", result["findings"])
        self.assertEqual(self.find(result, "OEE035")["category"], "parser_limitation")
        self.assertFalse(any(f["code"] in ("OEE027", "OEE028", "OEE029")
                             for f in result["findings"]))

    def test_unsupported_format_exit_is_incomplete(self):
        self.course.write_text((FIXTURES / "unsupported_v010_course.md").read_text(
            encoding="utf-8"), encoding="utf-8")
        run = subprocess.run([sys.executable, str(SCRIPT), "--course", str(self.course)],
                             capture_output=True, text=True, check=False)
        self.assertEqual(run.returncode, 3)
        self.assertIn("unsupported_format", run.stderr)


if __name__ == "__main__":
    unittest.main()
