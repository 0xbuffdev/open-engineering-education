<!-- markdownlint-disable MD041 -->
<img width="1800" height="287" alt="open-engineering-education-banner" src="https://github.com/user-attachments/assets/a6b8c842-9a5e-47e4-ae1a-6d3fabaf1c52" />

# Open Engineering Education (OEE)

**An open specification and curriculum for engineering education grounded in demonstrable capability.**

Open Engineering Education defines what learners should be able to do, how courses make those expectations public, and what evidence supports a claim of achievement. The specification and curriculum are free to read, teach, and implement independently.

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

OEE publishes a common contract for course structure, demonstrated learning, course status, and conformance. These requirements are owned by the specification, not by a course template, a validation script, or a particular teaching platform.

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

A course may combine explanations, exercises, investigations, labs, and project work. **Completion depends on the required outcomes, public assessment criteria, and supporting evidence**, not on consuming a fixed number of lessons or repeating a universal test-and-lab sequence.

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

The `v0.2.0` draft introduces outcome-driven course requirements, but some older course definitions have not yet been migrated. Their presence in the catalog must not be mistaken for conformance with the new format. The [curriculum inventory](curriculum/INVENTORY.md) makes migration status inspectable.

The historical `v0.2.0` release tag also contains incorrect citation metadata; see the [citation erratum](releases/ERRATA.md) for accurate version and date information. The tag itself is unchanged.

OEE does not independently certify learners, accredit programs, guarantee employment outcomes, or establish that published courses have been tested or verified without the required review evidence.

## Contribute and reuse

Contributions are welcome when they improve educational clarity, technical accuracy, assessment quality, or reproducibility. Read [Contributing](CONTRIBUTING.md), the [Code of Conduct](CODE_OF_CONDUCT.md), and the [DCO policy](DCO.md) before opening a pull request.

The specification and curriculum use [CC BY 4.0](LICENSE); covered source code uses the [MIT license](LICENSE-MIT). Consult the [licensing notice](NOTICE), [Toolkit licensing boundaries](tooling/LICENSING.md), and [trademark notice](TRADEMARKS.md) for scope and attribution details.
