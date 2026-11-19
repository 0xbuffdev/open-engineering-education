"""SEC direct prerequisites, inherited preparation and capstone admission."""

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"
SEC = CURRICULUM / "SEC"
CATALOG = SEC / "README.md"

LINK = re.compile(
    r"\[([A-Z]+\d+)\]\((?:\.\./[A-Z]+/)?([A-Z]+\d+)\.md\)"
)
CODE = re.compile(r"^([A-Z]+)(\d+)$")


def direct_prerequisites(course_code):
    match = CODE.fullmatch(course_code)
    if match is None:
        raise ValueError(f"Unsupported course code: {course_code}")

    path = CURRICULUM / match.group(1) / f"{course_code}.md"
    source = path.read_text(encoding="utf-8")
    header = re.search(r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
    if header is None:
        raise ValueError(f"Missing prerequisite metadata: {course_code}")
    statement = header.group(1)
    if statement.strip().lower() == "none":
        return ()

    links = list(LINK.finditer(statement))
    if not links:
        raise ValueError(f"Unrecognized prerequisites: {course_code}: {statement}")
    courses = []
    for i, link in enumerate(links):
        current, path_code = link.groups()
        if current != path_code:
            raise ValueError(f"Link label/path mismatch in {course_code}")
        if i and statement[links[i - 1].end():link.start()] == "–":
            previous = courses.pop()
            first, last = CODE.fullmatch(previous), CODE.fullmatch(current)
            if first.group(1) != last.group(1):
                raise ValueError(f"Cross-program prerequisite range: {course_code}")
            start, end = int(first.group(2)), int(last.group(2))
            if start >= end:
                raise ValueError(f"Invalid prerequisite range: {course_code}")
            courses.extend(f"{first.group(1)}{n}" for n in range(start, end + 1))
        else:
            courses.append(current)

    if len(courses) != len(set(courses)):
        raise ValueError(f"Duplicated prerequisite: {course_code}")
    for code in courses:
        found = CODE.fullmatch(code)
        if not (CURRICULUM / found.group(1) / f"{code}.md").is_file():
            raise ValueError(f"Missing prerequisite course: {course_code} -> {code}")
    return tuple(courses)


def inherited_prerequisites(course_code, trail=()):
    if course_code in trail:
        raise ValueError("Prerequisite cycle: " + " → ".join((*trail, course_code)))
    inherited = set()
    for direct in direct_prerequisites(course_code):
        inherited.add(direct)
        inherited.update(inherited_prerequisites(direct, (*trail, course_code)))
    return inherited


class SECPrerequisiteClosureTests(unittest.TestCase):
    def test_no_unnecessary_direct_edges_in_required_courses(self):
        # SEC9 is deliberately an explicit independent completion/admission gate,
        # not a topologically reduced knowledge prerequisite list.
        for path in sorted(SEC.glob("SEC[0-9]*.md")):
            if path.stem == "SEC9":
                continue
            direct = direct_prerequisites(path.stem)
            for candidate in direct:
                other_routes = set()
                for other in direct:
                    if other != candidate:
                        other_routes.add(other)
                        other_routes.update(inherited_prerequisites(other))
                self.assertNotIn(
                    candidate, other_routes,
                    f"{path.stem} needlessly lists {candidate} directly",
                )
            # Also reject cycles even where every course has only one parent.
            self.assertNotIn(path.stem, inherited_prerequisites(path.stem))

    def test_specialist_foundations_remain_verified_through_the_graph(self):
        required = {
            "SEC3": ("SEC1", "SEF10", "SEF6"),
            "SEC4": ("SEC2", "SEC1", "SEF10", "SEF7"),
            "SEC6": ("SEC4", "SEC2", "SEF7"),
            "SEC7": ("SEC6", "SEC4", "SEC2"),
            "SEC10": ("SEC4", "SEC2", "SEF7"),
        }
        exact_direct = {
            "SEC3": ("SEC1",),
            "SEC4": ("SEC2",),
            "SEC6": ("SEC4",),
            "SEC7": ("SEC6",),
            "SEC10": ("SEC4",),
        }
        for code, expected in required.items():
            self.assertEqual(direct_prerequisites(code), exact_direct[code])
            self.assertTrue(
                set(expected) <= inherited_prerequisites(code),
                f"{code} lost independently required prior preparation",
            )

    def test_catalog_lists_only_actual_direct_prerequisites(self):
        source = CATALOG.read_text(encoding="utf-8")
        found = set()
        for row in source.splitlines():
            if not row.startswith("| [SEC"):
                continue
            cells = [cell.strip() for cell in row.strip("|").split("|")]
            code = re.match(r"^\[(SEC\d+)\]\(", cells[0]).group(1)
            self.assertNotIn(code, found)
            found.add(code)
            if code == "SEC9":
                continue
            displayed = re.findall(r"[A-Z]+\d+", cells[3])
            self.assertEqual(
                list(direct_prerequisites(code)), displayed,
                f"{code}: published catalog differs from its course source",
            )

        self.assertEqual(
            found, {p.stem for p in SEC.glob("SEC[0-9]*.md")}
        )

    def test_sec9_remains_an_explicit_completion_gate(self):
        # Unlike knowledge prerequisites, every required core completion must
        # be reviewed individually before assessment of the SEC9 capstone.
        every_predecessor = {
            p.stem for p in SEC.glob("SEC[0-9]*.md")
            if p.stem != "SEC9"
        }
        self.assertEqual(
            set(direct_prerequisites("SEC9")), every_predecessor
        )
        capstone = (SEC / "SEC9.md").read_text(encoding="utf-8")
        self.assertIn(
            "independently reviewable satisfactory completion decisions",
            capstone,
        )
        self.assertIn(
            "SEC9 cannot invent credit, substitute project work",
            capstone,
        )


if __name__ == "__main__":
    unittest.main()
