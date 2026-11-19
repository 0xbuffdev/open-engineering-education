# OEE Curriculum

OEE publishes course definitions for five engineering programs. Each program catalog lists its courses, prerequisites and completion requirements. Learners, educators and reviewers can use the same public criteria without a required teaching platform.

These catalogs contain 65 required courses and 11 electives. AI has sixteen required courses, including its capstone, and four optional electives. All twenty AI courses remain `draft`. SEC has thirteen specialist courses and a capstone, each with `v0.2.0` outcomes and summative evidence requirements. All fourteen SEC courses also remain `draft`. Published source structure is checked automatically; course readiness requires the learner and reviewer evidence described in the specification.

## Choose a program

Each program README is the authoritative catalog for its **current** courses, study order, classification, and prerequisites.

| Code | Program | Course files in this revision | Catalog |
| --- | --- | --- | --- |
| `SEF` | Software Engineering Foundations | 11 core | [Explore SEF](SEF/README.md) |
| `APP` | Application Engineering | 14 core, 7 electives | [Explore APP](APP/README.md) |
| `SYS` | Systems Engineering | 10 core | [Explore SYS](SYS/README.md) |
| `AI` | AI Engineering | 16 core, 4 electives | [Explore AI](AI/README.md) |
| `SEC` | Security Engineering | 14 core | [Explore SEC](SEC/README.md) |
| **Total** | **Five programs** | **65 core, 11 electives** | |

SEF develops programming and mathematical foundations. Its [SEF11 discrete mathematics](SEF/SEF11.md) course precedes later algorithm and numerical work; the [SEF10 capstone](SEF/SEF10.md) checks evidence from the other foundation courses. APP builds on these foundations to develop and operate applications. SYS studies machine-level behavior, Rust, operating systems, concurrent services, storage and distributed systems. AI develops data, models, evaluation and deployed AI systems. SEC covers application and native-code security, infrastructure, identity, incident response, exposure management, security architecture and data privacy.

APP has fourteen required courses and seven optional electives. AI has sixteen required courses and four optional electives. SEC graduation requires evidence from every specialist course before its capstone. The linked program catalogs provide study order and prerequisites; each course file describes the assessed work. Reviewers record the revision under which a learner's evidence was evaluated.

## Follow a course

1. Open a program catalog and choose a course whose listed prerequisites you satisfy.
2. Read the canonical course file for its outcomes, learning sequence, and completion requirements.
3. Complete the required work and preserve reviewable evidence of the outcomes assessed.
4. Use a learner-controlled environment or [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) to organize implementations, investigations, projects, notes, and evidence.

The curriculum describes **what must be learned and demonstrated**, not a required paid platform or book purchase. Instruction and supplementary resources may differ among independent learners, educators, and learning products.

## Understand published status

A course's `draft`, `tested`, or `verified` label describes its **educational readiness evidence**, not its specification-format version. The definitive thresholds and promotion rules belong to [Status Labels](../spec/status-labels.md).

A course file or passing structural check does not establish `v0.2.0` conformance. The [curriculum inventory](INVENTORY.md) provides reproducible, commit-pinned source-format and structure reports; educational readiness follows independent review evidence.

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
