# Practice Backlog

This directory turns the curriculum into work you can begin later without deciding what to build from scratch. The exact readings, prerequisites, and exit checks remain in [curriculum.md](../curriculum.md); these guides supply the bounded labs and exercises that produce the evidence for those exit checks.

| Track | Practical guide |
| --- | --- |
| Foundations | [foundations.md](foundations.md) |
| Systems Engineering | [systems-engineering.md](systems-engineering.md) |
| AI & Machine Learning | [ai-machine-learning.md](ai-machine-learning.md) |
| Security Engineering | [security-engineering.md](security-engineering.md) |

## How to use a course brief

1. Confirm the prerequisites and acquire required material in `curriculum.md` and [resources/README.md](../resources/README.md).
2. Create the workspace with `./scripts/new-course-workspace <track> <course-slug>`. It adds a `PRACTICE.md` link to the correct guide.
3. Complete the core lab(s) first. Record the question, environment, reproducible procedure, raw-result location, and interpretation.
4. Complete the exercises in the stated order. Do not replace implementation exercises with library calls that hide the mechanism being learned.
5. Use the course exit check as the final oral/written demonstration. Link all evidence from the course summary.

## Rules that apply everywhere

- Prefer small, deterministic inputs and commit source, test fixtures, scripts, and concise reports. Keep generated outputs, large datasets, model weights, secrets, and private logs out of Git.
- State a prediction before collecting a measurement. A graph without a question, environment, and interpretation is not a completed systems/AI lab.
- Record versions, seeds, hardware, and commands whenever a result could change across machines or runs.
- Use only licensed or public data and locally controlled services. Security work is restricted to intentionally vulnerable targets, training platforms, or systems you have explicit written authority to assess.
- Stop and write down a blocker rather than silently substituting a different book, dataset, model, or platform. Put the decision in the course resource note.

## Evidence rubric

| Artifact | Minimum evidence |
| --- | --- |
| Exercise | problem restatement, solution or reasoning, tests/worked cases, complexity or trade-off, correction to one mistake |
| Lab | question, setup, procedure, raw evidence, interpretation, limitation, next experiment |
| ML experiment | dataset card, split, baseline, metric rationale, error analysis, reproducible run command |
| Security activity | scope/authorization, harmless evidence, affected control, remediation, regression/retest; never publish working exploit payloads |
| Project | design, setup, automated test/evaluation, benchmark or evaluation report, limitations, retrospective |
