"""Regression tests for focused SEF5 design and accessible review hardening.

Existing SEF5-O1..O12 and SEF5-AS1..AS6 are historical contracts.
New SEF5-O13..O15 must have new, independently reviewable evidence.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF5.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
SEF9 = ROOT / "curriculum" / "SEF" / "SEF9.md"
OUTCOME_CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"


def sections():
    source = COURSE.read_text(encoding="utf-8")
    learning = source.split("\n## Learning outcomes\n", 1)[1].split(
        "\n## Modules\n", 1
    )[0]
    modules = source.split("\n## Modules\n", 1)[1].split(
        "\n## Completion requirements\n", 1
    )[0]
    completion = source.split("\n## Completion requirements\n", 1)[1]
    return source, learning, modules, completion


class SEF5DesignQualityTests(unittest.TestCase):
    def test_course_passes_strict_current_outcome_validator(self):
        result = subprocess.run(
            [sys.executable, str(OUTCOME_CHECKER), "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_outcome_identity_and_new_required_assessment_coverage(self):
        _, learning, _, completion = sections()
        outcomes = re.findall(r"(?m)^- \*\*(SEF5-O\d+):\*\*", learning)
        self.assertEqual(outcomes, [f"SEF5-O{i}" for i in range(1, 16)])

        ids = re.findall(
            r"(?m)^- \*\*(SEF5-AS\d+)\*\* \(required ", completion
        )
        self.assertEqual(ids, [f"SEF5-AS{i}" for i in range(1, 8)])
        blocks = re.split(
            r"(?=^- \*\*SEF5-AS\d+\*\* \(required )",
            completion, flags=re.M,
        )[1:]
        coverage = set()
        for block in blocks:
            match = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(match)
            coverage.update(re.findall(r"SEF5-O\d+", match.group(1)))
            for field in ("Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
        self.assertEqual(coverage, set(outcomes))
        new = blocks[-1]
        self.assertTrue(new.startswith("- **SEF5-AS7**"))
        self.assertTrue(
            {"SEF5-O13", "SEF5-O14", "SEF5-O15"}.issubset(
                set(re.findall(r"SEF5-O\d+", new.split("\n  - Work:", 1)[0]))
            )
        )
        self.assertIn("same", new.split("  - Work:", 1)[1].split("\n", 1)[0])
        self.assertIn("real subprocess/persistence integration tests", new)
        self.assertIn("accessible Markdown or plain-text design review", new)

    def test_modules_derive_from_real_competency_prerequisites(self):
        _, learning, modules, _ = sections()
        known = set(re.findall(r"(?m)^- \*\*(SEF5-O\d+):\*\*", learning))
        heads = list(re.finditer(r"(?m)^### Module (\d+) — (.+)$", modules))
        self.assertTrue(heads)
        self.assertEqual(
            [int(h.group(1)) for h in heads],
            list(range(1, len(heads) + 1)),
        )
        first = {}
        for index, head in enumerate(heads):
            end = heads[index + 1].start() if index + 1 < len(heads) else len(modules)
            block = modules[head.start():end]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            refs, lessons = block.split("#### Lessons", 1)
            assigned = re.findall(r"(?m)^- (SEF5-O\d+)$", refs)
            self.assertTrue(assigned)
            self.assertEqual(len(assigned), len(set(assigned)))
            self.assertTrue(set(assigned).issubset(known))
            for outcome in assigned:
                first.setdefault(outcome, index)
            ordinals = [int(v) for v in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(ordinals)
            self.assertEqual(ordinals, list(range(1, len(ordinals) + 1)))
            self.assertEqual(
                len(re.findall(r"(?m)^\d+\. \*\*[^*]+\*\* — ", lessons)),
                len(ordinals),
                "lessons must name a distinct teachable objective and mechanism",
            )
        self.assertEqual(set(first), known)

        # Test pedagogical dependencies, not a fixed module quota or title.
        for prerequisite, application in (
            ("SEF5-O1", "SEF5-O5"),   # Git change history before refactoring
            ("SEF5-O3", "SEF5-O5"),   # characterization before refactoring
            ("SEF5-O3", "SEF5-O8"),   # tests before the CI gate
            ("SEF5-O5", "SEF5-O8"),   # working app before gate/release
            ("SEF5-O13", "SEF5-O15"), # design analysis before quality review
            ("SEF5-O14", "SEF5-O15"), # API evidence before quality review
            ("SEF5-O15", "SEF5-O11"), # accessible review before final handoff
        ):
            with self.subTest(dependency=f"{prerequisite}->{application}"):
                self.assertLess(first[prerequisite], first[application])

        for mechanism in (
            "cohesion", "coupling", "information hiding",
            "dependency direction", "preconditions", "side effects",
            "runtime", "compatibility", "accessible",
            "source locations", "independent", "subprocess",
            "test double", "CLI", "revert", "clock",
        ):
            with self.subTest(mechanism=mechanism):
                self.assertIn(mechanism.lower(), modules.lower())

    def test_review_and_ci_are_not_mislabeled_as_real_execution(self):
        source, _, modules, completion = sections()
        self.assertIn("simulated", modules.lower())
        self.assertIn("real independent reviewer", modules.lower())
        self.assertIn("pull_request_target", modules)
        self.assertIn("clean checkout", source.lower())
        self.assertIn("no paid account", completion.lower())
        self.assertIn("independent reviewer", completion.lower())

    def test_no_duplicated_capstone_or_hidden_paid_platform_gate(self):
        source, _, _, completion = sections()
        self.assertIn("**Duration:** 10–12 weeks", source)
        self.assertIn("**Prerequisites:** [SEF2](SEF2.md)", source)
        self.assertIn("**Status:** `draft`", source)
        self.assertIn("**Specification:** `v0.2.0`", source)
        self.assertIn("the **same** tested SEF5-AS6 CLI application", completion)
        self.assertIn("no independent second project", source)
        self.assertIn("seven required assessments", source.lower())
        self.assertIn("no paid account", completion)
        self.assertIn("proprietary grader", completion)
        self.assertNotIn("Final integration lab — required", source)
        self.assertIn("| 10–12 weeks | SEF2 |", CATALOG.read_text(encoding="utf-8"))
        self.assertIn("SEF5 already establishes", SEF9.read_text(encoding="utf-8"))

    def test_historical_revision_and_new_evidence_are_distinguished(self):
        source, _, _, _ = sections()
        history = source.split("### Revision history and evidence compatibility", 1)[1]
        for requirement in (
            "168b30cc304b0d57f019b2b289d2b11b647708e4",
            "`SEF5-O1`–`O12`", "`SEF5-AS1`–`AS6`",
            "SEF5-O13", "SEF5-O14", "SEF5-O15",
            "SEF5-AS7", "No global OEE",
        ):
            with self.subTest(requirement=requirement):
                self.assertIn(requirement, history)
        self.assertIn("not automatically revoked or converted", history)

    def test_omitting_any_new_summative_outcome_fails_validator(self):
        source, _, _, _ = sections()
        target = "SEF5-O13, SEF5-O14, SEF5-O15\n  - Work:"
        self.assertIn(target, source)
        for missing in ("SEF5-O13", "SEF5-O14", "SEF5-O15"):
            with self.subTest(missing=missing):
                replacement = ", ".join(
                    outcome for outcome in ("SEF5-O13", "SEF5-O14", "SEF5-O15")
                    if outcome != missing
                ) + "\n  - Work:"
                damaged = source.replace(target, replacement, 1)
                self.assertNotEqual(damaged, source)
                with tempfile.TemporaryDirectory() as folder:
                    course = Path(folder) / "SEF5.md"
                    course.write_text(damaged, encoding="utf-8")
                    proc = subprocess.run(
                        [sys.executable, str(OUTCOME_CHECKER), "--course", str(course)],
                        cwd=ROOT, capture_output=True, text=True, check=False,
                    )
                    self.assertNotEqual(proc.returncode, 0)
                    self.assertIn(missing, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
