"""SEF7 C/POSIX competency and current SYS boundary regressions."""

from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEF" / "SEF7.md"
SEF_CATALOG = ROOT / "curriculum" / "SEF" / "README.md"
SYS_CATALOG = ROOT / "curriculum" / "SYS" / "README.md"
OUTCOME_CHECKER = ROOT / "scripts" / "check-outcome-curriculum.py"


def sections():
    source = COURSE.read_text(encoding="utf-8")
    outcomes = source.split("\n## Learning outcomes\n", 1)[1].split(
        "\n## Modules\n", 1
    )[0]
    modules = source.split("\n## Modules\n", 1)[1].split(
        "\n## Completion requirements\n", 1
    )[0]
    completion = source.split("\n## Completion requirements\n", 1)[1]
    return source, outcomes, modules, completion


class SEF7AcademicBoundaryTests(unittest.TestCase):
    def test_current_course_and_program_validators_pass(self):
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

    def test_all_fourteen_outcomes_have_required_assessment_evidence(self):
        _, definitions, _, completion = sections()
        known = set(re.findall(r"(?m)^- \*\*(SEF7-O\d+):\*\*", definitions))
        self.assertEqual(known, {f"SEF7-O{i}" for i in range(1, 15)})
        markers = list(re.finditer(
            r"(?m)^- \*\*(SEF7-AS\d+)\*\* \(required ", completion
        ))
        self.assertEqual([m.group(1) for m in markers],
                         [f"SEF7-AS{i}" for i in range(1, 8)])
        covered = set()
        end = completion.index("### Completion decision")
        for i, marker in enumerate(markers):
            boundary = markers[i + 1].start() if i + 1 < len(markers) else end
            block = completion[marker.start():boundary]
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - {field}: \S")
            mapped = re.search(r"(?m)^  - Outcomes: (.+)$", block)
            self.assertIsNotNone(mapped)
            refs = set(re.findall(r"SEF7-O\d+", mapped.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs.issubset(known))
            covered.update(refs)
        self.assertEqual(covered, known)

    def test_module_sequence_teaches_all_outcomes(self):
        _, definitions, modules, _ = sections()
        known = set(re.findall(r"(?m)^- \*\*(SEF7-O\d+):\*\*", definitions))
        heads = list(re.finditer(r"(?m)^### Module (\d+) — [^\n]+$", modules))
        self.assertTrue(heads)
        self.assertEqual(
            [int(x.group(1)) for x in heads], list(range(1, len(heads) + 1))
        )
        covered = set()
        for i, head in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(modules)
            section = modules[head.start():end]
            self.assertEqual(section.count("#### Outcomes"), 1)
            self.assertEqual(section.count("#### Lessons"), 1)
            mapped, lessons = section.split("#### Lessons", 1)
            refs = re.findall(r"(?m)^- (SEF7-O\d+)$", mapped)
            self.assertTrue(set(refs).issubset(known))
            covered.update(refs)
            numbers = [int(n) for n in re.findall(r"(?m)^(\d+)\. ", lessons)]
            self.assertTrue(numbers)
            self.assertEqual(numbers, list(range(1, len(numbers) + 1)))
        self.assertEqual(covered, known)

    def test_active_sef_to_sys_boundary_requires_separate_completion(self):
        source, _, modules, _ = sections()
        sef = SEF_CATALOG.read_text(encoding="utf-8")
        sys_catalog = SYS_CATALOG.read_text(encoding="utf-8")
        self.assertIn("No SEF7 outcome or assessment is transferred", source)
        self.assertIn("No SEF7 outcome or assessment is transferred", sys_catalog)
        self.assertIn("SEF7 remains responsible for its own assessed outcomes", sef)
        self.assertFalse(
            (ROOT / "curriculum" / "SEF" / "UNIX-SYS-BOUNDARY.md").exists()
        )
        for topic in (
            "FD_CLOEXEC", "open-file description", "waitpid", "sig_atomic_t",
            "lstat", "fstatat", "readdir", "SIGPIPE", "EINTR", "EAGAIN",
            "CLOCK_MONOTONIC", "127.0.0.1", "poll", "partial",
            "deadline", "close", "SO_ERROR", "errno",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic.lower(), (source + modules).lower())
        self.assertIn("**Duration:** 12–16 weeks", source)
        self.assertIn("**Prerequisites:** [SEF3](SEF3.md), [SEF6](SEF6.md)",
                      source)
        self.assertIn("**Status:**", source)
        self.assertIn("[SYS2](SYS2.md)", sys_catalog)
        self.assertIn("[SYS10](SYS10.md)", sys_catalog)

    def test_uncovered_required_outcome_is_rejected(self):
        original, _, _, _ = sections()
        broken = re.sub(
            r"(?m)^(  - Outcomes: .+)$",
            lambda match: match.group(1).replace(", SEF7-O14", "").replace(
                "SEF7-O14, ", ""
            ),
            original,
        )
        self.assertNotEqual(broken, original)
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "SEF7.md"
            target.write_text(broken, encoding="utf-8")
            proc = subprocess.run(
                [sys.executable, str(OUTCOME_CHECKER), "--course", str(target)],
                cwd=ROOT, capture_output=True, text=True, check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("SEF7-O14", proc.stderr + proc.stdout)


if __name__ == "__main__":
    unittest.main()
