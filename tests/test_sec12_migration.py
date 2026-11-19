"""SEC12 vulnerability and exposure management: assessed competence and graduation."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum/SEC/SEC12.md"
CATALOG = COURSE.parent / "README.md"
CAPSTONE = COURSE.parent / "SEC9.md"
OVERVIEW = ROOT / "curriculum/README.md"


class SEC12CurriculumTests(unittest.TestCase):
    def test_official_curriculum_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)], cwd=ROOT,
            capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_course_identity_and_graduation(self):
        src, cat = COURSE.read_text(encoding="utf-8"), CATALOG.read_text(encoding="utf-8")
        cap, root = CAPSTONE.read_text(encoding="utf-8"), OVERVIEW.read_text(encoding="utf-8")
        for item in (
            "# SEC12 — Vulnerability & Exposure Management",
            "**Program:** SEC — Security Engineering", "**Type:** `course`",
            "**Prerequisites:** [SEC11](SEC11.md)", "**Duration:** 12–16 weeks",
            "**Status:** `draft`", "**Specification:** `v0.2.0`",
        ):
            self.assertIn(item, src)
        self.assertIn(
            "| [SEC12](SEC12.md) | Vulnerability & Exposure Management "
            "| 12–16 weeks | SEC11 | `course` |", cat)
        self.assertIn(
            "| [SEC9](SEC9.md) | Security Engineering Capstone | "
            "14–18 weeks | SEC1–SEC8, SEC10, SEC11, SEC12, SEC13, SEC14 | `project` |", cat)
        self.assertIn(
            "**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md), "
            "[SEC10](SEC10.md), [SEC11](SEC11.md), [SEC12](SEC12.md), "
            "[SEC13](SEC13.md)",
            cap)
        self.assertIn("Thirteen-entry predecessor", cap)
        self.assertIn("thirteen authentic predecessor decisions", cap)
        self.assertIn("every required core course from SEC1 through SEC8, "
                      "SEC10, SEC11, SEC12, SEC13 and SEC14", cat)
        self.assertIn("| `SEC` | Security Engineering | 14 core |", root)
        self.assertIn("**58 core, 7 electives**", root)
        self.assertNotIn("legacy", src.lower())

    def test_no_redundant_direct_predecessor(self):
        src = COURSE.read_text(encoding="utf-8")
        sec11 = (COURSE.parent / "SEC11.md").read_text(encoding="utf-8")
        sec7 = (COURSE.parent / "SEC7.md").read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEC11](SEC11.md)", src)
        self.assertIn(
            "**Prerequisites:** [SEC7](SEC7.md), [SEC10](SEC10.md)", sec11)
        self.assertIn(
            "**Prerequisites:** [SEC4](SEC4.md), [SEC6](SEC6.md)", sec7)

    def test_outcome_instruction_and_assessment_coverage(self):
        src = COURSE.read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"(?m)^## (.+)$", src)[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        learning = src.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        ids = re.findall(r"(?m)^- \*\*(SEC12-O\d+):\*\*", learning)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        known = set(ids)
        modules = src.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        heads = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(heads)
        self.assertEqual([int(h.group(1)) for h in heads],
                         list(range(1, len(heads)+1)))
        taught = set()
        for i, head in enumerate(heads):
            stop = heads[i+1].start() if i+1 < len(heads) else len(modules)
            block = modules[head.start():stop]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            outcomes, lessons = block.split("#### Lessons", 1)
            mapped = set(re.findall(r"(?m)^- (SEC12-O\d+)$", outcomes))
            self.assertTrue(mapped)
            self.assertTrue(mapped <= known)
            taught.update(mapped)
            nums = [int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", lessons)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums)+1)))
        self.assertEqual(taught, known)
        summative = src.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(r"(?=^- \*\*SEC12-AS\d+\*\* — )",
                          summative, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessed, seen = set(), set()
        for block in blocks:
            match = re.match(r"- \*\*(SEC12-AS\d+)\*\* — ", block)
            self.assertIsNotNone(match)
            self.assertNotIn(match.group(1), seen)
            seen.add(match.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            mapping = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(mapping)
            refs = set(re.findall(r"SEC12-O\d+", mapping.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(assessed, known)

    def test_true_remediation_and_threat_signal_boundaries(self):
        src = COURSE.read_text(encoding="utf-8")
        for item in (
            "actually loaded/running", "genuine locally enforced corrective change",
            "false positives", "backported distribution packages",
            "CISA KEV", "FIRST EPSS", "next 30 days",
            "not automatically binding on every organization", "VEX",
            "SSVC-style", "safe known-vulnerable regression",
            "individual recorded/written/live technical defense",
        ):
            self.assertIn(item, src)
        self.assertNotIn("kind: `test`", src)
        self.assertNotIn("kind: `lab`", src)


if __name__ == "__main__":
    unittest.main()
