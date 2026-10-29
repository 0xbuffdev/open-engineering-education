# OEE Curriculum

The OEE curriculum is the canonical educational framework of Open Engineering Education (OEE). It defines five engineering programs, their courses, learning outcomes, prerequisites, assessments, practical work, and completion requirements.

The curriculum is complete and ready to use by learners, educators, mentors, curriculum authors, reviewers, and platform developers. It provides a consistent structure for independent study, organized instruction, course development, quality review, and software systems that support engineering education.

This directory is the authoritative source for the curriculum's educational content. Its structure is governed by the public OEE specification, including [Course Format](../spec/course-format.md), [Evidence Rules](../spec/evidence-rules.md), [Status Labels](../spec/status-labels.md), and [Conformance](../spec/conformance.md).

## The five engineering programs

| Code | Program | Courses | Directory |
| --- | --- | ---: | --- |
| `SEF` | Software Engineering Foundations | 10 | [SEF/](SEF/) |
| `APP` | Application Engineering | 9 | [APP/](APP/) |
| `SYS` | Systems Engineering | 9 | [SYS/](SYS/) |
| `AI` | AI Engineering | 9 | [AI/](AI/) |
| `SEC` | Security Engineering | 9 | [SEC/](SEC/) |
| **Total** | **Five engineering programs** | **46** | |

Each program has a defined course sequence and a culminating project or capstone course. Course codes provide stable identifiers for prerequisites, progression, assessment definitions, cross-course relationships, and platform integrations.

The five programs cover complementary areas of engineering while maintaining distinct learning objectives and professional capabilities.

## How to use the curriculum

### For learners

Use the curriculum to select a program, understand its sequence, satisfy prerequisites, and work toward its defined outcomes.

Each course specifies what you are expected to understand, build, test, explain, and demonstrate. Follow its completion requirements and retain evidence of your work.

Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) to organize your actual implementations, labs, exercises, projects, notes, and progress records. The curriculum defines the required work; your workspace contains the work you produce.

### For educators and mentors

Use the curriculum as a consistent foundation for teaching, mentoring, assessment, and learner progression.

Course definitions establish shared expectations for outcomes, prerequisites, practical work, and completion. Educators may adapt delivery methods to their teaching context, but material changes to canonical requirements should be documented and handled through the appropriate governance process.

When supporting learners, distinguish between completing an activity and demonstrating the capability that the activity is intended to develop.

### For curriculum and course authors

Course authors are responsible for maintaining clear, technically accurate, internally consistent, and assessable course definitions.

Every course must follow the required OEE structure and specify:

- **Purpose and learning outcomes:** the professional capability being developed and what learners must demonstrate.
- **Prerequisites:** the prior knowledge and course requirements needed to proceed.
- **Course structure:** the ordered modules and lessons.
- **Assessments:** the intended outcomes and criteria for evaluating them.
- **Labs and exercises:** the practical work required to develop and demonstrate capability.
- **Completion requirements:** the conditions that must be satisfied to complete the course.
- **Evidence and retrospective:** the artifacts and explanations needed to support completion and document learning from experience.

Authors must follow [Course Format](../spec/course-format.md). Course definitions must remain consistent with the governing specification and must not introduce conflicting requirements or unsupported completion claims.

### For reviewers and maintainers

Review course changes for technical correctness, educational clarity, prerequisite consistency, valid identifiers, working links, and alignment with OEE requirements.

Changes should preserve consistency across the affected course files, program structure, and shared specification.

The status of a course must reflect the evidence available for its validation. Curriculum completeness does not automatically establish that every course has been tested or verified with learners.

Routine corrections may proceed through a pull request. Changes to normative requirements must follow the [RFC process](../rfcs/README.md).

### For platform developers

The OEE curriculum is canonical content that platforms may display, organize, and use to support learning workflows.

Platform implementations should preserve course identifiers, titles, prerequisites, program relationships, learning outcomes, assessment definitions, and completion requirements.

A platform may provide additional capabilities, including progress tracking, assessment workflows, analytics, or instructor tools. Such capabilities must remain distinguishable from the requirements defined by the curriculum and specification.

An interface's completion indicator does not replace the evidence required to establish course completion. Similarly, implementing curriculum features does not automatically establish conformance to OEE.

Consult [Conformance](../spec/conformance.md) when evaluating whether a course, program, or implementation satisfies the applicable requirements.

## Course structure

Every course follows the common OEE course format. The specification establishes the shared structure, while each course defines its subject-specific content and expectations.

Course definitions cover:

- The capability the course develops.
- Learning outcomes and prerequisites.
- The sequence of modules and lessons.
- Assessments and practical investigations.
- Required exercises and substantial lab work.
- Completion conditions and evidence to retain.
- Common failure modes and technical retrospectives.

Project-based courses additionally define their deliverables, evaluation criteria, and project defense.

The individual course file is the authoritative definition of that course's requirements. Program summaries, external interfaces, and platform representations should remain consistent with it.

## Course status and validation

The curriculum is complete and available for use. Individual course status labels describe the evidence supporting course validation and readiness.

| Status | Meaning |
| --- | --- |
| `draft` | The course is written but does not yet meet the evidence requirements for `tested`. |
| `tested` | At least one learner has completed the course, recorded feedback has informed a revision, and the required evidence is documented. |
| `verified` | At least two learners have completed the course, the exit check and labs have been reproduced or reviewed, and a qualified reviewer has signed off. |

New courses begin as `draft`. Promotion requires the evidence specified by [Status Labels](../spec/status-labels.md) and [Evidence Rules](../spec/evidence-rules.md).

These labels measure the evidence supporting course validation. They do not indicate whether the curriculum directory is complete, nor do they represent course difficulty, accreditation, or guaranteed learner outcomes.

## Completion and evidence

Course completion is determined by the requirements stated in the individual course definition and the applicable OEE specification.

Depending on the course, completion may require conceptual checkpoints, exercises, tests or evaluations, substantial lab work, explained design decisions, and a technical retrospective.

Where executable artifacts are required, the evidence must support reproduction and review. It should establish what was done, how the result was obtained, whether the stated outcomes were demonstrated, and what limitations remain.

Project-based courses also require their specified deliverables, project evaluation, and defense.

Completion must not be inferred solely from attendance, elapsed time, activity completion, or an unsupported declaration of success.

## Curriculum maintenance and change control

The curriculum is maintained as a coherent system. A change to one course may affect prerequisites, progression, assessments, program summaries, and platform integrations.

Contributors should:

1. Identify the problem or improvement being addressed.
2. Check the effect on related courses and program relationships.
3. Follow the required course format and applicable specification.
4. Validate identifiers, cross-references, and internal links.
5. Document significant changes and necessary transition steps.
6. Update affected summaries and metadata so they agree with the canonical course definitions.

Changes to normative OEE requirements must follow the RFC process. Curriculum changes must not silently introduce requirements that contradict the specification.

The governance process preserves a consistent standard while allowing the curriculum to improve through documented, reviewable changes.

## Repository structure

```text
curriculum/
  README.md    Curriculum overview and maintenance guidance
  SEF/         Software Engineering Foundations
  APP/         Application Engineering
  SYS/         Systems Engineering
  AI/          AI Engineering
  SEC/         Security Engineering
```

The `spec/` directory contains the governing OEE specification. The program directories contain the canonical course definitions for the five engineering programs.

Practical learner work and progress records belong in [OEE Workspace](https://github.com/0xbuffdev/oee-workspace), which provides the structure and tools for organizing implementations, exercises, labs, projects, notes, and evidence.

## Guiding principle

The OEE curriculum provides one consistent educational framework for multiple audiences:

- Learners use it to develop and demonstrate engineering capability.
- Educators and mentors use it to guide instruction, practice, and assessment.
- Course authors use it to define clear, assessable learning requirements.
- Reviewers and maintainers use it to preserve quality and consistency.
- Platform developers use it to build systems that represent and support the curriculum.

The objective is a complete, practical, and maintainable engineering curriculum whose requirements are explicit, whose changes are traceable, and whose claims about course readiness and learner achievement are supported by evidence.
