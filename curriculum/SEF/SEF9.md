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

Instruction is derived from actual professional decisions: stakeholder acceptance; traceable work and engineering decisions; ethical judgment; licensing and provenance; privacy stewardship; accessible, evidence-based review; authorized and attributable AI proposals; independent verification and repair of proposed code; and one genuine feature handoff. The **eight published summative assessments** measure the existing twenty outcomes, including the four distinct non-AI professional obligations in AS8, using one synthetic CSV feature and a documented scenario. First taught mechanisms are not repeated as disconnected introductions, and no module or lesson count is prescribed. This does not create another capstone, a per-module quiz/lab quota, a paid account or a requirement to publish personal data.

The provisional allocation increases from six to **10–12 weeks** at 10–15 focused hours/week (roughly 100–180 hours, before remediation). This estimate recognizes the added professional practice and real independent review; it is not observed learner-time calibration. Course status remains `draft`.

**Practice materials:** Learners or instructors prepare a synthetic stakeholder brief, a deliberately defective CSV exporter with independently written failing tests, a genuine and attributable assistant proposal, an untrusted repository-text example, and a professional dilemma. Use a disposable local repository and synthetic data. These materials support practice, but they are not completed learner work or a substitute for genuine independent review. Record the provenance of any assistant proposal: do not invent an AI conversation, model execution, test result or reviewer approval.

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

### Module 1 — Stakeholder Needs, Acceptance and Independent Evidence

#### Outcomes

- SEF9-O1
- SEF9-O2

#### Lessons

1. **Professional delivery begins with a real need** — Use the SEF5 tested CLI as the starting point, distinguish the user's desired CSV export from a prescribed interface, and identify where the resulting evidence will be examined by another engineer.
2. **Users, stakeholders and underserved cases** — Identify at least two user contexts and affected people, including users who cannot rely on a visual review tool or whose records might be exposed by an export.
3. **Outcome-oriented user stories** — Write statements of user, capability and value without silently choosing a particular UI or implementation, and mark uncertain assumptions for actual stakeholder clarification.
4. **Separate outcomes from implementation constraints** — Translate the request into a documented permitted scope and distinguish genuine user-visible behavior from an internal task, Git action or preferred library.
5. **Acceptance for correct CSV and empty state** — Specify observable output bytes, headers, quoting, embedded commas/quotes/newlines and empty-dataset behavior with independently derived expected results.
6. **Failure acceptance and noncorruption** — Specify invalid destination, malformed input, write failure and preservation of existing valid output, including exit/status expectations that can be falsified.
7. **Definition of done versus feature acceptance** — Distinguish confirmed behavior from review, documentation and quality-gate process obligations; a completed checklist or issue status is not a substitute for passing criteria.
8. **An ambiguous requirement challenged and revised** — Have another reader question a genuine unknown, write the clarification and connect the updated acceptance criterion to a negative test without inventing stakeholder approval.

*Optional practice:* Draft two CSV export user stories and an acceptance matrix for empty input, embedded quotes and an invalid output path; independently derive the output bytes.

### Module 2 — Traceable Work, Dependencies and Decision History

#### Outcomes

- SEF9-O2
- SEF9-O3
- SEF9-O4
- SEF9-O5

#### Lessons

1. **Repository and contribution contract** — Create a readable local Markdown/JSON issue board and README for the learner-owned CLI, assigning stable IDs that are independently traceable to source and test revisions.
2. **Decompose one bounded change** — Split the feature into linked implementation, test, documentation and review work only where dependencies or observable handoffs genuinely require separate tasks.
3. **Meaningful states and accountable owners** — Distinguish not-started, blocked, in-review and verified states, assign responsible owners honestly and prevent a board move from impersonating independently accepted behavior.
4. **Dependencies and a justified milestone** — Record an actual blocker, order the prerequisite tasks and explain a milestone boundary without multiplying epics or tickets to satisfy a template.
5. **Scope change without rewriting history** — Record a new stakeholder constraint, update impacted issues and acceptance links, and preserve the earlier scope and rationale in version history.
6. **Decision records worth keeping** — Choose a material serializer or error-handling decision and document context, affected user behavior, realistic alternatives and the drivers that distinguish them.
7. **Consequences and observable decision checks** — Link a choice to actual fixtures, the failure it avoids, measurable trade-offs and unresolved constraints, rather than treating an ADR as a generic design essay.
8. **Supersession and contradictory evidence** — Preserve an earlier accepted record while explicitly superseding it with new evidence; maintain reviewable old/new statuses and links instead of retroactive silent edits.
9. **Independent rationale reconstruction** — Ask a reader to reconstruct a decision and challenge a missing counterexample, record the actual response and make a bounded revision tied to an issue and test.

*Optional practice:* Plan three linked decisions for the same CSV feature: serializer, invalid-output policy and a later superseding decision triggered by a failing fixture.

### Module 3 — Professional Responsibility, Foreseeable Harm and Escalation

#### Outcomes

- SEF9-O4
- SEF9-O17

#### Lessons

1. **Ethical duty exists without AI** — Apply responsibility, honesty, competence, confidentiality and fair treatment to handwritten code as well as assistant-suggested changes; distinguish personal judgment from claimed organizational authorization.
2. **Affected people and concrete harm** — Map a CSV loss/overwrite failure, raw-log disclosure and unusable error reporting to users, severity and plausible consequences instead of asserting abstract policy compliance.
3. **Evidence, uncertainty and competing pressures** — Separate observed failing tests and verified facts from uncertain requirements, organizational constraints and the interests of people who bear the consequences.
4. **Proportionate risk and alternatives** — Evaluate a release hold, limited mitigation, safe rollback or reduced scope, explicitly stating what remains untested and why risk cannot be erased by a green status badge.
5. **Responding to pressure to bypass a gate** — Write a factual response to a manager asking to ship with known data loss, define a stop/mitigation/escalation route and avoid claiming an approver consented when they did not.
6. **Inclusive impacts and conflicts of interest** — Identify whose needs are absent, accessibility barriers and a conflict that could bias a reviewer; communicate disagreement respectfully with evidence.
7. **Incident recognition versus hypothetical risk** — Distinguish an observed disclosure from a possible threat, document immediate non-invasive containment options and route actual response through the organization's authorized process.
8. **Traceable professional decision and follow-up** — Record an owner, next check, open uncertainty and defensible decision that can be revisited independently, without creating fictitious approval or a second application.

*Optional practice:* Use the fully synthetic professional case to write a documented stop/go risk decision and a concrete safe alternative that addresses the failed data-preservation test.

### Module 4 — Copyright, Licensing and Evidence of Permission

#### Outcomes

- SEF9-O5
- SEF9-O11
- SEF9-O18

#### Lessons

1. **Copyright is not redistribution permission** — Distinguish author/owner, publication, copyright and an actual license grant, and explain why an online snippet or assistant output is not automatically permitted for copying.
2. **A source and dependency inventory** — Record file or package origin, source revision, retrieved license evidence, intended use and distribution destination for a proposed imported CSV helper.
3. **SPDX expressions and their actual scope** — Interpret a real SPDX identifier and simple AND/OR/WITH expression, distinguishing a label from retrieved permission and a project license from file-level exceptions.
4. **Obligations and incomplete rights** — Identify relevant notice, attribution, modified-source or redistribution conditions only when evidence supports them, marking legal interpretation and missing texts as unresolved.
5. **Use boundary and potential conflict** — Distinguish private experiment, copied code, linked dependency and redistributed artifact, and identify an apparent incompatibility without claiming lawyer-certified clearance.
6. **Unverified source and assistant provenance** — Assess code from an unattributed snippet, a recorded assistant proposal or a real repository, documenting what actual creator, model, license and permission facts are known.
7. **Quarantine, replace or seek authority** — Reject an uncertain dependency or fragment, select a documented original/appropriately licensed alternative or request authorized review rather than fabricating permission.
8. **Source-rights review and handoff** — Include the verified source/notice inventory and open questions in the focused review/release evidence; ensure a dependency does not enter the final diff unnoticed.

*Optional practice:* Inspect a sample package with absent or conflicting license evidence and write the minimum documentation needed before approving its distribution.

### Module 5 — Privacy, Confidentiality and Controlled Data Lifecycles

#### Outcomes

- SEF9-O2
- SEF9-O11
- SEF9-O19

#### Lessons

1. **Data map and purpose before export** — Trace task fields, CSV output, temporary files, logs, review artifacts and potential external assistant contexts, recognizing quasi-identifiers as well as explicit names.
2. **Minimization and permitted disclosure** — Select only needed fields and distinguish authorization to read local task data from authorization to publish it in a ticket, screenshot or assistant prompt.
3. **Actual policy, legal and organizational boundaries** — Identify who is authorized to decide collection, use and disclosure; record unknown contractual/jurisdictional requirements rather than inventing consent or universal compliance.
4. **Fully synthetic fixtures and safe reports** — Use reproducible invented records, redacted error messages and no private credentials; show why a purportedly anonymized sample might still identify someone.
5. **Failure-safe output and temporary state** — Specify invalid destination, partial write, old-file preservation and cleanup policies; verify a failed CSV export cannot publish incomplete records or corrupt existing valid output.
6. **Retention, access and disposal decisions** — Document intended recipients, storage duration, temporary output ownership and deletion/cleanup criteria, without claiming deletion guarantees the runtime cannot establish.
7. **Potential incident and accountable hold** — Respond to a request to paste protected records into a public review channel, keep the unsafe action blocked and identify the actual authorized disclosure/escalation path.
8. **Independent privacy failure check** — Run a controlled negative fixture that checks redacted logging, preserved prior output and lack of unintended extra exported fields, recording exact results and remaining limits.

*Optional practice:* Trace a synthetic CSV record from input through output and diagnostic log; mark which copies may be retained and which disclosure paths are prohibited.

### Module 6 — Accessible Engineering Communication and Evidence-Based Review

#### Outcomes

- SEF9-O6
- SEF9-O7
- SEF9-O16
- SEF9-O20

#### Lessons

1. **Real audiences and document purposes** — Distinguish a user release note, maintainer review, stakeholder risk update and incident/escalation message, with the decisions and evidence each reader needs.
2. **Navigable text as the reference format** — Write semantic Markdown headings, meaningful links, ordered commands, file locations and text explanations, making a hosted issue board or screenshot strictly optional.
3. **Accessibility beyond visual status colors** — Communicate severity, failure, progress and correction in words; provide a text equivalent to any diagram and acknowledge that text-first work is not automatically formally WCAG-compliant.
4. **Usable CLI help and public failure messages** — Check argument help, stable error/status explanation, reproducible commands and output format descriptions against unfamiliar keyboard/assistive-technology reader needs.
5. **Review standard and focused patch** — Apply a published correctness, safety, testability, maintainability and scope checklist to an actual small CSV diff instead of relying on an impression of code quality.
6. **Reproduce a substantive defect independently** — Use a hand-derived quoting/newline or preservation fixture to collect source location, before-fix exit status and expected/observed bytes.
7. **Actionable comments without personal criticism** — Write evidence-linked observations, severity, reproduction and a feasible requested correction; reject vague approval or style opinions as proof of correctness.
8. **Author response and bounded correction** — Answer or justify each substantive review finding, edit the smallest warranted behavior, retain a regression and link changed files to the reviewed issue.
9. **Independent reviewer versus simulated PR** — Record a real reviewer response and verification, while accurately labeling local mock PR artifacts or a proposed hosted workflow that was not actually executed.
10. **Candid release and stakeholder handoff** — Communicate what changed, what remains blocked, privacy/licensing/compatibility implications and next steps in accessible text; revise an ambiguity based on a genuine reader challenge.

*Optional practice:* Give a peer a text-only CSV change review and ask them to reproduce the negative case; improve the release note from the feedback rather than inventing reviewer approval.

### Module 7 — Bounded AI Assistance, Provenance and Instruction Authority

#### Outcomes

- SEF9-O8
- SEF9-O9
- SEF9-O11
- SEF9-O12
- SEF9-O13

#### Lessons

1. **What a coding assistant can and cannot establish** — Explain context-conditioned probabilistic proposals, model or tool/version uncertainty and the difference between generated code, executed tools, verified tests and human authorization.
2. **An explicit explore-plan-implement-verify scope** — Approve a bounded request with allowed files, permitted read/edit commands, trusted input, test oracles, stop conditions and prohibited dependencies, secrets, network and merge actions.
3. **Trusted task directions versus repository content** — Separate actual user authorization and reviewed plan from README comments, pasted search results or tool output that merely contain task data.
4. **Prompt injection in a local fixture** — Identify a malicious synthetic README instruction that impersonates authority, requests a fake secret and external upload, and reject it without executing commands or contacting any endpoint.
5. **Least privilege and unapproved change detection** — Inspect a candidate diff for added dependency, disabled test, overly broad path edit and network or credential access, explaining how an offline file/permission inventory exposes it.
6. **Unknown copyright and confidentiality in context** — Review what data and snippets an assistant would receive, exclude sensitive local content, and record unknown redistribution/provenance rights before adopting an output.
7. **Real versus recorded assistant evidence** — Use an authentic instructor-supplied recorded assistant proposal or a genuinely observed live session, recording model and tools if known and explicitly distinguishing proposed from executed actions.
8. **Human authorization at each acceptance boundary** — Record whether a suggestion was accepted, narrowed, rejected or never run; show how the written plan controls later implementation even if a document claims higher authority.
9. **A safe documented proposal handoff** — Present the scoped proposal, allowed-file table and sanitized attributable excerpt for independent review without treating it as a passed regression or a final implementation.

*Optional practice:* Annotate an authentic recorded assistant proposal and a locally prepared untrusted synthetic README, distinguishing authorized actions from suggestions, unknowns and prohibited requests.

### Module 8 — Independent Verification and Repair of Assistant-Proposed Code

#### Outcomes

- SEF9-O7
- SEF9-O9
- SEF9-O10
- SEF9-O11
- SEF9-O12
- SEF9-O13

#### Lessons

1. **Tests before trusting a proposed diff** — Derive predeclared independent expected CSV quoting/newline, exit-status, destination error and prior-file preservation results from requirements before inspecting the candidate implementation.
2. **A real seeded proposal and truthful setup** — Obtain an authentic, attributable assistant-proposed change containing the three specified defects. In a disposable local copy, independently demonstrate incorrect CSV escaping, suppressed I/O failure and corruption of existing output; record the actual results instead of assuming a prerecorded proposal has passed.
3. **CSV serialization and record boundaries** — Show why manual field concatenation fails commas, quotes and embedded newlines, then verify a proper csv-based correction against an independent reader or byte oracle.
4. **I/O failure must propagate** — Reproduce a swallowed write/open error and require a non-successful exit/status and useful redacted diagnostics, not a printed success message.
5. **Noncorruption of existing output** — Demonstrate why invalid source or destination must not overwrite an earlier valid CSV file; identify whether validation/temporary output/atomic replacement is actually supported by the chosen contract.
6. **Check provenance and diff scope** — Inspect actual changed paths for fabricated APIs, disabled checks, a new dependency, data exposure and unsupported licensing claims, then justify every kept line.
7. **Regression and negative evidence after repair** — Run the same failing-before test cases plus a reviewer-selected unfamiliar valid or malformed fixture and record expected/actual bytes and status from the real program.
8. **Independent unassisted explanation** — Explain a retained implementation branch and a remaining weakness without assistant help, distinguishing a model claim, a mock test and a real independently observed execution.

*Optional practice:* Fix a deliberately flawed exporter prepared locally or supplied by an instructor, retaining before-and-after test results for all three defects and an independent oracle for a quoted newline field.

### Module 9 — One Feature Delivery, Independent Review and Professional Defense

#### Outcomes

- SEF9-O1
- SEF9-O2
- SEF9-O3
- SEF9-O4
- SEF9-O5
- SEF9-O6
- SEF9-O7
- SEF9-O8
- SEF9-O9
- SEF9-O10
- SEF9-O11
- SEF9-O12
- SEF9-O13
- SEF9-O14
- SEF9-O15
- SEF9-O16
- SEF9-O17
- SEF9-O18
- SEF9-O19
- SEF9-O20

#### Lessons

1. **Reuse the same SEF5-derived feature** — Carry approved stories, issues, three decision records, code, tests, authentic proposal and documented synthetic professional scenario into one versioned CSV-export improvement, not another mandatory capstone.
2. **Evidence trace from need to behavior** — Link each required acceptance criterion and problem scenario to an issue, reviewed decision, actual source revision, independent test and observed passing or failing state.
3. **The risk and authorization ledger** — Combine the existing ethics hold/escalation, verified or unknown license/attribution, synthetic data lifecycle and assistant permission inventory without pretending they were individually approved when not.
4. **Failure-driven implementation and review** — Repair intentionally seeded quoting, error-reporting and overwrite defects with real before/after tests, maintain a focused diff and address genuine reviewer objections without hiding unaddressed risks.
5. **Clean independent reproduction** — Provide a plain-text/Markdown README, Python/stdlib commands, fixtures and expected output for a genuinely independent reviewer to reproduce normal and negative cases.
6. **A bounded reviewer-chosen change without AI** — Make and test one small previously unseen modification yourself, without assistant suggestions or generated code, recording the reviewer observation and actual results.
7. **Truthful release and accessibility decision** — Publish a navigable release/update statement with usable CLI error descriptions, non-color-only status, sensitive-data/permission/rights limitations and an honest stop/go conclusion.
8. **Defend every claimed outcome and remaining uncertainty** — Trace all eight existing summative assessments to reused inspectable artifacts, explain conflicts and alternative choices, and distinguish real learning/review evidence from green structural CI.

*Optional practice:* Give an independent reviewer the one feature and documentation, ask for a small unfamiliar CSV change, then demonstrate it unaided with a corrected test and a factual release note.

## Completion requirements

### Assessment setup and evidence boundaries

Use a learner-owned or instructor-prepared synthetic CSV-export scenario across the assessments. Prepare a stakeholder request, a deliberately flawed patch, independent tests for escaping, error reporting and output preservation, a genuine attributable assistant proposal, and suspicious repository text for a safe trust-boundary exercise. Document a professional dilemma involving release pressure, unknown licensing, privacy and accessible communication. Work locally with synthetic data; never execute malicious instructions, expose credentials or treat unverified rights as cleared.

A recorded assistant proposal is not evidence of live tool execution or reviewer acceptance. Prepared failing tests establish defects only: the learner must demonstrate actual failures, implement corrections and independently verify the passing results. Instructor-prepared examples cannot replace learner implementation, real peer or designated-reviewer feedback, or the final unassisted modification.

| Professional capability | Learning focus | Required summative evidence |
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
  - Work: Work on the **same CSV-export feature and versioned issue/review trail** used in SEF9-AS1–AS7. Using a fully synthetic, documented professional scenario, respond **without relying on an AI suggestion** to an urgent stakeholder request to ship despite an observed data-loss defect, publish task records or raw logs in a public review channel, and incorporate an external code fragment with missing or conflicting licensing evidence. Identify affected stakeholders, foreseeable harm, evidence versus assumptions, actual decision authority and professional obligations; write a concise risk assessment with a concrete stop/mitigation/escalation decision, accountable owner and next check, without inventing consent, legal clearance, reviewer approval or a fixed jurisdiction's law. Build a source/dependency provenance and license inventory distinguishing copyright ownership, verified permission, attribution/notice requirements, intended distribution and **unknown** rights; either obtain attributable evidence or exclude/replace the questionable material. Produce a synthetic data-flow and lifecycle table covering CSV fields, output, temporary files, diagnostics, sharing permissions, retention and deletion; demonstrate one independently checked privacy-preserving failure/cleanup or redacted reporting case. Prepare an accessible Markdown or plain-text stakeholder update and focused code-review/release handoff with descriptive headings, source locations, plain-language risk/severity, expected/actual behavior, usable CLI help/error explanation and non-color-only status information; an optional screenshot or diagram may supplement but not replace this text. Have an independent reader/reviewer follow the update, identify a substantive ambiguity or challenge the decision, and record the correction and remaining limitations. Reuse existing source, tests and reviewer participation whenever legitimate; do **not** build a separate application or repeat the AI assessment.
  - Criteria: The professional decision addresses foreseeable harm and organizational authority with proportionate, timely mitigation and truthful reporting, including a credible response to pressure to bypass a failing check; unknowns remain labeled unknown and no simulated consent/approval is passed off as real. The rights inventory accurately separates provenance, copyright, SPDX expressions, actual retrieved license terms, compatible use/distribution and unresolved permissions; code with unverified redistribution rights is not silently included or declared safe. The data map has a defensible collection/purpose/exposure/retention/deletion boundary, avoids real personal data and records an actual synthetic test or controlled evidence that errors do not publish protected records. The written review and stakeholder handoff are navigable without color, hosted UI or images, include explicit reproduction and decisions, communicate access/error behavior respectfully and accurately, and record a genuine independent reader response and the learner's revision. The learner demonstrates that **these duties exist even when no AI assistant is involved** and can defend all decisions unaided. Unresolved material disclosure, license, data-loss, accessibility-of-evidence or dishonest-approval claims block passing.
  - Evidence: Existing feature revision and requirement references, documented synthetic scenario and independently written impact/risk analysis, truthfully documented blocked/released decision and escalation trail, source/license/notice inventory with evidence and unresolved-rights treatment, synthetic data-flow and retention/disposal map, privacy-preserving error/log/cleanup fixture results, accessible Markdown/text stakeholder update and focused review/release notes, actual independent reader feedback and revised communication, and a technical defense of non-AI professional responsibility.

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

**Subsequent competency-derived instructional review:** The earlier twelve-module version repeated work-item decomposition across requirements and planning, code-review communication across accessibility and patch review, and AI provenance/permissions/verification across three disconnected modules. This revision consolidates those teaching responsibilities but retains distinct ethics, rights and privacy decisions, since their risks and evidence remain different. All twenty published outcomes and all eight full assessment contracts remain unchanged, including the material O17–O20/AS8 obligations introduced in the prior revision. Existing learner evidence stays tied to its actually assessed revision; instructional consolidation introduces no new graduation requirement or readiness claim.

A learner's historical completion is neither automatically revoked nor declared to satisfy the new outcomes without actual reviewable evidence. This is a **material addition** of four professional competencies with a clearly new assessment ID, not a reinterpretation of older ones. No blanket assessment-count rule, mandatory proprietary AI tool, new formal prerequisite, global OEE course-format amendment or premature `tested`/ `verified` promotion is introduced.
