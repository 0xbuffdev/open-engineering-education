"""SEF10 complete-prerequisite graduation and one-project integration guards.

RFC 0003 adds genuinely new assessed program-integration capabilities without
rewriting the historical eight outcomes or three summative assessment contracts.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF10.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"

# FNV-1a on Unicode code points, pinned to SEF10 at
# ef51f0a5765a5bb95ad4fdec4e2d58d64997c1b4.
OLD_OUTCOME_CHECKSUM = "1ebbbd9e"
OLD_ASSESSMENT_CHECKSUMS = ("0d0cef3e", "506bf454", "c5ebb0df")

HEADINGS = (
    "Problem and Scope",
    "Graduation Evidence and Cross-Course Transfer Planning",
    "Architecture and Design",
    "Incremental Implementation",
    "Measurement and Release",
    "Responsible Release, Privacy, Licensing and Accessible Handoff",
    "Integration and Review",
    "Delivery and Defense",
)
PREREQUISITES = tuple(f"SEF{i}" for i in range(1, 10)) + ("SEF11",)


def checksum(text: str) -> str:
    digest = 2166136261
    for c in text:
        digest = ((digest ^ ord(c)) * 16777619) & 0xFFFFFFFF
    return f"{digest:08x}"


def parts():
    source = COURSE.read_text(encoding="utf-8")
    outcomes = source.split("\n## Learning outcomes\n", 1)[1].split(
        "\n## Modules\n", 1
    )[0]
    modules = source.split("\n## Modules\n", 1)[1].split(
        "\n## Completion requirements\n", 1
    )[0]
    completion = source.split("\n## Completion requirements\n", 1)[1]
    return source, outcomes, modules, completion


def assessment_blocks(completion: str) -> list[str]:
    found = list(re.finditer(
        r"(?m)^- \*\*SEF10-AS\d+\*\* \(required ", completion
    ))
    end = completion.index("### Project defense and assessment rubric")
    return [
        completion[entry.start():found[i + 1].start() if i + 1 < len(found) else end].rstrip()
        for i, entry in enumerate(found)
    ]


class SEF10GraduationIntegrationTests(unittest.TestCase):
    def test_current_outcome_and_sef_catalog_validators_pass(self):
        for script, args in (
            ("check-outcome-curriculum.py", ["--course", str(COURSE)]),
            ("check-sef-curriculum.py", []),
        ):
            with self.subTest(script=script):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / script), *args],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_all_eight_old_outcome_descriptions_and_three_assessment_blocks_unchanged(self):
        _, outcomes, _, completion = parts()
        old_part = outcomes.split("- **SEF10-O9:**", 1)[0].rstrip()
        old_ids = re.findall(r"(?m)^- \*\*(SEF10-O\d+):\*\*", old_part)
        self.assertEqual(old_ids, [f"SEF10-O{i}" for i in range(1, 9)])
        self.assertEqual(checksum(old_part), OLD_OUTCOME_CHECKSUM)
        blocks = assessment_blocks(completion)
        self.assertEqual(len(blocks), 4)
        self.assertEqual(
            [checksum(b) for b in blocks[:3]],
            list(OLD_ASSESSMENT_CHECKSUMS),
        )
        for index, block in enumerate(blocks[:3], start=1):
            self.assertTrue(block.startswith(f"- **SEF10-AS{index}**"))
            for name in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {name}: \S")

    def test_all_ten_outcomes_have_required_evidence_in_four_assessments(self):
        _, outcomes, _, completion = parts()
        ids = re.findall(r"(?m)^- \*\*(SEF10-O\d+):\*\*", outcomes)
        self.assertEqual(ids, [f"SEF10-O{i}" for i in range(1, 11)])
        blocks = assessment_blocks(completion)
        self.assertEqual(len(blocks), 4)
        covered: set[str] = set()
        for i, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF10-AS{i}**"))
            for name in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {name}: \S")
            claim = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(claim)
            covered.update(re.findall(r"SEF10-O\d+", claim.group(1)))
        self.assertEqual(covered, set(ids))
        self.assertIn("SEF10-O9", blocks[-1])
        self.assertIn("SEF10-O10", blocks[-1])

    def test_eight_modules_with_six_original_gates_are_sequenced(self):
        _, outcomes, modules, _ = parts()
        known = set(re.findall(r"(?m)^- \*\*(SEF10-O\d+):\*\*", outcomes))
        headings = list(re.finditer(r"(?m)^### Module (\d+) — ([^\n]+)$", modules))
        self.assertEqual([int(h.group(1)) for h in headings], list(range(1, 9)))
        self.assertEqual(tuple(h.group(2) for h in headings), HEADINGS)
        count = 0
        for i, header in enumerate(headings):
            stop = headings[i + 1].start() if i + 1 < len(headings) else len(modules)
            block = modules[header.start():stop]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            outcome_part, lessons = block.split("#### Lessons", 1)
            mapped = set(re.findall(r"(?m)^- (SEF10-O\d+)$", outcome_part))
            self.assertTrue(mapped)
            self.assertTrue(mapped.issubset(known))
            nums = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(nums)
            self.assertEqual(nums, list(range(1, len(nums) + 1)))
            count += len(nums)
        self.assertEqual(count, 66)
        gate_ids = re.findall(r"(?m)^\*\*Milestone (M[1-6]) —", modules)
        self.assertEqual(gate_ids, [f"M{i}" for i in range(1, 7)])
        self.assertIn("same project", modules.lower())

    def test_every_prior_sef_course_has_unique_explicit_evidence_role(self):
        source, _, _, _ = parts()
        table = source.split(
            "### Prerequisite closure is different from capstone integration", 1
        )[1].split("\n## Learning outcomes", 1)[0]
        matches = re.findall(
            r"(?m)^\| \[(SEF\d+)\]\((SEF\d+\.md)\) \|", table
        )
        self.assertEqual(len(matches), 10)
        self.assertEqual(
            {key for key, _ in matches},
            set(PREREQUISITES),
        )
        for key, target in matches:
            self.assertEqual(target, f"{key}.md")
            self.assertTrue((COURSE.parent / target).is_file())
        for status in (
            "Previously verified", "Directly applied here",
            "Explained transfer", "Not directly applicable",
            "Gap or unknown",
        ):
            self.assertIn(status, table)
        for topic in (
            "SEF1", "SEF2", "SEF3", "SEF4", "SEF5", "SEF6",
            "SEF7", "SEF8", "SEF9", "SEF11",
            "memory", "statistics", "invariant", "privacy",
            "not", "without requiring C code", "not applicable",
        ):
            self.assertIn(topic.lower(), table.lower())

    def test_preentry_gaps_block_graduation_not_require_specialist_features(self):
        source, _, _, completion = parts()
        self.assertIn(
            "**Prerequisites:** [SEF1](SEF1.md)–[SEF9](SEF9.md), [SEF11](SEF11.md)",
            source,
        )
        self.assertIn("**Type:** " + chr(96) + "project" + chr(96), source)
        self.assertIn("**Duration:** 10–14 weeks", source)
        self.assertIn("**Status:** " + chr(96) + "draft" + chr(96), source)
        self.assertIn("All required SEF1–SEF9 and SEF11 capabilities", source)
        as4 = assessment_blocks(completion)[-1]
        for text in (
            "same learner-owned utility", "block to entry/award",
            "independently", "without implementing unrelated C",
            "release/hold", "source course revision",
            "privacy-sensitive", "copyright/license",
            "accessibility", "unknown", "no second implementation",
            "without assistant assistance during the challenge",
        ):
            with self.subTest(text=text):
                self.assertIn(text.lower(), as4.lower())
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn(
            "| [SEF10](SEF10.md) | Software Engineering Foundations Capstone | 10–14 weeks | SEF1–SEF9, SEF11 |",
            catalog,
        )
        self.assertIn("before starting sef10, verify actual prior completion evidence", catalog.lower())

    def test_review_and_release_rubric_protect_technical_and_professional_claims(self):
        source, _, _, completion = parts()
        rubric = completion.split(
            "### Project defense and assessment rubric", 1
        )[1].split("### Formative activities and revision history", 1)[0]
        for term in (
            "Correctness and safety", "Algorithms and quantitative reasoning",
            "Graduation evidence and transfer",
            "Professional release and accessibility", "Ownership and defense",
            "revise and reassess",
        ):
            self.assertIn(term, rubric)
        self.assertIn("clean-checkout", source.lower())
        self.assertIn("a self-review is not an independent reviewer", re.sub(r"\s+", " ", source.lower()))
        self.assertIn("No paid teaching platform", source)

    def test_revision_history_declares_material_new_ids_without_retroactive_credit(self):
        source, _, _, _ = parts()
        revision = source.split(
            "### RFC 0003 graduation integration revision and historical evidence", 1
        )[1]
        for required in (
            "ef51f0a5765a5bb95ad4fdec4e2d58d64997c1b4",
            "SEF10-O1", "SEF10-O8", "SEF10-AS1", "SEF10-AS3",
            "SEF10-O9", "SEF10-O10", "SEF10-AS4",
            "not automatically", "draft",
        ):
            self.assertIn(required.lower(), revision.lower())

    def test_strict_validator_rejects_silent_loss_of_new_outcome_coverage(self):
        source, _, _, _ = parts()
        for missing in ("SEF10-O9", "SEF10-O10"):
            with self.subTest(missing=missing):
                damaged = re.sub(
                    r"(?m)^(  - Outcomes: .+)$",
                    lambda m: m.group(1).replace(", " + missing, ""),
                    source,
                )
                self.assertNotEqual(source, damaged)
                with tempfile.TemporaryDirectory() as directory:
                    copy = Path(directory) / "SEF10.md"
                    copy.write_text(damaged, encoding="utf-8")
                    run = subprocess.run(
                        [sys.executable, str(CHECKER), "--course", str(copy)],
                        cwd=ROOT, capture_output=True, text=True, check=False,
                    )
                    self.assertNotEqual(run.returncode, 0)
                    self.assertIn(missing, run.stdout + run.stderr)


if __name__ == "__main__":
    unittest.main()
