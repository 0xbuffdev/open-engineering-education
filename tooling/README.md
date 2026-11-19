# OEE Toolkit

The Toolkit checks OEE course structure and produces deterministic curriculum exports from Git. It is a repository-local implementation of the approach accepted in [RFC 0002](../rfcs/0002-toolkit-stewardship-and-licensing.md).

The Toolkit has not been published as a standalone package, and its library API is not stable. Distribution and support will need a separate release review. [Toolkit licensing](LICENSING.md) explains which licenses apply to its files.

The Toolkit reads **OEE v0.2.0 course sources only** at a full, immutable 40-character Git commit SHA. It reads local Git objects and does not fetch a remote or take educational source from a moving branch, the index, or an uncommitted worktree.

The only editable educational source is the public OEE specification and
curriculum Markdown. The exported JSON is derived data, not a second
authoring format, conformance certificate, learner grade or evidence of
the course having been tested or verified.

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
untouched. The implemented repository-local Python command is
`python3 -m tooling.oee_toolkit`; no separately installed
`oee_toolkit` package, stabilized importable API or Toolkit semantic
version is approved yet. Public distribution, API support and release
mechanisms require a separate review.

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
- The existing scripts/check-outcome-curriculum.py remains the **single
  parser and structural validator**. Its optional extraction callback
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
repository inspection. Full program-catalog export, a distributable CLI
package and public release numbering are **not implemented or claimed**.
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
