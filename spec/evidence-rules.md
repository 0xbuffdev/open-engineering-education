# Evidence Rules

This document defines the evidence needed to support OEE learning outcomes,
course completion, course-readiness labels, and truthful engineering claims.
It implements [RFC 0001](../rfcs/0001-outcome-driven-curriculum.md).
Evidence demonstrates capability; completing a prescribed list of activities
does not, by itself, demonstrate capability.

## 1. Required outcomes and assessment evidence

An outcome evaluation MUST be:

- **Observable:** a reviewer can inspect a performance, explanation, or artifact.
- **Decidable:** published criteria distinguish acceptable from unacceptable work.
- **Relevant:** the evidence actually measures the claimed outcome.
- **Substantive:** completion requires the intended capability, not memorized
  terminology or unexplained copied work.
- **Bounded:** assumptions, limitations, and claims not established by the
  evidence are made clear when relevant.

Each required course outcome MUST be traceable to one or more required
summative assessments. A single substantial artifact MAY establish multiple
outcomes when its evaluation criteria support each claim. Evaluators MUST
NOT claim an outcome was demonstrated merely because an assessment ID
references it.

A course MUST publish required assessments, success criteria, and evidence
expectations in advance. The public requirements MUST support independent
study and review without a paid service or proprietary grading system.

## 2. Course completion

A learner completes a course only when:

1. All required outcomes have been demonstrated against the published criteria.
2. Every required summative evaluation has an inspectable decision and its
   stipulated supporting evidence.
3. Required reproducibility, explanation, and limitations requirements
   applicable to the work are met.
4. For a `project` course, the published project deliverables and an
   appropriate technical defense have been evaluated.

A course MAY require multiple evaluations for an outcome when justified,
provided the combined evidence requirements are explicit and published.

No fixed number of knowledge tests, module labs, exercises, or concluding
integration labs is mandatory across all OEE courses. An author SHOULD
avoid duplicated summative work where existing evidence adequately measures
the same capability. An integrated demonstration SHOULD be required when
the outcomes depend on integration; otherwise sufficient cumulative evidence
MAY establish completion.

Optional practice, formative feedback, self-checks, reading, attendance, and
time spent are not mandatory completion requirements unless the course has
explicitly and justifiably designated a relevant evaluated performance as
required evidence. No ordinary activity checkmark, attendance log, or
unsupported assertion can alone establish completion.

A project defense MAY be live, recorded, written, or conducted through
another reviewable format suitable for evaluating authorship, reasoning,
design choices, verification, results, and limitations. Its evaluation
criteria MUST be published.

## 3. Proportionate evidence for assessed work

Evidence obligations MUST be proportionate to the size, risks, and
claims of the evaluated work. Small conceptual or practice activities
MUST NOT universally require a full lab report, build log, environmental
inventory, or technical retrospective.

### 3.1 Traceability

A required evidence record MUST identify the course and assessment
requirements it supports and provide the artifact, explanation, or
performance record needed for review. For revised courses with stable
identifiers, the record SHOULD include the course revision, assessment
ID, evaluated outcome IDs, decision, and supporting evidence reference.
Where version control is used, a relevant repository and commit SHOULD
be identified.

### 3.2 Reproducibility

When an executable result is used as required evidence, the implementation
MUST be reproducible from a clean checkout or equivalent clean state
through documented instructions, subject to disclosed environment
assumptions. Instructions MUST NOT depend on undocumented private files,
hidden configuration, or unexplained manual steps.

Non-executable conceptual, mathematical, design, or analytical work
MAY be evaluated through a reviewable solution, explanation, derivation,
or observed performance. These do not require an artificial executable
artifact.

### 3.3 Verification and testing

Where code is assessed, evidence SHOULD include applicable normal,
boundary, invalid-input, and failure cases. Claims about reliability,
performance, security, or correctness MUST be limited to what the
verification actually establishes.

Expected and observed behavior MUST be distinguishable. An automated
software test establishes the tested behavior, not necessarily the
learner's independent understanding; a reviewer MUST seek additional
evidence when that understanding is a required outcome.

### 3.4 Environment and limitations

A required record MUST identify environment details when they materially
affect reproduction or interpretation. This MAY include operating system,
hardware, compiler, runtime, dependencies, commands, build flags, seeds,
and measurement conditions as applicable.

A substantive report MUST disclose material assumptions, limitations,
and unresolved problems. Performance or benchmark claims SHOULD state
sufficient methodology, repetitions, and variability to interpret them.
Irrelevant environment inventory MUST NOT be imposed by default.

### 3.5 Engineering reasoning and reflection

Substantial engineering work MUST provide an appropriate explanation of
meaningful design trade-offs, failures, corrections, changed assumptions,
or limitations when these affect the claim being evaluated. A project
course MUST contain a reviewable explanation of the learner's technical
decisions as part of its defense.

A course MAY request a retrospective when it evaluates a relevant
outcome. It MUST NOT demand a formulaic retrospective for every small
exercise or lab regardless of educational purpose.

## 4. Evidence that is insufficient on its own

The following do not independently establish mastery or completion:

- A checkbox, attendance record, or statement of understanding.
- An assertion that an activity was performed without the required result.
- Pasted output without the context needed to interpret it.
- A demonstration dependent on unexplained local configuration.
- A passing test used to imply untested properties or knowledge.
- A benchmark with no meaningful measurement context.
- A project report hiding relevant unresolved failures or limitations.
- An inaccessible record when the intended reviewer requires access.

These materials MAY provide supporting context but MUST NOT replace
the required outcome demonstration.

## 5. Records, revisions, and privacy

An assessment result SHOULD identify the applicable specification version,
course revision, assessment ID, evaluated outcomes, evidence location,
decision, and reviewer or evaluator as relevant. A record MUST state
material access restrictions affecting review.

Completed work MUST remain interpretable against the requirements in force
when it was assessed. A new course revision MUST NOT silently mark
historical learners as newly complete or incomplete; any needed
re-evaluation MUST be explicit and justified by the changed outcomes or
criteria.

Learners and reviewers MUST NOT publish secrets or private learner
information simply to satisfy an evidence requirement. Sensitive records
SHOULD be redacted, access-controlled, or summarized as appropriate,
while retaining sufficient inspectable material for the intended reviewer.
A public status claim MUST NOT rely on evidence unavailable to its
intended reviewer.

## 6. Evidence and course status

Course-readiness labels describe the evidence for the educational
course definition, not an individual learner's completion.

| Promotion | Minimum evidence |
| --- | --- |
| `draft` to `tested` | At least one learner completes the course; completion evidence is recorded; feedback is reviewed; and a revision note explains what changed as a result. |
| `tested` to `verified` | At least two learners complete the course; the required summative evaluations and applicable engineering artifacts are reviewed or reproduced; and a qualified reviewer records sign-off. |

A status change MUST have an inspectable supporting record. If the
evidence becomes unavailable, materially incorrect, or insufficient,
the status MUST be reassessed and lowered when no longer justified.
The learner-count thresholds and reviewer requirement are unchanged
by [RFC 0001](../rfcs/0001-outcome-driven-curriculum.md).
See [Status Labels](status-labels.md).

## 7. Assessment integrity and implementation independence

Course authors MUST identify what is being assessed and the evidence
sufficient for a valid decision. Public assessment requirements MUST NOT
depend on an undocumented grading implementation. Exact reusable exam
items, private challenge variants, answer keys, and grading algorithms
do not have to be publicly disclosed if equivalent public-required
work and success criteria are available.

Implementations MAY add formative practice, unseen equivalent
summative variants, automated grading, or reviewer feedback. They
MUST preserve OEE's published outcome requirements when claiming
completion of the canonical course. Where automated evaluation is
used, the record SHOULD retain its relevant context; an automated
result MUST NOT be represented as proof of properties or abilities
not actually evaluated.

These rules govern educational and evidentiary expectations, not
a mandatory commercial assessment service or technology.
