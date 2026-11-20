"""REL-I01: deterministic, non-publishing OEE curriculum release manifest.

Release identity is independent of the OEE specification, Toolkit software,
and derived course-export format. This publisher-only module requires an
explicit immutable Git source. A future consumer reads the signed, verified
snapshot without Git; that is REL-I02/REL-I03, not a fallback implemented here.

OEE Markdown remains the only editable educational authority. Course and
linked-brief structural checks are delegated to the ONE existing Toolkit
parser. No second course grammar, grade, conformance or readiness claim.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import posixpath
import re
from urllib.parse import unquote, urlsplit

from .core import REPOSITORY, SPECIFICATION, canonical_json, inspect
from .source import COURSE_PATH_RE, GitSource, SourceError

FORMAT_VERSION = 1
RELEASE_ID_RE = re.compile(r"(?:[0-9]{4})\.(?:0[1-9]|1[0-2])\.[1-9][0-9]*\Z")
HASH_RE = re.compile(r"[0-9a-f]{64}\Z")
SOURCE_SHA_RE = re.compile(r"[0-9a-f]{40}\Z")
CLEAN_NAME_RE = re.compile(r"[A-Za-z0-9_./-]+\Z")
TABLE_ROW_RE = re.compile(
    r"^\|\s*\[([A-Z]{2,6}[1-9][0-9]*)\]\(([^)\n]+)\)\s*\|", re.MULTILINE
)
LOCAL_LINK_RE = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")

MAX_FILE_BYTES = 1_000_000
MAX_RELEASE_BYTES = 32_000_000
MAX_ENTRIES = 2_000
ROOT_FILES = frozenset({"CITATION.cff", "LICENSE", "NOTICE"})
REQUIRED_FILES = ROOT_FILES | {"curriculum/README.md", "spec/README.md"}


class ReleaseManifestError(ValueError):
    """Structural or immutable-source failure, never a publication result."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReleaseManifestError(message)


def release_id(value: object) -> str:
    require(type(value) is str and bool(RELEASE_ID_RE.fullmatch(value)),
            "releaseId must be an explicit YYYY.MM.N calendar release identifier")
    return value


def selected_path(value: object) -> str:
    """Only readable public educational Markdown and attribution are in scope."""
    require(type(value) is str and bool(value) and bool(CLEAN_NAME_RE.fullmatch(value)),
            "noncanonical or unsafe release file path")
    require(not value.startswith("/") and all(
        item not in ("", ".", "..") for item in value.split("/")),
        "release path is absolute, traverses or contains empty components")
    require(
        value in ROOT_FILES or bool(re.fullmatch(
            r"(?:curriculum|spec)/(?:[A-Za-z0-9_-]+/)*[A-Za-z0-9_-]+\.md",
            value,
        )),
        "file is outside the reviewed curriculum/specification/notice allowlist",
    )
    return value


def manifest_shape(value: object) -> dict:
    """Validate the exact v1 structure without a third-party schema dependency.

    This is release-metadata validation, NOT another curriculum parser.
    The public JSON Schema is the machine-readable representation of this
    single format, consumed only by tooling that has verified source bytes.
    """
    require(type(value) is dict and set(value) == {
        "formatVersion", "releaseId", "source", "files"
    }, "manifest must have exactly the v1 top-level fields")
    require(type(value["formatVersion"]) is int and value["formatVersion"] == 1,
            "unsupported curriculum manifest formatVersion")
    release_id(value["releaseId"])
    source = value["source"]
    require(type(source) is dict and set(source) == {
        "repository", "commit", "specification"
    }, "manifest.source has unknown or missing identity fields")
    require(source["repository"] == REPOSITORY and
            source["specification"] == SPECIFICATION and
            type(source["commit"]) is str and
            bool(SOURCE_SHA_RE.fullmatch(source["commit"])),
            "manifest source must identify exact current OEE specification and commit")
    files = value["files"]
    require(type(files) is list and 1 <= len(files) <= MAX_ENTRIES,
            "manifest files must be a bounded nonempty array")
    names: list[str] = []
    total = 0
    for row in files:
        require(type(row) is dict and set(row) == {"path", "sha256", "size"},
                "file entry must contain only path, sha256 and size")
        name = selected_path(row["path"])
        require(type(row["sha256"]) is str and
                bool(HASH_RE.fullmatch(row["sha256"])),
                "file digest must be lowercase full SHA-256: " + name)
        length = row["size"]
        require(type(length) is int and 0 < length <= MAX_FILE_BYTES,
                "file size outside allowed bounds: " + name)
        names.append(name)
        total += length
    require(total <= MAX_RELEASE_BYTES, "source inventory exceeds total size bound")
    require(names == sorted(set(names), key=lambda name: name.encode("utf-8")),
            "manifest paths must be unique and sorted by canonical UTF-8 byte order")
    require(REQUIRED_FILES.issubset(names),
            "missing canonical attribution or curriculum/specification entrypoint")
    require(any(COURSE_PATH_RE.fullmatch(name) for name in names),
            "release contains no supported OEE courses")
    return value


def _git_inventory(source: GitSource) -> list[tuple[str, str, int]]:
    """Read one immutable tree (not HEAD, working files or a network request)."""
    try:
        raw = source._git(
            "ls-tree", "-r", "-l", "-z", source.revision, "--",
            "curriculum", "spec", "CITATION.cff", "LICENSE", "NOTICE",
        ).stdout
    except (OSError, ValueError) as exc:
        raise ReleaseManifestError("cannot enumerate exact Git source tree") from exc
    output: list[tuple[str, str, int]] = []
    for entry in (part for part in raw.split(b"\0") if part):
        try:
            metadata, encoded_path = entry.split(b"\t", 1)
            mode, kind, oid, size_text = metadata.decode("ascii").split()
            name = encoded_path.decode("utf-8", "strict")
            size = int(size_text)
        except (ValueError, UnicodeError) as exc:
            raise ReleaseManifestError("malformed or non-UTF-8 Git source entry") from exc
        selected_path(name)
        require(mode == "100644" and kind == "blob" and
                bool(SOURCE_SHA_RE.fullmatch(oid)) and
                0 < size <= MAX_FILE_BYTES,
                "not a bounded regular UTF-8 source blob: " + name)
        output.append((name, oid, size))
    require(output and len(output) <= MAX_ENTRIES,
            "missing or oversized canonical source inventory")
    require(len({name for name, _, _ in output}) == len(output),
            "duplicate source path")
    return sorted(output, key=lambda item: item[0].encode("utf-8"))


def _file_rows(source: GitSource) -> list[dict]:
    rows = []
    total = 0
    for name, oid, declared_size in _git_inventory(source):
        # GitSource already rejects foreign blobs, symlinks and invalid UTF-8.
        # Compare exact re-encoded bytes with the size from Git's selected tree.
        try:
            body = source.read_file(name).encode("utf-8")
        except SourceError as exc:
            raise ReleaseManifestError(
                "missing, unreadable or unsafe canonical source: " + name
            ) from exc
        require(len(body) == declared_size,
                "source byte-size mismatch at pinned commit: " + name)
        total += declared_size
        require(total <= MAX_RELEASE_BYTES, "release source size limit exceeded")
        rows.append({
            "path": name,
            "sha256": hashlib.sha256(body).hexdigest(),
            "size": declared_size,
        })
    return rows


def _catalog_closure(source: GitSource, paths: set[str]) -> list[str]:
    """Require every canonical course exactly once in its program catalog.

    This checks academic source *references*, not pedagogical semantics or
    a second grammar for course assessments. OEE's existing Toolkit parser
    performs the actual course and assessment structural evaluation.
    """
    course_paths = sorted(
        (name for name in paths if COURSE_PATH_RE.fullmatch(name)),
        key=lambda name: name.encode("utf-8"),
    )
    codes = {Path(name).stem: name for name in course_paths}
    require(len(codes) == len(course_paths), "ambiguous canonical course identity")
    require(set(source.list_courses()) == set(course_paths),
            "manifest course set differs from the selected full OEE Git tree")
    programs = {Path(name).parent.name for name in course_paths}
    root_catalog = source.read_file("curriculum/README.md")
    for program in programs:
        catalog_path = f"curriculum/{program}/README.md"
        require(catalog_path in paths, "program catalog absent: " + program)
        require(f"({program}/README.md)" in root_catalog,
                "root curriculum catalog omits program: " + program)
        content = source.read_file(catalog_path)
        rows = TABLE_ROW_RE.findall(content)
        require(bool(rows), "program catalog lacks course rows: " + program)
        seen: set[str] = set()
        for code, destination in rows:
            require(code not in seen, "duplicated catalog course: " + code)
            seen.add(code)
            require(destination == f"{code}.md",
                    "catalog course link does not match canonical path: " + code)
            require(codes.get(code) == f"curriculum/{program}/{code}.md",
                    "catalog references unknown or foreign course: " + code)
        expected = {code for code in codes if code.startswith(program) and
                    codes[code].startswith(f"curriculum/{program}/")}
        require(seen == expected,
                "program catalog omitted an active course or contains an extra course: " +
                program)
        # Validate relative curriculum/spec links in program catalogs. URLs
        # and informational links to the external repository are not bundled
        # sources; linked OEE course/assessment references must resolve.
        _local_source_links(content, catalog_path, paths)
    _local_source_links(root_catalog, "curriculum/README.md", paths)
    return [Path(p).stem for p in course_paths]


def _local_source_links(markdown: str, owner: str, paths: set[str]) -> None:
    for reference in LOCAL_LINK_RE.findall(markdown):
        try:
            parsed = urlsplit(reference)
        except ValueError as exc:
            raise ReleaseManifestError("malformed catalog source link: " + owner) from exc
        if parsed.scheme or parsed.netloc:
            continue
        if parsed.query:
            raise ReleaseManifestError("unsupported query in source link: " + owner)
        target = unquote(parsed.path)
        if not target:
            continue  # local heading/anchor
        require(not target.startswith(("/", "\\")) and "\\" not in target,
                "absolute or unsafe source link: " + owner)
        resolved = posixpath.normpath(posixpath.join(posixpath.dirname(owner), target))
        require(resolved != ".." and not resolved.startswith(("../", "/")),
                "source link escapes public OEE repository: " + owner)
        # Only local academic sources are part of the distribution contract;
        # editorial/rfcs/CONTRIBUTING links remain on the original OEE site.
        if resolved.startswith(("curriculum/", "spec/")) and resolved.endswith(".md"):
            require(resolved in paths,
                    "catalog references missing academic source: " + resolved)


def verify_source_closure(source: GitSource, manifest: dict) -> None:
    """Fail unless every source, catalog, public brief and course is complete."""
    files = {item["path"] for item in manifest["files"]}
    codes = _catalog_closure(source, files)
    for code in codes:
        report, extracted = inspect(source, code)
        require(report["structuralOutcome"] == "passed" and
                report["checksPerformed"] == ["v0.2.0-structure"] and
                not report["checksSkipped"] and not report["findings"] and
                report["manualReviewRequired"] is True and extracted is not None,
                "Toolkit rejected incomplete or unsupported academic source: " + code)
        # Linked public assessment briefs may own their actual criteria:
        # every source-located reference used by the one parser MUST be
        # included in the complete manifest; never publish a partial brief.
        for kind in ("outcomes", "assessments"):
            for item in extracted[kind]:
                location = item["location"]
                require(location["path"] in files,
                        "source-located " + kind + " refers outside release: " +
                        location["path"])


def build_manifest(source: GitSource, candidate_id: str) -> dict:
    """Derive a candidate from a complete pinned Git tree, without publishing."""
    value = {
        "formatVersion": FORMAT_VERSION,
        "releaseId": release_id(candidate_id),
        "source": {
            "repository": REPOSITORY,
            "commit": source.revision,
            "specification": SPECIFICATION,
        },
        "files": _file_rows(source),
    }
    manifest_shape(value)
    verify_source_closure(source, value)
    return value


def verify_manifest(source: GitSource, value: object) -> dict:
    """Verify an exact manifest against a selected Git commit and full closure.

    REL-I01 is a *publisher-side* check. The Git-free release installer and
    local consumer resolver are distinct, not yet implemented milestones.
    """
    manifest = manifest_shape(value)
    require(manifest["source"]["commit"] == source.revision,
            "release manifest references a different immutable Git commit")
    actual = _file_rows(source)
    require(manifest["files"] == actual,
            "manifest file inventory, source digests or completeness disagree with Git")
    verify_source_closure(source, manifest)
    return manifest


def digest_manifest(value: dict) -> str:
    return hashlib.sha256(canonical_json(manifest_shape(value))).hexdigest()


def read_canonical_manifest(raw: bytes) -> dict:
    require(len(raw) <= 256_000, "manifest exceeds safe size limit")
    try:
        data = json.loads(raw.decode("utf-8", "strict"))
    except (UnicodeError, ValueError) as exc:
        raise ReleaseManifestError("manifest is not valid UTF-8 JSON") from exc
    manifest_shape(data)
    require(raw == canonical_json(data),
            "manifest is not canonical, deterministic UTF-8 JSON")
    return data
