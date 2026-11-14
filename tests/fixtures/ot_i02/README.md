# Frozen structural validation fixtures (OT-I02)

These **synthetic** files are regression fixtures stored and versioned in Git.
They are not canonical OEE curriculum, do not enter the program catalogs,
and must not be represented as learner-tested or verified courses.
Their checked-in Git revision pins their contents for reproducible tests.

| Fixture | Expected behavior in the current maintenance checker |
| --- | --- |
| `valid_v020_course.md` | v0.2.0 structural pass, but **not** pedagogical conformance |
| `legacy_v010_course.md` | Classified as older unsupported format; direct outcome-only check fails |
| `linked_brief_v020.md` and `linked_brief.md` | Valid *candidate* linked-brief expression; current inline-only parser **cannot validate it** and must never report a structural pass without verifying the brief |

`test_toolkit_fixture_contract.py` exercises these files and additional
in-memory negative mutations (unsupported/contradictory version marker,
duplicate IDs, missing required coverage, invalid assessment fields,
project defense and missing linked brief). It does not create a second
course schema or implement old-format compatibility.

The current `scripts/check-outcome-curriculum.py` is a **migration-era,
inline-only** checker; a failure for linked syntax may reflect
`parser_limitation`, not a normative requirement violation. The public
Toolkit must support that brief *or* return an explicit incomplete/limitation
diagnostic (OT-I03), never a false conformance claim.

**Scope boundary:** No fixtures here assert that current legacy SEF/APP
validators become Toolkit APIs. The new Toolkit is strict v0.2.0-only.
