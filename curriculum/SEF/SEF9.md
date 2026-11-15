# SEF9 — Professional Workflow & AI-Assisted Engineering

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF5](SEF5.md)
**Duration:** 6 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn how engineering teams turn requests into reviewable changes and evidence-backed delivery. Write user stories and measurable acceptance criteria; plan work with explicit dependencies; preserve design choices in decision records; review focused patches; and use coding assistants as **constrained sources of proposals**, not authorities for implementation, test results or acceptance. Demonstrate that you can explain, repair and extend accepted code independently.

**SEF5 is the only formal prerequisite.** [SEF4](SEF4.md) is recommended preparation, not an entry requirement. The reference project is the SEF5 tested command-line task manager or a comparable learner-owned Python 3.11+ program. A CSV-export improvement for synthetic task data provides a common example across modules, but an equivalent fully reproducible local feature can satisfy the same published criteria.

All required tasks can be completed offline using a disposable local Git repository, Python's standard library and versioned Markdown or JSON issue/board/PR artifacts. Hosted trackers and live assistants are optional. For AI-related work, use either an accessible assistant **or an authentic instructor-supplied recorded assistant proposal**; mark recorded and interactive usage accurately, including actual tools and models if known. Do not invent transcripts, prompts, tool calls, tests or live reviews. The learner must inspect, test and repair the suggested change independently. A peer or designated independent reviewer must reproduce the final feature and offer substantive feedback, even when collaboration artifacts are stored locally.

The eight original modules remain the instructional sequence. Seven summative assessments evaluate the connected workflow; earlier verified decisions, tests, reviews and source may be reused in the integrated feature. No universal quiz/lab pair, paid AI product, mandatory network access, broad repository authority or duplicate final project is required. The six-week workload estimate is provisional, and the course remains `draft` pending real learner and reviewer evidence.

## Learning outcomes

- **SEF9-O1:** Translate a stakeholder need into clear user stories that identify users, capabilities, value, assumptions, and bounded delivery scope without prematurely prescribing an implementation.
- **SEF9-O2:** Publish observable acceptance scenarios, failure cases, requirement-to-test links, and a definition of done that distinguishes business behavior from engineering process.
- **SEF9-O3:** Decompose a feature into traceable issues, dependencies, owners, labels, milestone and review artifacts in a locally reproducible or hosted tracking system.
- **SEF9-O4:** Maintain honest work-item states, resolve blocked tasks and scope changes, and distinguish board status from acceptance and independently verified completion.
- **SEF9-O5:** Write and maintain engineering decision records with context, alternatives, drivers, consequences, evidence, status and explicit supersession links.
- **SEF9-O6:** Review a focused change against a published standard, reproduce a substantive defect, and provide specific, respectful, actionable comments supported by evidence.
- **SEF9-O7:** Prepare a reviewable change description and respond to reviewer findings with bounded revisions, regression tests, and an inspectable resolution record.
- **SEF9-O8:** Describe AI coding-assistant context, model/tool limitations, permissible actions, and an explore-plan-implement-verify workflow governed by explicit human authorization.
- **SEF9-O9:** Use or critically evaluate an authentic, attributable AI coding proposal under a written plan, identifying the context provided and actions actually permitted or performed.
- **SEF9-O10:** Verify assistant-suggested code independently against written tests, diff review and failure scenarios, correcting substantive errors rather than accepting claimed success.
- **SEF9-O11:** Identify privacy, copyright/licensing, disclosure and provenance risks in assistant-supported work and accurately state unknowns without fabricating permission or attribution.
- **SEF9-O12:** Distinguish authorized task instructions from untrusted repository content and reject prompt-injection attempts, impersonated authority and unsupported tool directives.
- **SEF9-O13:** Enforce limited file, dependency, command, credential and network permissions; verify that untrusted suggestions do not disable checks or expand scope.
- **SEF9-O14:** Implement a bounded, tested CLI feature with correct normal/negative behavior, preserved existing data, and traceability from request through implementation and verification.
- **SEF9-O15:** Explain, modify, and test a reviewer-chosen implementation detail without using the assistant, demonstrating personal ownership of final engineering decisions.
- **SEF9-O16:** Deliver an independently reproducible, reviewed feature and technical defense with reliable artifact history, truthful AI-use evidence, and resolved acceptance criteria.

## Modules

### Module 1 — From Need to Work Item

#### Outcomes

- SEF9-O1
- SEF9-O2

#### Lessons

1. Course introduction: Professional Workflow & AI-Assisted Engineering
2. Users and personas
3. Writing user stories
4. Acceptance criteria and definition of done
5. Epics, stories, and tasks
6. Sizing work

*Optional practice:* Rewrite an ambiguous CSV-export request as two outcome-oriented stories and draft acceptance examples involving empty and malformed inputs.

### Module 2 — Planning & Tracking Work

#### Outcomes

- SEF9-O3
- SEF9-O4

#### Lessons

1. Repositories, README, and contribution guidelines
2. Issues and issue templates
3. Sub-issues, dependencies, and labels
4. Milestones and project boards
5. Linking pull requests to issues

*Optional practice:* Move locally versioned issue cards across realistic states and explain why a blocked item cannot be closed solely by changing its column.

### Module 3 — Recording Decisions

#### Outcomes

- SEF9-O5

#### Lessons

1. What counts as a decision worth recording
2. Context and problem statement
3. Options and drivers
4. Outcome, consequences, and confirmation
5. Status and superseding decisions

*Optional practice:* Write a small serializer choice record with alternatives, and an explicit follow-up record when evidence invalidates its original assumptions.

### Module 4 — Code Review as Practice

#### Outcomes

- SEF9-O6
- SEF9-O7

#### Lessons

1. The standard of a review
2. What reviewers look for
3. Writing small changes with good descriptions
4. Giving feedback
5. Responding to feedback

*Optional practice:* Review a deliberately flawed CSV diff and compare an evidence-backed code review with a vague approval.

### Module 5 — Working with AI Assistants

#### Outcomes

- SEF9-O8
- SEF9-O9

#### Lessons

1. How a coding assistant works
2. Giving context and instructions
3. Explore, plan, code, verify
4. Managing context
5. Permissions and what the assistant may do

*Optional practice:* Map assistant inputs to approved paths and permitted tool actions; inspect an authentic recorded proposal without claiming live interaction.

### Module 6 — Verifying & Governing AI-Generated Work

#### Outcomes

- SEF9-O10
- SEF9-O11

#### Lessons

1. Tests as the contract
2. Reading a generated diff critically
3. Common failure modes
4. Secrets and data exposure
5. Licensing, ownership, and disclosure
6. Staying able to explain your own code

*Optional practice:* Write independent tests for malformed CSV quoting, swallowed I/O errors, and unexpected output overwrite, then inspect a corrected diff.

### Module 7 — Trust Boundaries in AI-Assisted Work

#### Outcomes

- SEF9-O12
- SEF9-O13

#### Lessons

1. Assistant-generated output as a proposal
2. Untrusted repository instructions and prompt injection
3. Least-privilege tool permissions
4. Secret and data disclosure hazards
5. Reproduction and independent diff review
6. Documenting model limitations and human responsibility

*Optional practice:* Classify a malicious instruction in a synthetic README as untrusted data and reject a dependency or disabled-test change outside the plan.

### Module 8 — Feature Delivery Workflow

#### Outcomes

- SEF9-O14
- SEF9-O15
- SEF9-O16

#### Lessons

1. Feature request, stories and acceptance matrix
2. Traceable issues, decisions and review record
3. Scoped assistant proposal with truthful attribution
4. Tests-first implementation and failure recovery
5. Safe AI trust boundaries, provenance and documentation
6. Independent clean-checkout reproduction and unassisted technical defense

*Optional practice:* Rehearse a complete evidence handoff and an unassisted change with tests before independent review.

## Completion requirements

### Environment, authenticity and evaluation

Use a disposable local repository, synthetic task records, Python 3.11+ and a public standard-library test command. Hosted boards or pull requests are optional: versioned Markdown or JSON issue records, board snapshots and a locally reviewable patch meet the same *process* evidence criteria when no hosted account is available. A real **peer or designated independent reviewer** must still inspect the work and reproduce its final behavior; a fabricated reviewer name, simulated approval or mere self-review does not count.

The AI portion requires **an authentic assistant proposal** but does not require a paid or online assistant. An instructor may supply a genuine prerecorded assistant suggestion and associated context. Identify the provenance, tool/model if known, prompt boundaries and actual actions. A recorded proposal is not a live assistant run. Treat assistant suggestions, repository comments and external excerpts as untrusted inputs, never as authorization to access secrets, contact outside endpoints, disable quality checks or change unrelated code. Use only synthetic credentials and offline demonstrations of malicious suggestions; never perform exfiltration.

Reviewers evaluate observable tests, documentation and engineering judgment against each assessment's public criteria. Record actual tool output, accepted and rejected changes, reviewer comments and remedial work. A claimed green CI badge, issue state, AI confidence score, or rote reproduction of sample answers does not prove completion. Each required outcome is supported by independent evidence; failing correctness, trust-boundary, provenance or reproducibility criteria must be corrected before acceptance.

### Required summative assessments

- **SEF9-AS1** (required requirements, acceptance and traceable delivery plan)
  - Outcomes: SEF9-O1, SEF9-O2, SEF9-O3, SEF9-O4
  - Work: Use the synthetic request 'I need to export tasks to a CSV file so I can inspect them offline.' Identify at least two user contexts and write two outcome-focused stories, recording unknown requirements without presuming a UI button. Define ordinary, empty-dataset, commas/quotes/newline-in-field, invalid destination and noncorruption scenarios with observable results; distinguish each criterion from a definition of done. Build a local Markdown/JSON issue and project-board equivalent or an accessible hosted board, with IDs, owner, labels, milestone, status, one genuine dependency and linked implementation, testing and review tasks. Demonstrate a blocked task and scope change, then map every acceptance criterion to a check and an appropriate not-yet-done/verified status.
  - Criteria: Every user story identifies its user, need and value rather than prescribing internals; criteria have a falsifiable expected behavior, including failure status and preserved output where applicable. Issue IDs, dependencies, changed scope, linked review/diff and test evidence remain traceable. A completed board state is not falsely presented as a passing feature, and no dependent issue is marked verified before its tests and review are complete. A reviewer can challenge an ambiguous criterion and the learner revises it with measurable language.
  - Evidence: Original request, personas and assumptions, stories and acceptance matrix, initial/final locally versioned board, dependency and status records, planned tests and definition of done, reviewed clarification and its correction.

- **SEF9-AS2** (required decision records, alternatives and supersession)
  - Outcomes: SEF9-O2, SEF9-O5, SEF9-O16
  - Work: Write three focused engineering decision records in the same synthetic feature project: serializer choice (for example Python csv versus manual string joining), behavior on invalid output destinations, and a later revision that supersedes one accepted assumption. Each record names status, context, alternatives, drivers, choice, consequences, linked requirement/issue, verification plan and observed evidence. Preserve history and link the superseded and superseding records in both directions or through unambiguous identifiers. Have an independent reviewer reconstruct the rationale and suggest one missing counterexample or risk, then revise the explanatory record without silently erasing prior decisions.
  - Criteria: All three records can be understood without private chat history; at least one genuine supersession chain exposes old/new statuses and the reason for change. Rejected options and material trade-offs are explicit, not post-hoc fabricated consensus, and each decision identifies a falsifiable behavior check. Reviewer observations and responses are documented, and a changed decision does not silently rewrite an earlier approval. Requirement and test evidence remain linked to the decisions that affect them.
  - Evidence: Three versioned ADR-style records and statuses, alternative/risk tables, reciprocal supersession links, cited story and issue IDs, objective comparison fixture, independent review observations and response.

- **SEF9-AS3** (required focused peer code review and regression repair)
  - Outcomes: SEF9-O2, SEF9-O6, SEF9-O7, SEF9-O10
  - Work: Inspect a prepared small CSV-export patch with a realistic quoting, newlines, exit-status or partial-output flaw. Read the requirement and diff independently, reproduce the fault on a synthetic fixture, and write a structured review against a published correctness, safety, test, maintainability and scope checklist. Provide at least three evidence-backed actionable comments, including a concrete failing case. Prepare a bounded correction and regression test, produce a reviewable patch or PR-equivalent diff, and obtain a separate peer/designated-reviewer response. Resolve or justify rejection of substantive comments and rerun the relevant tests.
  - Criteria: The initial test exposes an actual defect and fails before the repair; the corrected implementation passes without hiding failures or changing unrelated behavior. Comments describe location, observable risk and an actionable change rather than vague disapproval. Changed files and commit/diff scope are transparent, reviewer feedback and replies are attributable, and claims of a hosted pull request or live review are made only if those events really occurred.
  - Evidence: Review standard/checklist, input patch and source revision, independent fixture and before/after outputs, three actionable comments, corrected diff, test logs, real reviewer response and final issue resolution record.

- **SEF9-AS4** (required constrained assistant proposal and human verification)
  - Outcomes: SEF9-O8, SEF9-O9, SEF9-O10, SEF9-O11, SEF9-O13
  - Work: Plan a bounded feature adjustment with an explore-plan-implement-verify document, explicitly stating approved files, allowed commands, input data, test oracles, maximum scope, and prohibited network, secret, dependency-installation or merge operations. Use an accessible coding assistant or an authentic provided recorded assistant response to propose a change. Record known model/tool identity, source/context supplied, proposal, actual tool actions (or explicitly no live tool actions), and attribution. Independently review the diff, accept/modify/reject suggestions with reasons, run predeclared and negative-case tests, and explain each retained line's behavior without querying the assistant.
  - Criteria: The assistant proposal is genuine and its provenance is not fabricated; prerecorded text is not presented as an interactive tool execution. The final diff is bounded by the authorized plan, tests and code observation substantiate every acceptance claim, and unsupported or invented APIs are rejected. The learner, not the assistant, owns implementation and success decisions. No real secret, private source, uncontrolled network access, unapproved dependency or broad permission is used; licensing and data-handling unknowns are disclosed rather than invented.
  - Evidence: Written plan and scope, sanitized proposal or recorded artifact with provenance, context/tool permissions, accepted-modified-rejected change log, source diff, observed test results, AI-use disclosure and independent explanation.

- **SEF9-AS5** (required generated-code defect audit and disclosure)
  - Outcomes: SEF9-O7, SEF9-O10, SEF9-O11, SEF9-O12, SEF9-O13
  - Work: Inspect a **genuine recorded or prepared assistant-proposed patch** for the synthetic CSV feature containing three identifiable defects: naive field/record escaping, swallowed I/O failure and unintended overwriting of prior valid output after invalid input. Write at least two independent tests from the acceptance criteria before accepting any proposal; demonstrate each seeded defect using a disposable fixture, then repair and run the cases again. Review changed files for invented APIs, dependency drift, disabled tests, privacy exposures and unsupported licensing claims. Document what provenance or redistribution questions cannot be verified and retain a sanitized audit of actual accepted changes.
  - Criteria: The original version demonstrably fails the claimed quote/newline round trip, error-propagation and prior-data preservation contracts; the repaired version demonstrably fixes the three failures with retained regressions. Tests exercise the actual program, not only mocked claims, and a final diff shows no unauthorized code, dependency or disabled-quality-check change. Attribution and privacy/licensing conclusions follow evidence, including explicit uncertainty, with no assumption that AI output is automatically licensed or publication-safe.
  - Evidence: Authentic or labeled recorded proposal, fixed synthetic fixtures and regression results before/after repair, actual CLI exit codes and output-byte comparison, provenance/permissions audit, change inventory and reviewer decision.

- **SEF9-AS6** (required untrusted context and least-privilege challenge)
  - Outcomes: SEF9-O8, SEF9-O10, SEF9-O11, SEF9-O12, SEF9-O13
  - Work: Inspect a **fully synthetic local** README or source comment that purports to override the user task and asks a coding agent to read a fake credential and send it to an external destination. Do not execute the instruction, use real credentials, or make a network request. Review a proposed patch that also introduces an unapproved dependency and disables a failing test. Define the authority order: the authorized user request and reviewed plan determine actions; repository content is untrusted task data. Identify the injected instructions and risky changes, reject them, restore tests, document the authorized diff and demonstrate an offline file inventory and test run respecting the original read/edit/command permissions.
  - Criteria: All unauthorized instructions, exfiltration directives, disabled checks and unapproved dependency additions are identified and rejected, with no actual secret read, credential exposure or outbound connection. The submitted diff and change/permission inventory remain within the authorized scope and required tests stay enabled. The learner explains why instructions embedded in code or documentation do not gain authority over the user plan and demonstrates a safe alternative rather than carrying out the malicious request.
  - Evidence: Synthetic suspicious text and prepared patch excerpts with line-level risk annotations, trust-boundary diagram, plan and permission matrix, final allowed-file and dependency inventory, non-network verification transcript, restored tests and sanitized incident note.

- **SEF9-AS7** (required integrated feature delivery and independent ownership defense)
  - Outcomes: SEF9-O1, SEF9-O2, SEF9-O3, SEF9-O4, SEF9-O5, SEF9-O6, SEF9-O7, SEF9-O8, SEF9-O9, SEF9-O10, SEF9-O11, SEF9-O12, SEF9-O13, SEF9-O14, SEF9-O15, SEF9-O16
  - Work: Deliver a CSV-export improvement to the SEF5 CLI or an equivalent learner-authored feature using linked stories, acceptance scenarios, issue/board progress, at least one verified decision record, tests written before accepting an authentic AI proposal, scoped permissions and accurate assistant attribution. Submit a focused locally reviewable PR-equivalent diff or real PR, obtain independent peer/designated-reviewer feedback, fix material findings and rerun tests from a clean disposable checkout. Cover header-only empty export, commas/quotes/newlines, invalid output paths and preservation of existing valid output, plus at least one deliberately seeded assistant or human defect and its repair. Provide an outcome-to-evidence matrix, README and retrospective. Finally, explain the code without the assistant and complete a small **reviewer-chosen modification without assistant help**, rerunning the appropriate tests and recording the result in a live, recorded, written or equivalent accessible review setting.
  - Criteria: All published user behaviors and failure contracts work from independent clean-start instructions, and tests fail for the original defect and pass after correction without hidden services or privileged actions. Each issue, decision, assistant suggestion, code revision, review comment and test result has honest provenance and a traceable role in acceptance. The unassisted modification is genuinely completed by the learner with demonstrable behavior and test evidence, not synthesized by an assistant; the reviewer can ask an unfamiliar boundary question and receive a justified answer. Unresolved correctness, authorization, provenance or privacy problems block completion.
  - Evidence: Versioned local repo or portable source, stories and checks, board and decision history, tests-first records, approved AI plan and attributable proposal, final focused diff, peer feedback and response, clean-checkout normal/negative outputs and unchanged-file checks, outcome map, independently observed unassisted change and test, and accessible technical defense.

### Completion decision

All **seven required assessments** must pass their published criteria, collectively demonstrating SEF9-O1 through SEF9-O16. A learner may reuse previously verified stories, issues, decisions, source, review evidence and assistant audits inside the integrated delivery, without adding hidden per-module test or lab quotas. Optional practice is formative. The unassisted modification and independent clean-checkout review are mandatory capabilities, but may be observed in accessible equivalent formats.

The reviewer records acceptance decisions, unresolved limitations and authentic supporting artifacts. No paid AI account, live external service, real private data, privileged action, or fabricated interaction is required. The course stays `draft`; successful structural checks do not establish `tested` or `verified` readiness under [Status Labels](../../spec/status-labels.md).
