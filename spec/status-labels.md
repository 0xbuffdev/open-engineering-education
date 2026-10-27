# Status Labels

The curriculum is thousands of hours of material at varying stages of proof. Status labels say which stage each course is actually at. They exist so the repository never implies readiness it has not earned.

## The labels

| Label | Meaning | Requirement |
| --- | --- | --- |
| `draft` | Written, not yet run by a learner. | The course file exists and follows [course-format.md](course-format.md). |
| `tested` | At least one learner completed it and the course was revised from their feedback. | Evidence link, revision note. |
| `verified` | Multiple learners completed it; exit check and labs reproduced; chapter maps checked against the cited editions. | Evidence links, reviewer sign-off. |

Evidence requirements are defined in [evidence-rules.md](evidence-rules.md).

## Where a label appears

1. In the course file header: `**Status:** \`draft\` · [status labels](../spec/status-labels.md)`.
2. In the course's row in the track README table (for example [curriculum/foundations/README.md](../curriculum/foundations/README.md)).

Both must agree. A pull request that changes one and not the other is incomplete.

## Promotion rules

- **Start at `draft`.** Every course starts as `draft`; all courses are `draft` today.
- **Promote only on evidence.** No date, effort, or good intention promotes a course. Only the requirements in the table above do.
- **Promotion is a commit like any other.** The evidence links and the revision note go in the same commit that changes the label.
- **Labels come down too.** If a `tested` or `verified` course's evidence links stop resolving, or a defect is found that the course's own exit check missed, relabel to the level the evidence still supports and say so.

## What labels are for

- Learners can decide what to trust before spending 100 hours.
- Contributors know what a course needs to be promoted (`chapter-map-verify`, `lab-test-case`; see [CONTRIBUTING](../governance/CONTRIBUTING.md)).
- The steward cannot quietly overstate readiness, because the label is next to the course name.

## What labels are not

- Not a quality ranking between tracks. A `draft` systems course is not worse than a `draft` foundations course; it is less proven.
- Not a license to imply the rest of the repository is ready. Label status is per course, and the repository-level status is in the [README](../README.md).
