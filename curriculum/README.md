# Curriculum

This directory is the single source of truth for what to study, in what order, from which book sections, what to build, and how to prove you are done.

Each course has its own file so you can open exactly one page at a time. The structure of a course file is defined in [../spec/course-format.md](../spec/course-format.md), and every course currently carries the [`draft`](../spec/status-labels.md) status label.

## Start here

1. Pick **one primary program**. Do not study three programs at once.
2. Set up your weekly block before starting.
3. Check the local library policy and reading maps before buying books.
4. Check the small set of external materials you actually need now.
5. Open the first course file in your program. Do its labs and project increment before moving on.
6. Record completion in the progress log (kept in your study workspace) only after the course exit check is demonstrable.

## The curriculum is organised by program

| Code | Program | Directory |
| --- | --- | --- |
| `SEF` | Software Engineering Foundations | [SEF/](SEF/) |
| `APP` | Application Engineering | [APP/](APP/) |
| `SYS` | Systems Engineering | [SYS/](SYS/) |
| `AI` | AI Engineering | [AI/](AI/) |
| `SEC` | Security Engineering | [SEC/](SEC/) |

Course files are being re-added under each program directory.

## What every course file contains

- **Purpose** and the professional capability it develops.
- **Prerequisites** and a realistic time budget.
- **Required reading** with exact chapter/section identifiers and a time estimate.
- **Topic checklist** grouped into modules.
- **Labs** that produce runnable evidence.
- **Exercises** that force recall and implementation.
- **Project increment** linked to the project ladder (core courses) or an optional elective extension.
- **Exit check** you must demonstrate without notes.
- **Common failure modes**, evidence to commit, and optional depth.

Electives keep the same structure but do not require a ladder project. F0 has no project; it produces the environment and study system that P1 depends on.

A course is complete when the exit check is demonstrable, the artifact is committed, and the retrospective is written. Reading a chapter is not completion.

## Core versus elective

**Core** means the minimum defensible professional foundation for that track. Do not replace it with a different book, a shorter tutorial, or an LLM-generated summary.

**Elective** means depth for a role, a project, or curiosity. Electives are not required to finish the track. Add them only after the core and the capstone, or when a specific job description demands one.

## Weekly rhythm (15-hour default)

| Activity | Hours/week | What counts |
| --- | ---: | --- |
| Reading and annotated notes | 3–4 | One primary source, active notes, no passive video |
| Labs and implementation | 7–8 | Code, tests, measurements, debugging |
| Exercises and recall | 2 | Closed-book problems, derivations, traces |
| Writing and review | 2 | Lab report, retrospective, spaced review, commit |
| Buffer | 1 | Overflow, debugging, rest |

If you only have 8 hours/week, use the same proportions and accept a longer calendar. Do not compress the labs.

Use a six-week block: five weeks of new material, one consolidation week for the project increment, review, and cleanup. Add one full buffer week every twelve weeks. A plan without slack is a plan that breaks.

## The study loop

```text
read a bounded section
  -> write the mechanism in your own words
  -> predict an outcome
  -> build or measure
  -> compare prediction with evidence
  -> explain the gap
  -> write the retrospective
  -> revisit after 1 day, 1 week, 1 month
```

If you cannot state a prediction before running the experiment, you are following a tutorial, not studying engineering.

## Using an AI assistant without damaging your learning

Use an assistant for explanation, review, test ideas, and debugging questions. Do not let it produce the artifact you are supposed to learn. A useful rule: the assistant may write at most 10% of a course lab, and you must be able to explain every line you keep. For exercises and exit checks, close the assistant.

## Repository map

```text
curriculum/                 the curriculum itself
  SEF/                      Software Engineering Foundations
  APP/                      Application Engineering
  SYS/                      Systems Engineering
  AI/                       AI Engineering
  SEC/                      Security Engineering
scripts/                     repository checks
```

Learner state — `labs/`, `exercises/`, `notes/`, `projects/`, and `progress.md` — lives in **your own study workspace**, not in this repository. The root [README](../README.md#learner-workspaces) explains how to create one with the scripts.

## Time expectations at a glance

At 15 focused hours/week, one specialisation at a time is realistically 2.5–3.5 years. At 25 hours/week it is 18–24 months. At 35–40 hours/week it is 12–16 months.

## Non-negotiable rules

- Keep secrets, private data, model weights, and copyrighted books out of Git.
- Security work only on systems you own or have explicit written authorization to test.
- Record versions, seeds, hardware, commands, and limitations for every measurement.
- Prefer one primary resource per course. Finish it before adding another.
- Commit small, explain what changed, and keep a runnable artifact.
- Stop and write down a blocker instead of silently substituting a book, dataset, or model.
