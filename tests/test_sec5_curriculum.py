"""SEC5 competency and evidence validation, without arbitrary course-size quotas."""

from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curriculum" / "SEC" / "SEC5.md"
CATALOG = COURSE.parent / "README.md"


class SEC5CurriculumTests(unittest.TestCase):
    def test_official_outcome_curriculum_validation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check-outcome-curriculum.py"),
             "--course", str(COURSE)],
            cwd=ROOT, capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_public_identity_and_prerequisite_closure(self):
        source = COURSE.read_text(encoding="utf-8")
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertTrue(source.startswith(
            "# SEC5 — Applied Cryptography & Secure Protocols\n"))
        for expected in (
            "**Program:** SEC — Security Engineering",
            "**Type:** `course`",
            "**Status:** `draft`",
            "**Specification:** `v0.2.0`",
            "**Duration:** 12–16 weeks",
            "**Prerequisites:** [SEC1](SEC1.md)",
        ):
            self.assertIn(expected, source)
        self.assertIn(
            "| [SEC5](SEC5.md) | Applied Cryptography & Secure Protocols "
            "| 12–16 weeks | SEC1 | `course` |", catalog)
        match = re.search(r"(?m)^\*\*Prerequisites:\*\* (.+)$", source)
        self.assertIsNotNone(match)
        self.assertEqual(match.group(1), "[SEC1](SEC1.md)")
        self.assertNotIn("legacy", source.lower())
        self.assertNotIn("backward compatibility", source.lower())

    def test_every_outcome_taught_and_assessed(self):
        source = COURSE.read_text(encoding="utf-8")
        headings = re.findall(r"(?m)^## (.+)$", source)
        self.assertEqual(
            headings[:4],
            ["Overview", "Learning outcomes", "Modules", "Completion requirements"])
        outcomes_section = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        outcome_ids = re.findall(
            r"(?m)^- \*\*(SEC5-O\d+):\*\*", outcomes_section)
        self.assertTrue(outcome_ids)
        self.assertEqual(len(outcome_ids), len(set(outcome_ids)))
        known = set(outcome_ids)

        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        starts = list(re.finditer(r"(?m)^### Module (\d+) — ", modules))
        self.assertTrue(starts)
        self.assertEqual(
            [int(m.group(1)) for m in starts],
            list(range(1, len(starts) + 1)))
        taught = set()
        for index, marker in enumerate(starts):
            end = starts[index + 1].start() if index + 1 < len(starts) else len(modules)
            block = modules[marker.start():end]
            self.assertIn("#### Outcomes", block)
            self.assertIn("#### Lessons", block)
            targets, lessons = block.split("#### Lessons", 1)
            refs = set(re.findall(r"(?m)^- (SEC5-O\d+)$", targets))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            taught.update(refs)
            ordinals = [int(v) for v in re.findall(r"(?m)^(\d+)\. \*\*", lessons)]
            self.assertTrue(ordinals)
            self.assertEqual(ordinals, list(range(1, len(ordinals) + 1)))
        self.assertEqual(taught, known)

        completion = source.split("\n## Completion requirements\n", 1)[1]
        blocks = re.split(
            r"(?=^- \*\*SEC5-AS\d+\*\* — )", completion, flags=re.M)[1:]
        self.assertTrue(blocks)
        seen_assessments = set()
        assessed = set()
        for block in blocks:
            head = re.match(r"- \*\*(SEC5-AS\d+)\*\*", block)
            self.assertIsNotNone(head)
            self.assertNotIn(head.group(1), seen_assessments)
            seen_assessments.add(head.group(1))
            for field in ("Outcomes", "Work", "Criteria", "Evidence"):
                self.assertRegex(block, rf"(?m)^  - \*\*{field}:\*\* \S")
            mapping = re.search(r"(?m)^  - \*\*Outcomes:\*\* (.+)$", block)
            self.assertIsNotNone(mapping)
            refs = set(re.findall(r"SEC5-O\d+", mapping.group(1)))
            self.assertTrue(refs)
            self.assertTrue(refs <= known)
            assessed.update(refs)
        self.assertEqual(assessed, known)

    def test_crypto_critical_boundaries_and_readiness(self):
        source = COURSE.read_text(encoding="utf-8")
        for expected in (
            "No unauthenticated plaintext",
            "unique per-key nonces",
            "No paid service",
            "final NIST IR 8547",
            "October 2026",
            "Optional lesson experiments",
            "Do not force implementations",
        ):
            self.assertIn(expected, source)
        self.assertNotIn("kind: `test`", source)
        self.assertNotIn("kind: `lab`", source)
        self.assertNotIn("## Substantial course lab", source)


    def test_real_two_party_key_establishment_has_required_negative_evidence(self):
        source = COURSE.read_text(encoding="utf-8")
        outcomes = source.split("\n## Learning outcomes\n", 1)[1].split(
            "\n## Modules\n", 1)[0]
        modules = source.split("\n## Modules\n", 1)[1].split(
            "\n## Completion requirements\n", 1)[0]
        assessment = source.split("- **SEC5-AS3**", 1)[1].split(
            "- **SEC5-AS4**", 1)[0]
        catalog = CATALOG.read_text(encoding="utf-8")
        self.assertIn("Execute and independently verify one vetted-library", outcomes)
        self.assertIn("SEC5-O9", outcomes)
        for phrase in (
            "Execute a real local key agreement and derive session material",
            "Peer-key trust, authenticated context and transcripts",
            "wrong-party/wrong-context case",
        ):
            self.assertIn(phrase, modules)
        for phrase in (
            "Actually execute a second-party vetted-library",
            "two independent locally generated test identities",
            "explicit pretrusted identity map",
            "Before execution",
            "actively rejected at an explicit trust boundary",
            "context-mismatch failure",
            "redacted derived secrets",
            "supplied KEM/HPKE/TLS",
        ):
            self.assertIn(phrase, assessment)
        self.assertIn("No public endpoint or bespoke protocol", source)
        self.assertIn("RFC 7748", source)
        self.assertIn("Python `cryptography` X25519 key exchange", source)
        self.assertIn("real two-party vetted-library key agreement", catalog)
        self.assertNotIn("live public PKI is required", source)


if __name__ == "__main__":
    unittest.main()
