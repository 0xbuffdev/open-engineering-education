"""Current SYS prerequisite, evidence and graduation contract regressions."""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SYS = ROOT / "curriculum" / "SYS"
CATALOG = SYS / "README.md"
ORDER = ("SYS1", "SYS2", "SYS10", "SYS3", "SYS4",
         "SYS5", "SYS6", "SYS7", "SYS8", "SYS9")
PREREQUISITES = {
    "SYS1": (),
    "SYS2": ("SYS1",),
    "SYS10": ("SYS1", "SYS2"),
    "SYS3": ("SYS10",),
    "SYS4": ("SYS2", "SYS3"),
    "SYS5": ("SYS2", "SYS3"),
    "SYS6": ("SYS4", "SYS5"),
    "SYS7": ("SYS3", "SYS4"),
    "SYS8": ("SYS6", "SYS7"),
    "SYS9": tuple(x for x in ORDER if x != "SYS9"),
}


def read(path):
    return path.read_text(encoding="utf-8")


def metadata(source, name):
    match = re.search(rf"(?m)^\*\*{re.escape(name)}:\*\* (.+)$", source)
    assert match, name
    return match.group(1)


def assessment_blocks(source, code):
    section = source.split("\n## Completion requirements\n", 1)[1]
    markers = list(re.finditer(
        rf"(?m)^- \*\*({re.escape(code)}-AS\d+)\*\* — ", section
    ))
    return [
        (match.group(1), section[match.start():
         markers[i + 1].start() if i + 1 < len(markers) else len(section)])
        for i, match in enumerate(markers)
    ]


class SYSProgramConsistencyTests(unittest.TestCase):
    def test_catalog_order_and_source_metadata(self):
        catalog = read(CATALOG)
        rows = re.findall(
            r"(?m)^\| \[(SYS\d+)\]\(\1\.md\) \| ([^|]+) \| "
            r"([^|]+) \| ([^|]+) \| (.+?) \| Core · draft \|$",
            catalog,
        )
        self.assertEqual(tuple(x[0] for x in rows), ORDER)
        encountered = set()
        for code, title, duration, _prereq, kind in rows:
            with self.subTest(course=code):
                source = read(SYS / f"{code}.md")
                self.assertEqual(source.splitlines()[0], f"# {code} — {title.strip()}")
                self.assertEqual(metadata(source, "Duration"), duration.strip())
                self.assertEqual(metadata(source, "Status"),
                                 chr(96) + "draft" + chr(96))
                self.assertEqual(metadata(source, "Specification"),
                                 chr(96) + "v0.2.0" + chr(96))
                self.assertEqual(metadata(source, "Type"), kind.strip())
                if code == "SYS1":
                    self.assertIn("[SEF10](../SEF/SEF10.md)",
                                  metadata(source, "Prerequisites"))
                else:
                    refs = re.findall(
                        r"\[(SYS\d+)\]\(SYS\d+\.md\)",
                        metadata(source, "Prerequisites")
                    )
                    if code == "SYS9":
                        self.assertIn("assessed completion",
                                      metadata(source, "Prerequisites"))
                        self.assertEqual(set(refs),
                                         {"SYS1", "SYS8", "SYS10"})
                    else:
                        self.assertEqual(set(refs), set(PREREQUISITES[code]))
                self.assertTrue(set(PREREQUISITES[code]).issubset(encountered))
                encountered.add(code)
        self.assertEqual(encountered, set(ORDER))

    def test_every_outcome_has_teaching_and_summative_evidence(self):
        total_outcomes = 0
        total_assessments = 0
        for code in ORDER:
            with self.subTest(course=code):
                source = read(SYS / f"{code}.md")
                outcomes = re.findall(
                    rf"(?m)^- \*\*({re.escape(code)}-O\d+):\*\*", source
                )
                self.assertTrue(outcomes)
                self.assertEqual(outcomes,
                                 [f"{code}-O{i}" for i in
                                  range(1, len(outcomes) + 1)])
                known = set(outcomes)
                modules = source.split("\n## Modules\n", 1)[1].split(
                    "\n## Completion requirements\n", 1
                )[0]
                starts = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
                self.assertTrue(starts)
                self.assertEqual(
                    [int(m.group(1)) for m in starts],
                    list(range(1, len(starts) + 1)),
                )
                taught = set()
                for i, start in enumerate(starts):
                    end = starts[i + 1].start() if i + 1 < len(starts) else len(modules)
                    block = modules[start.start():end]
                    self.assertEqual(block.count("#### Outcomes"), 1)
                    self.assertEqual(block.count("#### Lessons"), 1)
                    targets, lessons = block.split("#### Lessons", 1)
                    refs = re.findall(rf"(?m)^- ({code}-O\d+)$", targets)
                    self.assertTrue(refs)
                    self.assertEqual(len(refs), len(set(refs)))
                    self.assertTrue(set(refs).issubset(known))
                    taught.update(refs)
                    numbered = [int(v) for v in re.findall(r"(?m)^(\d+)\. ", lessons)]
                    self.assertTrue(numbered)
                    self.assertEqual(numbered, list(range(1, len(numbered) + 1)))
                    self.assertEqual(
                        len(re.findall(r"(?m)^\d+\. \*\*.+?\*\* — \S", lessons)),
                        len(numbered),
                    )
                self.assertEqual(taught, known)
                assessments = assessment_blocks(source, code)
                self.assertTrue(assessments)
                self.assertEqual(
                    [x[0] for x in assessments],
                    [f"{code}-AS{i}" for i in range(1, len(assessments) + 1)],
                )
                covered = set()
                for id_, block in assessments:
                    self.assertTrue(id_.startswith(code + "-AS"))
                    for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                        self.assertRegex(
                            block, rf"(?m)^  - \*\*{field}:\*\* \S"
                        )
                    match = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
                    self.assertIsNotNone(match)
                    refs = set(re.findall(rf"{code}-O\d+", match.group(1)))
                    self.assertTrue(refs)
                    self.assertTrue(refs.issubset(known))
                    covered.update(refs)
                self.assertEqual(covered, known)
                self.assertNotIn("UNIX-SYS-BOUNDARY.md", source)
                self.assertNotIn("### Historical evidence", source)
                self.assertNotIn("The consolidation removes", source)
                self.assertNotRegex(source, r"\n{3,}")
                total_outcomes += len(outcomes)
                total_assessments += len(assessments)
        catalog = read(CATALOG)
        self.assertIn(
            f"**{total_outcomes} learning outcomes and "
            f"{total_assessments} required summative assessments**", catalog
        )

    def test_capstone_admission_and_graduation_are_independent(self):
        source = read(SYS / "SYS9.md")
        self.assertEqual(metadata(source, "Type"),
                         chr(96) + "project" + chr(96))
        self.assertIn("Before capstone admission", source)
        self.assertIn("**Before starting assessed implementation**", source)
        self.assertIn("**SYS1–SYS8 and SYS10**", source)
        self.assertIn("**two independent judgments**", source)
        self.assertIn("**(1)**", source)
        self.assertIn("**(2)**", source)
        first_five = assessment_blocks(source, "SYS9")[:5]
        first_coverage = set()
        for _, block in first_five:
            declaration = re.search(
                r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block
            )
            self.assertIsNotNone(declaration)
            first_coverage.update(re.findall(r"SYS9-O\d+", declaration.group(1)))
        self.assertEqual(
            first_coverage,
            {f"SYS9-O{i}" for i in range(1, 15)} -
            {"SYS9-O12", "SYS9-O14"},
        )
        as6 = assessment_blocks(source, "SYS9")[5][1]
        self.assertIn("SYS9-O12, SYS9-O14", as6)
        self.assertIn("independently derived", source)
        self.assertIn("two different relevant failure families", source)
        self.assertIn("five independent raw timed trials", source)

    def test_published_local_links_and_current_scope(self):
        self.assertFalse(
            (ROOT / "curriculum" / "SEF" / "UNIX-SYS-BOUNDARY.md").exists()
        )
        for path in [CATALOG] + [SYS / f"{code}.md" for code in ORDER]:
            with self.subTest(file=path.name):
                source = read(path)
                for href in re.findall(r"\]\(([^)\n]+)\)", source):
                    target = unquote(href.split("#", 1)[0].strip())
                    if not target.endswith(".md") or "://" in target:
                        continue
                    self.assertTrue((path.parent / target).resolve().is_file(),
                                    (path.name, href))
        catalog = read(CATALOG)
        self.assertIn("No SEF7 outcome or assessment is transferred", catalog)
        self.assertIn("**148–192 course-weeks**", catalog)
        self.assertIn("**1,480–2,880 focused hours**", catalog)
        self.assertIn("All ten courses remain educationally", catalog)


if __name__ == "__main__":
    unittest.main()
