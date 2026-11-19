"""SEC10 enterprise identity assurance and capstone prerequisite coverage."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum/SEC/SEC10.md"
CATALOG = COURSE.parent / "README.md"
CAPSTONE = COURSE.parent / "SEC9.md"


class SEC10CurriculumTests(unittest.TestCase):
    def test_official_validator(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_program_and_capstone_admission(self):
        src = COURSE.read_text(encoding="utf-8")
        cat = CATALOG.read_text(encoding="utf-8")
        cap = CAPSTONE.read_text(encoding="utf-8")
        for x in (
            "# SEC10 — Enterprise Identity & Access Security",
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Prerequisites:** [SEC2](SEC2.md), [SEC4](SEC4.md)",
            "**Duration:** 14–18 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(x, src)
        self.assertIn(
            "| [SEC10](SEC10.md) | Enterprise Identity & Access Security "
            "| 14–18 weeks | SEC2, SEC4 | `course` |", cat)
        self.assertIn(
            "| [SEC9](SEC9.md) | Security Engineering Capstone | "
            "14–18 weeks | SEC1–SEC8, SEC10, SEC11 | `project` |", cat)
        self.assertIn(
            "**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md), "
            "[SEC10](SEC10.md)", cap)
        self.assertIn("ten authentic predecessor decisions", cap)
        self.assertNotIn("legacy", src.lower())

    def test_all_outcomes_taught_and_independently_assessed(self):
        src = COURSE.read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"(?m)^## (.+)$", src)[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        outcome_text = src.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        ids = re.findall(r"(?m)^- \*\*(SEC10-O\d+):\*\*", outcome_text)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        modules = src.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        markers = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(markers)
        self.assertEqual(
            [int(x.group(1)) for x in markers],
            list(range(1, len(markers) + 1)))
        taught = set()
        for i, m in enumerate(markers):
            end = markers[i+1].start() if i+1 < len(markers) else len(modules)
            part = modules[m.start():end]
            self.assertIn("#### Outcomes", part)
            self.assertIn("#### Lessons", part)
            a, b = part.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC10-O\d+)$", a))
            self.assertTrue(refs)
            self.assertTrue(refs <= set(ids))
            taught.update(refs)
            nums = [int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", b)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums)+1)))
        self.assertEqual(taught, set(ids))

        summative = src.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC10-AS\d+\*\* — )", summative, flags=re.M)[1:]
        self.assertTrue(blocks)
        assessed, seen = set(), set()
        for b in blocks:
            name = re.match(r"- \*\*(SEC10-AS\d+)\*\* —", b)
            self.assertIsNotNone(name)
            self.assertNotIn(name.group(1), seen)
            seen.add(name.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(b, rf"(?m)^  - \*\*{field}:\*\* \S")
            row = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", b)
            self.assertIsNotNone(row)
            refs = set(re.findall(r"SEC10-O\d+", row.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= set(ids))
            assessed.update(refs)
        self.assertEqual(assessed, set(ids))

    def test_real_enforcement_and_labeled_external_evidence(self):
        src = COURSE.read_text(encoding="utf-8")
        for x in (
            "real locally running resource",
            "authentic signed test-issuer fixtures",
            "authorization-code/PKCE login",
            "cannot establish that a networked login/redirect occurred",
            "count as actually operating Active Directory",
            "A simulated SCIM-like lifecycle is a *declared subset*",
            "A successful deactivation API response",
            "No paid Microsoft/Google/Okta service",
            "independently observed",
            "Optional lesson investigations",
        ):
            self.assertIn(x, src)
        self.assertNotIn("kind: `test`", src)
        self.assertNotIn("kind: `lab`", src)


if __name__ == "__main__":
    unittest.main()
