"""SEC7 threat detection, preservation and response curriculum contracts."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC7.md"
CATALOG = COURSE.parent / "README.md"


class SEC7CurriculumTests(unittest.TestCase):
    def test_official_curriculum_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_and_prerequisite_identity(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith(
            "# SEC7 — Detection, Incident Response & Threat Hunting\n"))
        for expected in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC6](SEC6.md)",
            "**Duration:** 12–16 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(expected, source)
        self.assertIn(
            "| [SEC7](SEC7.md) | Detection, Incident Response & Threat Hunting "
            "| 12–16 weeks | SEC6 | `course` |", catalog)
        prerequisites = re.search(
            r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
        self.assertIsNotNone(prerequisites)
        self.assertEqual(
            prerequisites.group(1), "[SEC6](SEC6.md)")
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_every_outcome_taught_and_assessed_without_quota(self):
        source = COURSE.read_text(encoding="utf-8")
        sections = re.findall(r"(?m)^## (.+)$", source)
        self.assertEqual(
            sections[:4], [
                "Overview", "Learning outcomes", "Modules",
                "Completion requirements"])
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcomes = re.findall(r"(?m)^- \*\*(SEC7-O\d+):\*\*", learning)
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
        for i, marker in enumerate(markers):
            end = markers[i + 1].start() if i + 1 < len(markers) else len(modules)
            block = modules[marker.start():end]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            mapping, lesson_text = block.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC7-O\d+)$", mapping))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            taught.update(refs)
            nums = [
                int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", lesson_text)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums) + 1)))
        self.assertEqual(taught, known)

        completion = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC7-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        seen = set()
        assessed = set()
        for block in blocks:
            head = re.match(r"- \*\*(SEC7-AS\d+)\*\*", block)
            self.assertIsNotNone(head)
            self.assertNotIn(head.group(1), seen)
            seen.add(head.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            line = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(line)
            refs = set(re.findall(r"SEC7-O\d+", line.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(assessed, known)

    def test_real_acquisition_and_qualified_detection_evidence(self):
        source = COURSE.read_text(encoding="utf-8")
        for expected in (
            "actually acquire",
            "A copied log bundle is not a full-disk forensic image",
            "A hash proves equality",
            "NIST SP 800-61 Rev. 3",
            "current MITRE ATT&CK detection-strategy",
            "false alarms",
            "an alert count",
            "independently recompute",
            "Optional lesson investigations",
        ):
            self.assertIn(expected, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
