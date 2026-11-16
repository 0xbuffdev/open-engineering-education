"""SEF9 professional obligations, historical evidence and authentic public fixtures.

The four new capabilities must have independent assessment, without rewriting
old outcome/assessment meanings or substituting teaching examples for reviewers.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF9.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
SEF10 = ROOT / "curriculum" / "SEF" / "SEF10.md"
FIX = ROOT / "examples" / "sef9"
CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"

# FNV-1a Unicode code-point checksums from the published pre-change revision
# 8a0551c29b1639c4fb6cc336769c8a21d2c6e512.
PRIOR_OUTCOMES = "a4bc5675"
PRIOR_ASSESSMENTS = (
    "44846c7d", "cfab5249", "4c1a2a57", "c6cdc83c",
    "450a473a", "de6d4cb3", "26e47dad",
)

EXPECTED_MODULES = (
    "From Need to Work Item",
    "Professional Ethics, Duty of Care and Honest Escalation",
    "Planning & Tracking Work",
    "Recording Decisions",
    "Software Licensing, Copyright and Provenance",
    "Privacy, Confidentiality and Data Stewardship",
    "Accessible Communication and Inclusive Engineering Handoffs",
    "Code Review as Practice",
    "Working with AI Assistants",
    "Verifying & Governing AI-Generated Work",
    "Trust Boundaries in AI-Assisted Work",
    "Feature Delivery Workflow",
)


def checksum(text: str) -> str:
    value = 2166136261
    for char in text:
        value = ((value ^ ord(char)) * 16777619) & 0xFFFFFFFF
    return f"{value:08x}"


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


def assessment_blocks(completion: str) -> list[str]:
    found = list(re.finditer(r"(?m)^- \*\*SEF9-AS\d+\*\* \(required ", completion))
    end = completion.index("### Completion decision")
    return [
        completion[m.start():found[i+1].start() if i+1 < len(found) else end].rstrip()
        for i, m in enumerate(found)
    ]


class SEF9ProfessionalTests(unittest.TestCase):
    def test_current_course_and_program_validators_pass(self):
        for script, arguments in (
            ("check-outcome-curriculum.py", ["--course", str(COURSE)]),
            ("check-sef-curriculum.py", []),
        ):
            with self.subTest(script=script):
                p = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / script), *arguments],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_original_sixteen_outcome_descriptions_and_seven_blocks_are_exact(self):
        _, learning, _, completion = sections()
        old_outcomes = re.split(r"(?=^- \*\*SEF9-O17:\*\*)", learning, flags=re.M)[0]
        self.assertEqual(checksum(old_outcomes.rstrip()), PRIOR_OUTCOMES)
        blocks = assessment_blocks(completion)
        self.assertEqual(len(blocks), 8)
        self.assertEqual([checksum(x) for x in blocks[:7]], list(PRIOR_ASSESSMENTS))
        for i, block in enumerate(blocks[:7], start=1):
            self.assertTrue(block.startswith(f"- **SEF9-AS{i}**"))

    def test_twenty_outcomes_and_eight_assessments_are_fully_mapped(self):
        _, learning, _, completion = sections()
        ids = re.findall(r"(?m)^- \*\*(SEF9-O\d+):\*\*", learning)
        self.assertEqual(ids, [f"SEF9-O{i}" for i in range(1, 21)])
        blocks = assessment_blocks(completion)
        claimed = set()
        for i, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF9-AS{i}**"))
            for section in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {section}: \S")
            declaration = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(declaration)
            claimed.update(re.findall(r"SEF9-O\d+", declaration.group(1)))
        self.assertEqual(claimed, set(ids))
        for i in range(17, 21):
            self.assertRegex(blocks[-1], rf"(?m)^  - Outcomes: .*SEF9-O{i}")

    def test_twelve_ordered_teaching_modules_have_outcomes_and_lessons(self):
        _, learning, modules, _ = sections()
        known = set(re.findall(r"(?m)^- \*\*(SEF9-O\d+):\*\*", learning))
        heads = list(re.finditer(r"(?m)^### Module (\d+) — (.+)$", modules))
        self.assertEqual([int(m.group(1)) for m in heads], list(range(1, 13)))
        self.assertEqual(tuple(m.group(2) for m in heads), EXPECTED_MODULES)
        count = 0
        for i, head in enumerate(heads):
            stop = heads[i+1].start() if i+1 < len(heads) else len(modules)
            block = modules[head.start():stop]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            refs, lessons = block.split("#### Lessons", 1)
            linked = set(re.findall(r"(?m)^- (SEF9-O\d+)$", refs))
            self.assertTrue(linked)
            self.assertTrue(linked.issubset(known))
            nums = [int(m) for m in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums)+1)))
            count += len(nums)
        self.assertEqual(count, 88)

    def test_new_assessment_is_professional_and_does_not_add_another_project(self):
        source, _, _, completion = sections()
        block = assessment_blocks(completion)[-1]
        for text in (
            "same CSV-export feature", "without relying on an AI suggestion",
            "evidence versus assumptions", "stop/mitigation/escalation",
            "unknown", "license", "copyright", "SPDX", "attribution",
            "data-flow", "retention", "privacy", "accessible Markdown",
            "non-color-only", "genuine independent reader response",
        ):
            with self.subTest(text=text):
                self.assertIn(text.lower(), block.lower())
        self.assertIn("all **eight required assessments**", completion.lower())
        self.assertIn("**Duration:** 10–12 weeks", source)
        self.assertIn("**Prerequisites:** [SEF5](SEF5.md)", source)
        self.assertIn("**Status:** " + chr(96) + "draft" + chr(96), source)
        self.assertIn(
            "| [SEF9](SEF9.md) | Professional Workflow & AI-Assisted Engineering | 10–12 weeks |",
            CATALOG.read_text(encoding="utf-8"),
        )
        self.assertIn("honest risk communication", SEF10.read_text(encoding="utf-8"))

    def test_public_case_is_real_synthetic_no_false_approval_or_external_dependency(self):
        expected = {
            "README.md", "feature-request.md", "seeded_export.py",
            "test_seeded_export.py", "assistant-proposal.md",
            "untrusted-readme.md", "professional-case.md",
        }
        self.assertEqual({f.name for f in FIX.iterdir() if f.is_file()}, expected)
        readme = (FIX / "README.md").read_text(encoding="utf-8")
        provenance = (FIX / "assistant-proposal.md").read_text(encoding="utf-8")
        injection = (FIX / "untrusted-readme.md").read_text(encoding="utf-8")
        dilemma = (FIX / "professional-case.md").read_text(encoding="utf-8")
        self.assertIn("intentionally fail", readme.lower())
        self.assertIn("ChatGPT (GPT-6)", provenance)
        self.assertIn("not a transcript of a separate", provenance.lower())
        self.assertIn("No subprocesses", provenance)
        self.assertIn("Do **not** obey it", injection)
        for term in ("fictional", "license", "privacy", "accessibility", "No", "manager"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), dilemma.lower())
        self.assertNotIn("https://example.com/collect", injection)

    def test_all_three_seeded_failure_cases_fail_as_documented(self):
        result = subprocess.run(
            [
                sys.executable, "-m", "unittest", "discover",
                "-s", "examples/sef9", "-p", "test_seeded_export.py", "-v",
            ],
            cwd=ROOT, text=True, capture_output=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Ran 3 tests", result.stderr + result.stdout)
        self.assertIn("FAILED (failures=3)", result.stderr + result.stdout)
        for token in (
            "test_quotes_commas_and_newlines_round_trip",
            "test_directory_destination_reports_failure",
            "test_invalid_source_cannot_overwrite",
        ):
            self.assertIn(token, result.stderr + result.stdout)

    def test_reject_unassessed_new_professional_outcome(self):
        source, _, _, _ = sections()
        for removed in ("SEF9-O17", "SEF9-O18", "SEF9-O19", "SEF9-O20"):
            with self.subTest(removed=removed):
                damaged = re.sub(
                    r"(?m)^(  - Outcomes: .+)$",
                    lambda m: m.group(1).replace(", " + removed, ""),
                    source,
                )
                self.assertNotEqual(damaged, source)
                with tempfile.TemporaryDirectory() as directory:
                    target = Path(directory) / "SEF9.md"
                    target.write_text(damaged, encoding="utf-8")
                    check = subprocess.run(
                        [sys.executable, str(CHECKER), "--course", str(target)],
                        cwd=ROOT, text=True, capture_output=True, check=False,
                    )
                    self.assertNotEqual(check.returncode, 0)
                    self.assertIn(removed, check.stdout + check.stderr)


if __name__ == "__main__":
    unittest.main()
