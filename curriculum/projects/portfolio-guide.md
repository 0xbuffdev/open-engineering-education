# Portfolio Guide

A portfolio is not a list of repositories. It is a small set of artifacts that let a stranger judge how you think, build, measure, and recover. Two or three deep projects beat eleven unfinished ones.

## Choose the story before the projects

Pick a target role and one sentence you want a reviewer to believe:

- "I can build and operate a concurrent service with evidence."
- "I can build a durable storage/distributed system and state its guarantees."
- "I can build an evaluated ML/LLM system, not just a demo."
- "I can find, fix, and verify security weaknesses under scope."

Then choose the minimum projects that support that sentence:

| Story | Core artifacts | Supporting evidence |
| --- | --- | --- |
| Backend/platform | P4 + C1 | SLO, load test, rollback, incident postmortem |
| Storage/distributed | P5 + P6 + C2 | crash matrix, fault matrix, safety argument |
| Applied AI | P7 + P9 + C3 | dataset/model card, eval set, red-team, serving benchmark |
| AI infrastructure | P4 + P9 + S13 | memory calculator, throughput/latency, cost |
| Security engineering | P10 + P11 + C4 | threat model, fixes, retest, residual risk |
| Performance | P3 + P4 | memory mountain, false sharing, profile-driven fix |

Do not lead with a tutorial clone. Lead with the failure you found and the design change it caused.

## The three-artifact portfolio

1. **A deep system** (C1, C2, C3, or C4).
2. **A measurement/evaluation artifact** that proves a claim.
3. **A security/operations artifact** that shows you can handle failure and boundaries.

The same capstone can supply all three if it is genuinely complete.

## Case study format

Each project gets a one-page case study with:

```markdown
# <project> — <one-line claim>

## Problem and user
Who has the problem, and why a simpler tool is insufficient.

## Scope and non-goals
What I built, what I deliberately did not build, and the boundary.

## Architecture
One diagram; the two decisions that mattered.

## Evidence
The test/benchmark/fault matrix. Baseline vs candidate. Reproduce command.

## Biggest failure
What broke, how I found it, what changed. Link the issue/commit/test.

## Security and operations
Threat model, authorization, limits, rollback, residual risk.

## Limitations
What the evidence does not prove; the next experiment.
```

If you cannot fill "biggest failure" with a real example, the project is probably a demo.

## README standard

A reviewer should understand the project in five minutes:

- one-paragraph problem and claim;
- architecture diagram;
- quick start from a clean environment;
- exact test/evaluation commands;
- results table with baseline;
- limitations and non-goals;
- security/authorization note;
- license and data provenance.

No screenshots of code. No "coming soon." No checkboxes that are not true.

## Demo standard

A five-minute demo should show:

1. the user-visible behavior;
2. one failure or boundary case;
3. the evidence that backs the main claim;
4. the rollback/recovery path;
5. one limitation you would fix next.

Practice it without a network dependency. Record a short video only after the live demo works.

## Claims discipline

Use precise verbs:

- "reduced p95 latency from X to Y on hardware Z under workload W" — good;
- "optimized performance" — meaningless;
- "evaluated on a held-out set of N examples with metric M" — good;
- "state-of-the-art" — almost certainly false for a learning project;
- "production-ready" — only with SLOs, monitoring, auth, backups, and a rollback you have tested.

For every number, be ready for:

- What was the baseline?
- What was the workload and hardware?
- How many runs, and what was the variance?
- What did the measurement not include?
- What would make the result invalid?

## Security and privacy

- Do not publish real credentials, personal data, private corpora, or live malware.
- Sanitize packet captures, logs, screenshots, and evidence.
- State authorization for any security assessment.
- Use synthetic or licensed data; link to the source and license.
- Remove secrets from Git history, not just the latest commit.
- Add a threat model for anything networked or AI-driven.

## What to put on a CV

For each selected project, two lines:

```text
<Project> — <stack>. <one measurable claim>.
<Evidence: tests/fault matrix/eval; link>.
```

Example:

```text
workbenchd — Rust TCP service with bounded queues and graceful shutdown.
Sustained 12k req/s at p99 < 40 ms on 4 vCPU; 0 leaked tasks across 200 shutdown cycles.
```

Only use numbers you can reproduce. Keep the repository public if it contains no sensitive material; otherwise provide a sanitized case study and offer a walkthrough.

## Interview preparation

Be ready to:

- draw the architecture from memory;
- trace one request end to end;
- explain the hardest bug and the evidence that found it;
- defend a trade-off and name the alternative;
- calculate a capacity or memory number;
- explain what happens under a crash, partition, or overload;
- describe a security boundary and what you did not test;
- say what you would do with two more weeks.

A good answer includes uncertainty. "I measured X on this hardware; I did not test Y, so I would not claim Z" is stronger than confident hand-waving.

## Portfolio maintenance

- Keep one index page linking the selected artifacts.
- Re-run the clean-checkout test before applying.
- Update versions and broken links quarterly.
- Archive abandoned projects instead of leaving them half-explained.
- Remove claims you can no longer reproduce.

## Red flags

- Many repositories, no tests.
- A demo video but no runnable setup.
- Metrics without baseline or hardware.
- "Production-ready" with no auth, monitoring, or backup.
- Security findings against public systems without authorization.
- Private data or API keys in commit history.
- A capstone that is only a UI over an API call.
- No failure story.

## The final test

Give the repository and case study to a working engineer you do not know. Ask:

1. What does this person claim?
2. What evidence supports it?
3. What is the biggest weakness?
4. Would you interview them for the target role?

If they cannot answer 1 and 2 in ten minutes, improve the README and case study before adding another project.
