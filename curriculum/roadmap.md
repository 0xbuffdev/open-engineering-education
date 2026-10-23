# Realistic Roadmap

This roadmap replaces the optimistic calendar in the old `curriculum.md`. It assumes you are building professional competence, not collecting certificates or watching playlists.

## Assumptions

- **Default pace:** 15 focused hours/week, measured with a timer.
- **Focused** means reading with notes, writing code, debugging, testing, measuring, or writing. It does not mean passive video, tab-hopping, or setup fiddling.
- **Prior knowledge:** high-school algebra and basic computer use. No prior programming is assumed.
- **Course hours include** the reading, labs, exercises, project increment, and write-up for that course.
- **Buffer:** every calendar estimate below adds 20% for illness, work spikes, debugging rabbit holes, and life.
- **One primary track at a time.** A second track is added only after the first track's capstone, and only as selected courses.

If your real pace is 8 hours/week, multiply the calendar by about 1.8. If it is 25 hours/week, multiply by about 0.6. If it is 35–40 hours/week, multiply by about 0.4.

## The honest timeline

| Path | Foundations | Specialisation | Capstone | Total hours | 15 h/wk | 25 h/wk | 40 h/wk |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Systems Engineering | 720 h | 1,110 h | 180 h | **2,010 h** | ~3.1 years | ~22 months | ~14 months |
| AI & Machine Learning | 720 h | 990 h | 180 h | **1,890 h** | ~3.0 years | ~21 months | ~13 months |
| Security Engineering | 720 h | 1,305 h* | 180 h | **2,205 h** | ~3.4 years | ~24 months | ~15 months |
| All three tracks | shared | shared | shared | **4,200–4,800 h** | **6–8 years** | **4–5 years** | **2.5–3 years** |

\*Security includes the systems prerequisites S1, S2, S5, S6, S10, S11, and S14. D6 is an AI-security elective requiring AI1–AI6 and AI12; it is not counted in this core path.

These are not motivational numbers. They are planning numbers. A 2.5–3.5 year part-time path to a first professional role in one track is realistic; a 12-month path to all three is not.

## What "professional" means here

You are not done when you have read the books. You are done with a course when you can:

1. explain the mechanism from memory;
2. predict behaviour before running code;
3. build a small system that demonstrates it;
4. measure or test it reproducibly;
5. diagnose a failure from evidence;
6. write a short report another engineer can follow;
7. state the limitations and the next experiment.

The project ladder is where those seven abilities become a portfolio.

## Choose one path

### Path A — Systems Engineering (recommended default)

Best for: backend, infrastructure, performance, storage, distributed systems, AI infrastructure, security foundations.

| Phase | Courses | Course-weeks | Project spine | Gate |
| --- | --- | ---: | --- | --- |
| 0. Setup | F0 | 1 | environment + study system | reproducible setup |
| 1. Programming and math | F1, F2, F4 | 28 | **P1 ledgerlab** | tested CLI + math notebook |
| 2. Engineering and data | F3, F5, F6 | 19 | P1 hardened, **P2 sysprobe** starts | C/Rust/SQL/HTTP evidence |
| 3. Systems core | S1–S10 | 47 | **P2 sysprobe → P3 cachebench → P4 workbenchd** | service survives failure tests |
| 4. Distributed and storage | S11, S12 | 13 | **P5 minikv → P6 raftkv** | crash and partition proof |
| 5. Infrastructure and reliability | S13, S14, S15 | 14 | P4/P9 deployment, SLOs, incident drill | measured SLO + rollback |
| 6. Capstone | C1 or C2 | 12 | hardened portfolio system | design + evaluation + retrospective |

Course-weeks: 134. Calendar at 15 h/wk with 20% buffer: **~3.1 years**. At 25 h/wk: **~22 months**.

Critical path: `F1 → F2 → F3 → S1 → S2 → S3 → S4 → S6 → S9 → S10 → S11 → S12 → capstone`. S5 can run beside S4. S7/S8 can run beside S9. S10 can start after S6 even if S7–S9 are unfinished.

### Path B — AI & Machine Learning

Best for: data/ML engineering, applied AI, LLM systems, AI product engineering, MLOps.

| Phase | Courses | Course-weeks | Project spine | Gate |
| --- | --- | ---: | --- | --- |
| 0. Setup | F0 | 1 | environment + study system | reproducible setup |
| 1. Programming and math | F1, F2, F4 | 28 | **P1 ledgerlab** | tested CLI + math notebook |
| 2. Engineering and data | F3, F6, F5 recommended | 13–19 | P1 hardened | tests, SQL, HTTP, Git |
| 3. AI foundations | AI1–AI6, AI13 | 37 | **P7 signal-score → P8 tinygpt** | reproducible evaluation |
| 4. Training and serving | AI7–AI10 | 20 | **P9 doc-compass** | bounded agent + eval suite |
| 5. Production and governance | AI11, AI12 | 9 | P9 deployment + system card | rollback + risk register |
| 6. Capstone | C3 | 12 | hardened model/service | model card + eval + incident plan |

Course-weeks: 120–126. Calendar at 15 h/wk with 20% buffer: **~3 years**. At 25 h/wk: **~21 months**.

Critical path: `F1 → F2 → F4 → AI1 → AI2 → AI3 → AI4 → AI5 → AI6 → AI7 → AI9/AI10 → AI11 → AI12 → capstone`. AI13 can run beside AI3–AI6. AI8 is optional unless you target training infrastructure. S9/S11 are strong supporting courses for AI9/AI8.

### Path C — Security Engineering

Best for: application security, cloud security, detection/incident response, security engineering, authorized offensive work.

| Phase | Courses | Course-weeks | Project spine | Gate |
| --- | --- | ---: | --- | --- |
| 0. Setup | F0 | 1 | environment + isolated lab | authorized lab only |
| 1. Programming and math | F1, F2, F4 | 28 | **P1 ledgerlab** | tested CLI + crypto math |
| 2. Engineering and data | F3, F5, F6 | 19 | P1 hardened, **P2 sysprobe** | C/Rust/SQL/HTTP evidence |
| 3. Systems prerequisites | S1, S2, S5, S6, S10, S11, S14 | 42 | **P4 workbenchd**, **P5 minikv** | service and storage proof |
| 4. Security core | D1–D5 | 27 | **P10 secure-review**, **P11 assessment** | threat model + verified fix |
| 5. Security depth | D7–D10 | 18 | P11 extended to cloud/detection | detection + retest |
| 6. Capstone | C4 | 12 | authorized assessment | scope + evidence + residual risk |

Course-weeks: 147. Calendar at 15 h/wk with 20% buffer: **~3.4 years**. At 25 h/wk: **~24 months**.

D6 is an AI-security elective, not part of this core path. Add it only after AI1–AI6 and AI12 (105 h for AI6 and 60 h for AI12, plus 375 h for AI1–AI5), and extend P11 with the AI red-team work.

Critical path: `F1 → F2 → F3 → S1 → S2 → S5 → S6 → S10 → S11 → S14 → D1 → D2/D3 → D4 → D5 → D7/D8 → capstone`. D1 can start as soon as Foundations is complete; D2 waits for S2/S5, D3 for S10, D4 for D2/D3/S11, and D8 for S14.

## If you only have 8–10 hours/week

Choose a narrower outcome, not a shorter version of everything:

- **Junior Python/data role:** F0–F3 + F6 + AI1 + AI3 + P1/P7. Stop there and get paid experience before continuing.
- **Junior systems/ops role:** F0–F3 + F5 + S1–S5 + S9/S10 + P2/P4. Add S11–S12 later.
- **Junior AppSec role:** F0–F3 + F6 + S1/S10 + D1/D3/D9 + P1/P10. Add D2/D4 later.
- **AI product role:** F0–F3 + F6 + AI1–AI4 + AI10–AI12 + P7/P9. Add AI6/AI7 later.

A narrower path finished is worth more than a broad path abandoned.

## Weekly plan that actually fits

Default 15-hour week:

| Day | Time | Activity |
| --- | ---: | --- |
| Mon | 2 h | Read the week's section; write mechanism notes |
| Tue | 2.5 h | Lab/implementation |
| Wed | 2 h | Exercises and closed-book recall |
| Thu | 2.5 h | Lab/implementation; tests |
| Fri | 1.5 h | Debug, measure, commit |
| Sat | 3 h | Project increment or catch-up |
| Sun | 1.5 h | Review, retrospective, next-week plan |

If a day is lost, do not steal from sleep. Drop the lowest-value activity: usually extra reading, not the lab.

## Six-week block

| Week | Focus |
| --- | --- |
| 1 | Read + core implementation |
| 2 | Exercises + first tests |
| 3 | Lab variants + measurement |
| 4 | Project increment |
| 5 | Failure cases + write-up |
| 6 | Consolidation: review, refactor, exit check, retrospective |

Add a **buffer week** after every two blocks. Use it for unfinished labs, spaced review, or rest. Do not fill it in advance.

## Milestones and employability gates

| Gate | Evidence | What it unlocks |
| --- | --- | --- |
| G0 — Setup | reproducible environment, Git recovery drill, study log | start F1 |
| G1 — Programmer | P1 tested CLI, F2 implementations, C drills | junior Python/automation work |
| G2 — Systems | P2 sysprobe + P4 workbenchd survive failure tests | junior systems/backend roles |
| G3 — Storage/distributed | P5 minikv + P6 raftkv fault proofs | infrastructure/storage roles |
| G4 — ML | P7 signal-score + P8 tinygpt with reproducible evaluation | junior ML/data roles |
| G5 — Applied AI | P9 doc-compass with bounded tools, evals, observability | AI product/LLM roles |
| G6 — Security | P10 secure-review + P11 authorized assessment | AppSec/security engineering roles |
| G7 — Capstone | one hardened system, design doc, evaluation, retrospective | portfolio and interviews |

Do not put a project on your CV unless you can reproduce it from a clean checkout, explain its biggest failure, and show the evidence that changed your design.

## What to cut when you fall behind

Cut in this order:

1. Optional depth sections inside a course.
2. Elective courses (S16–S17, AI14–AI19, D6, D11–D14).
3. Extra practice problems beyond the required minimum.
4. A second specialisation.

Do **not** cut:

- the course exit check;
- tests and failure cases;
- the project increment;
- the retrospective;
- security/authorization boundaries;
- sleep and recovery.

## Stopping points that are genuinely useful

- After **F0–F3 + P1**: you can automate real work in Python and use Git/tests responsibly.
- After **S1–S5 + P2**: you understand processes, memory, caches, and can debug C/Rust systems.
- After **S6/S10 + P4**: you can build a concurrent network service and reason about shutdown/failure.
- After **S11/S12 + P6**: you can build and test a small durable distributed system.
- After **AI3 + P7**: you can build an honest tabular ML baseline and evaluation.
- After **AI6 + P8**: you understand transformers well enough to debug and evaluate a small LLM.
- After **D1/D3 + P10**: you can threat-model and review a web service.
- After **D4/D7 + P11**: you can run an authorized assessment and write a developer-actionable report.

## Burnout rules

- Sleep is part of the curriculum.
- One full rest day per week, no study.
- If you miss two weeks, restart at the last completed exit check; do not try to "catch up" by skipping labs.
- Keep a one-paragraph weekly log. If three weeks in a row feel like grinding without evidence, change the project increment, not the whole plan.
- Talk to working engineers. A 30-minute conversation can correct a month of wrong assumptions.

## Progress tracking

Use [../progress.md](../progress.md) for course completion and [../projects/](../projects/) for portfolio work. A checked box without a link to evidence is not progress.

At the end of each month, answer:

1. What can I now build that I could not build last month?
2. What did I measure, and what did the measurement change?
3. What is the weakest part of my evidence?
4. What is the next smallest deliverable?
