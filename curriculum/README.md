# OEE Curriculum

The Open Engineering Education (OEE) curriculum publishes five engineering programs and their course definitions. It is designed for independent learners, educators, reviewers, and implementations that need a common, publicly inspectable educational contract.

**Current state:** All five programs have published draft course definitions. [SEF](SEF/README.md) now has eleven outcome-driven `v0.2.0` core courses and a cumulative graduation capstone; [APP](APP/README.md) has fourteen outcome-driven `v0.2.0` core courses (including its capstone) and seven optional outcome-driven electives. All of these courses remain `draft` pending real learner and independent reviewer evidence. SYS now has ten outcome-driven `v0.2.0` draft core courses and a cumulative systems graduation capstone. **Integration branch only:** AI has twelve staged outcome-driven draft course definitions (AI1–AI12); the planned expanded AI1–AI20 sequence is incomplete, and the nine-course legacy AI catalog on `main` remains authoritative until an explicitly reviewed atomic cutover. SEC retains legacy course definitions. Source format or structural validation does not establish educational effectiveness or formal conformance.

## Choose a program

Each program README is the authoritative catalog for its **current** courses, study order, classification, and prerequisites.

| Code | Program | Course files in this revision | Catalog |
| --- | --- | --- | --- |
| `SEF` | Software Engineering Foundations | 11 core | [Explore SEF](SEF/README.md) |
| `APP` | Application Engineering | 14 core, 7 electives | [Explore APP](APP/README.md) |
| `SYS` | Systems Engineering | 10 core | [Explore SYS](SYS/README.md) |
| `AI` | AI Engineering | 12 staged core (integration only; program incomplete) | [Explore AI](AI/README.md) |
| `SEC` | Security Engineering | 9 core | [Explore SEC](SEC/README.md) |
| **Total** | **Five programs** | **56 core, 7 electives** | |

SEF provides the completed current **foundational curriculum design**, including [SEF11 discrete mathematics](SEF/SEF11.md) before algorithmic and numerical mathematics, plus a one-project [SEF10 capstone](SEF/SEF10.md) with ten prior-course evidence checks. APP develops applications and production delivery; **SYS develops machine-level understanding, Rust, OS internals, concurrency, networking, storage, distributed correctness and production systems engineering**; AI develops data, model, and production AI capabilities; SEC applies security engineering to systems and applications.

The APP catalog contains 14 required core courses and seven genuinely optional electives. The [current APP catalog](APP/README.md) and linked course definitions publish the authoritative study sequence, prerequisites and graduation requirements; reviewed Git history preserves earlier design rationale. Learner completion records retain the course revisions under which their evidence was evaluated.

## Follow a course

1. Open a program catalog and choose a course whose listed prerequisites you satisfy.
2. Read the canonical course file for its outcomes, learning sequence, and completion requirements.
3. Complete the required work and preserve reviewable evidence of the outcomes assessed.
4. Use a learner-controlled environment or [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) to organize implementations, investigations, projects, notes, and evidence.

The curriculum describes **what must be learned and demonstrated**, not a required paid platform or book purchase. Instruction and supplementary resources may differ among independent learners, educators, and learning products.

## Understand published status

A course's `draft`, `tested`, or `verified` label describes its **educational readiness evidence**, not its specification-format version. The definitive thresholds and promotion rules belong to [Status Labels](../spec/status-labels.md).

Likewise, a file being present or passing a structural check does not establish `v0.2.0` conformance. Legacy course revisions retain their historical requirements until explicitly migrated; they must not be silently reclassified. Consult the [curriculum inventory](INVENTORY.md) for reproducible, commit-pinned migration and structural reports.

## Where requirements live

| Source | Responsibility |
| --- | --- |
| [OEE specification](../spec/README.md) | Shared educational, evidence, status, and conformance requirements |
| Program READMEs (linked above) | Current program-level course sequence, classification, and prerequisites |
| Individual course files | Course-specific outcomes, learning sequence, assessed work, and completion conditions |
| [Curriculum Design Guide](DESIGN-GUIDE.md) | Non-normative writing and course-design advice |
| [Curriculum inventory](INVENTORY.md) | Generated observations about the published files, not a second curriculum registry |

Program and course authors should make changes in the authoritative file, then update affected references. Public RFCs record adopted decisions and rationale; future plans and implementation notes do not silently override the current catalog or course requirements.

## Contribute or teach with OEE

Educators can adapt explanations, exercises, and delivery to learners' circumstances without misrepresenting the published completion requirements. Course authors and reviewers should begin with the [Course Format](../spec/course-format.md), [Evidence Rules](../spec/evidence-rules.md), and the non-normative [Curriculum Design Guide](DESIGN-GUIDE.md).

For correction and review procedures, see [Contributing](../CONTRIBUTING.md). Changes to binding, repository-wide educational requirements follow [OEE governance](../GOVERNANCE.md) and the [RFC process](../rfcs/README.md). No program or course is promoted to a higher readiness label without the applicable review evidence.
