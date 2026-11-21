#!/usr/bin/env python3
"""OT-I05: independently exercise the public, current-only OEE Toolkit.

Use a local OEE Git clone as input. All operations run against a second
temporary, independent Git clone, without remotely fetching or publishing.
Python >= 3.11, Git and only the Python standard library are required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")
REPOSITORY = "0xbuffdev/open-engineering-education"
COURSES = ("SEF1", "SEF10", "APP1", "APP17")


class ReleaseCheckFailed(Exception):
    """A release-readiness assertion was not met."""


def ensure(condition: bool, reason: str) -> None:
    if not condition:
        raise ReleaseCheckFailed(reason)


def run(argv: list[str], cwd: Path, *, expected: int = 0,
        env: dict[str, str] | None = None) -> subprocess.CompletedProcess[bytes]:
    proc = subprocess.run(
        argv, cwd=cwd, env=env, capture_output=True, check=False, timeout=150,
    )
    if proc.returncode != expected:
        reason = proc.stderr.decode("utf-8", errors="replace")[-850:]
        output = proc.stdout.decode("utf-8", errors="replace")[-400:]
        raise ReleaseCheckFailed(
            f"expected exit {expected}, got {proc.returncode}: {argv!r}; "
            f"stderr={reason!r}; stdout={output!r}"
        )
    return proc


def git(repo: Path, *args: str) -> str:
    return run(["git", "-C", str(repo), *args], repo).stdout.decode(
        "utf-8", errors="strict"
    ).strip()


def parse(raw: bytes) -> dict:
    return json.loads(raw.decode("utf-8", errors="strict"))


def snapshot(report: dict, path: Path | None) -> None:
    encoded = json.dumps(report, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    if path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(encoded, encoding="utf-8", newline="\n")
        print(f"OT-I05 release-readiness report: {path}: {report['result']}")
    else:
        print(encoded, end="")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True,
                        help="trusted local OEE Git checkout (not a URL)")
    parser.add_argument("--report", type=Path, default=None,
                        help="optional local JSON report for maintainer review")
    options = parser.parse_args(argv)
    gates: list[dict] = []
    report = {
        "reportVersion": 1,
        "milestone": "OT-I05",
        "result": "incomplete",
        "toolkitReleasePublished": False,
        "packagedDistributionVerified": False,
        "packagedDistributionVerificationScope": (
            "source-only smoke does not run a wheel/sdist verifier; "
            "execute tooling/interop/verify_package_install.py separately "
            "and retain that result for the release decision"
        ),
        "formalOeeConformanceDetermined": False,
        "manualEducationalReviewRequired": True,
        "requiresPrivateService": False,
        "requiresPaidResource": False,
        "platform": sys.platform,
        "checks": gates,
    }

    def check(name: str, call) -> None:
        call()
        gates.append({"name": name, "state": "passed"})

    try:
        source = options.source.resolve(strict=True)
        ensure((source / ".git").exists(), "OEE source must be a public Git checkout")
        ensure(sys.version_info >= (3, 11), "Python 3.11+ is required")
        report["candidateSourceCommit"] = git(source, "rev-parse", "HEAD")
        ensure(FULL_SHA.fullmatch(report["candidateSourceCommit"]) is not None,
               "selected candidate is not a full Git commit")

        with tempfile.TemporaryDirectory(prefix="oee toolkit external ") as td:
            root = Path(td)
            checkout = root / "independent source clone"
            destination = root / "learner outputs"
            destination.mkdir()
            run(["git", "-c", "core.autocrlf=false", "clone", "--quiet",
                 "--no-hardlinks", str(source), str(checkout)], source)
            check("OT-20: independent public Git clone, no private source", lambda: (
                ensure((checkout / ".git").is_dir(), "independent clone missing .git"),
                ensure(git(checkout, "rev-parse", "HEAD") ==
                       report["candidateSourceCommit"], "clone has different source SHA"),
            ))

            offline = dict(os.environ)
            offline.update({
                "PYTHONIOENCODING": "utf-8",
                "GIT_TERMINAL_PROMPT": "0",
                "PIP_NO_INDEX": "1",
                "HTTP_PROXY": "http://127.0.0.1:9",
                "HTTPS_PROXY": "http://127.0.0.1:9",
                "ALL_PROXY": "http://127.0.0.1:9",
                "NO_PROXY": "",
            })
            offline.pop("OPENAI_API_KEY", None)
            offline.pop("ANTHROPIC_API_KEY", None)
            revision = git(checkout, "rev-parse", "HEAD")

            def toolkit(*params: str, expected: int = 0):
                return run([
                    sys.executable, "-m", "tooling.oee_toolkit._publisher_cli", *params,
                ], checkout, expected=expected, env=offline)

            def input_for(course: str, selected: str):
                return ("--repo", str(checkout), "--revision", selected,
                        "--course", course)

            def repo_readiness():
                output = toolkit("check", "--repo", str(checkout),
                                 "--revision", revision, "--all", "--json")
                parsed = parse(output.stdout)
                ensure(parsed["structuralOutcome"] == "passed",
                       "current repository-wide structural validation did not pass")
                ensure(not parsed["checksSkipped"],
                       "required structural checks were silently skipped")
                ensure(parsed["manualReviewRequired"] is True,
                       "Toolkit misrepresented structural validation as approval")
                ensure(parsed["source"]["revision"] == revision
                       and parsed["source"]["specification"] == "v0.2.0",
                       "Toolkit returned a different source version")
                ensure(len(parsed["courses"]) >= 4, "missing current course sources")
                report["currentCourseCount"] = len(parsed["courses"])
            check("OT-01/03/09/10/11/22/23: full v0.2.0 scan; never conformance",
                  repo_readiness)

            def version_support():
                old = git(checkout, "rev-parse", "refs/tags/v0.1.0^{commit}")
                ensure(FULL_SHA.fullmatch(old) is not None, "old format rejection tag absent")
                result = toolkit("check", *input_for("SEF1", old), "--json",
                                 expected=3)
                payload = parse(result.stdout)
                ensure(payload["structuralOutcome"] == "incomplete"
                       and payload["manualReviewRequired"] is True,
                       "historical format was silently interpreted as supported")
                absent = toolkit("check", *input_for("SEF1", "f" * 40), "--json",
                                 expected=3)
                ensure(b"missing_input" in absent.stderr
                       or b"source_missing" in absent.stderr,
                       "missing source did not fail closed")
                invalid = toolkit("check", "--repo", str(checkout),
                                  "--revision", "main", "--course", "SEF1",
                                  expected=3)
                ensure(b"unsupported" in invalid.stderr.lower(),
                       "moving Git branch was not rejected")
            check("OT-02/05/06/16: old and missing sources fail without HEAD fallback",
                  version_support)

            def export_contract():
                for code in COURSES:
                    params = ("export", *input_for(code, revision), "--output", "-")
                    once = toolkit(*params).stdout
                    twice = toolkit(*params).stdout
                    ensure(once == twice and once.endswith(b"\n"),
                           f"{code}: export bytes are not deterministic UTF-8/LF")
                    payload = parse(once)
                    ensure(payload["exportVersion"] == 1
                           and payload["source"]["revision"] == revision
                           and payload["source"]["specification"] == "v0.2.0"
                           and payload["source"]["repository"] == REPOSITORY,
                           f"{code}: wrong source or export identity")
                    ensure(payload["course"]["code"] == code
                           and payload["validation"] == {
                               "structural": "passed", "manualReviewRequired": True,
                           }, f"{code}: unreviewed/unsupported export presented as approved")
                    ensure(payload["outcomes"] and payload["assessments"]
                           and payload["modules"] and payload["coverage"],
                           f"{code}: empty canonical contract")
                    report.setdefault("exportSha256", {})[code] = hashlib.sha256(
                        once
                    ).hexdigest()
            check("OT-17/18/21/24: deterministic course exports and explicit source",
                  export_contract)

            def output_transaction():
                location = destination / "selection.json"
                original = b"valuable learner-owned data, do not overwrite"
                location.write_bytes(original)
                toolkit("export", *input_for("SEF9999", revision), "--output",
                        str(location), expected=3)
                ensure(location.read_bytes() == original,
                       "invalid course export overwrote existing data")
                toolkit("export", *input_for("SEF1", "f" * 40), "--output",
                        str(location), expected=3)
                ensure(location.read_bytes() == original,
                       "missing revision damaged existing output")
                created = destination / "current.json"
                toolkit("export", *input_for("SEF1", revision), "--output", str(created))
                ensure(created.is_file() and parse(created.read_bytes())["course"]["code"]
                       == "SEF1", "standalone UTF-8 file export failed")
                ensure(not list(destination.glob(".*.tmp")),
                       "temporary export debris left in output directory")
            check("OT-08/19: safe output on failed export, local no-network files",
                  output_transaction)

            def verify_golden():
                pins = json.loads(
                    (checkout / "tooling/interop/fixtures/pins.json")
                    .read_text(encoding="utf-8")
                )
                source_pin = pins["source"]["revision"]
                ensure(FULL_SHA.fullmatch(source_pin) is not None,
                       "golden manifest has no exact source pin")
                for code in pins["courses"]:
                    ensure((checkout / f"tooling/interop/golden/{code}.json").is_file(),
                           f"golden {code} absent")
                run([sys.executable, "tooling/interop/verify_golden.py",
                     "--repo", str(checkout)], checkout, env=offline)
                report["pinnedGoldenRevision"] = source_pin
                report["goldenCourses"] = list(pins["courses"])
            check("OT-18/24: immutable golden provenance and byte equality",
                  verify_golden)

            def moved_head():
                original_bytes = toolkit(
                    "export", *input_for("SEF1", revision), "--output", "-"
                ).stdout
                # Git commit changes only this disposable local clone's HEAD.
                run(["git", "-C", str(checkout), "-c", "user.name=OEE smoke",
                     "-c", "user.email=smoke@example.invalid",
                     "-c", "commit.gpgsign=false",
                     "commit", "--quiet", "--allow-empty",
                     "-m", "independent synthetic HEAD movement"], checkout)
                new_head = git(checkout, "rev-parse", "HEAD")
                ensure(new_head != revision, "temporary test commit did not move HEAD")
                returned = toolkit(
                    "export", *input_for("SEF1", revision), "--output", "-"
                ).stdout
                ensure(original_bytes == returned,
                       "changed OEE HEAD modified pinned curriculum export")
                report["headMovedInDisposableClone"] = True
            check("OT-16/17/24: immutable source bytes after local HEAD moves",
                  moved_head)

            def license_and_notice():
                required = (
                    "LICENSE", "LICENSE-MIT", "NOTICE",
                    "tooling/LICENSING.md", "rfcs/0002-toolkit-stewardship-and-licensing.md",
                    "AUTHORS", "CITATION.cff", "TRADEMARKS.md", "DCO.md",
                )
                for file in required:
                    ensure((checkout / file).is_file(), f"required public notice absent: {file}")
                rfc = (checkout / "rfcs/0002-toolkit-stewardship-and-licensing.md"
                       ).read_text(encoding="utf-8")
                licensing = (checkout / "tooling/LICENSING.md"
                             ).read_text(encoding="utf-8")
                notice = (checkout / "NOTICE").read_text(encoding="utf-8")
                ensure("- **Status:** `accepted`" in rfc,
                       "public RFC 0002 is not accepted")
                for needle in ("MIT", "CC BY 4.0", "tooling/interop/golden"):
                    ensure(needle in licensing and needle in notice,
                           f"missing distinct source/content licensing boundary: {needle}")
                require_files = (checkout / "tooling/oee_toolkit/__main__.py",
                                 checkout / "tooling/oee_toolkit/core.py",
                                 checkout / "tooling/oee_toolkit/source.py")
                ensure(all(file.is_file() for file in require_files),
                       "Toolkit implementation not supplied in public source")
                report["licenseNoticeFilesVerified"] = list(required)
                report["rightsAndThirdPartyApproval"] = "human-review-required"
            check("OT-20/21: public MIT/CC BY notices and approved stewardship",
                  license_and_notice)

            def preserve_source():
                ensure(git(checkout, "status", "--porcelain") == "",
                       "independent OEE source clone became dirty")
                ensure(git(source, "rev-parse", "HEAD") ==
                       report["candidateSourceCommit"],
                       "original source repository HEAD changed")
                report["independentCloneClean"] = True
            check("Privacy: no learner data or source edits in Toolkit checkout",
                  preserve_source)

        report["result"] = "passed"
        snapshot(report, options.report)
        return 0
    except (ReleaseCheckFailed, FileNotFoundError, OSError,
            subprocess.TimeoutExpired, UnicodeError, ValueError, KeyError) as exc:
        report["result"] = "failed"
        report["failure"] = {"type": type(exc).__name__, "message": str(exc)}
        snapshot(report, options.report)
        print(f"toolkit_release_smoke_failure: {type(exc).__name__}: {exc}",
              file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
