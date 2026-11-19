"""SEC8 competency, current prerequisite, actual control-evidence and safety checks."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC8.md"
CATALOG = COURSE.parent / "README.md"


class SEC8MigrationTests(unittest.TestCase):
    def test_official_curriculum_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_course_identity_and_prerequisite(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith(
            "# SEC8 — AI Security & Authorized Red Teaming\n"))
        for line in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC7](SEC7.md)",
            "**Duration:** 12–16 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(line, source)
        self.assertIn(
            "| [SEC8](SEC8.md) | AI Security & Authorized Red Teaming "
            "| 12–16 weeks | SEC7 | `course` |", catalog)
        direct = re.search(r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
        self.assertIsNotNone(direct)
        self.assertEqual(direct.group(1), "[SEC7](SEC7.md)")
        self.assertNotIn("AI5", direct.group(1))
        self.assertNotIn("AI11", direct.group(1))
        self.assertNotIn("AI12", direct.group(1))
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_outcomes_have_coherent_instruction_and_assessment(self):
        source = COURSE.read_text(encoding="utf-8")
        headings = re.findall(r"(?m)^## (.+)$", source)
        self.assertEqual(headings[:4], [
            "Overview", "Learning outcomes", "Modules", "Completion requirements"])
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcomes = re.findall(r"(?m)^- \*\*(SEC8-O\d+):\*\*", learning)
        self.assertTrue(outcomes)
        self.assertEqual(len(outcomes), len(set(outcomes)))
        known = set(outcomes)

        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        markers = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(markers)
        self.assertEqual(
            [int(x.group(1)) for x in markers],
            list(range(1, len(markers) + 1)))
        taught = set()
        for i, start in enumerate(markers):
            stop = markers[i + 1].start() if i + 1 < len(markers) else len(modules)
            block = modules[start.start():stop]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            map_text, lesson_text = block.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC8-O\d+)$", map_text))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            taught.update(refs)
            nums = [int(x) for x in re.findall(
                r"(?m)^(\d+)\. \*\*", lesson_text)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums) + 1)))
        self.assertEqual(taught, known)

        summative = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(r"(?=^- \*\*SEC8-AS\d+\*\* — )",
                          summative, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessed = set()
        seen = set()
        for block in blocks:
            head = re.match(r"- \*\*(SEC8-AS\d+)\*\*", block)
            self.assertIsNotNone(head)
            self.assertNotIn(head.group(1), seen)
            seen.add(head.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            line = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(line)
            refs = set(re.findall(r"SEC8-O\d+", line.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(assessed, known)

    def test_ai_evidence_and_authorization_limits(self):
        source = COURSE.read_text(encoding="utf-8")
        for phrase in (
            "actual model-mediated response or tool proposal",
            "A hard-coded fake text generator",
            "actual protected-state transition",
            "No third-party target",
            "Optional lesson investigations",
            "OWASP Top 10 for LLM Applications 2026",
            "user's permissions",
            "refuses every request",
        ):
            self.assertIn(phrase, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
