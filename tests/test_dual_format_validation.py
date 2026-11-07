"""Integration regression tests for mixed legacy and v0.2.0 curricula.

Tests use copied curriculum directories. No existing course is rewritten.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from course_format_versions import is_outcome_course  # noqa: E402


def load_validator(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def example_course(
    code: str, title: str, program: str, duration: str,
    prerequisites: str, project: bool = False,
) -> str:
    kind = "project" if project else "course"
    extra = (
        "\nRequired project deliverables: documented working artifact.\n"
        "Project defense: explain decisions, results, and limitations.\n"
        if project else ""
    )
    return f"""# {code} — {title}

**Program:** {program}
**Type:** `{kind}`
**Prerequisites:** {prerequisites}
**Duration:** {duration}
**Status:** `draft`
**Specification:** `v0.2.0`

## Overview

Develop and demonstrate a coherent capability without prescribed test/lab pairs.

## Learning outcomes

- **{code}-O1:** Explain and diagnose a system failure.
- **{code}-O2:** Justify a technical decision using observations.

## Modules

### Module 1 — Understand and Diagnose

#### Outcomes
- {code}-O1
- {code}-O2

#### Lessons
1. System behavior
2. Failure diagnosis
3. Design reasoning

## Completion requirements

- **{code}-AS1** (required investigation)
  - Outcomes: {code}-O1, {code}-O2
  - Work: diagnose an unfamiliar failure and justify a resolution.
  - Criteria: correct causal explanation supported by observations.
  - Evidence: diagnostic record and concise reasoning.
{extra}
""".replace("\\`", "`")


class DualFormatValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = load_validator("app_legacy_validation_test", "check-app-curriculum.py")
        cls.sef = load_validator("sef_legacy_validation_test", "check-sef-curriculum.py")

    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copytree(ROOT / "curriculum", self.root / "curriculum")
        shutil.copytree(ROOT / "spec", self.root / "spec")
        self.app.ROOT = self.root
        self.app.APP = self.root / "curriculum" / "APP"
        self.sef.ROOT = self.root
        self.sef.SEF = self.root / "curriculum" / "SEF"

    def replace_course(self, code: str, content: str):
        area = "APP" if code.startswith("APP") else "SEF"
        path = self.root / "curriculum" / area / f"{code}.md"
        path.write_text(content, encoding="utf-8")

    def test_untouched_legacy_catalogs_still_pass(self):
        self.assertEqual(self.app.validate(), 0)
        self.assertEqual(self.sef.validate(), 0)

    def test_migrated_app1_has_no_required_lab_or_quiz(self):
        course = example_course(
            "APP1", "Web & Internet Foundations", "APP — Application Engineering",
            "7 weeks", "[SEF10](../SEF/SEF10.md) — Software Engineering Foundations",
        )
        self.replace_course("APP1", course)
        self.assertEqual(self.app.validate(), 0)

    def test_migrated_sef1_has_no_required_lab_or_quiz(self):
        course = example_course(
            "SEF1", "Demystifying the Computer System",
            "SEF — Software Engineering Foundations", "5 weeks", "none",
        )
        self.replace_course("SEF1", course)
        self.assertEqual(self.sef.validate(), 0)

    def test_migrated_sef10_uses_project_evidence_and_defense(self):
        course = example_course(
            "SEF10", "Software Engineering Foundations Capstone",
            "SEF — Software Engineering Foundations", "8–10 weeks",
            "SEF1–SEF9", project=True,
        )
        self.replace_course("SEF10", course)
        self.assertEqual(self.sef.validate(), 0)

    def test_modern_app_course_with_missing_assessment_criteria_fails(self):
        course = example_course(
            "APP1", "Web & Internet Foundations", "APP — Application Engineering",
            "7 weeks", "[SEF10](../SEF/SEF10.md) — Software Engineering Foundations",
        )
        self.replace_course("APP1", course.replace(
            "  - Criteria: correct causal explanation supported by observations.\n", ""
        ))
        self.assertNotEqual(self.app.validate(), 0)

    def test_modern_sef_with_uncovered_outcome_fails(self):
        course = example_course(
            "SEF1", "Demystifying the Computer System",
            "SEF — Software Engineering Foundations", "5 weeks", "none",
        )
        self.replace_course("SEF1", course.replace(
            "Outcomes: SEF1-O1, SEF1-O2", "Outcomes: SEF1-O1"
        ))
        self.assertNotEqual(self.sef.validate(), 0)

    def test_modern_app_preserves_catalog_validation(self):
        course = example_course(
            "APP1", "Web & Internet Foundations", "APP — Application Engineering",
            "17 weeks", "[SEF10](../SEF/SEF10.md) — Software Engineering Foundations",
        )
        self.replace_course("APP1", course)
        self.assertNotEqual(self.app.validate(), 0)

    def test_modern_app_preserves_prerequisite_validation(self):
        course = example_course(
            "APP1", "Web & Internet Foundations", "APP — Application Engineering",
            "7 weeks", "none",
        )
        self.replace_course("APP1", course)
        self.assertNotEqual(self.app.validate(), 0)

    def test_unmarked_partial_migration_gets_new_validation(self):
        course = example_course(
            "SEF1", "Demystifying the Computer System",
            "SEF — Software Engineering Foundations", "5 weeks", "none",
        ).replace("**Specification:** `v0.2.0`\n", "")
        self.assertTrue(is_outcome_course(course))
        self.replace_course("SEF1", course.replace(
            "  - Evidence: diagnostic record and concise reasoning.\n", ""
        ))
        self.assertNotEqual(self.sef.validate(), 0)

    def test_invalid_explicit_future_version_fails_closed(self):
        course = example_course(
            "SEF1", "Demystifying the Computer System",
            "SEF — Software Engineering Foundations", "5 weeks", "none",
        ).replace("**Specification:** `v0.2.0`", "**Specification:** `v0.3.0`")
        with self.assertRaisesRegex(ValueError, "unsupported"):
            is_outcome_course(course)
        self.replace_course("SEF1", course)
        self.assertNotEqual(self.sef.validate(), 0)

    def test_legacy_marker_cannot_coexist_with_new_ids(self):
        course = example_course(
            "APP1", "Web & Internet Foundations", "APP — Application Engineering",
            "7 weeks", "[SEF10](../SEF/SEF10.md) — Software Engineering Foundations",
        ).replace("**Specification:** `v0.2.0`", "**Specification:** `v0.1.0`")
        with self.assertRaisesRegex(ValueError, "conflicts"):
            is_outcome_course(course)
        self.replace_course("APP1", course)
        self.assertNotEqual(self.app.validate(), 0)

    def test_legacy_course_without_final_lab_still_fails(self):
        path = self.root / "curriculum" / "APP" / "APP2.md"
        content = path.read_text(encoding="utf-8")
        self.assertIn("**Final integration lab", content)
        self.replace_course("APP2", content.replace(
            "**Final integration lab", "**Removed integration lab"
        ))
        self.assertNotEqual(self.app.validate(), 0)


if __name__ == "__main__":
    unittest.main()
