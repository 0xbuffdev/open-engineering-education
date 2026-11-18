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
- Evaluate finite sequential decision processes and reinforcement-learning policies with explicit feedback, uncertainty and safety limits.
- Build bounded retrieval and tool-using AI systems with explicit evaluation, permissions, and failure controls.
- Fine-tune and evaluate models while controlling for contamination, memorization, and misleading evaluation results.
- Deploy observable AI services and reason about latency, throughput, resource use, cost, rollback, and reliability.
- Identify AI risks, define measurable controls, and ship a production-grade AI system with documented limitations and safeguards.

## Program completion standard

**Graduation requires two separately reviewed decisions:** (1) genuine assessed completion of **every required AI1–AI15 predecessor** (or authorized outcome-equivalent decisions for the exact original revision and assessed outcomes), including the AI6 reinforcement-learning branch that is not inherited from AI15; and (2) satisfactory, independently reviewed completion of **all five AI16 summative assessments and all sixteen AI16 outcomes** through one coherent AI system and unfamiliar individual defense. Admission to AI16 verifies predecessor evidence *before* capstone work. An impressive AI16 project cannot waive an earlier course; earlier completion cannot replace new capstone mastery. The four planned AI17–AI20 electives are **not** graduation requirements. These are **integration-branch draft design rules**, not a declaration that the historic nine-course program on `main` has been replaced, learner records migrated, courses assessed with learners or graduation is currently enrollment-ready.

## Courses

**Integration-branch review only — not the currently published AI program.** AI1 has been migrated on main. This integration branch additionally stages **AI2 — Mathematics of Statistical and Neural Models**, **AI3 — Classical Artificial Intelligence, Search & Reasoning**, **AI4 — Machine Learning & Statistical Learning Theory**, **AI5 — Deep Learning & Representation Learning**, **AI6 — Sequential Decision Making & Reinforcement Learning**, **AI7 — Natural Language Processing & Information Retrieval**, **AI8 — Computer Vision & Multimodal Learning**, **AI9 — Transformers & Generative Modeling**, **AI10 — Model Training, Adaptation & Optimization**, **AI11 — Retrieval-Augmented AI Systems**, **AI12 — Agentic AI & Tool-Using Systems**, **AI13 — AI Evaluation, Testing & Reliability**, **AI14 — Responsible AI, Security & Governance**, **AI15 — Production AI Systems & MLOps**, and **AI16 — AI Engineering Capstone** and the optional **AI17 — Speech & Audio Intelligence**, **AI18 — Robotics & Embodied Intelligence**, and **AI19 — Causal Inference** electives under OEE v0.2.0. **AI20 remains planned but unauthored**, so the expanded sequence is incomplete. They must not be presented as an enrollment-ready prerequisite graph. The nine-course legacy catalog on main remains authoritative until an explicitly reviewed **atomic expanded-catalog cutover**. The migration does not award historic learner equivalence, establish educational readiness, or claim formal conformance. See the [curriculum inventory](../INVENTORY.md) for derived source-format observations.

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
| [AI11](AI11.md) | Retrieval-Augmented AI Systems (staged) | 16–22 weeks | AI9 | `course` |
| [AI12](AI12.md) | Agentic AI & Tool-Using Systems (staged) | 18–24 weeks | AI3 and AI9 | `course` |
| [AI13](AI13.md) | AI Evaluation, Testing & Reliability (staged) | 18–24 weeks | AI10, AI11 and AI12 | `course` |
| [AI14](AI14.md) | Responsible AI, Security & Governance (staged) | 18–26 weeks | AI13 | `course` |
| [AI15](AI15.md) | Production AI Systems & MLOps (staged) | 18–24 weeks | AI14 | `course` |
| [AI16](AI16.md) | AI Engineering Capstone (staged) | 12–18 weeks | AI6 and AI15; verify AI1–AI15 | `project` |
| [AI17](AI17.md) | Speech & Audio Intelligence (Elective · staged) | 18–26 weeks | AI9 | `course` |
| [AI18](AI18.md) | Robotics & Embodied Intelligence (Elective · staged) | 22–30 weeks | AI6 and AI8 | `course` |
| [AI19](AI19.md) | Causal Inference (Elective · staged) | 20–28 weeks | AI4 | `course` |

**Migration boundary:** AI2–AI15 above are *integration-branch replacements only*, and AI16 is a new integration-only capstone, and the historic nine-course catalog on main retains different course-code meanings. AI9 in particular is now transformers/generative modeling on this branch, whereas **historic AI9 on main is the capstone** (planned successor AI16). The partial expanded catalog lacks the planned AI20 elective course file. Do not use it as the published full AI graduation pathway. Each course definition is authoritative for its own revision, but a coherent, public program catalog requires the completed cutover. The old course identifiers must not be repurposed on main until downstream links and historical learner evidence have been reviewed. Use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or another learner-controlled environment for practical work and evidence. The [OEE specification](../../spec/README.md) governs newly authored or explicitly migrated course revisions.

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
| AI11 | Retrieval-Augmented AI Systems | Required · staged for review |
| AI12 | Agentic AI & Tool-Using Systems | Required · staged for review |
| AI13 | AI Evaluation, Testing & Reliability | Required · staged for review |
| AI14 | Responsible AI, Security & Governance | Required · staged for review |
| AI15 | Production AI Systems & MLOps | Required · staged for review |
| AI16 | AI Engineering Capstone | Required · staged for review |
| AI17 | Speech & Audio Intelligence | Optional · staged for review |
| AI18 | Robotics & Embodied Intelligence | Optional · staged for review |
| AI19 | Causal Inference | Optional · staged for review |
| AI20 | Graph Representation Learning | Optional · pending |

AI1 depends on completed SEF via SEF10; AI2 and AI3 each depend directly on AI1 and may be studied in parallel; AI4 requires completed AI2 but not AI3; AI5 requires completed AI4 but not AI3; AI6 requires both AI3 and AI5; AI7 requires AI5 but not AI3 or AI6; AI8 requires AI7 (with AI5 inherited transitively); and **AI9 requires AI8** for paired visual/language conditioning. AI10 requires AI9 for training/adaptation specialization. AI11 also requires AI9, independently of AI10, because AI9 supplies a bounded conditional generator and its transitive AI7 dependency supplies retrieval and relevance assessment; advanced model fine-tuning is not required for RAG. AI12 requires **AI3 and AI9** for independently assessed state-based planning and generative conditional action selection; **AI10 fine-tuning and AI11 retrieval-augmented answering are not required**, nor is AI6 reinforcement learning. Tool use, local trusted dispatch and action authorization are AI12's own new competencies. AI13 requires **AI10, AI11 and AI12** because its mandatory cross-system evaluation assesses adapted model behavior, RAG evidence chains and agent tool/effect reliability; each contributes independently assessed specialist evidence. AI6 reinforcement learning is not a hidden prerequisite for AI13. **AI14 requires AI13**, inheriting assessed AI10 model-training, AI11 RAG and AI12 tool-agent evaluation. It newly owns responsible-use impact and risk authority, fairness/privacy/security governance, meaningful oversight, legal/standards scoping and accountable risk controls; it does not duplicate AI13's general TEVV. No APP/SYS/SEC specialization is a hidden AI14 requirement. **AI15 directly requires AI14**, inheriting AI13 model/RAG/agent evaluation and AI14 risk governance; AI15 newly owns actual model serving, observed inference costs/SLIs, source-to-release provenance, progressive deployment, rollback, live data/feature quality and on-call recovery. These compulsory CPU-local competencies do **not** require a separate APP/SYS/SEC course or paid platform. No APP/SYS requirement is necessary for AI2–AI15. Later specialized AI courses will reference specific APP preparation only when their real assessment demands it, not an entire program by default. **AI17 is an optional elective with the single direct prerequisite AI9**: its transitive AI7/AI5 language and neural foundations plus AI9 conditional sequence modeling provide the assessed preparation for audio recognition and generation; no extra APP/SYS/SEC, AI6 RL, AI13 TEVV or AI15 production-platform prerequisite is invented. AI17 is **not required for AI16, AI core completion or any unrelated elective**. **AI18 directly requires AI6 and AI8** for sequential decision/control foundations and vision/physical perception; it introduces its own assessed robot kinematics, dynamics, sensor estimation, SLAM, geometric/kinodynamic planning, feedback, contact and safety. The elective does not require AI9/AI12/AI15, APP/SYS/SEC or physical robot equipment; AI18 is **not** core graduation or AI16 prerequisite. **AI19 directly requires AI4** for mathematical/statistical learning foundations and newly assesses intervention semantics, causal graphs, assignment designs, backdoor/frontdoor identification, standardization/IPW, doubly robust and longitudinal effects, quasi-experiments, transport, sensitivity and ethical interpretation. AI3 graph search, AI6 RL, AI13 general evaluation, AI20 future graph representation learning and APP/SYS/SEC are **not** hidden prerequisites; AI19 is optional and does not affect AI16/core completion. **AI16 has two direct prerequisites, AI6 and AI15**: AI15 transitively covers AI1–AI5 and AI7–AI15, but AI6 is a required separate branch; admission also checks actual completion decisions for **every** AI1–AI15 predecessor, and graduation separately checks the AI16 project. Historic AI9 capstone projects cannot automatically become new AI16 evidence, nor new AI9 transformer evidence. Electives are not hidden capstone prerequisites. Before promoting the complete integration branch to main, replace this temporary dual catalog with one coherent prerequisite-valid AI1–AI20 learner catalog, review downstream consumer identities and migration history, and perform a final program-wide academic and source validation. Historical AI9 capstone evidence must never silently convert into new AI9 transformer credit.
