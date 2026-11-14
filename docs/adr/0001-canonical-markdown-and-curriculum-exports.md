# ADR-0001: Canonical Markdown and deterministic curriculum exports

- **Status:** Proposed
- **Date:** 2026-11-14
- **Scope:** OEE repository tooling; public, non-normative export for consumers
- **Decision owner:** OEE steward
- **Depends on:** Existing [Course Format](../../spec/course-format.md), [Conformance](../../spec/conformance.md), and [Implementation Boundary](../../spec/implementation-boundary.md)
- **Related:** ADR-0002; OEE Workspace ADR-0003 and ADR-0005 (proposed separately)

## Context

OEE v0.2.0 defines canonical public course requirements as Markdown: metadata, outcomes with stable IDs, instructional modules, and assessments tied to required outcomes. The current structural checker recognizes only particular inline Markdown patterns. The specification also permits authoritative linked assessment briefs, which the current narrow parser does not fully support. Structural validation never proves pedagogical conformance.

OEE Workspace, 0xNAND, and potential third-party implementations need repeatable access to course identity, revision, catalog order, prerequisite relationships, outcomes, assessments, and published criteria without scraping Markdown independently or maintaining a duplicate editable source.

The curriculum is still mixed-format. SEF1, SEF10, and APP1 have v0.2.0 course definitions; other courses may use older formats. Any exporter must report this distinction, not turn legacy content into invented v0.2.0 evidence.

## Decision

1. **Markdown remains authoritative.** OEE's published specification, course documents, program catalogs, and explicitly linked public assessment briefs are the only editorial sources for their educational requirements. No parallel JSON or database authoring system will be added merely for consumption.
2. **Provide a deterministic, versioned derived export.** A supported OEE tool will transform a deliberately selected Git commit into an immutable consumer snapshot. Export formats and schemas describe *tool interoperability*; they are not automatically added to the normative Course Format.
3. **Preserve provenance.** Every exported course includes its stable code, source path, full source commit SHA, declared specification version (or explicit legacy/unknown classification), exporter schema version, and source references for requirements. Distinguish an OEE release tag, Git commit, and course requirement identity. An export must not silently substitute the checked-out latest branch.
4. **Preserve meaningful structure and authority.** The export represents program catalog row order separately from course code; core/elective classification, prerequisite relationships, modules, explicitly required versus optional activities, outcome IDs, required assessment IDs, criteria, and evidence references. Linked authoritative briefs must be resolved or explicitly identified as unresolved, never silently ignored.
5. **No semantic invention.** An incomplete, unsupported, ambiguous, or legacy format is recorded as unsupported/legacy with diagnostic information, rather than heuristically fabricating missing outcomes, requirements, completion decisions, or readiness claims. A partial export is explicitly labeled and cannot be presented as complete coverage.
6. **One parsing and validation implementation.** Existing OEE validator entry points should share a core parsing/validation library with the exporter instead of implementing divergent regular-expression interpretations. Parsing checks syntax and references; structural validation checks enforceable constraints; substantive review remains separate.
7. **Deterministic output.** For identical committed inputs and exporter version, serialized records and ordering are reproducible. Avoid timestamps or current branch lookups in identity-bearing output. A reproducible manifest index may enumerate included courses, their parsing status, and file digests.
8. **No paid service requirement.** Consumers may read a committed snapshot or generate it offline from a local checkout. OEE does not mandate a hosted API, JavaScript runtime, learning platform, or proprietary service.

The initial export scope should be the migrated v0.2.0 pilots and the APP catalog, then broaden only with explicit parser coverage and reviewable fixtures. Optional module/lesson IDs are not made mandatory by this ADR. An export must preserve current identities without deriving permanent IDs from numeric suffixes or title text.

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Maintain Markdown and JSON manually in parallel | Creates conflicting sources of truth and synchronization debt |
| Replace Markdown with a database or bespoke DSL | Breaks human-readable authoring and requires a separate normative migration |
| Let every consumer parse Markdown independently | Produces incompatible interpretations and drifting validation |
| Force all legacy courses into a v0.2.0-shaped export | Conceals real migration work and overstates conformance |
| Start with a hosted curriculum API | Adds hosting, availability, and maintenance dependencies before a stable format exists |

## Consequences

The exporter creates an additional **derived artifact**, not another source of course requirements. It will need explicit schema-version compatibility rules, parsers for supported Markdown variants and linked briefs, and fixtures to show exact coverage. Developers may use the export for navigation, scaffolding, and evidence references, but passing export validation does **not** establish course readiness, learner mastery, or implementation conformance.

Consumers must treat missing data as unknown rather than interpreting an absent mandatory assessment as no assessment required. A catalog may refer to future migration work; only current canonical published files and catalog state may be represented as active.

## Implementation and test gates

1. Record representative parsing fixtures for SEF1, SEF10, APP1, the APP catalog, at least one legacy course, a linked assessment brief, and malformed or missing linked content.
2. Define an export schema and compatibility policy, including deterministic ordering, provenance, strict failures, and partial-coverage diagnostics. Keep this schema in implementation/tooling documentation unless governance adopts normative constraints.
3. Refactor shared parsing/validation so exporters and existing validators cannot disagree silently about the same input. Preserve legacy checks while legacy sources remain.
4. Add golden snapshot tests for repeatability and round-trip cross-checks for all exported IDs and required assessment links.
5. Exercise a separate OEE Workspace consumer against a pinned OEE commit, including deliberately incompatible revisions.
6. Publish an explicit supported-input matrix. Do not advertise complete program exports while legacy or unsupported course definitions remain.

## Governance and deferred work

This ADR selects an implementation strategy; it does **not** revise the v0.2.0 course format or require every independent OEE implementation to consume JSON. If stable module/lesson IDs, new compulsory metadata, or a mandatory interchange format becomes a condition of OEE conformance, propose and accept an RFC first. Assessment validity and course status still require their existing human/evidence review gates.
