"""Guard SEF3 POSIX/Bash/GNU distinctions, process environments, and stable IDs.

The migration adds one evidence-bearing assessment without silently changing
historical outcomes or introducing a new independent shell project.
"""

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF3.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
SEF7 = ROOT / "curriculum" / "SEF" / "SEF7.md"


def parts():
    text = COURSE.read_text(encoding="utf-8")
    learning = text.split("\n## Learning outcomes\n", 1)[1].split(
        "\n## Modules\n", 1)[0]
    instruction = text.split("\n## Modules\n", 1)[1].split(
        "\n## Completion requirements\n", 1)[0]
    completion = text.split("\n## Completion requirements\n", 1)[1]
    return text, learning, instruction, completion


class SEF3PortabilityTests(unittest.TestCase):
    def test_current_sef_and_outcome_validators_pass(self):
        commands = (
            ["check-sef-curriculum.py"],
            ["check-outcome-curriculum.py", "--course", str(COURSE)],
        )
        for args in commands:
            with self.subTest(args=args):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / args[0]), *args[1:]],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_historical_outcome_and_assessment_ids_are_not_renumbered(self):
        _, learning, _, completion = parts()
        outcomes = re.findall(r"(?m)^- \*\*(SEF3-O\d+):\*\*", learning)
        self.assertEqual(outcomes, [f"SEF3-O{i}" for i in range(1, 15)])
        assessments = re.findall(
            r"(?m)^- \*\*(SEF3-AS\d+)\*\* \(required ", completion
        )
        self.assertEqual(assessments, [f"SEF3-AS{i}" for i in range(1, 8)])
        required = completion.split("- **SEF3-AS7**", 1)[1].split(
            "\n### Completion decision", 1)[0]
        self.assertRegex(required, r"(?m)^  - Outcomes: .*SEF3-O13, SEF3-O14$")
        for field in ("Work", "Criteria", "Evidence"):
            self.assertRegex(required, rf"(?m)^  - {field}: \S")
        self.assertIn("existing SEF3-AS6 toolkit", required)

    def test_all_outcomes_have_real_summative_claims(self):
        _, learning, _, completion = parts()
        definitions = set(re.findall(r"(?m)^- \*\*(SEF3-O\d+):\*\*", learning))
        blocks = re.split(
            r"(?=^- \*\*SEF3-AS\d+\*\* \(required )",
            completion, flags=re.M
        )[1:]
        self.assertEqual(len(blocks), 7)
        covered = set()
        for block in blocks:
            claim = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(claim)
            ids = set(re.findall(r"SEF3-O\d+", claim.group(1)))
            self.assertTrue(ids.issubset(definitions))
            covered.update(ids)
        self.assertEqual(covered, definitions)

    def test_two_new_modules_are_ordered_and_instructionally_specific(self):
        _, _, instruction, _ = parts()
        matches = list(re.finditer(r"(?m)^### Module (\d+) — (.+)$", instruction))
        self.assertEqual([int(x.group(1)) for x in matches], list(range(1, 14)))
        self.assertIn("Module 6 — Process Environments", instruction)
        self.assertIn("Module 12 — POSIX Shell", instruction)
        for index, header in enumerate(matches):
            stop = matches[index + 1].start() if index + 1 < len(matches) else len(instruction)
            block = instruction[header.start():stop]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            refs, lessons = block.split("#### Lessons", 1)
            self.assertRegex(refs, r"(?m)^- SEF3-O\d+")
            ordinals = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(ordinals)
            self.assertEqual(ordinals, list(range(1, len(ordinals) + 1)))
        for topic in (
            "export", "BASH_ENV", "env -i", "LC_ALL=C", "subshell",
            "POSIX", "Bash", "GNU", "printf", "pipefail", "set -e",
            "shebang", "read", "utility", "locale", "symlink",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic.lower(), instruction.lower())

    def test_sef3_reuses_toolkit_and_preserves_historical_contract(self):
        source, _, _, completion = parts()
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", source)
        self.assertIn("**Duration:** 10–12 weeks", source)
        self.assertIn("**Status:** `draft`", source)
        self.assertIn("**Specification:** `v0.2.0`", source)
        self.assertIn("SEF3-AS1", source)
        self.assertIn("SEF3-AS6", source)
        self.assertIn("SEF3-AS7", source)
        self.assertIn("not a new independent project", source)
        self.assertIn("No automatic equivalence", source)
        self.assertIn("1fb369a251a093736f63fa1cfa95656ded87ad99", source)
        self.assertIn("| 10–12 weeks | SEF2 |", CATALOG.read_text(encoding="utf-8"))
        self.assertIn("SEF3 already establishes", SEF7.read_text(encoding="utf-8"))
        self.assertIn("all seven required summative assessments", completion)

    def test_unassessed_new_portability_or_environment_outcome_fails(self):
        source, _, _, _ = parts()
        for removed in ("SEF3-O13", "SEF3-O14"):
            with self.subTest(removed=removed):
                damaged = source.replace(
                    "SEF3-O13, SEF3-O14\n  - Work:",
                    ("SEF3-O14" if removed == "SEF3-O13" else "SEF3-O13") + "\n  - Work:",
                    1,
                )
                self.assertNotEqual(damaged, source)
                with tempfile.TemporaryDirectory() as folder:
                    course = Path(folder) / "SEF3.md"
                    course.write_text(damaged, encoding="utf-8")
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
                         "--course", str(course)],
                        capture_output=True, text=True, cwd=ROOT, check=False,
                    )
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(removed, result.stderr)


if __name__ == "__main__":
    unittest.main()
