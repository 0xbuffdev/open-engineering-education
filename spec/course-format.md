# Course Format

This document defines the public educational contract for an Open Engineering Education
(OEE) course. A course describes observable capabilities, a coherent learning sequence,
and how completion is evaluated. Instructional delivery may differ among independent
study, OEE Workspace, 0xNAND, and other implementations. Learners MUST be able to
understand the public course requirements without purchasing materials or using a
commercial platform.

This revision implements [RFC 0001](../rfcs/0001-outcome-driven-curriculum.md).
The outcome and assessment model below applies to courses authored or migrated against
the revised specification; earlier published course revisions remain attributable to
the specification version under which they were authored.

## 1. Metadata

A course MUST begin with a level-one heading containing its title and, where assigned,
its unique course code. Required metadata follows the heading:

```markdown
# SEF1 — Demystifying the Computer System

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** none
**Duration:** 5 weeks
**Status:** `draft`
```

The `Program` line MAY be omitted for standalone courses. The assigned code,
program, type, prerequisites, duration, and status MUST agree with the authoritative
program catalog. `Type` MUST be `course` or `project`. Prerequisites MUST use
stable course codes, with links where applicable, or `none`. An unambiguous range
MAY express multiple prerequisite courses. Duration MUST be stated in weeks; it is
an estimate, not proof of competence. Optional workload estimates MAY be included.
New, unproven courses MUST begin as `draft`; promotion follows
[Status Labels](status-labels.md).

History, introductions, applications, strengths, limitations, and other explanatory
material belong in the relevant overview or instructional lesson, not in repetitive
mandatory metadata blocks.

## 2. Required course sections

Every course MUST contain these four top-level sections, in order:

| Section | Purpose |
| --- | --- |
| **Overview** | Purpose, scope, relevance, and entry-readiness information |
| **Learning outcomes** | Observable course capabilities, with stable IDs |
| **Modules** | Ordered instructional modules, their outcomes, and learning sequences |
| **Completion requirements** | Required summative assessments, outcome coverage, success criteria, and evidence |

Other headings MAY appear when useful. Authors SHOULD avoid duplicating assessment
requirements across sections or separate files. A linked public assessment brief
MAY carry the details for a substantial evaluation, but MUST be explicitly
referenced from the course.

A proprietary service, paid book, or private grading system MUST NOT be the only
place where learners can discover mandatory outcomes and acceptance criteria.

## 3. Outcomes and stable identifiers

Every required course outcome MUST describe an observable capability that can be
evaluated. Each outcome in a course authored or migrated against this specification
MUST have a stable identifier, such as `APP1-O1`. Required summative assessments MUST
have stable identifiers, such as `APP1-AS1`.

Identifiers MUST be unique within their course and MUST remain stable through
editorial revisions. If a requirement is materially replaced rather than clarified,
the author SHOULD assign a new identifier and document the relationship to its
predecessor. An identifier is not evidence that the outcome has been demonstrated.

A module MUST identify its relevant outcomes, using course outcome IDs where
appropriate or describing additional module-level learning objectives. The course
MUST preserve traceability from required outcomes to the assessments that establish
them. A single assessment MAY cover several outcomes; several assessments MAY
contribute evidence to one outcome.

Module and lesson identifiers MAY be introduced when useful. They are not globally
required by this version of the specification. A machine-readable serialization,
manifest, and API are likewise not prescribed.

## 4. Modules and learning activities

Modules MUST have a coherent order, descriptive titles, outcomes, and an ordered
learning sequence. The recommended basic structure is:

```markdown
### Module 1 — How Web Requests Work

#### Outcomes
- APP1-O1

#### Lessons
1. Client and server communication
2. Addressing and name resolution
3. Optional investigation: inspect a supplied browser trace
```

The `Lessons` heading MAY include conceptual instruction, demonstrations,
examples, guided exercises, simulations, investigations, labs, formative checks,
or project milestones. Activities MAY be labeled by kind for navigation, but
OEE does not mandate a closed set of `lesson`, `test`, and `lab` kinds.

A module MAY contain no test or no lab. No fixed activity count or
`lesson → test → lab` ordering is required. Activities SHOULD be selected
because they serve the module outcomes and prepare learners for the required
summative evaluations, not to fill a template.

Required activities MUST be distinguished from optional practice. A formative
exercise or self-check MUST NOT silently become a course completion condition.
Instructional activities are not necessarily separate assessed submissions.

## 5. Assessment design and outcome coverage

A **formative check** supplies feedback for learning; it does not independently
establish completion unless the course explicitly designates the resulting
performance as required assessment evidence.

A **summative assessment** evaluates specified outcomes against publicly
understandable criteria. A **lab** is a practical activity format, not a
mandatory assessment stage; a lab may be formative, summative, or both at
different stages. Automated tests of software behavior are distinct from
knowledge tests of the learner.

Every course MUST identify sufficient required summative evaluation to support
completion of all required course outcomes. Every required summative assessment MUST
identify:

- A stable assessment ID.
- The required course outcome IDs it evaluates.
- The work or performance expected of the learner.
- Published success or acceptance criteria.
- The evidence a learner must provide or make reviewable.
- Any relevant environment constraints, evaluation method, or safety boundaries.

An author MUST evaluate whether an assessment actually demonstrates its claimed
outcomes; linking IDs without a defensible evaluation is insufficient. Where
multiple evaluations jointly establish one outcome, their combined required
evidence MUST be explicit.

Assessment requirements MAY appear within the module, under Completion requirements,
or in a publicly accessible linked brief, with one clear authoritative definition.
Implementations MAY provide additional practice, variants, feedback mechanisms,
and evaluation tools, but MUST preserve the published OEE competency expectations
when asserting completion against the same course revision.

There is no universal requirement for one final `lab`, a single capstone exercise
in every course, or an integrated demonstration at a fixed position. Authors SHOULD
use integration tasks when the outcomes call for combined application; cumulative
assessment evidence MAY be sufficient when it validly demonstrates all outcomes.

## 6. Practical work and labs

Practical activities SHOULD be used wherever they meaningfully develop or verify
an engineering capability. Small exercises MAY be concise and self-checked.

A *required substantial lab* MUST disclose enough information, directly or in a
publicly linked brief, to identify its objective, task or constraints, expected
behavior or deliverable, verification and evaluation method, required evidence,
and any safety boundaries. Prerequisites, environment requirements, procedures,
failure analysis, and limitations MUST be supplied when materially necessary
to complete, reproduce, or interpret the work. An author MUST NOT require
unnecessary documentation solely to satisfy a uniform lab template.

For executable assessed artifacts, reproducibility requirements in
[Evidence Rules](evidence-rules.md) apply. Copying a result or presenting a
green test alone MUST NOT establish capabilities that the evidence does not test.

## 7. Project courses and continuous work

A `project` course MUST specify the coherent project problem or permissible
problem space, mandatory deliverables, evaluation criteria, applicable milestones,
and a technical defense of the learner's own work. A project SHOULD progress
cumulatively through scope, design, implementation, validation, and review,
rather than requiring artificial independent module labs.

Milestones MAY be formative reviews or summative evidence as explicitly stated.
A defense MAY be live, recorded, written, or another reviewable format appropriate
to the outcomes, but it MUST permit evaluation of the learner's understanding,
decisions, results, and limitations.

Project courses are not required to end with a lesson typed `lab`.
They remain subject to the same outcome coverage and evidence requirements as
other courses, plus their published project deliverables and defense.

## 8. Completion and independence

The Completion requirements section MUST state the required summative assessments,
how they establish every required outcome, and what evidence is needed for completion.
It MUST distinguish mandatory work from optional practice and make expectations
available before the learner undertakes assessed work.

A course is completed only when the required outcomes are demonstrated against the
published criteria and the evidence requirements in
[Evidence Rules](evidence-rules.md) are met. Attendance, elapsed time, passive
content consumption, or unchecked activity markers cannot establish completion.

Where an implementation uses an unseen variant or private item bank, it MUST
evaluate equivalent outcomes and criteria. Public required work and evaluation
standards MUST remain understandable and independently usable without a
commercial account. OEE does not require public disclosure of every exact exam
item, private grading rule, answer key, or reusable challenge seed.

## 9. Consistency, transition, and conformance

Course IDs, program relationships, prerequisites, titles, durations, type, and
status MUST agree with the relevant catalog. Internal links MUST resolve.

This revision changes the authoring contract. Existing course revisions and
historical learner evidence MUST remain identifiable by their original
specification/course revision. New or migrated courses claiming conformance to
the revised specification MUST meet its stable-ID, outcome-coverage, assessment,
and evidence requirements. Legacy files MUST NOT be described as conforming to
the revised requirements merely because they existed before migration.

Course migration SHOULD retain useful learning activities while deciding which
ones genuinely need summative evidence. Changes to competency expectations or
evaluation criteria MUST be documented for downstream consumers and learners.

Structural linting does not establish pedagogical validity, course status, or
conformance. See [Conformance](conformance.md).

## 10. Governance

Changes to normative requirements MUST follow the
[RFC process](../rfcs/README.md). This revision implements
[accepted RFC 0001](../rfcs/0001-outcome-driven-curriculum.md).
Individual curriculum authors and implementations MUST NOT silently alter these
requirements.
