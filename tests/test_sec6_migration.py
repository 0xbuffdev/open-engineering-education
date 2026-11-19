"""SEC6 outcome/evidence contracts; no artificial module-count or lesson quotas."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC6.md"
CATALOG = COURSE.parent / "README.md"


class SEC6MigrationTests(unittest.TestCase):
    def test_official_curriculum_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_and_direct_prerequisites(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith(
            "# SEC6 — Cloud, Containers & Identity Security\n"))
        for field in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC2](SEC2.md), [SEC4](SEC4.md), "
            "[APP7](../APP/APP7.md)",
            "**Duration:** 14–18 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(field, source)
        self.assertIn(
            "| [SEC6](SEC6.md) | Cloud, Containers & Identity Security "
            "| 14–18 weeks | SEC2, SEC4, APP7 | `course` |", catalog)
        line = re.search(r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
        self.assertIsNotNone(line)
        self.assertNotIn("SEC5", line.group(1))
        self.assertNotIn("SEC7", line.group(1))
        self.assertNotIn("SYS4", line.group(1))
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_every_outcome_taught_and_assessed(self):
        source = COURSE.read_text(encoding="utf-8")
        headings = re.findall(r"(?m)^## (.+)$", source)
        self.assertEqual(
            headings[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        outcomes = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        ids = re.findall(r"(?m)^- \*\*(SEC6-O\d+):\*\*", outcomes)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        known = set(ids)
        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        starts = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(starts)
        self.assertEqual(
            [int(m.group(1)) for m in starts],
            list(range(1, len(starts) + 1)))
        taught = set()
        for i, head in enumerate(starts):
            end = starts[i + 1].start() if i + 1 < len(starts) else len(modules)
            block = modules[head.start():end]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            labels, sequence = block.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC6-O\d+)$", labels))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            taught.update(refs)
            order = [int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", sequence)]
            self.assertTrue(order)
            self.assertEqual(order, list(range(1, len(order) + 1)))
        self.assertEqual(taught, known)

        completion = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC6-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        seen = set()
        assessed = set()
        for block in blocks:
            match = re.match(r"- \*\*(SEC6-AS\d+)\*\*", block)
            self.assertIsNotNone(match)
            self.assertNotIn(match.group(1), seen)
            seen.add(match.group(1))
            for name in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{name}:\*\* \S")
            values = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(values)
            refs = set(re.findall(r"SEC6-O\d+", values.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(assessed, known)

    def test_real_enforcement_and_provenance_claims(self):
        source = COURSE.read_text(encoding="utf-8")
        for phrase in (
            "real local container authority restriction",
            "not be claimed as proof of live container isolation",
            "A valid signature by the wrong identity is a failure",
            "SLSA v1.2 Source and Build tracks",
            "No public cloud account",
            "Never target a real cloud tenant",
            "Optional lesson investigations",
            "actual enforcement point",
        ):
            self.assertIn(phrase, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
