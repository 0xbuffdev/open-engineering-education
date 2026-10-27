# Course Format

This is the required structure of a course file in `curriculum/`. A document without these sections is not a course; it is notes. The sections exist so a stranger can pick up any course and know what to do, what it costs in hours, and what "done" means.

## Header (required)

The first lines of every course file carry the machine-readable facts:

```markdown
# <CODE> — <Title>

**Track:** <track> · **Prerequisite:** <codes or "none"> · **Core**/**Elective** · **Time:** <weeks and hours> · **Project:** <ladder increment or "none">
**Status:** `draft` · [status labels](../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)
```

Requirements:

- the status label is present and matches the course's row in the track README table;
- the hour budget is stated in hours, not in vague durations;
- prerequisites name course codes, not "some experience with X".

## Required sections

| # | Section | What it must contain |
| --- | --- | --- |
| 1 | **Purpose** | The professional capability this course builds, in one short paragraph. |
| 2 | **Outcomes** | Observable capabilities, each one demonstrable without notes. |
| 3 | **Prerequisites** | Course codes and the evidence expected before starting. |
| 4 | **Required reading** | Exact chapter and section identifiers by title (never page numbers), with a realistic hour estimate. One primary spine plus stated alternatives. |
| 5 | **Topic checklist** | The subject grouped into modules; checkable items, not chapters to skim. |
| 6 | **Labs** | Experiments that produce runnable evidence; one concrete question each. |
| 7 | **Exercises** | Closed-book recall and implementation drills. |
| 8 | **Project increment** | A linked increment on the [project ladder](../curriculum/projects/project-ladder.md), or an explicit statement of what replaces it (as in F0). |
| 9 | **Exit check** | Statements the learner demonstrates without notes; see [evidence-rules.md](evidence-rules.md). |
| 10 | **Common failure modes** | How learners actually fail this course, stated up front. |
| 11 | **Evidence to commit** | The exact artifacts that count toward completion. |
| 12 | **Optional depth** | Where to go further; explicitly not part of the exit check. |

## Format rules

- **One primary external resource.** Additional material is reference, not a second spine (see [resources](../curriculum/resources.md)).
- **Section identifiers, not page numbers.** Editions differ; titles do not.
- **Realistic hours.** The hour budget must survive contact with a learner; revise it when measurements disagree.
- **Electives keep the same structure.** They may drop the ladder project but nothing else.
- **Relative links must resolve.** CI fails the build on a broken internal link.
- **Status label in header and track table.** Both must agree; see [status-labels.md](status-labels.md).

## Where learner work goes

A course file is the assignment. The learner's work — labs, exercises, notes, project increments, and the evidence log — lives in their own study workspace, created with the scripts in [`../scripts/`](../scripts/). Nothing in this format requires, or permits, committing learner state to this repository.
