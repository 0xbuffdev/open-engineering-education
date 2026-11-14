"""Offline immutable Git-blob source for the proposed OEE Toolkit.

Only a full 40-character Git commit SHA selects educational input.
Never reads course content from HEAD, the index, worktree, or a network URL.
"""

from __future__ import annotations

from pathlib import Path, PurePosixPath
import posixpath
import re
import subprocess
from urllib.parse import unquote, urlsplit


REVISION_RE = re.compile(r"[0-9a-f]{40}\Z")
COURSE_PATH_RE = re.compile(
    r"curriculum/[A-Z]{2,6}/[A-Z]{2,6}[1-9]\d*\.md\Z"
)
VIRTUAL_ROOT = Path("/__oee_pinned_git_snapshot__")


class SourceError(Exception):
    def __init__(self, category: str, message: str, path: str = "") -> None:
        super().__init__(message)
        self.category = category
        self.path = path


class GitSource:
    """Read only objects reachable from exactly one local Git commit."""

    def __init__(self, repo: Path, revision: str) -> None:
        self.repo = repo.expanduser().resolve()
        self.revision = revision
        if not REVISION_RE.fullmatch(revision):
            raise SourceError("unsupported_format", "revision must be a full lowercase 40-character commit SHA")
        if not self.repo.is_dir():
            raise SourceError("missing_input", "local Git repository directory not found")
        result = self._git("cat-file", "-t", revision, check=False)
        if result.returncode != 0:
            raise SourceError("missing_input", "selected Git commit is not present locally")
        if result.stdout.strip() != b"commit":
            raise SourceError("unsupported_format", "revision refers to a non-commit Git object")

    def _git(self, *args: str, check: bool = True) -> subprocess.CompletedProcess:
        try:
            result = subprocess.run(
                ["git", "-C", str(self.repo), *args],
                capture_output=True, check=False,
            )
        except OSError as exc:
            raise SourceError("tool_error", f"unable to execute local git: {type(exc).__name__}") from exc
        if check and result.returncode:
            raise SourceError("tool_error", "local Git object lookup failed")
        return result

    @staticmethod
    def safe_path(path: str) -> str:
        if (not path or path.startswith(("/", "\\")) or "\\" in path
                or "\x00" in path or any(part in ("", ".", "..") for part in path.split("/"))
                or ":" in path):
            raise SourceError("unsafe_reference", "unsafe repository-relative source path", path)
        return path

    def read_file(self, path: str) -> str:
        path = self.safe_path(path)
        # Verify the exact selected tree entry; reject symlinks/submodules.
        listing = self._git("ls-tree", "-z", self.revision, "--", path).stdout
        entries = [item for item in listing.split(b"\x00") if item]
        selected = None
        for entry in entries:
            try:
                meta, found_path = entry.split(b"\t", 1)
            except ValueError:
                continue
            if found_path.decode("utf-8") == path:
                selected = meta.decode("ascii").split()
                break
        if selected is None:
            raise SourceError("missing_input", "source blob not found at selected Git commit", path)
        if len(selected) != 3 or selected[1] != "blob":
            raise SourceError("unsafe_reference", "source is not a regular Git blob", path)
        if selected[0] not in ("100644", "100755"):
            raise SourceError("unsafe_reference", "symlink or unsupported Git mode rejected", path)
        raw = self._git("cat-file", "blob", selected[2]).stdout
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise SourceError("parser_limitation", "source blob is not UTF-8", path) from exc

    def list_courses(self) -> list[str]:
        raw = self._git(
            "ls-tree", "-r", "-z", "--name-only", self.revision, "--", "curriculum"
        ).stdout
        names = [item.decode("utf-8") for item in raw.split(b"\x00") if item]
        return sorted(name for name in names if COURSE_PATH_RE.fullmatch(name))

    def brief(self, reference: str, owner: Path, root: Path):
        """Shared validator callback; resolve brief from same immutable Git tree."""
        if root != VIRTUAL_ROOT:
            return None, None, "unsafe_reference"
        try:
            parts = urlsplit(reference)
        except ValueError:
            return None, None, "parser_limitation"
        if parts.scheme or parts.netloc or parts.query:
            return None, None, "parser_limitation"
        target = unquote(parts.path)
        if not target or not target.endswith(".md"):
            return None, None, "parser_limitation"
        if target.startswith(("/", "\\")) or "\\" in target or "\x00" in target:
            return None, None, "unsafe_reference"
        try:
            parent = owner.relative_to(VIRTUAL_ROOT).parent.as_posix()
        except ValueError:
            return None, None, "unsafe_reference"
        joined = posixpath.normpath(posixpath.join(parent, target))
        if joined == ".." or joined.startswith("../") or joined.startswith("/"):
            return None, None, "unsafe_reference"
        try:
            normalized = self.safe_path(joined)
            content = self.read_file(normalized)
        except SourceError as exc:
            return None, VIRTUAL_ROOT / joined, exc.category
        return content, VIRTUAL_ROOT / normalized, None

    @staticmethod
    def virtual_path(relative: str) -> Path:
        return VIRTUAL_ROOT / GitSource.safe_path(relative)

    @staticmethod
    def label(virtual_path: Path) -> str:
        return virtual_path.relative_to(VIRTUAL_ROOT).as_posix()
