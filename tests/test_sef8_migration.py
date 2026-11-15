"""Regression checks for the SEF8 mathematical foundations v0.2.0 migration."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF8.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF8MigrationTests(unittest.TestCase):
    def test_strict_outcome_validator_accepts_mathematics_course(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_program_validation_accepts_remaining_legacy_sef9(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        migrated = sum(
            "**Specification:** `v0.2.0`" in path.read_text(encoding="utf-8")
            for path in COURSE.parent.glob("SEF[0-9]*.md")
        )
        self.assertIn(
            f"{migrated} v0.2.0, {10 - migrated} legacy", result.stdout
        )

    def test_eighteen_outcomes_covered_by_eight_summative_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"(?m)^- \*\*(SEF8-O\d+):\*\*", learning))
        self.assertEqual(outcomes, {f"SEF8-O{i}" for i in range(1, 19)})

        completion = text.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEF8-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(blocks), 8)
        covered = set()
        for index, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF8-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            refs = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(refs)
            used = set(re.findall(r"SEF8-O\d+", refs.group(1)))
            self.assertTrue(used)
            self.assertTrue(used.issubset(outcomes))
            covered.update(used)
        self.assertEqual(covered, outcomes)

    def test_ten_ordered_modules_with_mapped_outcomes_and_lessons(self):
        text = COURSE.read_text(encoding="utf-8")
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        headers = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertEqual([int(m.group(1)) for m in headers], list(range(1, 11)))
        for index, match in enumerate(headers):
            stop = headers[index + 1].start() if index + 1 < len(headers) else len(modules)
            block = modules[match.start():stop]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            mapped, lessons = block.split("#### Lessons", 1)
            self.assertRegex(mapped, r"(?m)^- SEF8-O\d+")
            ordinals = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(ordinals)
            self.assertEqual(ordinals, list(range(1, len(ordinals) + 1)))

    def test_ungraded_bridge_and_mathematical_accessibility_retained(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", text)
        self.assertIn("**Duration:** 11–12 weeks", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertIn("**ungraded entry diagnostic**", text)
        self.assertIn("no fixed number of attempts", text.lower())
        self.assertIn("No prior", text.replace("There is no prerequisite", "No prior"))
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        self.assertIn("NumPy", text)
        self.assertIn("independent reviewer", text.lower())
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF8](SEF8.md)", catalog)
        self.assertIn("All ten SEF courses (SEF1–SEF10)", catalog)
        self.assertIn("SEF8", catalog)


if __name__ == "__main__":
    unittest.main()
