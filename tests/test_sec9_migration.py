"""SEC9 graduation admission, project contract and summative evidence checks."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC9.md"
CATALOG = COURSE.parent / "README.md"


class SEC9MigrationTests(unittest.TestCase):
    def test_official_outcome_curriculum_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_project_identity_and_catalog_graduation_contract(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith("# SEC9 — Security Engineering Capstone\n"))
        for line in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `project`",
            "**Prerequisites:** [SEC1](SEC1.md)–[SEC8](SEC8.md)",
            "**Duration:** 14–18 weeks",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
        ):
            self.assertIn(line, source)
        self.assertIn(
            "| [SEC9](SEC9.md) | Security Engineering Capstone "
            "| 14–18 weeks | SEC1–SEC8 | `project` |", catalog)
        for expected in (
            "verified assessed completion of every required course "
            "from SEC1 through SEC8",
            "before admission to SEC9",
            "individual technical defense",
            "A completed capstone does not replace missing prerequisite mastery",
        ):
            self.assertIn(expected, catalog)
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_all_outcomes_taught_and_summatively_evaluated(self):
        source = COURSE.read_text(encoding="utf-8")
        heads = re.findall(r"(?m)^## (.+)$", source)
        self.assertEqual(heads[:4], [
            "Overview", "Learning outcomes", "Modules", "Completion requirements"])
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        ids = re.findall(r"(?m)^- \*\*(SEC9-O\d+):\*\*", learning)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        valid = set(ids)

        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        starts = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(starts)
        self.assertEqual(
            [int(x.group(1)) for x in starts],
            list(range(1, len(starts) + 1)))
        taught = set()
        for index, m in enumerate(starts):
            last = starts[index + 1].start() if index + 1 < len(starts) else len(modules)
            part = modules[m.start():last]
            self.assertIn("#### Outcomes", part)
            self.assertIn("#### Lessons", part)
            refs, lessons = part.split("#### Lessons", 1)
            mappings = set(re.findall(r"(?m)^- (SEC9-O\d+)$", refs))
            self.assertTrue(mappings)
            self.assertTrue(mappings <= valid)
            taught.update(mappings)
            numbers = [int(x) for x in re.findall(
                r"(?m)^(\d+)\. \*\*", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
        self.assertEqual(taught, valid)

        required = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC9-AS\d+\*\* — )", required, flags=re.M)[1:]
        self.assertTrue(blocks)
        seen = set()
        assessed = set()
        for block in blocks:
            head = re.match(r"- \*\*(SEC9-AS\d+)\*\*", block)
            self.assertIsNotNone(head)
            self.assertNotIn(head.group(1), seen)
            seen.add(head.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            mapping = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(mapping)
            refs = set(re.findall(r"SEC9-O\d+", mapping.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= valid)
            assessed.update(refs)
        self.assertEqual(assessed, valid)

    def test_reviewer_admission_technical_defense_and_real_implementation(self):
        source = COURSE.read_text(encoding="utf-8")
        for phrase in (
            "every one of SEC1–SEC8",
            "SEC3 and SEC5 separately",
            "Before admission",
            "one cumulative project",
            "material controlled security failure",
            "actual protected-state effect",
            "locally generated permitted and suspicious/denied event pair",
            "A cautious no-go",
            "independently chosen, previously unseen",
            "all fourteen SEC9 outcomes",
            "No optional course",
        ):
            self.assertIn(phrase, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
