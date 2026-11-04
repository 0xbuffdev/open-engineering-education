> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF9 — Professional Workflow & AI-Assisted Engineering

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF5
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course teaches how professional teams turn needs into delivered software. Learners write user stories with acceptance criteria, plan and track work with issues and project boards, record design decisions, review code to a published standard, and use AI coding assistants deliberately: giving them context, constraining what they may do, and verifying everything they produce. AI assistants are used here as a graded engineering practice, with the learner remaining responsible for understanding and defending every change.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Professional software is built by teams who agree on needs, track work, record decisions, review each other's changes, and increasingly use AI assistants. This course teaches those habits and the discipline needed to use assistants without surrendering understanding.
- **History:** Agile methods, including user stories, emerged in the 1990s and were named in the Agile Manifesto of 2001. Code inspection was formalized in the 1970s, and architecture decision records were proposed in 2011. AI coding assistants reached mainstream developers with GitHub Copilot in 2021, and conversational assistants spread from late 2022.
- **Usage:** The learner takes one feature through stories, tracked work, a decision record, an assistant-supported implementation, and a peer-reviewed pull request.
- **Applications:** Every professional team, whether it builds products, internal tools, or open-source software.
- **Strengths:** Shared practices reduce misunderstanding and rework, and assistants speed up routine work.
- **Limitations:** Process has overhead, practices vary between teams and tools, and assistants can be confidently wrong.
- **Key concepts:** user story; acceptance criteria; issue; project board; decision record; code review; AI assistant; context; verification; disclosure

## Prerequisites

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

## Modules

### Module 1 — From Need to Work Item

#### Module brief

- **Introduction:** Software starts with a need, not a design. This module teaches how teams state needs in a form that can be built and checked.
- **Overview:** It covers personas, user stories, acceptance criteria, the definition of done, epics, stories, tasks, and sizing.
- **History:** User stories came out of Extreme Programming in the late 1990s. Ron Jeffries described card, conversation, and confirmation in 2001, the year the Agile Manifesto was written.
- **Strengths:** Stories keep attention on user value and invite conversation.
- **Limitations:** A story can be too vague or too large, and stories do not replace detailed analysis for complex or safety-critical systems.
- **Key concepts:** persona; user story; acceptance criteria; definition of done; epic; task; estimate

#### Module outcomes

By the end of this module, the learner can:

- Write a user story from a persona, a need, and a purpose, without describing the implementation.
- Write acceptance criteria that can be checked, and state a definition of done.

1. **Course introduction: Professional Workflow & AI-Assisted Engineering** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: From Need to Work Item** — what the topic is, where it is used, and its strengths and limits
3. **Users and personas**
4. **Writing user stories**
5. **Acceptance criteria and definition of done**
6. **Epics, stories, and tasks**
7. **Sizing work**
8. **Stories and criteria**
   - kind: `test`
9. **Turn a request into stories** — convert a vague feature request into small stories with acceptance criteria and identify which story to build first
   - kind: `lab`

### Module 2 — Planning & Tracking Work

#### Module brief

- **Introduction:** A plan that nobody can see is not a plan. This module covers how teams track work in the repository.
- **Overview:** It covers repositories and READMEs, issues and templates, sub-issues, dependencies, labels, milestones, project boards, and linking pull requests.
- **Key concepts:** issue; template; label; milestone; dependency; board; pull request link

#### Module outcomes

By the end of this module, the learner can:

- Break a feature into issues and sub-issues, with dependencies and labels.
- Organize issues on a project board and link pull requests to the issues they close.

1. **Introduction: Planning & Tracking Work** — what the topic is, where it is used, and its strengths and limits
2. **Repositories, README, and contribution guidelines**
3. **Issues and issue templates**
4. **Sub-issues, dependencies, and labels**
5. **Milestones and project boards**
6. **Linking pull requests to issues**
7. **Planning and tracking**
   - kind: `test`
8. **Set up tracking for a feature** — create issues from the stories, add templates, labels, and dependencies, and arrange them on a board
   - kind: `lab`

### Module 3 — Recording Decisions

#### Module brief

- **Introduction:** Teams forget why they decided things. A decision record keeps the reason with the code.
- **Overview:** It covers deciding what to record, context and problem statement, options and drivers, outcome and consequences, confirmation, and status.
- **History:** Michael Nygard proposed architecture decision records in a 2011 post, and MADR is a template that makes the options and consequences explicit.
- **Strengths:** Records are cheap, reviewable, and durable.
- **Limitations:** Records go stale, and recording trivial decisions hides the important ones.
- **Key concepts:** architectural decision; context; considered options; outcome; consequences; confirmation; status

#### Module outcomes

By the end of this module, the learner can:

- Write a decision record with context, options, outcome, consequences, and a way to confirm it.
- Keep decision records in the repository with a status and links to superseding records.

1. **Introduction: Recording Decisions** — what the topic is, where it is used, and its strengths and limits
2. **What counts as a decision worth recording**
3. **Context and problem statement**
4. **Options and drivers**
5. **Outcome, consequences, and confirmation**
6. **Status and superseding decisions**
7. **Decision records**
   - kind: `test`
8. **Write three decision records** — record three real design decisions for one project, including one that is later superseded
   - kind: `lab`

### Module 4 — Code Review as Practice

#### Module brief

- **Introduction:** Review is how teams share knowledge and keep quality. This module teaches the standard and the manners.
- **Overview:** It covers the review standard, what reviewers look for, small changes with good descriptions, giving feedback, and responding to feedback.
- **History:** Michael Fagan formalized inspections at IBM in 1976, and change-based review spread with open-source patches and pull requests.
- **Strengths:** Review finds defects early and spreads knowledge.
- **Limitations:** Review is slow when changes are large, and poor feedback harms teams.
- **Key concepts:** review standard; change description; small change; feedback; revision

#### Module outcomes

By the end of this module, the learner can:

- Review a change for design, correctness, tests, and clarity, and write feedback that is specific and actionable.
- Write a small, well-described change and respond to review comments.

1. **Introduction: Code Review as Practice** — what the topic is, where it is used, and its strengths and limits
2. **The standard of a review**
3. **What reviewers look for**
4. **Writing small changes with good descriptions**
5. **Giving feedback**
6. **Responding to feedback**
7. **Review practice**
   - kind: `test`
8. **Review and revise a pull request** — review a prepared pull request, then revise your own change in response to a peer's comments
   - kind: `lab`

### Module 5 — Working with AI Assistants

#### Module brief

- **Introduction:** AI coding assistants write and edit code from instructions. They are useful and unreliable in equal measure, so using them well is a skill.
- **Overview:** It covers how an assistant works, giving context and instructions, the explore, plan, code, and verify loop, managing context, and permissions.
- **History:** Code completion tools existed for decades. GitHub Copilot's technical preview in 2021 brought model-based completion to many developers, and conversational and agentic assistants followed from 2022.
- **Strengths:** Assistants are fast at routine work and at exploring unfamiliar code.
- **Limitations:** They can state wrong things confidently, lose context in long sessions, and take harmful actions if trusted too much.
- **Key concepts:** model; context window; tool; agent loop; instruction file; plan; permission

#### Module outcomes

By the end of this module, the learner can:

- Explain how an AI coding assistant works at the level of context, tools, and an action loop.
- Give an assistant the context, constraints, and a written plan it needs to complete a small change.

1. **Introduction: Working with AI Assistants** — what the topic is, where it is used, and its strengths and limits
2. **How a coding assistant works** — a model, a limited context window, tools, and a loop
3. **Giving context and instructions**
4. **Explore, plan, code, verify**
5. **Managing context**
6. **Permissions and what the assistant may do**
7. **Working with assistants**
   - kind: `test`
8. **Complete a change under a written plan** — complete a small change in an existing project with an assistant, starting from a written plan and a limited set of permissions, and record each step
   - kind: `lab`

### Module 6 — Verifying & Governing AI-Generated Work

#### Module brief

- **Introduction:** A change is only as good as the evidence that it works. This module teaches how to check what an assistant produced.
- **Overview:** It covers tests as the contract, reading diffs critically, common failure modes, secrets and data exposure, licensing and disclosure, and staying able to explain your own code.
- **Strengths:** Verification turns fast generation into trustworthy work.
- **Limitations:** Verification takes time, and tests cannot prove correctness.
- **Key concepts:** test as contract; diff review; invented interface; secret exposure; license; disclosure

#### Module outcomes

By the end of this module, the learner can:

- Verify generated code with tests written first, a critical reading of the diff, and checks for known failure modes.
- Explain the privacy, licensing, and disclosure obligations that apply to AI-assisted work.

1. **Introduction: Verifying & Governing AI-Generated Work** — what the topic is, where it is used, and its strengths and limits
2. **Tests as the contract**
3. **Reading a generated diff critically**
4. **Common failure modes** — invented interfaces, needless complexity, insecure code, and ignored project conventions
5. **Secrets and data exposure**
6. **Licensing, ownership, and disclosure**
7. **Staying able to explain your own code**
8. **Verification and governance**
   - kind: `test`
9. **Find defects in a generated change** — review a prepared AI-generated change that contains seeded defects, find and fix them, and write the tests that would have caught each one
   - kind: `lab`

### Module 7 — Feature Delivery Workflow

#### Module brief

- **Introduction:** This lab integrates the course. The learner delivers one feature through the full professional workflow and defends it without the assistant.
- **Overview:** It combines stories, tracked issues, a decision record, an assistant-supported implementation, a peer-reviewed pull request, and an evidence log.
- **Applications:** Feature work in every professional team follows some version of this cycle.
- **Key concepts integrated:** user stories; issue tracking; decision records; code review; assistant use; verification; disclosure

1. **Plan, build, review, and defend a feature delivered through the full workflow**
   - kind: `lab`

## Topics

- User stories and personas
- Acceptance criteria and definition of done
- Epics, stories, and tasks
- Issues, templates, labels, and milestones
- Dependencies and project boards
- Architecture decision records
- Code review standards
- Writing change descriptions
- How coding assistants work
- Context and project instruction files
- Plan-first workflows
- Permissions for assistants
- Verifying generated code
- Failure modes of generated code
- Disclosure and ownership

## Practical exercises

2. Convert a feature request into stories with acceptance criteria.
3. Set up issues, labels, and a project board for a feature.
4. Write a decision record for a real design choice.
5. Review a pull request and revise your own in response to review.
6. Complete a small change with an assistant under a written plan.
7. Find defects in a generated change and write tests for them.

## Course lab

**Feature Delivery Workflow**

Take a feature request for the SEF5 tested command-line application and deliver it through the full workflow. The submission must include:

- User stories with acceptance criteria
- Issues and a project board for the feature
- At least one decision record
- An implementation developed with an AI assistant from a written plan, with tests written first
- A pull request reviewed by a peer against a published standard
- An evidence log recording where the assistant was wrong, what was changed or rejected, and what the learner did without assistance

The defense includes a live modification made without the assistant.

## Exit check

The learner can take a need through stories, tracked work, recorded decisions, and a reviewed change, use an assistant without surrendering understanding, and explain and modify every line delivered.
