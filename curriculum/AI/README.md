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

**Integration-branch review only — not the currently published AI program.** AI1 has been migrated on main. This integration branch additionally stages the revised **AI2 — Mathematics of Statistical and Neural Models** under OEE v0.2.0. **AI3–AI9 here remain legacy drafts**, and their old course-code assumptions are not compatible with the proposed expanded sequence. They must not be presented as an enrollment-ready prerequisite graph. The nine-course legacy catalog on main remains authoritative until an explicitly reviewed **atomic expanded-catalog cutover**. The migration does not award historic learner equivalence, establish educational readiness, or claim formal conformance. See the [curriculum inventory](../INVENTORY.md) for derived source-format observations.

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [AI1](AI1.md) | Scientific Computing & Data Engineering for AI | 14–18 weeks | Completed SEF (SEF10) | `course` |
| [AI2](AI2.md) | Mathematics of Statistical and Neural Models (staged) | 16–20 weeks | AI1 | `course` |
| [AI3](AI3.md) | Deep Learning & Representation Learning | 6 weeks | AI2 | `course` |
| [AI4](AI4.md) | Transformers & Large Language Models | 7 weeks | AI3 | `course` |
| [AI5](AI5.md) | Retrieval, Agents & Applied Generative AI | 6 weeks | AI4 | `course` |
| [AI6](AI6.md) | Training, Fine-Tuning & Evaluation | 5 weeks | AI4 | `course` |
| [AI7](AI7.md) | Production AI Systems & MLOps | 6 weeks | AI5 and AI6 | `course` |
| [AI8](AI8.md) | Responsible AI, Safety & Governance | 3 weeks | AI5 | `course` |
| [AI9](AI9.md) | AI Engineering Capstone | 8–10 weeks | AI1–AI8 | `project` |

**Migration boundary:** the AI2 row above refers to the *proposed integration-branch replacement only*; the existing AI3–AI9 rows retain historical identities and may carry dependencies on the historic AI2 rather than the staged revision. Do not use this mixed intermediate catalog as a published degree pathway. Each course definition is authoritative for its own revision, but a coherent, public program catalog requires the completed cutover. The old course identifiers must not be repurposed on main until downstream links and historical learner evidence have been reviewed. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment for practical work and evidence. The [OEE specification](../../spec/README.md) governs newly authored or explicitly migrated course revisions.

## Expanded AI architecture under review (integration branch only)

The steward-approved working target is **sixteen required core courses (AI1–AI16, including the capstone) and four optional electives (AI17–AI20)**. This planning list does not claim the referenced successor course files already exist. Course boundaries, prerequisites and duration estimates require course-by-course academic review against SEF/APP/SYS.

| Proposed code | Proposed competency owner | Track |
| --- | --- | --- |
| AI1 | Scientific Computing & Data Engineering for AI | Required · migrated on main |
| AI2 | Mathematics of Statistical and Neural Models | Required · staged for review |
| AI3 | Classical Artificial Intelligence, Search & Reasoning | Required · pending |
| AI4 | Machine Learning & Statistical Learning Theory | Required · pending |
| AI5 | Deep Learning & Representation Learning | Required · pending |
| AI6 | Sequential Decision Making & Reinforcement Learning | Required · pending |
| AI7 | Natural Language Processing & Information Retrieval | Required · pending |
| AI8 | Computer Vision & Multimodal Learning | Required · pending |
| AI9 | Transformers & Generative Modeling | Required · pending |
| AI10 | Model Training, Adaptation & Optimization | Required · pending |
| AI11 | Retrieval-Augmented AI Systems | Required · pending |
| AI12 | Agentic AI & Tool-Using Systems | Required · pending |
| AI13 | AI Evaluation, Testing & Reliability | Required · pending |
| AI14 | Responsible AI, Security & Governance | Required · pending |
| AI15 | Production AI Systems & MLOps | Required · pending |
| AI16 | AI Engineering Capstone | Required · pending |
| AI17 | Speech & Audio Intelligence | Optional · pending |
| AI18 | Robotics & Embodied Intelligence | Optional · pending |
| AI19 | Causal Inference | Optional · pending |
| AI20 | Graph Representation Learning | Optional · pending |

AI1 depends on completed SEF via SEF10; AI2 depends on AI1. No APP/SYS dependency is necessary for AI2. Later specialized AI courses will reference specific APP preparation only when their real assessment demands it, not an entire program by default. Electives are not hidden capstone prerequisites. Before promoting the complete integration branch to main, replace this temporary dual catalog with one coherent prerequisite-valid AI1–AI20 learner catalog, review downstream consumer identities and migration history, and perform a final program-wide academic and source validation. Historical AI9 capstone evidence must never silently convert into new AI9 transformer credit.
