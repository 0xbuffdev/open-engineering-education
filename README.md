# Open Engineering Education (OEE)

**An open specification for engineering education built around demonstrable capability.**

Open Engineering Education (OEE) defines how engineering courses are structured, how learning is demonstrated, and how claims about course readiness are supported by evidence. It combines a public specification with a curriculum designed to follow that specification.

OEE emphasizes underlying mechanisms, practical engineering work, reproducible results, and transparent claims about what learners can demonstrate.

**Project status:** `v0.0.1` — draft. The specification is evolving and is not a finalized standard. Course status labels describe the evidence available for each course.

- **Steward:** [0xBUFF](https://github.com/0xbuffdev)
- **Author:** Christopher S. Aondona
- **Licensing:** [CC BY 4.0](LICENSE) for specification and curriculum text; [MIT](LICENSE-MIT) for code and scripts.

## What OEE defines

OEE establishes:

- **Principles:** the expectations that govern the specification and its curriculum.
- **Course format:** the required structure and metadata for course definitions.
- **Evidence rules:** what counts as demonstrated learning and completed engineering work.
- **Status labels:** the evidence required to describe a course as `draft`, `tested`, or `verified`.
- **Conformance:** the requirements for evaluating whether a course, program, or implementation follows the specification.
- **Governance:** how the specification evolves and how significant changes are proposed and reviewed.

Start with the [specification overview](spec/README.md).

## The five programs

The OEE curriculum is organized into five engineering programs:

| Code | Program |
| --- | --- |
| `SEF` | Software Engineering Foundations |
| `APP` | Application Engineering |
| `SYS` | Systems Engineering |
| `AI` | AI Engineering |
| `SEC` | Security Engineering |

The [curriculum directory](curriculum/) contains the program definitions and their course structures.

## Core principles

### 1. Evidence over completion

A course is complete when its required outcomes are demonstrated and its required work is supported by appropriate evidence. Time spent, material consumed, and unchecked claims are not substitutes for demonstrated capability.

### 2. Mechanism before tooling

Learners should understand the underlying mechanisms before relying on abstractions, frameworks, or managed services. Engineering decisions must be explainable rather than based solely on familiarity with an interface.

### 3. Honest claims

Course status, assessment results, benchmarks, and project outcomes must state what the evidence supports and what it does not establish. No course should be described as tested or verified without meeting the corresponding requirements.

### 4. Open by default

The public specification and curriculum are published under their declared licenses. Optional commercial products may provide additional services, but they do not change the requirements of the public specification.

Read the full [principles](spec/principles.md).

## OEE, 0xBUFF, and 0xNAND

**0xBUFF** stewards OEE and oversees the development of its public specification.

**[0xNAND](https://nand.0xbuff.com)** is the paid reference implementation developed under 0xBUFF. It may implement OEE concepts and provide additional tooling or services, but using 0xNAND is not required to study, teach, or implement OEE.

The public specification remains distinct from any individual implementation. Product features, commercial arrangements, and implementation choices do not change the specification unless the relevant change is formally adopted through the OEE governance process.

An implementation's relationship to OEE does not, by itself, establish that it conforms to the specification.

## Learning and evidence

OEE distinguishes between completing activities and demonstrating engineering capability.

Depending on the course, completion may require conceptual checkpoints, implementation exercises, practical labs, tests or evaluations, explained design decisions, and a technical retrospective. Project-based courses also require their specified deliverables and evaluation.

Evidence should make it possible for a reviewer to understand what was done, how the result was produced, whether it can be reproduced, and what limitations remain.

Read [Evidence Rules](spec/evidence-rules.md) and [Status Labels](spec/status-labels.md).

## Learner workspaces

Learner work belongs in a workspace controlled by the learner, not in the OEE specification repository.

OEE provides a public workspace for individual learners and groups to use: [oee-workspace](https://github.com/0xbuffdev/oee-workspace).

The OEE repository may also provide templates and scripts to help learners set up their workspaces. Learners should keep their exercises, experiments, project implementations, notes, and evidence logs in their own workspace. Only changes intended for the public OEE repository should be committed to that repository.

Never commit credentials, secrets, private learner data, or unrelated personal material.

## Repository structure

| Path | Purpose |
| --- | --- |
| `spec/` | Normative documents that define OEE |
| `curriculum/` | Programs and course definitions |
| `templates/` | Templates for learner work and project documentation |
| `scripts/` | Utilities that support local workflows and repository checks |
| `governance/` | Contribution policy, conduct, and decision-making |
| `rfcs/` | Proposals for significant changes to the specification |
| `.github/` | Repository automation and contribution templates |

The specification defines the common requirements. Curriculum files apply those requirements to particular programs and courses. Templates, scripts, and implementations may support the process, but must not silently redefine the specification.

## Contributing

Contributions should improve clarity, correctness, reproducibility, or consistency with the specification.

Before submitting a change:

1. Read the [principles](spec/principles.md).
2. Review the [contribution guidelines](governance/CONTRIBUTING.md).
3. Search existing issues and [RFCs](rfcs/README.md).
4. Follow the repository's sign-off, review, and validation requirements.

Changes to normative requirements should be proposed through the RFC process rather than introduced indirectly through a course or implementation.

## Licensing

Specification and curriculum text are licensed under [Creative Commons Attribution 4.0 International](LICENSE). Code and scripts covered by the repository's software license are licensed under the [MIT License](LICENSE-MIT).

Contributors must have the rights needed to submit their work under the applicable license. See the repository's contribution and attribution documents for additional details.

## Current limitations

OEE is a draft specification. Its requirements may change through the documented governance process.

A published course, program, or implementation must not be described as `verified`, conforming, accredited, or certified unless the applicable criteria and documented review support that claim. OEE does not, by itself, guarantee employment outcomes, professional accreditation, or mastery of every subject associated with a course.