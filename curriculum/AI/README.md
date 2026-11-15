# Program 4 — AI: AI Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [SYS](../SYS/README.md) · Next: [SEC](../SEC/README.md)

## Overview

AI Engineering turns the programming and mathematics from the foundations program into practical machine learning. You work through data, classical machine learning, deep learning, transformers and language models, retrieval and agents, training and evaluation, and production AI systems. The program stresses reproducible experiments and measurable evaluation, so you learn to operate models, measure their behavior, and document their limits.

## Prerequisites

**Program 1 — SEF — Software Engineering Foundations.**

Python and the mathematics covered in SEF8 are used throughout the program. Individual AI courses have their own explicit prerequisites; systems preparation is recommended where noted.

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

The nine published course files are **legacy drafts**. They preserve their original learning activities and completion requirements but have not been migrated or assessed against the `v0.2.0` outcome-driven contract. They are course outlines for study and review, not claims of learner-tested readiness or `v0.2.0` conformance. See the [curriculum inventory](../INVENTORY.md) for a reproducible structural audit.

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [AI1](AI1.md) | Data & Scientific Python | 5 weeks | SEF2 and SEF8 | `course` |
| [AI2](AI2.md) | Machine Learning Foundations | 6 weeks | AI1 | `course` |
| [AI3](AI3.md) | Deep Learning & Representation Learning | 6 weeks | AI2 | `course` |
| [AI4](AI4.md) | Transformers & Large Language Models | 7 weeks | AI3 | `course` |
| [AI5](AI5.md) | Retrieval, Agents & Applied Generative AI | 6 weeks | AI4 | `course` |
| [AI6](AI6.md) | Training, Fine-Tuning & Evaluation | 5 weeks | AI4 | `course` |
| [AI7](AI7.md) | Production AI Systems & MLOps | 6 weeks | AI5 and AI6 | `course` |
| [AI8](AI8.md) | Responsible AI, Safety & Governance | 3 weeks | AI5 | `course` |
| [AI9](AI9.md) | AI Engineering Capstone | 8–10 weeks | AI1–AI8 | `project` |

The course files remain the authoritative source for each course's published work and prerequisites. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment for practical work and evidence. The [OEE specification](../../spec/README.md) governs newly authored or explicitly migrated course revisions.
