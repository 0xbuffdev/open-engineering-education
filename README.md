<!-- markdownlint-disable MD041 -->
<img width="1800" height="287" alt="open-engineering-education-banner" src="https://github.com/user-attachments/assets/a6b8c842-9a5e-47e4-ae1a-6d3fabaf1c52" />

# Open Engineering Education (OEE)

Open Engineering Education (OEE) publishes a free specification and curriculum for engineering education. Course definitions explain what learners should be able to do, how their work is assessed, and what evidence supports completion. Educators, reviewers and learning platforms can use the same published requirements.

**Current release:** `v0.2.0` (draft). OEE is evolving; its publication is not a claim that every course has been tested or verified.

## Get started

| Your goal | Start here |
| --- | --- |
| Understand the educational requirements | [Specification](spec/README.md) |
| Explore engineering programs and courses | [Curriculum](curriculum/README.md) |
| Understand assessment and evidence | [Evidence Rules](spec/evidence-rules.md) |
| Build a learner workspace | [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) |
| Propose a correction or change | [Contributing](CONTRIBUTING.md) |

## The specification

The specification defines the common requirements for courses, demonstrated learning, readiness status and conformance. The course files apply those requirements; automated checks and teaching platforms do not create additional completion rules.

| Document | What it establishes |
| --- | --- |
| [Principles](spec/principles.md) | The values behind course and assessment decisions |
| [Course Format](spec/course-format.md) | Required course structure and assessment definitions |
| [Evidence Rules](spec/evidence-rules.md) | How learning and engineering work are demonstrated |
| [Status Labels](spec/status-labels.md) | What `draft`, `tested`, and `verified` mean |
| [Conformance](spec/conformance.md) | How claims about following OEE are evaluated |

Course definitions apply these requirements to specific topics. Automated checks can identify structural problems, but do not establish assessment quality or educational conformance by themselves.

## Explore the curriculum

The curriculum is organized into five programs. Each program's README is the entry point for its published course catalog.

| Code | Program |
| --- | --- |
| [SEF](curriculum/SEF/README.md) | Software Engineering Foundations |
| [APP](curriculum/APP/README.md) | Application Engineering |
| [SYS](curriculum/SYS/README.md) | Systems Engineering |
| [AI](curriculum/AI/README.md) | AI Engineering |
| [SEC](curriculum/SEC/README.md) | Security Engineering |

A course may combine explanations, exercises, investigations, labs and project work. Completion is determined by its required learning outcomes, published assessment criteria and supporting evidence. A fixed number of lessons is never a completion standard.

Learner implementations, notes, and evidence belong in a learner-controlled workspace rather than in this specification repository.

## Independent by design

[0xBUFF](https://github.com/0xbuffdev) stewards OEE. [0xNAND](https://nand.0xbuff.com) is an optional paid learning implementation; it is not required to use the public specification or curriculum. The free [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) helps learners organize their own work.

An implementation may offer additional teaching or feedback without changing the public completion requirements. Use of an OEE-related product does not, by itself, establish conformance.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`spec/`](spec/README.md) | Authoritative educational requirements |
| [`curriculum/`](curriculum/README.md) | Program catalogs and course definitions |
| [`rfcs/`](rfcs/README.md) | Proposals and decisions explaining significant changes |
| [`tooling/`](tooling/README.md) | Optional, repository-local checking and derived exports |
| [`scripts/`](scripts/README.md) | Maintenance checks and validation utilities |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Stewardship and decision-making |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution and review instructions |

Changes to binding requirements follow [OEE governance](GOVERNANCE.md) and the [RFC process](rfcs/README.md). Accepted RFCs record decisions; the current requirements are published in `spec/`.

## Status and limitations

All five programs publish draft course definitions under OEE `v0.2.0`. AI has sixteen required courses and four electives. SEC has thirteen specialist courses and an integrated capstone, which requires separate evidence of completion for every other SEC course before admission. Each program catalog publishes the requirements and study order for this revision.

Course publication, structural checks and academic review do not establish learner-tested effectiveness, professional accreditation or OEE conformance. A course can be promoted from `draft` only when the evidence specified in [Status Labels](spec/status-labels.md) is available. The [curriculum inventory](curriculum/INVENTORY.md) reports the source files and structural checks.

The `v0.2.0` release tag contains incorrect citation metadata. The [citation erratum](releases/ERRATA.md) gives the accurate version and date information. The tag itself is unchanged.

OEE does not independently certify learners, accredit programs or guarantee employment outcomes.

## Contribute and reuse

Contributions are welcome when they improve educational clarity, technical accuracy, assessment quality, or reproducibility. Read [Contributing](CONTRIBUTING.md), the [Code of Conduct](CODE_OF_CONDUCT.md), and the [DCO policy](DCO.md) before opening a pull request.

The specification and curriculum use [CC BY 4.0](LICENSE); covered source code uses the [MIT license](LICENSE-MIT). Consult the [licensing notice](NOTICE), [Toolkit licensing boundaries](tooling/LICENSING.md), and [trademark notice](TRADEMARKS.md) for scope and attribution details.
