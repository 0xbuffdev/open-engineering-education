"""OT-I02: frozen v0.2.0 fixtures and unsupported-format rejection.

The pre-Toolkit scripts are migration utilities, not supported public APIs.
No legacy parser or new normative authoring format is introduced here.
"""

from __future__ import annotations

from pathlib import Path
import importlib.util
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures" / "ot_i02"
sys.path.insert(0, str(SCRIPTS))
from course_format_versions import is_outcome_course  # noqa: E402

spec = importlib.util.spec_from_file_location("ot_i02_checker", SCRIPTS / "check-outcome-curriculum.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def fixture(name):
    return (FIXTURES / name).read_text(encoding="utf-8")


def errors(text):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "FXT1.md"
        path.write_text(text, encoding="utf-8")
        return checker.validate_course(path)


class ToolkitFixtureContractTests(unittest.TestCase):
    def setUp(self):
        self.good = fixture("valid_v020_course.md")

    def test_valid_v020_passes_structural_check(self):
        self.assertTrue(is_outcome_course(self.good))
        self.assertEqual(errors(self.good), [])

    def test_explicit_historical_format_is_not_toolkit_input(self):
        legacy = fixture("legacy_v010_course.md")
        self.assertFalse(is_outcome_course(legacy))
        self.assertTrue(errors(legacy))

    def test_unsupported_and_conflicting_version_markers(self):
        for version, expected in [("v0.3.0", "unsupported"), ("v0.1.0", "conflicts")]:
            with self.subTest(version=version):
                with self.assertRaisesRegex(ValueError, expected):
                    is_outcome_course(self.good.replace("`v0.2.0`", f"`{version}`"))

    def test_unmarked_recognizable_v020_source_is_checked(self):
        course = self.good.replace("**Specification:** `v0.2.0`\n", "")
        self.assertTrue(is_outcome_course(course))
        self.assertEqual(errors(course), [])

    def test_duplicate_outcome_rejected(self):
        course = self.good.replace("## Modules", "- **FXT1-O1:** Repeat outcome.\n\n## Modules")
        self.assertTrue(any("duplicate outcome ID" in e for e in errors(course)))

    def test_duplicate_assessment_rejected(self):
        block = self.good[self.good.index("- **FXT1-AS1** (required investigation)"):]
        self.assertTrue(any("duplicate assessment ID" in e for e in errors(self.good + block)))

    def test_coverage_and_foreign_outcome_fail(self):
        for outcomes, message in [
            ("FXT1-O1", "FXT1-O2 has no required summative assessment"),
            ("FXT1-O1, APP1-O1", "foreign outcome reference APP1-O1"),
        ]:
            with self.subTest(outcomes=outcomes):
                course = self.good.replace("Outcomes: FXT1-O1, FXT1-O2",
                                           "Outcomes: " + outcomes)
                self.assertTrue(any(message in e for e in errors(course)))

    def test_missing_required_assessment_fields_fail(self):
        for field in ("Work", "Criteria", "Evidence"):
            with self.subTest(field=field):
                course = "\n".join(
                    line for line in self.good.splitlines()
                    if not line.strip().startswith("- " + field + ":")
                )
                self.assertTrue(any("missing or empty " + field.lower() in e
                                    for e in errors(course)))

    def test_optional_assessment_cannot_cover_required_outcomes(self):
        course = self.good.replace("(required investigation)", "(optional practice)")
        self.assertIn("no required summative assessments found", errors(course))

    def test_project_requires_defense_and_deliverables(self):
        course = self.good.replace("**Type:** `course`", "**Type:** `project`")
        failures = errors(course)
        self.assertTrue(any("requires public deliverables" in e for e in failures))
        self.assertTrue(any("requires a reviewable technical defense" in e for e in failures))

    def test_supported_local_linked_brief_passes(self):
        from pathlib import Path
        linked = FIXTURES / "linked_brief_v020.md"
        self.assertTrue(is_outcome_course(linked.read_text(encoding="utf-8")))
        report = checker.inspect_course(linked)
        self.assertEqual(report["structuralOutcome"], "passed", report["findings"])
        self.assertEqual(report["findings"], [])

    def test_missing_linked_brief_is_incomplete(self):
        linked = FIXTURES / "linked_brief_v020.md"
        missing = linked.read_text(encoding="utf-8").replace(
            "](linked_brief.md)", "](missing_brief.md)"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "FXT1.md"
            path.write_text(missing, encoding="utf-8")
            report = checker.inspect_course(path)
        self.assertEqual(report["structuralOutcome"], "incomplete")
        self.assertTrue(any(f["category"] == "missing_input" for f in report["findings"]))

    def test_legacy_cli_does_not_pass_direct_outcome_check(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "check-outcome-curriculum.py"), "--course",
             str(FIXTURES / "legacy_v010_course.md")],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.returncode, 3)
        self.assertIn("unsupported legacy/unknown course format", result.stderr)


if __name__ == "__main__":
    unittest.main()
