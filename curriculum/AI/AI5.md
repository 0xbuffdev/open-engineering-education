# AI5 — Retrieval, Agents & Applied Generative AI

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** AI4 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Move from model understanding to AI application engineering through retrieval, tool use, agent loops, permissions, prompt/tool boundaries, evaluation, and failure analysis.

## Learning outcomes

- Design a retrieval pipeline and evaluate retrieval quality.
- Build bounded tool-using or agentic workflows with explicit permissions.
- Separate durable knowledge, transient state, tool execution, and model generation concerns.
- Test retrieval failures, tool failures, and prompt-injection risks in a controlled environment.
- Evaluate an AI workflow using reproducible cases rather than anecdotal prompts.

## Modules

### Module 1 — Retrieval Foundations

#### Outcomes

By the end of this module, the learner can:

- Explain **Embeddings and retrieval** in the context of the course.
- Apply **Chunking, ranking, and retrieval quality** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Embeddings and retrieval** — `lesson`
2. **Chunking, ranking, and retrieval quality** — `lesson`
3. **Checkpoint: retrieval design** — `test`
4. **Micro-lab: Compare two chunking strategies on a small corpus.** — `lab`

### Module 2 — RAG Pipelines

#### Outcomes

By the end of this module, the learner can:

- Explain **Retrieval-augmented generation** in the context of the course.
- Apply **Grounding and citations** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Retrieval-augmented generation** — `lesson`
2. **Grounding and citations** — `lesson`
3. **Checkpoint: grounded generation** — `test`
4. **Micro-lab: Build a retrieval step that returns evidence with each generated answer.** — `lab`

### Module 3 — Tool Use & Structured Outputs

#### Outcomes

By the end of this module, the learner can:

- Explain **Tool calling and structured outputs** in the context of the course.
- Apply **Permissions and bounded action spaces** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Tool calling and structured outputs** — `lesson`
2. **Permissions and bounded action spaces** — `lesson`
3. **Checkpoint: tool boundary design** — `test`
4. **Micro-lab: Allowlist one tool and reject an unapproved call.** — `lab`

### Module 4 — Agents, Memory & Injection

#### Outcomes

By the end of this module, the learner can:

- Explain **Agent loops, state, and memory** in the context of the course.
- Apply **Prompt injection and failure evaluation** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Agent loops, state, and memory** — `lesson`
2. **Prompt injection and failure evaluation** — `lesson`
3. **Checkpoint: agent failure modes** — `test`
4. **Micro-lab: Construct a benign injection test and verify the control blocks the unsafe path.** — `lab`

### Module 5 — Bounded RAG/Tool-Using Agent

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, evaluate, red-team, and document the Bounded RAG/Tool-Using Agent** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- embeddings
- retrieval
- chunking
- ranking
- RAG
- tool calling
- structured outputs
- agent loops
- state and memory
- tool permissions
- prompt injection
- evaluation

### Labs

- retrieval experiment
- retrieval failure analysis
- tool allowlisting
- prompt-injection test
- citation evaluation

### Substantial course lab

**Bounded RAG/Tool-Using Agent**

The system must include:

- licensed corpus
- citations
- allowlisted tools
- evaluation dataset
- failure tests
- human stop/control
- logs
