"""Regression tests for SEF8 numerical mathematics after RFC 0003."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF8.md"
CATALOG = COURSE.parent / "README.md"


class SEF8MigrationTests(unittest.TestCase):
    def test_outcome_and_program_validators_accept_sef8(self):
        for cmd in (
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
        ):
            with self.subTest(cmd=cmd):
                result = subprocess.run(cmd, cwd=ROOT, capture_output=True,
                                        text=True, check=False)
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("11 v0.2.0, 0 legacy", result.stdout)

    def test_retained_and_new_outcomes_have_six_required_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        defined = set(re.findall(r"(?m)^- \*\*(SEF8-O\d+):\*\*", learning))
        expected = {f"SEF8-O{i}" for i in
                    (3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20)}
        self.assertEqual(defined, expected)
        completion = text.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(r"(?=^- \*\*SEF8-AS\d+\*\* \(required )",
                          completion, flags=re.M)[1:]
        ids = [re.match(r"- \*\*(SEF8-AS\d+)\*\*", b).group(1) for b in blocks]
        self.assertEqual(ids, ["SEF8-AS3", "SEF8-AS4", "SEF8-AS6",
                               "SEF8-AS9", "SEF8-AS7", "SEF8-AS10"])
        covered = set()
        for block in blocks:
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            refs = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(refs)
            claims = set(re.findall(r"SEF8-O\d+", refs.group(1)))
            self.assertTrue(claims.issubset(defined))
            covered.update(claims)
        self.assertEqual(covered, expected)

    def test_eight_modules_are_ordered_and_mapped(self):
        text = COURSE.read_text(encoding="utf-8")
        block = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        heads = list(re.finditer(r"(?m)^### Module (\d+) — ", block))
        self.assertEqual([int(m.group(1)) for m in heads], list(range(1, 9)))
        for index, header in enumerate(heads):
            end = heads[index + 1].start() if index + 1 < len(heads) else len(block)
            module = block[header.start():end]
            mapped, lessons = module.split("#### Lessons", 1)
            self.assertIn("#### Outcomes", mapped)
            self.assertRegex(mapped, r"(?m)^- SEF8-O\d+")
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

    def test_numerical_course_has_explicit_readiness_and_revision_contract(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF11](SEF11.md)", text)
        self.assertIn("**Duration:** 12–14 weeks", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertIn("**Status:** `draft`", text)
        for keyword in ("logarithm", "limit", "integral", "gradient", "NumPy",
                        "independent", "finite", "probability", "statistical"):
            self.assertIn(keyword.lower(), text.lower())
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF8](SEF8.md)", catalog)
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("**SEF11 is the prerequisite**", text)
        self.assertIn("intentionally nonconsecutive", text)
        self.assertNotIn("MATH-MIGRATION.md", text)
        self.assertNotIn("migration table", text.lower())


if __name__ == "__main__":
    unittest.main()
