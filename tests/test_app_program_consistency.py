"""Regressions for the current APP program and graduation contract."""

from pathlib import Path
import re
import sys
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "curriculum" / "APP"
sys.path.insert(0, str(ROOT / "scripts"))
from app_catalog import prerequisite_codes, read_app_catalog  # noqa: E402

TICK = chr(96)


def read(path):
    return path.read_text(encoding="utf-8")


def metadata(source, key):
    found = re.search(rf"(?m)^\*\*{re.escape(key)}:\*\* (.+)$", source)
    if found is None:
        raise AssertionError(f"Missing {key} metadata")
    return found.group(1)


def assessments(source, code):
    section = source.split("\n## Completion requirements\n", 1)[1]
    matches = list(re.finditer(
        rf"(?m)^- \*\*({re.escape(code)}-AS\d+)\*\* ", section
    ))
    return [
        (match.group(1), section[match.start():
         matches[i + 1].start() if i + 1 < len(matches) else len(section)])
        for i, match in enumerate(matches)
    ]


class APPProgramConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = read(APP / "README.md")
        cls.entries, errors = read_app_catalog(APP / "README.md")
        assert not errors, errors
        cls.by_code = {entry.code: entry for entry in cls.entries}

    def test_catalog_matches_current_course_metadata_and_order(self):
        self.assertEqual(
            {entry.code for entry in self.entries},
            {f"APP{i}" for i in range(1, 22)},
        )
        self.assertEqual(
            sum(entry.classification == "core" for entry in self.entries), 14
        )
        self.assertEqual(
            sum(entry.classification == "elective" for entry in self.entries), 7
        )
        seen = set()
        for entry in self.entries:
            with self.subTest(course=entry.code):
                course = read(APP / f"{entry.code}.md")
                self.assertEqual(
                    course.splitlines()[0], f"# {entry.code} — {entry.title}"
                )
                self.assertEqual(metadata(course, "Duration"), entry.duration)
                self.assertEqual(metadata(course, "Type"),
                                 f"{TICK}{entry.kind}{TICK}")
                self.assertEqual(metadata(course, "Status"),
                                 f"{TICK}draft{TICK}")
                self.assertEqual(metadata(course, "Specification"),
                                 f"{TICK}v0.2.0{TICK}")
                if entry.classification == "elective":
                    self.assertEqual(
                        metadata(course, "Classification"),
                        f"{TICK}elective{TICK}",
                    )
                actual = set(prerequisite_codes(
                    metadata(course, "Prerequisites")
                ))
                declared = set(prerequisite_codes(entry.prerequisites))
                self.assertEqual(actual, declared)
                self.assertTrue(actual.issubset(seen))
                if entry.classification == "core":
                    self.assertFalse(any(
                        self.by_code[dep].classification == "elective"
                        for dep in actual
                    ))
                seen.add(entry.code)
        for code in ("APP1", "APP4", "APP18"):
            self.assertIn(
                "SEF10", metadata(read(APP / f"{code}.md"), "Prerequisites")
            )

    def test_every_outcome_is_taught_and_has_required_evidence(self):
        for entry in self.entries:
            code = entry.code
            with self.subTest(course=code):
                source = read(APP / f"{code}.md")
                outcomes = re.findall(
                    rf"(?m)^- \*\*({re.escape(code)}-O\d+):\*\*", source
                )
                self.assertTrue(outcomes)
                self.assertEqual(
                    outcomes,
                    [f"{code}-O{i}" for i in range(1, len(outcomes) + 1)],
                )
                known = set(outcomes)
                module_text = source.split("\n## Modules\n", 1)[1].split(
                    "\n## Completion requirements\n", 1
                )[0]
                starts = list(re.finditer(r"(?m)^### Module (\d+) — ", module_text))
                self.assertTrue(starts)
                self.assertEqual(
                    [int(m.group(1)) for m in starts],
                    list(range(1, len(starts) + 1)),
                )
                taught = set()
                for i, start in enumerate(starts):
                    end = starts[i + 1].start() if i + 1 < len(starts) else len(module_text)
                    block = module_text[start.start():end]
                    self.assertEqual(block.count("#### Outcomes"), 1)
                    self.assertEqual(block.count("#### Lessons"), 1)
                    targets, lesson_text = block.split("#### Lessons", 1)
                    ids = re.findall(
                        rf"(?m)^- ({re.escape(code)}-O\d+)$", targets
                    )
                    self.assertTrue(ids)
                    self.assertEqual(len(ids), len(set(ids)))
                    self.assertTrue(set(ids).issubset(known))
                    taught.update(ids)
                    lessons = [
                        int(v) for v in re.findall(
                            r"(?m)^(\d+)\. ", lesson_text
                        )
                    ]
                    self.assertTrue(lessons)
                    self.assertEqual(lessons, list(range(1, len(lessons) + 1)))
                self.assertEqual(taught, known)
                required = assessments(source, code)
                self.assertTrue(required)
                self.assertEqual(
                    [aid for aid, _ in required],
                    [f"{code}-AS{i}" for i in range(1, len(required) + 1)],
                )
                measured = set()
                for aid, block in required:
                    for name in ("Outcomes", "Work", "Criteria", "Evidence"):
                        self.assertRegex(
                            block,
                            rf"(?m)^  - (?:\*\*)?{name}:(?:\*\*)? \S",
                            f"{aid}: missing {name.lower()}",
                        )
                    line = re.search(
                        r"(?m)^  - (?:\*\*)?Outcomes:(?:\*\*)? (.+)$",
                        block,
                    )
                    self.assertIsNotNone(line, aid)
                    ids = set(re.findall(
                        rf"{re.escape(code)}-O\d+", line.group(1)
                    ))
                    self.assertTrue(ids, aid)
                    self.assertTrue(ids.issubset(known), aid)
                    measured.update(ids)
                self.assertEqual(measured, known)

    def test_capstone_entry_is_separate_from_graduation_evidence(self):
        required_core = {
            entry.code for entry in self.entries
            if entry.classification == "core" and entry.code != "APP9"
        }
        electives = {
            entry.code for entry in self.entries
            if entry.classification == "elective"
        }
        capstone = self.by_code["APP9"]
        self.assertEqual(capstone.kind, "project")
        self.assertEqual(
            set(prerequisite_codes(capstone.prerequisites)), required_core
        )
        self.assertTrue(required_core.isdisjoint(electives))
        source = read(APP / "APP9.md")
        self.assertEqual(
            set(prerequisite_codes(metadata(source, "Prerequisites"))),
            required_core,
        )
        self.assertIn("Before starting Module 1", source)
        self.assertIn("assessed completion", source)
        self.assertEqual(len(assessments(source, "APP9")), 8)
        self.assertIn("unfamiliar", source.lower())
        self.assertIn("independent", source.lower())
        self.assertIn("Electives provide optional specialization", self.catalog)
        graduate_outcomes = self.catalog.split(
            "\n## Learning outcomes\n", 1
        )[1].split("\n## Program completion standard\n", 1)[0]
        self.assertNotIn("realtime features", graduate_outcomes.lower())

    def test_course_links_and_public_documentation(self):
        for entry in self.entries:
            path = APP / f"{entry.code}.md"
            source = read(path)
            with self.subTest(course=entry.code):
                for href in re.findall(r"\]\(([^)\n]+)\)", source):
                    target = unquote(href.split("#", 1)[0].strip())
                    if "://" in target or not target.endswith(".md"):
                        continue
                    self.assertTrue(
                        (path.parent / target).resolve().is_file(),
                        (path.name, href),
                    )
                self.assertNotRegex(
                    source.lower(),
                    r"legacy (?:seven|eight|nine|checkpoint|course|format)",
                )
        self.assertNotIn("migration target", self.catalog)
        self.assertIn("**174–228 course-weeks**", self.catalog)
        self.assertIn("**1740–3420 focused course-hours**", self.catalog)


if __name__ == "__main__":
    unittest.main()
