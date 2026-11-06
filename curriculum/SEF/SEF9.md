# SEF9 — Professional Workflow & AI-Assisted Engineering

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF5](SEF5.md)
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course teaches how professional teams turn needs into delivered software. Learners write user stories with acceptance criteria, plan and track work with issues and project boards, record design decisions, review code to a published standard, and use AI coding assistants deliberately: giving them context, constraining what they may do, and verifying everything they produce. AI assistants are used here as a graded engineering practice, with the learner remaining responsible for understanding and defending every change.

- [**SEF5 — Software Engineering Practice**](SEF5.md)
- [SEF4 — Data Structures & Algorithms](SEF4.md) is recommended preparation.

## Learning outcomes

By the end of the course, the learner will be able to:

- Turn a need into user stories with testable acceptance criteria and a clear definition of done.
- Plan and track a feature using issues, labels, milestones, dependencies, and a project board.
- Record a design decision so that a later reader can see the context, the options, the outcome, and how it was confirmed.
- Review a change against a published standard and write a change description that supports review.
- Work with an AI coding assistant using explicit context, a written plan, and limited permissions.
- Verify AI-generated work with tests, careful diff review, and checks for known failure modes.
- Document where an assistant was used and what the learner changed or rejected, and defend the final code without the assistant.
- Independently verify AI-assisted work, reject instructions from untrusted context and protect sensitive project data.

## Modules

### Module 1 — From Need to Work Item

#### Outcomes

- Write a user story from a persona, a need, and a purpose, without describing the implementation.
- Write acceptance criteria that can be checked, and state a definition of done.

#### Lessons

1. **Course introduction: Professional Workflow & AI-Assisted Engineering** — `lesson`

   Professional software is built by teams who agree on needs, track work, record decisions, review each other's changes, and increasingly use AI assistants. This course teaches those habits and the discipline needed to use assistants without surrendering understanding.
2. **Users and personas** — `lesson`
3. **Writing user stories** — `lesson`
4. **Acceptance criteria and definition of done** — `lesson`
5. **Epics, stories, and tasks** — `lesson`
6. **Sizing work** — `lesson`
7. **Stories and criteria** — `test`
8. **Turn a request into stories** — `lab`

### Module 2 — Planning & Tracking Work

#### Outcomes

- Break a feature into issues and sub-issues, with dependencies and labels.
- Organize issues on a project board and link pull requests to the issues they close.

#### Lessons

1. **Repositories, README, and contribution guidelines** — `lesson`
2. **Issues and issue templates** — `lesson`
3. **Sub-issues, dependencies, and labels** — `lesson`
4. **Milestones and project boards** — `lesson`
5. **Linking pull requests to issues** — `lesson`
6. **Planning and tracking** — `test`
7. **Set up tracking for a feature** — `lab`

### Module 3 — Recording Decisions

#### Outcomes

- Write a decision record with context, options, outcome, consequences, and a way to confirm it.
- Keep decision records in the repository with a status and links to superseding records.

#### Lessons

1. **What counts as a decision worth recording** — `lesson`
2. **Context and problem statement** — `lesson`
3. **Options and drivers** — `lesson`
4. **Outcome, consequences, and confirmation** — `lesson`
5. **Status and superseding decisions** — `lesson`
6. **Decision records** — `test`
7. **Write three decision records** — `lab`

### Module 4 — Code Review as Practice

#### Outcomes

- Review a change for design, correctness, tests, and clarity, and write feedback that is specific and actionable.
- Write a small, well-described change and respond to review comments.

#### Lessons

1. **The standard of a review** — `lesson`
2. **What reviewers look for** — `lesson`
3. **Writing small changes with good descriptions** — `lesson`
4. **Giving feedback** — `lesson`
5. **Responding to feedback** — `lesson`
6. **Review practice** — `test`
7. **Review and revise a pull request** — `lab`

### Module 5 — Working with AI Assistants

#### Outcomes

- Explain how an AI coding assistant works at the level of context, tools, and an action loop.
- Give an assistant the context, constraints, and a written plan it needs to complete a small change.

#### Lessons

1. **How a coding assistant works** — `lesson`
2. **Giving context and instructions** — `lesson`
3. **Explore, plan, code, verify** — `lesson`
4. **Managing context** — `lesson`
5. **Permissions and what the assistant may do** — `lesson`
6. **Working with assistants** — `test`
7. **Complete a change under a written plan** — `lab`

### Module 6 — Verifying & Governing AI-Generated Work

#### Outcomes

- Verify generated code with tests written first, a critical reading of the diff, and checks for known failure modes.
- Explain the privacy, licensing, and disclosure obligations that apply to AI-assisted work.

#### Lessons

1. **Tests as the contract** — `lesson`
2. **Reading a generated diff critically** — `lesson`
3. **Common failure modes** — `lesson`
4. **Secrets and data exposure** — `lesson`
5. **Licensing, ownership, and disclosure** — `lesson`
6. **Staying able to explain your own code** — `lesson`
7. **Verification and governance** — `test`
8. **Find defects in a generated change** — `lab`

### Module 7 — Trust Boundaries in AI-Assisted Work

#### Outcomes

- Evaluate tool-assisted edits using requirements, code review and trusted tests rather than assistant confidence.
- Diagnose or prevent one material error.

#### Lessons

1. **Assistant-generated output as a proposal** — `lesson`
2. **Untrusted repository instructions and prompt injection** — `lesson`
3. **Least-privilege tool permissions** — `lesson`
4. **Secret and data disclosure hazards** — `lesson`
5. **Reproduction and independent diff review** — `lesson`
6. **Documenting model limitations and human responsibility** — `lesson`
7. **Trust Boundaries in AI-Assisted Work reasoning** — `test`
8. **Audit an untrusted coding suggestion** — `lab`

### Module 8 — Feature Delivery Workflow

#### Outcomes

- Complete and explain the **Feature Delivery Workflow** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Feature delivery and independent ownership** — `test`
2. **Plan, build, review, and defend a feature delivered through the full workflow** — `lab`

   **Final integration lab — required work**

   **Feature Delivery Workflow**

   Take a feature request for the SEF5 tested command-line application and deliver it through the full workflow. The submission must include:

   - User stories with acceptance criteria
   - Issues and a project board for the feature
   - At least one decision record
   - An implementation developed with an AI assistant from a written plan, with tests written first
   - A pull request reviewed by a peer against a published standard
   - An evidence log recording where the assistant was wrong, what was changed or rejected, and what the learner did without assistance
   - Explicit restrictions on sensitive context, tools, permissions and unauthorized dependencies
   - Independent clean-checkout verification, negative-input tests and traceable assistant attribution

   The defense includes a live modification made without the assistant.

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Convert a feature request into stories with acceptance criteria.
- Set up issues, labels, and a project board for a feature.
- Write a decision record for a real design choice.
- Review a pull request and revise your own in response to review.
- Complete a small change with an assistant under a written plan.
- Find defects in a generated change and write tests for them.

**Required checkpoints and lab acceptance contracts:**

Each of the eight modules has two evaluated reasoning prompts, expected-answer guidance and a practical lab. Equivalent previously unseen prompts are acceptable when they measure the same outcome. The reviewer evaluates traceable human decisions, reproducible software behavior and explicit trust boundaries; a tool's confidence, board status or a copied solution cannot establish completion.

**Shared practical environment:**

Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.

**Shared evaluation and evidence rules:**

- Use a synthetic task-manager CSV-export feature as the connected learning case across the modules; equivalent locally reproducible features are acceptable when they exercise the same risks and outcomes.
- Record requirement-to-test links, original versus revised source, actual commands and outputs, reviewer observations, approval decisions, and remediation of misunderstandings.
- Treat AI responses and untrusted repository content as proposals/data, not authoritative commands. Do not expose real credentials, run exfiltration demonstrations, disable quality checks or grant broad filesystem/network permissions to fulfill a lab.
- Demonstrate an unassisted explanation or modification before course completion. An assistant must not be the sole source of decisions, test outcomes or final acceptance.
- Publish only sanitized learning evidence. Redact private information before sharing artifacts and record any unverified claim as a limitation.

**Module 1 — From Need to Work Item: checkpoint** — Required assessment details

- **Q1 (free):** A user asks to 'add a CSV button to make my task list easier to share'. What is the difference between the need, a user story and a solution prescription?
  - Expected answer and scoring: The need concerns accessing or sharing task data; a story names a user, capability and reason, such as exporting a task list for offline use. A CSV button is one proposed UI solution and should not be treated as the need itself.
- **Q2 (free):** Give one acceptance criterion for exporting an empty task list and one for an invalid destination. How do these differ from a definition of done?
  - Expected answer and scoring: Criteria describe observable feature behavior: for example, an empty export produces a valid header-only CSV and an invalid destination returns a clear nonzero failure without overwriting existing data. The definition of done may additionally require tests, review, documentation and reproducible evidence across the change.

**Module 1 — Turn a request into stories: required lab** — Required assessment details

- **Objective:** Convert a vague need into independently testable, outcome-focused stories rather than a list of preferred implementation details.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Use this fixed simulated request for an existing SEF5-tested task CLI: 'I need to export tasks to a CSV file so I can inspect them offline.' Work only with synthetic local task records.
  2. Identify at least two user personas/contexts, write two outcome-focused stories and record assumptions or questions not answered by the request.
  3. Specify acceptance scenarios covering ordinary tasks, empty data, commas/quotes/newlines in fields and an invalid output path. Include preconditions, action and observable outcome for each.
  4. Distinguish a feature epic, user stories and implementation tasks. Select one independently deliverable story and explain why it is first.
  5. Create a traceability table mapping each accepted criterion to a manual or automated check; have a reviewer point out one ambiguous criterion and refine it.
- **Expected result:** Stories describe user value without prescribing internals; criteria cover valid and failure behaviors with tests that can clearly pass or fail.
- **Verification:** A reviewer receives the same request, identifies the scenarios and can distinguish which outputs and errors satisfy each criterion without guessing unspecified requirements.
- **Evidence:** Request, personas, stories, assumptions, criteria-to-checks matrix, refined ambiguous criterion and reviewer note.
- **Failure analysis:** Explain a criterion that merely says 'works', an implementation detail mistaken for user value or an omitted failure scenario.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 2 — Planning & Tracking Work: checkpoint** — Required assessment details

- **Q1 (free):** A story requires implementing CSV serialization and adding tests before merging. How would you express the work-item dependency and acceptance link?
  - Expected answer and scoring: Create a story with a user-level acceptance contract and associated implementation/test tasks. Identify the dependent work explicitly and link each task/PR to the relevant acceptance criterion; avoid declaring the story complete when code exists but tests or review are unfinished.
- **Q2 (free):** What changes between a board column labelled 'Done' and a verified feature?
  - Expected answer and scoring: A board state is coordination metadata, not evidence of correctness. Done must be justified by defined acceptance checks, a reviewed change, and retained test or reproduction evidence, not just moving a card.

**Module 2 — Set up tracking for a feature: required lab** — Required assessment details

- **Objective:** Plan a bounded feature through linked, traceable work items and a reviewable workflow.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Create an issue tracker in a local Markdown/JSON fixture or a free accessible hosted project board, with equivalent fields for ID, description, owner, label, milestone, status and dependencies.
  2. Import the two Module 1 stories and break the first one into an implementation task, a test task and a documentation/review task. Express at least one real dependency.
  3. Create board columns such as Backlog, Ready, In progress, In review and Done; show initial and updated item positions.
  4. Link a simulated or real pull-request record to its issue and describe how the reviewed commit satisfies the story acceptance criteria.
  5. Test a blocked task and a request for scope expansion; explain how dependency state and a changed requirement are recorded without silently closing incomplete work.
- **Expected result:** Every story links to acceptance evidence, each task has a traceable ID and state, and a blocked work item cannot be mistaken for verified completion.
- **Verification:** Review the issue/board artifacts and links from story to task to change/test; compare before and after status of the blocked item.
- **Evidence:** Versioned issue records, local board snapshot or export, dependency map, status transitions, simulated PR reference and scope-decision note.
- **Failure analysis:** Explain orphaned tasks, treating board status as proof, failing to record a dependency or silently increasing scope.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 3 — Recording Decisions: checkpoint** — Required assessment details

- **Q1 (free):** A team chooses the Python csv module over manually concatenating strings for task export. What should an engineering decision record capture beyond the chosen option?
  - Expected answer and scoring: State the context and requirements, viable alternatives, decision drivers, the selected option, expected consequences, verification method, status, date and links to affected work. The reason should address quoting, embedded newlines and maintenance, not only assert that a library is better.
- **Q2 (free):** What should happen to an accepted record when new evidence leads to a different decision?
  - Expected answer and scoring: Retain the historical record with a superseded status and a link to the newer record; the successor explains the new evidence and implications. Do not silently rewrite the earlier rationale as if the original decision never occurred.

**Module 3 — Write three decision records: required lab** — Required assessment details

- **Objective:** Document decisions with alternatives, tradeoffs, validation, status changes and supersession traceability.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Write three small decision records for the same synthetic task-export project: data format/serializer, output-failure behavior and a later change of one design assumption.
  2. Include status, context, options, drivers, selected approach, consequences, evidence and affected issue IDs in each.
  3. Explicitly supersede one earlier decision and provide reciprocal links or identifiers that let readers follow the change of direction.
  4. Design a small, falsifiable check for each decision, including one failure-case check where a rejected alternative could have violated a requirement.
  5. Ask an independent reviewer to reconstruct why the choice was made and whether the evidence supports it; revise unclear language without erasing history.
- **Expected result:** Three individually understandable records exist; one has a valid successor chain, and their consequences can be checked against specified behavior.
- **Verification:** Inspect statuses and links, reproduce at least one stated comparison and confirm no record relies on knowledge held only in chat.
- **Evidence:** Three dated/status-bearing records, options matrix, verification fixtures, links to work items, reviewer feedback and corrected rationale.
- **Failure analysis:** Explain decisions without alternatives, a claimed benefit without tests or changing a decision without recording supersession.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 4 — Code Review as Practice: checkpoint** — Required assessment details

- **Q1 (free):** A pull request changes CSV export, refactors unrelated storage classes and upgrades dependencies. What should a reviewer ask and why?
  - Expected answer and scoring: Ask to separate unrelated refactoring and dependency upgrades unless the coupling is justified, then assess the feature against its acceptance contract. A focused diff is easier to verify, review and revert.
- **Q2 (free):** A reviewer writes 'this is bad' on a faulty escaping routine. Rewrite the feedback so it is actionable.
  - Expected answer and scoring: Name the failing behavior and a minimal fixture, e.g., a task title containing a comma or quote produces an invalid CSV column count; propose a test and use a standards-compliant CSV serializer. Feedback should identify impact and verification, not attack the author.

**Module 4 — Review and revise a pull request: required lab** — Required assessment details

- **Objective:** Evaluate a bounded change objectively, give specific review feedback and demonstrate a corrected revision.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Use a deliberately prepared small patch to the task CLI's export logic containing a realistic CSV-quoting or exit-status defect. All data is synthetic.
  2. Read the issue, acceptance criteria and diff independently. Reproduce the defect with a minimal fixture and record the command/output mismatch.
  3. Write a structured review covering correctness, security/data handling, tests, maintainability and scope; include at least three specific comments with evidence.
  4. Prepare a focused repair in a separate branch or proposed patch. Add or update a regression test and document the changed behavior.
  5. Exchange feedback with a peer or designated independent reviewer, record resolution of substantive comments, and show the final reviewed diff with passing tests.
- **Expected result:** Review evidence identifies the seeded defect and the revised patch passes its regression test without unrelated changes.
- **Verification:** Compare original failing fixture with revised results, inspect actionable comments and reviewer sign-off or independent review notes.
- **Evidence:** Initial and corrected diffs, issue and PR-style summary, review comments, fixture outputs, test logs and response history.
- **Failure analysis:** Explain superficial approval, a personal/nonactionable comment, a repair that hides the defect or unreviewed scope expansion.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 5 — Working with AI Assistants: checkpoint** — Required assessment details

- **Q1 (free):** Does an AI coding assistant necessarily see every repository file or have permission to execute commands? What determines its working context?
  - Expected answer and scoring: No. Visibility and tool access depend on supplied context, product capabilities, environment and granted permissions. Distinguish text the learner provides from files a connected tool can read; inspect permissions rather than presuming access.
- **Q2 (free):** An assistant says it finished and all tests pass, but no test output is provided. Is that sufficient to merge?
  - Expected answer and scoring: No. Treat the message as a proposal. Inspect the actual diff, reproduce documented tests in the learner's environment, compare against acceptance criteria and withhold approval until evidence exists.

**Module 5 — Complete a change under a written plan: required lab** — Required assessment details

- **Objective:** Use a coding assistant under an explicit plan and limited permissions while retaining responsibility for each change and its verification.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Choose one small, non-sensitive feature change to the synthetic task CLI, such as validating or formatting its CSV export. Define a written requirement, non-goals, acceptance tests and maximum edit scope.
  2. Write an explore-plan-implement-verify plan, including which paths may be read or changed and which commands may run. Do not authorize secrets access, network calls, dependency installation or merging.
  3. Use an accessible coding assistant or an instructor-provided authentic recorded assistant response to propose the change. Record the selected model/tool if known, relevant synthetic context, prompt/response and any tool actions. Do not fabricate the assistant transcript or imply that a prerecorded proposal was an interactive session.
  4. Review and edit the proposal manually, rejecting anything outside the allowed scope. Record each accepted, modified or rejected suggestion and a reason.
  5. Run the predeclared tests locally with the exact source revision, add a negative-case test, and explain the final implementation to another person without querying the assistant.
- **Expected result:** The final change meets a concrete acceptance contract and stays within scope; the evidence distinguishes the assistant's suggestions from the learner's verified implementation.
- **Verification:** Compare plan, assistant proposal, final diff and test outputs; check no unapproved file, command, credential or network operation was required.
- **Evidence:** Written plan and permission boundary, sanitized authentic assistant artifact, accepted/rejected decision log, source diff, test results and independent explanation.
- **Failure analysis:** Explain hallucinated APIs, misunderstood constraints, undocumented assistant actions or treating claimed success as observed verification.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 6 — Verifying & Governing AI-Generated Work: checkpoint** — Required assessment details

- **Q1 (free):** An assistant proposes replacing Python csv.writer with naive string joining and claims that passing one simple test proves the export is correct. What independent test exposes the mistake?
  - Expected answer and scoring: Write a fixture with commas, quotes and embedded newlines in task fields, then parse the output with Python's csv reader and assert correct field round-trip. A single simple line does not cover CSV record-encoding requirements.
- **Q2 (free):** Can a learner assume every AI-generated snippet is license-free, safe to publish and free of private data?
  - Expected answer and scoring: No. Assess provenance and applicable project/license policy, review for copied or sensitive material, and disclose relevant AI assistance according to the applicable rules. Avoid making unsupported blanket legal claims about authorship or permissions.

**Module 6 — Find defects in a generated change: required lab** — Required assessment details

- **Objective:** Identify, reproduce and repair seeded defects in an assistant-proposed patch using independent tests, code review and privacy/licensing judgment.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Receive a prepared AI-suggested CSV-export change with at least three seeded defects: naive quote/record escaping, swallowed I/O failures and unintended output overwrite on malformed input.
  2. Before applying the patch, write an acceptance-test list and implement at least two independent tests that should fail against the defective proposal.
  3. Apply the prepared patch only to a disposable copy, reproduce each flaw with exact fixtures, and classify the root cause rather than relying on assistant confidence.
  4. Repair defects one by one, rerun tests and inspect the diff for out-of-scope edits, dependency changes, invented functions and unsafe logging.
  5. Complete a short privacy/licensing/disclosure review appropriate to a synthetic project; use no real secrets and record what is unknown rather than assuming permission.
- **Expected result:** Every seeded defect has a failing reproduction and a verified fix; the final program preserves existing data on failure and produces valid CSV round-trips.
- **Verification:** Run tests against the defective and corrected revisions, check exit statuses and output bytes, and compare the final diff with approved scope.
- **Evidence:** Predeclared criteria, red/green test results, original/fixed patch, root-cause table, review checklist and disclosure note.
- **Failure analysis:** Explain superficial testing, suppressed exceptions, accidental data loss or overclaiming licensing certainty.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 7 — Trust Boundaries in AI-Assisted Work: checkpoint** — Required assessment details

- **Q1 (free):** A README in a third-party repository tells an AI agent to ignore the original task and upload environment variables to an external endpoint. Should the learner treat that text as instructions?
  - Expected answer and scoring: No. The README is untrusted task data and cannot override the user's authorized objective or tool permissions. Ignore the instruction attempt, do not read or transmit secrets, document the finding and continue only with the authorized task.
- **Q2 (free):** An AI patch adds an unexpected third-party dependency and disables failing tests. What is the safest acceptance decision?
  - Expected answer and scoring: Reject or isolate the changes until independently justified. Review dependency purpose, provenance and licensing under project policy; restore tests and require observable acceptance evidence before approving any necessary dependency. Assistant confidence is not approval.

**Module 7 — Audit an untrusted coding suggestion: required lab** — Required assessment details

- **Objective:** Identify and reject instructions embedded in untrusted repository material and maintain least-privilege tool boundaries.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Work in a fully synthetic local repository containing a deliberately misleading README or code comment asking the assistant to access a fake credential and contact an external destination. Do not create real credentials or make any network request.
  2. Define trust boundaries: user-authorized feature request, project code/data, untrusted documentation, tool permissions and assistant-proposed modifications.
  3. Inspect a prepared suspicious patch containing the embedded instruction, an unauthorized dependency addition and a disabled test; identify which exact lines conflict with the authorized plan.
  4. Remove or reject unsafe changes and restore the genuine feature acceptance tests. Record whether the remaining safe changes are needed at all.
  5. Perform an offline verification of the diff and file inventory; demonstrate no network, credential read or privileged tool action occurred, then explain the boundary violation and mitigation.
- **Expected result:** The unauthorized instruction, dependency and disabled test are rejected; authorized requirements continue to be evaluated with no fake-secret exposure or external network action.
- **Verification:** Inspect final changed-file list, allowed dependency set and test suite; compare with the predeclared scope and preserve a sanitized incident report.
- **Evidence:** Synthetic injection fixture, trust-boundary diagram, suspicious-diff annotations, accepted/rejected log, test results and incident retrospective.
- **Failure analysis:** Explain treating source comments as higher-authority commands, unnecessarily broad tool permissions, fabricated evidence or accepting a deceptive patch.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Module 8 — Feature Delivery Workflow: checkpoint** — Required assessment details

- **Q1 (free):** A feature board says Done and the assistant claims it passed tests, but a reviewer finds a failing CSV quote round-trip. Has the feature met its definition of done?
  - Expected answer and scoring: No. The failing acceptance criterion takes priority over board status or assistant claims. Correct the defect, rerun the relevant tests, update review and evidence, and only then mark the work accepted.
- **Q2 (free):** The learner cannot explain a line generated by an assistant during an unassisted defense. What should the reviewer conclude?
  - Expected answer and scoring: Understanding has not yet been demonstrated. Require the learner to reason through, test and explain the code or revise it to something they can defend, then reassess. A working artifact alone does not satisfy this course's independent-ownership outcome.

**Module 8 — Feature Delivery Workflow: required lab** — Required assessment details

- **Objective:** Deliver and independently defend a small feature from user need to reviewed implementation using documented, bounded AI assistance.
- **Prerequisites:** Complete the corresponding module lessons and conceptual checkpoint; use only approved, previously verified project artifacts as inputs.
- **Environment:** Use the existing SEF5-tested command-line application or a clean local equivalent with a documented Python 3.11+ standard-library test runner, a disposable repository and synthetic task data. All required issue/board and PR workflows may use versioned local artifacts when a hosted account is unavailable; a free hosted alternative is optional. No paid AI service, external network access, organization credential, installation permission or real private source data is required. For AI exercises, use an accessible assistant or an authentic instructor-supplied recorded assistant output; mark recorded versus interactive use accurately. Record actual model/tool identity when known, input context, outputs and permitted actions; do not claim deterministic AI responses. Every final accepted code result must be independently reproducible from fixed source and test fixtures.
- **Procedure:**
  1. Select a bounded CSV-export improvement to the existing SEF5-tested CLI. Use synthetic tasks and retain explicit story acceptance criteria including empty data, escaping, invalid destination and noncorruption of existing output.
  2. Create linked story and task records, dependencies and an inspectable project board (local versioned equivalent or hosted board). Write at least one decision record with alternatives and verification.
  3. Write acceptance/regression tests before adopting an assistant proposal. Create a written plan with allowed paths and explicit restrictions on tools, data and network access.
  4. Use an actual, attributable assistant proposal (from an accessible tool or authentic provided recorded response), log relevant context and suggested changes, then inspect and constrain the final implementation.
  5. Prepare a focused pull request or local PR-equivalent diff, obtain independent peer/designated-reviewer comments and resolve substantive findings with evidence.
  6. Run clean-checkout tests and a synthetic negative case, verify there are no unapproved dependencies, secret exposures or disabled checks, and record the before/after results.
  7. Perform an unassisted defense explaining acceptance scenarios, architecture, code paths, tests, rejected assistant advice and relevant licensing/privacy constraints. Complete a small reviewer-chosen modification without assistant help and test it.
  8. Deliver an outcomes-to-evidence matrix, clear operating instructions and a retrospective identifying at least one actual incorrect suggestion or mistaken assumption and its corrected result.
- **Expected result:** The feature meets all declared user-visible criteria; tracked decisions and review are traceable; the learner independently reproduces, explains and changes the resulting code.
- **Verification:** A reviewer uses the documented clean-checkout instructions to run normal and failure cases, inspect the accepted diff and assistant attribution, and observe the unassisted modification and retest.
- **Evidence:** Stories, tracker/board, ADR, written plan, synthetic assistant artifact, accepted/rejected log, code, tests, review notes, defense record and retrospective.
- **Failure analysis:** Explain a missed requirement, invented assistant success claim, unauthorized change, swallowed error or inability to defend an implementation decision.
- **Acceptance:** All specified deliverables and normal/negative cases are verified, decisions and assistant contributions are accurately attributed, and an independent reviewer can reproduce the relevant evidence. An unapproved tool action, unresolved acceptance failure or inability to explain the work blocks completion.

**Exit demonstration:**

The learner can take a need through stories, tracked work, recorded decisions, and a reviewed change, use an assistant without surrendering understanding, and explain and modify every line delivered.
