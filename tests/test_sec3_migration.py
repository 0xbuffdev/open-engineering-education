"""SEC3 outcome/evidence and preparation checks without numeric curriculum quotas."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "curriculum" / "SEC"
COURSE = SEC / "SEC3.md"
CATALOG = SEC / "README.md"


class SEC3MigrationTests(unittest.TestCase):
    def test_official_outcome_curriculum_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_identity_and_no_hidden_rust_prerequisite(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith("# SEC3 — Systems & Binary Security\n"))
        for field in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
            "**Duration:** 10–14 weeks",
            "**Prerequisites:** [SEC1](SEC1.md)",
        ):
            self.assertIn(field, source)
        self.assertIn(
            "| [SEC3](SEC3.md) | Systems & Binary Security | 10–14 weeks "
            "| SEC1 | `course` |", catalog)
        prereq = re.search(r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
        self.assertIsNotNone(prereq)
        self.assertNotIn("SYS1", prereq.group(1))
        self.assertNotIn("SYS2", prereq.group(1))
        self.assertIn("or a Rust compiler are not prerequisites", source)
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_every_outcome_taught_and_assessed_with_explicit_criteria(self):
        text = COURSE.read_text(encoding="utf-8")
        learning = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcomes = re.findall(r"(?m)^- \*\*(SEC3-O\d+):\*\*", learning)
        self.assertTrue(outcomes)
        self.assertEqual(len(outcomes), len(set(outcomes)))
        known = set(outcomes)
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        heads = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(heads)
        self.assertEqual(
            [int(x.group(1)) for x in heads],
            list(range(1, len(heads) + 1)))
        taught = set()
        for i, head in enumerate(heads):
            stop = heads[i + 1].start() if i + 1 < len(heads) else len(modules)
            block = modules[head.start():stop]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            targets, sequence = block.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC3-O\d+)$", targets))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            taught.update(refs)
            ordinal = [int(x) for x in re.findall(r"(?m)^(\d+)\. \*\*", sequence)]
            self.assertTrue(ordinal)
            self.assertEqual(ordinal, list(range(1, len(ordinal) + 1)))
        self.assertEqual(taught, known)
        completion = text.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC3-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        ids = []
        assessed = set()
        for block in blocks:
            head = re.match(r"- \*\*(SEC3-AS\d+)\*\*", block)
            self.assertIsNotNone(head)
            ids.append(head.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            values = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(values)
            refs = set(re.findall(r"SEC3-O\d+", values.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(assessed, known)

    def test_required_work_is_safe_and_distinguishes_evidence(self):
        text = COURSE.read_text(encoding="utf-8")
        for needle in (
            "nonprivileged",
            "undefined behavior",
            "independently",
            "No mandatory exploit construction",
            "or a Rust compiler are not prerequisites",
            "All other lesson investigations and formative checks are optional",
        ):
            self.assertIn(needle, text)
        self.assertNotIn("kind: `lab`", text)
        self.assertNotIn("kind: `test`", text)
        self.assertNotIn("## Substantial course lab", text)


if __name__ == "__main__":
    unittest.main()
