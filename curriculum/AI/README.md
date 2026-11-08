# Program 4 — AI: AI Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · [Historical source at 0e14d4ff5808](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md)

**Migration status:** The course documents below are preserved historical drafts and **not yet conforming to OEE v0.2.0**. Their old curriculum sequence and prerequisites must be reviewed; the source's books, chapters, and other resource assignments stay in the content repository.

## Overview

AI Engineering turns the programming and mathematics from the foundations program into practical machine learning. You work through data, classical machine learning, deep learning, transformers and language models, retrieval and agents, training and evaluation, and production AI systems. The program stresses reproducible experiments and measurable evaluation, so you learn to operate models, measure their behavior, and document their limits.

## Prerequisites

**Program 1 — SEF — Software Engineering Foundations.**

Python and the mathematics covered in SEF6 are used throughout the program. Individual AI courses have their own explicit prerequisites; systems preparation is recommended where noted.

## Learning outcomes

By the end of this program, you will be able to:

- Prepare, inspect, and analyze datasets using reproducible scientific Python workflows.
- Explain and implement the mathematical and optimization foundations behind common machine-learning methods.
- Train, evaluate, and compare classical machine-learning and deep-learning models using appropriate baselines and metrics.
- Explain transformer architectures, attention, tokenization, causal masking, and the basic mechanics of language models.
- Build bounded retrieval and tool-using AI systems with explicit evaluation, permissions, and failure controls.
- Fine-tune and evaluate models while controlling for contamination, memorization, and misleading evaluation results.
- Deploy observable AI services and reason about latency, throughput, resource use, cost, rollback, and reliability.
- Identify AI risks, define measurable controls, and ship a production-grade AI system with documented limitations and safeguards.

## Program completion standard

The learner must demonstrate the knowledge, practical skills, and engineering judgment described by the program outcomes and successfully complete the program capstone.

## Courses

| Code | Course | Type | Duration |
| --- | --- | --- | --- |
| [AI1](AI1.md) | Data & Scientific Python | `course` | 5 weeks |
| [AI2](AI2.md) | Machine Learning Foundations | `course` | 6 weeks |
| [AI3](AI3.md) | Deep Learning & Representation Learning | `course` | 6 weeks |
| [AI4](AI4.md) | Transformers & Large Language Models | `course` | 7 weeks |
| [AI5](AI5.md) | Retrieval, Agents & Applied Generative AI | `course` | 6 weeks |
| [AI6](AI6.md) | Training, Fine-Tuning & Evaluation | `course` | 5 weeks |
| [AI7](AI7.md) | Production AI Systems & MLOps | `course` | 6 weeks |
| [AI8](AI8.md) | Responsible AI, Safety & Governance | `course` | 3 weeks |
| [AI9](AI9.md) | AI Engineering Capstone | `project` | 8–10 weeks |

## Required next review

1. Reconcile original prerequisites against today's OEE SEF/APP course codes and the full program dependency graph.
2. Review the learning outcomes and lesson progression under [Course Format](../../spec/course-format.md) and the one-primary-objective-per-lesson guidance in [Curriculum Design Guide](../DESIGN-GUIDE.md).
3. Give the course observable, stable outcome IDs and required summative assessment IDs, with public work, success criteria, and proportionate evidence for **every** required outcome.
4. Treat old module checkpoint and micro-lab placements as **historical proposals**, not mandatory `v0.2.0` completion gates.
5. Specify safe, reproducible experimentation and a reviewable technical defense when substantial project outcomes require it.
6. Preserve book/resource mappings **outside OEE**, keyed by OEE course codes in the content repository.
7. Verify educational coverage manually. A structurally valid file or `draft` status does not constitute course or implementation conformance.
