"""Regression checks for the SEF5 outcome-driven engineering course."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF5.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF5MigrationTests(unittest.TestCase):
    def test_strict_outcome_checker_passes_course(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_sef_validator_accepts_current_mixed_catalog(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        migrated = sum(
            "**Specification:** `v0.2.0`" in course.read_text(encoding="utf-8")
            for course in COURSE.parent.glob("SEF[0-9]*.md")
        )
        self.assertIn(f"{migrated} v0.2.0, {11 - migrated} legacy", result.stdout)

    def test_fifteen_stable_outcomes_covered_by_seven_required_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        section = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"(?m)^- \*\*(SEF5-O\d+):\*\*", section))
        self.assertEqual(outcomes, {f"SEF5-O{i}" for i in range(1, 16)})
        completion = text.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEF5-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(blocks), 7)
        covered = set()
        for index, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF5-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            references = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(references)
            covered.update(re.findall(r"SEF5-O\d+", references.group(1)))
        self.assertEqual(covered, outcomes)

    def test_modules_have_covered_outcomes_and_sequential_lessons(self):
        text = COURSE.read_text(encoding="utf-8")
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        matches = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(matches)
        # Competency determines the module count, never an old editorial shape.
        self.assertEqual(
            [int(match.group(1)) for match in matches],
            list(range(1, len(matches) + 1)),
        )
        covered = set()
        for i, match in enumerate(matches):
            next_index = matches[i + 1].start() if i + 1 < len(matches) else len(modules)
            chunk = modules[match.start():next_index]
            self.assertEqual(chunk.count("#### Outcomes"), 1)
            self.assertEqual(chunk.count("#### Lessons"), 1)
            outcome_segment, lesson_segment = chunk.split("#### Lessons", 1)
            mapped = re.findall(r"(?m)^- (SEF5-O\d+)$", outcome_segment)
            self.assertTrue(mapped)
            self.assertEqual(len(mapped), len(set(mapped)))
            covered.update(mapped)
            lesson_numbers = [
                int(x) for x in re.findall(r"(?m)^(\d+)\. ", lesson_segment)
            ]
            self.assertTrue(lesson_numbers)
            self.assertEqual(lesson_numbers, list(range(1, len(lesson_numbers) + 1)))
        self.assertEqual(covered, {f"SEF5-O{i}" for i in range(1, 16)})

    def test_version_scope_and_offline_review_boundaries(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", text)
        self.assertIn("**Duration:** 10–12 weeks", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        self.assertIn("No real remote repository", text)
        self.assertIn("independent reproduction", text.lower())
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF5](SEF5.md)", catalog)
        self.assertIn("| 10–12 weeks | SEF2 |", catalog)
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("no historical-format SEF course definitions remain", catalog)


if __name__ == "__main__":
    unittest.main()
