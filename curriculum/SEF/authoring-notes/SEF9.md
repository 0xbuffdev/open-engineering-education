# SEF9 — Lesson authoring notes

> Optional instructional context preserved from the original source. These are not required course metadata, assessments or module briefs.

## Course orientation

- **Introduction:** Professional software is built by teams who agree on needs, track work, record decisions, review each other's changes, and increasingly use AI assistants. This course teaches those habits and the discipline needed to use assistants without surrendering understanding.
- **History:** Agile methods, including user stories, emerged in the 1990s and were named in the Agile Manifesto of 2001. Code inspection was formalized in the 1970s, and architecture decision records were proposed in 2011. AI coding assistants reached mainstream developers with GitHub Copilot in 2021, and conversational assistants spread from late 2022.
- **Usage:** The learner takes one feature through stories, tracked work, a decision record, an assistant-supported implementation, and a peer-reviewed pull request.
- **Applications:** Every professional team, whether it builds products, internal tools, or open-source software.
- **Strengths:** Shared practices reduce misunderstanding and rework, and assistants speed up routine work.
- **Limitations:** Process has overhead, practices vary between teams and tools, and assistants can be confidently wrong.
- **Key concepts:** user story; acceptance criteria; issue; project board; decision record; code review; AI assistant; context; verification; disclosure

## Module 1 — From Need to Work Item

- **Introduction:** Software starts with a need, not a design. This module teaches how teams state needs in a form that can be built and checked.
- **Overview:** It covers personas, user stories, acceptance criteria, the definition of done, epics, stories, tasks, and sizing.
- **History:** User stories came out of Extreme Programming in the late 1990s. Ron Jeffries described card, conversation, and confirmation in 2001, the year the Agile Manifesto was written.
- **Strengths:** Stories keep attention on user value and invite conversation.
- **Limitations:** A story can be too vague or too large, and stories do not replace detailed analysis for complex or safety-critical systems.
- **Key concepts:** persona; user story; acceptance criteria; definition of done; epic; task; estimate

## Module 2 — Planning & Tracking Work

- **Introduction:** A plan that nobody can see is not a plan. This module covers how teams track work in the repository.
- **Overview:** It covers repositories and READMEs, issues and templates, sub-issues, dependencies, labels, milestones, project boards, and linking pull requests.
- **Key concepts:** issue; template; label; milestone; dependency; board; pull request link

## Module 3 — Recording Decisions

- **Introduction:** Teams forget why they decided things. A decision record keeps the reason with the code.
- **Overview:** It covers deciding what to record, context and problem statement, options and drivers, outcome and consequences, confirmation, and status.
- **History:** Michael Nygard proposed architecture decision records in a 2011 post, and MADR is a template that makes the options and consequences explicit.
- **Strengths:** Records are cheap, reviewable, and durable.
- **Limitations:** Records go stale, and recording trivial decisions hides the important ones.
- **Key concepts:** architectural decision; context; considered options; outcome; consequences; confirmation; status

## Module 4 — Code Review as Practice

- **Introduction:** Review is how teams share knowledge and keep quality. This module teaches the standard and the manners.
- **Overview:** It covers the review standard, what reviewers look for, small changes with good descriptions, giving feedback, and responding to feedback.
- **History:** Michael Fagan formalized inspections at IBM in 1976, and change-based review spread with open-source patches and pull requests.
- **Strengths:** Review finds defects early and spreads knowledge.
- **Limitations:** Review is slow when changes are large, and poor feedback harms teams.
- **Key concepts:** review standard; change description; small change; feedback; revision

## Module 5 — Working with AI Assistants

- **Introduction:** AI coding assistants write and edit code from instructions. They are useful and unreliable in equal measure, so using them well is a skill.
- **Overview:** It covers how an assistant works, giving context and instructions, the explore, plan, code, and verify loop, managing context, and permissions.
- **History:** Code completion tools existed for decades. GitHub Copilot's technical preview in 2021 brought model-based completion to many developers, and conversational and agentic assistants followed from 2022.
- **Strengths:** Assistants are fast at routine work and at exploring unfamiliar code.
- **Limitations:** They can state wrong things confidently, lose context in long sessions, and take harmful actions if trusted too much.
- **Key concepts:** model; context window; tool; agent loop; instruction file; plan; permission

## Module 6 — Verifying & Governing AI-Generated Work

- **Introduction:** A change is only as good as the evidence that it works. This module teaches how to check what an assistant produced.
- **Overview:** It covers tests as the contract, reading diffs critically, common failure modes, secrets and data exposure, licensing and disclosure, and staying able to explain your own code.
- **Strengths:** Verification turns fast generation into trustworthy work.
- **Limitations:** Verification takes time, and tests cannot prove correctness.
- **Key concepts:** test as contract; diff review; invented interface; secret exposure; license; disclosure

## Module 7 — Feature Delivery Workflow

- **Introduction:** This lab integrates the course. The learner delivers one feature through the full professional workflow and defends it without the assistant.
- **Overview:** It combines stories, tracked issues, a decision record, an assistant-supported implementation, a peer-reviewed pull request, and an evidence log.
- **Applications:** Feature work in every professional team follows some version of this cycle.
- **Key concepts integrated:** user stories; issue tracking; decision records; code review; assistant use; verification; disclosure

1. **Plan, build, review, and defend a feature delivered through the full workflow**
   - kind: `lab`

## Original topic inventory

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
