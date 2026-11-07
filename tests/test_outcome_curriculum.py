"""Regression tests for OEE v0.2.0 course-structure validation."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check-outcome-curriculum.py"

COURSE = """# APP1 — Web and Internet Foundations

**Program:** APP — Application Engineering
**Type:** \`course\`
**Prerequisites:** none
**Duration:** 8 weeks
**Status:** \`draft\`

## Overview

Study the behavior of browsers and requests.

## Learning outcomes

- **APP1-O1:** Trace a web request through name resolution and transport.
- **APP1-O2:** Explain and diagnose an HTTP response failure.

## Modules

### Module 1 — Request Lifecycles

#### Outcomes
- APP1-O1
- APP1-O2

#### Lessons
1. Client/server communications
2. Inspect a supplied request trace
3. Optional reflection on failure modes

## Completion requirements

- **APP1-AS1** (required practical investigation)
  - Outcomes: APP1-O1, APP1-O2
  - Work: diagnose a request trace and explain its failure.
  - Evidence: annotated trace and written reasoning.
  - Criteria: distinguish layers and justify conclusions.

"""


def validate(text, filename="APP1.md"):
    with tempfile.TemporaryDirectory() as directory:
        file = Path(directory) / filename
        file.write_text(text, encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--course", str(file)],
            capture_output=True, text=True, check=False,
        )


class OutcomeCurriculumValidatorTests(unittest.TestCase):
    def test_valid_course_without_test_or_lab_passes(self):
        result = validate(COURSE)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("1 checked", result.stdout)

    def test_missing_course_outcome_id_fails(self):
        result = validate(COURSE.replace(
            "- **APP1-O2:** Explain and diagnose an HTTP response failure.",
            "- Explain and diagnose an HTTP response failure.",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("every course outcome bullet", result.stderr)

    def test_uncovered_outcome_fails(self):
        result = validate(COURSE.replace(
            "Outcomes: APP1-O1, APP1-O2", "Outcomes: APP1-O1",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("APP1-O2 has no required summative assessment", result.stderr)

    def test_undefined_assessment_reference_fails(self):
        result = validate(COURSE.replace(
            "Outcomes: APP1-O1, APP1-O2", "Outcomes: APP1-O1, APP1-O3",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown course outcome APP1-O3", result.stderr)

    def test_optional_assessment_does_not_count_toward_completion(self):
        result = validate(COURSE.replace(
            "(required practical investigation)", "(optional practice)",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no required summative assessments", result.stderr)

    def test_missing_assessment_criteria_fails(self):
        result = validate(COURSE.replace(
            "  - Criteria: distinguish layers and justify conclusions.\n", "",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing or empty criteria", result.stderr)

    def test_duplicate_assessment_id_fails(self):
        block = COURSE.split("- **APP1-AS1**", 1)[1]
        result = validate(COURSE + "- **APP1-AS1**" + block)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate assessment ID APP1-AS1", result.stderr)

    def test_missing_module_learning_sequence_fails(self):
        result = validate(COURSE.replace(
            "1. Client/server communications\n2. Inspect a supplied request trace\n"
            "3. Optional reflection on failure modes\n", "",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ordered learning sequence is empty", result.stderr)

    def test_project_requires_deliverables_and_defense(self):
        result = validate(COURSE.replace("**Type:** \`course\`", "**Type:** \`project\`"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires public deliverables", result.stderr)
        self.assertIn("requires a reviewable technical defense", result.stderr)

    def test_project_with_public_deliverables_and_defense_passes(self):
        project = COURSE.replace("**Type:** \`course\`", "**Type:** \`project\`")
        project += "\nRequired deliverables: reproducible artifact.\n"
        project += "Project defense: review design choices and limitations.\n"
        result = validate(project)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_foreign_course_outcome_reference_fails(self):
        result = validate(COURSE.replace(
            "Outcomes: APP1-O1, APP1-O2", "Outcomes: APP1-O1, SEF1-O1",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("foreign outcome reference SEF1-O1", result.stderr)

    def test_wrong_course_heading_fails(self):
        result = validate(COURSE.replace(
            "# APP1 — Web and Internet Foundations",
            "# Not a canonical course heading",
        ))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("expected a first-line course heading", result.stderr)


if __name__ == "__main__":
    unittest.main()
