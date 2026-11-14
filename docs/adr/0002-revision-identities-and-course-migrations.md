# ADR-0002: Revision identities and non-destructive course migrations

- **Status:** Proposed
- **Date:** 2026-11-14
- **Scope:** OEE versioned curriculum requirements and downstream identity resolution
- **Decision owner:** OEE steward
- **Depends on:** [Course Format](../../spec/course-format.md), [Evidence Rules](../../spec/evidence-rules.md), [Conformance](../../spec/conformance.md), and ADR-0001
- **Related:** OEE Workspace ADR-0003 and ADR-0005 (proposed separately)

## Context

OEE v0.2.0 is a breaking draft authoring revision. Its stable course outcome and assessment identifiers do not make every earlier course completion equivalent to a new one. The published specification already preserves earlier course revisions and learner evidence under the requirements that originally governed them.

The APP migration preserves historical identities APP1–APP16, while allocating APP17–APP21 for genuinely new capabilities. The ordered catalog, rather than numeric suffixes, defines progression. SEF1 changed from ten modules to eight during migration, and OEE Workspace's current resource map still references the older ten-module structure. A consumer that reads `main` while recording a different source revision cannot reliably interpret requirements.

## Decision

1. **Separate three kinds of identity.** `courseCode` identifies a continuing curriculum capability; `specificationVersion` identifies the applicable educational contract; and a full Git commit SHA plus canonical course path identifies the exact source revision used for an assessment, resource map, or export. A release tag is a human-friendly reference, not a substitute for content-addressed source identity.
2. **Keep outcome and assessment IDs stable within the course.** Editorial changes retain IDs when capability and evaluation meaning are preserved. Material replacements, splits, merges, and changed acceptance criteria require a documented correspondence and explicit compatibility review; reused text labels do not imply equivalence.
3. **Do not infer progression from identifiers.** Catalog row order and explicitly declared prerequisites are authoritative. Course codes are not ordinal steps. Core/elective designation and course readiness status are different dimensions.
4. **Freeze the assessed contract, not the entire learner workspace.** A learner evidence record identifies the exact published course requirements under which it was evaluated, including an available source commit and applicable specification version. Later curriculum publication must not change that record's meaning.
5. **Classify differences explicitly.** Consumers distinguish: editorial-only changes; non-breaking clarifications; changes to prerequisites or catalog placement; material outcome/assessment/criteria changes; and unsupported or structurally unparseable source revisions. Automated comparison can identify potential changes but must not establish educational equivalence by itself.
6. **Migration is explicit and non-destructive.** A changed course never silently marks prior learners complete or incomplete. Old evidence remains linked to old requirements. Where a material change affects claimed competence, an authorized reviewer decides whether old evidence suffices, requires supplemental assessment, or remains historical only.
7. **Downstream update is deliberate.** Resource maps, generated guides, learner progress, and 0xNAND integrations pin a source revision or clearly disclose a live/unpinned preview mode. Any tool updating a source revision must validate structure, detect drift, and report changes before rewriting derived state.
8. **Legacy remains legacy until reviewed.** Transferred SYS, AI, and SEC drafts and unmigrated SEF/APP courses do not acquire v0.2.0 compliance from copying files or running a generic checker. Their prerequisite discrepancies and program metadata must be reconciled through separate curriculum reviews.

## Compatibility model

| Change | Required response |
| --- | --- |
| Typographical clarification with unchanged meaning | Retain stable IDs, record source revision, update downstream display deliberately |
| Catalog sequence or prerequisite adjustment | Revalidate dependencies and consumer reading paths; do not reinterpret completed requirements |
| Materially changed outcome, rubric, or assessment | Identify new requirement identity or explicit versioned correspondence; require substantive equivalence review |
| Legacy course migrated to v0.2.0 | Publish migration notes, required assessments, outcome coverage, and scope of historic evidence |
| Unavailable or mismatched source commit | Fail strict resolution with actionable diagnostics; never silently replace with `main` |
| Unchanged assessment under newer revision | Preserve original record and optionally associate a reviewed compatibility claim, without rewriting provenance |

## Alternatives considered

| Alternative | Reason not selected |
| --- | --- |
| Always resolve latest `main` | Changes learner requirements without notice and breaks reproducibility |
| Use semantic version alone for a course | OEE repo release versions do not uniquely describe individual evolving course files |
| Rename every course during migration | Breaks existing references even where the capability is still recognizable |
| Automatically upgrade historical completions | Confuses historical work with outcomes never assessed |
| Make every minor editorial change a new outcome ID | Creates identity churn without educational benefit |

## Consequences

Consumers need a consistent resolver, compatibility diagnostics, and provenance in exported records. The same course may be represented by several historical valid source revisions. Neither an old completion nor a Git commit proves mastery by itself. Adopting this design should reduce drift while preserving flexibility to improve an early-stage draft curriculum.

The Git SHA is a precise content reference, not a guarantee that an arbitrary remote will retain commits forever. Consumers needing long-term reproducibility should retain lawful snapshots or generated archives with source digests. Sensitive evidence does not belong in the public OEE repository.

## Implementation and test gates

1. Document the identifier and revision-resolution rules in the non-normative export/consumer contract.
2. Add fixtures for editorial edits, changed prerequisite paths, changed required assessments, course splits, deleted source revisions, and legacy-to-v0.2.0 migration.
3. Verify that APP17 is introduced as its own identity, not inserted by renumbering existing courses.
4. Verify that migrated resource maps fail a strict mismatch when their pinned revision differs and cannot be resolved, while supporting explicitly reviewed remapping to the intended new revision.
5. Confirm no migration process writes into a learner's existing evidence or history without explicit authorization.
6. Update downstream integration guidance and test a pinned cross-repository consumer before claiming interoperability.

## Governance and deferred work

This ADR operationalizes existing historical-integrity principles. It does not independently elevate new metadata fields, a particular source protocol, or a portability schema into normative requirements. Any change that strengthens current `SHOULD` guidance to a new OEE `MUST`, changes completion requirements, or affects conformance must pass an accepted RFC followed by specification review. The v0.2.0 release citation erratum is tracked separately in [issue #46](https://github.com/0xbuffdev/open-engineering-education/issues/46); this ADR does not move or rewrite the published release tag.
