"""Source-driven SEF program/catalog consistency and public-readiness guards.

These tests apply only to the currently adopted SEF program, rather than
adding repository-wide OEE format requirements or learner-ready claims.
"""

from __future__ import annotations

from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SEF = ROOT / "curriculum" / "SEF"
CATALOG = SEF / "README.md"
PROGRAMS = ROOT / "curriculum" / "README.md"

EXPECTED_SEF_IDS = tuple(f"SEF{i}" for i in range(1, 12))
EXPECTED_STUDY_ORDER = (
    "SEF1", "SEF2", "SEF11", "SEF3", "SEF4",
    "SEF5", "SEF8", "SEF6", "SEF7", "SEF9", "SEF10",
)
EXPECTED_OUTCOME_TOTAL = 147
EXPECTED_ASSESSMENT_TOTAL = 68
EXPECTED_NOMINAL_WEEKS = (115, 143)

COURSE_ROW = re.compile(
    r"(?m)^\| \[(SEF\d+)\]\((SEF\d+\.md)\) \| "
    r"([^|]+) \| ([^|]+) \| ([^|]+) \| "
    r"(\x60course\x60|\x60project\x60) \|$"
)
OUTCOME_ID = re.compile(r"(?m)^- \*\*(SEF\d+-O\d+):\*\* ")
ASSESSMENT_HEADER = re.compile(
    r"(?m)^- \*\*(SEF\d+-AS\d+)\*\* \(required "
)


def expand_codes(value: str) -> list[str]:
    """Read catalog ranges and linked course metadata without ID reordering."""
    value = re.sub(
        r"\[SEF(\d+)\]\(SEF\d+\.md\)\s*–\s*"
        r"\[SEF(\d+)\]\(SEF\d+\.md\)",
        lambda m: f"SEF{m.group(1)}–SEF{m.group(2)}",
        value,
    )
    # Normalize ordinary linked course references before extracting codes;
    # otherwise the label and target filename would count as two courses.
    value = re.sub(
        r"\[SEF(\d+)\]\(SEF\d+\.md\)",
        lambda m: f"SEF{m.group(1)}",
        value,
    )
    value = re.sub(
        r"SEF(\d+)\s*–\s*SEF(\d+)",
        lambda m: ",".join(
            f"SEF{i}" for i in range(int(m.group(1)), int(m.group(2))+1)
        ),
        value,
    )
    return re.findall(r"SEF\d+", value)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def metadata(source: str, key: str) -> str:
    match = re.search(rf"(?m)^\*\*{re.escape(key)}:\*\* (.+)$", source)
    assert match, f"missing {key} metadata"
    return match.group(1)


def rows():
    result = []
    for m in COURSE_ROW.finditer(text(CATALOG)):
        result.append({
            "id": m.group(1),
            "path": m.group(2),
            "title": m.group(3).strip(),
            "duration": m.group(4).strip(),
            "prerequisites": m.group(5).strip(),
            "type": m.group(6),
        })
    return result


def summatives(source: str) -> list[tuple[str, str]]:
    matches = list(ASSESSMENT_HEADER.finditer(source))
    # Each course has a completion block, but most contain additional
    # non-summative teaching/revision prose after the last assessment.
    blocks = []
    for i, m in enumerate(matches):
        end = matches[i+1].start() if i+1 < len(matches) else len(source)
        blocks.append((m.group(1), source[m.start():end]))
    return blocks


class SEFProgramConsistencyTests(unittest.TestCase):
    def test_all_eleven_published_course_metadata_matches_live_catalog(self):
        catalog = rows()
        self.assertEqual(
            tuple(r["id"] for r in catalog),
            EXPECTED_STUDY_ORDER,
        )
        self.assertEqual(
            {p.name for p in SEF.glob("SEF[0-9]*.md")},
            {f"{id}.md" for id in EXPECTED_SEF_IDS},
        )
        for row in catalog:
            with self.subTest(course=row["id"]):
                self.assertEqual(row["path"], f"{row['id']}.md")
                source = text(SEF / row["path"])
                self.assertEqual(
                    metadata(source, "Prerequisites").lower() == "none",
                    row["prerequisites"] == "—",
                )
                self.assertEqual(
                    expand_codes(metadata(source, "Prerequisites")),
                    expand_codes(row["prerequisites"]),
                )
                self.assertEqual(metadata(source, "Duration"), row["duration"])
                self.assertEqual(metadata(source, "Status"), "\x60draft\x60")
                self.assertEqual(metadata(source, "Specification"), "\x60v0.2.0\x60")
                self.assertEqual(metadata(source, "Type"), row["type"])

    def test_dependency_graph_is_acyclic_and_capstone_closes_all_ten(self):
        ordered = rows()
        position = {r["id"]: i for i, r in enumerate(ordered)}
        dep = {r["id"]: expand_codes(r["prerequisites"]) for r in ordered}
        for course, prereqs in dep.items():
            self.assertEqual(len(prereqs), len(set(prereqs)))
            for before in prereqs:
                self.assertIn(before, position)
                self.assertLess(position[before], position[course])
        self.assertEqual(dep["SEF1"], [])
        self.assertEqual(dep["SEF2"], ["SEF1"])
        self.assertEqual(dep["SEF11"], ["SEF2"])
        self.assertEqual(dep["SEF4"], ["SEF11"])
        self.assertEqual(dep["SEF8"], ["SEF11"])
        self.assertEqual(dep["SEF6"], ["SEF3", "SEF4", "SEF5"])
        self.assertEqual(dep["SEF7"], ["SEF3", "SEF6"])
        self.assertEqual(dep["SEF9"], ["SEF5"])
        self.assertEqual(
            set(dep["SEF10"]),
            set(EXPECTED_SEF_IDS) - {"SEF10"},
        )

    def test_required_assessments_cover_all_147_outcomes_without_unknown_ids(self):
        course_outcomes = 0
        required_count = 0
        for row in rows():
            source = text(SEF / row["path"])
            identity = row["id"]
            course_ids = re.findall(
                rf"(?m)^- \*\*({identity}-O\d+):\*\* ",
                source,
            )
            self.assertEqual(len(course_ids), len(set(course_ids)))
            self.assertTrue(course_ids)
            course_outcomes += len(course_ids)
            summative_blocks = summatives(source)
            self.assertTrue(summative_blocks)
            block_ids = [id for id, _ in summative_blocks]
            self.assertEqual(len(block_ids), len(set(block_ids)))
            required_count += len(block_ids)
            covered = set()
            for number, block in summative_blocks:
                with self.subTest(assessment=number):
                    self.assertTrue(number.startswith(identity + "-AS"))
                    for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                        self.assertRegex(block, rf"(?m)^  - {field}: \S")
                    declared = re.search(r"(?m)^  - Outcomes: (.+)$", block)
                    self.assertIsNotNone(declared)
                    refs = set(re.findall(rf"{identity}-O\d+", declared.group(1)))
                    self.assertTrue(refs, number)
                    self.assertTrue(refs.issubset(set(course_ids)))
                    covered.update(refs)
            self.assertEqual(
                covered, set(course_ids),
                f"{identity} has missing or incorrectly claimed outcomes",
            )
        self.assertEqual(course_outcomes, EXPECTED_OUTCOME_TOTAL)
        self.assertEqual(required_count, EXPECTED_ASSESSMENT_TOTAL)

    def test_duration_sum_is_explained_without_imposing_calendar_credit(self):
        total_min = 0
        total_max = 0
        for row in rows():
            numbers = [int(x) for x in re.findall(r"\d+", row["duration"])]
            self.assertIn(len(numbers), (1, 2))
            total_min += numbers[0]
            total_max += numbers[-1]
        self.assertEqual((total_min, total_max), EXPECTED_NOMINAL_WEEKS)
        curriculum = text(CATALOG)
        for term in (
            "115–143 course-weeks", "1,150–2,145 focused hours",
            "provisional", "parallel courses",
            "147 learning outcomes", "68 required summative",
            "not an elapsed-time requirement",
        ):
            self.assertIn(term.lower(), curriculum.lower())

    def test_readme_has_nine_program_outcomes_and_navigable_study_guidance(self):
        curriculum = text(CATALOG)
        outcome_section = curriculum.split("## Learning outcomes\n", 1)[1].split(
            "\n## Program completion standard", 1
        )[0]
        outcome_lines = [
            line for line in outcome_section.splitlines()
            if line.startswith("- ")
        ]
        self.assertEqual(len(outcome_lines), 9)
        pathway = curriculum.split("## How the courses fit together\n", 1)[1].split(
            "\n## Workload and pacing", 1
        )[0]
        for course in EXPECTED_SEF_IDS:
            self.assertIn(course, pathway)
            self.assertIn(f"[{course}]({course}.md)", curriculum)
        for topic in (
            "SEF11", "SEF4", "SEF8", "SEF9", "SEF10",
            "may proceed concurrently", "bounded", "professional",
            "without", "local-loopback", "SEF7–SYS competency destination map",
        ):
            with self.subTest(topic=topic):
                self.assertIn(topic.lower(), pathway.lower())
        self.assertNotIn("MATH-MIGRATION.md", curriculum)
        self.assertIn("UNIX-SYS-BOUNDARY.md", curriculum)
        self.assertIn("../../spec/status-labels.md", curriculum)
        self.assertIn("../../spec/conformance.md", curriculum)

    def test_public_docs_point_to_current_canonical_curriculum(self):
        summaries = {
            "root": text(ROOT / "README.md"),
            "curriculum": text(PROGRAMS),
            "sef": text(CATALOG),
            "rfcs": text(ROOT / "rfcs" / "README.md"),
            "rfc_0003": text(ROOT / "rfcs" / "0003-sef-academic-progression.md"),
            "guide": text(ROOT / "curriculum" / "DESIGN-GUIDE.md"),
            "scripts": text(ROOT / "scripts" / "README.md"),
        }
        for key, source in summaries.items():
            with self.subTest(document=key):
                self.assertNotIn("under review; not merged", source.lower())
                self.assertNotIn(
                    "other sef academic hardening work proceeds",
                    source.lower(),
                )
        self.assertIn("no historical-format sef course definitions remain", summaries["sef"].lower())
        self.assertFalse((SEF / "MATH-MIGRATION.md").exists())
        for course in ("SEF8.md", "SEF11.md"):
            self.assertNotIn("MATH-MIGRATION.md", text(SEF / course))
        self.assertIn("SEF/README.md", summaries["root"])
        self.assertIn("SEF/README.md", summaries["curriculum"])
        self.assertIn("PR #101", summaries["rfc_0003"])
        self.assertIn("PR #83", summaries["rfc_0003"])
        self.assertIn("learner", summaries["rfc_0003"].lower())
        self.assertIn("**all eleven", summaries["sef"].lower())
        self.assertIn("remain `draft`", summaries["sef"].lower())

    def test_umbrella_catalog_numbers_follow_actual_live_program_rows(self):
        overview = text(PROGRAMS)
        counts = {"SEF": (11, 0), "APP": (14, 7),
                  "SYS": (10, 0), "AI": (11, 0), "SEC": (9, 0)}
        for code, (core, elective) in counts.items():
            catalog = text(ROOT / "curriculum" / code / "README.md")
            if code == "APP":
                entries = [
                    line for line in catalog.splitlines()
                    if re.match(r"^\| \[APP\d+\]\(APP\d+\.md\) \|", line)
                ]
                current_core = sum("Core · draft" in l for l in entries)
                current_elective = sum("Elective · draft" in l for l in entries)
                self.assertEqual(
                    (current_core, current_elective), (core, elective)
                )
                self.assertIn("| \x60APP\x60 | Application Engineering | 14 core, 7 electives |", overview)
            else:
                current = re.findall(
                    rf"(?m)^\| \[{code}\d+\]\({code}\d+\.md\) \|",
                    catalog,
                )
                self.assertEqual(len(current), core)
        self.assertIn(
            "| `SYS` | Systems Engineering | 10 core |",
            overview,
        )
        expected_core = sum(core for core, _ in counts.values())
        expected_electives = sum(electives for _, electives in counts.values())
        self.assertEqual((expected_core, expected_electives), (55, 7))
        self.assertIn(
            f"| **Total** | **Five programs** | "
            f"**{expected_core} core, {expected_electives} electives** |",
            overview,
        )

    def test_readiness_is_truthful_and_has_normative_sources(self):
        curriculum = text(CATALOG)
        for term in (
            "remain `draft`", "actual learner completions",
            "independent review evidence", "formal program conformance",
            "real learner experience", "not an incomplete course file",
        ):
            self.assertIn(term.lower(), curriculum.lower())
        status_spec = text(ROOT / "spec" / "status-labels.md")
        self.assertIn("At least one learner", status_spec)
        self.assertIn("At least two learners", status_spec)
        self.assertIn("not-assessed", text(ROOT / "spec" / "conformance.md"))


if __name__ == "__main__":
    unittest.main()
