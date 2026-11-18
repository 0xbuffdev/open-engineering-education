"""Regression checks for SEF2 object abstraction and typing hardening.

The ten original SEF2 outcomes and five required assessments remain intact;
new capability is separately identified rather than quietly changing an ID.
"""

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF2.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"


class SEF2AbstractionTests(unittest.TestCase):
    def test_structural_validators_accept_current_revision(self):
        for script, args in (
            ("check-outcome-curriculum.py", ["--course", str(COURSE)]),
            ("check-sef-curriculum.py", []),
        ):
            with self.subTest(script=script):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / script), *args],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_old_ids_retained_and_new_outcomes_have_distinct_summative_evidence(self):
        source = COURSE.read_text(encoding="utf-8")
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcomes = re.findall(r"(?m)^- \*\*(SEF2-O\d+):\*\*", learning)
        self.assertEqual(outcomes, [f"SEF2-O{i}" for i in range(1, 13)])
        completion = source.split("\n## Completion requirements\n", 1)[1]
        ids = re.findall(r"(?m)^- \*\*(SEF2-AS\d+)\*\* \(required ", completion)
        self.assertEqual(ids, [f"SEF2-AS{i}" for i in range(1, 7)])
        new = completion.split("- **SEF2-AS6**", 1)[1].split(
            "\n### Completion decision", 1)[0]
        self.assertRegex(new, r"(?m)^  - Outcomes: .*SEF2-O11, SEF2-O12$")
        for field in ("Work", "Criteria", "Evidence"):
            self.assertRegex(new, rf"(?m)^  - {field}: \S")
        self.assertIn("existing SEF2-AS5 task manager", new)
        self.assertIn("without an unnecessary inheritance hierarchy", new)

    def test_classes_type_annotations_and_runtime_validation_are_teachable(self):
        source = COURSE.read_text(encoding="utf-8")
        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        heads = list(re.finditer(r"(?m)^### Module (\d+) — (.+)$", modules))
        # The curriculum derives module count from competencies: never lock a quota.
        self.assertTrue(heads)
        self.assertEqual(
            [int(m.group(1)) for m in heads],
            list(range(1, len(heads) + 1)),
        )
        first_instruction = {}
        for i, head in enumerate(heads):
            next_pos = heads[i + 1].start() if i + 1 < len(heads) else len(modules)
            chunk = modules[head.start():next_pos]
            self.assertEqual(chunk.count("#### Outcomes"), 1)
            self.assertEqual(chunk.count("#### Lessons"), 1)
            outcomes_part = chunk.split("#### Outcomes", 1)[1].split("#### Lessons", 1)[0]
            assigned = re.findall(r"(?m)^- (SEF2-O\d+)$", outcomes_part)
            self.assertTrue(assigned, "every module must identify a needed outcome")
            for outcome in assigned:
                first_instruction.setdefault(outcome, i)
            numbers = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", chunk)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

        # Check actual preparatory dependencies, not a cosmetic module count.
        # A learner must encounter the mechanism before its integrated use.
        for earlier, later in (
            ("SEF2-O2", "SEF2-O10"),   # running Python before a CLI
            ("SEF2-O5", "SEF2-O6"),    # collections before nested aliasing
            ("SEF2-O6", "SEF2-O11"),   # references before class invariants
            ("SEF2-O10", "SEF2-O11"),  # working CLI before object refactoring
            ("SEF2-O11", "SEF2-O12"),  # objects before typed domain APIs
        ):
            with self.subTest(preparation=f"{earlier} before {later}"):
                self.assertIn(earlier, first_instruction)
                self.assertIn(later, first_instruction)
                self.assertLess(first_instruction[earlier], first_instruction[later])
        required_examples = (
            "__init__", "self", "class attributes", "composition",
            "encapsulation", "instance", "Task | None", "runtime",
            "validation", "annotations", "comprehensions", "iterator",
        )
        for subject in required_examples:
            with self.subTest(subject=subject):
                self.assertIn(subject.lower(), source.lower())
        self.assertIn("**Duration:** 10–12 weeks", source)
        self.assertIn("**Status:** `draft`", source)
        self.assertIn("10–12 weeks", CATALOG.read_text(encoding="utf-8"))

    def test_new_required_outcome_must_not_be_left_unassessed(self):
        original = COURSE.read_text(encoding="utf-8")
        edited = original.replace(
            "SEF2-O11, SEF2-O12\n  - Work:", "SEF2-O11\n  - Work:", 1,
        )
        self.assertNotEqual(edited, original)
        with tempfile.TemporaryDirectory() as location:
            target = Path(location) / "SEF2.md"
            target.write_text(edited, encoding="utf-8")
            check = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
                 "--course", str(target)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(check.returncode, 0)
            self.assertIn("SEF2-O12", check.stderr)
            self.assertIn("no required summative assessment", check.stderr)

    def test_revision_preserves_old_evidence_without_auto_equivalence(self):
        source = COURSE.read_text(encoding="utf-8")
        revision = source.split("### Revision history and evidence compatibility", 1)[1]
        # Retain revision-scoped evidence without requiring a particular
        # typography variant or frozen narrative wording.
        for term in (
            "SEF2-O1", "O10", "SEF2-O11", "SEF2-O12",
            "SEF2-AS1", "AS5", "SEF2-AS6",
            "original course revision", "not automatically", "draft",
        ):
            self.assertIn(term, revision)


if __name__ == "__main__":
    unittest.main()
