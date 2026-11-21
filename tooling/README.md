# OEE Toolkit

The Toolkit checks OEE course structure and produces deterministic exports from a digest-locked, locally installed curriculum release. It is the first-party implementation of the approach accepted in [RFC 0002](../rfcs/0002-toolkit-stewardship-and-licensing.md) and [RFC 0005](../rfcs/0005-immutable-curriculum-releases.md).

The Toolkit has not been published as an official standalone package, and its library API is not stable. The first independent wheel/source-archive **candidate** is buildable from the public repository; publication, distribution terms and support still need a separate steward approval. [Toolkit licensing](LICENSING.md) explains which licenses apply to its files.

**Consumer commands require an approved `oee-curriculum.lock.json` and verified installed release**. They never need a Git checkout, fetch the network or consult moving `main`. Git source revisions remain publisher-only provenance of a complete archive and the historical golden regression tests.

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
v0.2.0 parser, the release resolver, and the current `course-export-v2` JSON Schema.
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

The verifier needs a Python installation that can create a fresh virtual
environment with pip. On Debian/Ubuntu, install the matching `python3-venv`
package (for example `python3.12-venv`). If you cannot install system
packages, select another Python with `venv` and `ensurepip`:

~~~sh
python3 tooling/interop/verify_package_install.py --dist dist \
  --python /path/to/uv-managed/python3.12
~~~

Install the test-only `cryptography` dependency in the selected interpreter.
If `ensurepip` is unavailable, the verifier reports an actionable host
environment error before any wheel is tested. Separately, the source-readiness
JSON's `packagedDistributionVerified: false` only means its source-only checks
do not run a wheel/sdist install. Keep the independent package-verifier JSON
as distinct evidence.

The verifier installs the built wheel in an isolated environment outside
this source repository, exercises the `oee-toolkit` CLI against a disposable, signed and locally installed
release, compares v2 exports byte-for-byte with the source consumer CLI, and checks
software-license attribution and source-archive contents. The
[`toolkit-package.yml`](../.github/workflows/toolkit-package.yml) workflow
repeats the test on Linux, macOS and Windows; it has no publishing
permissions or registry credentials.

REL-I03 has implemented the **offline installed-release resolver and
current-only export format 2**, without approving an official curriculum
release, Toolkit package version or steward key. A consumer must first
acquire an explicitly approved, independently verified release artifact
using REL-I02's trusted installation process. Package installation and
curriculum-release selection are separate concerns.

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

REL-I03 implements the pinned release resolver and current-only v2
export, but Workspace and private Content remain on their existing
interfaces until the separately approved REL-I04/REL-I05 cutovers. No
official release archive has yet been published.

## Consumer commands (REL-I03)

The installed Python wheel and the source checkout's `python3 -m
tooling.oee_toolkit` expose the **same offline consumer CLI**. They do not
accept `--repo`, `--revision`, a v1 export selector or `latest`.

A project must commit a reviewed `oee-curriculum.lock.json`:

~~~json
{
  "formatVersion": 1,
  "releaseId": "2026.11.1",
  "manifestSha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
}
~~~

The example values are **illustrative only**, not a released curriculum or
a trusted manifest digest. With an independently approved, signed
curriculum release already installed in the user's trusted cache:

~~~sh
oee-toolkit check SEF1 --json
oee-toolkit check --all --json
oee-toolkit export SEF1 --output sef1.json

# Hermetic CI can choose explicit reviewed inputs:
oee-toolkit export SEF1 --lock ./oee-curriculum.lock.json \
  --store ./trusted-releases --output -
~~~

The default lock is **only** `./oee-curriculum.lock.json` in the current
directory. The default store uses the platform's user cache directory;
neither defaults to searching parent directories or fetching data.
`--store` selects an existing, access-controlled installation folder.
A missing/altered manifest, unapproved release ID, changed course bytes,
extra files or symlinks **fails closed**, before writing the export.
The consumer rechecks every listed file against the manifest digest,
not just the course currently exported.

The exported JSON uses the
[version-2 release schema](oee_toolkit/schemas/course-export-v2.schema.json),
with release ID, complete manifest SHA-256, course source digest, original
Git provenance **as an audit field only**, toolkit version and OEE source
status. Structural validation is **not** accreditation, academic readiness,
learner completion or commercial entitlement.

Publisher-maintainer workflows that prepare new releases and compare
historical golden fixtures are separately located at
`python3 -m tooling.oee_toolkit._publisher_cli`. That internal CLI still
reads an exact immutable Git commit to verify source authoring, but is
**not a consumer mode, supported runtime fallback or an alternative
authoritative course catalogue**.

**Exit codes:** 0 passed, 1 structural/unsafe reference error, 2 invalid
CLI arguments, 3 missing/incomplete/unsupported release, 4 unexpected
filesystem/tool failure. Output is written atomically only after a
complete validation succeeds.

## Architecture and authority

- `release_source.py` verifies the exact digest-locked installed release,
  rejects changed/missing/extra files, and adapts the verified bytes to
  the existing parser's source interface. It reuses the existing immutable
  source callback for linked public briefs, without running Git.
- `source.py` remains a **publisher-only** exact-Git reader used for
  candidate archive creation, source maintenance and historical tests.
- The packaged `oee_toolkit/_outcome_parser.py` is the **single
  parser and structural validator**. The repository's checker imports it;
  its optional extraction callback
  collects exactly the outcome, assessment, module and coverage identities
  observed by validation. There is no second Markdown course parser in
  this package.
- core.py builds a deterministic derived export only when that shared
  structural inspection reports passed. It never invents assessments,
  outcomes or outcomes for unsupported files.
- The current consumer format is
  [course-export-v2.schema.json](oee_toolkit/schemas/course-export-v2.schema.json).
  The old source-only v1 golden fixture format remains internal test
  evidence and is **not shipped as an active consumer export schema**.
  Curriculum release, specification, parser software and JSON format
  are distinct identities. Academic outcome and assessment IDs remain
  exactly the OEE-authored identities; lesson ordinals are navigation.
- A draft source validator does not establish teaching quality, a
  learner's mastery, formal conformance, accreditation or official OEE
  Toolkit status. Manual review remains required.

## Limitations and review gates

The source format supports the public v0.2.0 structural subset already
handled by the shared checker, including supported local linked assessment
briefs. Unrecognized valid Markdown expressions yield explicit parser
limitations/incomplete results rather than invented requirements.
Cross-course prerequisite codes are checked against the same verified
installed release. Course-level exports **do not invent program catalog
order** or establish the assessed quality of prerequisite work.

This implementation provides offline course check and export, plus
read-only full-release inspection. Full program-catalog export and an
**approved published** Toolkit package/curriculum release are **not yet
implemented or claimed**. The source-buildable package remains
engineering verification, not publication.
RFC 0002 has been accepted, but its approval does not complete the
remaining release-readiness work.

Tests first build disposable signed releases from synthetic Git fixtures,
then exercise the installed consumer **without Git**: deterministic v2
exports, linked public briefs, lock mismatches, missing or altered source,
unlisted cache files, symlinks, protected atomic output and no network
fallback. Internal publisher tests continue to check exact source revisions.

Run:

~~~sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m unittest discover -s tests -p 'test_toolkit_release_consumer.py' -v
~~~

**License boundaries:** Original Toolkit implementation, software
interface schemas and tests are MIT; normative OEE curriculum and actual
course-derived golden exports remain CC BY 4.0. See
[Toolkit licensing](LICENSING.md) and the repository
[NOTICE](../NOTICE). RFC 0002 records these boundaries. A separate
release-readiness review must verify distribution notices before an
official release. This does not retroactively change any contributor's
license or rights.
