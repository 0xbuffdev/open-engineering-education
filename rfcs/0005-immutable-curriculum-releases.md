# RFC 0005: Immutable curriculum releases without consumer Git revisions

- **Status:** `accepted`
- **Author:** Public OEE interoperability proposal for steward review
- **Created:** 2026-11-20
- **Last updated:** 2026-11-20
- **Related issue:** [Stage 2 release implementation tracker #257](https://github.com/0xbuffdev/open-engineering-education/issues/257)
- **Affected specification version:** OEE `v0.2.0` draft; no educational requirement change proposed

## 1. Summary

Introduce a separately versioned, immutable **OEE curriculum release** with a
content-addressed manifest and complete, read-only source snapshot. A learner
or content author selects a human-readable curriculum release, not an OEE Git
commit. The first-party Toolkit resolves a locally installed release through
a reviewed lockfile, verifies all required SHA-256 digests, and exports the
same course requirements through its one canonical parser.

The public OEE Markdown remains the **only editable academic source**.
Git remains the provenance and release-construction mechanism, but is not a
runtime requirement for consuming an installed curriculum release. This is
distribution and interoperability, not a new curriculum authoring standard,
course status, learner grade or conformance certification.

## 2. Problem

The first-party Toolkit currently requires `--repo` plus an exact 40-character
`--revision` on each operation. That makes independent OEE Workspace and
Content consumers require a local Git checkout, source pin management and a
repository-specific Python CLI path. Both must interpret identical public
source identities while needing different learner- and author-facing flows.

The full Git revision currently guarantees important properties: deterministic
re-execution, source authenticity evidence, no moving HEAD, and explicit
assessment/outcome provenance. Merely dropping `--revision`, checking `main`,
or trusting a mutable release-name lookup would destroy those properties.
A valid alternative must preserve immutable **bytes**, not just a friendly
version string.

OEE currently has software-specific Toolkit release-readiness work and OEE
`v0.2.0` specification tags, but no distinct immutable curriculum snapshot
format with a consumer lock. The two version axes must not be conflated.

## 3. Proposed change

### Authority and boundaries

1. **OEE** retains sole authority over educational Markdown, requirements,
   assessment briefs, statuses and specification. It publishes each approved
   read-only curriculum snapshot from one reviewed exact repository commit.
2. **Curriculum release** is a derived, reproducible distribution artifact.
   It never becomes a second editable course source or new normative OEE
   grammar. A changed source requires a new release identity and new digest.
3. **OEE Toolkit** resolves and validates a release snapshot using the same
   parser as OEE repository maintenance. It never guesses the current
   revision or treats export success as educational review.
4. **Consumers** pin one approved release manifest digest. Workspace may
   add optional reviewed resources and learner files; a commercial product
   may add private instructional overlays. Neither may redefine the OEE
   curriculum, assessment criteria or status.
5. **Independent OEE implementations** remain free to interpret public
   Markdown directly. Installing the first-party Toolkit or using this
   artifact is not a new OEE conformance requirement.

This is an **optional official distribution mechanism**. Accepted RFC 0002
continues to govern Toolkit software stewardship and file-scoped licensing.
A curriculum release, Toolkit package release, OEE normative specification
version and Toolkit JSON export format have different identities.

### Proposed decisions to approve

The following choices were adopted for the distribution contract in the
steward's November 20 decision (Section 10). They do not authorize archive
publication or downstream consumer deployment:

1. **Release scope:** distribute the complete current OEE course set, not a
   hand-selected SEF1-only or incomplete prerequisite subset. Validate
   every included course and the closure of every referenced public
   assessment brief. A course that the Toolkit cannot inspect completely
   blocks the release candidate instead of disappearing from it. Include
   the published public program catalogs and required source references.
   This does not imply a course's educational readiness is beyond
   its authored `draft`, `tested` or `verified` status.
2. **Naming:** use independent monotonically allocated CalVer release IDs
   `YYYY.MM.N` (for example `2026.11.1`); the third component is a
   one-based release sequence for that UTC month, not an OEE specification
   revision. Never overwrite or reassign an ID, including after a failed
   or withdrawn distribution.
3. **Distribution:** prefer an OEE-owned GitHub Release containing the
   exact deterministic archive, its manifest digest, a signed provenance
   attestation and relevant license notices. The reviewer verifies the
   exact build before publishing. GitHub tag names and release asset URLs
   are **transport/discovery labels**, never the source identity; consumers
   verify the approved manifest digest from their lockfile.
4. **Consumer behavior:** user commands require only a locked curriculum
   release and the installed Toolkit. Git may be used by the publisher,
   but neither a learner's Workspace nor Content's authoring/compiler
   runtime needs Git. The consumer reads a locally installed snapshot and
   never invokes a network or Git fallback.
5. **Trust:** matching a checksum detects unexpected changed bytes but
   does **not authenticate the publisher**. Before approving a lockfile
   or accepting a downloaded release into a trusted cache, maintainers
   check the signed release provenance against the approved OEE steward.
   Ordinary offline export verifies the previously approved pinned digest
   and needs no network or online signing service.

### Curriculum release identity and format

The first candidate manifest format is `formatVersion: 1`. The following is
**illustrative only**; it is not an already published curriculum release:

```json
{
  "formatVersion": 1,
  "releaseId": "2026.11.1",
  "source": {
    "repository": "0xbuffdev/open-engineering-education",
    "commit": "0000000000000000000000000000000000000000",
    "specification": "v0.2.0"
  },
  "files": [
    {
      "path": "curriculum/SEF/SEF1.md",
      "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "size": 12345
    }
  ]
}
```

Release `source.commit` is a full, exact Git SHA captured by the maintainer
for traceable provenance. Consumers **do not provide or select** that SHA.
Each listed file has its original Git blob bytes, relative POSIX path,
byte size and full SHA-256 digest. The original source remains viewable
at the recorded Git revision, but a consumer does not fetch or parse it
from Git.

- Files are sorted by canonical bytewise POSIX path; duplicate paths,
  symlinks, dot components, traversal, invalid UTF-8 source and unexpected
  entries are rejected. Manifest serialization is a single documented
  canonical UTF-8 JSON encoding, no timestamps or absolute paths.
- A complete source set includes all active course definitions, their
  referenced public assessment briefs, required catalog/source links,
  and other public files needed to evaluate those references. Missing
  referenced material is an incomplete release. No private content or
  learner evidence belongs in a bundle.
- The archive is an allowlisted, normalized **uncompressed TAR** candidate:
  one `release.json` manifest plus only the source and license/NOTICE files
  explicitly listed in `files`. The manifest never hashes itself.
  Archive entries use sorted POSIX paths, regular-file type only, fixed
  mode/ownership/mtime, and byte-for-byte Git-source content. No
  compression metadata or operating-system-dependent line endings are
  introduced. Two clean builds from one reviewed commit must produce
  identical archive bytes on Linux, macOS and Windows.
- The file inventory includes the applicable CC BY 4.0 attribution and
  rights notices. Every archive entry other than `release.json` must
  have a corresponding size and SHA-256 in the manifest; unlisted entries,
  duplicate entries, symlinks, hard links, devices, absolute/traversal
  paths, invalid UTF-8 names and oversized entries are rejected before
  extraction. A safe installer verifies manifest integrity and all
  listed bytes before an atomic, no-clobber cache update.
- Publication is append-only by release ID: a second, different digest
  under the same ID is an error. Source fixes create **new** releases; no
  force-changing an old manifest, reusing an old name, or mutable `latest`.
- An immutable source repository commit is still recorded for audits,
  reproducing original Markdown and attribution. It is not an input
  consumer operators need to know.

### Consumer lock and integrity

Each consumer selects the release through one machine-readable
`oee-curriculum.lock.json` committed alongside that consumer's own code.
Example with **illustrative** digest:

```json
{
  "formatVersion": 1,
  "releaseId": "2026.11.1",
  "manifestSha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
}
```

The lock's exact `manifestSha256` authenticates which manifest bytes a
consumer expects, independent of an artifact URL or mutable GitHub tag.
Acquisition must be explicit (for example a separate install command,
reviewed CI artifact fetch, or a downloaded release bundle), with
checksum verification **before** a cache update. A trusted approval
record and artifact signature/attestation are separate release checks;
SHA-256 consistency alone does not prove who published an artifact.

A release installation can be reused by Workspace and Content, but each
consumer keeps its **own reviewed lock** for dependency resolution. A
deterministic export includes the release ID, manifest digest, course
source path/digest, OEE specification version and Toolkit export version.
Source provenance additionally records the originating Git commit **inside
the verified release**, never as an operator-provided source selector.
Neither the CLI nor the consumer lock needs a `--revision` argument.

The default CLI lockfile is **only** `oee-curriculum.lock.json` in the
current project's working directory; the optional explicit `--lock`
argument chooses a specific approved file for CI or embedded consumers.
Do not walk parent directories or infer a lock from the user's home
directory. Lock paths must resolve to a regular, non-symlink file. The
release store uses a platform-appropriate user cache directory by
default and permits an explicit directory for hermetic CI. Content and
Workspace never search the network, `main`, or the local Git checkout
when the requested digest is missing.

The cache is keyed by **full manifest digest**, not just the human release
ID. A resolver refuses conflicting ID-to-digest mappings, mixed sources,
unlisted files, altered license files and any package/archive with an
invalid or incomplete manifest. It does not rewrite the project lockfile.
An explicit install command may fetch a reviewed asset before offline
use, but acquisition, trusted-release provenance review and source
verification are separate operations.

The installed curriculum resolver is offline: after an explicit,
integrity-checked acquisition, validation and export read only local
files. No implicit network fetch, moving HEAD, guessed default source or
unapproved automatic upgrade is allowed.

### Toolkit user interface and output contract

The intended user-facing command is:

```sh
oee-toolkit export SEF1 --output sef1.json
```

It resolves `oee-curriculum.lock.json` from the selected project, verifies
the installed release manifest and referenced file digests, then uses
the one canonical OEE parser. The package can additionally support an
explicit lockfile path for hermetic CI; absence or mismatch is a
failure, never fallback to `main`. Consumer software is pinned with
its own Python environment/package lock, not embedded as a second
version in the curriculum release.

Changing the JSON `source` identity is a **breaking wire-format change**:
the new source contract should be `exportVersion: 2`, without a runtime
`exportVersion: 1` fallback, migration parser or dual-source reader.
The Toolkit must use one parser behind a small, read-only source adapter:
a release-backed adapter supplies verified source bytes, stable relative
paths, linked public briefs and prerequisite lookup to the **same**
`_outcome_parser.parse_structure` implementation. The existing Git reader
may remain a maintainer-only release-build source; it must not be a
second consumer interpretation or fallback.

At minimum, version 2 records:

- Curriculum `releaseId` and full `manifestSha256`.
- Source repository, OEE specification version, canonical course code and
  source-relative course path, plus full SHA-256 of original course bytes.
- Original outcome IDs, required assessment IDs, public criteria,
  public evidence and source-located references, with no invented
  permanent module/lesson IDs.
- Source status `draft` / `tested` / `verified` exactly as authored.
- Toolkit software version and export-format version as separate metadata.

The released Markdown continues to contain actual educational
requirements; the derived JSON does not acquire independent authority.

### Source preparation and release safety

A maintainer prepares a candidate from one explicit approved commit,
validates the complete source set and its references, builds the manifest
and deterministic archive, independently rebuilds, checks attribution,
signs/reviews the release and only then approves publication. This
procedure does not modify `curriculum/` or silently promote course
statuses. The publication mechanism must refuse an existing release ID
whose manifest digest differs from its prior published digest.

No package, archive, tag, existing release or private deployment is
authorized by approval of the RFC alone.

## 4. Alternatives considered

| Alternative | Advantage | Why not selected |
| --- | --- | --- |
| Always consume Git `main` | One simple command | Mutable results invalidate assessments and reviewed resource mappings |
| Replace SHA with a Git tag only | Human-friendly name | Tags and release assets can be replaced or mismatched without a consumer digest lock |
| Ship complete curricula inside every Toolkit wheel | One package | Every curriculum edit requires software release; combines MIT-covered software with CC BY educational data |
| Keep only explicit Git commit everywhere | Maximum existing provenance | Burdens learners, authors and cross-platform consumers with repository pinning |
| Immutable archive and digest-locked human release ID | Simple consumer interface, byte-for-byte provenance | Needs separately maintained release artifacts and deliberate consumer upgrade reviews |

## 5. Impact assessment

### Existing courses and programs

No course outcomes, lessons, module count, assessments, prerequisites,
pedagogical standards or status meaning change. Course files remain at
their canonical paths. The first release must be assembled from a
reviewed, complete source tree; a draft `v0.2.0` course remains draft.
OEE specification versioning is **not** the curriculum snapshot
release counter.

### Implementations

- **First-party Toolkit:** add a digest-verifying immutable release
  source that uses the one parser and existing structural validation;
  provide an explicit release install/verify path and version-2 export.
  Keep repository maintenance Git operations distinct from public
  consumer-facing commands.
- **OEE Workspace:** update the active public map schema, generator,
  CLI and learner evidence source identity in a coordinated, current-only
  change. Re-review course resource references for the specific released
  course, rather than renaming a SHA field mechanically.
- **0xNAND Content:** replace the candidate's raw source SHA input with
  the locked immutable release and Toolkit export v2; publisher and host
  must agree on the selected release. No second curriculum parser or
  shadow authoritative course catalogue.
- **Independent implementations:** not compelled to use first-party
  packaging or release archives.

### Evidence and status labels

The same immutable outcomes, assessment criteria and source digests
remain available for new academic evidence. Neither package installation
nor an archive release can grant mastery, academic credit or source
`tested`/`verified` status. Existing non-disposable evidence, learner
artifacts or purchased entitlements are never destroyed by an automatic
upgrade; any real remote-data disposition requires explicit approval.

### Conformance

No normative requirement or claim changes merely because the same
course is distributed in a new container. Conformance still requires
the actual published OEE source and relevant evidence; Toolkit
structural checks do not certify teaching quality.

### Licensing and governance

Toolkit software remains scoped to MIT under RFC 0002. The curriculum
release, educational briefs and any golden-derived text remain CC BY
4.0, with source attribution and separate third-party rights review.
The public steward must approve release name, digest, provenance,
distributable archive, notices and publication. Any future normative
format or legal change requires its own reviewed process.

## 6. Compatibility and transition

This proposal intentionally establishes **one new active version-2
consumer contract**, not a historical runtime compatibility layer:

1. Accept RFC and review deterministic release format/interface
   documentation, schema and malicious-archive test matrix in a
   dedicated public OEE PR.
2. Build and independently verify a **candidate** curriculum release,
   with explicit trusted source commit, complete file inventory, linked
   briefs and full digest coverage. Do not publish yet.
3. Review the release and receive explicit steward distribution
   approval; publish an immutable archive with checksum/attestation.
4. Update the first-party Toolkit to use locked release identity and
   supported export version 2. Drop consumer-facing Git flags and
   version-1 export fallback in the same approved cutover.
5. Review OEE Workspace resource maps, generators and evidence contracts
   against the released source. Replace current v2 maps with a single
   active release-keyed schema; keep raw historical source in Git only.
   Preserve learner-owned files and report unknown real user data before
   destructive changes.
6. Update private Content publisher and approved host consumer to the
   same format; remove old parallel academic feeds, positional official
   IDs and incompatible private interfaces. No automatic source
   reinterpretation, course-credit conversion or silent repin.
7. Verify that both consumers produce and accept the same **byte-level**
   Toolkit export at the same release, while retaining separate authored
   resources, instruction, commercial access and grading authority.

No previous v0.1.0 or resource-map-v1 input becomes supported. Historical
published facts remain attributable to their original exact source,
without requiring an obsolete live reader in the new release path.

## 7. Risks and mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Release label is reused for new bytes | Critical source ambiguity | Reject duplicate labels with changed manifest digest; pin release ID and full manifest SHA |
| Manifest or archive replaced | Supply-chain integrity breach | Verify consumer lock digest, signed provenance and published release record before activation |
| Linked briefs or prerequisites omitted | Invalid academic requirements | Validate full linked-source closure; no partial source fallback |
| Tool/parser and format versions drift | Contradictory export semantics | Explicit Toolkit release version, separate format version, no dual readers |
| Resource map attaches outdated chapter | Misleading study guide | Manual revision-to-release editorial review; fail closed on mismatch |
| CC BY data accidentally shipped as MIT-only | Attribution/rights violation | Separate archive notices and legal review, software-only wheel gate |
| Existing learner evidence accidentally overwritten | Data loss | No-clobber workspaces and separate remote-data approval before destructive operations |

## 8. Validation plan

A successful implementation must demonstrate, before approval:

1. **Reproducibility:** independent clean builds of the same approved
   source yield identical manifest bytes, archive bytes, file digests and
   deterministic Toolkit export bytes on Linux, macOS and Windows.
2. **Provenance:** each export can locate the exact original public
   course/assessment source and attest to a byte-exact digest and release
   manifest; no moving Git reference is resolved by a learner command.
3. **Fail closed:** reject unknown release ID, unsupported format,
   missing archive, changed manifest SHA, changed course bytes, duplicate
   paths, symlink/path traversal, altered linked brief, incomplete
   assessment coverage and cross-course identity mismatch.
4. **Licensing:** verify CC BY attributions for the archive; MIT license
   for code; no private Content data or learner records in either
   distribution.
5. **No mutation:** import/install/export never overwrites learner notes,
   changes current resource maps, grants commercial access, awards formal
   credit, promotes OEE status or silently upgrades released material.
6. **Current-only consumers:** Workspace and private Content reject
   unsupported old exported source identities; no compatibility
   readers, auto-migration or arbitrary current-main fallback.
7. **Review:** independent maintainer staging and artifact examination,
   source file completeness, rights provenance, semantic quality
   boundaries and explicit steward publication decision are recorded.

Tests validate structural and distribution behavior only; source
educational quality and real course conformance require separate
human evidence.

## 9. Open questions

The release scope, UTC-month CalVer IDs, GitHub Releases distribution,
reproducible uncompressed TAR, offline lockfile resolution and source
integrity requirements are decided in Section 10.

A separate implementation review must select and test the precise signing
and attestation mechanism before *any* archive can be distributed. The
steward retains publication and revocation authority. The candidate
implementation may proceed without distribution approval; the consumer
cutover remains gated on verified release artifacts and independent review.

The package release schedule remains an operational decision, not an
alternative semantic version for OEE curriculum.

## 10. Decision

- **Decision:** Accepted for implementation design; does **not** authorize publication or consumer deployment.
- **Decision date:** 2026-11-20
- **Decision-maker:** OEE steward (project owner, instruction to proceed after review).
- **Rationale:** Eliminate raw Git-revision inputs from independent learner and
  author workflows without sacrificing exact source provenance, reproducibility,
  licensed distribution boundaries or the single-parser requirement.
  Immutable content digests and a separately reviewed release lock replace
  the moving-reference and manual-checkout requirements.
- **Adopted architecture:** Whole-curriculum source closure; immutable CalVer
  `YYYY.MM.N` IDs; content-addressed, deterministic uncompressed TAR and
  canonical manifest; OEE GitHub Releases as an artifact transport; manifest
  digest locks; offline-only consumer resolution; Toolkit exportVersion 2;
  no Git-based consumer fallback or historical-format readers.
- **Conditions:** Before **any** release asset or Toolkit package publication,
  review a concrete signed-provenance/attestation method, license notices,
  artifact provenance, cross-platform test results and exact build hash.
  Before Workspace/Content cutover, review the completed Toolkit export and
  manifest protocol and confirm non-disposable learner/host data safety.
  Do not alter OEE `v0.2.0` normative course requirements.
- **Implementation tracking:** [Stage 2 tracker #257](https://github.com/0xbuffdev/open-engineering-education/issues/257).
  REL-I01 follows only after the accepted RFC has actually merged to
  `main`; issue discussion or a still-open PR does not remove this gate.
- **Implementation pull request:** pending.
