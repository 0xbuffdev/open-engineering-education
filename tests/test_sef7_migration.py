"""Regressions for the current SEF7 Unix systems outcome contract."""

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

    def test_all_sef_courses_use_current_course_format(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(run.returncode, 0, run.stderr or run.stdout)
        current = sum(
            "**Specification:** `v0.2.0`" in path.read_text(encoding="utf-8")
            for path in COURSE.parent.glob("SEF[0-9]*.md")
        )
        self.assertEqual(current, 11)
        self.assertIn("(OEE v0.2.0)", run.stdout)

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

    def test_competency_modules_own_all_existing_outcomes_without_quota(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        known = set(re.findall(r"(?m)^- \*\*(SEF7-O\d+):\*\*", learning))
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        heads = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(heads)
        self.assertEqual(
            [int(m.group(1)) for m in heads],
            list(range(1, len(heads) + 1)),
        )
        covered = set()
        for index, head in enumerate(heads):
            end = heads[index + 1].start() if index + 1 < len(heads) else len(modules)
            section = modules[head.start():end]
            self.assertEqual(section.count("#### Outcomes"), 1)
            self.assertEqual(section.count("#### Lessons"), 1)
            mapping, lessons = section.split("#### Lessons", 1)
            refs = re.findall(r"(?m)^- (SEF7-O\d+)$", mapping)
            self.assertTrue(refs)
            self.assertEqual(len(refs), len(set(refs)))
            self.assertTrue(set(refs).issubset(known))
            covered.update(refs)
            indexes = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(indexes)
            self.assertEqual(indexes, list(range(1, len(indexes) + 1)))
        self.assertEqual(covered, known)

    def test_course_identity_and_system_boundaries_are_preserved(self):
        course = COURSE.read_text(encoding="utf-8")
        self.assertIn(
            "**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)", course
        )
        self.assertIn("**Duration:** 12–16 weeks", course)
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
        self.assertIn("| 12–16 weeks | SEF3, SEF6 |", catalog)
        self.assertIn("SEF7 remains responsible for its own assessed outcomes", catalog)
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("OEE `v0.2.0` outcome and summative assessment contracts", catalog)

if __name__ == "__main__":
    unittest.main()
