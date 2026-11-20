"""REL-I02: immutable OEE curriculum archive and explicit offline trust gate.

This is derived *distribution*, not a new OEE parser or publication authority.
Only the publisher reads Git; safe consumers verify a pinned archive digest
and a detached Ed25519 signature from an independently trusted steward key.

The archive is byte-stable USTAR with regular files, known attributes, sorted
POSIX paths, and no extended headers or compression. It has one release.json
manifest plus exactly its listed source bytes. No implicit downloads.
"""

from __future__ import annotations

import hashlib
import io
import os
from pathlib import Path
import re
import tarfile
import tempfile

from .core import canonical_json
from .release_manifest import (
    MAX_ENTRIES, MAX_FILE_BYTES, ReleaseManifestError,
    digest_manifest, manifest_shape, read_canonical_manifest, require,
    selected_path,
)
from .source import GitSource, SourceError

MAX_ARCHIVE_BYTES = 40 * 1024 * 1024
MANIFEST_NAME = "release.json"
ATTESTATION_VERSION = 1
DIGEST_RE = re.compile(r"[0-9a-f]{64}\Z")


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _verify_source_bytes(manifest: dict, contents: dict[str, bytes]) -> None:
    expected = {row["path"] for row in manifest["files"]}
    require(set(contents) == expected, "archive file set differs from manifest")
    for row in manifest["files"]:
        name = row["path"]
        value = contents[name]
        require(type(value) is bytes and len(value) == row["size"] and
                sha256(value) == row["sha256"],
                "source bytes or SHA-256 disagree with manifest: " + name)
        try:
            value.decode("utf-8", "strict")
        except UnicodeError as exc:
            raise ReleaseManifestError("not UTF-8 source: " + name) from exc


def canonical_archive(manifest: dict, contents: dict[str, bytes]) -> bytes:
    """Build one exact canonical USTAR stream; never extract untrusted paths."""
    manifest_shape(manifest)
    _verify_source_bytes(manifest, contents)
    raw_manifest = canonical_json(manifest)
    require(len(raw_manifest) <= 256_000, "release.json exceeds v1 size limit")
    entries = {**contents, MANIFEST_NAME: raw_manifest}
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:", format=tarfile.USTAR_FORMAT) as archive:
        for name in sorted(entries, key=lambda item: item.encode("utf-8")):
            data = entries[name]
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.type = tarfile.REGTYPE
            info.mode = 0o644
            info.uid = info.gid = 0
            info.uname = info.gname = ""
            info.mtime = 0
            info.pax_headers = {}
            archive.addfile(info, io.BytesIO(data))
    produced = buffer.getvalue()
    require(len(produced) <= MAX_ARCHIVE_BYTES, "candidate archive exceeds size bound")
    return produced


def build_archive(source: GitSource, release_id: str) -> tuple[dict, bytes]:
    """Publisher-only: require complete source closure before reading bytes."""
    from .release_manifest import build_manifest
    manifest = build_manifest(source, release_id)
    files = {}
    for row in manifest["files"]:
        try:
            # GitSource supplies exact blob text at the selected immutable commit.
            files[row["path"]] = source.read_file(row["path"]).encode("utf-8")
        except SourceError as exc:
            raise ReleaseManifestError(
                "selected source blob unavailable: " + row["path"]) from exc
    return manifest, canonical_archive(manifest, files)


def inspect_archive(archive_bytes: bytes, expected_manifest_sha256: str) -> tuple[dict, dict[str, bytes]]:
    """Read a strictly canonical archive, reject unsafe content before writes.

    An exact digest is required from a *previously approved* source/lock.
    Consistent bytes alone are not authentication; use verify_attestation
    with a trusted steward public key before considering installation.
    """
    require(type(expected_manifest_sha256) is str and
            bool(DIGEST_RE.fullmatch(expected_manifest_sha256)),
            "expected manifest digest must be a full SHA-256")
    require(type(archive_bytes) is bytes and
            0 < len(archive_bytes) <= MAX_ARCHIVE_BYTES,
            "release archive exceeds bounded byte limit")
    contents: dict[str, bytes] = {}
    try:
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:") as archive:
            members = archive.getmembers()
            require(1 < len(members) <= MAX_ENTRIES + 1,
                    "release archive has missing or excessive entries")
            for info in members:
                name = info.name
                if name != MANIFEST_NAME:
                    selected_path(name)
                require(name not in contents, "duplicate archive entry: " + name)
                require(info.type in (tarfile.REGTYPE, tarfile.AREGTYPE) and
                        info.isfile() and info.uid == 0 and info.gid == 0 and
                        info.uname == "" and info.gname == "" and
                        info.mode == 0o644 and info.mtime == 0 and
                        not info.linkname and not info.pax_headers and
                        0 < info.size <= (256_000 if name == MANIFEST_NAME
                                          else MAX_FILE_BYTES),
                        "unsafe archive entry type, metadata, or size: " + name)
                reader = archive.extractfile(info)
                require(reader is not None, "archive entry cannot be read: " + name)
                with reader:
                    data = reader.read(info.size + 1)
                require(len(data) == info.size, "archive entry truncated: " + name)
                contents[name] = data
    except (tarfile.TarError, EOFError, OSError, OverflowError) as exc:
        raise ReleaseManifestError("malformed or unsafe USTAR input") from exc
    require(MANIFEST_NAME in contents, "archive is missing release.json")
    raw_manifest = contents.pop(MANIFEST_NAME)
    require(sha256(raw_manifest) == expected_manifest_sha256,
            "release manifest digest differs from the approved lock")
    manifest = read_canonical_manifest(raw_manifest)
    _verify_source_bytes(manifest, contents)
    # A byte-identical rebuild rejects hidden PAX/GNU headers, ordering
    # changes, extra padding/trailing data, ambiguous duplicate members,
    # noncanonical filenames and platform-specific metadata.
    require(canonical_archive(manifest, contents) == archive_bytes,
            "archive is not byte-for-byte canonical USTAR")
    return manifest, contents


def attestation_claims(archive_bytes: bytes, manifest: dict) -> dict:
    """The separate human-reviewed, signed subject: source and archive."""
    return {
        "attestationVersion": ATTESTATION_VERSION,
        "releaseId": manifest["releaseId"],
        "manifestSha256": digest_manifest(manifest),
        "archiveSha256": sha256(archive_bytes),
    }


def _private_key(pem: bytes):
    try:
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
    except ImportError as exc:
        raise ReleaseManifestError(
            "signing needs the reviewed optional oee-toolkit[release] dependency"
        ) from exc
    try:
        key = serialization.load_pem_private_key(pem, password=None)
    except (TypeError, ValueError) as exc:
        raise ReleaseManifestError("invalid unencrypted signing key") from exc
    require(isinstance(key, Ed25519PrivateKey),
            "only Ed25519 steward signing keys are permitted")
    return key


def _public_key(pem: bytes):
    try:
        from cryptography.hazmat.primitives import serialization
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
    except ImportError as exc:
        raise ReleaseManifestError(
            "verification needs the reviewed optional oee-toolkit[release] dependency"
        ) from exc
    try:
        key = serialization.load_pem_public_key(pem)
    except (TypeError, ValueError) as exc:
        raise ReleaseManifestError("invalid trusted public key") from exc
    require(isinstance(key, Ed25519PublicKey),
            "trusted release key must be Ed25519")
    return key


def sign_candidate(archive_bytes: bytes, manifest_digest: str,
                   private_key_pem: bytes) -> tuple[bytes, bytes]:
    """Explicit maintainer action; never generate or select a steward key."""
    manifest, _ = inspect_archive(archive_bytes, manifest_digest)
    attestation = canonical_json(attestation_claims(archive_bytes, manifest))
    return attestation, _private_key(private_key_pem).sign(attestation)


def verify_attestation(archive_bytes: bytes, expected_manifest_sha256: str,
                       attestation_bytes: bytes, signature: bytes,
                       trusted_public_key_pem: bytes) -> dict:
    """A checksum is not authorship; verify a trusted *externally pinned* key."""
    manifest, _ = inspect_archive(archive_bytes, expected_manifest_sha256)
    expected = canonical_json(attestation_claims(archive_bytes, manifest))
    require(type(attestation_bytes) is bytes and attestation_bytes == expected,
            "signed attestation claims disagree with exact candidate")
    require(type(signature) is bytes and len(signature) == 64,
            "detached Ed25519 signature has invalid length")
    public_key = _public_key(trusted_public_key_pem)
    try:
        from cryptography.exceptions import InvalidSignature
        public_key.verify(signature, attestation_bytes)
    except InvalidSignature as exc:
        raise ReleaseManifestError("signature is not from the trusted steward key") from exc
    return manifest


def _trusted_store(store: Path) -> Path:
    """Caller chooses an already-existing trusted directory; never create it."""
    store = store.expanduser().absolute()
    require(store.is_dir() and not store.is_symlink(),
            "release store must be an existing real trusted directory")
    return store


def _no_symlink_entry(path: Path) -> bool:
    return not path.exists() and not path.is_symlink()


def install_verified_archive(archive_bytes: bytes, manifest_digest: str,
                             attestation_bytes: bytes, signature: bytes,
                             trusted_public_key_pem: bytes, store: Path) -> Path:
    """Offline, no-clobber installation after *all* signature and source checks.

    The store is a caller-owned trusted location. Cooperative concurrent
    installers use an O_EXCL lock. The lock guarantees only one Toolkit
    installer; untrusted local processes with write access to the store are
    outside this trust boundary and must not be granted such access.
    """
    manifest = verify_attestation(archive_bytes, manifest_digest,
                                  attestation_bytes, signature,
                                  trusted_public_key_pem)
    _, contents = inspect_archive(archive_bytes, manifest_digest)
    destination_root = _trusted_store(store)
    target = destination_root / manifest_digest
    lock = destination_root / ".oee-install.lock"
    try:
        fd = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except (OSError, FileExistsError) as exc:
        raise ReleaseManifestError("release store is locked or not writable") from exc

    staged: Path | None = None
    try:
        os.close(fd)
        require(_no_symlink_entry(target),
                "immutable manifest digest already installed: no overwrite")
        for entry in destination_root.iterdir():
            if not DIGEST_RE.fullmatch(entry.name):
                continue
            require(not entry.is_symlink() and entry.is_dir(),
                    "unsafe indexed digest entry in trusted store")
            registered = entry / MANIFEST_NAME
            require(registered.is_file() and not registered.is_symlink(),
                    "unverifiable existing release store entry")
            try:
                bytes_on_disk = registered.read_bytes()
                prior = read_canonical_manifest(bytes_on_disk)
            except (OSError, ValueError) as exc:
                raise ReleaseManifestError("invalid existing release manifest") from exc
            require(sha256(bytes_on_disk) == entry.name,
                    "existing release manifest digest disagrees with its cache key")
            require(prior["releaseId"] != manifest["releaseId"],
                    "releaseId is already installed under another digest; no repin")
        staged = Path(tempfile.mkdtemp(prefix=".oee-stage-", dir=destination_root))
        files = {**contents, MANIFEST_NAME: canonical_json(manifest)}
        for name in sorted(files):
            path = staged.joinpath(*name.split("/"))
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as writer:
                writer.write(files[name])
                writer.flush()
                os.fsync(writer.fileno())
            if os.name != "nt":
                path.chmod(0o444)
        require(_no_symlink_entry(target), "release appeared during staging; no overwrite")
        os.rename(staged, target)
        staged = None
        return target
    except (OSError, ValueError) as exc:
        if isinstance(exc, ReleaseManifestError):
            raise
        raise ReleaseManifestError("immutable installation failed without activation") from exc
    finally:
        if staged is not None:
            import shutil
            shutil.rmtree(staged)
        lock.unlink(missing_ok=True)
