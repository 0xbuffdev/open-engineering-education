# REL-I01 — Immutable OEE curriculum release manifest

**Status:** Candidate source-integrity implementation, **not an OEE curriculum
release or a published Toolkit package**.

The authority is [accepted RFC 0005](../rfcs/0005-immutable-curriculum-releases.md).
This implementation is deliberately narrower than REL-I02 (deterministic
archive, signatures and safe installation) and REL-I03 (Git-free, locked
consumer resolver and Toolkit exportVersion 2).

## Publisher and consumer responsibilities

- The **publisher** chooses a reviewed full 40-character OEE Git commit and
  an explicit, human-readable calendar release identity (`YYYY.MM.N`).
- This source-only code reads **that exact Git tree**, not a dirty worktree,
  moving `main`, a tag, network input or a consumer's local files.
- It inventories all `curriculum/**/*.md`, `spec/**/*.md`, `LICENSE`,
  `NOTICE` and `CITATION.cff`. It rejects unknown files, symlinks,
  non-UTF-8 data, duplicate/unsafe paths and oversized sources in these
  academic trees instead of silently excluding them.
- A full release must contain every canonical OEE course and its catalog;
  each program's authoritative catalog must list every corresponding
  course exactly once. OEE Toolkit **reuses the existing parser** to check
  all course requirements, required assessments, prerequisites and linked
  public briefs. Incomplete or unsupported source blocks the candidate.
- A derived `formatVersion: 1` manifest records each file's exact original
  byte length and SHA-256, full originating Git SHA, OEE specification
  version and independent curriculum release ID. Paths are sorted
  lexicographically by UTF-8 bytes; canonical UTF-8 JSON has a single LF
  terminator, no timestamps and no absolute machine paths.
- The **consumer** will eventually select an approved release by an
  independently reviewed `oee-curriculum.lock.json` manifest digest.
  That Git-free lockfile resolver, source archive, signature and version-2
  course exporter are **not implemented by REL-I01**. No consumer is
  permitted to treat this candidate manifest as a trusted publication.

Academic course status (`draft` / `tested` / `verified`) remains exactly as
authored. Structural verification is not academic conformance, independent
course review, completion or learner mastery.

## Candidate commands

Run with Git and Python 3.11+ from an OEE source checkout (no new runtime
dependencies):

```sh
REVISION="$(git rev-parse HEAD)"

# Publisher-side candidate preview only, with an illustrative release ID.
python3 scripts/build-curriculum-release-manifest.py \
  --repo . --revision "$REVISION" --release-id 2099.01.1 \
  --output release-manifest-candidate.json

# Fail unless the same exact commit produces the same complete manifest.
python3 scripts/build-curriculum-release-manifest.py \
  --repo . --revision "$REVISION" \
  --check release-manifest-candidate.json

# Write the deterministic preview to stdout, without creating a file.
python3 scripts/build-curriculum-release-manifest.py \
  --repo . --revision "$REVISION" --release-id 2099.01.1 \
  --output -
```

The identifier is illustrative and **not an allocated or published release**.
The builder writes neither curriculum sources nor any learner files. Its
output may be a local CI test artifact, but is not a distributable OEE release
and carries no approval signature, archive or release URL.

## Single source of truth and verification

- **Manifest implementation:** [release_manifest.py](oee_toolkit/release_manifest.py).
- **Manifest JSON Schema:** [curriculum-release-manifest-v1.schema.json](oee_toolkit/schemas/curriculum-release-manifest-v1.schema.json).
- **Course interpretation:** [the single OEE parser](oee_toolkit/_outcome_parser.py), called via
  [Toolkit Core](oee_toolkit/core.py). REL-I01 does not duplicate the academic
  course/assessment grammar or canonical course status.
- **Tests:** [test_curriculum_release_manifest.py](../tests/test_curriculum_release_manifest.py)
  rejects invalid versions and digests, unknown/missing courses, catalog drift,
  linked assessment-brief gaps, symlink and traversal references, source
  mismatch, noncanonical manifests, oversize files and incomplete criteria.
- **CI:** [curriculum-release-manifest.yml](../.github/workflows/curriculum-release-manifest.yml)
  runs synthetic and full-current-source checks on Windows, macOS and Linux,
  compares candidate JSON bytes, and publishes **no release artifacts**.

The release manifest is a derived inventory, **not a second editable course
catalog**. The OEE Markdown and program READMEs stay authoritative. A future
change to the source creates a new manifest digest and requires a separately
approved release; never silently repin an existing lockfile.

## Remaining explicit milestones

1. **REL-I02:** reproducible uncompressed TAR, complete archive/manifest
   checks, safe immutable installation, signed provenance and attestation
   tests; release publication is a separate steward decision.
2. **REL-I03:** Git-free Toolkit resolver using the reviewed manifest lock,
   one existing parser, only the current output `exportVersion: 2`.
3. **REL-I04/REL-I05:** reviewed Workspace and private Content/0xNAND
   consumer replacements, without compatibility adapters or silent changes
   to existing non-disposable learner records and entitlements.

See [Stage 2 tracker #257](https://github.com/0xbuffdev/open-engineering-education/issues/257).
