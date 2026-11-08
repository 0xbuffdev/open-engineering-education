# SEC8 — AI Security & Authorized Red Teaming

**Program:** SEC — Security Engineering
**Type:** `course`
**Prerequisites:** SEC1, SEC2, SEC7, and AI5 *(legacy mapping; reconcile before activation)*
**Duration:** 4 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/SEC.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Apply security engineering to retrieval systems, tool-using agents, and model-powered applications. Learners examine permissions, prompt injection, data isolation, dangerous outputs, rate limits, escalation, and layered defenses within explicitly authorized environments.

## Learning outcomes

- Identify AI-specific attack surfaces involving retrieval, tools, permissions, and generated outputs.
- Conduct bounded and authorized security tests against a controlled AI system.
- Evaluate isolation, rate limiting, dangerous-action controls, logging, and escalation paths.
- Translate findings into layered mitigations and regression tests.
- Produce a clear AI security assessment and demonstrate the retest results.

## Modules

### Module 1 — AI Attack Surfaces

#### Outcomes

By the end of this module, the learner can:

- Explain **Prompt injection and instruction boundaries** in the context of the course.
- Apply **Retrieval isolation and data access** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Prompt injection and instruction boundaries** — `lesson`
2. **Retrieval isolation and data access** — `lesson`
3. **Checkpoint: AI attack surfaces** — `test`
4. **Micro-lab: Create a benign retrieval-isolation test and observe the boundary.** — `lab`

### Module 2 — Tool & Agent Controls

#### Outcomes

By the end of this module, the learner can:

- Explain **Tool permissions and agent boundaries** in the context of the course.
- Apply **Dangerous tool execution and output handling** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Tool permissions and agent boundaries** — `lesson`
2. **Dangerous tool execution and output handling** — `lesson`
3. **Checkpoint: tool security** — `test`
4. **Micro-lab: Attempt an unauthorized tool path and verify the permission control blocks it.** — `lab`

### Module 3 — Abuse Cases & Defensive Controls

#### Outcomes

By the end of this module, the learner can:

- Explain **AI-specific abuse cases and rate limits** in the context of the course.
- Apply **Layered controls and logging** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **AI-specific abuse cases and rate limits** — `lesson`
2. **Layered controls and logging** — `lesson`
3. **Checkpoint: layered defense** — `test`
4. **Micro-lab: Turn an abuse case into prevention, detection, and recovery controls.** — `lab`

### Module 4 — Authorized Red Teaming & Retest

#### Outcomes

By the end of this module, the learner can:

- Explain **Red-team methodology and evidence** in the context of the course.
- Apply **Remediation and regression testing** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Red-team methodology and evidence** — `lesson`
2. **Remediation and regression testing** — `lesson`
3. **Checkpoint: assessment reasoning** — `test`
4. **Micro-lab: Retest a repaired control using the same bounded attack case.** — `lab`

### Module 5 — AI Security Assessment

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Assess only a controlled AI system or local training application; produce findings, remediation, and retest evidence** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- prompt injection
- retrieval isolation
- tool permissions
- model output risks
- agent boundaries
- dangerous tool execution
- rate limiting
- AI-specific abuse cases
- red-team methodology
- remediation

### Substantial course lab

**AI Security Assessment**

Assess a controlled AI system or local training application, produce findings, implement defenses, and retest.
