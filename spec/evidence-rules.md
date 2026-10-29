# Evidence Rules

This document defines the evidence required to demonstrate course completion and support claims about course readiness. It gives practical meaning to the principle of evidence over completion.

## 1. Evidence must demonstrate an outcome

An exit check is a set of requirements that a learner demonstrates at the end of a course.

Each requirement MUST be:

- **Observable:** a reviewer can see the learner perform the task, produce the result, or explain the reasoning.
- **Decidable:** the evidence and criteria allow a reviewer to distinguish an acceptable result from an unacceptable one.
- **Relevant:** the requirement directly measures a stated learning outcome.
- **Substantive:** success requires the intended capability, not merely recognition of terminology or reproduction of an unexplained answer.
- **Bounded:** the evidence identifies material assumptions, limitations, and claims it does not establish.

A course MUST state its exit requirements in advance. Those requirements MUST be specific enough that learners and reviewers can understand what successful completion entails.

## 2. Course completion requirements

A learner completes a course only when all of the course's required completion conditions have been met.

Unless a course explicitly defines a different justified assessment arrangement, completion MUST include:

1. Required conceptual checkpoints passed.
2. Required exercises completed.
3. The final lab completed.
4. Required tests and evaluations documented.
5. Relevant design decisions explained.
6. A technical retrospective written.
7. Required evidence recorded and linked.

A course MAY impose additional requirements, provided they are stated before the learner begins the assessed work.

For a project course, completion MUST also include:

- The specified project deliverables.
- A documented project evaluation against stated criteria.
- A project defense in which the learner explains the design, implementation, trade-offs, results, and limitations.

A project defense may be conducted through a live demonstration, recorded walkthrough, written technical defense, or another documented format appropriate to the course. The format MUST still allow the learner's understanding and responsibility for the work to be evaluated.

## 3. Requirements for demonstrable artifacts

An artifact used as evidence MUST meet the applicable requirements below.

### 3.1 Traceability

The evidence record MUST link to the relevant artifact or clearly identify where the artifact can be reviewed.

Where version control is used, the record SHOULD identify the relevant repository and commit.

### 3.2 Reproducibility

Where an executable result is required, the artifact MUST be reproducible from a clean checkout using documented instructions, subject to explicitly stated environment assumptions.

Instructions MUST NOT rely on undocumented files, hidden configuration, or unexplained manual steps.

### 3.3 Testing

Where code is involved, the evidence SHOULD cover the applicable normal, boundary, invalid-input, and failure cases.

The expected behavior and the observed result MUST be distinguishable.

A test result MUST NOT be presented as proof of properties the test does not establish.

### 3.4 Environment

Evidence MUST record environment details when those details materially affect the result. Depending on the work, this may include:

- Operating system and relevant hardware.
- Language, compiler, interpreter, runtime, or dependency versions.
- Relevant build flags and configuration.
- Commands used to build, run, test, or measure the artifact.
- Random seeds, repetitions, and measurement conditions where applicable.

Unnecessary environment details need not be recorded when they do not affect reproduction or interpretation.

### 3.5 Limitations

A report MUST identify material assumptions, limitations, and unresolved issues.

A benchmark or performance claim SHOULD include the measurement conditions, number of repetitions, and variability needed to interpret the result.

### 3.6 Technical retrospective

The learner MUST explain at least one meaningful incorrect assumption, failed approach, unexpected result, or design decision that changed during the work.

The retrospective MUST identify the evidence that prompted the change and explain what was learned. It MUST NOT be reduced to a generic statement that the work was difficult or successful.

## 4. Evidence that is insufficient on its own

The following do not establish course completion by themselves:

- A checked box without supporting evidence.
- A declaration that the learner understands a concept.
- A statement that an activity was completed without the required output.
- Pasted output without identifying how it was produced.
- A demonstration that only works in an unexplained local environment.
- A benchmark without sufficient information to interpret the measurement.
- A project report that omits important failures or limitations.
- A completion claim whose required evidence cannot be accessed or reviewed.

Such material may be included as context, but it MUST NOT replace the required demonstration.

## 5. Evidence records and learner privacy

Evidence records SHOULD identify the course, completion requirements, artifact locations, evaluation results, and relevant review notes.

Evidence MUST be sufficient for its intended reviewer to determine whether the requirements have been met. Access restrictions MUST be disclosed where they affect review.

Personal data, credentials, secrets, and private learner information MUST NOT be published as part of an evidence record unless publication is appropriate and authorized. Public summaries SHOULD disclose only what is necessary to substantiate the claim.

A status claim MUST NOT rely on evidence that its intended reviewer cannot reasonably inspect.

## 6. Evidence and course status

Course status is determined by evidence, not by the author's confidence or the age of the course.

| Promotion | Minimum evidence |
| --- | --- |
| `draft` to `tested` | At least one learner completes the course; completion evidence is recorded; feedback is reviewed; and a revision note explains what changed as a result. |
| `tested` to `verified` | At least two learners complete the course; the exit check and labs are reproduced or reviewed; and a qualified reviewer records sign-off. |

A status change MUST be accompanied by a record of the evidence supporting it.

If required evidence becomes unavailable, materially incorrect, or insufficient, the course status MUST be reassessed and lowered when the evidence no longer supports the published claim.

See [Status Labels](status-labels.md).

## 7. Assessment integrity

Course authors MUST define what is being assessed and what evidence is sufficient. The requirements MUST remain understandable without relying on an undocumented grading implementation.

Where automated evaluation is used, its result SHOULD be recorded alongside the relevant context. Automated results MUST NOT be represented as proving skills or properties that were not actually evaluated.

The specification defines educational and evidentiary expectations. It does not prescribe a proprietary assessment implementation.