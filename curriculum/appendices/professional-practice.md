# Professional Practice

Technical knowledge is necessary, not sufficient. Two engineers can know the same material while one is trusted with a production system and the other is not. The difference is usually reliability, judgment, evidence, and communication.

This appendix describes the standard the curriculum expects. It is not a corporate policy manual, and it does not replace the law, your employer's rules, or a signed authorization.

## 1. The professional loop

Use the same loop for a lab, a ticket, or a production incident:

1. **Clarify the problem.** Who is affected, what is the current behaviour, what would "fixed" mean, and what is out of scope?
2. **Model the system.** Draw the components, state ownership, data flow, trust boundaries, and the failure modes that matter.
3. **Predict.** Write the expected result, cost, latency, error rate, or security property before changing anything.
4. **Make the smallest change.** Prefer a reversible change with a test over a large rewrite with a story.
5. **Verify.** Test normal, boundary, invalid, and failure cases. Measure where performance or reliability is claimed.
6. **Review.** Ask someone to attack the assumptions, not just the formatting.
7. **Operate.** Add logs, metrics, limits, rollback, and an owner. A change is not finished when it merges.
8. **Learn.** Record what surprised you and update the model, the test, or the runbook.

The loop is deliberately boring. Professionals repeat it under pressure; amateurs improvise and call it speed.

## 2. Artifacts that carry judgment

A project needs different documents at different stages. Do not write all of them for every lab. Do write the ones that reduce real uncertainty.

| Artifact | Question it answers | When it is required |
| --- | --- | --- |
| README | What is this, how do I run it, what does it not do? | Every project and substantial lab |
| Design doc | What are the requirements, components, interfaces, state, and trade-offs? | Multi-component or long-lived work |
| ADR (architecture decision record) | Why did we choose this option, and what did we reject? | A decision that is expensive to reverse |
| Test plan | What behaviour is verified, at which level, and with what data? | Any code with users or failure modes |
| Benchmark/evaluation plan | What claim is being tested, against which baseline, with what threshold? | Performance, ML, and reliability claims |
| Threat model | What are the assets and trust boundaries, and how could they be misused? | Networked, multi-user, AI, or security work |
| Runbook | How do I deploy, roll back, restore, and respond to alerts? | Anything operated beyond a laptop |
| Postmortem | What happened, why, what was the impact, and what changes now? | Incidents and significant near misses |
| Model/data card | What is this model or dataset for, what are its limits, and what should it not be used for? | ML and generative-AI work |
| Retrospective | What did I believe, what did the evidence change, and what next? | Every course and project |

### README minimum

A reviewer should be able to answer these questions without reading the source:

- What problem does this solve, and for whom?
- What is in scope and explicitly out of scope?
- What are the prerequisites and exact setup commands?
- How do I run the tests, the demo, and the evaluation?
- What is the failure behaviour and the known limitation?
- Where is the evidence, and which commit produced it?

### Design-doc minimum

- requirements and quality attributes (latency, durability, security, cost);
- architecture diagram with boundaries;
- component responsibilities and interfaces;
- state ownership and persistence;
- failure handling, retries, timeouts, and degradation;
- observability and rollback;
- rejected alternatives and the reason;
- open questions and non-goals.

Long documents do not create clarity. A short document with a diagram, explicit interfaces, and a failure table usually does.

## 3. Code quality and review

### As an author

- Keep a change focused. A review that mixes refactoring, behaviour change, and formatting hides bugs.
- Write the test that would fail without the change.
- Name things by what they mean, not by their type or temporary role.
- Handle errors at the layer that can make a decision. Do not swallow them to make the output quiet.
- Avoid speculative abstraction. Duplicate twice before extracting a general mechanism.
- Document the non-obvious **why**, not the obvious **what**.
- Remove debug prints, dead code, secrets, and generated artifacts before review.
- State the risk, the rollback, and what you did not test.

### As a reviewer

Review in this order:

1. **Correctness:** Does it do what the description claims? What input breaks it?
2. **Boundaries:** Are permissions, limits, validation, and error paths correct?
3. **State:** Who owns it, when is it freed, and what happens on retry or restart?
4. **Tests:** Do they test the risk, or only the happy path?
5. **Operability:** Logs, metrics, timeouts, shutdown, migration, rollback.
6. **Readability:** Can a new engineer follow it without a meeting?
7. **Style:** Only after the above.

Do not approve a security-sensitive or data-destructive change because "it looks fine". Ask for the failure case and the rollback.

### Definition of done for code

- [ ] Requirement and non-goals stated.
- [ ] Tests cover normal, boundary, invalid, and failure behavior.
- [ ] Errors are visible and actionable.
- [ ] Resource limits, timeouts, and shutdown are handled.
- [ ] Secrets and private data are excluded.
- [ ] Logs and metrics are useful without leaking sensitive values.
- [ ] Documentation and examples match the code.
- [ ] A clean checkout can run the verification command.

## 4. Debugging discipline

Debugging is a controlled experiment, not random editing.

1. **Reproduce** with the smallest command and record the environment.
2. **Stabilize** the failure: reduce noise, fix the seed/input, and confirm it is deterministic enough to test.
3. **Localize** by layer: input, parsing, state, concurrency, I/O, network, dependency, environment.
4. **Hypothesize** one cause and predict what the evidence would look like if it were true.
5. **Instrument** with a log, debugger, trace, metric, or minimal test. Change one variable at a time.
6. **Fix the cause**, not the symptom. Add a regression test that fails on the old code.
7. **Check the neighbourhood.** The same mistake often exists in a sibling path.
8. **Write it down.** A short root-cause note saves the next person hours.

Useful questions:

- What changed immediately before the failure?
- What is the smallest input that still fails?
- Does it fail on a clean checkout, another machine, or with a different compiler/runtime?
- Is the failure deterministic, timing-dependent, or data-dependent?
- What does the system do at the boundary (empty, max, zero, negative, partial, duplicate, slow)?
- Is the observed value measured at the layer I think it is?

## 5. Working in an existing codebase

- Read the README, build files, tests, and recent history before writing.
- Trace one user-visible path end to end. Draw the call and data flow.
- Find the conventions: naming, error handling, logging, test style, dependency policy.
- Make the smallest change that proves you understand the seam.
- Ask before introducing a new framework, datastore, or cross-cutting abstraction.
- Leave the codebase easier to change, not merely different.
- Do not reformat unrelated files in a functional change.

A professional can be productive in an unfamiliar repository in a day. That skill is built by reading code, not only by writing greenfield projects.

## 6. Communication

### Status update

Use four lines:

```text
Done:        what is complete and verified
Next:        the next concrete deliverable
Blocked by:  the exact dependency or decision needed
Risk:        what could invalidate the plan
```

### Design review

Lead with the decision, then the evidence:

1. the problem and constraints;
2. the proposed design and the one-sentence reason;
3. the alternatives and why they lost;
4. the failure modes and mitigation;
5. the cost, migration, and rollback;
6. the questions you need answered.

### Incident communication

- State impact in user terms: who, what, since when, how severe.
- State current mitigation and next update time.
- Do not speculate about cause in the customer channel.
- Keep a timestamped timeline in the technical channel.
- After recovery, separate trigger, contributing factors, and systemic cause.

### Writing for decision-makers

Translate mechanism into consequence:

- "The queue grows without bound under a 2x traffic spike, so requests time out after 30 seconds and users see failed checkouts."
- "The model has 0.91 AUROC but is badly calibrated at the threshold we would deploy, so the false-alarm load is unacceptable."

Avoid tool-name theater. A list of scanners is not a risk assessment; a list of technologies is not an architecture.

## 7. Security, privacy, and ethics

These rules apply to every track, not only Security.

- **Authorization first.** Test only systems you own or have explicit written permission to test. Define scope, time window, prohibited actions, and stop conditions.
- **Least privilege.** Use the minimum account, token, network, and data access needed. Do not run labs as root by default.
- **Data minimization.** Use synthetic or licensed data. Do not copy production data into a lab. If you must use real data, document the legal basis, retention, and access.
- **Secrets hygiene.** Keep credentials in a manager or environment, never in Git, notebooks, screenshots, logs, or prompts. Rotate immediately after exposure.
- **Responsible disclosure.** Do not publish a working exploit against a third-party system. Report privately, allow a fix window, and follow the owner's policy.
- **Honest claims.** Do not call something secure, private, fair, or production-ready because a narrow test passed.
- **Licensing.** Respect software, dataset, book, and model licenses. Record the license and attribution.
- **Human impact.** High-stakes decisions about people (health, employment, credit, safety) require domain expertise, legal review, and a level of evidence this curriculum alone cannot provide.

If an action could affect availability, integrity, privacy, or someone else's property, stop and get explicit approval.

## 8. Career development

### What changes by level

| Level | Expected contribution |
| --- | --- |
| Junior | Completes bounded tasks correctly, tests their work, asks precise questions, learns the codebase. |
| Mid | Owns a component, diagnoses unfamiliar failures, makes trade-offs, reviews others' changes, communicates with users. |
| Senior | Owns a problem area, designs systems, prevents classes of failure, mentors, influences decisions across teams. |
| Staff/principal | Sets technical direction, resolves ambiguous cross-team problems, balances reliability/cost/security, grows other leaders. |

Titles vary by company. The underlying progression is from **task execution** to **problem ownership** to **direction setting**.

### Evidence that compounds

- two or three deep projects with reproducible evaluation and a clear failure story;
- a design document you can defend;
- a production-style runbook and postmortem;
- a security assessment or threat model with verified remediation;
- a model/data card and an honest evaluation;
- writing that explains a hard idea without jargon;
- mentoring or review evidence: a colleague who became more effective because of you.

A certificate is a weak signal on its own. A working system with tests, measurements, and a limitation section is a strong signal.

### Interviews

Prepare to:

- explain a project from problem to evidence in five minutes;
- draw the architecture and the failure paths;
- answer "what would you do if traffic doubled / a node died / the model drifted / the key leaked?";
- debug a small program or reason about a system under constraints;
- discuss a decision you reversed and what evidence changed your mind;
- write clear code in a shared editor, narrating trade-offs.

Do not memorize a system design answer. Practice deriving it from requirements.

### Staying current

- Follow primary sources: specifications, papers, official docs, maintainer write-ups.
- Read postmortems and incident reports from organizations with real scale.
- Reproduce one new technique per quarter in a lab; do not rewrite your stack for every release.
- Keep a "watch list" with a reason and a review date. Most new tools do not matter to your current problem.
- Teach a topic publicly or internally. Teaching exposes the gaps.

## 9. Sustainable practice

- Protect sleep. Fatigue produces confident wrong explanations.
- Use one primary track and one active project. Context switching is more expensive than it feels.
- Schedule a full rest day and a buffer week. Recovery is part of the plan.
- When behind, cut optional depth before cutting tests, evidence, or the project increment.
- Compare your current evidence with your own evidence three months ago, not with someone else's timeline.
- Ask for help early. A 30-minute conversation with a working engineer can correct a month of wrong assumptions.

Burnout is not a badge. A curriculum that destroys your health is a failed curriculum, even if you finish it.

## 10. Professional checklist

Use this before calling a course or project complete:

- [ ] I can explain the mechanism without notes.
- [ ] I predicted a result before measuring it.
- [ ] The artifact runs from a clean checkout.
- [ ] Tests cover the failure modes that matter.
- [ ] I measured or verified the claim, with environment and limitations.
- [ ] I handled the security, privacy, and authorization boundary.
- [ ] Another engineer can reproduce the result from the documentation.
- [ ] I named one thing I got wrong and what changed because of it.
- [ ] I know the next smallest experiment.
- [ ] The work is committed with a message that explains why.

If any box is unchecked, the honest status is "in progress", not "done".
