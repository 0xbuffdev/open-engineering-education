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

1. **Plan, build, review, and defend a feature delivered through the full workflow** — `lab`

   **Final integration lab — required work**

   **Feature Delivery Workflow**

   Take a feature request for the SEF5 tested command-line application and deliver it through the full workflow. The submission must include:

   - User stories with acceptance criteria
   - Issues and a project board for the feature
   - At least one decision record
   - An implementation developed with an AI assistant from a written plan, with tests written first
   - A pull request reviewed by a peer against a published standard
   - An evidence log recording where the assistant was wrong, what was changed or rejected, and what the learner did without assistance

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

**Additional required micro-lab steps:**

- **Turn a request into stories:** Convert a vague feature request into small stories with acceptance criteria and identify which story to build first.
- **Set up tracking for a feature:** Create issues from the stories, add templates, labels, and dependencies, and arrange them on a board.
- **Write three decision records:** Record three real design decisions for one project, including one that is later superseded.
- **Review and revise a pull request:** Review a prepared pull request, then revise your own change in response to a peer's comments.
- **Complete a change under a written plan:** Complete a small change in an existing project with an assistant, starting from a written plan and a limited set of permissions, and record each step.
- **Find defects in a generated change:** Review a prepared AI-generated change that contains seeded defects, find and fix them, and write the tests that would have caught each one.

**Additional required practical assessments:**

- **Module 7 — Audit an untrusted coding suggestion:**
  - Objective: Evaluate tool-assisted edits using requirements, code review and trusted tests rather than assistant confidence.
  - Environment: Document safe fixtures, runtime/compiler versions and necessary command lines.
  - Procedure: Inspect a prepared change containing deceptive instructions and an unauthorized dependency; identify and reject the unsafe modifications.
  - Verification: The accepted changes meet requirements, tests pass and no privileged information is disclosed.
  - Evidence: Include source, failing and passing checks, diagnostic output, assumptions and a retrospective.
  - Failure analysis: Identify an invalid assumption or negative path and justify the verified correction.

**Final integration extension:**

- Include an explicit negative case, reproducible build and explanation of the expanded outcomes in the final lab or defense.

**Exit demonstration:**

The learner can take a need through stories, tracked work, recorded decisions, and a reviewed change, use an assistant without surrendering understanding, and explain and modify every line delivered.
