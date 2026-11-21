# REL-I03 — Git-free installed curriculum resolution and export v2

**Status: current-only Toolkit implementation candidate, not a published
OEE curriculum release, approved Toolkit release, Workspace/Content migration,
academic conformance decision, learner credit or hosted deployment.**

This milestone implements the consumer side of
[accepted RFC 0005](../rfcs/0005-immutable-curriculum-releases.md), after
[REL-I01](RELEASE-MANIFEST.md) and [REL-I02](RELEASE-ARCHIVE.md).
It is tracked in [issue #257](https://github.com/0xbuffdev/open-engineering-education/issues/257).

## One curriculum authority and one active consumer contract

The only authoritative academic sources remain the OEE public curriculum,
program catalogues and assessment briefs. REL-I01 produces the immutable
source inventory; REL-I02 builds and independently verifies a detached,
steward-signed archive before installation. The consumer never treats an
export or an archived course as a separately editable academic source.

REL-I03 selects **one** approved release by its human release ID **and exact
manifest SHA-256**, with the full Git commit preserved **inside** the
signed manifest for audits, never as a learner/author CLI argument.

The installed binary `oee-toolkit` and `python -m oee_toolkit` expose only:

```sh
oee-toolkit check SEF1 --json
oee-toolkit check --all --json
oee-toolkit export SEF1 --output sef1.json
```

Default project source selection uses only
`./oee-curriculum.lock.json` in the current directory. The caller may
provide `--lock` and `--store` explicitly in hermetic CI or private Content.
Neither CLI accepts `--repo`, `--revision`, a moving `latest`, a network
repository, nor an exportVersion-1 input. The publisher-only
`tooling.oee_toolkit._publisher_cli` retains exact-Git source inspection
for build verification and historical golden test generation; it is **not**
a consumer fallback or an alternative schema authority.

The default cache is the user-scoped OEE release directory:
`%LOCALAPPDATA%/oee/curriculum-releases` on Windows,
`~/Library/Caches/oee/curriculum-releases` on macOS, and
`$XDG_CACHE_HOME/oee/curriculum-releases` on Linux where set, otherwise
`~/.cache/oee/curriculum-releases`. The Toolkit does not create the
cache on export, auto-download missing releases, search parent directories
for locks, or silently update a project lock.

## Reviewed release lock

Consumers commit one reviewed lock, with the exact active format:

```json
{
  "formatVersion": 1,
  "releaseId": "2026.11.1",
  "manifestSha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
}
```

**These values are illustrative only and not a released source identity.**
The lock must use unique keys, a supported format, a valid independent
`YYYY.MM.N` identifier and a full lowercase 64-character manifest SHA-256.
Unknown/missing fields, duplicate keys, invalid UTF-8 and symlinks are
rejected. A lock digest is expected to be obtained from a **reviewed,
approved release record**, not derived solely from an untrusted download.

REL-I02 separately verifies the release's Ed25519 signature against a
pre-approved steward public key **before** safe installation. A digest
match alone does not authenticate a publisher. REL-I03 does not re-sign or
re-approve a release: it trusts the operator's access-controlled store and
reviewed lock, then rechecks every installed source byte against the locked
manifest digest on each resolution.

## How verification works behind the scenes

1. Read exactly the selected lock. Fail closed if missing, symlinked,
   oversized, duplicated or otherwise invalid.
2. Open the already-installed directory named by the **full manifest
   SHA-256** under the trusted store. Refuse a missing or symlinked entry.
3. Read the canonical `release.json` and confirm its exact SHA-256 equals
   the lock. Validate the release ID and OEE specification version.
4. Walk the release directory, reject *any* unlisted extra file, missing
   listed file, symlink or noncanonical directory structure; compare
   **every** listed file's complete byte size, SHA-256 and UTF-8 status.
   Refuse to continue if a file, its license/notice or its manifest
   differs from the signed snapshot.
5. Expose the exact verified in-memory bytes through
   [release_source.py](oee_toolkit/release_source.py). This adapter
   uses the **same** first-party
   [outcome parser](oee_toolkit/_outcome_parser.py) and exactly the
   existing linked-public-assessment and prerequisite callbacks. It
   does not fork a Markdown grammar or consult a Git object.
6. Export **only format 2** using
   [course-export-v2.schema.json](oee_toolkit/schemas/course-export-v2.schema.json).
   The resulting JSON records `releaseId`, `manifestSha256`, the original
   course's exact `courseSha256` and `originCommit`, the supported OEE
   specification, source-located assessment/outcome IDs, current source
   status, rule-set and Toolkit version.
7. Write JSON only after all checks have passed. Missing or invalid
   sources never overwrite an existing output or learner file.

The existing source-only v1 golden snapshots remain internal test evidence
for detecting parser drift. The *distributed package* does not expose
v1 as a supported runtime schema or fallback input/output.

## Local candidate validation (no publication)

The CLI becomes useful to an author only **after** an explicitly approved
release has been securely acquired and installed. REL-I03 CI creates a
temporary test-only signed snapshot using a disposable key; it does not
publish a release, accept the test key as an official steward or generate
a trusted public lock for real users.

For an already verified, installed release with a separately approved
lockfile:

```sh
oee-toolkit export SEF1 --lock ./oee-curriculum.lock.json \
  --store ./verified-releases --output ./SEF1.json
```

No Git binary, remote fetch, file-writing installation, version fallback or
repository path is needed for this operation. Verification is offline.
All source and parser metadata is read from the pinned local snapshot.

## Tests and cutover gate

[REL-I03 test suite](../tests/test_toolkit_release_consumer.py) verifies
tampered files, changed manifest hashes, duplicate/invalid JSON fields,
lock mismatch, unlisted paths, symlinked cache entries, missing releases,
atomic output preservation, deterministic v2 exports, authored assessment
locations and structurally complete course inspection without Git.

The [cross-platform workflow](../.github/workflows/toolkit-release-consumer.yml)
builds a disposable 76-course snapshot from exact publisher-side Git
source, signs with a **test-only** key, securely installs locally, then
exports format-2 SEF1 and checks all courses on Linux, macOS and Windows.
It compares exact JSON export bytes and manifest digests independently;
ephemeral private keys and public release artifacts are **not uploaded**.

REL-I04 replaces Workspace's resource map and evidence source keys only
after editorial review of the selected curriculum release. REL-I05
coordinates private Content's compiler with the 0xNAND host and removes
obsolete academic feeds. Neither downstream repository is modified by
this PR. Official Toolkit package publication, steward key authority,
OEE release asset publication, and production consumer deployment remain
separate reviewed decisions.
