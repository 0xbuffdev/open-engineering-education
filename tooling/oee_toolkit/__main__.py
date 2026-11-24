"""OEE Toolkit consumer CLI: offline releases, no Git or moving source refs.

The approved project lock is the only source selector. This entrypoint
retains course exportVersion 2 and offers a separately versioned assessment-context
export; neither falls back to v1 course export, HEAD,
a repository checkout, guessed default course, network, or cached latest.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .core import ExportBlocked, canonical_json, outcome
from ._publisher_cli import atomic_write
from .release_manifest import ReleaseManifestError
from .release_source import (
    LOCK_FILENAME, export_release_course, inspect_release, resolve_release,
)
from .source import SourceError


def build_parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(description=__doc__)
    actions = cli.add_subparsers(dest="command", required=True)
    for name in ("check", "export", "assessment-context"):
        cmd = actions.add_parser(name, help=(
            "inspect selected release course(s)" if name == "check"
            else ("export a structurally valid course from the pinned release"
                  if name == "export" else "export source-bound assessment review context")
        ))
        if name == "check":
            cmd.add_argument("course", nargs="?",
                             help="canonical OEE course code, for example SEF1")
        else:
            cmd.add_argument("course",
                             help="required canonical OEE course code, for example SEF1")
        cmd.add_argument("--lock", type=Path, default=None,
                         help="explicit project lock; defaults only to ./oee-curriculum.lock.json")
        cmd.add_argument("--store", type=Path, default=None,
                         help="existing trusted installed-release store")
        if name == "check":
            cmd.add_argument("--all", action="store_true",
                             help="inspect every course from the locked release")
            cmd.add_argument("--json", action="store_true",
                             help="emit deterministic inspection JSON")
        else:
            cmd.add_argument("--output", required=True,
                             help="write UTF-8 JSON atomically to path, or '-' for stdout")
    return cli


def _summarize(reports: list[dict], source, *, all_courses: bool) -> dict:
    findings = [item for report in reports for item in report["findings"]]
    return {
        "toolVersion": reports[0]["toolVersion"],
        "ruleSetVersion": reports[0]["ruleSetVersion"],
        "source": {
            "repository": source.manifest["source"]["repository"],
            "releaseId": source.release_id,
            "manifestSha256": source.manifest_sha256,
            "specification": source.manifest["source"]["specification"],
            "originCommit": source.revision,
        },
        "scope": "repository" if all_courses else "course",
        "checksPerformed": ["v0.2.0-structure"] if any(
            r["checksPerformed"] for r in reports) else [],
        "checksSkipped": [
            {"course": r["source"]["coursePath"], **skip}
            for r in reports for skip in r["checksSkipped"]
        ],
        "findings": findings,
        "structuralOutcome": outcome(findings),
        "manualReviewRequired": True,
        "courses": reports,
    }


def _print_report(report: dict) -> None:
    address = report["source"]
    print(f"{address['coursePath']} [release {address['releaseId']}]: "
          f"{report['structuralOutcome']}", file=sys.stderr)
    for finding in report["findings"]:
        at = finding["location"]
        print(f"{at['path']}:{at['line']}: {finding['code']} "
              f"[{finding['category']}]: {finding['message']}", file=sys.stderr)
    print("Structural check only; academic review remains necessary.",
          file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    cli = build_parser()
    args = cli.parse_args(argv)
    if args.command == "check" and bool(args.course) == bool(args.all):
        cli.error("check requires exactly one course or --all")
    lock = args.lock if args.lock is not None else Path.cwd() / LOCK_FILENAME
    try:
        source = resolve_release(lock, args.store)
        if args.command in ("export", "assessment-context"):
            try:
                if args.command == "assessment-context":
                    from .assessment_context import export_assessment_context
                    data = export_assessment_context(source, args.course)
                else:
                    data = export_release_course(source, args.course)
            except ExportBlocked as exc:
                _print_report(exc.report)
                return 1 if exc.report["structuralOutcome"] == "failed" else 3
            atomic_write(args.output, canonical_json(data))
            return 0

        codes = source.list_courses() if args.all else [args.course]
        if args.all:
            codes = [Path(code).stem for code in codes]
        if not codes:
            print("missing_input: no courses in the selected curriculum release",
                  file=sys.stderr)
            return 3
        reports = [inspect_release(source, code)[0] for code in codes]
        summary = _summarize(reports, source, all_courses=args.all)
        if args.json:
            sys.stdout.buffer.write(canonical_json(summary))
        else:
            for report in reports:
                _print_report(report)
        return 0 if summary["structuralOutcome"] == "passed" else (
            1 if summary["structuralOutcome"] == "failed" else 3)
    except ReleaseManifestError as exc:
        print(f"invalid_release: {exc}", file=sys.stderr)
        return 3
    except SourceError as exc:
        print(f"{exc.category}: {exc}", file=sys.stderr)
        return 1 if exc.category in ("invalid_reference", "unsafe_reference") else 3
    except OSError as exc:
        print(f"tool_error: release filesystem input unavailable: {type(exc).__name__}",
              file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
