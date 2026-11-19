"""SEC11 endpoint/platform security evidence and graduation prerequisites."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC11.md"
CATALOG = COURSE.parent / "README.md"
CAPSTONE = COURSE.parent / "SEC9.md"
UMBRELLA = ROOT / "curriculum" / "README.md"


class SEC11CurriculumTests(unittest.TestCase):
    def test_official_outcome_curriculum_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_course_catalog_and_graduation_contract(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        capstone = CAPSTONE.read_text(encoding="utf-8")
        umbrella = UMBRELLA.read_text(encoding="utf-8")
        for line in (
            "# SEC11 — Endpoint & Platform Defense",
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC7](SEC7.md), [SEC10](SEC10.md)",
            "**Duration:** 14–18 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(line, source)
        self.assertIn(
            "| [SEC11](SEC11.md) | Endpoint & Platform Defense "
            "| 14–18 weeks | SEC7, SEC10 | `course` |", catalog)
        self.assertIn(
            "| [SEC9](SEC9.md) | Security Engineering Capstone "
            "| 14–18 weeks | SEC1–SEC8, SEC10, SEC11, SEC12, SEC13, SEC14 | `project` |", catalog)
        self.assertIn(
            "**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md), "
            "[SEC10](SEC10.md), [SEC11](SEC11.md), [SEC12](SEC12.md), "
            "[SEC13](SEC13.md)", capstone)
        self.assertIn("Thirteen-entry predecessor", capstone)
        self.assertIn("thirteen authentic predecessor decisions", capstone)
        self.assertIn(
            "from SEC1 through SEC8, SEC10, SEC11, SEC12, SEC13 and SEC14 before admission to SEC9",
            catalog,
        )
        self.assertIn("| `SEC` | Security Engineering | 14 core |", umbrella)
        self.assertIn("**65 core, 11 electives**", umbrella)
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_all_outcomes_have_instruction_and_required_assessment_evidence(self):
        source = COURSE.read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"(?m)^## (.+)$", source)[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcomes = re.findall(r"(?m)^- \*\*(SEC11-O\d+):\*\*", learning)
        self.assertTrue(outcomes)
        self.assertEqual(len(outcomes), len(set(outcomes)))
        known = set(outcomes)

        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        starts = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(starts)
        self.assertEqual(
            [int(x.group(1)) for x in starts],
            list(range(1, len(starts) + 1)))
        taught = set()
        for index, match in enumerate(starts):
            end = (starts[index+1].start()
                   if index+1 < len(starts) else len(modules))
            block = modules[match.start():end]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            refs, lesson_text = block.split("#### Lessons", 1)
            mapped = set(re.findall(r"(?m)^- (SEC11-O\d+)$", refs))
            self.assertTrue(mapped)
            self.assertTrue(mapped <= known)
            taught.update(mapped)
            lesson_nums = [int(x) for x in re.findall(
                r"(?m)^(\d+)\. \*\*", lesson_text)]
            self.assertTrue(lesson_nums)
            self.assertEqual(
                lesson_nums, list(range(1, len(lesson_nums) + 1)))
        self.assertEqual(taught, known)

        completion = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC11-AS\d+\*\* — )",
            completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessed, seen = set(), set()
        for block in blocks:
            assessment = re.match(r"- \*\*(SEC11-AS\d+)\*\* —", block)
            self.assertIsNotNone(assessment)
            self.assertNotIn(assessment.group(1), seen)
            seen.add(assessment.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            mapping = re.search(
                r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(mapping)
            refs = set(re.findall(r"SEC11-O\d+", mapping.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(assessed, known)

    def test_real_linux_enforcement_without_false_windows_qualification(self):
        source = COURSE.read_text(encoding="utf-8")
        for claim in (
            "real operating-system enforcement",
            "genuine kernel-enforced denial",
            "actual kernel-enforced",
            "authentic Windows Event 4688",
            "audit mode",
            "A supplied trace does not establish hands-on Windows administration",
            "App Control for Business",
            "real local Linux",
            "Windows administration cannot be certified from trace-only work",
            "Optional formative feedback",
            "legitimately licensed Windows",
        ):
            self.assertIn(claim, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
