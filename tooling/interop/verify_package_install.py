#!/usr/bin/env python3
"""Independent OEE Toolkit wheel/sdist verification, with no publication.

Build the distributions before executing. This verifier installs the wheel in
a fresh venv, runs outside the source repository, checks the installed
entrypoint and export, verifies package attribution and inspects the sdist
against accidental curriculum bundling. No third-party test framework.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import os
import subprocess
import sys
import tarfile
import tempfile
import venv
import zipfile

ROOT = Path(__file__).resolve().parents[2]
EXCLUDED = {"curriculum", "rfcs", "spec", "docs", "tests", ".github"}
PACKAGE = "oee_toolkit"


def run(*args: object, cwd: Path, expected: int = 0, env: dict | None = None) -> bytes:
    command = [str(arg) for arg in args]
    process = subprocess.run(command, cwd=cwd, env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, timeout=160, check=False)
    if process.returncode != expected:
        raise AssertionError(
            f"command {command[0]} exited {process.returncode}, expected {expected}: "
            + process.stderr.decode("utf-8", "replace")[:1600]
        )
    return process.stdout


def contents_ok(wheel: Path, archive: Path) -> None:
    with zipfile.ZipFile(wheel) as zipped:
        names = zipped.namelist()
        for member in ("oee_toolkit/_outcome_parser.py",
                       "oee_toolkit/_course_format_versions.py",
                       "oee_toolkit/schemas/course-export-v1.schema.json"):
            if member not in names:
                raise AssertionError(f"wheel missing {member}")
        if not any(n.endswith(".dist-info/entry_points.txt") for n in names):
            raise AssertionError("wheel missing console entrypoint metadata")
        if not any(n.endswith(".dist-info/licenses/LICENSE-MIT") for n in names):
            raise AssertionError("wheel missing MIT software license")
        if not any(n.endswith(".dist-info/licenses/NOTICE") for n in names):
            raise AssertionError("wheel missing notice/attribution")
        if any("/curriculum/" in "/" + n or "/golden/" in "/" + n for n in names):
            raise AssertionError("wheel contains CC BY educational source")

    with tarfile.open(archive, "r:gz") as tar:
        names = [Path(n).parts[1:] for n in tar.getnames()]
        if any(parts and parts[0] in EXCLUDED for parts in names):
            raise AssertionError("sdist includes non-package curriculum/spec or tests")
        if any("golden" in parts or
               (parts and parts[0] == "scripts") for parts in names):
            raise AssertionError("sdist includes repository maintenance or golden data")
        for required in ("tooling/oee_toolkit/_outcome_parser.py",
                         "tooling/oee_toolkit/_course_format_versions.py",
                         "tooling/oee_toolkit/schemas/course-export-v1.schema.json"):
            if not any(Path(*parts).as_posix() == required for parts in names):
                raise AssertionError(f"sdist missing {required}")


def verify(wheel: Path, archive: Path, source: Path) -> dict:
    contents_ok(wheel, archive)
    full_revision = run("git", "rev-parse", "HEAD", cwd=source).decode().strip()
    assert len(full_revision) == 40
    with tempfile.TemporaryDirectory(prefix="oee-toolkit-wheel-") as temp:
        outside = Path(temp)
        envdir = outside / "venv"
        venv.EnvBuilder(with_pip=True).create(envdir)
        if os.name == "nt":
            installed_python = envdir / "Scripts/python.exe"
            executable = envdir / "Scripts/oee-toolkit.exe"
        else:
            installed_python = envdir / "bin/python"
            executable = envdir / "bin/oee-toolkit"
        safe_env = {**os.environ, "PYTHONPATH": ""}
        run(installed_python, "-m", "pip", "install", "--no-index",
            "--no-deps", str(wheel), cwd=outside, env=safe_env)
        marker = run(installed_python, "-c", "from importlib.resources import files; "
            "import oee_toolkit, oee_toolkit._outcome_parser; "
            "print(oee_toolkit.__version__); "
            "assert files('oee_toolkit').joinpath("
            "'schemas/course-export-v1.schema.json').is_file()",
            cwd=outside, env=safe_env).decode().strip()
        if not marker:
            raise AssertionError("wheel package version not importable")

        args = ("--repo", str(source), "--revision", full_revision, "--course", "SEF1")
        report = json.loads(run(executable, "check", *args, "--json",
                                cwd=outside, env=safe_env))
        if report["structuralOutcome"] != "passed" or report["source"]["revision"] != full_revision:
            raise AssertionError("wheel CLI did not validate exact OEE source")
        if report["toolVersion"] != marker or report["manualReviewRequired"] is not True:
            raise AssertionError("wheel CLI version or educational-review marker inconsistent")
        exported = run(executable, "export", *args, "--output", "-",
                       cwd=outside, env=safe_env)
        direct = run(sys.executable, "-m", "tooling.oee_toolkit", "export",
                     *args, "--output", "-", cwd=source)
        if exported != direct:
            raise AssertionError("installed wheel bytes disagree with source-only CLI")
        if exported != run(executable, "export", *args, "--output", "-",
                           cwd=outside, env=safe_env):
            raise AssertionError("repeated exports are not byte-identical")
        body = json.loads(exported)
        if (body["source"]["revision"] != full_revision or
            body["course"]["code"] != "SEF1" or
            body["validation"]["manualReviewRequired"] is not True):
            raise AssertionError("wheel exported incorrect academic source")
        if (len(body["outcomes"]), len(body["assessments"])) != (7, 3):
            raise AssertionError("current SEF1 acceptance identities changed")

        # Missing immutable Git objects are incomplete, not silently HEAD.
        failed = run(executable, "check", "--repo", str(source),
                     "--revision", "0" * 40, "--course", "SEF1",
                     "--json", cwd=outside, expected=3, env=safe_env)
        if failed:
            raise AssertionError("unknown Git revision unexpectedly emitted valid source")

        return {
            "packageVersion": marker,
            "course": body["course"]["code"],
            "revision": full_revision,
            "outcomes": len(body["outcomes"]),
            "assessments": len(body["assessments"]),
            "separateEnvironment": True,
            "byteIdenticalToRepositoryCli": True,
            "sdistExcludesEducationalSource": True,
            "publication": "not-authorized",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=ROOT)
    args = parser.parse_args()
    files = list(args.dist.glob("*.whl"))
    archives = list(args.dist.glob("*.tar.gz"))
    if len(files) != 1 or len(archives) != 1:
        parser.error("requires exactly one wheel and one source archive")
    result = verify(files[0].resolve(), archives[0].resolve(), args.source.resolve())
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
