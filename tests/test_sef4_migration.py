"""Regressions for SEF4's outcome-driven algorithm course migration."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF4.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF4MigrationTests(unittest.TestCase):
    def test_strict_outcome_validator_accepts_sef4(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_program_validator_accepts_mixed_sef_catalog(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        migrated = sum(
            "**Specification:** `v0.2.0`" in course.read_text(encoding="utf-8")
            for course in COURSE.parent.glob("SEF[0-9]*.md")
        )
        self.assertIn(f"{migrated} v0.2.0, {10 - migrated} legacy", result.stdout)

    def test_all_fourteen_outcomes_have_required_assessments(self):
        course = COURSE.read_text(encoding="utf-8")
        learning = course.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"(?m)^- \*\*(SEF4-O\d+):\*\*", learning))
        self.assertEqual(outcomes, {f"SEF4-O{i}" for i in range(1, 15)})
        completion = course.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEF4-AS\d+\*\* \(required )",
            completion, flags=re.M,
        )[1:]
        self.assertEqual(len(blocks), 7)
        covered = set()
        for number, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF4-AS{number}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            reference = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(reference)
            covered.update(re.findall(r"SEF4-O\d+", reference.group(1)))
        self.assertEqual(covered, outcomes)

    def test_all_eight_modules_reference_stable_outcomes(self):
        course = COURSE.read_text(encoding="utf-8")
        modules = course.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        matches = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertEqual([int(m.group(1)) for m in matches], list(range(1, 9)))
        for i, module in enumerate(matches):
            next_start = matches[i + 1].start() if i + 1 < len(matches) else len(modules)
            block = modules[module.start():next_start]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            refs, lessons = block.split("#### Lessons", 1)
            self.assertRegex(refs, r"(?m)^- SEF4-O\d+")
            numbers = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
            self.assertGreater(len(numbers), 0)

    def test_status_and_program_authority_preserved(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", text)
        self.assertIn("**Duration:** 10 weeks", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF4](SEF4.md)", catalog)
        self.assertIn("SEF1, SEF2, SEF3, SEF4 and SEF10 use", catalog)


if __name__ == "__main__":
    unittest.main()
