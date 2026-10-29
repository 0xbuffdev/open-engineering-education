# Course Format

This document defines the required structure for an OEE course file. The format is intended to make each course understandable, reviewable, and usable without relying on undocumented expectations.

## 1. Required metadata

Every course MUST begin with the following metadata. The course code and program are optional: use the title-only heading when no code is assigned, and omit the Program line when the course does not belong to a program.

```markdown
# <CODE> — <Course Title>
# <Course Title>

**Program:** <program code and name>
**Type:** `course` or `project`
**Prerequisites:** <course codes or `none`>
**Duration:** <number of weeks or stated range>
**Status:** `draft`
````

Requirements:

- If a course code is stated, it MUST be unique within the OEE curriculum.
- The title MUST identify the course clearly.
- If a program is stated, the program code MUST match the program to which the course belongs.
- The type MUST be `course` or `project`.
- Prerequisites MUST identify specific course codes or state `none`.
- Duration MUST be stated in weeks. When the course belongs to a program, duration MUST agree with the program catalogue.
- Every new or unproven course MUST start with the `draft` status.
- Status requirements are defined in [Status Labels](status-labels.md).

A project course is an advanced, integrated project or capstone. It MUST include the additional deliverables and evaluation requirements defined in [Evidence Rules](evidence-rules.md).

## 2. Required sections

Every course MUST contain the following sections. A course may use additional sections where they improve clarity, but additional sections MUST NOT replace the required ones.

| #  | Section                 | Requirements                                                                                                    |
| -- | ----------------------- | --------------------------------------------------------------------------------------------------------------- |
| 1  | Purpose                 | Explain the capability the course is intended to develop and why it matters in engineering practice.            |
| 2  | Learning Outcomes       | State observable outcomes that can be demonstrated and evaluated.                                               |
| 3  | Prerequisites           | Identify prior knowledge or course requirements and state what a learner should already be able to demonstrate. |
| 4  | Course Structure        | Organize the course into ordered modules and identify their learning objectives.                                |
| 5  | Lessons                 | Explain concepts, mechanisms, constraints, and examples needed to reach the outcomes.                           |
| 6  | Assessments             | Identify conceptual checkpoints, tests, or other evaluations and the outcomes they measure.                     |
| 7  | Labs                    | Define practical work that produces inspectable evidence of learning.                                           |
| 8  | Required Exercises      | Identify exercises that the learner must complete.                                                              |
| 9  | Completion Requirements | State the conditions that must be met to complete the course.                                                   |
| 10 | Common Failure Modes    | Identify likely misconceptions, implementation errors, and debugging challenges.                                |
| 11 | Evidence to Retain      | Identify the artifacts and records needed to support the completion claim.                                      |
| 12 | Technical Retrospective | Require the learner to explain a wrong assumption, the evidence that challenged it, and the resulting change.   |

The course MUST link to relevant prerequisite courses by their current identifiers. Internal links MUST resolve.

## 3. Course and lesson types

A course MUST identify its type as either `course` or `project`.

Lesson entries MUST use one of the following kinds:

| Kind     | Purpose                                                         |
| -------- | --------------------------------------------------------------- |
| `lesson` | Explains concepts, mechanisms, design decisions, or techniques. |
| `test`   | Evaluates specified learning outcomes.                          |
| `lab`    | Requires practical work and produces inspectable evidence.      |

A lesson file or entry MUST identify its kind consistently. A course MUST NOT use an undefined kind to represent required assessed work.

## 4. Module ordering

Modules MUST have a clear learning sequence. Each module MUST identify its intended outcomes and its required lesson entries.

Where a module includes both a test and a micro-lab, the order MUST be:

1. Instructional lessons.
2. Test.
3. Micro-lab.

In that arrangement, the test MUST be the second-to-last lesson entry and the micro-lab MUST be the final entry in the module.

A module without a micro-lab MAY still include a test. Any assessment used in a module MUST have a clear purpose and identify the outcomes it measures. A test MUST NOT be appended to the end of a module merely to fill the final position.

Every course MUST end with a lab module. The final lesson entry in that module MUST be a lab that demonstrates practical integration of the course's intended outcomes.

## 5. Assessment requirements

Each assessment MUST identify the learning outcomes it evaluates and make the success criteria clear enough for a learner and reviewer to understand.

Where a test uses typed questions, the supported question types are:

| Type         | Intended use                                |
| ------------ | ------------------------------------------- |
| `single`     | Select one answer.                          |
| `multi`      | Select more than one answer.                |
| `free`       | Provide a free-form written answer.         |
| `math`       | Express or calculate a mathematical result. |
| `code`       | Produce, complete, or analyze code.         |

A course MAY use only the question types appropriate to its outcomes. Listing a question type does not require every course to use it.

Assessment instructions MUST state what the learner is expected to demonstrate. Course files MUST describe the educational requirement rather than depend on an undocumented implementation detail.

## 6. Lab requirements

Every required lab MUST specify:

- Objective: the question, capability, or behavior being investigated.
- Prerequisites: concepts, tools, and prior work needed to begin.
- Environment: relevant operating system, dependencies, versions, and configuration.
- Procedure: the work the learner is expected to perform.
- Expected result: the observable behavior or artifact to produce.
- Verification: how the learner or reviewer determines whether the result is correct.
- Evidence: the files, output, measurements, tests, or explanations to retain.
- Failure analysis: relevant failure cases and what the learner should learn from them.

A lab MUST require meaningful work. Copying a provided result without producing or explaining it MUST NOT satisfy a lab's completion criteria.

## 7. Course completion

The course MUST state completion requirements before the learner reaches the final assessment.

These requirements MUST align with [Evidence Rules](./evidence-rules.md). They MUST identify all required checkpoints, exercises, labs, evaluations, explanations, and retrospective work.

For a project course, the completion requirements MUST additionally identify the required deliverables, project evaluation, and defense.

Completion MUST NOT depend solely on reading, attendance, elapsed time, or an unsubstantiated declaration of success.

## 8. Evidence and reproducibility

Course instructions MUST identify the evidence needed to demonstrate completion.

Where code or an executable artifact is required, the course SHOULD specify how to run and verify it from a clean checkout. Relevant environment details, test commands, expected behavior, and known limitations MUST be documented.

Learner work belongs in the learner's own workspace. The course file defines the assignment and expected evidence; it does not serve as the learner's personal progress record.

See [Evidence Rules](./evidence-rules.md).

## 9. Links and consistency

All relative internal links MUST resolve.

Where stated, course identifiers, titles, program assignments, prerequisites, durations, and status labels MUST agree with the corresponding program catalogue and course metadata.

A change that updates only one location while leaving conflicting information elsewhere is incomplete.

## 10. Changes to the format

Changes to required metadata, lesson kinds, module ordering, assessment types, or completion requirements affect the normative course format. Such changes MUST be proposed through the RFC process.

Course authors MUST NOT introduce a conflicting structure and treat it as conforming by default.
