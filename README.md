# Learning Lab

A build-first curriculum for people who want to become systems, AI/ML, or security engineers. It starts with programming fundamentals and ends with a capstone you operate, evaluate, or put through a security review.

Learning Lab is the free curriculum from [0xBUFF](https://github.com/0xbuffdev). We build everyday tools for the general public, developer tools, and 0xNAND, a learning platform for engineers who want to understand hard systems.

This repository holds the plan and the evidence log. Each course has its own file, so you can open the page you need. The books stay out of Git.

> Mentorship is optional. The curriculum is free and will stay free. If you want help, I take 3–5 engineers at a time. We make a plan for where you are, review your code and designs, and work through the parts that tutorials skip. [Read how it works](MENTORSHIP.md).

## Start here

1. Read [curriculum/README.md](curriculum/README.md) for the structure and study rules.
2. Read [curriculum/roadmap.md](curriculum/roadmap.md) and choose **one primary track**. Do not start three.
3. Read [curriculum/study-method.md](curriculum/study-method.md) and block the time.
4. Check [curriculum/books/README.md](curriculum/books/README.md) for the local-library policy and exact chapter maps.
5. Check [curriculum/resources.md](curriculum/resources.md) for the one primary external source per course.
6. Create the workspace for the course you are starting, then open its course file and do its labs. Do not create workspaces for later courses.

If you are starting from zero, the first course is [F0 — Setup, Tools & Study System](curriculum/foundations/F0-setup-tools-and-study-system.md). Create its workspace with:

```bash
./scripts/new-course-workspace foundations F0
```

## Repository map

```text
curriculum/                 the curriculum (source of truth)
  README.md                 how the curriculum works
  roadmap.md                realistic pace, sequences, gates, cuts
  study-method.md           how to read, practise, review, and record
  resources.md              primary external sources and legal access
  books/                    per-book chapter/section maps (B1–B6)
  foundations/              F0–F6
  systems/                  S1–S15 core, S16–S17 electives
  ai/                       AI1–AI13 core, AI14–AI19 electives
  security/                 D1–D5, D7–D10 core; D6, D11–D14 electives
  projects/                 P1–P11 ladder, C1–C4 capstones
  appendices/               professional practice, coverage map, glossary

labs/<track>/<CODE>/        experiments and implementation notes
exercises/<track>/<CODE>/   drills, written answers, tests
notes/<track>/<CODE>/       resource log, summary, retrospective
projects/<slug>/            portfolio project created by script
books/                      legal local copies only; ignored by Git
templates/                  workspace starters
scripts/                    workspace creation
progress.md                 completion and evidence log
MENTORSHIP.md               optional 1:1 mentorship, pricing, and policies
LICENSE                     CC BY 4.0 for curriculum text
LICENSE-MIT                 MIT for code, scripts, and templates
```

Tracks use short codes: `foundations`, `systems`, `ai`, `security`; courses use `F0`–`F6`, `S1`–`S17`, `AI1`–`AI19`, `D1`–`D14`.

## Create a course workspace

```bash
./scripts/new-course-workspace foundations F2
./scripts/new-course-workspace systems S1
./scripts/new-course-workspace ai AI6
./scripts/new-course-workspace security D3
```

The script validates that the course exists, then creates:

```text
labs/<track>/<CODE>/README.md
exercises/<track>/<CODE>/README.md
notes/<track>/<CODE>/resources.md
notes/<track>/<CODE>/summary.md
```

The course file is the assignment. The workspace is where you do it. Do not create a workspace for a course you have not reached; an empty directory is not progress.

## Create a project workspace

```bash
./scripts/new-project-workspace ledgerlab
./scripts/new-project-workspace workbenchd
./scripts/new-project-workspace c1-resilient-backend-platform
```

The project brief is in [curriculum/projects/project-ladder.md](curriculum/projects/project-ladder.md) or [curriculum/projects/capstones.md](curriculum/projects/capstones.md). Start only after the stated gate. The script creates the README, design doc, evaluation plan, and retrospective skeleton under `projects/<slug>/`.

## What each course file contains

- purpose, outcomes, prerequisites, and a realistic hour budget;
- required reading with exact chapter and section identifiers (not page numbers);
- a topic checklist grouped into modules;
- labs that produce runnable evidence;
- exercises that force recall and implementation;
- a project increment linked to the ladder;
- an exit check, failure modes, evidence to commit, and optional depth.

A course is complete only when the exit check is demonstrable, the artifact is committed, and the retrospective is written. Reading a chapter is not completion.

## Books and resources

The six core reference books are mapped in [curriculum/books/](curriculum/books/README.md). Maps use chapter and section titles because page numbers differ across print, PDF, and reflowed editions.

- Keep legally obtained PDFs/EPUBs in `books/`; that directory is ignored by Git except for its README.
- Do **not** commit copyrighted books, scans, paywalled chapters, datasets, model weights, credentials, or private data.
- The curriculum works without local books: each course names a legal primary source and an alternative.
- Modern distributed systems, ML, web security, cloud-native security, and AI safety are not covered by the local library. Use [curriculum/resources.md](curriculum/resources.md).

## Progress and evidence

Record completion in [progress.md](progress.md), but only with a link to evidence. A checked box without a reproducible artifact is not progress.

Each substantial lab or project should leave:

- a README with setup, commands, and limitations;
- tests covering normal, boundary, invalid, and failure cases;
- a measurement or evaluation with environment and variance;
- a design/threat model where relevant;
- a retrospective naming one wrong assumption and what changed.

## Tracks

| Track | Entry | Core | Electives | Capstone |
| --- | --- | --- | --- | --- |
| [Foundations](curriculum/foundations/README.md) | none | F0–F6, 720 h | none | P1 |
| [Systems Engineering](curriculum/systems/README.md) | Foundations | S1–S15, 1,110 h | S16–S17 | C1 or C2 |
| [AI & Machine Learning](curriculum/ai/README.md) | Foundations | AI1–AI13, 990 h | AI14–AI19 | C3 |
| [Security Engineering](curriculum/security/README.md) | Foundations + systems prerequisites | D1–D5, D7–D10, 675 h | D6*, D11–D14 | C4 |

\*D6 is the AI-security elective and assumes AI1–AI6 plus AI12. The core Security path does not include it; take it after the AI prerequisites if you target AI security.

At 15 hours a week, one specialization after Foundations is realistically **2.5–3.5 years**. At 25 hours a week it is **18–24 months**. Doing all three tracks at once is not recommended; see the [roadmap](curriculum/roadmap.md) for honest timelines and useful stopping points.

## Working rules

- Security work only on systems you own or have **explicit written authorization** to test.
- Keep secrets, private data, model weights, and copyrighted books out of Git.
- Record versions, seeds, hardware, commands, and limitations for every measurement.
- Prefer one primary resource per course; finish it before adding another.
- Commit small, explain what changed, and keep a runnable artifact.
- Stop and write down a blocker instead of silently substituting a book, dataset, or model.

## Mentorship

I take 3–5 engineers at a time. We start with where you are, make a plan, and review the code and designs you write. I do not write the work for you.

- **Roadmap Audit:** 90 minutes and a written 4-week plan.
- **Guided Month:** two sessions and code review between them.
- **Guided Sprint:** 12 weeks and six sessions, enough for one phase of a track.
- **Async Review:** a written review of a project or PR, plus a 30-minute call.
- **Group Cohort:** six weeks with a small group.

[Read the plans and apply](MENTORSHIP.md).

## License

Curriculum text and course materials are licensed under [CC BY 4.0](LICENSE). Code samples, scripts, and templates are licensed under [MIT](LICENSE-MIT). Attribution: © 2026 Christopher S. Aondona.

## Reference

- [Professional practice](curriculum/appendices/professional-practice.md): the standard the evidence must meet.
- [Coverage map](curriculum/appendices/coverage-map.md): every course, topic, and deliberate boundary.
- [Glossary](curriculum/appendices/glossary.md): precise working definitions.
- [Study method](curriculum/study-method.md): the weekly loop and review cadence.
