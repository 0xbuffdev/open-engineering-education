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
import shutil
import sys
from pathlib import Path
import os
import subprocess
import tarfile
import tempfile
import venv
import zipfile

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
EXCLUDED = {"curriculum", "rfcs", "spec", "docs", "tests", ".github"}
PACKAGE = "oee_toolkit"


class PackageVerificationEnvironmentError(Exception):
    """A clean pip-equipped verification environment cannot be created."""


def make_verification_venv(directory: Path) -> None:
    """Provide an actionable diagnostic for Python without ensurepip."""
    try:
        venv.EnvBuilder(with_pip=True).create(directory)
    except (OSError, RuntimeError, subprocess.CalledProcessError) as exc:
        raise PackageVerificationEnvironmentError(
            "Could not create an isolated Python environment with pip. "
            "On Debian/Ubuntu, install the matching python3-venv package "
            "(for example python3.12-venv). Without system package access, "
            "use --python /path/to/ensurepip-enabled/python (such as a "
            "uv-managed CPython). The wheel was NOT tested by this invocation."
        ) from exc


def selected_python(value: str) -> Path:
    """Resolve an explicitly selected interpreter; never choose one silently."""
    path = Path(value).expanduser()
    executable = str(path) if path.is_absolute() else shutil.which(value)
    if not executable or not Path(executable).is_file():
        raise PackageVerificationEnvironmentError(
            f"Selected --python interpreter was not found: {value}"
        )
    return Path(executable).resolve()


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
                       "oee_toolkit/schemas/course-export-v2.schema.json"):
            if member not in names:
                raise AssertionError(f"wheel missing {member}")
        if "oee_toolkit/schemas/course-export-v1.schema.json" in names:
            raise AssertionError("installed consumer wheel still ships obsolete v1 export schema")
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
        if any(Path(*parts).as_posix() ==
               "tooling/oee_toolkit/schemas/course-export-v1.schema.json"
               for parts in names):
            raise AssertionError("consumer source archive still ships obsolete v1 schema")
        for required in ("tooling/oee_toolkit/_outcome_parser.py",
                         "tooling/oee_toolkit/_course_format_versions.py",
                         "tooling/oee_toolkit/schemas/course-export-v2.schema.json"):
            if not any(Path(*parts).as_posix() == required for parts in names):
                raise AssertionError(f"sdist missing {required}")


def verify(wheel: Path, archive: Path, source: Path) -> dict:
    """Install package outside repository, run from a signed local release.

    The publisher's temporary Git checkout is used to *prepare* fixture
    bytes. The installed wheel runs the consumer without Git, a source
    checkout or a network fetch. Keys are disposable and non-authoritative.
    """
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    from tooling.oee_toolkit.release_archive import (
        build_archive, install_verified_archive, sign_candidate,
    )
    from tooling.oee_toolkit.release_manifest import digest_manifest
    from tooling.oee_toolkit.core import canonical_json
    from tooling.oee_toolkit.source import GitSource

    contents_ok(wheel, archive)
    full_revision = run("git", "rev-parse", "HEAD", cwd=source).decode().strip()
    assert len(full_revision) == 40
    with tempfile.TemporaryDirectory(prefix="oee-toolkit-wheel-") as temp:
        outside = Path(temp)
        envdir = outside / "venv"
        make_verification_venv(envdir)
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
            "import oee_toolkit, oee_toolkit.release_source; "
            "print(oee_toolkit.__version__); "
            "assert files('oee_toolkit').joinpath("
            "'schemas/course-export-v2.schema.json').is_file()",
            cwd=outside, env=safe_env).decode().strip()
        if not marker:
            raise AssertionError("wheel package version not importable")

        # All Git operations occur here, outside the installed wheel.
        selected_manifest, source_archive = build_archive(
            GitSource(source, full_revision), "2099.01.1")
        digest = digest_manifest(selected_manifest)
        key = Ed25519PrivateKey.generate()
        private_pem = key.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
        public_pem = key.public_key().public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        signed_claims, signed_proof = sign_candidate(
            source_archive, digest, private_pem)
        trusted_store = outside / "verified-curriculum"
        trusted_store.mkdir()
        install_verified_archive(source_archive, digest, signed_claims,
                                 signed_proof, public_pem, trusted_store)
        lock = outside / "oee-curriculum.lock.json"
        lock.write_bytes(canonical_json({
            "formatVersion": 1, "releaseId": selected_manifest["releaseId"],
            "manifestSha256": digest,
        }))
        args = ("--lock", str(lock), "--store", str(trusted_store))
        report = json.loads(run(executable, "check", "SEF1", *args, "--json",
                                cwd=outside, env=safe_env))
        if (report["structuralOutcome"] != "passed" or
            report["source"]["manifestSha256"] != digest):
            raise AssertionError("wheel CLI did not validate exact installed OEE release")
        if report["toolVersion"] != marker or report["manualReviewRequired"] is not True:
            raise AssertionError("wheel version or review marker inconsistent")
        exported = run(executable, "export", "SEF1", *args, "--output", "-",
                       cwd=outside, env=safe_env)
        direct = run(sys.executable, "-m", "tooling.oee_toolkit", "export", "SEF1",
                     *args, "--output", "-", cwd=source)
        if exported != direct:
            raise AssertionError("installed wheel and source consumer bytes differ")
        if exported != run(executable, "export", "SEF1", *args, "--output", "-",
                           cwd=outside, env=safe_env):
            raise AssertionError("repeated v2 exports are not byte-identical")
        body = json.loads(exported)
        if (body["exportVersion"] != 2 or
            body["source"]["manifestSha256"] != digest or
            body["source"]["originCommit"] != full_revision or
            body["course"]["code"] != "SEF1" or
            body["validation"]["manualReviewRequired"] is not True):
            raise AssertionError("wheel exported incorrect v2 academic release identity")
        if (len(body["outcomes"]), len(body["assessments"])) != (7, 3):
            raise AssertionError("current SEF1 acceptance identities changed")

        # No consumer fallback to Git revisions or an absent project lock.
        if run(executable, "export", "SEF1", "--repo", str(source),
               "--revision", full_revision, "--output", "-",
               cwd=outside, expected=2, env=safe_env):
            raise AssertionError("disallowed repository flags emitted consumer output")
        if run(executable, "export", "SEF1", "--output", "-",
               cwd=outside / "verified-curriculum", expected=3,
               env=safe_env):
            raise AssertionError("no-lock fallback emitted course data")

        return {
            "packageVersion": marker,
            "course": body["course"]["code"],
            "sourceCommitInternal": full_revision,
            "manifestSha256": digest,
            "exportVersion": body["exportVersion"],
            "outcomes": len(body["outcomes"]),
            "assessments": len(body["assessments"]),
            "separateEnvironment": True,
            "byteIdenticalToRepositoryConsumer": True,
            "installedWheelUsesGit": False,
            "sdistExcludesEducationalSource": True,
            "publication": "not-authorized",
        }

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, required=True)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--python", help=(
        "alternate Python with venv/ensurepip; rerun under it before the clean install"
    ))
    args = parser.parse_args(argv)
    try:
        if args.python is not None:
            interpreter = selected_python(args.python)
            if interpreter != Path(sys.executable).resolve():
                return subprocess.call([
                    str(interpreter), str(Path(__file__).resolve()),
                    "--dist", str(args.dist.resolve()),
                    "--source", str(args.source.resolve()),
                ])
        files = list(args.dist.glob("*.whl"))
        archives = list(args.dist.glob("*.tar.gz"))
        if len(files) != 1 or len(archives) != 1:
            parser.error("requires exactly one wheel and one source archive")
        result = verify(files[0].resolve(), archives[0].resolve(), args.source.resolve())
    except PackageVerificationEnvironmentError as exc:
        print(f"toolkit_verifier_environment: {exc}", file=sys.stderr)
        return 3
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
