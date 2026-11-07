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
        self.app.ROOT = self.root
        self.app.APP = self.root / "curriculum" / "APP"
        self.catalog = self.app.APP / "README.md"

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

    def add_app17(self, link_capstone: bool):
        row = "| [APP17](APP17.md) | HTML & CSS Engineering | 8 weeks | APP1 | \x60course\x60 | Core · draft |\n"
        cat = self.catalog.read_text(encoding="utf-8")
        cap_line = next(x for x in cat.splitlines() if x.startswith("| [APP9]("))
        self.assertIn(cap_line, cat)
        cat = cat.replace(cap_line, row + cap_line, 1)
        if link_capstone:
            cat = cat.replace(
                "| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8 |",
                "| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8, APP17 |",
            )
            app9 = self.app.APP / "APP9.md"
            data = app9.read_text(encoding="utf-8")
            old_meta = next(
                line for line in data.splitlines()
                if line.startswith("**Prerequisites:**")
            )
            data = data.replace(
                old_meta, old_meta + ", [APP17](APP17.md)", 1
            )
            app9.write_text(data, encoding="utf-8")
        self.catalog.write_text(cat, encoding="utf-8")
        (self.app.APP / "APP17.md").write_text(
            new_outcome_course("APP17", "HTML & CSS Engineering", "8 weeks"),
            encoding="utf-8",
        )

    def test_current_catalog_passes(self):
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

    def test_new_core_app17_can_follow_app1_without_renumbering(self):
        self.add_app17(link_capstone=True)
        entries, errors = read_app_catalog(self.catalog)
        self.assertFalse(errors, errors)
        self.assertEqual(
            next(entry.classification for entry in entries if entry.code == "APP17"),
            "core",
        )
        status, errors = self.check()
        self.assertEqual(status, 0, errors)

    def test_new_core_cannot_be_omitted_from_capstone_prerequisites(self):
        self.add_app17(link_capstone=False)
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP17", errors)

    def test_unknown_course_file_cannot_be_silently_skipped(self):
        (self.app.APP / "APP17.md").write_text("Unlisted\n", encoding="utf-8")
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("unlisted course file APP17.md", errors)

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
        self.change_catalog(
            "| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8 | \x60project\x60 |",
            "| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8 | \x60course\x60 |",
        )
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("APP9 must be a core project", errors)

    def test_prerequisite_mismatch_fails(self):
        self.change_catalog(
            "| [APP2](APP2.md) | Frontend Engineering | 9 weeks | APP1 |",
            "| [APP2](APP2.md) | Frontend Engineering | 9 weeks | APP1, APP3 |",
        )
        status, errors = self.check()
        self.assertNotEqual(status, 0)
        self.assertIn("prerequisites differ from catalog", errors)

    def test_core_cannot_require_an_elective(self):
        self.change_catalog(
            "| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8 |",
            "| [APP9](APP9.md) | Application Engineering Capstone | 12–16 weeks | APP1–APP8, APP10 |",
        )
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
