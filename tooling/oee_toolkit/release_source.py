"""REL-I03: read-only, offline, digest-locked curriculum source adapter.

Source archives are built and signed separately (REL-I01/I02). Consumers
read a pre-installed snapshot by its exact manifest SHA-256 and *never* use
Git, network discovery, mutable tags, implicit upgrades or v1 export data.
This adapts immutable bytes to the ONE existing OEE course parser.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
import sys

from .core import REPOSITORY, SPECIFICATION, TOOL_VERSION, RULE_SET_VERSION
from .release_manifest import (
    ReleaseManifestError, read_canonical_manifest,
    release_id, require,
)
from .source import COURSE_PATH_RE, GitSource, SourceError

LOCK_FILENAME = "oee-curriculum.lock.json"
LOCK_VERSION = 1
HEX_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
LOCK_MAX_BYTES = 4096


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _unique_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate release lock JSON property: " + key)
        result[key] = value
    return result


def read_lock(path: Path) -> dict:
    """Require one explicit project lock, never search parents or home."""
    path = path.expanduser().absolute()
    require(path.is_file() and not path.is_symlink(),
            "release lock is missing, not a regular file or is a symlink")
    require(path.stat().st_size <= LOCK_MAX_BYTES, "release lock exceeds size limit")
    try:
        data = json.loads(path.read_bytes().decode("utf-8", "strict"),
                          object_pairs_hook=_unique_keys)
    except (UnicodeError, ValueError, OSError) as exc:
        raise ReleaseManifestError("release lock must be valid unique-key UTF-8 JSON") from exc
    require(type(data) is dict and set(data) == {
        "formatVersion", "releaseId", "manifestSha256"
    }, "release lock requires only the v1 identity fields")
    require(type(data["formatVersion"]) is int and data["formatVersion"] == LOCK_VERSION,
            "unsupported release lock formatVersion")
    release_id(data["releaseId"])
    require(type(data["manifestSha256"]) is str and
            bool(HEX_SHA256.fullmatch(data["manifestSha256"])),
            "release lock must pin full lowercase manifest SHA-256")
    return data


def default_store() -> Path:
    """Cache lookup only; never make directories or populate a store."""
    if os.name == "nt":
        root = os.environ.get("LOCALAPPDATA")
        require(bool(root), "LOCALAPPDATA must identify the trusted user cache")
        return Path(root) / "oee" / "curriculum-releases"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Caches" / "oee" / "curriculum-releases"
    root = os.environ.get("XDG_CACHE_HOME")
    base = Path(root) if root else Path.home() / ".cache"
    require(base.is_absolute(), "XDG_CACHE_HOME must be an absolute path")
    return base / "oee" / "curriculum-releases"


class ReleaseSource(GitSource):
    """Adapt verified snapshots to GitSource's *parser-facing* methods.

    The inheritance shares the brief/link resolution and safe virtual source
    path logic verbatim; GitSource.__init__ and ._git are NEVER invoked here.
    The internal source commit is provenance only, not a consumer input.
    """

    def __init__(self, manifest: dict, manifest_sha256: str,
                 verified_files: dict[str, bytes]) -> None:
        self.manifest = manifest
        self.manifest_sha256 = manifest_sha256
        self.release_id = manifest["releaseId"]
        self.revision = manifest["source"]["commit"]
        self._files = verified_files
        self._hashes = {row["path"]: row["sha256"] for row in manifest["files"]}

    def _git(self, *args: str, **kwargs):
        raise AssertionError("REL-I03 consumer attempted to invoke Git")

    def read_file(self, path: str) -> str:
        path = self.safe_path(path)
        if path not in self._files:
            raise SourceError("missing_input", "file absent from verified release", path)
        return self._files[path].decode("utf-8", "strict")

    def course_sha256(self, path: str) -> str:
        path = self.safe_path(path)
        if path not in self._hashes:
            raise SourceError("missing_input", "course not in installed release", path)
        return self._hashes[path]

    def list_courses(self) -> list[str]:
        return sorted(path for path in self._files if COURSE_PATH_RE.fullmatch(path))


def _check_store_entry(root: Path, digest: str) -> Path:
    root = root.expanduser().absolute()
    require(root.is_dir() and not root.is_symlink(),
            "trusted release store is missing or symlinked")
    selected = root / digest
    require(selected.is_dir() and not selected.is_symlink(),
            "pinned curriculum release is not installed")
    return selected


def resolve_release(lock_path: Path, store: Path | None = None) -> ReleaseSource:
    """Read and re-hash every installed file, reject anything not in manifest.

    The installer already verified a steward-signed attestation against its
    independently trusted key. This offline resolver verifies the reviewed
    lock and *current bytes*; it does not mistake a checksum for identity
    authorization or download an alternative release.
    """
    lock = read_lock(lock_path)
    digest = lock["manifestSha256"]
    entry = _check_store_entry(store if store is not None else default_store(), digest)
    manifest_file = entry / "release.json"
    require(manifest_file.is_file() and not manifest_file.is_symlink(),
            "installed release has no regular canonical manifest")
    raw_manifest = manifest_file.read_bytes()
    require(sha256(raw_manifest) == digest, "installed release manifest digest mismatch")
    manifest = read_canonical_manifest(raw_manifest)
    require(manifest["releaseId"] == lock["releaseId"],
            "release ID disagrees with pinned project lock")
    require(manifest["source"]["repository"] == REPOSITORY and
            manifest["source"]["specification"] == SPECIFICATION,
            "release source is incompatible with this Toolkit")

    expected_files = {row["path"] for row in manifest["files"]} | {"release.json"}
    expected_dirs: set[str] = set()
    for name in expected_files:
        parts = name.split("/")
        expected_dirs.update("/".join(parts[:i]) for i in range(1, len(parts)))
    actual_files: set[str] = set()
    actual_dirs: set[str] = set()
    for item in entry.rglob("*"):
        relative = item.relative_to(entry).as_posix()
        require(not item.is_symlink(),
                "installed release contains a symlink: " + relative)
        if item.is_dir():
            actual_dirs.add(relative)
        elif item.is_file():
            actual_files.add(relative)
        else:
            raise ReleaseManifestError("installed release has unsupported entry: " + relative)
    require(actual_files == expected_files and actual_dirs == expected_dirs,
            "installed release has missing, unlisted or altered file layout")

    verified: dict[str, bytes] = {}
    for row in manifest["files"]:
        name = row["path"]
        data = (entry / name).read_bytes()
        require(len(data) == row["size"] and sha256(data) == row["sha256"],
                "installed source bytes differ from reviewed manifest: " + name)
        try:
            data.decode("utf-8", "strict")
        except UnicodeError as exc:
            raise ReleaseManifestError("installed source is not valid UTF-8: " + name) from exc
        verified[name] = data

    # No Git, subprocess, network, filesystem writes, or source read fallback.
    return ReleaseSource(manifest, digest, verified)


def release_source_identity(source: ReleaseSource, course_path: str) -> dict:
    return {
        "repository": REPOSITORY,
        "releaseId": source.release_id,
        "manifestSha256": source.manifest_sha256,
        "specification": SPECIFICATION,
        "coursePath": course_path,
        "courseSha256": source.course_sha256(course_path),
        "originCommit": source.revision,
    }


def inspect_release(source: ReleaseSource, code: str) -> tuple[dict, dict | None]:
    """One canonical parser, with release identity replacing Git CLI identity."""
    from .core import inspect
    report, extracted = inspect(source, code)
    report["source"] = release_source_identity(source, report["source"]["coursePath"])
    return report, extracted


def export_release_course(source: ReleaseSource, code: str) -> dict:
    """Only active consumer format v2; no v1 runtime export or fallback."""
    from .core import ExportBlocked
    report, data = inspect_release(source, code)
    if data is None:
        raise ExportBlocked(report)
    return release_course_payload(report, data)


def release_course_payload(report: dict, data: dict) -> dict:
    """One v2 envelope shared with the assessment-context digest."""
    from .core import course_payload
    return {
        "exportVersion": 2,
        "source": report["source"],
        "toolkit": {"toolVersion": TOOL_VERSION, "ruleSetVersion": RULE_SET_VERSION},
        **course_payload(data),
    }
