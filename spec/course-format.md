# Course Format

This document defines the required structure for an Open Engineering Education (OEE) course. A course identifies the capabilities learners must demonstrate and the requirements for assessing them. A product may provide more extensive teaching material, but independent learners MUST be able to understand the public curriculum's requirements without a commercial platform or paid book.

## 1. Metadata

A course MUST begin with one level-one heading containing its title and, where assigned, its unique code. The following metadata MUST follow the heading:

```markdown
# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 4 weeks
**Status:** `draft`
```

The `Program` line MAY be omitted for a standalone course. The assigned code and program MUST agree with the curriculum catalog. The `Type` MUST be `course` or `project`. Prerequisites MUST identify stable course codes, with links to existing prerequisite files where applicable, or be stated as `none`. An unambiguous range MAY describe multiple prerequisites. Duration MUST be expressed in weeks and agree with the program catalog. New and unproven courses MUST begin in `draft` status; promotion follows [Status Labels](status-labels.md) and [Evidence Rules](evidence-rules.md). Optional workload estimates MAY be included.

A repeated `Course brief` metadata block containing Introduction, History, Usage, Applications, Strengths, Limitations, and Key Concepts is not required. Pertinent background belongs in the Overview or the appropriate instructional lesson.

## 2. Required course sections

Every course MUST contain these four top-level sections, in order:

| Section | Required content |
| --- | --- |
| **Overview** | Purpose, scope, practical relevance, and any additional entry-readiness explanation |
| **Learning outcomes** | Observable capabilities that can be evaluated |
| **Modules** | An ordered module sequence with module outcomes and typed lesson entries |
| **Completion requirements** | Required exercises, tests, labs, deliverables, evaluations, evidence, explanations, and retrospective |

These are the only mandatory top-level headings. Additional sections MAY be used where useful, but authors SHOULD NOT repeat the same information under multiple headings. Separate Course brief, Topics, Prerequisites, Course Structure, Lessons, Assessments, Labs, Required Exercises, Common Failure Modes, Evidence to Retain, and Technical Retrospective headings are not mandatory.

**Simplifying headings MUST NOT remove the underlying educational requirements.** The course or its publicly linked briefs MUST still disclose all required practical work, success criteria, evidence, failure analysis, and completion conditions. A proprietary implementation MUST NOT be the sole source of these requirements.

## 3. Modules and lesson kinds

Every module MUST have a sequential position and descriptive title, followed by exactly two core subsections:

- **Outcomes:** observable module-level capabilities.
- **Lessons:** ordered and explicitly typed entries describing what is taught, tested, or practiced.

A `Module brief` with repeated Introduction, Overview, History, Applications, Strengths, Limitations, or Key Concepts fields is not required. Background that materially contributes to understanding SHOULD be presented in the relevant lesson. The first lesson of the first module SHOULD orient the learner to the course; there is no requirement to add an otherwise redundant introduction lesson.

A lesson entry MUST use one of the following kinds:

| Kind | Purpose |
| --- | --- |
| `lesson` | Teach concepts, mechanisms, decisions, or techniques |
| `test` | Assess identified learning outcomes |
| `lab` | Require practical work that yields inspectable evidence |

For example:

```markdown
### Module 1 — Inside the Machine

#### Outcomes

- Explain and model binary states, bits, and bytes.

#### Lessons

1. **Course orientation** — `lesson`
2. **Bits and two-state systems** — `lesson`
3. **Understanding bits and bytes** — `test`
4. **Model a byte** — `lab`
```

This is a course navigation and assessment contract, not a mandate to publish a complete lecture script. A public course MUST nevertheless include or link to any instructions necessary for learners to complete its required activities.

## 4. Learning sequence and final lab

Modules MUST follow a coherent learning sequence. Where instructional lessons, a conceptual test, and a micro-lab occur in the same module, the normal order SHOULD be `lesson` → `test` → `lab`, with the test preceding the practical work it prepares the learner to perform. Tests MUST NOT be added solely to satisfy a positional convention.

A module MAY omit tests or micro-labs when the outcomes and overall assessment design justify this. Each included assessment MUST have a clear purpose.

Every course, including a project course, MUST culminate in a final integration `lab`: the final lesson entry of the final module MUST be of kind `lab` and demonstrate integration of the intended course outcomes. **The final module does not need to be a separate lab-only module.** A lab-only module MAY be retained when it makes educational sense.

## 5. Assessment and exercise requirements

Each required assessment MUST identify the outcomes evaluated, the work expected, and success criteria sufficient for a learner and reviewer to distinguish acceptable from unacceptable results. Required and optional exercises MUST be distinguished.

Where typed questions are used, supported question types are:

| Type | Intended use |
| --- | --- |
| `single` | Select one answer |
| `multi` | Select multiple answers |
| `free` | Provide a written explanation |
| `math` | Express or compute a mathematical result |
| `code` | Produce, complete, or analyze code |

Implementations MAY use additional presentation or evaluation mechanisms, but they MUST preserve the public assessment requirements. Assessment criteria MAY be placed near the typed `test` entry, under Completion requirements, or in a linked public assessment brief.

## 6. Lab requirements

Every required `lab` MUST provide, within the course or in a publicly accessible linked brief:

- Objective: the capability or behavior to investigate.
- Prerequisites: relevant concepts, tools, and prior work.
- Environment: relevant platform, dependencies, versions, and configuration when material.
- Procedure: work the learner must perform.
- Expected result: observable behavior or artifact.
- Verification: how correctness will be determined.
- Evidence: files, output, tests, measurements, and explanations to retain.
- Failure analysis: expected difficulties and the learning they reveal.

A concise lab MAY include these instructions directly under its lesson entry. A substantial lab MAY link to a separate public brief. No generic `requirements/` directory is required. Copying a result without producing or explaining it MUST NOT establish completion.

## 7. Completion, evidence, and reproducibility

Completion requirements MUST be clear before the learner undertakes the final assessment. They MUST identify required conceptual checkpoints, exercises, evaluated work, the final integration lab, design explanations, reproducibility instructions where applicable, a meaningful technical retrospective, and the evidence required under [Evidence Rules](evidence-rules.md).

For executable artifacts, applicable build and verification instructions, environment assumptions, expected behavior, and known limitations MUST be documented sufficiently to reproduce and interpret the result. Learner artifacts belong in the learner's workspace or another appropriate record, not in the public course definition.

A `project` course MUST additionally identify required deliverables, evaluation against criteria, and a project defense. Reading, attendance, elapsed time, or an unsupported claim of success cannot alone satisfy completion.

## 8. Consistency and independence

Course codes, titles, prerequisites, program assignments, duration, type, and status MUST agree with the corresponding program catalog. Relative internal links MUST resolve.

OEE MUST NOT depend on particular books, affiliate purchases, proprietary educational platforms, or commercial subscriptions for the public requirements. Implementations MAY offer guided instruction and feedback without changing the underlying requirements.

Passing a structural validation script does not establish course conformance or justify `tested` or `verified` status.

## 9. Changes to the format

This initial v0.0.1 baseline is being established under the narrowly scoped [bootstrap procedure](../GOVERNANCE.md). Once the first stabilization pull request is merged, subsequent changes to normative requirements MUST follow the [RFC process](../rfcs/README.md), except for corrections with no change in normative meaning.

Curriculum authors and implementations MUST NOT silently introduce conflicting requirements or represent unassessed material as conforming.
