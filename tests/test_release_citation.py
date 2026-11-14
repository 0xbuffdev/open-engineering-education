"""Release citation checks cover matching, mismatched, and immutable historic tags."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check-release-citation.py"
spec = importlib.util.spec_from_file_location("oee_release_citation", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)

CFF = """cff-version: 1.2.0
title: "Open Engineering Education"
date-released: "2026-11-07"
version: "0.2.0"
"""


class ReleaseCitationTests(unittest.TestCase):
    def test_exact_tag_and_release_date_match(self):
        self.assertEqual(checker.validate(CFF, "v0.2.0", "2026-11-07T12:59:08Z"), [])

    def test_timezone_date_normalizes_to_utc(self):
        self.assertEqual(checker.validate(CFF, "v0.2.0", "2026-11-08T01:00:00+13:00"), [])

    def test_tag_version_mismatch(self):
        errors = checker.validate(CFF, "v0.3.0", "2026-11-07")
        self.assertEqual(len(errors), 1)
        self.assertIn("does not match tag", errors[0])

    def test_release_date_mismatch(self):
        errors = checker.validate(CFF, "v0.2.0", "2026-11-08")
        self.assertEqual(len(errors), 1)
        self.assertIn("UTC release publication date", errors[0])

    def test_duplicate_top_level_metadata_fails(self):
        errors = checker.validate(CFF + '\nversion: "0.2.0"\n', "v0.2.0", "2026-11-07")
        self.assertTrue(any("found 2" in error for error in errors))

    def test_missing_release_date_fails(self):
        errors = checker.validate(CFF.replace('date-released: "2026-11-07"', ""), "v0.2.0", "2026-11-07")
        self.assertTrue(any("date-released" in error for error in errors))

    def test_non_iso_date_fails(self):
        errors = checker.validate(CFF.replace("2026-11-07", "07/11/2026"), "v0.2.0", "2026-11-07")
        self.assertTrue(any("ISO date" in error for error in errors))

    def test_invalid_release_tag_fails(self):
        self.assertTrue(checker.validate(CFF, "main", "2026-11-07"))

    def test_malformed_scalar_fails(self):
        errors = checker.validate(CFF.replace('"0.2.0"', '"0.2.0'), "v0.2.0", "2026-11-07")
        self.assertTrue(any("unterminated" in error for error in errors))

    def test_repository_citation_is_well_formed_across_future_releases(self):
        current = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        version = checker.cff_scalar(current, "version")
        released = checker.cff_scalar(current, "date-released")
        self.assertEqual(checker.validate(current, "v" + version, released), [])

    def test_cli_nonzero_on_mismatch_without_network(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "CITATION.cff"
            file.write_text(CFF, encoding="utf-8")
            cmd = [sys.executable, str(SCRIPT), "--citation", str(file),
                   "--tag", "v0.2.0", "--published-at", "2026-11-07"]
            ok = subprocess.run(cmd, capture_output=True, text=True, check=False)
            self.assertEqual(ok.returncode, 0, ok.stderr)
            bad = subprocess.run(cmd[:-1] + ["2026-11-08"], capture_output=True, text=True, check=False)
            self.assertNotEqual(bad.returncode, 0)
            self.assertIn("FAILED", bad.stderr)


if __name__ == "__main__":
    unittest.main()
