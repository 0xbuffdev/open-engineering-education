# OEE Architecture Decision Records

These records document **proposed engineering implementation choices** for Open Engineering Education (OEE). They do not amend the published OEE specification, assert course conformance, approve migrations, or replace the [RFC process](../../rfcs/README.md).

An ADR is a reviewable decision about how to build or integrate software. Normative educational requirements belong in [`spec/`](../../spec/README.md) and must follow [governance](../../GOVERNANCE.md). A proposed ADR becomes accepted only after explicit steward review and a recorded decision; merging a document does not by itself authorize an unapproved normative change.

| ADR | Status | Scope |
| --- | --- | --- |
| [ADR-0001 — Canonical Markdown and deterministic curriculum exports](0001-canonical-markdown-and-curriculum-exports.md) | Proposed | OEE tooling and downstream read contract |
| [ADR-0002 — Revision identities and non-destructive course migrations](0002-revision-identities-and-course-migrations.md) | Proposed | OEE curriculum change and consumer compatibility |

Related proposed OEE Workspace decisions (kept in that repository): ADR-0003 for evidence records, ADR-0004 for local tooling, ADR-0005 for resource mapping synchronization, and ADR-0006 for optional AI integration.

## Decision lifecycle

- **Proposed:** candidate design; no claim of implementation, conformance, or normative authority.
- **Accepted:** reviewed and explicitly accepted by the appropriate maintainers.
- **Superseded:** replaced by a named subsequent decision; retain the history.
- **Rejected:** evaluated and not adopted; preserve the reasoning.

Each ADR records context, the recommended decision, alternatives, consequences, implementation gates, and follow-up specification work. An accepted ADR can guide repository tooling but cannot weaken or extend a normative `MUST` in OEE without an accepted RFC and corresponding specification change.

## Change and compatibility discipline

Keep one canonical source for each requirement. Cross-repository consumers must not maintain independent editable versions of OEE outcomes or completion rules. Changes to published requirements must be revision-aware and preserve the interpretation of historical learner evidence. All proposed implementation contracts require independent tests before claiming supported interoperability.
