"""Guard the first course-level SEF v0.2.0 migration after the initial pilots."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF2.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF2MigrationTests(unittest.TestCase):
    def test_v020_outcome_checker_accepts_sef2(self):
        result = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "check-outcome-curriculum.py"),
                "--course",
                str(COURSE),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_program_validator_accepts_mixed_sef_curriculum(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-sef-curriculum.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("3 v0.2.0, 7 legacy", result.stdout)

    def test_stable_outcome_ids_are_covered_by_five_required_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        outcomes_section = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"^- \*\*(SEF2-O\d+):\*\*", outcomes_section, re.M))
        self.assertEqual(len(outcomes), 10)

        completion = text.split("\n## Completion requirements\n", 1)[1]
        assessment_blocks = re.split(
            r"(?=^- \*\*SEF2-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(assessment_blocks), 5)
        covered = set()
        for number, block in enumerate(assessment_blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF2-AS{number}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            covered.update(
                re.findall(r"SEF2-O\d+", re.search(
                    r"(?m)^  - Outcomes: (.+)$", block
                ).group(1))
            )
        self.assertEqual(covered, outcomes)

    def test_revised_course_does_not_reintroduce_legacy_lab_gates(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF2](SEF2.md)", catalog)
        self.assertIn("SEF1, SEF2 and SEF10 use", catalog)


if __name__ == "__main__":
    unittest.main()
