# SEF10 — Software Engineering Foundations Capstone

**Program:** SEF — Software Engineering Foundations
**Type:** `project`
**Prerequisites:** [SEF1](SEF1.md)–[SEF9](SEF9.md), [SEF11](SEF11.md)
**Duration:** 10–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Design, build, measure, review, release and defend **one useful command-line developer utility**. Before entry, an assessor verifies all ten prerequisite SEF course completions or genuinely governed assessed equivalences; an unverified prerequisite cannot be earned through this project. The learner scopes the useful problem at the first teaching stage, develops the **same artifact** through test-driven changes and measured decisions, and presents the result under an unfamiliar unassisted defense. The ten-course graduation index records authentic prior evidence and meaningful application or conceptual transfer, **not** ten miniature re-assessments.

The capstone integrates software construction, algorithms, data structures, computing/operating-system models, version control, testing, debugging, reproducible measurement, mathematical reasoning and the professional responsibilities acquired throughout SEF. [SEF9](SEF9.md) supplies **honest risk communication**, non-AI ethics, licensing, privacy, accessible communication and truthful AI-use disclosures; those obligations still apply to hand-written code. **Integration is not a requirement to embed every earlier course's tool or exercise into one utility.** A Python-only tool need not implement C pointers or Unix sockets; a command-line tool need not manufacture calculus or a hardware simulator. Prior course evidence establishes that mastery, while the capstone makes genuine, relevant transfer visible and tests its own technical and professional claims.

There is no prescribed implementation language, repository hosting
platform, paid infrastructure, AI assistant, or external mentor. All
requirements and evaluation criteria are public. Instructional
examples should demonstrate **different** problems rather than
supply a complete assessed implementation. Feedback and escalating
hints are permitted; the learner must own the technical decisions,
code, verification, and final unassisted challenge.

After [SEF11](SEF11.md) establishes discrete proof and recurrence readiness, SEF4 and SEF8 may be studied concurrently. **All required SEF1–SEF9 and SEF11 capabilities must have verified course-completion evidence (or separately approved, genuinely assessed equivalence) before entry.** A completed attendance log, unchecked portfolio link, self-declared experience or a capstone plan does not meet the prerequisite standard. This course verifies the recorded evidence and its source revision, records uncertainties honestly, and routes actual gaps back to the prerequisite course for reassessment; it does not waive them. The architecture and defense integrate proof/invariants, realistic complexity, quantitative measurement, resource boundaries and professional duties, without demanding a new SEF mathematics, C or POSIX assessment.

**Pacing:** provisional **10–14 weeks** at about 10–15 focused hours/week (100–210 focused hours before individual remediation and defense scheduling), reflecting the full evidence audit, release-risk review and realistic independent reproduction. Actual completion is determined by criteria and observable work, **not elapsed time**. The course remains `draft` pending authentic learner and reviewer calibration.

As a non-normative external comparison, [ABET's 2026–2027 computing criteria](https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-computing-programs-2026-2027/) emphasize design/implementation/evaluation, communication, professional judgment and documented graduate attainment. OEE does **not** claim ABET accreditation, course-credit equivalence or certification based on this reference.

### Prerequisite closure is different from capstone integration

Before M1 begins, the assessor verifies each of the **ten existing prerequisite course-completion decisions** against the applicable version of that course's public outcome/assessment contract. An authorized equivalence decision must name the assessed outcomes, evidence and approval; do not turn a self-written checkbox into mastery credit. Store only safe links/identifiers and redacted summaries, not real personal data. A missing course or an unresolved required outcome **blocks entry**; the capstone cannot silently compensate for it.

The capstone evidence index uses these distinct statuses for each prior course:

- **Previously verified:** an actual reviewed outcome/assessment completion (or separately approved assessed equivalence) tied to its authentic course revision; this is the entry requirement, not a new graded capstone task.
- **Directly applied here:** code, test, measurement, release or review evidence in this exact utility; link to a verifiable source revision, result and acceptance claim.
- **Explained transfer:** a bounded unfamiliar scenario demonstrating reasoning from an earlier course (for example a C pointer-lifetime hazard or POSIX partial write) without forcing that implementation language or API into the utility.
- **Not directly applicable:** identify why no direct implementation is justified, while retaining the actual earlier verified completion; **never mark the original prerequisite itself not applicable**.
- **Gap or unknown:** actual missing prior completion, unverified claim or failed new defense; route it to review, correction or prerequisite reassessment. An absence of proof is not a passed row.

| Prerequisite | Existing evidence to verify before entry | Relevant SEF10 transfer to the *one* project |
| --- | --- | --- |
| [SEF1](SEF1.md) | Bit/logic, storage, instruction and program-to-output model | Explain a byte/encoding or source→execution→OS/output boundary and its model limits; **do not** rebuild an ALU |
| [SEF2](SEF2.md) | Real programming, input state, files, errors, composition and type/runtime behavior | Build and defend the CLI's actual input/output and state contracts; another implementation language is allowed |
| [SEF3](SEF3.md) | Shell quoting, subprocess/error handling, portability and reproducible scripts | Reproduce safe command invocation, path handling and environment-dependent diagnostics; **do not** mandate a separate shell toolkit |
| [SEF4](SEF4.md) | Invariants, data structures, complexity and independent oracles | Apply a substantial algorithm/structure, state assumptions and correctness argument, and check it independently |
| [SEF5](SEF5.md) | Git history, modular contracts, quality gates, review and maintainability | Demonstrate evolving architecture, regression evidence, honest review and clean-build commands |
| [SEF6](SEF6.md) | C11 types, lifetime/ownership, allocation, parsing and undefined behavior | Explain a relevant memory, representation or resource safety boundary (including a C11 failure distinction) **without requiring C code** |
| [SEF7](SEF7.md) | Bounded POSIX files, children, signals, directory identity, pipes and loopback | Explain the utility's relevant OS resource/error/cleanup boundary and one POSIX edge case **without requiring sockets or fork** |
| [SEF8](SEF8.md) | Algebra, calculus, linear algebra, probability, statistics and numerical error | Treat measured numerical results with justified units, variability, limitations and uncertainty; **do not** add artificial calculus |
| [SEF9](SEF9.md) | Requirements, decisions, peer review, ethics, rights, privacy, accessibility and responsible AI | Deliver auditable stakeholder scope, risk, license/data-flow checks, accessible review/release and truthful assistance disclosure |
| [SEF11](SEF11.md) | Logic, proof, recurrences, finite graphs and mathematical counterexamples | Defend a relevant invariant, termination/cost assumption or formal counterexample; test results do not replace a general proof |

For each row, link the prior assessment/decision and identify the one most relevant **direct** capstone artifact or honest transfer explanation. The reviewer can challenge a selected unfamiliar relation or boundary and demand a reasoned answer; there is no need to repeat all prior assessments. The direct capstone quality gates remain the published `SEF10-AS1`–`AS4`. The entry audit and its mapping must be inspectable, but **no eleventh course**, separate final project or blanket new course-format rule is introduced.

## Learning outcomes

- **SEF10-O1:** Select and bound a useful developer-utility problem with users, safe operating constraints, testable acceptance cases, and explicit exclusions.
- **SEF10-O2:** Design a modular architecture with clear interfaces and justify at least one substantial data-structure and algorithmic choice, including time/space reasoning.
- **SEF10-O3:** Implement a usable, safe CLI incrementally with meaningful version history, input contracts, error handling, and reproducible behavior.
- **SEF10-O4:** Use automated tests, debugging, and a repeatable CI or equivalent local workflow to verify normal, boundary, invalid, and operational-failure cases.
- **SEF10-O5:** Measure a meaningful engineering property under controlled conditions and use a documented before/after comparison to justify a technical decision.
- **SEF10-O6:** Package and document the project for clean-checkout installation, execution, testing, and independent evaluation.
- **SEF10-O7:** Relate each core requirement to inspectable evidence, reproduce the project independently, and resolve material review and safety findings.
- **SEF10-O8:** Defend the implementation, limitations, trade-offs, and any AI assistance, and complete a scoped change or debugging challenge without an assistant.
- **SEF10-O9:** Verify prerequisite completion across SEF1–SEF9 and SEF11 against authentic, version-linked assessed evidence or approved equivalence, then defend an honest program-to-capstone transfer matrix distinguishing direct application, bounded conceptual transfer, justified non-applicability and unresolved evidence without inventing credit or arbitrary features.
- **SEF10-O10:** Make and defend a responsible release or hold decision for the same utility using evidenced ethical and safety risks, copyright/license provenance, privacy/confidentiality and data lifecycle, accessible CLI/review communication, documented ownership and truthful AI-use or non-use, including a reviewer-challenged remediation.

## Modules

### Module 1 — Verified Entry, User Problem and Safe Scope

#### Outcomes

- SEF10-O1
- SEF10-O7
- SEF10-O9
- SEF10-O10

#### Lessons

1. **Prerequisite evidence is an entry gate** — Before any project work, an assessor checks actual reviewed completions or governed equivalences for SEF1–SEF9 and SEF11 with source revisions; a missing course blocks entry instead of becoming capstone credit.
2. **Select and bound one useful problem** — Choose a genuinely useful and feasible developer-utility problem, identify intended users and a substantive core algorithm/operation, then reject unrelated stretch features, copied tutorials and artificial predecessor demonstrations.
3. **State the operating envelope** — Declare nonprivileged commands, supported tools, disposable paths, data limits, file permissions and safe cleanup before accepting a potentially destructive project.
4. **Define observable CLI contracts** — Specify actual commands, argument/input validation, text or binary output, exit codes and persistence effects for an unfamiliar reader.
5. **Construct independent acceptance oracles** — Derive normal, empty, boundary, malformed and operational-failure expectations from requirements rather than copying the first implementation.
6. **Identify real professional risk** — Map data loss, private reporting, missing code rights or inaccessible evidence to plausible harm, an accountable authority and a proportionate safe fallback.
7. **Review and revise the brief** — Challenge an assumption with a reproducible input and record actual scope approval or a clearly labeled structured self-review before implementation.

**Milestone M1 — Scope:** All ten genuine prerequisite completions have been verified before entry; the one-project brief, safe CLI scope and independent acceptance cases are inspectable. Missing evidence blocks entry, while unsafe or untestable proposals require revision. This prepares `SEF10-AS1`, not a new graded activity.

*Optional practice:* Compare a log analyzer with a dependency explorer, reject an unbounded option and identify exactly which existing prerequisite records must already be verified.

### Module 2 — Algorithmic Architecture, Contracts and Proof Obligations

#### Outcomes

- SEF10-O1
- SEF10-O2
- SEF10-O4
- SEF10-O10

#### Lessons

1. **Decompose actual responsibilities** — Separate parsing, validation, meaningful computation and reporting into justified components, resisting file-count and design-pattern quotas.
2. **Choose a substantial data representation** — Compare a real data structure with a plausible simpler alternative using the required input size, memory model and supported operations.
3. **Establish correctness and termination** — Propose a relevant invariant, loop variant or counterexample and derive what must remain true for an actual capstone algorithm, not just a passing test.
4. **Qualify algorithmic costs** — Explain worst-case and, where legitimate, amortized or expected time/space under explicit assumptions, keeping asymptotic claims distinct from machine timing.
5. **Specify public interfaces and resources** — Describe valid and invalid inputs, error outputs, dependency direction, file effects and resource ownership for the actual components.
6. **Plan independent tests and a viable vertical slice** — Derive normal/failure oracles from promised behavior, trace one input across command parsing, validated state and the selected algorithm, and map high-risk interfaces to concrete tests and privacy/licensing checks.
7. **Make and review a decision** — Record alternatives, consequences and a testable decision driver, then resolve a genuine challenged assumption instead of retroactively fabricating agreement.

**Milestone M2 — Design:** The bounded algorithm, architecture, invariant/termination reasoning, resource contracts, alternative and test-oracle strategy are inspectable. Repair material gaps before relying on the implementation. This develops the existing `SEF10-AS1`.

*Optional practice:* Compare two representations for the chosen utility's real input and derive a counterexample that would violate a poorly chosen invariant.

### Module 3 — Versioned CLI Construction and Failure-Driven Verification

#### Outcomes

- SEF10-O2
- SEF10-O3
- SEF10-O4
- SEF10-O7

#### Lessons

1. **Reproducible project environment** — Set up the same learner-owned repository with known runtime/tool versions, local test commands and no undeclared hosted or private dependencies.
2. **An actual red requirement test** — Run an independently specified acceptance test before implementation and retain real expected/observed outputs and source revision, not a reconstructed red/green story.
3. **One complete useful vertical slice** — Implement parsing, validated processing and real CLI output end to end for one agreed behavior instead of building disconnected demonstration modules.
4. **Normal and malformed input boundaries** — Extend the same feature with empty, large/boundary, malformed and invalid-resource cases checked against the published behavior.
5. **State integrity on partial failure** — Reproduce a failure in parsing, output writing or resource access and verify previous valid files and unrelated sentinel data remain safe.
6. **A causal bug correction** — Capture a reproducible defect, compare plausible hypotheses, repair the fault and preserve a regression that fails on the old version.
7. **Traceable source evolution** — Keep focused commits, changed behavior, issue/decision references and genuine review observations without treating a board status as test evidence.
8. **A failure-sensitive local quality gate** — Run real unit/integration/CLI checks and reject a deliberately failing required stage with nonzero status, describing hosted CI as optional unless it actually executed.

**Milestone M3 — Build:** One complete functional slice, an actual red-then-green test, a repaired failure, reproducible negative cases and source history demonstrate the same utility's progress. The evidence belongs to `SEF10-AS2`, not a per-module lab quota.

*Optional practice:* Introduce a harmless invalid-input bug, establish a failed independent expectation, correct the behavior and preserve the regression.

### Module 4 — Controlled Quantitative Decision and Reproducible Candidate

#### Outcomes

- SEF10-O2
- SEF10-O4
- SEF10-O5
- SEF10-O6

#### Lessons

1. **Design a genuinely comparable measurement** — Choose a meaningful runtime or memory property, units, declared input scale, stable fixtures, comparable versions, run repetitions and significant cache/environment confounders before observing results.
2. **Collect a genuine baseline** — Execute the declared measurement on a known initial revision and preserve raw observations, outliers and actual conditions.
3. **Compare a bounded alternative** — Measure a justified implementation revision with an equivalent workload, avoiding an accidental speedup that silently changes required behavior.
4. **Interpret variation and report qualified conclusions** — Apply suitable SEF8 variability reasoning to measured values and unknown confounders; link the actual source revisions, raw observations, units and scope of any conclusion to a decision a later independent reviewer can inspect.
5. **Accept, reject or defer the change** — Explain whether the observed evidence justifies the revision, rollback or further study without demanding an improvement for the sake of assessment.
6. **Verify correctness after any optimization** — Recheck normal and failure contracts and a substantial invariant across the candidate versions so that lower latency cannot disguise incorrect data or unsafe state.
7. **Package one clean-start candidate** — Document supported runtime, dependencies, install/run/test/quality commands and real local release artifacts, then verify they work from a clean checkout.

**Milestone M4 — Measure and Prepare:** Comparable baseline/revision measurements, documented variability and a defensible engineering decision accompany a clean-start release candidate. A properly explained inconclusive result is acceptable; manufactured performance improvement is not. This supports `SEF10-AS2`.

*Optional practice:* Compare the same synthetic input under two algorithm settings, identify an actual confounder and justify why measured results do or do not warrant a change.

### Module 5 — Independent Reproduction, Professional Risk and Release Review

#### Outcomes

- SEF10-O3
- SEF10-O4
- SEF10-O6
- SEF10-O7
- SEF10-O10

#### Lessons

1. **Requirements-to-evidence trace** — Connect every mandatory behavior and negative case to real code, independent expected results, executed tests and a specific source revision.
2. **Separate clean-start replay** — Run the documented setup in an isolated checkout, distinguishing a self-conducted fresh replay from another person's genuine independent reproduction.
3. **Material reviewer findings** — Capture actual source-located faults and feedback when available, repair critical defects and retain regression evidence; do not invent external approval or present screenshots as sole evidence.
4. **Harm and accountable release authority** — Assess real destructive-path, data-loss, misleading success or vulnerability risks and document an evidence-backed hold or conditional release with an authorized owner.
5. **Synthetic privacy and retention proof** — Trace input, output, logs and temporary records through their permitted readers and deletion policy, and execute a redacted failure/cleanup fixture without personal data.
6. **Rights, provenance and notice audit** — Record the actual source, copyright/license permission and notice evidence for dependencies and copied material; hold or replace unverified distribution rights.
7. **Accessible interfaces and explanations** — Produce navigable Markdown, meaningful CLI help and deterministic error/status text with text alternatives to optional diagrams and no color-only meaning.
8. **Authentic AI-use or non-use disclosure** — Describe actual model/tool proposals and independently verified actions if used, without fabricating executions; maintain the same human ethical duties when no AI was involved.
9. **Review remediation and release manifest** — Re-run critical cases after fixes, state unsupported platforms, residual risks, versioned outputs and real feedback before forming the final accountable release/hold decision.

**Milestone M5 — Rehearse:** Clean-start evidence, actual reviewer observations or labeled self-review, corrected material faults and a truthful rights/privacy/accessibility release decision are available. Self-review is not independent endorsement. This prepares `SEF10-AS3` and `SEF10-AS4`.

*Optional practice:* Reproduce and repair a synthetic data leak in a failed CLI report, then revise an accessible release-risk summary without assuming permission from an unknown owner.

### Module 6 — Graduation Transfer, Unassisted Challenge and Technical Defense

#### Outcomes

- SEF10-O2
- SEF10-O5
- SEF10-O6
- SEF10-O7
- SEF10-O8
- SEF10-O9
- SEF10-O10

#### Lessons

1. **Confirm prior assessed closure** — Present the already-authenticated SEF1–SEF9/SEF11 course/revision decisions and escalate any newly discovered gap; do not reinterpret capstone work as earned predecessor credit.
2. **Demonstrate meaningful direct transfer** — Show the real project's programming, data-structure, Git, testing, algorithm and measured-evidence uses with specific commits and independently verifiable behavior.
3. **Explain machine and operating-system boundaries** — Defend a concrete SEF1/SEF3 representation/invocation model and a relevant SEF6 C-lifetime or SEF7 POSIX-resource failure at a conceptual level without implementing artificial C/OS features.
4. **Prove rather than merely time an algorithm** — Connect one actual SEF4 invariant/cost claim to SEF11 proof/termination/counterexample reasoning and distinguish it from finite test runs.
5. **Defend uncertainty and professional judgment** — Explain a relevant SEF8 measured quantity with justified variability, and SEF9 ethical, privacy, rights, accessibility and AI/no-AI accountability in the final release choice.
6. **An unfamiliar bounded change unaided** — Respond to an evaluator-selected valid input, malformed case, small option or edge-case bug within the disclosed categories, implement or diagnose it **without an assistant**, then rerun appropriate tests.
7. **Independent technical defense and limitations** — Explain algorithms, trade-offs, performance uncertainty, prior corrected defects, actual review findings and known risks in an inspectable live, recorded or written defense.
8. **Publish the evidence map and actual graduation decision** — Map all ten capstone outcomes and the four existing summative assessments to actual source, normal/negative, measurement, professional and prerequisite evidence; apply the complete rubric and record an attributable pass or revise-and-reassess decision with specific unresolved gaps and labeled external or self-review provenance.

**Milestone M6 — Defend:** The same project begun in M1 is defended under `SEF10-AS3` and `SEF10-AS4` with an unassisted unfamiliar change, authentic previously verified prerequisites, source-linked transfer and an evidence-backed release/hold decision. This is not a new final lab.

*Optional practice:* Have a reviewer supply a previously unseen edge case plus a relevant SEF concept, and defend the response using actual evidence rather than a memorized script.

## Completion requirements

The capstone is completed by satisfying its outcomes, the prior verified completion of **all ten prerequisite courses**, the public one-project contract, and **four required summative assessments** below. These evaluate **one cumulative project**, not four unrelated builds, a separate mathematics course or a quota of labs. `SEF10-AS4` adds program-integration and professional-release evidence that was not explicitly assessed by the original three blocks.

| Assessment | Required outcome coverage | Primary evaluation |
| --- | --- | --- |
| `SEF10-AS1` — Scope and Architecture | SEF10-O1, SEF10-O2 | Approved problem brief, acceptance and safety contract, design and algorithm decisions |
| `SEF10-AS2` — Engineering Delivery | SEF10-O3, SEF10-O4, SEF10-O5, SEF10-O6 | Working utility, tests, Git history, reproducible build, measured revision |
| `SEF10-AS3` — Review and Defense | SEF10-O7, SEF10-O8, SEF10-O3, SEF10-O5, SEF10-O6 | Clean-environment review, defended technical choices, bounded unassisted change |
| `SEF10-AS4` — Program Integration and Responsible Release | SEF10-O1, SEF10-O2, SEF10-O5, SEF10-O6, SEF10-O7, SEF10-O8, SEF10-O9, SEF10-O10 | Verified prerequisite evidence index, honest cross-course transfer, professional release-risk/rights/privacy/accessibility decision |

A milestone is a progress and review gate for the same project.
Milestones M1–M6 identify when evidence should become inspectable;
they are **not six additional submissions** or separate graded labs.
Earlier material may be refined when findings justify revision.
The final evaluation must consider the current complete artifact
and the retained evidence of its engineering progression.

### Public project brief

Before substantial implementation, record these items in a
learner-owned version-controlled brief:

- **User and problem:** intended user, practical need, and bounded
  result that is independently useful.
- **CLI contract:** commands, arguments, accepted inputs, outputs,
  exit statuses, persistence or file effects, and exclusions.
- **Acceptance cases:** concrete normal, empty, boundary,
  malformed, and operational-failure scenarios, each with
  expected observable outcomes.
- **Environment and safety:** supported runtime/toolchain, data
  boundaries, file permissions, cleanup behavior, dependencies,
  and conditions for reproducible offline testing.
- **Data and algorithms:** one nontrivial operation and
  substantive structure, expected complexity, and a measurement
  question related to the design.
- **Risk and evidence:** likely failures, verification strategy,
  relevant limitations, and the evidence that will support
  each acceptance claim.
- **Graduation readiness:** verified assessment-completion identifiers,
  versioned source references and any genuinely assessed, approved
  equivalence for SEF1–SEF9 and SEF11; do not expose sensitive
  learner records or mark an unknown as a pass.
- **Responsible release:** expected users and potential harm,
  privacy/logging/temporary-output behavior, source and license
  provenance, accessible review and a release/hold authority plan.
- **Core versus stretch:** the smallest useful deliverable
  and expressly optional enhancements.
- **Scope review:** recorded approval against the public
  criteria or reasoned self-review; rejected proposals must
  be revised, not treated as silently accepted.

### Project options

Choose one of these public problem briefs or propose an equivalent
bounded CLI utility. They describe **problem space**, not a
provided solution, implementation template, or prescribed algorithm:

| Option | Minimum useful behavior | Safety and reasoning |
| --- | --- | --- |
| Local log analyzer | Parse fixture logs, filter and aggregate events, report deterministic counts | Define malformed-record policy, data structure, and a measured property |
| Read-only duplicate-file finder | Scan an explicitly disposable directory and report duplicate candidates | Never delete; justify size/digest/content verification and time or memory trade-offs |
| Dependency explorer | Read a documented local manifest and report a graph and cycles | Reject invalid references; explain traversal, ordering, and complexity |
| Test-result reporter | Parse a bounded local test-result format and summarize outcomes and durations | Account for missing/malformed results and defend data collection/indexing |

A different project is acceptable when it satisfies the same
outcomes, core complexity, safe operating boundaries, and public
evaluation standards. Cosmetic changes to a copied full
implementation or reproducing a tutorial solution alone do
not demonstrate independent engineering ownership.

### Required core deliverables

Every approved project must provide:

1. **Usable CLI:** meaningful normal behavior, documented
   inputs and outputs, validation, informative errors,
   correct exit statuses, and safe handling of empty,
   boundary, invalid, and failure cases.
2. **Engineering design:** modular components with explainable
   interfaces, a nontrivial algorithm and data-structure
   decision, correctness argument, and justified time/space
   complexity under stated assumptions.
3. **Engineering history:** incremental version control,
   an initially failing acceptance test that is made to
   pass, subsequent regression evidence, and a documented
   significant design or debugging correction.
4. **Verification:** automated tests for the agreed
   acceptance and failure cases, safe filesystem behavior,
   a reproducible test command, and CI configuration or
   a locally runnable equivalent verification workflow.
5. **Measurement:** controlled before/after evaluation of
   one relevant property, fixed or comparable fixtures,
   units, repetitions, conditions, observed variability,
   and a justified decision including any uncertainty.
6. **Documentation and release:** a README, install/run/test
   commands, architecture diagram, important decisions,
   local release/package instructions, explicit
   environmental assumptions and known limitations.
7. **Reproducibility and review:** independent clean-checkout
   rehearsal, acceptance-to-evidence map, material
   review findings and fixes, and a meaningful
   engineering retrospective appropriate to a capstone.
8. **Defense:** evaluated explanation of the actual code,
   data structures, performance claims, safety boundaries,
   AI assistance where used, and a small scoped
   independently implemented or diagnosed change.
9. **Graduation and professional handoff:** a ten-course
   source-revision-pinned prerequisite index with an honest
   direct/conceptual/not-applicable transfer map, followed by
   an evidence-based ethical, privacy, license/provenance
   and accessibility release-risk decision on the same utility.

Do not add requirements for concurrency, extensive
visualizations, plugins, cloud deployment, advanced
performance optimization, cross-platform installation,
or unrelated production features solely to demonstrate
breadth. These are optional stretch work and cannot
compensate for a missing core criterion.

### Safe and independent environment

Use a nonprivileged local toolchain and version-controlled
source with synthetic or explicitly authorized public
fixtures. Test file-writing behavior only in a known
disposable project/temporary directory. Read-only
operation is the default for analysis tools; a
utility requiring writes must clearly bound its allowed
paths and cleanup behavior.

Record meaningful OS, compiler/runtime, dependency,
and build/test command information, including deterministic
inputs or seeds as applicable. Do not use real personal
files, secrets, privileged execution, destructive operations,
mandatory hosted CI, paid cloud resources, or proprietary
credentials in required evaluation.

An automated test or green CI badge is supporting
evidence, not proof of untested safety or capability.
No paid teaching platform, compulsory mentor, or AI
assistant is required.

### Milestone review criteria

| Gate | What must be inspectable | Stop or revise when |
| --- | --- | --- |
| M1 — Scope | Verified ten-course prerequisite entry index, feasible brief, safe CLI, acceptance cases | A required prior course is unverified or scope is unsafe, unbounded or untestable |
| M2 — Design | Interfaces, decision record, algorithm/structure reasoning, test plan | Core scenarios lack a credible path or material risks are hidden |
| M3 — Build | First red/green test, vertical slice, incremental history, failure handling | End-to-end behavior or key safety case does not work |
| M4 — Measure | Controlled baseline/revision, repeatable tests, release guide and preliminary risk/rights/data map | Measurement is uninterpretable, risk is hidden or setup depends on undisclosed state |
| M5 — Rehearse | Clean-start replay, graduation-transfer matrix, ethical/privacy/license/accessibility findings, reviewed fixes | Critical issues, missing prerequisite evidence or nonreproducible claims remain |
| M6 — Defend | Final deliverable, unassisted challenge, responsible release decision and rubric | Technical ownership, real evidence or any mandatory dimension is unproven |

The provisional 10–14-week study range should reserve the largest
share of work for iterative implementation, measured revisions, responsible
release assessment and enough time for a legitimate independent review. Failing a gate means revise
and reassess the relevant work; it is not a demand for
a new standalone lab or an arbitrary numerical score.

### Required assessments

- **SEF10-AS1** (required scope and architecture evaluation)
  - Outcomes: SEF10-O1, SEF10-O2
  - Work: choose one bounded useful developer utility and
    complete the public project brief. Explain who needs
    the utility, define its safe CLI and input/output
    contracts, enumerate concrete acceptance and
    failure cases, and distinguish core behavior from
    optional features. Propose a modular design,
    interface boundaries, selected data structures,
    a substantial algorithm and its expected
    time/space cost. Identify risks and a failing
    initial test; conduct a recorded scope/design
    review or structured self-review before building
    the core implementation.
  - Criteria: useful and feasible scoped objective,
    explicit safe operating envelope, testable normal
    and failure paths, credible decomposition, correct
    assumptions for complexity reasoning, planned
    evaluation and measurement, and meaningful
    response to a challenged design assumption.
    Projects with arbitrary complexity, unsupported
    destructive behavior, or no independently
    checkable acceptance conditions must be revised.
  - Evidence: versioned brief, acceptance-case matrix,
    architecture and interface sketches, data/algorithm
    reasoning, risk register, initial test plan,
    design decision record, and reviewer/self-review
    findings with any revised scope.

- **SEF10-AS2** (required implementation, verification, and measurement)
  - Outcomes: SEF10-O3, SEF10-O4, SEF10-O5, SEF10-O6
  - Work: develop the approved project from an initial
    failing acceptance test through a working vertical
    slice to the complete core scope. Demonstrate safe
    input validation, meaningful failures, a versioned
    correction and regression test, and repeatable
    build/test/CI-equivalent commands. Explain
    the implemented algorithms and their data costs.
    Perform a controlled baseline and a justified
    revision with comparable measurements. Prepare
    install/run/test and release documentation and
    demonstrate clean-checkout setup.
  - Criteria: required scenarios behave as specified;
    no unexplained critical data-loss, trust-boundary,
    permission, or resource-cleanup failure; meaningful
    history and test coverage; independently verifiable
    algorithm choice; honest measurement with recorded
    conditions, repetitions, variability, and limitations;
    reproduction from declared commands without hidden
    files, services, secrets, or undocumented state.
    An inconclusive measurement may support a decision
    to revert, retain, or investigate rather than a
    fabricated improvement.
  - Evidence: complete version-controlled code,
    red/green and regression history, normal/invalid
    and boundary test fixtures/results, local
    CI-equivalent commands or CI config, actual
    measurement records and revision identifiers,
    documented trade-offs, architecture diagram,
    README and release/packaging instructions,
    clean-environment test record, and limitations.

- **SEF10-AS3** (required independent review and technical defense)
  - Outcomes: SEF10-O7, SEF10-O8, SEF10-O3, SEF10-O5, SEF10-O6
  - Work: map every agreed core criterion to project
    evidence; replay build, tests, normal/failure
    behavior and the release from an isolated clean
    environment, or obtain an equivalent independent
    review. Correct each critical finding or explicitly
    reopen an earlier milestone. Present and defend
    the **same project** begun under SEF10-AS1.
    Explain architecture, algorithms, time/space
    reasoning, measurement interpretation, significant
    mistakes and corrections, limitations, and
    AI assistance where used. Without AI help during
    the defense, complete one reviewer-selected
    small change or debugging challenge from the
    published categories: a new valid input, a
    controlled malformed-input case, a minor CLI
    option, or a repaired edge-case regression test.
    Record a dimension-by-dimension decision.
  - Criteria: clean-start operation and material
    acceptance cases reproduce; there are no
    unresolved critical safety defects; the learner
    can substantively explain and change their own
    implementation, trace evidence to requirements,
    justify measurement claims, disclose relevant
    assistance, and verify the scoped challenge
    using appropriate tests. A challenge must
    stay within the existing system and may not
    require a brand-new subsystem. The final
    defense must be reviewable in the format used.
  - Evidence: clean-checkout reproduction and
    requirement-to-evidence map, review findings
    and remediations, final release and assessment
    rubric, code/command/output inspection record,
    a focused unassisted change or debugging trace
    with verification results, AI-use disclosure
    if applicable, technical defense recording
    or written transcript with references, and
    technical retrospective.

- **SEF10-AS4** (required program-level prerequisite integration and responsible release)
  - Outcomes: SEF10-O1, SEF10-O2, SEF10-O5, SEF10-O6, SEF10-O7, SEF10-O8, SEF10-O9, SEF10-O10
  - Work: On the **same learner-owned utility** already assessed under SEF10-AS1–AS3, prepare a ten-row graduation and transfer index for `SEF1`–`SEF9` and `SEF11`. For each row identify its actual prior assessed outcome/assessment completion or authorized equivalence, source course revision, reviewer/decision provenance and safe evidence pointer; a missing genuine prerequisite is a **block to entry/award**, not an opportunity to claim a pass in the capstone. Link a relevant direct capstone behavior or precise conceptual transfer to each course, with reasoned not-applicable treatment where implementation would be artificial. Give evidence-backed examples of an actual SEF4 algorithm invariant and cost assumption; an SEF11 logical/termination/counterexample claim; SEF8 measurement units, variability and uncertainty; SEF1 representation/execution and SEF3 invocation assumptions; SEF6 C memory/representation/undefined-behavior boundary; and a SEF7 POSIX descriptor/process/failure boundary **without implementing unrelated C, Rust, sockets, calculus or CPU hardware**. An assessor chooses one unfamiliar bounded, project-relevant cross-course question; answer it unaided and distinguish a proof from finite testing and a claim from an observation. Independently audit this utility's **real** privacy-sensitive data flow (including logs and temporary outputs), permission and retention/deletion policy; sources/dependencies and actual copyright/license/notice evidence; accessibility of CLI errors, semantic Markdown/text review and release commands; and potential user harm, failure rollback and professional communication. Make an evidenced, accountable **release/hold** decision stating unresolved risks, mitigation and next verification. Invite a substantive independent review of the same artifact when available, or preserve a reproducible cold-start and clearly labeled self-evaluation limitation under the existing defense policy; never fabricate an approval. Reuse the tests, review, version history and evidence from AS1–AS3, with **no second implementation or specialist-system requirements**.
  - Criteria: All ten prerequisite completion decisions are authentic, revision-linked and actually verified before capstone entry or else reported as a blocking gap; self-declared attendance, AI output, unassessed code or a status-board checkmark cannot substitute for earlier assessed outcomes. The matrix differentiates prior demonstrated competence, direct capstone transfer, explanation-only transfer and justified non-applicability without pretending the project itself re-assesses every prerequisite. The challenge demonstrates correct relevant reasoning on unfamiliar values/situations, with a documented invariant/cost argument and justified quantitative-uncertainty treatment rather than an unjustified benchmark proof. The release/hold conclusion follows observed failures, risk severity, actual rights/permission evidence and real stakeholder authority, with unknown licensing or privacy permission left unknown rather than invented. Personal/secret data remain out of fixtures and review logs; cleanup and retention policy is actually checked in a controlled failure case. CLI instructions, error messages, review/evidence paths and release limitations are navigable and understandable in text without color-only state or screenshot-only claims. Genuine reviewer findings and their revisions are attributable; a self-evaluation is not called independent third-party endorsement. The learner owns the technical and ethical judgment **without assistant assistance during the challenge**. Any missing prior completion, unresolved critical safety/data rights or fabricated evidence prevents the capstone graduation decision.
  - Evidence: Ten-course versioned prerequisite-completion/equivalence index with non-sensitive pointers and stop/approval records, capability-to-project transfer matrix, independently inspectable algorithm/complexity and statistical measurement explanation, bounded unassisted cross-course challenge record, source/right/notice inventory, synthetic data-flow/retention/cleanup and failure-test outputs, accessible textual CLI/review/release handoff, risk/mitigation owner log with reasoned ship/hold outcome, real reviewer observations or explicitly labeled replay/self-review, and links to the **same** versioned utility and existing AS1–AS3 artifacts.

### Project defense and assessment rubric

A live technical review is appropriate where
available, but a recorded walkthrough, structured
written defense with inspectable code/commands, or
another reviewable evaluation may establish the
same outcomes. A reviewer may choose a challenge
within one of the published categories; the
category is disclosed, but the specific input
or bug need not be disclosed in advance.

For independent learners without access to a
reviewer, a time-ordered unassisted session
record, a separate clean-environment replay
and an explicitly declared self-evaluation
can supply reviewable evidence. **Lack of
external sign-off must be disclosed**; a
self-review is not an independent reviewer
endorsement. AI assistance is permitted in
the broader project consistent with SEF9,
but it must be understood, verified, and
disclosed where applicable; no assistant may
perform the scoped defense change for the learner.

All mandatory rubric dimensions must pass. The final two additional dimensions carry the new SEF10-O9/O10 evidence in `SEF10-AS4`, not a new project:

| Dimension | Required demonstration |
| --- | --- |
| User value and scope | The approved useful task and acceptance boundaries are met |
| Correctness and safety | Normal, empty, malformed, boundary, and failure behavior is verified without unresolved critical hazards |
| Engineering quality | Modularity, meaningful Git progression, reproducible tests and release, and documentation |
| Algorithms and quantitative reasoning | Justified data structure/algorithm, complexity analysis, and interpretable measurement-based decision |
| Traceability and reproduction | Core claims link to inspectable evidence and can be repeated from a clean start |
| Ownership and defense | Learner explains actual implementation, responds to a bounded challenge unassisted, and documents limitations |
| Graduation evidence and transfer | All ten course completions verified by versioned assessed evidence or governed equivalence; direct versus conceptual application and gaps honestly distinguished |
| Professional release and accessibility | Justified ethical release/hold, privacy and retention controls, license/source status, text-accessible user/review handoff and responsible communications |

A missing dimension results in **revise and reassess**,
with a specific evidence gap or defect recorded;
there is no arbitrary numerical passing score.
A polished interface, optional stretch feature,
copied tutorial, AI-generated code, or successful
happy-path demonstration cannot substitute for
required capability and safety evidence.

### Formative activities and revision history

Optional practice may include critiquing unrelated
sample project briefs, testing hypothetical
algorithm claims, exploring design alternatives,
debugging small synthetic examples, or rehearsing
an explanation. These activities help learning but
are not extra graded submissions.

The previous SEF10 revision mandated one checkpoint
and one lab in each of six modules plus a final
lab-shaped delivery requirement. The later v0.2.0 rewrite
established **one project, six M1–M6 progress gates
and three coherent summative assessments**. This RFC 0003
academic hardening keeps those six milestone identities
and the original eight outcomes and three assessment definitions,
adds two instructional stages (eight modules overall) and
one new `SEF10-AS4` for previously unassessed program
integration and professional release judgment.
Neither adding new assessment identifiers nor changing
the timetable retroactively revokes historical learner
evidence or pretends prior records satisfy new requirements.

This capstone remains `draft`. Passing the
structural validator does not establish
teaching efficacy, independently reproduced
project options, learner testing, or `verified`
status. See [Evidence Rules](../../spec/evidence-rules.md)
and [Status Labels](../../spec/status-labels.md).

### RFC 0003 graduation integration revision and historical evidence

This revision completes the **SEF10 course follow-up** under [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). Its historical contract is [SEF10 at OEE commit `ef51f0a5765a5bb95ad4fdec4e2d58d64997c1b4`](https://github.com/0xbuffdev/open-engineering-education/blob/ef51f0a5765a5bb95ad4fdec4e2d58d64997c1b4/curriculum/SEF/SEF10.md). **All eight original `SEF10-O1`–`SEF10-O8` descriptions and all three original `SEF10-AS1`–`SEF10-AS3` Work, Criteria and Evidence contracts remain textually identical.** Their historical outcomes, reviews and decisions retain their meaning.

| Previously required | Revised integration/evaluation | Historical evidence treatment |
| --- | --- | --- |
| `SEF10-O1`–`SEF10-O8` and `SEF10-AS1`–`SEF10-AS3` | **Exact old definitions** plus new `SEF10-O9`, `SEF10-O10`, `SEF10-AS4` | Earlier records remain pinned to their assessed version; no new competence is silently inferred from an old completion |
| Ten prerequisite course completions, stated but not integrated into a public evidence map | Genuine ten-course completion verification and a direct/conceptual/justified-not-applicable transfer index | Pre-entry evidence is not recreated or waived; an absent completed course remains a blocker |
| Six teaching modules and six milestone gates | Eight instructional modules and the **same six M1–M6 milestone identities**, no additional standalone exams | Same developer utility from M1 through final defense |
| Provisional 8–10 weeks | Provisional 10–14 weeks | Calibration only, not a credit-hour equivalence, learner readiness guarantee or pass condition |
| Focus on correctness, CI, review, measuring and unassisted defense | Explicit professional release/hold decision including ethics, rights, privacy, accessibility, honest reviewer provenance and relevant mathematical/OS transfer | No mandatory hosted deployment, Rust, C, multi-client service or unrelated APP/SYS capability |

An earlier SEF10 completion is not automatically rescinded or automatically upgraded to include O9/O10; any transition must use actual reviewed evidence and the applicable published revision. The [SEF catalog](README.md) remains the authoritative prerequisite order. SEF10 still has no hidden paid tool, AI requirement, new course-format rule or promotion beyond `draft`.

**Subsequent competency-derived instructional consolidation:** The prior eight-module revision repeated pre-entry course evidence in two consecutive teaching blocks, blended measurement with release decisions before giving professional review its own purpose, and retaught integration/review in both final modules. This review consolidates these into genuine project milestones and distinguishes *assessor-verified entry eligibility* from later *capstone-specific transfer and defense*. The original ten outcomes and four complete summative assessment contracts stay unchanged, including the material O9/O10/AS4 obligations; six original M1–M6 progress milestones remain, and one cumulative utility still supplies the work. Module and lesson counts are outcomes of those boundaries, never a template. No historical learner credit, specialist-language gate or readiness status changes.

This is the **Program 1 graduation requirement**.
