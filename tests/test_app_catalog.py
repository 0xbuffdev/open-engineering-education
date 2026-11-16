"""Regression coverage for APP's canonical, ordered Markdown catalog."""

from __future__ import annotations

import contextlib
import importlib.util
import io
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from app_catalog import prerequisite_codes, read_app_catalog  # noqa: E402


def load_app_validator():
    spec = importlib.util.spec_from_file_location(
        "app_catalog_validation_test", SCRIPTS / "check-app-curriculum.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def new_outcome_course(code: str, title: str, duration: str) -> str:
    """Minimal structural v0.2.0 course with one required evaluation."""
    return f"""# {code} — {title}

**Program:** APP — Application Engineering
**Classification:** \x60core\x60
**Type:** \x60course\x60
**Prerequisites:** [APP1](APP1.md)
**Duration:** {duration}
**Status:** \x60draft\x60
**Specification:** \x60v0.2.0\x60

## Overview

Explain, build and inspect an independent engineering capability.

## Learning outcomes

- **{code}-O1:** Explain a relevant mechanism and reproduce an observation.

## Modules

### Module 1 — Independent Investigation

#### Outcomes

- {code}-O1

#### Lessons

1. Core mechanism
2. Trace an example
3. Review the result

## Completion requirements

- **{code}-AS1** (required reproducible investigation)
  - Outcomes: {code}-O1
  - Work: reproduce the result and explain the reasoning.
  - Criteria: correct observation and a justified explanation.
  - Evidence: an inspectable artifact and reproduction instructions.
"""


class APPCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = load_app_validator()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "curriculum", self.root / "curriculum")
        shutil.copytree(ROOT / "spec", self.root / "spec")
        self.app.ROOT = self.root
        self.app.APP = self.root / "curriculum" / "APP"
        self.catalog = self.app.APP / "README.md"
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        self.future_code = f"APP{max(int(entry.code[3:]) for entry in entries) + 1}"

    def change_catalog(self, before: str, after: str):
        data = self.catalog.read_text(encoding="utf-8")
        self.assertIn(before, data)
        self.catalog.write_text(data.replace(before, after, 1), encoding="utf-8")

    def change_course(self, code: str, before: str, after: str):
        path = self.app.APP / f"{code}.md"
        data = path.read_text(encoding="utf-8")
        self.assertIn(before, data)
        path.write_text(data.replace(before, after, 1), encoding="utf-8")

    def check(self) -> tuple[int, str]:
        error = io.StringIO()
        with contextlib.redirect_stderr(error), contextlib.redirect_stdout(io.StringIO()):
            status = self.app.validate()
        return status, error.getvalue()

    def add_future_core_course(self, link_capstone: bool):
        """Introduce a fresh core ID without assuming any published ID is unused."""
        code = self.future_code
        title = "Hypothetical Core Test Course"
        row = (
            f"| [{code}]({code}.md) | {title} | 8 weeks | APP1 | "
            "`course` | Core · draft |\n"
        )
        cat = self.catalog.read_text(encoding="utf-8")
        cap_line = next(x for x in cat.splitlines() if x.startswith("| [APP9]("))
        self.assertIn(cap_line, cat)
        cat = cat.replace(cap_line, row + cap_line, 1)
        if link_capstone:
            updated = cap_line.replace(
                " | `project` |", f", {code} | `project` |", 1
            )
            self.assertNotEqual(cap_line, updated)
            cat = cat.replace(cap_line, updated, 1)
            app9 = self.app.APP / "APP9.md"
            data = app9.read_text(encoding="utf-8")
            old_meta = next(
                line for line in data.splitlines()
                if line.startswith("**Prerequisites:**")
            )
            data = data.replace(
                old_meta, old_meta + f", [{code}]({code}.md)", 1
            )
            app9.write_text(data, encoding="utf-8")
        self.catalog.write_text(cat, encoding="utf-8")
        (self.app.APP / f"{code}.md").write_text(
            new_outcome_course(code, title, "8 weeks"),
            encoding="utf-8",
        )

    def test_current_catalog_passes(self):
        status, errors = self.check()
        self.assertEqual(status, 0, errors)

    def test_app17_is_core_immediately_after_app1_and_versioned(self):
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        self.assertEqual([entry.code for entry in entries[:2]], ["APP1", "APP17"])
        app17 = next(entry for entry in entries if entry.code == "APP17")
        self.assertEqual((app17.title, app17.kind, app17.classification, app17.status),
                         ("HTML & CSS Engineering", "course", "core", "draft"))
        self.assertEqual(prerequisite_codes(app17.prerequisites), ["APP1"])
        source = (self.app.APP / "APP17.md").read_text(encoding="utf-8")
        self.assertIn("**Specification:** `v0.2.0`", source)
        self.assertIn("**Classification:** `core`", source)
        capstone = next(entry for entry in entries if entry.code == "APP9")
        self.assertIn("APP17", prerequisite_codes(capstone.prerequisites))
        self.assertIn("[APP17](APP17.md)",
                      (self.app.APP / "APP9.md").read_text(encoding="utf-8"))

    def test_app20_react_core_requires_app2_without_backend_runtime(self):
        # APP20 is a React client-application course, not a Node service
        # course. The program's numeric IDs do not imply sequence.
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        codes = [entry.code for entry in entries]
        react = next(entry for entry in entries if entry.code == "APP20")
        self.assertEqual(
            (react.title, react.kind, react.classification, react.status),
            ("React Application Engineering", "course", "core", "draft"),
        )
        self.assertEqual(prerequisite_codes(react.prerequisites), ["APP2"])
        self.assertLess(codes.index("APP2"), codes.index("APP20"))
        self.assertLess(codes.index("APP20"), codes.index("APP3"))
        source = (self.app.APP / "APP20.md").read_text(encoding="utf-8")
        self.assertIn("**Specification:** `v0.2.0`", source)
        self.assertIn("**Classification:** `core`", source)
        capstone = next(entry for entry in entries if entry.code == "APP9")
        self.assertIn("APP20", prerequisite_codes(capstone.prerequisites))

    def test_react_core_catalog_mismatch_still_fails(self):
        # A course-specific prerequisite mutation must be detected even
        # when APP9's full-core closure remains otherwise complete.
        catalog = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in catalog.splitlines()
                   if line.startswith("| [APP20](APP20.md) |"))
        changed = row.replace(" | APP2 |", " | APP2, APP21 |", 1)
        self.assertNotEqual(row, changed)
        self.change_catalog(row, changed)
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP20", errors)
        self.assertIn("prerequisites differ from catalog", errors)

    def test_app3_framework_core_requires_ts_node_and_database(self):
        # Backend framework design combines three independent core
        # foundations; the browser/React branch is not its prerequisite.
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        app3 = next(entry for entry in entries if entry.code == "APP3")
        self.assertEqual(
            (app3.title, app3.kind, app3.classification, app3.status),
            ("Backend Framework Engineering", "course", "core", "draft"),
        )
        self.assertEqual(
            prerequisite_codes(app3.prerequisites),
            ["APP19", "APP21", "APP4"],
        )
        source = (self.app.APP / "APP3.md").read_text(encoding="utf-8")
        self.assertIn("**Specification:** `v0.2.0`", source)
        self.assertIn("**Classification:** `core`", source)
        capstone = next(entry for entry in entries if entry.code == "APP9")
        self.assertIn("APP3", prerequisite_codes(capstone.prerequisites))

    def test_app3_catalog_only_prerequisite_edit_is_rejected(self):
        catalog = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in catalog.splitlines()
                   if line.startswith("| [APP3](APP3.md) |"))
        self.assertIn(" | APP19, APP21, APP4 |", row)
        changed = row.replace(
            " | APP19, APP21, APP4 |", " | APP19, APP21 |", 1
        )
        self.assertNotEqual(row, changed)
        self.change_catalog(row, changed)
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP3", errors)
        self.assertIn("prerequisites differ from catalog", errors)

    def test_app5_full_stack_core_requires_react_and_backend(self):
        # APP5 combines the two course branches; APP4 remains
        # required transitively through APP3 rather than duplicated.
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        codes = [entry.code for entry in entries]
        app5 = next(entry for entry in entries if entry.code == "APP5")
        self.assertEqual(
            (app5.title, app5.kind, app5.classification, app5.status),
            ("Full-Stack Application Architecture", "course", "core", "draft"),
        )
        self.assertEqual(prerequisite_codes(app5.prerequisites),
                         ["APP20", "APP3"])
        self.assertLess(codes.index("APP20"), codes.index("APP5"))
        self.assertLess(codes.index("APP3"), codes.index("APP5"))
        source = (self.app.APP / "APP5.md").read_text(encoding="utf-8")
        self.assertIn("**Specification:** `v0.2.0`", source)
        self.assertIn("**Classification:** `core`", source)
        capstone = next(entry for entry in entries if entry.code == "APP9")
        self.assertIn("APP5", prerequisite_codes(capstone.prerequisites))

    def test_app5_catalog_only_prerequisite_edit_is_rejected(self):
        catalog = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in catalog.splitlines()
                   if line.startswith("| [APP5](APP5.md) |"))
        self.assertIn(" | APP20, APP3 |", row)
        changed = row.replace(
            " | APP20, APP3 |", " | APP20, APP3, APP4 |", 1
        )
        self.assertNotEqual(row, changed)
        self.change_catalog(row, changed)
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP5", errors)
        self.assertIn("prerequisites differ from catalog", errors)

    def test_app8_cannot_be_silently_removed_from_capstone_closure(self):
        # APP20 is now required transitively through migrated APP5.
        # APP8 has no further required core successor before APP9.
        # Removing APP8 from the project must still fail closed.
        catalog = self.catalog.read_text(encoding="utf-8")
        self.assertIn("APP1–APP8, APP17–APP21 | `project`", catalog)
        self.catalog.write_text(
            catalog.replace("APP1–APP8, APP17–APP21 | `project`",
                            "APP1–APP7, APP17–APP21 | `project`", 1),
            encoding="utf-8",
        )
        self.change_course("APP9", ", [APP8](APP8.md)", "")
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP8", errors)
        self.assertIn("graduation capstone is missing core prerequisites", errors)

    def test_app17_remains_required_transitively_through_app2(self):
        # Direct APP9 links can be shortened only when the validated
        # transitive graph still includes the complete core.
        catalog = self.catalog.read_text(encoding="utf-8")
        app9_row = next(line for line in catalog.splitlines()
                        if line.startswith("| [APP9](APP9.md) |"))
        self.assertIn("APP17–APP21", app9_row)
        revised = app9_row.replace("APP17–APP21", "APP18–APP21", 1)
        self.change_catalog(app9_row, revised)
        self.change_course("APP9", ", [APP17](APP17.md)", "")
        status, errors = self.check()
        self.assertEqual(status, 0, errors)

    def test_catalog_is_explicitly_ordered_not_sorted_by_code(self):
        lines = self.catalog.read_text(encoding="utf-8").splitlines()
        a = next(i for i, line in enumerate(lines) if line.startswith("| [APP2]("))
        b = next(i for i, line in enumerate(lines) if line.startswith("| [APP3]("))
        lines[a], lines[b] = lines[b], lines[a]
        self.catalog.write_text("\n".join(lines) + "\n", encoding="utf-8")
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        codes = [e.code for e in entries]
        self.assertLess(codes.index("APP3"), codes.index("APP2"))
        status, errors = self.check()
        self.assertEqual(status, 0, errors)

    def test_future_core_can_follow_existing_courses_without_renumbering(self):
        self.add_future_core_course(link_capstone=True)
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        self.assertEqual(
            next(entry.classification for entry in entries if entry.code == self.future_code),
            "core",
        )
        status, errors = self.check()
        self.assertEqual(status, 0, errors)

    def test_future_core_cannot_be_omitted_from_capstone_prerequisites(self):
        self.add_future_core_course(link_capstone=False)
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn(self.future_code, errors)

    def test_unknown_course_file_cannot_be_silently_skipped(self):
        (self.app.APP / f"{self.future_code}.md").write_text("Unlisted\n", encoding="utf-8")
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn(f"unlisted course file {self.future_code}.md", errors)

    def test_missing_course_file_fails(self):
        (self.app.APP / "APP3.md").unlink()
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("missing course file APP3.md", errors)

    def test_duplicate_row_fails(self):
        content = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in content.splitlines() if line.startswith("| [APP3]("))
        self.catalog.write_text(content.replace(row, row + "\n" + row), encoding="utf-8")
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("duplicate course row APP3", errors)

    def test_classification_mismatch_fails(self):
        self.change_catalog("**Elective · draft**", "Core · draft")
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("classification differs from catalog", errors)

    def test_catalog_course_type_and_readiness_must_agree(self):
        content = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in content.splitlines() if line.startswith("| [APP9]("))
        self.change_catalog(row, row.replace("`project`", "`course`", 1))
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP9 must be a core project", errors)

    def test_prerequisite_mismatch_fails(self):
        # Keep this regression independent of renaming and duration
        # revisions to APP2. Mutate only its prerequisite column.
        catalog = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in catalog.splitlines()
                   if line.startswith("| [APP2](APP2.md) |"))
        parts = row.split(" | ")
        self.assertIn("APP17, APP19", row)
        self.assertIn("APP17, APP19", parts[3])
        updated = row.replace(" | APP17, APP19 |", " | APP17, APP19, APP3 |", 1)
        self.assertNotEqual(updated, row)
        self.change_catalog(row, updated)
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("prerequisites differ from catalog", errors)

    def test_core_cannot_require_an_elective(self):
        content = self.catalog.read_text(encoding="utf-8")
        row = next(line for line in content.splitlines() if line.startswith("| [APP9]("))
        updated = row.replace(" | `project` |", ", APP10 | `project` |", 1)
        self.assertNotEqual(row, updated)
        self.change_catalog(row, updated)
        app9 = self.app.APP / "APP9.md"
        content = app9.read_text(encoding="utf-8")
        old = next(line for line in content.splitlines() if line.startswith("**Prerequisites:**"))
        app9.write_text(content.replace(old, old + ", [APP10](APP10.md)", 1), encoding="utf-8")
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("core course cannot require an elective", errors)

    def test_prerequisite_ranges_expand_without_missing_ids(self):
        self.assertEqual(
            prerequisite_codes("APP1–APP3, APP2, [APP4](APP4.md)"),
            ["APP1", "APP2", "APP3", "APP4"],
        )
        with self.assertRaisesRegex(ValueError, "invalid APP prerequisite range"):
            prerequisite_codes("APP5–APP2")


if __name__ == "__main__":
    unittest.main()
