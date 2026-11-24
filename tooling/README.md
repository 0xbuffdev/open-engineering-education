# OEE Toolkit

The Toolkit checks OEE course structure and produces deterministic exports from a digest-locked, locally installed curriculum release. It is the first-party implementation of the approach accepted in [RFC 0002](../rfcs/0002-toolkit-stewardship-and-licensing.md) and [RFC 0005](../rfcs/0005-immutable-curriculum-releases.md).

The [OEE Toolkit `0.1.0`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) is published as a Python wheel and source distribution. It has a supported command-line interface; its importable Python library API is not yet promised to be stable. See [Toolkit licensing](LICENSING.md) for the software and curriculum license boundaries.

To run a consumer command, install a verified curriculum release and pin it in `oee-curriculum.lock.json`. Consumer commands work without Git or network access and never follow a moving `main` branch. Git revisions are used by maintainers to record where a release came from and to run source regression tests.

The specification and curriculum Markdown remain the editable educational source. The Toolkit's JSON exports are derived from that source. They do not certify a course, grade learners or create a separate authoring format.

## Check source and distribution

The published Toolkit passed separate source and clean-install verification on Linux, macOS and Windows. To repeat the source-only smoke, use [verify_release_readiness.py](interop/verify_release_readiness.py) on a local checkout:

~~~sh
python3 tooling/interop/verify_release_readiness.py --source . \
  --report ../toolkit-readiness.json
~~~

This command tests repository source. To check the distributed wheel and source archive, run the separate package verifier below. The Toolkit's software version and the OEE specification version are independent.

## Install and test the Toolkit package

Packaging is configured in [`pyproject.toml`](../pyproject.toml). The version is defined in [`oee_toolkit/__init__.py`](oee_toolkit/__init__.py), and the installed command is `oee-toolkit`. Download the audited wheel or source distribution from the [Toolkit `0.1.0` GitHub release](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0). The project has not claimed a PyPI distribution here.

The package contains only the MIT-covered Toolkit implementation, the shared
v0.2.0 parser, the release resolver, and the current `course-export-v2` JSON Schema.
The CC BY educational course Markdown and actual-course golden JSON exports
are **not bundled**. The OEE repository maintenance checker calls the exact
same installed-package parser implementation. `scripts/` is no longer a
runtime dependency of the installed Toolkit.

To build and test a distribution from your checkout:

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

The installed Toolkit reads an approved curriculum archive through the offline release resolver and exports course data in format 2. The current public curriculum is [signed release `2026.11.1`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1). Verify its Ed25519 signature against the independently approved steward public-key fingerprint before installing it. Installing the Toolkit package alone does not install a curriculum.

## Immutable curriculum release manifest (REL-I01)

The [release manifest format](RELEASE-MANIFEST.md) records the complete curriculum and specification at an explicit Git commit. The publisher uses the Toolkit's course parser to inventory source files and record their hashes with `python3 scripts/build-curriculum-release-manifest.py`.

Manifest generation checks source integrity without signing or publishing anything. [RFC 0005](../rfcs/0005-immutable-curriculum-releases.md) also requires a verified archive, explicit release lock and offline consumer export.

## Signed, offline curriculum archive (REL-I02)

The [release archive format](RELEASE-ARCHIVE.md) is a canonical, uncompressed TAR built from the complete OEE manifest. The release tools verify the Ed25519 attestation and install the archive without replacing existing data. Signing uses a separately trusted key and the optional `oee-toolkit[release]` dependency. The installer does not publish releases, modify learner work or change course status.

The release resolver and v2 exporter are available in the published Toolkit.
The next Toolkit candidate also provides a separate, versioned
[assessment context export](RELEASE-CONSUMER.md#source-bound-assessment-context-toolkit-020-candidate)
for complete source-bound review; it does not change course export v2. [OEE Workspace v0.1.0](https://github.com/0xbuffdev/oee-workspace/releases/tag/v0.1.0) uses the signed curriculum and its reviewed lock. Content and 0xNAND integration is a separate consumer task.

## Consumer commands (REL-I03)

The installed Python wheel and the source checkout's `python3 -m
tooling.oee_toolkit` expose the **same offline consumer CLI**. They do not
accept `--repo`, `--revision`, a v1 export selector or `latest`.

A project must commit a reviewed `oee-curriculum.lock.json`:

~~~json
{
  "formatVersion": 1,
  "releaseId": "2026.11.1",
  "manifestSha256": "57441494eb69c2ff9cb3f6029c8adc3c6a56f8c6ecabc43196c9b686e5959a6c"
}
~~~

The lock above identifies the actual published `2026.11.1` release, not a disposable test fixture. Before installing, independently confirm the manifest digest and steward signing key against the [published release decision](RELEASE-DECISION.md) and [curriculum release](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1). Then install the signed archive into a trusted local store and run:

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
  Historical source-regression fixtures remain internal test evidence
  and are **not shipped as an active consumer export schema**.
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

The Toolkit supports offline course checks, deterministic exports and read-only inspection of an installed release. Full program-catalog export is not available. The [Toolkit package](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) and [signed curriculum](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1) have been published; future software changes still require their own release review.

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

**Release records:** The [0.1.0 and 2026.11.1 release decision](RELEASE-DECISION.md) preserves verified hashes and the independent signing-key fingerprint. The [publication runbook](RELEASE-PUBLICATION.md) documents steward signing, key security and how releases are audited. Future packages and curriculum archives need their own source review, cross-platform acceptance, and explicit publication approval.

**License boundaries:** Original Toolkit implementation, software
interface schemas and tests are MIT; normative OEE curriculum and actual
course-derived golden exports remain CC BY 4.0. See
[Toolkit licensing](LICENSING.md) and the repository
[NOTICE](../NOTICE). RFC 0002 records these boundaries. A separate
release review checks distribution notices. Publication does not change any contributor's license or rights.
