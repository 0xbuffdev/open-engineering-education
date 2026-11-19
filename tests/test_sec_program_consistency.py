"""Program-wide checks for current SEC course contracts and public documentation.

Course sizes are derived from published sources, not prescribed quotas.
"""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEC = ROOT / "curriculum" / "SEC"
ROW = re.compile(
    r"(?m)^\| \[(SEC\d+)\]\((SEC\d+\.md)\) \| "
    r"([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$"
)


def read(path):
    return path.read_text(encoding="utf-8")


def meta(source, field):
    match = re.search(rf"(?m)^\*\*{field}:\*\* (.+)$", source)
    if match is None:
        raise AssertionError(f"Missing {field} metadata")
    return match.group(1)


class SECProgramConsistencyTests(unittest.TestCase):
    def test_current_catalog_matches_course_sources(self):
        rows = [
            tuple(cell.strip() for cell in match)
            for match in ROW.findall(read(SEC / "README.md"))
        ]
        codes = {row[0] for row in rows}
        files = {path.stem for path in SEC.glob("SEC[0-9]*.md")}
        self.assertEqual(len(rows), len(codes))
        self.assertEqual(codes, files)
        self.assertEqual(
            {row[0] for row in rows if row[-1] == chr(96) + "project" + chr(96)},
            {"SEC9"},
        )
        for code, filename, title, duration, shown_prereqs, kind in rows:
            with self.subTest(course=code):
                self.assertEqual(filename, code + ".md")
                source = read(SEC / filename)
                self.assertEqual(source.splitlines()[0], f"# {code} — {title}")
                self.assertEqual(meta(source, "Type"), kind)
                self.assertEqual(meta(source, "Duration"), duration)
                self.assertEqual(meta(source, "Status"), chr(96) + "draft" + chr(96))
                self.assertEqual(
                    meta(source, "Specification"), chr(96) + "v0.2.0" + chr(96)
                )
                linked = re.findall(
                    r"\[([A-Z]+\d+)\]\([^)]*\)",
                    meta(source, "Prerequisites"),
                )
                self.assertEqual(
                    linked, re.findall(r"[A-Z]+\d+", shown_prereqs)
                )
                self.assertNotIn("legacy", source.lower())

    def test_all_outcomes_are_taught_and_summatively_assessed(self):
        for path in sorted(SEC.glob("SEC[0-9]*.md")):
            source = read(path)
            code = path.stem
            with self.subTest(course=code):
                outcomes, tail = source.split(
                    "\n## Learning outcomes\n", 1
                )[1].split("\n## Modules\n", 1)
                modules, assessments = tail.split(
                    "\n## Completion requirements\n", 1
                )
                declared = re.findall(
                    rf"(?m)^- \*\*({code}-O\d+):\*\*", outcomes
                )
                self.assertTrue(declared)
                self.assertEqual(len(declared), len(set(declared)))
                known = set(declared)
                headings = list(re.finditer(
                    r"(?m)^### Module (\d+) — ", modules
                ))
                self.assertTrue(headings)
                self.assertEqual(
                    [int(m.group(1)) for m in headings],
                    list(range(1, len(headings) + 1)),
                )
                taught = set()
                for index, start in enumerate(headings):
                    end = (
                        headings[index + 1].start()
                        if index + 1 < len(headings)
                        else len(modules)
                    )
                    block = modules[start.start():end]
                    self.assertIn("#### Outcomes", block)
                    self.assertIn("#### Lessons", block)
                    mapping, lesson_source = block.split("#### Lessons", 1)
                    refs = re.findall(
                        rf"(?m)^- ({code}-O\d+)$", mapping
                    )
                    self.assertTrue(refs)
                    self.assertEqual(len(refs), len(set(refs)))
                    self.assertTrue(set(refs) <= known)
                    taught.update(refs)
                    numbers = [
                        int(x) for x in re.findall(
                            r"(?m)^(\d+)\. \*\*", lesson_source
                        )
                    ]
                    self.assertTrue(numbers)
                    self.assertEqual(
                        numbers, list(range(1, len(numbers) + 1))
                    )
                self.assertEqual(taught, known)

                blocks = re.split(
                    rf"(?=^- \*\*{code}-AS\d+\*\* — )",
                    assessments, flags=re.M,
                )[1:]
                self.assertTrue(blocks)
                seen = set()
                evaluated = set()
                for block in blocks:
                    head = re.match(rf"- \*\*({code}-AS\d+)\*\*", block)
                    self.assertIsNotNone(head)
                    self.assertNotIn(head.group(1), seen)
                    seen.add(head.group(1))
                    for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                        self.assertRegex(
                            block, rf"(?m)^  - \*\*{field}:\*\* \S"
                        )
                    line = re.search(
                        r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block
                    )
                    self.assertIsNotNone(line)
                    refs = set(re.findall(
                        rf"{code}-O\d+", line.group(1)
                    ))
                    self.assertTrue(refs)
                    self.assertTrue(refs <= known)
                    evaluated.update(refs)
                self.assertEqual(evaluated, known)

    def test_capstone_and_documentation_are_current(self):
        catalog = read(SEC / "README.md")
        index = read(ROOT / "curriculum" / "README.md")
        root = read(ROOT / "README.md")
        inventory = read(ROOT / "curriculum" / "INVENTORY.md")
        ai = read(ROOT / "curriculum" / "AI" / "README.md")
        capstone = read(SEC / "SEC9.md")
        self.assertIn("before admission to SEC9", catalog)
        self.assertIn("individual technical defense", catalog)
        self.assertIn("all thirteen predecessor courses", capstone)
        self.assertIn("two actual authority/enforcement layers", capstone)
        self.assertIn("65 core, 11 electives", index)
        self.assertIn("16 core, 4 electives", index)
        self.assertIn("14 core", index)
        self.assertIn("AI1–AI16 are required", ai)
        self.assertIn("AI17–AI20 are optional specializations", ai)
        self.assertIn("[SEC](curriculum/SEC/README.md)", root)
        self.assertIn("capstone", root)
        self.assertIn("# Curriculum inventory", inventory)
        for name, source in (
            ("SEC catalog", catalog),
            ("curriculum index", index),
            ("repository README", root),
            ("inventory guide", inventory),
        ):
            with self.subTest(document=name):
                self.assertNotIn("legacy", source.lower())
                self.assertNotIn("draft outlines", source.lower())
                self.assertNotIn("migration target", source.lower())


if __name__ == "__main__":
    unittest.main()
