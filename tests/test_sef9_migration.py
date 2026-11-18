"""Guard SEF9's OEE v0.2.0 workflow and independent AI-verification contract."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF9.md"
SEF_DIR = COURSE.parent
CATALOG = SEF_DIR / "README.md"


class SEF9MigrationTests(unittest.TestCase):
    def test_strict_outcome_validator_accepts_course(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_program_validator_accepts_all_outcome_driven_sef(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/check-sef-curriculum.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        self.assertIn("11 v0.2.0, 0 legacy", result.stdout)

    def test_all_eleven_program_courses_are_current_draft_format(self):
        paths = sorted(SEF_DIR.glob("SEF[0-9]*.md"))
        self.assertEqual(len(paths), 11)
        for path in paths:
            with self.subTest(course=path.name):
                source = path.read_text(encoding="utf-8")
                self.assertIn("**Specification:** `v0.2.0`", source)
                self.assertIn("**Status:** `draft`", source)
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("All eleven SEF course files use", catalog)
        self.assertIn("no historical-format SEF course definitions remain", catalog)

    def test_twenty_outcomes_mapped_to_eight_required_assessments(self):
        course = COURSE.read_text(encoding="utf-8")
        learning = course.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        defined = set(re.findall(r"(?m)^- \*\*(SEF9-O\d+):\*\*", learning))
        self.assertEqual(defined, {f"SEF9-O{i}" for i in range(1, 21)})
        completion = course.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEF9-AS\d+\*\* \(required )", completion, flags=re.M
        )[1:]
        self.assertEqual(len(blocks), 8)
        covered = set()
        for index, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF9-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            references = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(references)
            refs = set(re.findall(r"SEF9-O\d+", references.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs.issubset(defined))
            covered.update(refs)
        self.assertEqual(covered, defined)

    def test_competency_owned_modules_map_all_outcomes_without_a_fixed_quota(self):
        source = COURSE.read_text(encoding="utf-8")
        learning = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1
        )[0]
        known = set(re.findall(r"(?m)^- \*\*(SEF9-O\d+):\*\*", learning))
        content = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1
        )[0]
        modules = list(re.finditer(r"(?m)^### Module (\d+) — ", content))
        self.assertTrue(modules)
        self.assertEqual(
            [int(m.group(1)) for m in modules],
            list(range(1, len(modules) + 1)),
        )
        covered = set()
        for index, module in enumerate(modules):
            stop = modules[index + 1].start() if index + 1 < len(modules) else len(content)
            block = content[module.start():stop]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            mapped, lessons = block.split("#### Lessons", 1)
            ids = re.findall(r"(?m)^- (SEF9-O\d+)$", mapped)
            self.assertTrue(ids)
            self.assertEqual(len(ids), len(set(ids)))
            self.assertTrue(set(ids).issubset(known))
            covered.update(ids)
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
        self.assertEqual(covered, known)

    def test_prerequisite_and_human_ai_trust_requirements_remain(self):
        text = COURSE.read_text(encoding="utf-8")
        self.assertIn("**Prerequisites:** [SEF5](SEF5.md)", text)
        self.assertIn("**Duration:** 10–12 weeks", text)
        self.assertIn("[SEF9-AS8]", text.replace("**SEF9-AS8**", "[SEF9-AS8]"))
        self.assertIn("fully synthetic", text.lower())
        self.assertIn("**Status:** `draft`", text)
        self.assertIn("**Specification:** `v0.2.0`", text)
        self.assertNotIn("— `test`", text)
        self.assertNotIn("— `lab`", text)
        self.assertNotIn("Final integration lab — required", text)
        for fragment in (
            "authentic instructor-supplied recorded assistant proposal",
            "independent reviewer",
            "without assistant help",
            "untrusted",
            "permissions",
            "licensing",
            "synthetic",
            "No paid AI account",
        ):
            self.assertIn(fragment.lower(), text.lower())


if __name__ == "__main__":
    unittest.main()
