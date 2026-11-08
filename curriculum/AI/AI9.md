## AI9 — AI Engineering Capstone

**Duration:** 8–10 weeks
**Expected workload:** 10–15 focused hours/week

### Overview
The capstone is the final project course in AI Engineering. You will combine data, model selection or training, evaluation, serving, monitoring, and responsible-AI practices into an AI system that can be meaningfully assessed in a realistic workflow.

### Prerequisites
**AI1–AI8 — AI Engineering**

**Kind:** `project`

### Learning outcomes
By the end of the project, you will be able to:

- Define an AI problem, evaluation target, data policy, and measurable success criteria.
- Build an AI system using an appropriate model and engineering architecture.
- Design an evaluation suite that reveals meaningful strengths and failures.
- Measure quality, latency, resource use, and cost where applicable.
- Deploy and observe an AI system with appropriate controls and rollback procedures.
- Identify and mitigate material safety, security, reliability, and misuse risks.
- Explain limitations and defend system design decisions using evidence.

### Resource map

**Required**

- Review the AI1–AI8 readings module by module.
- **B38** Ch. 3–4 and 9–10 · **B35** Ch. 2 and 6–10 · **R55** · **R60**.

### Modules

#### Module 1 — Problem Definition & Evaluation Design

**Reading:** **B38** Ch. 3 (Evaluation Methodology), Ch. 4 (Evaluate AI Systems). **B35** Ch. 2 (Introduction to Machine Learning Systems Design — objectives and requirements). **R55** Core function MAP.


### Module outcomes

By the end of this module, the learner can:

- Explain **Problem framing, data policy, baseline, metrics, and evaluation plan** in the context of the course.

1. **Problem framing, data policy, baseline, metrics, and evaluation plan**
   - kind: `lesson`
2. **Evaluation checkpoint**
   - kind: `test`

3. **Micro-lab: Write an evaluation specification and construct a small representative test set.**
   - kind: `lab`
#### Module 2 — Model & System Implementation

**Reading:** **B38** Ch. 5–6 and 10. **B35** Ch. 6–7.


### Module outcomes

By the end of this module, the learner can:

- Explain **Model selection, system architecture, data flow, and implementation** in the context of the course.

1. **Model selection, system architecture, data flow, and implementation**
   - kind: `lesson`
2. **System design checkpoint**
   - kind: `test`

3. **Micro-lab: Build one end-to-end inference path and log its key measurements.**
   - kind: `lab`
#### Module 3 — Evaluation, Failure Analysis & Safety

**Reading:** **B38** Ch. 4. **B35** Ch. 6. **R60** LLM01–LLM10 as the misuse-test checklist. **R55** Core function MEASURE.


### Module outcomes

By the end of this module, the learner can:

- Explain **Experimentation, error analysis, robustness, safety, and misuse testing** in the context of the course.
- Apply **Evaluation review** in a problem, implementation, experiment, or design decision.

1. **Experimentation, error analysis, robustness, safety, and misuse testing**
   - kind: `lesson`
2. **Evaluation review**
   - kind: `test`

3. **Micro-lab: Create a small adversarial or edge-case evaluation set and analyze failures.**
   - kind: `lab`
#### Module 4 — Serving & Operations

**Reading:** **B35** Ch. 7–10. **B38** Ch. 9–10. **B26** Ch. 8 (Release Engineering), Ch. 14–15 (incidents; postmortems).


### Module outcomes

By the end of this module, the learner can:

- Explain **Deployment, observability, latency, cost, incident handling, and rollback** in the context of the course.

1. **Deployment, observability, latency, cost, incident handling, and rollback**
   - kind: `lesson`
2. **Production readiness checkpoint**
   - kind: `test`

3. **Micro-lab: Introduce a deliberately bad release and demonstrate detection and rollback.**
   - kind: `lab`
#### Module 5 — Final Project Lab

**Reading:** Apply all earlier readings. **R56** for the model/system card. **B26** Ch. 3–4 for the defense.


1. **Build, evaluate, deploy, operate, document, and prepare the production AI system for defense**
   - kind: `lab`

### Suitable capstone shapes

- evaluated RAG platform
- production AI assistant
- domain-specific document intelligence system
- agentic developer tool
- model-serving platform
- AI workflow/orchestration system

### Required qualities

- problem definition
- dataset/data policy
- architecture diagram
- baseline
- evaluation suite
- failure analysis
- model/system card
- API/service
- tests
- observability
- deployment
- cost/performance measurements
- security controls
- incident and rollback procedure
- final retrospective

A capstone is not accepted because it “works.” The learner must demonstrate **how it was evaluated, where it fails, and how it is operated safely.**

This is the **Program 4 — AI graduation requirement**.