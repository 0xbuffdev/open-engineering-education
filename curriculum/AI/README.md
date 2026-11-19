# Program 4 — AI: AI Engineering

> [OEE curriculum](../README.md) · [Specification](../../spec/README.md) · Previous: [SYS](../SYS/README.md) · Next: [SEC](../SEC/README.md)

## Overview

AI Engineering develops the ability to design, build, evaluate and operate AI systems whose behavior can be independently examined. The program builds on Software Engineering Foundations and progresses through scientific computing, mathematical modeling, classical AI, machine learning, neural systems, language and vision, generative models, retrieval, agents, evaluation, governance and production operations. Learners use reproducible experiments to test what a model can do, where it fails and whether a particular use is justified.

## Entry requirements

Complete [SEF10](../SEF/SEF10.md), which requires assessed mastery of Software Engineering Foundations, before beginning AI1. Python, software testing, discrete mathematics, numerical computing and probability are assumed from SEF. Each subsequent course lists its direct prerequisites below. No APP, SYS or SEC course is a general entry requirement for AI.

## Program outcomes

After successfully completing the required courses and capstone, a learner can:

- Prepare lawful, reproducible datasets, investigate numerical error and define meaningful scientific evidence.
- Derive and implement mathematical models, search and reasoning methods, and finite sequential decision processes.
- Fit, test and compare classical and neural learning methods under valid sampling and measurement conditions.
- Explain and implement language, retrieval, vision, multimodal and generative-model mechanisms.
- Train or adapt bounded models while evaluating contamination, optimization constraints and uncertainty.
- Build retrieval-augmented and tool-using systems with real source permissions, observable effects and safe failure behavior.
- Evaluate model and composed-system quality, reliability, privacy, security and responsible-use limitations.
- Operate an actual locally reachable model-dependent service with measurable performance, release checks and verified recovery.
- Deliver and independently defend a coherent AI system, including an unfamiliar change, with separate evidence of prerequisite mastery.

## Courses

AI1–AI16 are required. AI16 is the cumulative capstone. AI17–AI20 are optional specializations and are not needed for core graduation.

| Course | Title | Duration | Direct prerequisites | Track |
| --- | --- | --- | --- | --- |
| [AI1](AI1.md) | Scientific Computing & Data Engineering for AI | 14–18 weeks | SEF10 | Required course |
| [AI2](AI2.md) | Mathematics of Statistical and Neural Models | 16–20 weeks | AI1 | Required course |
| [AI3](AI3.md) | Classical Artificial Intelligence, Search & Reasoning | 18–24 weeks | AI1 | Required course |
| [AI4](AI4.md) | Machine Learning & Statistical Learning Theory | 20–26 weeks | AI2 | Required course |
| [AI5](AI5.md) | Deep Learning & Representation Learning | 20–26 weeks | AI4 | Required course |
| [AI6](AI6.md) | Sequential Decision Making & Reinforcement Learning | 20–28 weeks | AI3, AI5 | Required course |
| [AI7](AI7.md) | Natural Language Processing & Information Retrieval | 18–24 weeks | AI5 | Required course |
| [AI8](AI8.md) | Computer Vision & Multimodal Learning | 20–28 weeks | AI7 | Required course |
| [AI9](AI9.md) | Transformers & Generative Modeling | 20–26 weeks | AI8 | Required course |
| [AI10](AI10.md) | Model Training, Adaptation & Optimization | 16–22 weeks | AI9 | Required course |
| [AI11](AI11.md) | Retrieval-Augmented AI Systems | 16–22 weeks | AI9 | Required course |
| [AI12](AI12.md) | Agentic AI & Tool-Using Systems | 18–24 weeks | AI3, AI9 | Required course |
| [AI13](AI13.md) | AI Evaluation, Testing & Reliability | 18–24 weeks | AI10, AI11, AI12 | Required course |
| [AI14](AI14.md) | Responsible AI, Security & Governance | 18–26 weeks | AI13 | Required course |
| [AI15](AI15.md) | Production AI Systems & MLOps | 18–24 weeks | AI14 | Required course |
| [AI16](AI16.md) | AI Engineering Capstone | 12–18 weeks | AI6, AI15; verify AI1–AI15 | Required project |
| [AI17](AI17.md) | Speech & Audio Intelligence | 18–26 weeks | AI9 | Elective |
| [AI18](AI18.md) | Robotics & Embodied Intelligence | 22–30 weeks | AI6, AI8 | Elective |
| [AI19](AI19.md) | Causal Inference | 20–28 weeks | AI4 | Elective |
| [AI20](AI20.md) | Graph Representation Learning | 19–27 weeks | AI5 | Elective |

Durations are planning estimates. Course completion depends on demonstrated outcomes and independent assessment, not elapsed weeks.

## Learning sequence

AI2 and AI3 both follow AI1 and may be studied in parallel. AI2 prepares learners for statistical and neural mathematics in AI4 and AI5; AI3 develops a separate foundation in search, constraints, logic and planning. Those branches meet in AI6, where sequential decisions and reinforcement learning require both reasoning and learned-model preparation.

AI7 builds on AI5 to study language and information retrieval. AI8 applies language and neural foundations to vision and multimodal systems, followed by AI9's transformer and generative modeling. AI10 specializes in model training and adaptation; AI11 develops evidence-grounded retrieval systems. AI12 combines AI3 planning with AI9 generative modeling to implement bounded, authorized tool use. Each has a separate assessed purpose.

AI13 evaluates adapted models, retrieval and tool-using systems, so it requires AI10, AI11 and AI12. AI14 adds risk, privacy, security and accountable governance. AI15 then develops serving, observability, release and recovery of a running AI service. AI15 does not inherit AI6 through its prerequisites, which is why the capstone requires AI6 separately.

The optional courses extend relevant prior skills. AI17 studies speech and audio after AI9. AI18 studies embodied robotics after AI6 and AI8. AI19 adds causal inference after AI4. AI20 develops graph representation learning after AI5. Completing an elective provides evidence of that specialization but does not replace any required course.

## Graduation requirements

Graduation has two distinct, independently reviewed decisions.

1. **Prerequisite mastery:** Confirm assessed completion of every course AI1–AI15 against its required outcomes and course revision, or a separately authorized, independently assessed outcome-equivalent decision. Check the AI6 branch explicitly before admission to AI16. Enrollment or a capstone artifact cannot substitute for unassessed prerequisite competence.
2. **Capstone mastery:** Complete all five [AI16](AI16.md) summative assessments and demonstrate all sixteen AI16 outcomes through one genuine, model-dependent system. The work includes independent evaluation, a locally accessible working service, observed recovery, an unfamiliar reviewer-selected change and an individually attributable technical defense.

Prior course completion does not establish capstone mastery, and a strong capstone result does not erase missing prerequisite evidence. AI17–AI20 remain optional.

## Study, assessment and readiness

Course files contain the authoritative outcomes, lessons, public reference cases and summative evidence requirements. Required work uses bounded, reproducible CPU-local experiments with synthetic or appropriately licensed source material. Some methods involve domain-specific numerical reasoning or small model training; no paid learning platform, GPU, proprietary inference provider or unrelated engineering program is universally required.

Learners may use [OEE Workspace](https://github.com/0xbuffdev/oee-workspace) or their own environment for implementations, records and technical defense. The [OEE specification](../../spec/README.md) defines the educational and evidence requirements, while the [curriculum inventory](../INVENTORY.md) reports structural checks for this repository revision.

**All twenty AI courses have educational status `draft`.** Source checks and academic review do not establish learner-tested effectiveness, professional certification, accreditation or independent OEE conformance. Promotion to `tested` or `verified` requires the evidence described in [Status Labels](../../spec/status-labels.md).
