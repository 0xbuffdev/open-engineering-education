"""Host interpreter and virtual environment portability in the wheel verifier."""
from __future__ import annotations

import subprocess
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

from tooling.interop import verify_package_install as verifier


class PackageVerifierEnvironmentTests(TestCase):
    def test_missing_ensurepip_reports_venv_and_alternate_python(self):
        with patch.object(verifier.venv, "EnvBuilder") as builder:
            builder.return_value.create.side_effect = subprocess.CalledProcessError(
                1, ["python", "-m", "ensurepip"]
            )
            with self.assertRaises(verifier.PackageVerificationEnvironmentError) as ctx:
                verifier.make_verification_venv(Path("temporary-test-venv"))
        message = str(ctx.exception)
        self.assertIn("python3-venv", message)
        self.assertIn("--python", message)
        self.assertIn("wheel was NOT tested", message)

    def test_selected_python_reexecs_without_recursive_argument(self):
        with patch.object(verifier.shutil, "which", return_value="/tmp/test-python"):
            with patch.object(Path, "is_file", return_value=True):
                with patch.object(verifier.subprocess, "call", return_value=0) as call:
                    result = verifier.main([
                        "--dist", "dist", "--python", "test-python",
                    ])
        self.assertEqual(result, 0)
        args = call.call_args.args[0]
        self.assertEqual(args[0], str(Path("/tmp/test-python").resolve()))
        self.assertNotIn("--python", args)
        self.assertIn("--dist", args)
        self.assertIn("--source", args)

    def test_missing_selected_python_gives_exit_code_three(self):
        with patch.object(verifier.shutil, "which", return_value=None):
            result = verifier.main([
                "--dist", "dist", "--python", "not-installed-python",
            ])
        self.assertEqual(result, 3)
