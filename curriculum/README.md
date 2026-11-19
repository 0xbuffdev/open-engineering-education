# OEE Curriculum

The Open Engineering Education (OEE) curriculum publishes five engineering programs and their course definitions. It is designed for independent learners, educators, reviewers, and implementations that need a common, publicly inspectable educational contract.

**Current state:** All five programs have published draft course definitions. [SEF](SEF/README.md) now has eleven outcome-driven `v0.2.0` core courses and a cumulative graduation capstone; [APP](APP/README.md) has fourteen outcome-driven `v0.2.0` core courses (including its capstone) and seven optional outcome-driven electives. All of these courses remain `draft` pending real learner and independent reviewer evidence. SYS now has ten outcome-driven `v0.2.0` draft core courses and a cumulative systems graduation capstone; AI1 publishes an outcome-driven `v0.2.0` draft. AI2–AI9 remain draft outlines pending the separate AI program integration. The SEC catalog now publishes twelve outcome-driven `v0.2.0` draft core courses, including enterprise identity, endpoint defense, continuous vulnerability management and a capstone requiring evidence of all core predecessors. Source format or structural validation does not establish educational effectiveness or formal conformance.

## Choose a program

Each program README is the authoritative catalog for its **current** courses, study order, classification, and prerequisites.

| Code | Program | Published course files | Catalog |
| --- | --- | --- | --- |
| `SEF` | Software Engineering Foundations | 11 core | [Explore SEF](SEF/README.md) |
| `APP` | Application Engineering | 14 core, 7 electives | [Explore APP](APP/README.md) |
| `SYS` | Systems Engineering | 10 core | [Explore SYS](SYS/README.md) |
| `AI` | AI Engineering | 9 core | [Explore AI](AI/README.md) |
| `SEC` | Security Engineering | 12 core | [Explore SEC](SEC/README.md) |
| **Total** | **Five programs** | **56 core, 7 electives** | |

SEF publishes eleven required draft courses, including [SEF11 discrete mathematics](SEF/SEF11.md) before algorithms and numerical mathematics and a one-project [SEF10 capstone](SEF/SEF10.md) that verifies all ten prior-course completions. Course requirements are public; learner-tested readiness has not yet been established. APP develops applications and production delivery; **SYS develops machine-level understanding, Rust, OS internals, concurrency, networking, storage, distributed correctness and production systems engineering**; AI develops data, model, and production AI capabilities; SEC applies security engineering to software, enterprise identity, endpoints, hosts, cloud systems, vulnerability and exposure treatment, and defensive operations.

The APP catalog contains 14 required core courses and seven genuinely optional electives. The [current APP catalog](APP/README.md) and linked course definitions publish the authoritative study sequence, prerequisites and graduation requirements; reviewed Git history preserves earlier design rationale. Learner completion records retain the course revisions under which their evidence was evaluated.

## Follow a course

1. Open a program catalog and choose a course whose listed prerequisites you satisfy.
2. Read the canonical course file for its outcomes, learning sequence, and completion requirements.
3. Complete the required work and preserve reviewable evidence of the outcomes assessed.
4. Use a learner-controlled environment or [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) to organize implementations, investigations, projects, notes, and evidence.

The curriculum describes **what must be learned and demonstrated**, not a required paid platform or book purchase. Instruction and supplementary resources may differ among independent learners, educators, and learning products.

## Understand published status

A course's `draft`, `tested`, or `verified` label describes its **educational readiness evidence**, not its specification-format version. The definitive thresholds and promotion rules belong to [Status Labels](../spec/status-labels.md).

Likewise, a file being present or passing a structural check does not establish `v0.2.0` conformance. An outline without the current outcome and assessment contract cannot count as a completed `v0.2.0` course. The [curriculum inventory](INVENTORY.md) reports which published sources meet the structural checks and which still need revision; those reports do not establish conformance.

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
