"""SEF7 foundational Unix scope and SYS destination-map regression checks.

SEF7 changes instruction only: the full historical outcome and assessment
contract must remain available until separately reviewed SYS migration.
"""

from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SEF7 = ROOT / "curriculum" / "SEF" / "SEF7.md"
BOUNDARY = ROOT / "curriculum" / "SEF" / "UNIX-SYS-BOUNDARY.md"
SEF_CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
SYS_CATALOG = ROOT / "curriculum" / "SYS" / "README.md"
OUTCOME_CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"

# Original published requirement identity at commit
# 635661746826e00751315a42ec39c4938f417f67.
PRIOR_OUTCOMES = "18ab4131"
PRIOR_ASSESSMENTS = (
    "54945074", "ff29d0df", "5f7a4b0f", "88ea06dd",
    "47f57310", "e95b0b86", "2fedbd2e",
)



def checksum(text: str) -> str:
    digest = 2166136261
    for char in text:
        digest = ((digest ^ ord(char)) * 16777619) & 0xFFFFFFFF
    return f"{digest:08x}"


def sections():
    text = SEF7.read_text(encoding="utf-8")
    outcomes = text.split("\n## Learning outcomes\n", 1)[1].split(
        "\n## Modules\n", 1
    )[0]
    modules = text.split("\n## Modules\n", 1)[1].split(
        "\n## Completion requirements\n", 1
    )[0]
    assessed = text.split("\n## Completion requirements\n", 1)[1]
    return text, outcomes, modules, assessed


def assessment_blocks(completion: str) -> list[str]:
    markers = list(re.finditer(
        r"(?m)^- \*\*SEF7-AS\d+\*\* \(required ", completion
    ))
    end = completion.index("### Completion decision")
    return [
        completion[match.start():markers[i + 1].start() if i + 1 < len(markers) else end].rstrip()
        for i, match in enumerate(markers)
    ]


class SEF7AcademicBoundaryTests(unittest.TestCase):
    def test_current_course_and_program_validators_pass(self):
        for script, additional in (
            ("check-outcome-curriculum.py", ["--course", str(SEF7)]),
            ("check-sef-curriculum.py", []),
        ):
            with self.subTest(script=script):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "scripts" / script), *additional],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr or proc.stdout)

    def test_historical_fourteen_outcomes_and_seven_summatives_unchanged(self):
        _, defined, _, assessed = sections()
        self.assertEqual(
            re.findall(r"(?m)^- \*\*(SEF7-O\d+):\*\*", defined),
            [f"SEF7-O{i}" for i in range(1, 15)],
        )
        self.assertEqual(checksum(defined.rstrip()), PRIOR_OUTCOMES)
        blocks = assessment_blocks(assessed)
        self.assertEqual(len(blocks), 7)
        self.assertEqual([checksum(block) for block in blocks], list(PRIOR_ASSESSMENTS))
        covered = set()
        for index, block in enumerate(blocks, start=1):
            self.assertTrue(block.startswith(f"- **SEF7-AS{index}**"))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            declaration = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(declaration)
            covered.update(re.findall(r"SEF7-O\d+", declaration.group(1)))
        self.assertEqual(covered, {f"SEF7-O{i}" for i in range(1, 15)})

    def test_instructional_sequence_is_derived_from_outcome_prerequisites(self):
        _, defined, modules, _ = sections()
        known = set(re.findall(r"(?m)^- \*\*(SEF7-O\d+):\*\*", defined))
        heads = list(re.finditer(r"(?m)^### Module (\d+) — ([^\n]+)$", modules))
        self.assertTrue(heads)
        self.assertEqual(
            [int(m.group(1)) for m in heads],
            list(range(1, len(heads) + 1)),
        )
        first = {}
        for i, head in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(modules)
            content = modules[head.start():end]
            self.assertEqual(content.count("#### Outcomes"), 1)
            self.assertEqual(content.count("#### Lessons"), 1)
            mapped, lessons = content.split("#### Lessons", 1)
            ids = re.findall(r"(?m)^- (SEF7-O\d+)$", mapped)
            self.assertTrue(ids)
            self.assertEqual(len(ids), len(set(ids)))
            self.assertTrue(set(ids).issubset(known))
            for id_ in ids:
                first.setdefault(id_, i)
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
            # Real lessons name an objective and its observable task, not
            # an unqualified list of Unix interface terms.
            self.assertEqual(
                len(re.findall(r"(?m)^\d+\. \*\*.+?\*\* — \S", lessons)),
                len(numbers),
            )
        self.assertEqual(set(first), known)
        for earlier, later in (
            ("SEF7-O1", "SEF7-O7"),   # descriptor semantics before pipes
            ("SEF7-O2", "SEF7-O7"),   # shared handles before pipe EOF
            ("SEF7-O3", "SEF7-O7"),   # child/wait before two-child IPC
            ("SEF7-O8", "SEF7-O9"),   # blocking protocol before nonblocking
            ("SEF7-O9", "SEF7-O13"),  # finite deadlines before integration
            ("SEF7-O7", "SEF7-O13"),  # IPC before integration
            ("SEF7-O6", "SEF7-O13"),  # safe traversal before integration
        ):
            with self.subTest(prerequisite=f"{earlier}->{later}"):
                self.assertLess(first[earlier], first[later])

        # Identity and directory traversal belong to one coherent stage.
        # Verify actual intra-module preparation rather than artificially
        # forcing them into two separate modules.
        self.assertLess(
            modules.index("**Pathnames versus object identity**"),
            modules.index("**Owned DIR streams and readdir errors**"),
        )
        self.assertLess(
            modules.index("**Owned DIR streams and readdir errors**"),
            modules.index("**Directory-relative identity checks**"),
        )

    def test_version_aware_posix_failures_and_downstream_sys_are_accurate(self):
        source, _, modules, _ = sections()
        for topic in (
            "FD_CLOEXEC", "open-file description", "waitpid", "sig_atomic_t",
            "lstat", "fstatat", "readdir", "SIGPIPE", "EINTR", "EAGAIN",
            "CLOCK_MONOTONIC", "127.0.0.1", "poll", "partial",
            "independent", "deadline", "close", "SO_ERROR", "errno",
            "Linux", "POSIX.1-2024", "POLLHUP", "TOCTOU",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic.lower(), (source + modules).lower())
        self.assertIn("All ten published SYS courses now", source)
        self.assertIn("not an enacted assessment migration", source)
        self.assertIn("draft", source.lower())

    def test_complete_explicit_mapping_to_real_SYS_files_and_no_auto_credit(self):
        mapping = BOUNDARY.read_text(encoding="utf-8")
        outcome_table = mapping.split(
            "## Explicit mapping of every existing SEF7 learning outcome", 1
        )[1].split("## Explicit mapping of every existing SEF7 assessment", 1)[0]
        assessment_table = mapping.split(
            "## Explicit mapping of every existing SEF7 assessment", 1
        )[1].split("## Preconditions for any future transfer", 1)[0]
        for i in range(1, 15):
            with self.subTest(outcome=i):
                self.assertEqual(
                    outcome_table.count(f"| {chr(96)}SEF7-O{i}{chr(96)} |"), 1
                )
        for i in range(1, 8):
            with self.subTest(assessment=i):
                self.assertEqual(
                    assessment_table.count(f"| {chr(96)}SEF7-AS{i}{chr(96)} |"), 1
                )
        for section in (outcome_table, assessment_table):
            lines = [
                line for line in section.splitlines()
                if re.match(r"^\| \x60SEF7-(?:O|AS)\d+\x60 \|", line)
            ]
            self.assertTrue(lines)
            for line in lines:
                paths = re.findall(
                    r"\[SYS(\d+)\]\(\.\./SYS/(SYS\d+\.md)\)", line
                )
                self.assertTrue(paths, line)
                for n, filename in paths:
                    self.assertEqual(filename, f"SYS{n}.md")
                    self.assertTrue(
                        (ROOT / "curriculum" / "SYS" / filename).exists()
                    )
        for phrase in (
            "v0.2.0", "draft",
            "not an enacted transfer or assessment migration",
            "No SEF7 requirement may be removed",
            "C/Rust comparison", "Rust", "separately approved",
        ):
            self.assertIn(phrase.lower(), mapping.lower())
        sys_catalog = SYS_CATALOG.read_text(encoding="utf-8")
        self.assertIn("All ten courses remain educationally `draft`", sys_catalog)
        self.assertIn(
            "no sef7 outcome or assessment is transferred",
            sys_catalog.lower(),
        )
        # Migration changes source format, not historical SEF7 completion.
        self.assertEqual(
            len(re.findall(r"(?m)^\| \[SYS\d+\]\(SYS\d+\.md\) \|", sys_catalog)),
            10,
        )
        self.assertIn("[SYS10](SYS10.md)", sys_catalog)

    def test_non_normative_SYS_handoff_preserves_C_and_single_peer_SEF(self):
        source, _, modules, _ = sections()
        self.assertIn("**Duration:** 12–16 weeks", source)
        self.assertIn("**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)", source)
        self.assertIn("**Status:** " + chr(96) + "draft" + chr(96), source)
        self.assertIn("Rust is not silently introduced", source)
        for topic in (
            "FD_CLOEXEC", "open-file description", "waitpid", "sig_atomic_t",
            "lstat", "fstatat", "readdir", "SIGPIPE", "EINTR", "EAGAIN",
            "CLOCK_MONOTONIC", "127.0.0.1", "poll", "partial",
            "independent", "deadline",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic.lower(), modules.lower())
        self.assertIn("Linux/POSIX.1-2024 divergence", source)
        self.assertIn("same seven required summative assessments", source.lower())
        self.assertIn(
            "| [SEF7](SEF7.md) | Unix System Interfaces | 12–16 weeks |",
            SEF_CATALOG.read_text(encoding="utf-8"),
        )
        self.assertIn(
            "[SEF7–SYS boundary map](../SEF/UNIX-SYS-BOUNDARY.md)",
            SYS_CATALOG.read_text(encoding="utf-8"),
        )

    def test_original_evidence_crosswalk_and_revision_are_explicit(self):
        source, _, _, completion = sections()
        table = completion.split(
            "### Existing assessment evidence by instructional stage", 1
        )[1].split("### Assessment environment and evaluation", 1)[0]
        for i in range(1, 8):
            self.assertIn(
                "| " + chr(96) + f"SEF7-AS{i}" + chr(96) + " |", table
            )
        revision = source.split(
            "### Historical evidence and SEF/SYS transition", 1
        )[1]
        for word in (
            "635661746826e00751315a42ec39c4938f417f67",
            "SEF7-O1", "SEF7-O14", "SEF7-AS1", "SEF7-AS7",
            "not an enacted transfer", "Rust", "No", "draft",
        ):
            self.assertIn(word.lower(), revision.lower())

    def test_removing_a_historical_outcome_from_summatives_is_rejected(self):
        original, _, _, _ = sections()
        broken = re.sub(
            r"(?m)^(  - Outcomes: .+)$",
            lambda match: match.group(1).replace(", SEF7-O14", "").replace(
                "SEF7-O14, ", ""
            ),
            original,
        )
        self.assertNotEqual(broken, original)
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "SEF7.md"
            target.write_text(broken, encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(OUTCOME_CHECKER), "--course", str(target)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("SEF7-O14", proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
