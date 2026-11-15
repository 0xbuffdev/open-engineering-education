"""Regression tests for public documentation's internal-link boundary."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "public_docs_checker", ROOT / "scripts" / "check-public-docs.py"
)
assert SPEC is not None and SPEC.loader is not None
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class PublicDocsTests(unittest.TestCase):
    def test_public_docs_without_private_links_pass(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "rfcs").mkdir()
            (root / "README.md").write_text(
                "See https://github.com/0xbuffdev/open-engineering-education\n",
                encoding="utf-8",
            )
            (root / "rfcs" / "0001.md").write_text(
                "See https://github.com/0xbuffdev/oee-workspace\n",
                encoding="utf-8",
            )
            self.assertEqual(checker.check_public_documents(root), [])

    def test_private_link_reports_file_and_line(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            folder = root / "spec"
            folder.mkdir()
            (folder / "README.md").write_text(
                "Public requirements\n"
                "https://github.com/0xbuffdev/context/blob/main/tickets.md\n",
                encoding="utf-8",
            )
            self.assertEqual(
                checker.check_public_documents(root),
                ["spec/README.md:2: remove link to an internal planning repository"],
            )

    def test_private_context_variant_and_query_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "HTTPS://GITHUB.COM/0xBUFFDEV/internal-context?tab=readme\n",
                encoding="utf-8",
            )
            self.assertEqual(len(checker.check_public_documents(root)), 1)

    def test_external_resource_links_are_not_blocked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "https://github.com/0xbuffdev/contextual-tool\n"
                "https://github.com/another-organization/context\n",
                encoding="utf-8",
            )
            self.assertEqual(checker.check_public_documents(root), [])

    def test_course_files_included_and_test_fixtures_excluded(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            course_folder = root / "curriculum" / "SEF"
            course_folder.mkdir(parents=True)
            (course_folder / "SEF1.md").write_text(
                "https://github.com/0xbuffdev/context\n", encoding="utf-8"
            )
            fixture_folder = root / "tests" / "fixtures"
            fixture_folder.mkdir(parents=True)
            (fixture_folder / "example.md").write_text(
                "https://github.com/0xbuffdev/internal-context\n",
                encoding="utf-8",
            )
            self.assertEqual(
                checker.check_public_documents(root),
                ["curriculum/SEF/SEF1.md:1: remove link to an internal planning repository"],
            )


if __name__ == "__main__":
    unittest.main()
