"""Expected-to-fail independent contract tests for the SEF9 teaching patch.

Run manually as documented in examples/sef9/README.md, not as repository CI.
All writes are confined to TemporaryDirectory() fixtures.
"""

from __future__ import annotations

import csv
from pathlib import Path
import tempfile
import unittest

try:
    from .seeded_export import export_tasks
except ImportError:
    from seeded_export import export_tasks


class CSVExportContractTests(unittest.TestCase):
    def test_quotes_commas_and_newlines_round_trip(self):
        rows = [{"id": 7, "title": 'Ops, "urgent"\nnext step'}]
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "tasks.csv"
            self.assertTrue(export_tasks(rows, target))
            with target.open(encoding="utf-8", newline="") as stream:
                observed = list(csv.DictReader(stream))
            self.assertEqual(observed, [{"id": "7", "title": 'Ops, "urgent"\nnext step'}])

    def test_directory_destination_reports_failure_instead_of_success(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)  # opening a directory for writing raises OSError
            self.assertFalse(export_tasks([{"id": 1, "title": "demo"}], target))

    def test_invalid_source_cannot_overwrite_prior_valid_output(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "last-good.csv"
            original = b"id,title\n1,Previously valid\n"
            target.write_bytes(original)
            malformed_rows = [{"id": 2, "title": "first"}, {"id": 3}]
            try:
                export_tasks(malformed_rows, target)
            except (KeyError, TypeError, ValueError):
                pass  # failure may be expressed as an exception or false result
            self.assertEqual(target.read_bytes(), original)


if __name__ == "__main__":
    unittest.main()
