# OT-I06 — Pinned Golden Exports and Workspace Consumer Contract

**Status:** Draft interoperability PR. The [Toolkit RFC 0002](../../rfcs/0002-toolkit-stewardship-and-licensing.md)
remains a draft pending the steward decision in
[issue #57](https://github.com/0xbuffdev/open-engineering-education/issues/57).
Passing these checks does **not** publish an official Toolkit, certify
course conformance or promote a course's readiness status.

## Immutable source and generated fixtures

[`fixtures/pins.json`](fixtures/pins.json) is the **single recorded
source-revision and consumer-revision pin**. Four golden snapshots under
`golden/` are generated with the one public OEE Toolkit parser from
that exact immutable Git tree: **SEF1, SEF10, APP1 and APP17**.

The golden snapshots are **derived exports, not alternative editable
curriculum or normative specification**. They contain excerpts of OEE
educational requirements, which retain the applicable **CC BY 4.0**
educational attribution/licensing. Toolkit implementation and test code
is subject to the separately reviewed software licensing decision.
No contributed educational text is silently relicensed by this PR.

From an offline OEE checkout containing that historical commit:

~~~sh
python3 tooling/interop/verify_golden.py --repo .
~~~

The command regenerates each snapshot twice at the **manifest's full
Git SHA**, byte-compares canonical UTF-8/LF JSON to the committed files
and rejects missing objects, corrupted snapshots, extra files or
unsupported sources. It does **not** auto-rewrite snapshots.

For an intentional reviewed baseline update only:

~~~sh
python3 tooling/interop/verify_golden.py --repo . --emit
~~~

The emitted records are candidates for a **separately reviewed PR**.
Never auto-repin to the latest branch or infer that same-identifier
assessments are pedagogically equivalent after a criteria change.

## Independent Workspace consumer

The [OT-I06 workflow](../../.github/workflows/toolkit-interop.yml)
checks out the **public Workspace consumer at the exact commit
declared in the fixture manifest**, not moving Workspace main.
It runs `scripts/verify-oee-export.py` from that Workspace source
against real committed OEE golden exports and requires:

- Export format 1, OEE v0.2.0, canonical course/path, complete required
  outcomes and assessment coverage, and a matching selected 40-char SHA.
- Explicit **wrong-SHA rejection**, including when all other output
  fields remain plausible.
- Explicit rejection of Workspace **resource-map schema v1**, without
  a converter, old-course parser, or reusing stale module numbers.
- No private service, paid resource, network lookup or competing OEE
  Markdown interpretation in Workspace.

**Dependency:** Workspace's old v1 SEF1 map remains **unreviewed for the
new course revision**. WS-I03 (v2 schema), WS-I01 (pinned map validation)
and WS-I02 (reviewed v2 SEF1 map) have not been completed. These
golden/consumer tests are a valuable independent integration seam, but
cannot establish release-ready v2 Workspace mapping by themselves.

## Advisory source drift report

Pass the baseline snapshot and **both explicit revisions**:

~~~sh
python3 tooling/interop/drift.py \
  --repo . \
  --base-export tooling/interop/golden/SEF1.json \
  --base-revision PIN_FROM_MANIFEST \
  --target-revision FULL_TARGET_COMMIT_SHA
~~~

Optionally append `--workspace-map /path/to/v2-map.json`.
The result is deterministic JSON listing added, removed or changed
outcome descriptions, assessment work/criteria/evidence, required
coverage, module/lesson navigation and prerequisites. For a valid
baseline-pinned **v2** map, it also identifies affected resource IDs.

The advisory distinguishes `source_missing`, `unsupported_version`,
`unsupported_map_schema` and `source_mismatch`. No old schema is
reinterpreted, no learner evidence is rewritten, and **no resource
map or course revision is automatically updated**. An output of
`compatible` indicates only observed structural equality, not
substantive equivalence or authorization to repin.

## Tests

~~~sh
python3 -m unittest discover -s tests -p 'test_toolkit_interop.py' -v
python3 -m unittest discover -s tests -p 'test_*.py' -v
~~~

CI additionally exercises all four real pinned source exports, the
independent Workspace consumer and a separate advisory current-HEAD
comparison. Current HEAD is supplied as an explicit full SHA, not
silently substituted for the manifest's revision.

## Review order

Review [Workspace consumer PR #5](https://github.com/0xbuffdev/oee-workspace/pull/5)
before finalizing the OEE interoperation PR. If that PR merges at a
different commit SHA, update **both** the manifest and the CI checkout
to the new reviewed commit and re-run the contract tests. The current
consumer checkout is deliberately pinned to the reviewable PR commit,
not a floating branch.

The Workspace schema-v2 and pinned map-validator dependencies still
need separate source reviews. Merging an export-fixture PR does not
automatically complete those tickets.

**No curriculum rewrites, backward compatibility, compulsory private
integration, verified learner claims or formal conformance claims.**
