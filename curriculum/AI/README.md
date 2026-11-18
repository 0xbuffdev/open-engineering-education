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

**Integration-branch review only — not the currently published AI program.** AI1 has been migrated on main. This integration branch additionally stages **AI2 — Mathematics of Statistical and Neural Models**, **AI3 — Classical Artificial Intelligence, Search & Reasoning**, **AI4 — Machine Learning & Statistical Learning Theory**, **AI5 — Deep Learning & Representation Learning**, **AI6 — Sequential Decision Making & Reinforcement Learning**, **AI7 — Natural Language Processing & Information Retrieval**, **AI8 — Computer Vision & Multimodal Learning**, **AI9 — Transformers & Generative Modeling**, and **AI10 — Model Training, Adaptation & Optimization** under OEE v0.2.0. **AI11–AI20 remain planned but unmigrated**, so the expanded sequence is incomplete. They must not be presented as an enrollment-ready prerequisite graph. The nine-course legacy catalog on main remains authoritative until an explicitly reviewed **atomic expanded-catalog cutover**. The migration does not award historic learner equivalence, establish educational readiness, or claim formal conformance. See the [curriculum inventory](../INVENTORY.md) for derived source-format observations.

| Course | Title | Duration | Prerequisites | Type |
| --- | --- | --- | --- | --- |
| [AI1](AI1.md) | Scientific Computing & Data Engineering for AI | 14–18 weeks | Completed SEF (SEF10) | `course` |
| [AI2](AI2.md) | Mathematics of Statistical and Neural Models (staged) | 16–20 weeks | AI1 | `course` |
| [AI3](AI3.md) | Classical Artificial Intelligence, Search & Reasoning (staged) | 18–24 weeks | AI1 | `course` |
| [AI4](AI4.md) | Machine Learning & Statistical Learning Theory (staged) | 20–26 weeks | AI2 | `course` |
| [AI5](AI5.md) | Deep Learning & Representation Learning (staged) | 20–26 weeks | AI4 | `course` |
| [AI6](AI6.md) | Sequential Decision Making & Reinforcement Learning (staged) | 20–28 weeks | AI3 and AI5 | `course` |
| [AI7](AI7.md) | Natural Language Processing & Information Retrieval (staged) | 18–24 weeks | AI5 | `course` |
| [AI8](AI8.md) | Computer Vision & Multimodal Learning (staged) | 20–28 weeks | AI7 | `course` |
| [AI9](AI9.md) | Transformers & Generative Modeling (staged) | 20–26 weeks | AI8 | `course` |
| [AI10](AI10.md) | Model Training, Adaptation & Optimization (staged) | 16–22 weeks | AI9 | `course` |

**Migration boundary:** AI2–AI10 above are *integration-branch replacements only*, and the historic nine-course catalog on main retains different course-code meanings. AI9 in particular is now transformers/generative modeling on this branch, whereas **historic AI9 on main is the capstone** (planned successor AI16). The partial expanded catalog lacks the planned AI11–AI20 courses. Do not use it as the published full AI graduation pathway. Each course definition is authoritative for its own revision, but a coherent, public program catalog requires the completed cutover. The old course identifiers must not be repurposed on main until downstream links and historical learner evidence have been reviewed. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment for practical work and evidence. The [OEE specification](../../spec/README.md) governs newly authored or explicitly migrated course revisions.

## Expanded AI architecture under review (integration branch only)

The steward-approved working target is **sixteen required core courses (AI1–AI16, including the capstone) and four optional electives (AI17–AI20)**. This planning list does not claim the referenced successor course files already exist. Course boundaries, prerequisites and duration estimates require course-by-course academic review against SEF/APP/SYS.

| Proposed code | Proposed competency owner | Track |
| --- | --- | --- |
| AI1 | Scientific Computing & Data Engineering for AI | Required · migrated on main |
| AI2 | Mathematics of Statistical and Neural Models | Required · staged for review |
| AI3 | Classical Artificial Intelligence, Search & Reasoning | Required · staged for review |
| AI4 | Machine Learning & Statistical Learning Theory | Required · staged for review |
| AI5 | Deep Learning & Representation Learning | Required · staged for review |
| AI6 | Sequential Decision Making & Reinforcement Learning | Required · staged for review |
| AI7 | Natural Language Processing & Information Retrieval | Required · staged for review |
| AI8 | Computer Vision & Multimodal Learning | Required · staged for review |
| AI9 | Transformers & Generative Modeling | Required · staged for review |
| AI10 | Model Training, Adaptation & Optimization | Required · staged for review |
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

AI1 depends on completed SEF via SEF10; AI2 and AI3 each depend directly on AI1 and may be studied in parallel; AI4 requires completed AI2 but not AI3; AI5 requires completed AI4 but not AI3; AI6 requires both AI3 and AI5; AI7 requires AI5 but not AI3 or AI6; AI8 requires AI7 (with AI5 inherited transitively); and **AI9 requires AI8** for paired visual/language conditioning. AI10 requires AI9 and inherits its assessed transformer, generative, deep-learning and language/vision foundations; AI6 reinforcement learning is not a hidden prerequisite for AI9 or AI10. No APP/SYS requirement is necessary for AI2–AI10. Later specialized AI courses will reference specific APP preparation only when their real assessment demands it, not an entire program by default. Electives are not hidden capstone prerequisites. Before promoting the complete integration branch to main, replace this temporary dual catalog with one coherent prerequisite-valid AI1–AI20 learner catalog, review downstream consumer identities and migration history, and perform a final program-wide academic and source validation. Historical AI9 capstone evidence must never silently convert into new AI9 transformer credit.
