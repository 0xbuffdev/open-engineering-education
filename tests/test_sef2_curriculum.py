"""Regression checks for SEF2's current v0.2.0 course contract."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF2.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF2CurriculumTests(unittest.TestCase):
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

    def test_program_validator_accepts_current_sef_curriculum(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-sef-curriculum.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        current = sum(
            "**Specification:** `v0.2.0`" in course.read_text(encoding="utf-8")
            for course in (ROOT / "curriculum" / "SEF").glob("SEF[0-9]*.md")
        )
        self.assertEqual(current, 11)
        self.assertIn("(OEE v0.2.0)", result.stdout)

    def test_stable_outcome_ids_are_covered_by_six_required_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        outcomes_section = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"^- \*\*(SEF2-O\d+):\*\*", outcomes_section, re.M))
        self.assertEqual(outcomes, {f"SEF2-O{i}" for i in range(1, 13)})

        completion = text.split("\n## Completion requirements\n", 1)[1]
        assessment_blocks = re.split(
            r"(?=^- \*\*SEF2-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(assessment_blocks), 6)
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

    def test_course_uses_current_summative_contract(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF2](SEF2.md)", catalog)
        self.assertIn("10–12 weeks", catalog)
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("OEE `v0.2.0` outcome and summative assessment contracts", catalog)


if __name__ == "__main__":
    unittest.main()
