"""Publisher-only Git source inspection CLI used for OEE maintenance and golden tests.

Not the installed consumer entrypoint. No backwards-compatible consumer reader.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys
import tempfile

from .core import ExportBlocked, canonical_json, export_course, inspect, outcome
from .source import GitSource, SourceError


def status_code(state: str) -> int:
    return {"passed": 0, "failed": 1, "incomplete": 3}[state]


def print_inspection(report: dict) -> None:
    source = report["source"]
    location = source.get("coursePath", "(repository)")
    print(f"{location} [{source['revision']}]: {report['structuralOutcome']}",
          file=sys.stderr)
    for finding in report["findings"]:
        at = finding["location"]
        print(f"{at['path']}:{at['line']}: {finding['code']} "
              f"[{finding['category']}]: {finding['message']}",
              file=sys.stderr)
    print("Structural inspection only; substantive review required.",
          file=sys.stderr)


def atomic_write(target: str, data: bytes) -> None:
    if target == "-":
        sys.stdout.buffer.write(data)
        return
    file = Path(target).expanduser()
    if not file.parent.is_dir():
        raise SourceError("missing_input", "output parent directory does not exist")
    if file.is_symlink():
        raise SourceError("unsafe_reference", "refusing to replace a symlink output")
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=file.parent, prefix=f".{file.name}.", suffix=".tmp", delete=False
        ) as temp:
            temp_path = Path(temp.name)
            temp.write(data)
            temp.flush()
            os.fsync(temp.fileno())
        os.replace(temp_path, file)
    except OSError as exc:
        raise SourceError("tool_error", f"atomic export write failed: {type(exc).__name__}") from exc
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="inspect a pinned course or repository")
    export = sub.add_parser("export", help="export one structurally valid pinned course")
    for command in (check, export):
        command.add_argument("--repo", required=True, type=Path,
                             help="local OEE Git repository (never fetched remotely)")
        command.add_argument("--revision", required=True,
                             help="exact full 40-character Git commit SHA")
    selector = check.add_mutually_exclusive_group(required=True)
    selector.add_argument("--course", help="canonical course code, e.g. SEF1")
    selector.add_argument("--all", action="store_true",
                          help="inspect all active course files; unsupported inputs are incomplete")
    check.add_argument("--json", action="store_true",
                       help="write deterministic machine-readable structural diagnostics")
    export.add_argument("--course", required=True)
    export.add_argument("--output", required=True,
                        help="write UTF-8 JSON atomically to path, or '-' for stdout")
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        source = GitSource(args.repo, args.revision)
        if args.command == "export":
            try:
                result = export_course(source, args.course)
            except ExportBlocked as exc:
                print_inspection(exc.report)
                return status_code(exc.report["structuralOutcome"])
            atomic_write(args.output, canonical_json(result))
            return 0

        codes = ([args.course] if args.course else [
            Path(path).stem for path in source.list_courses()
        ])
        if not codes:
            print("No active OEE course files at selected revision", file=sys.stderr)
            return 3
        reports = [inspect(source, code)[0] for code in codes]
        overall = outcome([finding for report in reports
                           for finding in report["findings"]])
        if args.json:
            summary = {
                "toolVersion": reports[0]["toolVersion"],
                "ruleSetVersion": reports[0]["ruleSetVersion"],
                "source": {"repository": reports[0]["source"]["repository"],
                           "revision": source.revision,
                           "specification": reports[0]["source"]["specification"]},
                "scope": "repository" if args.all else "course",
                "checksPerformed": ["v0.2.0-structure"] if any(
                    report["checksPerformed"] for report in reports
                ) else [],
                "checksSkipped": [
                    {"course": r["source"]["coursePath"], **skipped}
                    for r in reports for skipped in r["checksSkipped"]
                ],
                "findings": [
                    finding for report in reports for finding in report["findings"]
                ],
                "structuralOutcome": overall,
                "manualReviewRequired": True,
                "courses": reports,
            }
            sys.stdout.buffer.write(canonical_json(summary))
        else:
            for report in reports:
                print_inspection(report)
            print(f"{len(reports)} inspected, "
                  f"{sum(r['structuralOutcome'] == 'passed' for r in reports)} passed, "
                  f"{sum(r['structuralOutcome'] == 'incomplete' for r in reports)} incomplete, "
                  f"{sum(r['structuralOutcome'] == 'failed' for r in reports)} failed.",
                  file=sys.stderr)
        return status_code(overall)
    except SourceError as exc:
        print(f"{exc.category}: {exc}", file=sys.stderr)
        return 4 if exc.category == "tool_error" else (
            1 if exc.category in ("unsafe_reference", "invalid_reference") else 3
        )
    except Exception as exc:
        print(f"tool_error: unexpected {type(exc).__name__}: {exc}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
