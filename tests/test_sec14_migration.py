"""SEC14 data security and privacy engineering regression contracts."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum/SEC/SEC14.md"
CATALOG = COURSE.parent / "README.md"
CAPSTONE = COURSE.parent / "SEC9.md"
ROOT_CATALOG = ROOT / "curriculum/README.md"


class SEC14Tests(unittest.TestCase):
    def test_official_validator(self):
        p = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)], cwd=ROOT,
            capture_output=True, text=True, check=False)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_program_ownership_and_graduation(self):
        s = COURSE.read_text(encoding="utf-8")
        cat = CATALOG.read_text(encoding="utf-8")
        cap = CAPSTONE.read_text(encoding="utf-8")
        root = ROOT_CATALOG.read_text(encoding="utf-8")
        for v in (
            "# SEC14 — Data Security & Privacy Engineering",
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC5](SEC5.md), [SEC13](SEC13.md)",
            "**Duration:** 14–18 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(v, s)
        self.assertIn(
            "| [SEC14](SEC14.md) | Data Security & Privacy Engineering "
            "| 14–18 weeks | SEC5, SEC13 | `course` |", cat)
        self.assertIn(
            "| [SEC9](SEC9.md) | Security Engineering Capstone | "
            "14–18 weeks | SEC1–SEC8, SEC10, SEC11, SEC12, SEC13, SEC14 "
            "| `project` |", cat)
        self.assertIn(
            "**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md), "
            "[SEC10](SEC10.md), [SEC11](SEC11.md), [SEC12](SEC12.md), "
            "[SEC13](SEC13.md), [SEC14](SEC14.md)", cap)
        self.assertIn("all thirteen predecessor courses", cap)
        self.assertIn("Thirteen-entry predecessor", cap)
        self.assertIn(
            "every required core course from SEC1 through SEC8, SEC10, "
            "SEC11, SEC12, SEC13 and SEC14 before admission to SEC9", cat)
        self.assertIn("| `SEC` | Security Engineering | 14 core |", root)
        self.assertIn("**65 core, 11 electives**", root)
        self.assertNotIn("legacy", s.lower())

    def test_outcomes_taught_and_summatively_assessed(self):
        s = COURSE.read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"(?m)^## (.+)$", s)[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        outcomes = s.split("\n## Learning outcomes\n")[1].split("\n## Modules\n")[0]
        ids = re.findall(r"(?m)^- \*\*(SEC14-O\d+):\*\*", outcomes)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        valid = set(ids)
        modules = s.split("\n## Modules\n")[1].split("\n## Completion requirements\n")[0]
        marks = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(marks)
        taught = set()
        for i, m in enumerate(marks):
            self.assertEqual(int(m.group(1)), i + 1)
            stop = marks[i+1].start() if i+1 < len(marks) else len(modules)
            block = modules[m.start():stop]
            head, lessons = block.split("#### Lessons", 1)
            self.assertIn("#### Outcomes", head)
            mapped = set(re.findall(r"(?m)^- (SEC14-O\d+)$", head))
            self.assertTrue(mapped <= valid)
            taught.update(mapped)
            numbers = [int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers)+1)))
        self.assertEqual(taught, valid)
        completion = s.split("\n## Completion requirements\n")[1]
        blocks = re.split(r"(?=^- \*\*SEC14-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessed, seen = set(), set()
        for b in blocks:
            m = re.match(r"- \*\*(SEC14-AS\d+)\*\* — ", b)
            self.assertIsNotNone(m)
            self.assertNotIn(m.group(1), seen)
            seen.add(m.group(1))
            for f in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(b, rf"(?m)^  - \*\*{f}:\*\* \S")
            row = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", b)
            self.assertIsNotNone(row)
            refs = set(re.findall(r"SEC14-O\d+", row.group(1)))
            self.assertTrue(refs <= valid)
            assessed.update(refs)
        self.assertEqual(assessed, valid)

    def test_executed_data_state_and_honest_disposal_limits(self):
        s = COURSE.read_text(encoding="utf-8").lower()
        for required in (
            "run the local service", "real at-source",
            "genuine prior backup/snapshot", "deliberately restore",
            "real saved bytes", "primary-store", "stale backup",
            "synthetic auxiliary-data join", "nIST sp 800-88 rev. 2",
            "physical sanitization", "not a gdpr",
            "independent technical defense",
        ):
            self.assertIn(required.lower(), s)
        self.assertNotIn("kind: `test`", s)
        self.assertNotIn("kind: `lab`", s)


if __name__ == "__main__":
    unittest.main()
