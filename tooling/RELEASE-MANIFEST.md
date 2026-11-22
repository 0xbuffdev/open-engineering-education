# REL-I01 — Immutable OEE curriculum release manifest

The manifest builder is part of the published [OEE Toolkit `0.1.0`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/toolkit-v0.1.0) release pipeline. The first steward-signed curriculum release is [`2026.11.1`](https://github.com/0xbuffdev/open-engineering-education/releases/tag/curriculum-2026.11.1). This document describes the publisher-side format established under [RFC 0005](../rfcs/0005-immutable-curriculum-releases.md). The archive and offline consumer are covered in [REL-I02](RELEASE-ARCHIVE.md) and [REL-I03](RELEASE-CONSUMER.md).

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
- The **consumer** selects an approved release by its reviewed `oee-curriculum.lock.json` manifest digest. Archive verification, Ed25519 signature checks, and the Git-free Toolkit version-2 exporter operate separately from manifest construction. An unsigned candidate manifest cannot authorize installation.

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

## Current consumers

The first published curriculum uses this manifest format. The [signed archive contract](RELEASE-ARCHIVE.md) and [offline Toolkit consumer](RELEASE-CONSUMER.md) implement the remaining release boundaries. [Workspace v0.1.0](https://github.com/0xbuffdev/oee-workspace/releases/tag/v0.1.0) consumes the signed release; private Content/0xNAND integration has its own review and rollout. New curriculum versions require a new immutable manifest and steward approval. Historical implementation work is recorded in [issue #257](https://github.com/0xbuffdev/open-engineering-education/issues/257).
