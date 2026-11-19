"""SEC4 public metadata, learning outcomes, scope, and summative evidence checks."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC4.md"
CATALOG = COURSE.parent / "README.md"


class SEC4MigrationTests(unittest.TestCase):
    def test_official_outcome_curriculum_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_source_and_catalog_identity(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith("# SEC4 — Network & Infrastructure Security\n"))
        for expected in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
            "**Duration:** 10–14 weeks",
            "**Prerequisites:** [SEC2](SEC2.md)",
        ):
            self.assertIn(expected, source)
        self.assertIn(
            "| [SEC4](SEC4.md) | Network & Infrastructure Security "
            "| 10–14 weeks | SEC2 | `course` |", catalog)
        prereq = re.search(r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
        self.assertIsNotNone(prereq)
        self.assertNotIn("SYS4", prereq.group(1))
        self.assertNotIn("APP7", prereq.group(1))
        self.assertNotIn("SEC5", prereq.group(1))
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_all_outcomes_taught_and_assessed(self):
        source = COURSE.read_text(encoding="utf-8")
        heads = re.findall(r"(?m)^## (.+)$", source)
        self.assertEqual(
            heads[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcome_ids = re.findall(r"(?m)^- \*\*(SEC4-O\d+):\*\*", learning)
        self.assertTrue(outcome_ids)
        self.assertEqual(len(outcome_ids), len(set(outcome_ids)))
        known = set(outcome_ids)
        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        markers = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(markers)
        self.assertEqual(
            [int(m.group(1)) for m in markers],
            list(range(1, len(markers) + 1)))
        taught = set()
        for index, marker in enumerate(markers):
            end = markers[index + 1].start() if index + 1 < len(markers) else len(modules)
            block = modules[marker.start():end]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            target_block, lesson_block = block.split("#### Lessons", 1)
            references = set(re.findall(r"(?m)^- (SEC4-O\d+)$", target_block))
            self.assertTrue(references)
            self.assertTrue(references <= known)
            taught.update(references)
            numbers = [
                int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", lesson_block)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
        self.assertEqual(taught, known)

        completion = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC4-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessment_ids = []
        assessed = set()
        for block in blocks:
            match = re.match(r"- \*\*(SEC4-AS\d+)\*\*", block)
            self.assertIsNotNone(match)
            assessment_ids.append(match.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            mapping = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(mapping)
            references = set(re.findall(r"SEC4-O\d+", mapping.group(1)))
            self.assertTrue(references)
            self.assertTrue(references <= known)
            assessed.update(references)
        self.assertEqual(len(assessment_ids), len(set(assessment_ids)))
        self.assertEqual(assessed, known)

    def test_safety_and_enforcement_provenance(self):
        source = COURSE.read_text(encoding="utf-8")
        for needle in (
            "no root access",
            "Never scan external ranges",
            "loopback addresses by themselves",
            "not prove system-wide firewalling",
            "Never globally disable certificate checking",
            "independently verified",
            "Optional module investigations",
        ):
            self.assertIn(needle, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
