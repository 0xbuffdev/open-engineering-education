"""SEF11 course and SEF mathematical dependency migration regressions."""

import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEF = ROOT / "curriculum" / "SEF"
COURSE = SEF / "SEF11.md"
CATALOG = SEF / "README.md"
SEF4 = SEF / "SEF4.md"
SEF8 = SEF / "SEF8.md"
SEF10 = SEF / "SEF10.md"


class SEF11CurriculumTests(unittest.TestCase):
    def test_both_structural_validators_pass(self):
        for args in (["--course", str(COURSE)],):
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"), *args],
                capture_output=True, text=True, cwd=ROOT, check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
        proc = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            capture_output=True, text=True, cwd=ROOT, check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)
        self.assertIn("11 courses", proc.stdout)

    def test_ten_outcomes_and_six_assessments_are_mapped(self):
        text = COURSE.read_text(encoding="utf-8")
        lesson = text.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcomes = set(re.findall(r"(?m)^- \*\*(SEF11-O\d+):\*\*", lesson))
        self.assertEqual(outcomes, {f"SEF11-O{i}" for i in range(1, 11)})
        completion = text.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(r"(?=^- \*\*SEF11-AS\d+\*\* \(required )",
                          completion, flags=re.M)[1:]
        self.assertEqual(len(blocks), 6)
        covered = set()
        for index, block in enumerate(blocks, 1):
            self.assertTrue(block.startswith(f"- **SEF11-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            refs = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(refs)
            claimed = set(re.findall(r"SEF11-O\d+", refs.group(1)))
            self.assertTrue(claimed.issubset(outcomes))
            covered.update(claimed)
        self.assertEqual(covered, outcomes)

    def test_nine_instructional_modules_and_accessible_bridge(self):
        text = COURSE.read_text(encoding="utf-8")
        source = text.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        modules = list(re.finditer(r"(?m)^### Module (\d+) — ", source))
        self.assertEqual([int(x.group(1)) for x in modules], list(range(1, 10)))
        for i, match in enumerate(modules):
            stop = modules[i + 1].start() if i + 1 < len(modules) else len(source)
            module = source[match.start():stop]
            self.assertIn("#### Outcomes", module)
            self.assertIn("#### Lessons", module)
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", module)]
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
            self.assertGreater(len(numbers), 0)
        self.assertIn("ungraded entry diagnostic", text)
        self.assertIn("fixed attempt limit", text)
        self.assertIn("**Status:** `draft`", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", text)

    def test_prerequisites_and_topological_course_order(self):
        catalog = CATALOG.read_text(encoding="utf-8")
        order = re.findall(r"(?m)^\| \[(SEF\d+)\]\(SEF\d+\.md\)", catalog)
        self.assertEqual(set(order), {f"SEF{i}" for i in range(1, 12)})
        self.assertEqual(len(order), 11)
        self.assertEqual(order[-1], "SEF10")
        for dependent in ("SEF4", "SEF8"):
            self.assertLess(order.index("SEF11"), order.index(dependent))
        self.assertIn("**Prerequisites:** [SEF11](SEF11.md)",
                      SEF4.read_text(encoding="utf-8"))
        self.assertIn("**Prerequisites:** [SEF11](SEF11.md)",
                      SEF8.read_text(encoding="utf-8"))
        self.assertIn("[SEF11](SEF11.md)",
                      SEF10.read_text(encoding="utf-8"))
        self.assertIn("SEF1–SEF9, SEF11", catalog)

    def test_validator_expands_linked_capstone_range_and_rejects_duplicate(self):
        scripts = ROOT / "scripts"
        sys.path.insert(0, str(scripts))
        self.addCleanup(lambda: sys.path.remove(str(scripts)))
        spec = importlib.util.spec_from_file_location("sef_validator", scripts / "check-sef-curriculum.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sequence = "[SEF1](SEF1.md)–[SEF9](SEF9.md), [SEF11](SEF11.md)"
        result = module.prerequisites(sequence, owner="test")
        self.assertEqual(result, [f"SEF{i}" for i in range(1, 10)] + ["SEF11"])
        self.assertEqual(module.ERRORS, [])
        self.assertEqual(module.prerequisites("SEF11, SEF11", owner="test"),
                         ["SEF11", "SEF11"])
        self.assertTrue(any("duplicate" in error for error in module.ERRORS))


if __name__ == "__main__":
    unittest.main()
