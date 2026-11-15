"""Regressions for the SEF7 Unix system interfaces v0.2.0 migration."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF7.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF7MigrationTests(unittest.TestCase):
    def test_strict_outcome_validator_accepts_course(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr or run.stdout)

    def test_mixed_sef_catalog_validator_reports_actual_maturity(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr or run.stdout)
        migrated = sum(
            "**Specification:** `v0.2.0`" in path.read_text(encoding="utf-8")
            for path in COURSE.parent.glob("SEF[0-9]*.md")
        )
        self.assertIn(f"{migrated} v0.2.0, {10 - migrated} legacy", run.stdout)

    def test_all_fourteen_outcomes_map_to_seven_required_assessments(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        defined = set(re.findall(r"(?m)^- \*\*(SEF7-O\d+):\*\*", learning))
        self.assertEqual(defined, {f"SEF7-O{i}" for i in range(1, 15)})
        completion = text.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEF7-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(blocks), 7)
        covered = set()
        for index, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF7-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            match = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(match)
            refs = set(re.findall(r"SEF7-O\d+", match.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs.issubset(defined))
            covered.update(refs)
        self.assertEqual(covered, defined)

    def test_eight_modules_have_stable_outcomes_and_ordered_lessons(self):
        text = COURSE.read_text(encoding="utf-8")
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        headings = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertEqual([int(m.group(1)) for m in headings], list(range(1, 9)))
        for index, heading in enumerate(headings):
            stop = headings[index + 1].start() if index + 1 < len(headings) else len(modules)
            body = modules[heading.start():stop]
            self.assertEqual(body.count("#### Outcomes"), 1)
            self.assertEqual(body.count("#### Lessons"), 1)
            mapped, lessons = body.split("#### Lessons", 1)
            self.assertRegex(mapped, r"(?m)^- SEF7-O\d+")
            indexes = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(indexes)
            self.assertEqual(indexes, list(range(1, len(indexes) + 1)))

    def test_course_identity_and_system_boundaries_are_preserved(self):
        course = COURSE.read_text(encoding="utf-8")
        self.assertIn(
            "**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)", course
        )
        self.assertIn("**Duration:** 7 weeks", course)
        self.assertIn("**Status:** `draft`", course)
        self.assertIn("**Specification:** `v0.2.0`", course)
        self.assertNotIn("— `test`", course)
        self.assertNotIn("— `lab`", course)
        self.assertNotIn("Final integration lab — required", course)
        for term in ("EINTR", "FD_CLOEXEC", "waitpid", "lstat", "SIGPIPE",
                     "poll", "127.0.0.1", "independent reviewer"):
            self.assertIn(term.lower(), course.lower())
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("[SEF7](SEF7.md)", catalog)
        self.assertIn("SEF1, SEF2, SEF3, SEF4, SEF5, SEF6, SEF7 and SEF10 use", catalog)


if __name__ == "__main__":
    unittest.main()
