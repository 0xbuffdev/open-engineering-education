# OEE Toolkit

The Toolkit checks OEE course structure and produces deterministic curriculum exports from Git. It is a repository-local implementation of the approach accepted in [RFC 0002](../rfcs/0002-toolkit-stewardship-and-licensing.md).

The Toolkit has not been published as an official standalone package, and its library API is not stable. The first independent wheel/source-archive **candidate** is buildable from the public repository; publication, distribution terms and support still need a separate steward approval. [Toolkit licensing](LICENSING.md) explains which licenses apply to its files.

The Toolkit reads **OEE v0.2.0 course sources only** at a full, immutable 40-character Git commit SHA. It reads local Git objects and does not fetch a remote or take educational source from a moving branch, the index, or an uncommitted worktree.

The only editable educational source is the public OEE specification and
curriculum Markdown. The exported JSON is derived data, not a second
authoring format, conformance certificate, learner grade or evidence of
the course having been tested or verified.

## Independent release-readiness verification

The [OT-I05 public release checklist](RELEASE-READINESS.md) documents the
24 Toolkit acceptance gates, licensing/source provenance, independent
Windows/macOS/Linux smoke and the separate OEE steward decision needed
before any official distribution. The [release smoke](interop/verify_release_readiness.py)
clones the public OEE checkout locally and executes the **repository-local**
Toolkit without network access or private services:

~~~sh
python3 tooling/interop/verify_release_readiness.py --source . \
  --report ../toolkit-readiness.json
~~~

This is **engineering verification, not package publication**. The
accepted RFC approves optional Toolkit source, not a package version,
installed importable API or an official release tag. The current
CLI and OEE curriculum specification remain versioned separately.

## Installable-package candidate (Stage 1)

This repository now carries Python packaging metadata in
[`pyproject.toml`](../pyproject.toml), one package version authority in
[`oee_toolkit/__init__.py`](oee_toolkit/__init__.py), and a console
entrypoint, `oee-toolkit`. The version currently denotes an **unreleased
development candidate**. No PyPI project claim, release tag or official
package version is implied by building it.

The package contains only the MIT-covered Toolkit implementation, the shared
v0.2.0 parser, the source reader, and the software export JSON Schema.
The CC BY educational course Markdown and actual-course golden JSON exports
are **not bundled**. The OEE repository maintenance checker calls the exact
same installed-package parser implementation. `scripts/` is no longer a
runtime dependency of the installed Toolkit.

To inspect a local candidate, without publishing:

~~~sh
python3 -m pip install build
python3 -m build --wheel --sdist
python3 tooling/interop/verify_package_install.py --dist dist
~~~

The verifier installs the built wheel in an isolated environment outside
this source repository, exercises the `oee-toolkit` CLI against a source
commit, compares exports byte-for-byte with the repository's CLI, and checks
software-license attribution and source-archive contents. The
[`toolkit-package.yml`](../.github/workflows/toolkit-package.yml) workflow
repeats the test on Linux, macOS and Windows; it has no publishing
permissions or registry credentials.

Until Stage 2's separately approved immutable **curriculum-release
manifest** exists, the installed command continues to require a trusted
local OEE Git repository and an exact full source revision. This is an
intentional provenance guarantee, not a public usability requirement we
intend to keep indefinitely. Package installation and curriculum source
selection are separate concerns.

## Immutable curriculum release manifest (REL-I01)

The [release manifest candidate](RELEASE-MANIFEST.md) inventories the
**entire** current public curriculum and specification at an exact
publisher-selected Git commit, using the Toolkit's existing course parser
and a deterministic, full-digest source file manifest. The publisher-only
command is `python3 scripts/build-curriculum-release-manifest.py`.

This is source-integrity preparation **only**. The accepted
[RFC 0005](../rfcs/0005-immutable-curriculum-releases.md) separately gates
the archive, installed release lock, Git-free Toolkit export, and consumer
cutovers. No archive, package, release tag, learner data, or publication
is created by REL-I01.

## Signed, offline curriculum archive (REL-I02)

[REL-I02's release archive proposal](RELEASE-ARCHIVE.md) builds a canonical,
uncompressed TAR from the **REL-I01-verified complete OEE manifest**, and
supplies explicit Ed25519 attestation verification and no-clobber offline
installation. Signing uses a separately trusted key and the optional
`oee-toolkit[release]` dependency; it is not part of the default course
parser. No GitHub Release, package upload, source promotion or learner
mutation is performed or authorized by this implementation.

The separate REL-I03 gate will replace consumer-facing Git revisions with a
pinned manifest lock and current-only Toolkit exportVersion 2. Until it
lands, this candidate is **not** a ready-to-use Workspace/Content source
contract.

## Commands

From the public OEE repository checkout (Python 3.11+ and Git installed):

~~~sh
REVISION="$(git rev-parse HEAD)"

python3 -m tooling.oee_toolkit check \
  --repo . --revision "$REVISION" --course SEF1

python3 -m tooling.oee_toolkit check \
  --repo . --revision "$REVISION" --all --json

python3 -m tooling.oee_toolkit export \
  --repo . --revision "$REVISION" --course SEF1 \
  --output sef1.json
~~~

Use `--output -` to write derived JSON to stdout. A file export is written
atomically only **after** the entire selected course passes structural
checks; a missing/unsupported source leaves an existing destination
untouched. The repository-local command remains `python3 -m tooling.oee_toolkit`. The
installable candidate exposes `oee-toolkit` and `python3 -m oee_toolkit`.
A stabilized importable API, official package release version and public
distribution still require separate approval.

**Exit codes:** 0 structurally passed; 1 structural violation or unsafe
reference; 2 invalid CLI arguments; 3 missing/incomplete/unsupported
input; 4 unexpected local Git or tool failure.

A repository-wide `--all` inspection is incomplete when any published
course has an unsupported version or insufficient outcome/assessment data.
Every course must satisfy the current OEE v0.2.0 structural contract.

## Architecture and authority

- source.py uses Git object queries to verify the exact commit and read
  selected blobs. It rejects missing objects, symlinks, path escapes and
  unsupported file contents. Linked public briefs resolve only at the
  selected Git tree, without reading current disk files.
- The packaged `oee_toolkit/_outcome_parser.py` is the **single
  parser and structural validator**. The repository's checker imports it;
  its optional extraction callback
  collects exactly the outcome, assessment, module and coverage identities
  observed by validation. There is no second Markdown course parser in
  this package.
- core.py builds a deterministic derived export only when that shared
  structural inspection reports passed. It never invents assessments,
  outcomes or outcomes for unsupported files.
- The exported course format is described by
  [course-export-v1.schema.json](oee_toolkit/schemas/course-export-v1.schema.json).
  Source revision, specification, export format, and tool version have
  distinct identities. Course IDs and assessment/outcome IDs are stable
  within their published course revision; lesson ordinals are navigation.
- A draft source validator does not establish teaching quality, a
  learner's mastery, formal conformance, accreditation or official OEE
  Toolkit status. Manual review remains required.

## Limitations and review gates

The source format supports the public v0.2.0 structural subset already
handled by the shared checker, including supported local linked assessment
briefs. Unrecognized valid Markdown expressions yield explicit parser
limitations/incomplete results rather than invented requirements.
Cross-course prerequisite codes are checked for presence in the same
Git tree; a course-level snapshot **does not invent program catalog order**
or establish the assessed quality of prerequisite work.

This draft implements course check and course export, with a read-only
repository inspection. Full program-catalog export and an **approved published** Toolkit package
or public release numbering are **not yet implemented or claimed**. The
source-buildable package candidate is verification work, not publication.
RFC 0002 has been accepted, but its approval does not complete the
remaining release-readiness work.

Tests build isolated synthetic local Git repositories and exercise:
immutable revisions across dirty worktrees/moved HEAD, byte-identical
exports, valid/invalid public briefs, missing/unknown sources, unsupported
source versions, path traversal and symlinks, protected atomic output, and
offline CLI behavior.

Run:

~~~sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m unittest discover -s tests -p 'test_toolkit_pinned_export.py' -v
~~~

**License boundaries:** Original Toolkit implementation, software
interface schemas and tests are MIT; normative OEE curriculum and actual
course-derived golden exports remain CC BY 4.0. See
[Toolkit licensing](LICENSING.md) and the repository
[NOTICE](../NOTICE). RFC 0002 records these boundaries. A separate
release-readiness review must verify distribution notices before an
official release. This does not retroactively change any contributor's
license or rights.
