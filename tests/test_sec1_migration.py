"""SEC1 staging checks; competency mapping, not arbitrary lesson-count quotas."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC1.md"
CATALOG = COURSE.parent / "README.md"


class SEC1MigrationTests(unittest.TestCase):
    def test_official_outcome_checker(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            capture_output=True, text=True, check=False, cwd=ROOT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_and_legacy_boundaries(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF10](../SEF/SEF10.md)", source)
        for field in ("**Type:** `course`", "**Status:** `draft`",
                      "**Specification:** `v0.2.0`",
                      "**Duration:** 7–10 weeks"):
            self.assertIn(field, source)
        self.assertIn(
            "| [SEC1](SEC1.md) | Security Foundations & Threat Modeling "
            "| 7–10 weeks | SEF10 (assessed SEF completion) | `course` |",
            catalog)
        self.assertIn("SEC2–SEC9 remain legacy", catalog)
        self.assertIn("SEC8 legacy AI5 prerequisite", catalog)

    def test_all_outcomes_taught_and_assessed(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        expected = set(re.findall(r"(?m)^- \*\*(SEC1-O\d+):\*\*", learning))
        self.assertTrue(expected)
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        starts = list(re.finditer(r"(?m)^### Module \d+ — ", modules))
        taught = set()
        for index, marker in enumerate(starts):
            stop = starts[index + 1].start() if index + 1 < len(starts) else len(modules)
            part = modules[marker.start():stop]
            self.assertIn("#### Outcomes", part)
            self.assertIn("#### Lessons", part)
            targets, lessons = part.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC1-O\d+)$", targets))
            self.assertTrue(refs)
            self.assertTrue(refs <= expected)
            taught.update(refs)
            self.assertRegex(lessons, r"(?m)^1\. \*\*\S")
        self.assertEqual(taught, expected)
        completion = text.split("\n## Completion requirements\n", 1)[1]
        assessments = re.split(
            r"(?=^- \*\*SEC1-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(assessments)
        covered = set()
        for assessment in assessments:
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(assessment,
                                 rf"(?m)^  - \*\*{field}:\*\* \S")
            match = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$",
                              assessment)
            self.assertIsNotNone(match)
            covered.update(re.findall(r"SEC1-O\d+", match.group(1)))
        self.assertEqual(covered, expected)

    def test_formative_is_optional_and_work_requires_scope(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("optional formative feedback", text)
        self.assertIn("No unauthorized access", text)
        self.assertNotIn("kind: `test`", text)
        self.assertNotIn("kind: `lab`", text)


if __name__ == "__main__":
    unittest.main()
