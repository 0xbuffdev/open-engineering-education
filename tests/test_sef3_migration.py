"""Guard SEF3's strict OEE v0.2.0 course contract and safety boundaries."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF3.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF3MigrationTests(unittest.TestCase):
    def test_strict_outcome_validator_passes_sef3(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_program_validator_accepts_sef3_with_legacy_courses(self):
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

    def test_fourteen_outcomes_covered_by_seven_required_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        outcomes = set(re.findall(r"(?m)^- \*\*(SEF3-O\d+):\*\*", learning))
        self.assertEqual(
            outcomes, {f"SEF3-O{i}" for i in range(1, 15)}
        )

        completion = text.split("\n## Completion requirements\n", 1)[1]
        assessment_blocks = re.split(
            r"(?=^- \*\*SEF3-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(assessment_blocks), 7)
        covered = set()
        for number, block in enumerate(assessment_blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF3-AS{number}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            references = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(references)
            covered.update(re.findall(r"SEF3-O\d+", references.group(1)))
        self.assertEqual(covered, outcomes)

    def test_all_instructional_modules_have_stable_outcome_references(self):
        text = COURSE.read_text(encoding="utf-8")
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        matches = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(matches)
        # Modules are derived from actual competencies; do not encode a count.
        self.assertEqual(
            [int(match.group(1)) for match in matches],
            list(range(1, len(matches) + 1)),
        )
        mapped_all = set()
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(modules)
            content = modules[match.start():end]
            self.assertEqual(content.count("#### Outcomes"), 1)
            self.assertEqual(content.count("#### Lessons"), 1)
            outcome_segment, lessons = content.split("#### Lessons", 1)
            ids = re.findall(r"(?m)^- (SEF3-O\d+)$", outcome_segment)
            self.assertTrue(ids)
            self.assertEqual(len(ids), len(set(ids)))
            mapped_all.update(ids)
            ordinals = [
                int(number)
                for number in re.findall(r"(?m)^(\d+)\. [^\n]+", lessons)
            ]
            self.assertEqual(ordinals, list(range(1, len(ordinals) + 1)))
            self.assertGreater(len(ordinals), 0)
        self.assertEqual(mapped_all, {f"SEF3-O{i}" for i in range(1, 15)})

    def test_preserved_scope_and_no_legacy_assessment_quotas(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", text)
        self.assertIn("**Duration:** 10–12 weeks", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        self.assertIn("No root privileges", text)
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF3](SEF3.md)", catalog)
        self.assertIn("| 10–12 weeks | SEF2 |", catalog)
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("OEE `v0.2.0` outcome and summative assessment contracts", catalog)


if __name__ == "__main__":
    unittest.main()
