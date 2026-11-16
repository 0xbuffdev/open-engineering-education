"""SEF6 C11 language, memory safety and library instructional progression guards.

The learning sequence changes; original outcomes and assessed evidence do not.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEF6 = ROOT / "curriculum" / "SEF" / "SEF6.md"
SEF7 = ROOT / "curriculum" / "SEF" / "SEF7.md"
CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"

# FNV-1a checksums of published requirements at
# 922dbe11fd7968097d1b8711ef6f59b763fc0b17.
OLD_OUTCOMES = "935fe456"
OLD_ASSESSMENTS = (
    "0b6c813c", "99e8c1bd", "75d85d76", "2626ebf0",
    "84dd7925", "2026f5bc", "b3898d17",
)

EXPECTED_HEADINGS = (
    "C Programs, Types and Control Flow",
    "Object Representation, Integer Conversions and Checked Arithmetic",
    "Functions, Interfaces and Translation Units",
    "Compiler Diagnostics, Debugging and Defined Test Fixtures",
    "Pointers, Arrays, Strings and Object Bounds",
    "Defined, Unspecified, Implementation-Defined and Undefined C Behavior",
    "Storage Duration, Allocation, Reallocation and Cleanup",
    "Structures, Layout and C Standard-Library I/O",
    "Resource Ownership and Public C API Contracts",
    "Bounded Text and Binary Parsers",
    "Owned Integer Dynamic Arrays and Linked Lists",
    "Hash Maps, Collisions and Adversarial Allocation Tests",
    "Integrated C11 Data-Structure Library and Engineering Defense",
)


def fnv1a(text: str) -> str:
    result = 2166136261
    for character in text:
        result = ((result ^ ord(character)) * 16777619) & 0xFFFFFFFF
    return f"{result:08x}"


def parts() -> tuple[str, str, str, str]:
    source = SEF6.read_text(encoding="utf-8")
    outcomes = source.split("\n## Learning outcomes\n", 1)[1].split(
        "\n## Modules\n", 1
    )[0]
    modules = source.split("\n## Modules\n", 1)[1].split(
        "\n## Completion requirements\n", 1
    )[0]
    completion = source.split("\n## Completion requirements\n", 1)[1]
    return source, outcomes, modules, completion


def required_assessment_blocks(source: str) -> list[str]:
    matches = list(re.finditer(
        r"(?m)^- \*\*SEF6-AS\d+\*\* \(required ", source
    ))
    cutoff = source.index("### Completion decision")
    return [
        source[m.start():matches[i+1].start() if i+1 < len(matches) else cutoff].rstrip()
        for i, m in enumerate(matches)
    ]


class SEF6AcademicProgressionTests(unittest.TestCase):
    def test_strict_course_and_program_validators_accept_revision(self):
        for script, args in (
            ("check-outcome-curriculum.py", ["--course", str(SEF6)]),
            ("check-sef-curriculum.py", []),
        ):
            with self.subTest(script=script):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / script), *args],
                    cwd=ROOT, text=True, capture_output=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr or result.stdout)

    def test_existing_sixteen_outcomes_and_seven_assessment_contracts_unchanged(self):
        _, outcomes, _, completion = parts()
        ids = re.findall(r"(?m)^- \*\*(SEF6-O\d+):\*\*", outcomes)
        self.assertEqual(ids, [f"SEF6-O{i}" for i in range(1, 17)])
        self.assertEqual(fnv1a(outcomes.rstrip()), OLD_OUTCOMES)
        blocks = required_assessment_blocks(completion)
        self.assertEqual(len(blocks), 7)
        self.assertEqual([fnv1a(block) for block in blocks], list(OLD_ASSESSMENTS))
        claimed = set()
        for i, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF6-AS{i}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            declared = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(declared)
            claimed.update(re.findall(r"SEF6-O\d+", declared.group(1)))
        self.assertEqual(claimed, set(ids))

    def test_thirteen_modules_have_distinct_sequence_and_complete_lessons(self):
        _, outcomes, modules, _ = parts()
        known = set(re.findall(r"(?m)^- \*\*(SEF6-O\d+):\*\*", outcomes))
        headers = list(re.finditer(r"(?m)^### Module (\d+) — (.+)$", modules))
        self.assertEqual([int(h.group(1)) for h in headers], list(range(1, 14)))
        self.assertEqual(tuple(h.group(2) for h in headers), EXPECTED_HEADINGS)
        lesson_total = 0
        for i, h in enumerate(headers):
            end = headers[i+1].start() if i+1 < len(headers) else len(modules)
            block = modules[h.start():end]
            self.assertEqual(block.count("#### Outcomes"), 1)
            self.assertEqual(block.count("#### Lessons"), 1)
            references, lessons = block.split("#### Lessons", 1)
            found = set(re.findall(r"(?m)^- (SEF6-O\d+)$", references))
            self.assertTrue(found)
            self.assertTrue(found.issubset(known))
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers)+1)))
            lesson_total += len(numbers)
        self.assertEqual(lesson_total, 138)

    def test_safety_topics_taught_before_ownership_heavy_library_implementations(self):
        _, _, modules, _ = parts()
        self.assertLess(modules.index("### Module 4 — Compiler Diagnostics"),
                        modules.index("### Module 7 — Storage Duration"))
        self.assertLess(modules.index("### Module 6 — Defined, Unspecified"),
                        modules.index("### Module 7 — Storage Duration"))
        self.assertLess(modules.index("### Module 9 — Resource Ownership"),
                        modules.index("### Module 11 — Owned Integer"))
        self.assertLess(modules.index("### Module 10 — Bounded Text"),
                        modules.index("### Module 13 — Integrated C11"))
        for topic in (
            "CHAR_BIT", "strtol", "errno", "realloc", "unsigned char",
            "C11", "POSIX", "one-past", "signed overflow",
            "pointer", "fgets", "size_t", "padding", "aliasing",
            "allocation-failure", "linked-list", "hash", "collision",
            "C/Python", "sanitizer", "independent state-model",
            "object lifetime",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic.lower(), modules.lower())

    def test_no_new_completion_gate_and_existing_crosswalk_is_complete(self):
        source, _, _, completion = parts()
        self.assertIn("**Duration:** 14–18 weeks", source)
        self.assertIn(
            "**Prerequisites:** [SEF3](SEF3.md), [SEF4](SEF4.md), [SEF5](SEF5.md)",
            source,
        )
        self.assertIn("**Status:** " + chr(96) + "draft" + chr(96), source)
        self.assertIn("The **same seven required summative assessments**", source)
        self.assertIn("not a new grading contract", completion)
        self.assertIn("The thirteen learning modules", completion)
        table = completion.split(
            "### Teaching sequence and existing assessment alignment", 1
        )[1].split("### Assessment environment and review", 1)[0]
        for number in range(1, 8):
            self.assertIn(
                "| " + chr(96) + f"SEF6-AS{number}" + chr(96) + " |", table
            )
        self.assertIn(
            "| [SEF6](SEF6.md) | C Programming & Machine Memory | 14–18 weeks |",
            CATALOG.read_text(encoding="utf-8"),
        )
        self.assertIn("SEF6 also establishes", SEF7.read_text(encoding="utf-8"))

    def test_historical_revision_unchanged_and_tools_optional(self):
        source, _, _, completion = parts()
        history = source.split(
            "### Historical revision and learner evidence compatibility", 1
        )[1]
        for text in (
            "922dbe11fd7968097d1b8711ef6f59b763fc0b17",
            "SEF6-O1", "SEF6-O16",
            "SEF6-AS1", "SEF6-AS7", "no second assessed library",
            "neither revoked nor automatically regraded",
        ):
            self.assertIn(text.lower(), history.lower())
        for phrase in (
            "no sanitizer or debugger is assumed available",
            "No change is made to SEF3/SEF4/SEF5 prerequisite codes",
            "No independent new outcome or additional assessment has been introduced.",
        ):
            self.assertIn(phrase.lower(), source.lower())
        self.assertIn("A free offline source/build path is required", completion)

    def test_silently_unassessed_existing_outcome_fails_strict_validation(self):
        source, _, _, _ = parts()
        damaged = re.sub(
            r"(?m)^(  - Outcomes: .+)$",
            lambda match: match.group(1).replace(", SEF6-O16", "").replace(
                "SEF6-O16, ", ""
            ),
            source,
        )
        self.assertNotEqual(damaged, source)
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "SEF6.md"
            target.write_text(damaged, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(CHECKER), "--course", str(target)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("SEF6-O16", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
