# SEF9 — Professional Workflow & AI-Assisted Engineering

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF5](SEF5.md)
**Duration:** 10–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Learn how engineering teams turn requests into reviewable changes and evidence-backed delivery **with or without AI tools**. Write user stories and measurable acceptance criteria; evaluate ethical obligations and harm; manage dependencies; preserve decisions; handle software licensing and confidential data responsibly; communicate risk and change accessibly; and review focused patches. Use coding assistants as **constrained sources of proposals**, not authorities for implementation, tests or acceptance. Demonstrate professional judgment and ownership independently of any assistant.

**SEF5 is the only formal prerequisite.** SEF5 already establishes concrete module boundaries, dependency direction, interface contracts, quality evidence and accessible code review. SEF9 builds on that verified foundation to teach requirements, issue/decision tracking, change governance, responsible AI assistance and release communication, rather than silently treating software-design principles as unassessed new SEF9 entry requirements. [SEF4](SEF4.md) is recommended preparation, not an entry requirement. The reference project is the SEF5 tested command-line task manager or a comparable learner-owned Python 3.11+ program. A CSV-export improvement for synthetic task data provides a common example across modules, but an equivalent fully reproducible local feature can satisfy the same published criteria.

All required tasks can be completed offline using a disposable local Git repository, Python's standard library and versioned Markdown or JSON issue/board/PR artifacts. Hosted trackers and live assistants are optional. For AI-related work, use either an accessible assistant **or an authentic instructor-supplied recorded assistant proposal**; mark recorded and interactive usage accurately, including actual tools and models if known. Do not invent transcripts, prompts, tool calls, tests or live reviews. The learner must inspect, test and repair the suggested change independently. A peer or designated independent reviewer must reproduce the final feature and offer substantive feedback, even when collaboration artifacts are stored locally.

The original eight instructional topics are retained and ordered alongside **four distinct non-AI professional-practice modules**: ethical judgment, licensing and provenance, privacy/data stewardship, and accessible stakeholder communication. Twelve modules now teach 20 outcomes through **eight summative assessments**. The first seven assessments retain their original published Work, Criteria and Evidence unchanged; the eighth checks genuinely new professional obligations using the **same CSV feature and public synthetic case**. This does not create another capstone, a per-module quiz/lab quota, a paid account or a requirement to publish personal data.

The provisional allocation increases from six to **10–12 weeks** at 10–15 focused hours/week (roughly 100–180 hours, before remediation). This estimate recognizes the added professional practice and real independent review; it is not observed learner-time calibration. Course status remains `draft`.

**Public authored learning fixtures:** [SEF9 reproducible case pack](../../examples/sef9/README.md) provides a synthetic stakeholder brief, an actual ChatGPT-authored candidate proposal explicitly labeled with its limited provenance, an intentionally flawed runnable CSV exporter with independently failing tests, a trust-boundary injection document and a non-AI professional dilemma. They are examples, **not a completed learner submission or a replacement for independent real reviewer feedback**. Instructors may replace them with independently documented equivalent genuine fixtures; a purported transcript of a separate AI session must never be invented. The example tests are intentionally failing until the learner fixes the supplied implementation; they are separate from repository CI.

Optional professional reference material includes the [ACM Code of Ethics](https://www.acm.org/code-of-ethics), [SPDX handling of license identifiers and expressions](https://spdx.dev/learn/handling-license-info/), [NIST Privacy Framework](https://www.nist.gov/privacy-framework), and [W3C WCAG2ICT accessibility guidance for non-web software and documents](https://www.w3.org/TR/wcag2ict-22/). Such standards provide reasoning tools, **not** a claim that a license is legally cleared, a jurisdiction's privacy law is satisfied or a product has passed an accessibility certification.

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
- **SEF9-O17:** Recognize ethical and professional obligations independent of AI use, evaluate foreseeable harm, fairness, competence, honesty and conflicting stakeholder instructions, and document an evidence-based risk decision, escalation and mitigation without fabricating approval.
- **SEF9-O18:** Evaluate software and content provenance and licensing in a proposed change, distinguish copyright from permission, identify actual license evidence and attribution/notice obligations, and withhold or replace material whose redistribution rights or compatibility cannot be established.
- **SEF9-O19:** Apply privacy and confidentiality principles to a software feature through a bounded data inventory and lifecycle, data minimization, retention/deletion controls, safe logs, least exposure and a documented response to a proposed unauthorized disclosure.
- **SEF9-O20:** Prepare and evaluate inclusive, accessible engineering communication and CLI/review artifacts with navigable text, meaningful error/status descriptions, non-color-only information, respectful actionable feedback and a candid stakeholder handoff that conveys risks and limitations.

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

7. **Professional readiness** — Identify stakeholders and potentially harmed users, not just expected export functionality; begin a traceable risk list before implementation.

*Optional practice:* Rewrite an ambiguous CSV-export request as two outcome-oriented stories and draft acceptance examples involving empty and malformed inputs.

### Module 2 — Professional Ethics, Duty of Care and Honest Escalation

#### Outcomes

- SEF9-O1
- SEF9-O2
- SEF9-O4
- SEF9-O17

#### Lessons

1. **Professional responsibility without AI** — Explain that avoiding harm, competent work, honesty, confidentiality and fair treatment apply equally to hand-written and assistant-proposed changes.
2. **Stakeholders and foreseeable harm** — Identify affected users and potential failures of a CSV export, including lost output, misleading success, data exposure and inaccessible error reporting.
3. **Ethical decision method** — Separate observations, uncertainty, competing goals, affected people, duty of care, alternatives, severity and proportional risk treatment; avoid a checklist with no decision.
4. **Responsibility and competence** — Do not claim tests ran, reviews passed or legal compliance exists without evidence; ask for assistance when work exceeds actual expertise.
5. **Pressure to ship and dissent** — Respond to pressure to skip a failing regression with a factual risk note, proposed hold/mitigation and an appropriate escalation route without invented sign-off.
6. **Fairness and inclusive impacts** — Consider who cannot use visual-only review material, whose needs were not represented, and whether accessibility or language limits disadvantage affected users.
7. **Incident awareness and remediation** — Distinguish an observed privacy/security problem from a theoretical concern, record timing and containment options, and follow actual organizational reporting policy.
8. **Professional review and conflicts** — Make criticism evidence-based and respectful; disclose a conflict of interest or unknown requirement rather than hiding an uncomfortable trade-off.
9. **Decision record and follow-through** — Trace the chosen mitigation to an owner, deadline or next check, and clearly describe what remains blocked and why.

*Optional practice:* Use the synthetic stakeholder request to write a factual release-blocking note and a viable alternative that does not ignore the failed output-preservation test.

### Module 3 — Planning & Tracking Work

#### Outcomes

- SEF9-O3
- SEF9-O4

#### Lessons

1. Repositories, README, and contribution guidelines
2. Issues and issue templates
3. Sub-issues, dependencies, and labels
4. Milestones and project boards
5. Linking pull requests to issues

6. **Risk ownership and escalation** — Track a blocked privacy or licensing decision with a responsible owner and stop treating a status column as professional approval.

*Optional practice:* Move locally versioned issue cards across realistic states and explain why a blocked item cannot be closed solely by changing its column.

### Module 4 — Recording Decisions

#### Outcomes

- SEF9-O5

#### Lessons

1. What counts as a decision worth recording
2. Context and problem statement
3. Options and drivers
4. Outcome, consequences, and confirmation
5. Status and superseding decisions

6. **Decision provenance and rationale** — Connect professional/privacy/license decisions to real evidence and keep rejected alternatives discoverable.

*Optional practice:* Write a small serializer choice record with alternatives, and an explicit follow-up record when evidence invalidates its original assumptions.

### Module 5 — Software Licensing, Copyright and Provenance

#### Outcomes

- SEF9-O5
- SEF9-O11
- SEF9-O18

#### Lessons

1. **Copyright is distinct from license** — Explain why publicly accessible code is not automatically available for copying or redistribution and why a missing license is not permission.
2. **SPDX identifiers and expressions** — Read SPDX-License-Identifier fields and simple AND/OR/WITH expressions, distinguishing a machine-readable label from evidence that licensing actually applies.
3. **Sources and dependency inventory** — Record source URL or repository revision, file origin, version, copyright notice, retrieved license text and the actual use/distribution action.
4. **License obligations** — Identify possible attribution, notice, source-disclosure, modification and distribution conditions; state uncertainty rather than inventing legal clearance.
5. **Compatibility and distribution boundary** — Distinguish internal study, linking, copying and redistribution; compare possible conflicts while referring real legal interpretation to qualified review.
6. **Unknown or conflicting rights** — Quarantine an unlicensed snippet or dependency and replace it with a documented independent implementation or obtain authorization rather than assuming AI output is free to use.
7. **Generated and human-authored work** — Track provenance of suggested snippets and any original code regardless of whether an assistant, a colleague or a web page supplied them.
8. **License risk in a change diff** — Inspect import/dependency additions and copied content; require justified approved changes rather than hidden package additions.
9. **Release evidence** — Write a factual license/attribution note and explicit unresolved-risk status without falsely declaring a project legally compliant.

*Optional practice:* Review the synthetic third-party package manifest with missing license data and decide what evidence is needed before incorporating or distributing it.

### Module 6 — Privacy, Confidentiality and Data Stewardship

#### Outcomes

- SEF9-O2
- SEF9-O11
- SEF9-O19

#### Lessons

1. **Data inventory and purpose** — Map fields collected, read, exported, logged, retained and shared; state whether any field might identify a person even without a direct name.
2. **Minimization and purpose limitation** — Export only user-requested fields, avoid collecting hidden metadata and justify why an apparently convenient extra field is not needed.
3. **Authorized access and confidentiality** — Distinguish permission to read a local task from permission to publish it in a ticket, chat, screenshot or external model context.
4. **Consent, policy and law boundaries** — Identify actual contractual/legal obligations as jurisdiction- and organization-dependent; do not invent compliance or universal consent rules.
5. **Safe fixtures and sanitized reports** — Use wholly synthetic records and redact identifiers in test logs, errors and review artifacts; check whether a value can be re-identified.
6. **Retention and deletion** — Design limited storage and output file lifecycles, avoid stale temp-file residue and document deletion/cleanup for failed exports.
7. **Error and observability hygiene** — Report useful failures without dumping full records, access tokens, filesystem secrets or unexpected personal data into logs.
8. **Incident and escalation decision** — When a request would disclose protected information, refuse or hold the unsafe action, document facts and notify the appropriate authorized owner.
9. **Privacy test and threat model** — Write a basic data-flow table and test that malformed input, an invalid destination or a failed operation does not reveal or corrupt unrelated records.

*Optional practice:* Trace a fully synthetic CSV field from local task input to export and review log; identify what must not leave the user's machine.

### Module 7 — Accessible Communication and Inclusive Engineering Handoffs

#### Outcomes

- SEF9-O6
- SEF9-O7
- SEF9-O16
- SEF9-O20

#### Lessons

1. **Audience and communication purpose** — Differentiate an end-user release note, maintainer review request, stakeholder status update and an incident/escalation record.
2. **Semantic and navigable documents** — Use concise descriptive headings, list structure, meaningful links, ordered steps, file locations and plain-language explanations in Markdown or text.
3. **Avoid color-only or visual-only meaning** — Spell out severity, statuses and pass/fail results without relying on colors, screenshots or diagrams; add text-equivalent descriptions where diagrams help.
4. **CLI help and error clarity** — Supply textual command usage, deterministic exit codes, understandable error messages and an honest description of output formats.
5. **Keyboard and assistive technology awareness** — Explain that CLI/text-first artifacts may be more accessible but are not automatically WCAG-compliant; consider keyboard navigation, screen-reader usability and reader-tested evidence.
6. **Respectful and actionable feedback** — Write review findings with observed problem, reproduction, risk, expected behavior and an attainable improvement, avoiding dismissive personal comments.
7. **Accessible review equivalence** — Offer a structured plain-text evidence path rather than a mandatory hosted UI, visual PR screenshot or color-coded project board.
8. **Risk communication and release notes** — State implemented behavior, breaking changes, known issues, privacy/licensing limitations and required next actions without unverified claims.
9. **Independent readability check** — Have a reviewer reconstruct a decision and execute a CLI reproduction using only accessible text, then revise confusing headings or omissions.

*Optional practice:* Produce a one-page semantic Markdown release and review note for the same CSV feature, including a blocked privacy or licensing risk and actionable next steps.

### Module 8 — Code Review as Practice

#### Outcomes

- SEF9-O6
- SEF9-O7

#### Lessons

1. The standard of a review
2. What reviewers look for
3. Writing small changes with good descriptions
4. Giving feedback
5. Responding to feedback

6. **Communication and accessibility review** — Check whether a reviewer can reproduce the defect using text-only, descriptive steps rather than a color-coded screenshot.

*Optional practice:* Review a deliberately flawed CSV diff and compare an evidence-backed code review with a vague approval.

### Module 9 — Working with AI Assistants

#### Outcomes

- SEF9-O8
- SEF9-O9

#### Lessons

1. How a coding assistant works
2. Giving context and instructions
3. Explore, plan, code, verify
4. Managing context
5. Permissions and what the assistant may do

6. **AI-free professional obligations** — State which review, licensing, privacy and reporting decisions remain the human engineer's responsibility with no assistant present.

*Optional practice:* Map assistant inputs to approved paths and permitted tool actions; inspect an authentic recorded proposal without claiming live interaction.

### Module 10 — Verifying & Governing AI-Generated Work

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

7. **Reuse the public flawed proposal** — Start from the provided intentionally failing CSV case, document provenance, then independently derive what repair and tests are required.

*Optional practice:* Write independent tests for malformed CSV quoting, swallowed I/O errors, and unexpected output overwrite, then inspect a corrected diff.

### Module 11 — Trust Boundaries in AI-Assisted Work

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

7. **Untrusted policy or license claims** — Reject repository-supplied directives to claim legal clearance or leak user records, not only requests to run dangerous commands.

*Optional practice:* Classify a malicious instruction in a synthetic README as untrusted data and reject a dependency or disabled-test change outside the plan.

### Module 12 — Feature Delivery Workflow

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

7. **Non-AI ethics and accessibility handoff** — Carry the same feature's release-risk log, data map, rights inventory and accessible communications into AS8 without building a second project.

*Optional practice:* Rehearse a complete evidence handoff and an unassisted change with tests before independent review.

## Completion requirements

### Public example fixtures and assessment/evidence boundaries

The [SEF9 example pack](../../examples/sef9/README.md) offers a complete, **synthetic and reproducible** starting point for the previously required CSV review/repair and AI-trust exercises. It includes an assistant-authored candidate captured for this teaching example with honest provenance and **three known failing behaviors**. The source is deliberately unsafe for production and must be copied only into a disposable learner-owned directory. The provided red-team README is untrusted data; its instructions must **never** be obeyed. The sample stakeholder dilemma supports **SEF9-AS8** without accessing private records or declaring unknown license rights as cleared.

The existing assessments `SEF9-AS1`–`SEF9-AS7` keep all original Work, Criteria, Evidence and real independent-review expectations unchanged. A saved assistant-authored suggestion is not evidence that an assistant ran tools or that a learner completed an actual live AI session. The example's failing tests demonstrate the defect only; a learner must author the repair and show the subsequent passes. Teacher-provided examples **cannot count as authentic learner implementation, a live reviewer response or the final independent unassisted modification**.

| Professional capability | Instruction and example | Required summative evidence |
| --- | --- | --- |
| Ethical judgment and truthful reporting (`SEF9-O17`) | Module 2 and synthetic release-pressure scenario | `SEF9-AS8` documented stop/go, mitigation and escalation |
| Software licensing and provenance (`SEF9-O18`) | Module 5 and intentionally unknown-rights sample | `SEF9-AS8` source/right/notice inventory and defensible decision |
| Privacy and confidentiality (`SEF9-O19`) | Module 6 and synthetic record/report exposure dilemma | `SEF9-AS8` data lifecycle, safer alternative and retention/cleanup check |
| Inclusive accessible communication (`SEF9-O20`) | Module 7 and text-only issue/release handoff | `SEF9-AS8` navigable, actionable documentation with independent reader feedback |

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

- **SEF9-AS8** (required non-AI professional ethics, licensing, privacy and accessible communication)
  - Outcomes: SEF9-O2, SEF9-O4, SEF9-O5, SEF9-O6, SEF9-O7, SEF9-O11, SEF9-O16, SEF9-O17, SEF9-O18, SEF9-O19, SEF9-O20
  - Work: Work on the **same CSV-export feature and versioned issue/review trail** used in SEF9-AS1–AS7. Using the public, entirely synthetic [professional case](../../examples/sef9/professional-case.md) or an independently documented equivalent, respond **without relying on an AI suggestion** to an urgent stakeholder request to ship despite an observed data-loss defect, publish task records or raw logs in a public review channel, and incorporate an external code fragment with missing or conflicting licensing evidence. Identify affected stakeholders, foreseeable harm, evidence versus assumptions, actual decision authority and professional obligations; write a concise risk assessment with a concrete stop/mitigation/escalation decision, accountable owner and next check, without inventing consent, legal clearance, reviewer approval or a fixed jurisdiction's law. Build a source/dependency provenance and license inventory distinguishing copyright ownership, verified permission, attribution/notice requirements, intended distribution and **unknown** rights; either obtain attributable evidence or exclude/replace the questionable material. Produce a synthetic data-flow and lifecycle table covering CSV fields, output, temporary files, diagnostics, sharing permissions, retention and deletion; demonstrate one independently checked privacy-preserving failure/cleanup or redacted reporting case. Prepare an accessible Markdown or plain-text stakeholder update and focused code-review/release handoff with descriptive headings, source locations, plain-language risk/severity, expected/actual behavior, usable CLI help/error explanation and non-color-only status information; an optional screenshot or diagram may supplement but not replace this text. Have an independent reader/reviewer follow the update, identify a substantive ambiguity or challenge the decision, and record the correction and remaining limitations. Reuse existing source, tests and reviewer participation whenever legitimate; do **not** build a separate application or repeat the AI assessment.
  - Criteria: The professional decision addresses foreseeable harm and organizational authority with proportionate, timely mitigation and truthful reporting, including a credible response to pressure to bypass a failing check; unknowns remain labeled unknown and no simulated consent/approval is passed off as real. The rights inventory accurately separates provenance, copyright, SPDX expressions, actual retrieved license terms, compatible use/distribution and unresolved permissions; code with unverified redistribution rights is not silently included or declared safe. The data map has a defensible collection/purpose/exposure/retention/deletion boundary, avoids real personal data and records an actual synthetic test or controlled evidence that errors do not publish protected records. The written review and stakeholder handoff are navigable without color, hosted UI or images, include explicit reproduction and decisions, communicate access/error behavior respectfully and accurately, and record a genuine independent reader response and the learner's revision. The learner demonstrates that **these duties exist even when no AI assistant is involved** and can defend all decisions unaided. Unresolved material disclosure, license, data-loss, accessibility-of-evidence or dishonest-approval claims block passing.
  - Evidence: Existing feature revision and requirement references, public synthetic scenario and independently written impact/risk analysis, truthfully documented blocked/released decision and escalation trail, source/license/notice inventory with evidence and unresolved-rights treatment, synthetic data-flow and retention/disposal map, privacy-preserving error/log/cleanup fixture results, accessible Markdown/text stakeholder update and focused review/release notes, actual independent reader feedback and revised communication, and a technical defense of non-AI professional responsibility.

### Completion decision

All **eight required assessments** must pass their published criteria, collectively demonstrating SEF9-O1 through SEF9-O20. A learner may reuse previously verified stories, issues, decisions, source, review evidence and assistant audits inside the integrated delivery, without adding hidden per-module test or lab quotas. Optional practice is formative. The unassisted modification and independent clean-checkout review are mandatory capabilities, but may be observed in accessible equivalent formats.

The reviewer records acceptance decisions, unresolved limitations and authentic supporting artifacts. No paid AI account, live external service, real private data, privileged action, or fabricated interaction is required. The course stays `draft`; successful structural checks do not establish `tested` or `verified` readiness under [Status Labels](../../spec/status-labels.md).

### Revision history, stable-ID policy and learner evidence

This focused revision implements the **SEF9 follow-up** of [accepted RFC 0003](../../rfcs/0003-sef-academic-progression.md). The authoritative historical baseline is [SEF9 at OEE commit `8a0551c29b1639c4fb6cc336769c8a21d2c6e512`](https://github.com/0xbuffdev/open-engineering-education/blob/8a0551c29b1639c4fb6cc336769c8a21d2c6e512/curriculum/SEF/SEF9.md).

| Earlier learner evidence contract | Revised contract | Interpretation |
| --- | --- | --- |
| `SEF9-O1`–`SEF9-O16` | Same 16 IDs and **identical descriptions**, plus four newly distinct `SEF9-O17`–`SEF9-O20` | Original outcomes are not silently rewritten; new professional capabilities receive new IDs |
| `SEF9-AS1`–`SEF9-AS7` | Exactly unchanged published Work, Criteria, Evidence and reviewer conditions, plus a new `SEF9-AS8` | Previous assessed work remains attributable to its published course revision; new requirements are not retroactively inferred as passed |
| Eight teaching modules and six-week planning estimate | Twelve instructional modules, provisional 10–12 weeks | Sequence adds ethics, license, privacy and accessible communication without another independent application |
| Prepared patch and trust-boundary exercise prescribed without committed public sample | New reproducible [public SEF9 sample pack](../../examples/sef9/README.md) with explicit assistant-origin claims and deliberately failing tests | Examples prepare original assessments but cannot impersonate real student work or independent reviewer participation |

A learner's historical completion is neither automatically revoked nor declared to satisfy the new outcomes without actual reviewable evidence. This is a **material addition** of four professional competencies with a clearly new assessment ID, not a reinterpretation of older ones. No blanket assessment-count rule, mandatory proprietary AI tool, new formal prerequisite, global OEE course-format amendment or premature `tested`/ `verified` promotion is introduced.
