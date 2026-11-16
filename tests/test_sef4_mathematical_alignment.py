"""SEF4 mathematics-to-algorithms curriculum regression tests.

The revision is instructional; original outcomes and assessments must not change.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF4.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
SEF11 = ROOT / "curriculum" / "SEF" / "SEF11.md"
SEF6 = ROOT / "curriculum" / "SEF" / "SEF6.md"
OUTCOME_CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"

# FNV-1a checksum on Unicode code points, pinned to the published requirements
# at commit c66ccd3da563fb308dd46a7ce6513d2145490040.
OUTCOME_CHECKSUM = "62d0f068"
ASSESSMENT_CHECKSUMS = (
    "4a61094c", "48006060", "381046b5", "55268446",
    "c0072188", "5c36db88", "2d99d38f",
)


def checksum(value: str) -> str:
    digest = 2166136261
    for char in value:
        digest = ((digest ^ ord(char)) * 16777619) & 0xFFFFFFFF
    return f"{digest:08x}"


def content_parts():
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
    matches = list(re.finditer(
        r"(?m)^- \*\*SEF4-AS\d+\*\* \(required ", completion
    ))
    end = completion.index("### Completion decision")
    return [
        completion[match.start():matches[i+1].start() if i+1 < len(matches) else end].rstrip()
        for i, match in enumerate(matches)
    ]


class SEF4MathAlignmentTests(unittest.TestCase):
    def test_existing_outcome_and_sef_program_validators_accept_course(self):
        for name, arguments in (
            ("check-outcome-curriculum.py", ["--course", str(COURSE)]),
            ("check-sef-curriculum.py", []),
        ):
            with self.subTest(name=name):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / name), *arguments],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_original_fourteen_outcomes_and_seven_assessments_are_unchanged(self):
        _, learning, _, completion = content_parts()
        outcome_ids = re.findall(r"(?m)^- \*\*(SEF4-O\d+):\*\*", learning)
        self.assertEqual(outcome_ids, [f"SEF4-O{i}" for i in range(1, 15)])
        self.assertEqual(checksum(learning.rstrip()), OUTCOME_CHECKSUM)
        contracts = assessment_blocks(completion)
        self.assertEqual(len(contracts), 7)
        self.assertEqual([checksum(c) for c in contracts], list(ASSESSMENT_CHECKSUMS))
        for i, contract in enumerate(contracts, start=1):
            self.assertTrue(contract.startswith(f"- **SEF4-AS{i}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(contract, rf"(?m)^  - {field}: \S")

    def test_nine_ordered_modules_teach_proof_before_search_and_sort(self):
        _, learning, modules, _ = content_parts()
        known = set(re.findall(r"(?m)^- \*\*(SEF4-O\d+):\*\*", learning))
        heads = list(re.finditer(r"(?m)^### Module (\d+) — ([^\n]+)$", modules))
        self.assertEqual([int(h.group(1)) for h in heads], list(range(1, 10)))
        self.assertEqual(heads[0].group(2), "Mathematical Reasoning for Executable Algorithms")
        self.assertEqual(heads[3].group(2), "Algorithm Correctness & Cost Arguments")
        self.assertEqual(heads[4].group(2), "Searching, Sorting & Complexity")
        self.assertEqual(heads[-1].group(2), "Algorithm Toolkit")
        for i, header in enumerate(heads):
            stop = heads[i+1].start() if i+1 < len(heads) else len(modules)
            block = modules[header.start():stop]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            references, lessons = block.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEF4-O\d+)$", references))
            self.assertTrue(refs)
            self.assertTrue(refs.issubset(known))
            sequence = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(sequence)
            self.assertEqual(sequence, list(range(1, len(sequence)+1)))

    def test_sef11_transfer_crosswalk_and_proof_method_are_explicit(self):
        source, _, modules, completion = content_parts()
        self.assertIn("**Prerequisites:** [SEF11](SEF11.md)", source)
        self.assertIn("**Duration:** 12–14 weeks", source)
        self.assertIn("**Status:** " + chr(96) + "draft" + chr(96), source)
        table = source.split("### Transfer of SEF11 mathematical readiness", 1)[1].split(
            "\n## Learning outcomes", 1
        )[0]
        for word in (
            "SEF11-O3", "SEF11-O7", "SEF11-O8", "SEF11-O9",
            "SEF4-O5", "SEF4-O7", "SEF4-O12", "SEF4-AS3",
            "not an extra entry examination", "finite oracle",
        ):
            with self.subTest(word=word):
                self.assertIn(word.lower(), table.lower())
        for word in (
            "termination variant", "recurrence", "independent oracles",
            "worst, expected and amortized",
        ):
            self.assertIn(word.lower(), modules.lower())
        self.assertIn("does not add a new rubric", completion)
        self.assertIn("all seven required assessments", completion)

    def test_existing_seven_assessments_have_an_independent_evidence_map(self):
        _, _, _, completion = content_parts()
        crosswalk = completion.split(
            "### How the existing assessments demonstrate mathematical transfer", 1
        )[1].split("### Assessment setup and evidence", 1)[0]
        for i in range(1, 8):
            with self.subTest(i=i):
                self.assertIn("| " + chr(96) + f"SEF4-AS{i}" + chr(96) + " |", crosswalk)
        for word in ("invariant", "independent", "Bellman", "DAG", "counterexample", "recurrence"):
            self.assertIn(word.lower(), crosswalk.lower())

    def test_historical_evidence_and_downstream_scope_are_respected(self):
        source, _, _, _ = content_parts()
        history = source.split("### Revision record: mathematical alignment", 1)[1].lower()
        for token in (
            "c66ccd3da563fb308dd46a7ce6513d2145490040",
            "sef4-o1", "o14", "sef4-as1", "as7",
            "not a new completion contract", "sef6", "sef10",
        ):
            self.assertIn(token, history)
        self.assertIn(
            "| [SEF4](SEF4.md) | Data Structures & Algorithms | 12–14 weeks | SEF11 |",
            CATALOG.read_text(encoding="utf-8"),
        )
        self.assertIn(
            "how [sef4](sef4.md) will apply demonstrated quantified reasoning",
            SEF11.read_text(encoding="utf-8").lower(),
        )
        self.assertIn(
            "Prior [SEF4](SEF4.md) study establishes",
            SEF6.read_text(encoding="utf-8"),
        )

    def test_unassessed_existing_outcome_is_rejected_not_silently_accepted(self):
        source, _, _, _ = content_parts()
        damaged = re.sub(
            r"(?m)^(  - Outcomes: .+)$",
            lambda m: m.group(1).replace(", SEF4-O14", "").replace("SEF4-O14, ", ""),
            source,
        )
        self.assertNotEqual(damaged, source)
        with tempfile.TemporaryDirectory() as folder:
            copied = Path(folder) / "SEF4.md"
            copied.write_text(damaged, encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(OUTCOME_CHECKER), "--course", str(copied)],
                cwd=ROOT, text=True, capture_output=True, check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("SEF4-O14", proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
