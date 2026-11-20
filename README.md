<!-- markdownlint-disable MD041 -->
<img width="1800" height="287" alt="open-engineering-education-banner" src="https://github.com/user-attachments/assets/a6b8c842-9a5e-47e4-ae1a-6d3fabaf1c52" />

# Open Engineering Education (OEE)

Open Engineering Education publishes a free specification and curriculum for practical engineering education. Each course describes the capabilities learners are expected to develop, the work that demonstrates those capabilities, and the evidence used to assess completion.

Educators can teach the material in different ways. Learners can study independently, and tools can present the curriculum, while the published requirements remain available to everyone.

**Current specification:** `v0.2.0` (draft). Publication and automated checks do not mean a course has been tested with learners or formally verified.

## Find what you need

| I want to… | Read |
| --- | --- |
| Understand OEE requirements | [Specification](spec/README.md) |
| Browse programs and courses | [Curriculum](curriculum/README.md) |
| Understand how completion is assessed | [Evidence Rules](spec/evidence-rules.md) |
| Organize independent study | [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) |
| Correct or improve OEE | [Contributing](CONTRIBUTING.md) |

## How OEE works

The [specification](spec/README.md) defines the shared educational requirements. Its documents cover [principles](spec/principles.md), [course structure](spec/course-format.md), [evidence](spec/evidence-rules.md), [readiness labels](spec/status-labels.md), and [conformance](spec/conformance.md).

The curriculum applies those requirements to particular subjects. A course identifies its outcomes, modules, learning activities, and required assessments. Completion depends on meeting published assessment criteria with reviewable evidence. There is no required lesson count, prescribed teaching platform, or automatic credit for completing activities.

Automated checks find structural errors, missing references, and other inconsistencies. They cannot determine whether a learner has demonstrated a capability or whether a course's assessments are educationally sound.

## Programs

OEE currently contains five programs, with 65 required courses and 11 electives.

| Code | Program |
| --- | --- |
| [SEF](curriculum/SEF/README.md) | Software Engineering Foundations |
| [APP](curriculum/APP/README.md) | Application Engineering |
| [SYS](curriculum/SYS/README.md) | Systems Engineering |
| [AI](curriculum/AI/README.md) | AI Engineering |
| [SEC](curriculum/SEC/README.md) | Security Engineering |

Each program catalog lists its courses, prerequisites, and study order. Read the individual course files for the actual learning and assessment requirements. The [curriculum design guide](curriculum/DESIGN-GUIDE.md) explains how courses are researched and structured.

## Use OEE independently

[0xBUFF](https://github.com/0xbuffdev) stewards the specification. [0xNAND](https://nand.0xbuff.com) provides an optional paid learning implementation. The free [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) helps learners organize their work and evidence.

Neither product is required to follow OEE. An implementation may provide teaching, feedback, or additional tools, but it cannot silently change the public completion requirements. Using an OEE-related product does not establish conformance.

Learners keep their implementations, notes, and assessment evidence in their own workspaces, outside this specification repository.

## Repository structure

| Path | Contains |
| --- | --- |
| [`spec/`](spec/README.md) | Binding educational requirements |
| [`curriculum/`](curriculum/README.md) | Program catalogs and course definitions |
| [`examples/sef9/`](examples/sef9/README.md) | Public, synthetic assessment fixtures used by SEF9 |
| [`rfcs/`](rfcs/README.md) | Public proposals and decision records |
| [`tooling/`](tooling/README.md) | Repository-local checks and derived exports |
| [`scripts/`](scripts/README.md) | Curriculum and documentation validation |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Stewardship and the change process |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and review instructions |

Binding changes follow [governance](GOVERNANCE.md) and the [RFC process](rfcs/README.md). Accepted RFCs explain decisions; the current requirements remain in `spec/`.

## Current status

All five program catalogs publish `v0.2.0` draft course definitions. AI contains 16 required courses and four electives. SEC contains 13 specialist courses and a capstone; entry to the capstone requires separate completion evidence from the other SEC courses.

Every course remains `draft`. Source completeness and academic review do not establish learner-tested effectiveness, professional accreditation, or OEE conformance. Course status can change only with the evidence required by [Status Labels](spec/status-labels.md). The [curriculum inventory](curriculum/INVENTORY.md) explains the generated source and structure reports.

The published `v0.2.0` tag contains an error in its citation metadata. The [release erratum](releases/ERRATA.md) records the correct citation information without changing the tag.

OEE does not independently certify learners, accredit programs, or guarantee employment outcomes.

## Contribute and reuse

Read [Contributing](CONTRIBUTING.md), the [Code of Conduct](CODE_OF_CONDUCT.md), and the [DCO policy](DCO.md) before opening a pull request. Corrections to technical content, learning outcomes, assessments, and documentation are welcome.

The specification and curriculum are licensed under [CC BY 4.0](LICENSE). Covered source code uses the [MIT license](LICENSE-MIT). See [NOTICE](NOTICE), [Toolkit licensing](tooling/LICENSING.md), and [trademark guidance](TRADEMARKS.md) for the applicable boundaries.
