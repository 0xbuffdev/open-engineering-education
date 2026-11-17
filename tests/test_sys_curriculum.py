"""Regression checks for the first SYS v0.2.0 migration.

SYS1 retains its published course capability and follows the completed SEF
program. The other SYS course files remain legacy drafts during staged work.
This is a structural acceptance fixture, not evidence of learner readiness.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "curriculum" / "SYS" / "README.md"
SYS1 = ROOT / "curriculum" / "SYS" / "SYS1.md"
VALIDATOR = ROOT / "scripts" / "check-outcome-curriculum.py"


class Sys1MigrationTests(unittest.TestCase):
    def test_program_requires_completed_sef_and_sys1_requires_sef10(self):
        catalog = CATALOG.read_text(encoding="utf-8")
        source = SYS1.read_text(encoding="utf-8")
        self.assertIn("including SEF10", catalog)
        self.assertIn("**Prerequisites:** [SEF10](../SEF/SEF10.md)", source)
        self.assertTrue((ROOT / "curriculum" / "SEF" / "SEF10.md").is_file())

    def test_sys1_catalog_matches_current_course_contract(self):
        catalog = CATALOG.read_text(encoding="utf-8")
        source = SYS1.read_text(encoding="utf-8")
        self.assertTrue(source.startswith("# SYS1 — Computer Architecture, Memory & Performance\n"))
        for metadata in (
            "**Program:** SYS — Systems Engineering",
            "**Type:** `course`",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
            "**Duration:** 10–14 weeks",
        ):
            self.assertIn(metadata, source)
        self.assertRegex(
            catalog,
            re.compile(
                r"^\| \[SYS1\]\(SYS1\.md\) \| Computer Architecture, Memory "
                r"& Performance \| 10–14 weeks \| SEF10 \| `course` \|$",
                re.MULTILINE,
            ),
        )

    def test_sys1_advanced_sef_boundary_is_explicit(self):
        source = SYS1.read_text(encoding="utf-8")
        self.assertIn("SEF baseline (already assessed; do not reteach)", source)
        self.assertIn("New SYS competency (must be taught and assessed)", source)
        self.assertIn("Neither basic gate construction nor general C compilation is reassessed", source)

    def test_outcome_curriculum_validator_accepts_sys1(self):
        proc = subprocess.run(
            [sys.executable, str(VALIDATOR), "--course", str(SYS1), "--format", "json"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        report = json.loads(proc.stdout)
        self.assertEqual(report["structuralOutcome"], "passed")
        self.assertEqual(report["passedCourses"], 1)
        self.assertFalse(report["findings"])
        self.assertTrue(report["manualReviewRequired"])


if __name__ == "__main__":
    unittest.main()
