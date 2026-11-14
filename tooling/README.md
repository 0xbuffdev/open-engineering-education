# Draft OEE Toolkit — Immutable, Offline Curriculum Views

**Status:** implementation proposal for OT-I04; **not an official release**.
[RFC 0002](../rfcs/0002-toolkit-stewardship-and-licensing.md) is
still draft and public [issue #57](https://github.com/0xbuffdev/open-engineering-education/issues/57)
requires the steward's explicit governance and license-scope decision.
This code is independently reviewable, but **must not be advertised as
official or merged as an approved tool** before its governance gate is met.

This implementation reads outcome-driven **OEE v0.2.0 only** from local
Git objects at one **full, immutable 40-character commit SHA**. It never
reads educational input from moving HEAD, the index or an uncommitted
worktree, and it never fetches a Git remote.

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

Use --output - to write derived JSON to stdout. A file export is written
atomically only **after** the entire selected course passes structural
checks; a missing/unsupported source leaves an existing destination
untouched. The proposed Python invocation is currently located under
tooling/; the final installed command and packaging need a separate
public review and must not be assumed from this draft.

**Exit codes:** 0 structurally passed; 1 structural violation or unsafe
reference; 2 invalid CLI arguments; 3 missing/incomplete/unsupported
input; 4 unexpected local Git or tool failure.

A repository-wide --all inspection is **incomplete** while any active
course remains in an older or unrecognized format, even if all migrated
v0.2.0 courses pass. There is no old-format compatibility reader,
converter or transparent schema negotiation.

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
or establish that legacy prerequisites conform to v0.2.0.

This draft implements course check and course export, with a read-only
repository inspection. Full program-catalog export, a distributable CLI
package, public release numbering and independent governance approval are
**not yet included or claimed**. The README explicitly documents this
scope so a partial implementation is not presented as a complete release.

Tests build isolated synthetic local Git repositories and exercise:
immutable revisions across dirty worktrees/moved HEAD, byte-identical
exports, valid/invalid public briefs, missing/unknown sources, unsupported
legacy files, path traversal and symlinks, protected atomic output, and
offline CLI behavior.

Run:

~~~sh
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 -m unittest discover -s tests -p 'test_toolkit_pinned_export.py' -v
~~~

**Licensing proposed, not adopted:** MIT for new Toolkit software,
software schema and test code, preserving CC BY 4.0 for normative OEE
specification/course text. A steward's recorded file-level approval and
notice review remain prerequisites to official publication. No existing
contributor's license is retroactively altered by this PR.
