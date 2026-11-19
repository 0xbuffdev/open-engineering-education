"""SEC2 curriculum contracts; no arbitrary module or lesson-count targets."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "curriculum" / "SEC"
COURSE = SEC / "SEC2.md"
CATALOG = SEC / "README.md"


class SEC2MigrationTests(unittest.TestCase):
    def test_official_outcome_curriculum_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_catalog_and_source_prerequisites_match(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith("# SEC2 — Web & Application Security\n"))
        for expected in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
            "**Duration:** 12–16 weeks",
            "**Prerequisites:** [SEC1](SEC1.md), [APP1](../APP/APP1.md)",
        ):
            self.assertIn(expected, source)
        self.assertIn(
            "| [SEC2](SEC2.md) | Web & Application Security | 12–16 weeks "
            "| SEC1, APP1 | `course` |", catalog)
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_backend_preparation_is_taught_without_weakening_security_proof(self):
        source = COURSE.read_text(encoding="utf-8")
        metadata = next(
            line for line in source.splitlines()
            if line.startswith("**Prerequisites:**"))
        self.assertNotIn("APP3", metadata)
        self.assertIn("**Prerequisites:** [SEC1](SEC1.md), [APP1](../APP/APP1.md)", metadata)
        for expected in (
            "source-inspectable local HTTP service",
            "reproducible setup",
            "server-side actor/action/resource decision",
            "actual local SQLite database",
            "real security corrections",
            "independently expected legitimate, denied and failure-state behavior",
            "through its handler, session principal, authorization condition",
        ):
            self.assertIn(expected, source)
        # Teaching a ready-to-run service is not a substitute for live boundary
        # enforcement, source changes, authoritative data and negative evidence.
        self.assertIn("locally executed state checks", source)
        self.assertIn("a reintroduced fault", source)

    def test_each_outcome_has_instruction_and_summative_evidence(self):
        text = COURSE.read_text(encoding="utf-8")
        outcomes_section = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        ids = re.findall(r"(?m)^- \*\*(SEC2-O\d+):\*\*", outcomes_section)
        self.assertTrue(ids)
        self.assertEqual(len(ids), len(set(ids)))
        known = set(ids)
        modules = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        starts = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(starts)
        self.assertEqual(
            [int(m.group(1)) for m in starts],
            list(range(1, len(starts) + 1)))
        taught = set()
        for index, match in enumerate(starts):
            stop = starts[index + 1].start() if index + 1 < len(starts) else len(modules)
            block = modules[match.start():stop]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            targets, sequence = block.split("#### Lessons", 1)
            references = set(re.findall(r"(?m)^- (SEC2-O\d+)$", targets))
            self.assertTrue(references)
            self.assertTrue(references <= known)
            taught.update(references)
            entries = [int(v) for v in re.findall(r"(?m)^(\d+)\. \*\*", sequence)]
            self.assertTrue(entries)
            self.assertEqual(entries, list(range(1, len(entries) + 1)))
        self.assertEqual(taught, known)
        completion = text.split("\n## Completion requirements\n", 1)[1]
        assessment_blocks = re.split(
            r"(?=^- \*\*SEC2-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(assessment_blocks)
        assessment_ids = []
        covered = set()
        for block in assessment_blocks:
            heading = re.match(r"- \*\*(SEC2-AS\d+)\*\*", block)
            self.assertIsNotNone(heading)
            assessment_ids.append(heading.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(
                    block, rf"(?m)^  - \*\*{field}:\*\* \S")
            line = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(line)
            references = set(re.findall(r"SEC2-O\d+", line.group(1)))
            self.assertTrue(references)
            self.assertTrue(references <= known)
            covered.update(references)
        self.assertEqual(len(assessment_ids), len(set(assessment_ids)))
        self.assertEqual(covered, known)

    def test_safety_and_nonmandatory_practice(self):
        source = COURSE.read_text(encoding="utf-8")
        self.assertIn("Optional lesson investigations", source)
        self.assertIn("No real credential theft", source)
        self.assertIn("loopback", source)
        self.assertIn("## Completion requirements", source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


if __name__ == "__main__":
    unittest.main()
