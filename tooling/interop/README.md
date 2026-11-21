# Pinned curriculum exports and Workspace interoperability

These internal source-golden checks verify reproducible historical pinned
exports and an independently pinned OEE Workspace consumer. The active
installed Toolkit uses only offline digest-locked release exports v2;
see [REL-I03](../RELEASE-CONSUMER.md). The Toolkit architecture was accepted in
[RFC 0002](../../rfcs/0002-toolkit-stewardship-and-licensing.md).
Passing the checks does **not** publish an official Toolkit package,
establish educational conformance, or promote a course's readiness status.
See the [OT-I05 release-readiness checklist](../RELEASE-READINESS.md)
for independent smoke and separate public steward approval.

## Immutable source and generated fixtures

[`fixtures/pins.json`](fixtures/pins.json) is the **single recorded
source-revision and consumer-revision pin**. Four golden snapshots under
`golden/` are generated with the one public OEE Toolkit parser from
that exact immutable Git tree: **SEF1, SEF10, APP1 and APP17**.

The golden snapshots are **derived exports, not alternative editable
curriculum or normative specification**. They contain excerpts of OEE
educational requirements, which retain the applicable **CC BY 4.0**
educational attribution/licensing. Toolkit implementation and test code
is subject to the file-level licensing scope in
[Toolkit licensing](../LICENSING.md). The checks do not relicense
contributed educational text.

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

## Independent current Workspace consumer

The manifest's full Workspace consumer commit now references the **merged
current Workspace v2 and CLI release-readiness source**, rather than an
old pre-v2 checkout. The golden exports continue to represent their own
**historical exact OEE source revision**, preserving independent regression
provenance.

The [interoperability workflow](../../.github/workflows/toolkit-interop.yml)
checks out the **public Workspace consumer at the exact commit
declared in the fixture manifest**, not moving Workspace main.
It runs `scripts/verify-oee-export.py` from that Workspace source
against real committed OEE golden exports and requires:

- Export format 1, OEE v0.2.0, canonical course/path, complete required
  outcomes and assessment coverage, and a matching selected 40-char SHA.
- Explicit **wrong-SHA rejection**, including when all other output
  fields remain plausible.
- Explicit rejection of the **resource-map schema v1 negative
  fixture**, without a runtime converter or acceptance of stale module
  numbers.
- The current reviewed Workspace v2 map is **rejected** against
  historical golden exports from a different source commit and
  **accepted** against a fresh Toolkit export from the map's recorded
  exact OEE revision. An exported historical snapshot does not certify
  the contents of a newer mapping.
- No private service, paid resource, network lookup or competing OEE
  Markdown interpretation in Workspace.

**Scope limitation:** These tests verify the declared export and consumer
contract, not the educational accuracy or approval of Workspace resource
maps. Schema changes, source mappings, and other Workspace-specific
requirements must be reviewed independently in the Workspace repository.

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

## Updating consumer pins

The fixture manifest records an exact Workspace consumer commit, not a
floating branch. When the consumer changes, review the new revision,
update the manifest pin, and rerun the contract tests. The CI checkout
resolves its consumer revision from the same manifest.

An interoperability pass does not automatically approve changes to
curriculum, resource mappings or learner evidence. This integration
does not add backward compatibility, require a private service, or
establish a formal OEE conformance claim.
