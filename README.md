# Open Engineering Education (OEE)

**An open standard for how software engineering is taught and proven, plus a reference curriculum that follows it.**

OEE® is written principles, a course-file format, evidence rules, and public status labels, and the curriculum built to those rules: Foundations, Systems, AI/ML, and Security tracks with exact chapter maps, labs that leave runnable evidence, and exit checks that must be demonstrated.

**Status:** `v0.0.1` draft. The standard is not final, every course is currently labeled [`draft`](spec/status-labels.md), and nothing here has been verified yet. Nothing is published as final.

- **Steward:** [0xBUFF®](https://github.com/0xbuffdev)
- **Author:** Christopher S. Aondona
- **License:** [CC BY 4.0](LICENSE) for text, [MIT](LICENSE-MIT) for code.

> 0xBUFF, the steward of this standard, offers optional paid mentorship separately. The standard does not require it.

## The principles

1. **Evidence over completion.** A course is done when its exit check is demonstrable and the artifact runs from a clean checkout. Reading is not completion.
2. **Mechanism before tooling.** Explain what happens underneath before leaning on a framework.
3. **Honest claims.** Every course and result states its limits; status labels are public.
4. **Open by default, paid where it costs to run.** The curriculum is free forever, and the line is written down.

Full text with what each one rules out: [spec/principles.md](spec/principles.md).

## Free and paid

This line is written down and never moves silently; changing it requires an [RFC](rfcs/README.md).

### Always free, forever, in this repository

- The standard: `spec/` (principles, course format, evidence rules, status labels)
- All course files, book maps, resource maps, glossary, roadmap, project ladder, capstones
- Public lab specs and public exercises
- Templates and workspace scripts
- Study method and professional-practice appendix

### Paid, outside this repository

- Hidden-test grading and the grading harness
- Code-execution sandbox and instructor agent with per-student memory
- Throughline visualizations, the Prove arena, and certificates
- Cohort access, live sessions, and mentor review, offered by 0xBUFF (disclosure above)

Hidden tests and grading harnesses are deliberately **not** here: they cannot be cloned by copying a repository, and they cost money to run. Everything needed to learn from this curriculum is in the free layer.

## Start here

1. Read [curriculum/README.md](curriculum/README.md) for the structure and study rules.
2. Read [curriculum/roadmap.md](curriculum/roadmap.md) and choose **one primary track**. Do not start three.
3. Read [curriculum/study-method.md](curriculum/study-method.md) and block the time.
4. Check [curriculum/books/README.md](curriculum/books/README.md) for the local-library policy and exact chapter maps.
5. Check [curriculum/resources.md](curriculum/resources.md) for the one primary external source per course.
6. Create your study workspace (below), start [F0 — Setup, Tools & Study System](curriculum/foundations/F0-setup-tools-and-study-system.md), and work in it.

## Your study workspace

**Do not commit learner work to this repository.** Labs, exercises, notes, projects, and your progress log live in *your own* workspace repository. This repo ships the templates and the scripts that fill them.

Create your workspace, then run the script from its root (the script reads the curriculum from a clone of this repository and writes into your workspace):

```bash
git clone git@github.com:0xbuffdev/open-engineering-education.git
mkdir my-study-workspace && cd my-study-workspace && git init
../open-engineering-education/scripts/new-course-workspace foundations F0
```

```bash
# or name the target explicitly from anywhere:
./scripts/new-course-workspace foundations F0 /path/to/my-study-workspace
./scripts/new-course-workspace systems S1          # OEE_WORKSPACE=/path also works
./scripts/new-project-workspace ledgerlab /path/to/my-study-workspace
```

The script validates that the course exists, then creates `labs/`, `exercises/`, and `notes/` for it in your workspace, linking back to the course file here. Project briefs stay canonical in the curriculum; your implementation goes in your workspace. Start only the course you are actually on; an empty directory is not progress.

The full starter content lives in [templates/](templates/README.md), including [templates/progress.md](templates/progress.md), the evidence log you copy into your workspace.

## Repository map

```text
README.md                  what it is, draft status, who stewards it
spec/                      the standard itself
  principles.md            the four principles and what each rules out
  course-format.md         required sections of a course file
  evidence-rules.md        what counts as an exit check and demonstrable artifact
  status-labels.md         draft / tested / verified, and what each requires
  conformance.md           what "conforms to OEE" means (deliberately unwritten)
curriculum/                the reference curriculum (the tracks)
  roadmap.md  study-method.md  resources.md
  books/                    per-book chapter/section maps (B1–B6)
  foundations/              F0–F6
  systems/                  S1–S15 core, S16–S17 electives
  ai/                       AI1–AI13 core, AI14–AI19 electives
  security/                 D1–D5, D7–D10 core; D6, D11–D14 electives
  projects/                 P1–P11 ladder, C1–C4 capstones
  appendices/               professional practice, coverage map, glossary
templates/                  workspace starters (course, project, progress log)
scripts/                    workspace creation and repository checks
governance/                 GOVERNANCE, CONTRIBUTING, CODE_OF_CONDUCT, DCO
rfcs/                       proposals for spec or curriculum changes
NOTICE  AUTHORS  CITATION.cff  TRADEMARKS.md
LICENSE                     CC BY 4.0 (spec and curriculum text)
LICENSE-MIT                 MIT (code, scripts, templates)
.github/                    issue templates and CI (DCO, links, markdown lint)
```

## Course status labels

| Label | Meaning |
| --- | --- |
| `draft` | Written, not yet run by a learner. |
| `tested` | One learner completed it; revised from their feedback. |
| `verified` | Multiple learners completed it; reproduced and reviewed. |

**Every course in this repository is `draft` today.** Labels move only on evidence; see [spec/status-labels.md](spec/status-labels.md) for the requirements and where labels appear.

## Tracks

| Track | Entry | Core | Electives | Capstone |
| --- | --- | --- | --- | --- |
| [Foundations](curriculum/foundations/README.md) | none | F0–F6, 720 h | none | P1 |
| [Systems Engineering](curriculum/systems/README.md) | Foundations | S1–S15, 1,110 h | S16–S17 | C1 or C2 |
| [AI & Machine Learning](curriculum/ai/README.md) | Foundations | AI1–AI13, 990 h | AI14–AI19 | C3 |
| [Security Engineering](curriculum/security/README.md) | Foundations + systems prerequisites | D1–D5, D7–D10, 675 h | D6*, D11–D14 | C4 |

\*D6 is the AI-security elective and assumes AI1–AI6 plus AI12. The core Security path does not include it.

At 15 hours a week, one specialization after Foundations is realistically **2.5–3.5 years**. At 25 hours a week it is **18–24 months**. Doing all three tracks at once is not recommended; see the [roadmap](curriculum/roadmap.md) for honest timelines and useful stopping points.

## What each course file contains

Purpose, outcomes, prerequisites, and a realistic hour budget · required reading with exact chapter and section identifiers (never page numbers) · a topic checklist grouped into modules · labs that produce runnable evidence · exercises that force recall · a project increment linked to the ladder · an exit check, common failure modes, evidence to commit, and optional depth. The required structure is [spec/course-format.md](spec/course-format.md).

## Working rules

- Security work only on systems you own or have **explicit written authorization** to test.
- Keep secrets, private data, model weights, and copyrighted books out of Git.
- Record versions, seeds, hardware, commands, and limitations for every measurement.
- Prefer one primary resource per course; finish it before adding another.
- Commit small, explain what changed, and keep a runnable artifact.
- Stop and write down a blocker instead of silently substituting a book, dataset, or model.

## Contributing

Start with [governance/CONTRIBUTING.md](governance/CONTRIBUTING.md): DCO sign-off (`git commit -s`), what is in scope, and the starter issues. Changes to the standard go through an [RFC](rfcs/README.md). [governance/GOVERNANCE.md](governance/GOVERNANCE.md) covers the single-steward model and how decisions are recorded. Everyone in community spaces is covered by the [code of conduct](governance/CODE_OF_CONDUCT.md).

## License and attribution

Curriculum text and the spec are licensed under [CC BY 4.0](LICENSE). Code, scripts, and templates are licensed under [MIT](LICENSE-MIT). Open Engineering Education® (OEE®), 0xBUFF®, and 0xNAND® are registered trademarks, and names and marks are not licensed; see [TRADEMARKS.md](TRADEMARKS.md).

Attribution: © 2026 0xBUFF. Created by Christopher S. Aondona; stewarded by 0xBUFF (see [NOTICE](NOTICE)). To cite this work, see [CITATION.cff](CITATION.cff).

## Reference

- [spec/](spec/principles.md): the standard itself: principles, course format, evidence rules, status labels.
- [Professional practice](curriculum/appendices/professional-practice.md): the standard the evidence must meet.
- [Coverage map](curriculum/appendices/coverage-map.md): every course, topic, and deliberate boundary.
- [Glossary](curriculum/appendices/glossary.md): precise working definitions.
- [Study method](curriculum/study-method.md): the weekly loop and review cadence.
