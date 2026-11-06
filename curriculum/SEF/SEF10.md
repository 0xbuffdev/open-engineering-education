# SEF10 — Software Engineering Foundations Capstone

**Program:** SEF — Software Engineering Foundations
**Type:** `project`
**Prerequisites:** [SEF1](SEF1.md)–[SEF9](SEF9.md)
**Duration:** 8–10 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

The capstone is the final project course in Software Engineering Foundations. Each learner chooses and builds **one useful command-line developer utility across all six modules**, moving from a bounded problem brief through design, incremental implementation, verification, quantitative measurement, independent review and final defense. Core expectations are public and consistent across project choices; implementation details remain the learner's responsibility. Guidance teaches an engineering process, not a project-specific solution or tutorial to copy. Learners use appropriate programming, systems, data-structure, algorithmic and quantitative reasoning rather than adding artificial features merely to mention every prior topic.

- **SEF1–SEF9 — Software Engineering Foundations**

SEF8 may be completed alongside SEF4–SEF7, but all SEF1–SEF9 competencies must be demonstrated before the capstone is completed.

## Learning outcomes

By the end of the project, the learner will be able to:

- Turn an open-ended problem into scoped requirements, acceptance criteria, and a design.
- Build a working command-line developer utility that integrates the programming, data structures, systems, and mathematical skills from the foundation courses.
- Apply version control, automated testing, debugging, and refactoring throughout the build.
- Use appropriate data structures and algorithms and explain their time and space cost.
- Package and document the tool so another person can install, run, and extend it.
- Measure one meaningful property of the tool and use the evidence to improve it.
- Defend the implementation and explain the major design and trade-off decisions.
- Demonstrate integrated foundations outcomes with reproducible artifacts and defensible evidence, not just a successful demo.

## Modules

### Module 1 — Problem Definition & Scope

#### Outcomes

- Choose a bounded, useful CLI problem and produce a reviewed public-format project brief with users, constraints, acceptance scenarios, excluded features and success criteria.

#### Lessons

1. **Course introduction: Software Engineering Foundations Capstone** — `lesson`

   This capstone begins with the learner's own project in Module 1 and builds it throughout the course. The early modules teach the process through examples from unrelated projects and feedback at published milestone gates; the final module is delivery and independent defense, not the first opportunity to implement a feature.
2. **Project brief** — `lesson`
3. **Users** — `lesson`
4. **Requirements** — `lesson`
5. **Constraints** — `lesson`
6. **Success criteria** — `lesson`
7. **Scope and requirements** — `test`
8. **Problem statement** — `lab`

### Module 2 — Architecture & Design

#### Outcomes

- Decompose the approved project into components with clear interfaces, error boundaries and an explainable algorithm/data-structure choice.
- Review a design against its requirements.

#### Lessons

1. **Decomposition** — `lesson`
2. **Data structures** — `lesson`
3. **Interfaces** — `lesson`
4. **Architecture diagrams** — `lesson`
5. **Project structure** — `lesson`
6. **Design review** — `test`
7. **Component sketch** — `lab`

### Module 3 — Implementation & Testing

#### Outcomes

- Build the same approved project incrementally from a first failing test to an end-to-end working vertical slice, with version control and evidence-driven debugging.

#### Lessons

1. **Incremental implementation** — `lesson`
2. **Testing during the build** — `lesson`
3. **Debugging** — `lesson`
4. **Version control workflow** — `lesson`
5. **Implementation review** — `test`
6. **First failing test** — `lab`

### Module 4 — Measurement, Documentation & Release

#### Outcomes

- Collect and interpret a controlled baseline for a meaningful property, make an evidence-informed revision, and document reproducibility.
- Review a project's readiness for release.

#### Lessons

1. **Benchmarking** — `lesson`
2. **Profiling** — `lesson`
3. **Technical documentation** — `lesson`
4. **Reproducibility** — `lesson`
5. **Release preparation** — `lesson`
6. **Readiness review** — `test`
7. **Baseline measurement** — `lab`

### Module 5 — Integration, Risk & Independent Review

#### Outcomes

- Connect each graduation outcome to an inspectable project artifact, independently reproduce the deliverable, and resolve substantive review findings.
- Diagnose or prevent one material error.

#### Lessons

1. **Requirements traceability and acceptance matrix** — `lesson`
2. **Validation and error-path coverage** — `lesson`
3. **Algorithm analysis and measurement claims** — `lesson`
4. **Reproducible packaging and setup** — `lesson`
5. **Technical defense and evidence indexing** — `lesson`
6. **Integration, Risk & Independent Review reasoning** — `test`
7. **Conduct a capstone rehearsal** — `lab`

### Module 6 — Final Project Lab

#### Outcomes

- Deliver and defend the **same project built since Module 1**, including clean-checkout reproduction, an unassisted scoped change, and complete core-rubric evidence.

#### Lessons

1. **Independent defense readiness** — `test`
2. **Developer utility** — `lab`

   **Final integration lab — required work**

   The project must include:

   - Clear requirements
   - Modular architecture
   - Git history
   - Automated tests
   - Input validation
   - Error handling
   - Documentation
   - Reproducible setup
   - CI
   - Basic performance measurements
   - Release/package instructions
   - Architecture diagram
   - Decision records
   - Technical retrospective
   - Verified core scope and acceptance-to-evidence map
   - Independent clean-checkout rehearsal and substantive review findings
   - Controlled baseline and revised measurement with limitations
   - Unassisted scoped change or debugging challenge, with test evidence

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).
- Deliver, evaluate, and defend the capstone project against the published criteria.

**Capstone model — guided independence:**

One learner-owned developer utility is designed and built across Modules 1–5; Module 6 is the final submission and defense, **not** the point at which implementation starts. The course teaches how to approach an engineering project: scope, design review, testing, measurement, reproducibility, and defense. It does not supply a task-specific finished architecture or a step-by-step solution. Guidance and examples must use a **different** sample project from the learner's assessed project.

The learner chooses the language, data structures, algorithms, interfaces, and engineering trade-offs appropriate to the approved CLI problem, then demonstrates why those choices work. Coaches may ask diagnostic questions, review evidence, provide escalating hints, and explain general engineering methods, but they must not replace the learner's design and implementation. A free self-directed learner may use the public criteria, an explicit self-review record, and isolated clean-checkout reproduction; a hosted board, commercial teaching platform, paid AI service, or compulsory mentor must not be a prerequisite.

**Public project brief template — required before substantial implementation:**

- **User and problem:** Who has the problem, what currently fails, and which observable task the utility should improve.
- **CLI scope:** Commands, arguments, accepted input formats, output schema, exit statuses, persistence or filesystem behavior, and clearly excluded features.
- **Functional acceptance:** At least one ordinary use case and explicit empty, boundary, invalid-input, and failure-path scenarios; define expected outputs or errors and how each will be tested.
- **Engineering constraints:** Supported environment and dependencies, resource/data-size assumptions, safe filesystem behavior, privacy, offline reproducibility, and an approximate effort plan.
- **Data and algorithms:** Identify a meaningful structure and a nontrivial algorithmic decision (for example counting/indexing, traversal/cycle detection, streaming, or comparison), expected time/space reasoning, and a measurable property to investigate.
- **Risk and evidence:** Identify key failure modes, testing strategy, what artifact proves each acceptance criterion, and any unverified assumptions.
- **Core versus stretch:** State the smallest independently useful deliverable. Optional advanced features must not become hidden graduation requirements.
- **Review decision:** Record an explicit scoped approval or self-review against the published complexity and safety rules before major implementation. If rejected, note why and revise, rather than starting an unbounded build.

**Suggested briefs — choose one or propose an equivalent:**

- **Local log analyzer:** Read specified fixture logs, aggregate and filter events, report deterministically ordered counts, reject malformed records per an explicit policy, and measure a relevant processing property.
- **Read-only duplicate-file finder:** Scan a disposable tree, compare file sizes and content digests with an explicitly justified verification policy, report candidates without deleting files, and measure time or memory across fixture sizes.
- **Dependency explorer:** Parse a documented local manifest format, build a graph, detect cycles and produce an ordered report when possible; clearly report invalid references and measure graph traversal at chosen sizes.
- **Test-result reporter:** Parse a defined local test-result format, summarize pass/fail categories and duration data, handle missing or malformed results, and justify a collection/indexing strategy using measurements.

The above briefs define problems and acceptance boundaries, not code, starter repositories, mandated algorithms or reference solutions. A learner-proposed CLI utility is equally acceptable when it meets the same published core requirements. Existing tutorials, copied full implementations and cosmetic modifications alone do not meet the independent problem-solving objective.

**Minimum core scope — required for every approved project:**

- A useful command-line interface with clear usage, correct normal behavior, sensible output/error messages and distinct success/failure statuses.
- An explicit input/data contract, input validation and a safe policy for malformed data, missing files, boundary cases and failure cleanup. Work only on disposable fixtures for grading; no destructive effects on unrelated files.
- At least one substantive data-structure choice and one nontrivial algorithmic operation justified by correctness and time/space analysis. Mathematical reasoning is used where relevant for bounds, scaling, counting, probability or measurement—not as an arbitrary requirement to demonstrate every SEF8 topic.
- A modular, version-controlled implementation with a meaningful decision record, incremental Git history, regression tests, normal/boundary/invalid/failure coverage, a clean reproducible setup and a CI configuration or an independently runnable CI-equivalent validation workflow.
- A documented baseline and evidence-informed improvement: choose one meaningful property, measure it with repeatable controlled inputs, attempt a justified change, compare before/after conditions, and report variability and limitations. An unsupported speedup claim does not count.
- A README, installation/run/test instructions, a short architecture diagram, usable release/package instructions, requirements-to-evidence map and technical retrospective.
- An independent reproducibility rehearsal and final project defense including one small unassisted change or debugging challenge that tests ownership of the code.

**Optional stretch work — never required for graduation:**

Large data support beyond the accepted fixture bounds, concurrency, caching, cross-platform packaging, sophisticated visualization, plugin systems, advanced optimizations, or broader production-hardening features. Stretch work cannot compensate for missing core safety, correctness, tests or defense.

**Guidance ladder and project access:**

- **Early:** Public brief-format examples from unrelated projects, a scope checklist, acceptance-scenario examples and milestone feedback; the learner writes the actual project brief.
- **Middle:** Design review questions, a list of things to inspect, conceptual examples, and progressively specific debugging hints on request; the learner makes and verifies code decisions.
- **Final:** Clarify published requirements and evaluation procedure, not the implementation. The learner independently diagnoses, modifies and explains the completed project.

All mandatory instructions and evaluation criteria are public in this course. Paid mentoring may deliver extra feedback but cannot change the OEE exit standard. AI assistance is permitted under SEF9's verification and disclosure practices; it is never required, and any assisted work must be independently understood and verified.

**Milestone gates — one continuous project:**

| Milestone | Reviewable output | Gate before continuing |
| --- | --- | --- |
| M1 — Scope | Approved or self-reviewed project brief, criteria and bounded plan | Problem is useful, feasible, safe and objectively testable; no major build before scope gate |
| M2 — Design | Architecture sketch, interface contracts, algorithm/data choices, decision record and test plan | Design covers core acceptance and explains trade-offs, risks and failure cases |
| M3 — Build | Versioned vertical slice, first failing test then passing test, and incremental working features | End-to-end behavior and at least one negative path reproduce under documented commands |
| M4 — Measure and prepare | Baseline/revised measurement, documented assumptions, packaging, README and CI-style checks | Measurement is interpretable; project can be built/tested from a clean start |
| M5 — Rehearse | Requirements-to-evidence map, independent clean-environment reproduction and addressed review findings | No unexplained critical failure or missing graduation evidence remains |
| M6 — Defend | Final release, evaluated artifact, retrospective and independent technical defense | All mandatory rubric dimensions pass, including an unassisted scoped change |

Suggested pacing within 8–10 weeks: scope first, then design; allocate the largest share to iterative implementation; reserve time for measurement, independent review and defense. A learner needing remediation may revisit a milestone. Milestone acceptance depends on evidence, not the calendar or a board status.

**Assessment rubric — all dimensions required, no arbitrary numerical passing score:**

- **User value and scope:** The accepted user task and mandatory acceptance scenarios are met; any limitations are disclosed.
- **Correctness and safety:** Tests demonstrate normal, boundary, malformed and failure handling; no unresolved critical data-loss, security or resource-cleanup hazard is accepted.
- **Engineering quality:** Clear modules/interfaces, meaningful Git progression, regression tests, documentation, reproducible setup and CI or equivalent repeatable validation.
- **Algorithms and quantitative reasoning:** Explain why selected data structures and algorithms fit the task, justify time/space cost under assumptions and provide an interpretable measured comparison with a related engineering decision.
- **Traceability and independent review:** Requirements map to inspectable code/tests; a clean environment can reproduce the project and the learner responds to substantive feedback or a recorded self-review finding.
- **Human ownership:** The learner explains and changes their own final implementation without AI during the defense, discloses AI use if any and demonstrates critical understanding of trade-offs, failures and limitations.

A missing mandatory dimension means 'revise and reassess,' not automatic rejection or indefinite failure. A polished interface, optional feature, AI-generated code or a successful demo cannot substitute for missing evidence. The reviewer must state specifically which expectation is unmet and what would demonstrate it.

**Project-independent defense and assessment format:**

A live review is preferred where available, but OEE also permits a recorded walkthrough, written defense with independently inspectable code/commands, or an equivalent documented format that allows the learner's understanding to be evaluated. The reviewer may present a small, scope-bounded change from published challenge categories (new valid input case, a controlled malformed-input bug, a small CLI option, or a corrected edge-case test); do not introduce a brand-new subsystem. For a self-directed learner without a reviewer, a time-ordered unassisted session record, independent clean-environment replay and self-evaluation against the same rubric can provide inspectable evidence, with lack of external sign-off disclosed. Learners must not use an assistant during the change/defense itself, although SEF9-compliant assistance elsewhere is permitted.

**Common safe laboratory environment:**

Use a local nonprivileged environment, a version-controlled repository and synthetic project data or a learner-approved public fixture. Record operating system, language/runtime/toolchain versions, dependencies, commands and deterministic seeds where relevant. No secret credentials, real user files, destructive tools, cloud subscription, hosted CI account or mandatory internet access are required. Read-only operation is the default for analysis tasks; any intended output/overwrite must be contained in an explicitly allowed temporary/project directory. Projects using different languages or platforms must supply their own equivalent reproducible toolchain and verification commands.

**Module 1 — Problem Definition & Scope: checkpoint** — Required assessment details

- **Q1 (free):** A proposal says 'build a fast tool for organizing any files'. What information is needed before implementation can responsibly begin?
  - Expected answer and scoring: Identify a specific user and bounded task, accepted inputs/output, permissions, safe file scope, representative fixtures, ordinary/invalid cases and a measurable success criterion. 'Fast' is not independently decidable without conditions.
- **Q2 (free):** A proposed duplicate finder can delete real files, add cloud sync and display charts. Which features belong in the first core release under the published rubric?
  - Expected answer and scoring: Keep a safe read-only, bounded duplicate report and documented validation as core. Destructive deletion/cloud integration/charts are optional or out of scope. Justify scope by risk, time and observable usefulness.

**Module 1 — Problem statement: required lab** — Required assessment details

- **Objective:** Choose and bound one developer utility, writing testable acceptance scenarios and a feasible project brief before substantial coding.
- **Prerequisites:** Demonstrate the module's concepts and prerequisites from earlier SEF courses; reuse the same project artifact and satisfy the preceding milestone gate before claiming the next milestone is complete.
- **Environment:** The common safe laboratory environment and the chosen project's declared language/toolchain, with a versioned repository and synthetic fixtures. Record actual versions and commands.
- **Procedure:**
  1. Choose one of the four public example briefs or propose an equivalent developer-utility problem with an identified user, an offline fixture and a clearly stated success condition.
  2. Complete every field in the public project brief template, explicitly separating required core behavior from optional stretch requests and declaring which files and processes the CLI may affect.
  3. Write representative ordinary, empty, boundary, invalid and operational-failure scenarios; each must include a concrete input and independently checkable output, state change or error.
  4. Select a substantive structure/algorithm to investigate, explain a preliminary complexity expectation, and nominate one measurable property under controlled conditions.
  5. Perform a scope review against time budget, safety, reproducibility and difficulty; receive documented feedback from a peer/mentor or complete the same published self-review checklist and record revisions.
  6. Freeze a small initial acceptance baseline and record approved changes later as decisions, rather than allowing untracked scope creep.
- **Expected result:** A feasible, nontrivial and safe brief exists with an independently testable core, visible exclusions, acceptance/evidence mapping and a reviewable initial plan.
- **Verification:** A reviewer can pick each scenario, predict whether a submission passes it, identify relevant skill integration and confirm the scope can be completed without optional features.
- **Evidence:** Completed brief, representative fixtures, user stories, acceptance criteria, feasibility/risk table, scope-review decision and versioned changes.
- **Failure analysis:** Explain a rejected overlarge scope, an ambiguous success criterion, an unsafe permission assumption or an untestable requirement and its correction.
- **Acceptance:** The associated milestone gate and all explicitly required outputs, safe failure behaviors and independent evidence are satisfied. If not, record specific deficiencies, remediate and reassess; completing a checklist or receiving AI-generated approval alone cannot close the gate.

**Module 2 — Architecture & Design: checkpoint** — Required assessment details

- **Q1 (free):** Why is naming modules 'parser, service, output' insufficient as an architecture review?
  - Expected answer and scoring: A module name is not a contract. Identify inputs/outputs, error boundaries, data ownership, control/data flow and a reasoned data-structure/algorithm choice that supports actual acceptance scenarios.
- **Q2 (free):** If two candidate algorithms handle a small fixture, how should the learner choose without pretending to have proven performance?
  - Expected answer and scoring: Compare correctness, input sizes, complexity, space cost and likely failure modes; use small experiments as supporting evidence, not proof. Record the choice as a revisitable decision.

**Module 2 — Component sketch: required lab** — Required assessment details

- **Objective:** Create a defensible design that makes early testing possible without supplying a finished implementation.
- **Prerequisites:** Demonstrate the module's concepts and prerequisites from earlier SEF courses; reuse the same project artifact and satisfy the preceding milestone gate before claiming the next milestone is complete.
- **Environment:** The common safe laboratory environment and the chosen project's declared language/toolchain, with a versioned repository and synthetic fixtures. Record actual versions and commands.
- **Procedure:**
  1. Draw a high-level data flow from CLI argument parsing through input validation, core algorithm/data structure, report generation and bounded error outputs.
  2. Describe at least two plausible designs or algorithm choices and document the selected approach, expected time/space costs, important assumptions and trade-offs in a short decision record.
  3. Define module boundaries and key function or CLI contracts, including failure results, resource ownership and which inputs are trusted.
  4. Choose fixtures representing normal, empty, malformed and boundary cases and trace one case through the proposed components.
  5. Review design against the M1 acceptance matrix, identify one risk that could invalidate the design, and refine the design on the basis of recorded feedback or structured self-review.
  6. Document the first small vertical slice to build and the acceptance test that must fail before the implementation exists.
- **Expected result:** The architecture names responsible components, measurable algorithm/data choices and error behavior; every mandatory scenario has a plausible path through the design.
- **Verification:** Use an acceptance-to-component matrix and a worked input trace; independently challenge a design assumption and record the response.
- **Evidence:** Architecture diagram, interface contracts, options/decision record, algorithm bounds, test plan, reviewer notes and chosen vertical slice.
- **Failure analysis:** Explain a design that hides failures, unjustified complexity claim, coupling that blocks testing or an option dismissed without reasons.
- **Acceptance:** The associated milestone gate and all explicitly required outputs, safe failure behaviors and independent evidence are satisfied. If not, record specific deficiencies, remediate and reassess; completing a checklist or receiving AI-generated approval alone cannot close the gate.

**Module 3 — Implementation & Testing: checkpoint** — Required assessment details

- **Q1 (free):** What does a red-to-green test demonstrate, and what does it not establish about the rest of the project?
  - Expected answer and scoring: It shows a specified behavior initially failed and later passed under the stated test conditions. It does not establish other paths, security, scalability or full feature completeness.
- **Q2 (free):** What should be done when a learner discovers a new requirement while implementing the first slice?
  - Expected answer and scoring: Record the change and its impact, update scope/acceptance evidence and re-review if material; do not silently expand implementation beyond agreed core.

**Module 3 — First failing test and working vertical slice: required lab** — Required assessment details

- **Objective:** Build the first working end-to-end behavior of the learner's project with tests, visible revisions and a reproducible failure repair.
- **Prerequisites:** Demonstrate the module's concepts and prerequisites from earlier SEF courses; reuse the same project artifact and satisfy the preceding milestone gate before claiming the next milestone is complete.
- **Environment:** The common safe laboratory environment and the chosen project's declared language/toolchain, with a versioned repository and synthetic fixtures. Record actual versions and commands.
- **Procedure:**
  1. Create the version-controlled project skeleton and one single-command test entry point using the chosen language/toolchain; record interpreter/compiler and dependencies.
  2. Write a failing acceptance test for one complete command/input-to-output feature from the approved brief, and retain the initial failure output and commit.
  3. Implement the minimal vertical slice from CLI parsing through core processing and reporting, then demonstrate the same test passes.
  4. Add normal, empty and invalid-input cases, including one controlled failure path that must not corrupt or unexpectedly delete a fixture.
  5. Implement another small feature or revise design as evidence justifies, keeping meaningful Git history; add a regression test for one discovered bug.
  6. Use local CI-style checks, or a free compatible CI runner if already available, to repeat formatting/lint where applicable, tests and the project's declared static checks, recording results rather than only a green badge.
- **Expected result:** A user can run a minimal useful core command end to end; its original red test is green, negative behavior is defined, and the repository has reviewable change history.
- **Verification:** Run the documented test command from a fresh working copy with fixed fixtures, compare stdout/stderr/status or artifact bytes and inspect the regression before/after.
- **Evidence:** Code revision history, red/green test logs, end-to-end outputs, negative fixtures, automation command and recorded fix explanation.
- **Failure analysis:** Explain a test that passed before implementation, hidden external state, failing error path, unbounded file operation or an unexplained copied implementation.
- **Acceptance:** The associated milestone gate and all explicitly required outputs, safe failure behaviors and independent evidence are satisfied. If not, record specific deficiencies, remediate and reassess; completing a checklist or receiving AI-generated approval alone cannot close the gate.

**Module 4 — Measurement, Documentation & Release: checkpoint** — Required assessment details

- **Q1 (free):** A report claims an algorithm is 'three times faster' using one run before and after a change on different inputs. What is missing?
  - Expected answer and scoring: Use equivalent documented input conditions, hardware/runtime versions, multiple repetitions and variability, comparable baselines and correct units. One uncontrolled measurement cannot support a reliable speedup claim.
- **Q2 (free):** What makes a release reproducible even for someone without the author's editor settings or hosted account?
  - Expected answer and scoring: A clean checkout can follow documented runtime/dependency setup, build/test/run/package commands and fixture preparation with no hidden configuration or secrets. Known limitations and optional services are explicit.

**Module 4 — Baseline measurement and evidence-informed revision: required lab** — Required assessment details

- **Objective:** Measure a meaningful property, make and assess one evidence-informed improvement, and prepare a replicable release.
- **Prerequisites:** Demonstrate the module's concepts and prerequisites from earlier SEF courses; reuse the same project artifact and satisfy the preceding milestone gate before claiming the next milestone is complete.
- **Environment:** The common safe laboratory environment and the chosen project's declared language/toolchain, with a versioned repository and synthetic fixtures. Record actual versions and commands.
- **Procedure:**
  1. Choose a single meaningful target such as processing time for a fixed size, memory use under a bounded workload, parsing error rate on a fixed fixture, or a documented reliability metric.
  2. Define fixtures, measurement method, platform/runtime, units, repetitions and variability report; collect a baseline while retaining the exact source revision.
  3. Change one relevant implementation or test/reliability decision based on the evidence, keeping other conditions controlled; rerun the same measurement and compare results without implying that a single number proves asymptotic complexity.
  4. If the claimed improvement is not supported, describe uncertainty or regression, revise/undo the proposed improvement as warranted and repeat until an evidence-based engineering decision is documented; do not fabricate a positive benchmark.
  5. Write a README with clean setup, commands and failure behavior, document architecture and decision records, and prepare release/package instructions including a local build artifact where appropriate.
  6. Run a repeatable clean-checkout test/build/package check and retain the CI configuration or local equivalent command sequence for a reviewer.
- **Expected result:** A justified baseline and revised result with appropriate caveats exists, and the project is installable/testable from a clean environment without privileged or paid services.
- **Verification:** Reproduce the measurement with documented fixtures, check the interpretation against variation, then follow clean-checkout build/test/package instructions.
- **Evidence:** Before/after revision hashes, raw measurements/repetitions and conditions, analysis, README, release instructions, CI-style checks and limitations.
- **Failure analysis:** Explain a confounded benchmark, unreliable timing claim, hidden dependency or performance change that sacrifices correctness.
- **Acceptance:** The associated milestone gate and all explicitly required outputs, safe failure behaviors and independent evidence are satisfied. If not, record specific deficiencies, remediate and reassess; completing a checklist or receiving AI-generated approval alone cannot close the gate.

**Module 5 — Integration, Risk & Independent Review: checkpoint** — Required assessment details

- **Q1 (free):** A project passes unit tests but cannot start from a clean checkout because it needs a local uncommitted config file. Is its reproducibility gate satisfied?
  - Expected answer and scoring: No. Document how to create the configuration from safe defaults or fixtures, commit only appropriate templates, and demonstrate clean setup without private credentials or hidden state.
- **Q2 (free):** What happens if a reviewer finds one unrepaired data-loss path in a program that otherwise passes most tests?
  - Expected answer and scoring: The critical correctness/safety criterion remains unmet. Fix and test the issue, or narrow approved scope and demonstrate that the dangerous operation is not exposed; a high pass count or polished presentation does not compensate.

**Module 5 — Conduct a capstone rehearsal: required lab** — Required assessment details

- **Objective:** Rehearse the same project against the whole published rubric and resolve critical defects before the final defense.
- **Prerequisites:** Demonstrate the module's concepts and prerequisites from earlier SEF courses; reuse the same project artifact and satisfy the preceding milestone gate before claiming the next milestone is complete.
- **Environment:** The common safe laboratory environment and the chosen project's declared language/toolchain, with a versioned repository and synthetic fixtures. Record actual versions and commands.
- **Procedure:**
  1. Build a requirement-to-evidence matrix mapping every mandatory criterion to a source location, test, trace, measurement, explanation or reviewer observation.
  2. Clone or reproduce the project into a clean isolated environment (or obtain independent peer review where accessible), then follow the README without hidden files or setup shortcuts.
  3. Run normal, empty, malformed, boundary and operational-failure cases, check that unrelated fixture files survive and record actual outcomes and unresolved limitations.
  4. Review algorithm/data choices, risk register, permissions, CI-style checks and before/after measurement claims for evidence overconfidence.
  5. Have a reviewer suggest one scope-bounded change or use a documented surprise fixture from a published challenge category; inspect the implementation's adaptability, then record findings and a planned fix.
  6. Resolve every critical review finding with a changed revision and regression evidence, or return to the appropriate earlier milestone and revise acceptance scope explicitly.
- **Expected result:** The project independently reproduces under documented conditions; critical acceptance, safety and evidence gaps are corrected or reopened for revision.
- **Verification:** A second checkout/environment or a documented independent reviewer repeats setup and representative tests using the published acceptance matrix, and review findings link to fixes.
- **Evidence:** Rehearsal commands, environment assumptions, traceability matrix, failure logs, review notes, repaired defects, limitations and readiness decision.
- **Failure analysis:** Explain trusting a local green badge, an undocumented configuration, an ignored destructive failure or unverifiable review feedback.
- **Acceptance:** The associated milestone gate and all explicitly required outputs, safe failure behaviors and independent evidence are satisfied. If not, record specific deficiencies, remediate and reassess; completing a checklist or receiving AI-generated approval alone cannot close the gate.

**Module 6 — Final Project Lab: checkpoint** — Required assessment details

- **Q1 (free):** A polished project has all optional extensions but fails an approved malformed-input test. Can the learner pass by citing stretch work?
  - Expected answer and scoring: No. All mandatory core, correctness, safety and evidence dimensions must pass; stretch work cannot replace missing acceptance behavior.
- **Q2 (free):** A learner used an AI assistant and passes all tests but cannot explain one critical algorithm or make a small requested fix without the assistant. Is the defense complete?
  - Expected answer and scoring: No. Code evidence and independent ownership are separate requirements. Revisit and explain the algorithm, perform and test the scoped modification without assistance, then reassess.

**Module 6 — Developer utility — delivery and independent defense: required lab** — Required assessment details

- **Objective:** Deliver one independently engineered developer utility, defend every critical decision and prove a small unassisted change.
- **Prerequisites:** Demonstrate the module's concepts and prerequisites from earlier SEF courses; reuse the same project artifact and satisfy the preceding milestone gate before claiming the next milestone is complete.
- **Environment:** The common safe laboratory environment and the chosen project's declared language/toolchain, with a versioned repository and synthetic fixtures. Record actual versions and commands.
- **Procedure:**
  1. Release the same project begun in M1, showing its original approved brief, architecture, code, complete mandatory tests, release/setup instructions, measurement report, review records and retrospective.
  2. From a clean checkout execute the stated build, test, usage and negative-case commands; demonstrate the exact CLI behavior, relevant safe filesystem limits and final artifact bytes when outputs are persisted.
  3. Explain important data structures and algorithms using the actual implementation, calculate time/space reasoning under declared assumptions, and connect the measurement decision to a meaningful revision.
  4. Show requirements-to-evidence traceability, CI/configuration or CI-equivalent repeatable commands, real Git progression and one previously repaired mistake with regression evidence.
  5. Explain any AI use, including accepted/rejected suggestions, and separately identify what the learner personally implemented, tested, corrected and now understands.
  6. Perform a small reviewer-chosen change or debug challenge from a declared category without AI help, produce a focused diff and rerun relevant tests. For self-directed evaluation, record a time-ordered unassisted session and disclose lack of external sign-off.
  7. Submit a defense that another reviewer can inspect: live presentation, recorded walkthrough or well-supported written defense, containing code explanations, actual command/output evidence, limitations and open issues.
  8. Apply the full core rubric and record a pass or an actionable revise-and-reassess decision for every dimension. Optional features may be discussed but never substitute for a failed core criterion.
- **Expected result:** The reviewer can reproduce and understand the project, verify all core requirements and observe a successfully defended unassisted change under the declared challenge scope.
- **Verification:** Recreate build/test/release from clean checkout, compare mandatory acceptance scenarios and measurement evidence, inspect the unassisted change/tests and record dimension-by-dimension judgment.
- **Evidence:** Version-controlled project and commits, project brief, design, decision record, tests, CI-style validation, benchmark records, release instructions, rehearsal findings, defense evidence, scoped change, retrospective and final rubric.
- **Failure analysis:** Explain a remaining critical test failure, hidden setup, unsubstantiated performance claim, misunderstood assisted change or a correction required before graduation.
- **Acceptance:** The associated milestone gate and all explicitly required outputs, safe failure behaviors and independent evidence are satisfied. If not, record specific deficiencies, remediate and reassess; completing a checklist or receiving AI-generated approval alone cannot close the gate.

**Project defense:**

The learner demonstrates or documents the completed utility under the permitted evaluable formats and explains its architecture, data structures/algorithmic complexity, design trade-offs, tests, a reproduced failure and correction, measurement evidence, limitations and relevant assistant disclosures. The learner also performs and verifies a small scoped change or debugging challenge **without an AI assistant**. The final evaluation identifies pass or revise-and-reassess for each published core rubric dimension; incomplete critical safety or understanding evidence prevents graduation until remediated.

This is the **Program 1 graduation requirement**.
