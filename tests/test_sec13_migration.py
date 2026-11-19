"""SEC13 professional system architecture and independent assurance guards."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum/SEC/SEC13.md"
CATALOG = COURSE.parent / "README.md"
CAPSTONE = COURSE.parent / "SEC9.md"
OVERVIEW = ROOT / "curriculum/README.md"


class SEC13Tests(unittest.TestCase):
    def test_outcome_curriculum_validator(self):
        run = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)], cwd=ROOT,
            capture_output=True, text=True, check=False)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_metadata_catalog_and_capstone(self):
        src = COURSE.read_text(encoding="utf-8")
        cat = CATALOG.read_text(encoding="utf-8")
        cap = CAPSTONE.read_text(encoding="utf-8")
        root = OVERVIEW.read_text(encoding="utf-8")
        for required in (
            "# SEC13 — Security Architecture & Control Assurance",
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC6](SEC6.md), [SEC10](SEC10.md)",
            "**Duration:** 14–18 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(required, src)
        self.assertIn(
            "| [SEC13](SEC13.md) | Security Architecture & Control Assurance "
            "| 14–18 weeks | SEC6, SEC10 | `course` |", cat)
        self.assertIn(
            "| [SEC9](SEC9.md) | Security Engineering Capstone "
            "| 14–18 weeks | SEC1–SEC8, SEC10, SEC11, SEC12, SEC13 "
            "| `project` |", cat)
        self.assertIn(
            "**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md), "
            "[SEC10](SEC10.md), [SEC11](SEC11.md), "
            "[SEC12](SEC12.md), [SEC13](SEC13.md)", cap)
        self.assertIn("all twelve predecessor courses", cap)
        self.assertIn("Twelve-entry predecessor", cap)
        self.assertIn("from SEC1 through SEC8, SEC10, SEC11, "
                      "SEC12 and SEC13 before admission to SEC9", cat)
        self.assertIn("| `SEC` | Security Engineering | 13 core |", root)
        self.assertIn("**57 core, 7 electives**", root)
        self.assertNotIn("legacy", src.lower())

    def test_all_outcomes_taught_and_assessed(self):
        src = COURSE.read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"(?m)^## (.+)$", src)[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        learning = src.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        ids = re.findall(r"(?m)^- \*\*(SEC13-O\d+):\*\*", learning)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        modules = src.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        marks = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(marks)
        self.assertEqual([int(x.group(1)) for x in marks],
                         list(range(1, len(marks)+1)))
        taught = set()
        for i, mark in enumerate(marks):
            stop = marks[i+1].start() if i+1 < len(marks) else len(modules)
            part = modules[mark.start():stop]
            a, b = part.split("#### Lessons", 1)
            self.assertIn("#### Outcomes", a)
            taught.update(re.findall(r"(?m)^- (SEC13-O\d+)$", a))
            nums = [int(n) for n in re.findall(r"(?m)^(\d+)\. \*\*", b)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums)+1)))
        self.assertEqual(taught, set(ids))
        summative = src.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(r"(?=^- \*\*SEC13-AS\d+\*\* — )",
                          summative, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessed = set()
        for block in blocks:
            self.assertRegex(block, r"^- \*\*SEC13-AS\d+\*\* — ")
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            mapping = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(mapping)
            assessed.update(re.findall(r"SEC13-O\d+", mapping.group(1)))
        self.assertEqual(assessed, set(ids))

    def test_real_cross_component_enforcement_and_evidence_honesty(self):
        src = COURSE.read_text(encoding="utf-8").lower()
        for required in (
            "real protected state",
            "genuinely distinct process/trust authorities",
            "actually executed controls",
            "source-inspectable api",
            "independent state tests",
            "safe reintroduced flaw",
            "genuine inter-component trust boundary",
            "unavailable permission decision",
            "claim/argument/evidence",
            "nist sp 800-53a rev. 5",
            "risk-owner",
            "independent reviewer",
            "unsupported platform mechanisms",
        ):
            self.assertIn(required, src)
        self.assertNotIn("kind: `test`", src)
        self.assertNotIn("kind: `lab`", src)


if __name__ == "__main__":
    unittest.main()
