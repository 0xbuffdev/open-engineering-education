"""Regression tests for SEF6 C and memory ownership."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF6.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF6CurriculumTests(unittest.TestCase):
    def test_strict_outcome_validator_accepts_course(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)

    def test_sef_program_validator_accepts_current_course(self):
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)
        current = sum(
            "**Specification:** `v0.2.0`" in p.read_text(encoding="utf-8")
            for p in COURSE.parent.glob("SEF[0-9]*.md")
        )
        self.assertEqual(current, 11)
        self.assertIn("(OEE v0.2.0)", completed.stdout)

    def test_all_sixteen_outcomes_have_required_assessment_coverage(self):
        course = COURSE.read_text(encoding="utf-8")
        learning = course.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"(?m)^- \*\*(SEF6-O\d+):\*\*", learning))
        self.assertEqual(outcomes, {f"SEF6-O{i}" for i in range(1, 17)})
        completion = course.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEF6-AS\d+\*\* \(required )", completion, flags=re.M,
        )[1:]
        self.assertEqual(len(blocks), 7)
        covered = set()
        for index, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF6-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            refs = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(refs)
            covered.update(re.findall(r"SEF6-O\d+", refs.group(1)))
        self.assertEqual(covered, outcomes)

    def test_modules_have_real_outcome_ownership_not_fixed_counts(self):
        course = COURSE.read_text(encoding="utf-8")
        learning = course.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        known = set(re.findall(r"(?m)^- \*\*(SEF6-O\d+):\*\*", learning))
        modules = course.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        headers = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(headers)
        self.assertEqual(
            [int(header.group(1)) for header in headers],
            list(range(1, len(headers) + 1)),
        )
        covered = set()
        for index, header in enumerate(headers):
            end = headers[index + 1].start() if index + 1 < len(headers) else len(modules)
            block = modules[header.start():end]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            module_refs, lessons = block.split("#### Lessons", 1)
            refs = re.findall(r"(?m)^- (SEF6-O\d+)$", module_refs)
            self.assertTrue(refs)
            self.assertEqual(len(refs), len(set(refs)))
            self.assertTrue(set(refs).issubset(known))
            covered.update(refs)
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
        self.assertEqual(covered, known)

    def test_source_authority_and_memory_safety_contract_retained(self):
        course = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF3](SEF3.md), [SEF4](SEF4.md), [SEF5](SEF5.md)", course)
        self.assertIn("**Duration:** 14–18 weeks", course)
        self.assertIn("**Status:** `draft`", course)
        self.assertIn("**Specification:** `v0.2.0`", course)
        self.assertNotIn("— `test`", course)
        self.assertNotIn("— `lab`", course)
        self.assertNotIn("Final integration lab — required", course)
        for term in ("CHAR_BIT", "realloc", "allocation failure", "one-past",
                     "undefined behavior", "independent reviewer"):
            self.assertIn(term.lower(), course.lower())
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF6](SEF6.md)", catalog)
        self.assertIn("| 14–18 weeks | SEF3, SEF4, SEF5 |", catalog)
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("OEE `v0.2.0` outcome and summative assessment contracts", catalog)


if __name__ == "__main__":
    unittest.main()
