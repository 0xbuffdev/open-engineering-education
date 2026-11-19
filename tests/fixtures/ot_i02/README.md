# Structural validation fixtures

These **synthetic** Markdown files exercise the outcome-driven structural
checker and the repository-local Toolkit. They are test fixtures, **not**
canonical curriculum or evidence that a course has been taught or verified.
The fixtures support outcome-based structural and Toolkit regression checks.

| Fixture | Expected behavior |
| --- | --- |
| `valid_v020_course.md` | Passes supported `v0.2.0` structural checks, not educational conformance |
| `unsupported_v010_course.md` | Is rejected as unsupported by the outcome-only checker |
| `linked_brief_v020.md` and `linked_brief.md` | Pass when the local linked brief resolves and supplies the required assessment fields |

The [fixture regression tests](../../test_toolkit_fixture_contract.py)
cover valid and unsupported source formats, conflicting version markers,
duplicate IDs, missing outcome coverage, incomplete assessment fields,
project-defense requirements, and linked-brief resolution.

The shared [outcome checker](../../../scripts/check-outcome-curriculum.py)
accepts supported repository-local assessment briefs and reports missing
or unsupported inputs as incomplete, rather than treating them as passed.
The [Toolkit](../../../tooling/README.md) additionally checks content
at an immutable Git commit; neither check certifies educational quality
or accepts a source with an unsupported specification version.
