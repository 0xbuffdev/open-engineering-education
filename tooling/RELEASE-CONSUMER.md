# REL-I03 — Git-free installed curriculum resolution and export v2

**Current status:** This offline consumer is shipped in [OEE Toolkit `0.1.0`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) and reads the steward-signed [curriculum `2026.11.1`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1). [Workspace `v0.1.0`](https://github.com/0xbuffdev/oee-workspace/releases/tag/v0.1.0) consumes the published release. This does not grade learners, certify courses or authorize a Content/0xNAND deployment.

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
  "manifestSha256": "57441494eb69c2ff9cb3f6029c8adc3c6a56f8c6ecabc43196c9b686e5959a6c"
}
```

The example identifies the actual signed `2026.11.1` curriculum. Check its independently approved [source digest and steward public-key fingerprint](RELEASE-DECISION.md) before accepting or installing the release. A lock must use unique keys, a supported format, an approved `YYYY.MM.N` identifier and a full lowercase 64-character manifest SHA-256.
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

## Offline use and disposable test releases

An author or learner must acquire and verify the approved release before using its locked course source. CI also creates a temporary test-only signed archive with a disposable key. That fixture checks the consumer's failure handling; its signing key and generated lock cannot establish trust in a public curriculum release.

For an already verified, installed release with a separately approved
lockfile:

```sh
oee-toolkit export SEF1 --lock ./oee-curriculum.lock.json \
  --store ./verified-releases --output ./SEF1.json
```

No Git binary, remote fetch, file-writing installation, version fallback or
repository path is needed for this operation. Verification is offline.
All source and parser metadata is read from the pinned local snapshot.

## Tests and integration

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

[Workspace `v0.1.0`](https://github.com/0xbuffdev/oee-workspace/releases/tag/v0.1.0) uses the current release-locked Toolkit export and independently governs its resource maps and learner evidence. Its optional reading plans require a separately approved release-keyed resource map. Content/0xNAND host integration remains an independent consumer decision. Toolkit publication, curriculum publication and hosted deployment require separate approvals.

## Source-bound assessment context (Toolkit 0.2.0 candidate)

Course export v2 remains unchanged in shape. It is a structural projection,
not the complete academic task specification. The separate context v1 command
preserves shared constraints, multiline fields, and required linked briefs
from the same verified release:

```sh
oee-toolkit assessment-context SEF1 --output sef1-context.json
```

The [context schema](oee_toolkit/schemas/assessment-context-v1.schema.json)
identifies the exact release, course, Toolkit, canonical course-export SHA-256,
and complete original UTF-8 Markdown for the course and each required linked
brief. Documents carry their manifest digest and inclusive source-line range.
The context SHA-256 covers canonical JSON of every field except itself.

The reviewed SEF1 index is applicable only to the exact published course
SHA-256. Its ranges point to shared rules, individual assessment definitions,
completion rules and explicitly optional practice. Each mandatory range names
the assessment IDs to which it applies; optional ranges name none. The
shared investigation range retains the source's conditional applicability
(e.g. inspectable circuits for AS1/AS2 and the permitted AS3 state-model
alternatives); consumers must not interpret every sentence as a separate
submission or change its conditions.

For other source revisions or courses without an index, applicability is
`manual-resolution-required`; no automatic classification is invented.
The complete course and applicable linked brief are the review scope.
Reviewers must resolve all relevant requirements, including referenced
public specification rules, or refuse approval. Optional practice remains
optional. A source index is not academic approval.

Consumers must verify the context and course export against the same trusted
installed release, recompute document and range hashes from the source, bind
the context digest and independently reviewed applicability to approval and
learner-facing tasks, and reject stale or unresolved context. No private
Markdown parser or second curriculum is needed. The current published
Toolkit 0.1.0 does not provide this command; separate package review and
release are required before downstream adoption.
