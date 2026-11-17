# Program 4 — AI: AI Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [SYS](../SYS/README.md) · Next: [SEC](../SEC/README.md)

## Overview

AI Engineering turns the assessed programming and numerical mathematics from the foundations program into practical, evidence-driven artificial intelligence. You work through data, classical machine learning, deep learning, transformers and language models, retrieval and agents, training and evaluation, and production AI systems. The program stresses reproducible experiments and measurable evaluation, so you learn to operate models, measure their behavior, and document their limits.

## Prerequisites

**Assessed completion of Program 1 — SEF — Software Engineering Foundations**, including [SEF10](../SEF/SEF10.md). Python and the mathematics covered in SEF2 and SEF8 are assumed, not repeated. Individual AI courses have their own explicit prerequisites; downstream specialist courses must be reviewed against relevant APP and SYS competencies rather than silently making an elective or entire separate program mandatory.

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

**AI1 has been substantively migrated to the outcome-driven OEE `v0.2.0` draft format**, with its own assessed scientific-data competence, source/evaluation integrity checks and clean-reproduction requirements. **AI2–AI9 remain legacy draft outlines** until their academic boundaries, stable course identities and replacement assessments have been separately reviewed and migrated. The migration does not claim learner-tested readiness, independent academic verification or automatic equivalence with historical learner records. See the [curriculum inventory](../INVENTORY.md) for a derived structural audit.

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [AI1](AI1.md) | Scientific Computing & Data Engineering for AI | 14–18 weeks | Completed SEF (SEF10) | `course` |
| [AI2](AI2.md) | Machine Learning Foundations | 6 weeks | AI1 | `course` |
| [AI3](AI3.md) | Deep Learning & Representation Learning | 6 weeks | AI2 | `course` |
| [AI4](AI4.md) | Transformers & Large Language Models | 7 weeks | AI3 | `course` |
| [AI5](AI5.md) | Retrieval, Agents & Applied Generative AI | 6 weeks | AI4 | `course` |
| [AI6](AI6.md) | Training, Fine-Tuning & Evaluation | 5 weeks | AI4 | `course` |
| [AI7](AI7.md) | Production AI Systems & MLOps | 6 weeks | AI5 and AI6 | `course` |
| [AI8](AI8.md) | Responsible AI, Safety & Governance | 3 weeks | AI5 | `course` |
| [AI9](AI9.md) | AI Engineering Capstone | 8–10 weeks | AI1–AI8 | `project` |

The individual course files remain the authoritative source for each course's published work, identity and prerequisites. The existing AI2–AI9 identifiers must not be repurposed silently for a proposed expanded architecture: any replacement requires explicit catalog, downstream-link and historical evidence review. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment for practical work and evidence. The [OEE specification](../../spec/README.md) governs newly authored or explicitly migrated course revisions.
