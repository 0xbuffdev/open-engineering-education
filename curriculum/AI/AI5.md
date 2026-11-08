## AI5 — Retrieval, Agents & Applied Generative AI

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** AI4

### Overview

Move from model understanding to AI application engineering through retrieval, tool use, agent loops, permissions, prompt/tool boundaries, evaluation, and failure analysis.

### Prerequisites

**AI4 — Transformers & Large Language Models**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Design a retrieval pipeline and evaluate retrieval quality.
- Build bounded tool-using or agentic workflows with explicit permissions.
- Separate durable knowledge, transient state, tool execution, and model generation concerns.
- Test retrieval failures, tool failures, and prompt-injection risks in a controlled environment.
- Evaluate an AI workflow using reproducible cases rather than anecdotal prompts.


### Resource map

**Required**

- **B38** Ch. 5 (Prompt Engineering) and Ch. 6 (RAG and Agents), with Ch. 2 (Sampling — structured outputs), Ch. 4 (Evaluate AI Systems) and Ch. 10 (architecture, guardrails, feedback).
- **B39** Ch. 1, 6 and 8 (Boolean retrieval; scoring, term weighting and the vector space model; evaluation in information retrieval).
- **R57** Building effective agents · **R58** the RAG paper · **R60** LLM01, LLM05, LLM06, LLM08.

### Modules

#### Module 1 — Retrieval Foundations

**Reading:** **B38** Ch. 6 §6.1 (RAG — architecture; retrieval algorithms; retrieval optimization: chunking, reranking, query rewriting). **B39** Ch. 1 (Boolean retrieval), Ch. 6 (Scoring, term weighting and the vector space model), Ch. 8 (Evaluation in information retrieval).


### Module outcomes

By the end of this module, the learner can:

- Explain **Embeddings and retrieval** in the context of the course.
- Apply **Chunking, ranking, and retrieval quality** in a problem, implementation, experiment, or design decision.

1. **Embeddings and retrieval**
   - kind: `lesson`
2. **Chunking, ranking, and retrieval quality**
   - kind: `lesson`
3. **Checkpoint: retrieval design**
   - kind: `test`

4. **Micro-lab: Compare two chunking strategies on a small corpus.**
   - kind: `lab`
#### Module 2 — RAG Pipelines

**Reading:** **B38** Ch. 6 §6.1 (RAG architecture; retrieval algorithms; RAG beyond text), Ch. 5 (Prompt Engineering — context and grounding). **R58** the RAG paper. **R60** LLM08 (Vector and Embedding Weaknesses).


### Module outcomes

By the end of this module, the learner can:

- Explain **Retrieval-augmented generation** in the context of the course.
- Apply **Grounding and citations** in a problem, implementation, experiment, or design decision.

1. **Retrieval-augmented generation**
   - kind: `lesson`
2. **Grounding and citations**
   - kind: `lesson`
3. **Checkpoint: grounded generation**
   - kind: `test`

4. **Micro-lab: Build a retrieval step that returns evidence with each generated answer.**
   - kind: `lab`
#### Module 3 — Tool Use & Structured Outputs

**Reading:** **B38** Ch. 6 (Agents: tools and planning), Ch. 2 (Sampling — structured outputs). **R57** Building effective agents. **R60** LLM05 (Improper Output Handling), LLM06 (Excessive Agency).


### Module outcomes

By the end of this module, the learner can:

- Explain **Tool calling and structured outputs** in the context of the course.
- Apply **Permissions and bounded action spaces** in a problem, implementation, experiment, or design decision.

1. **Tool calling and structured outputs**
   - kind: `lesson`
2. **Permissions and bounded action spaces**
   - kind: `lesson`
3. **Checkpoint: tool boundary design**
   - kind: `test`

4. **Micro-lab: Allowlist one tool and reject an unapproved call.**
   - kind: `lab`
#### Module 4 — Agents, Memory & Injection

**Reading:** **B38** Ch. 6 (agent failure modes and evaluation; memory), Ch. 5 (defensive prompt engineering — prompt attacks). **R60** LLM01 (Prompt Injection). **R59** indirect prompt injection.


### Module outcomes

By the end of this module, the learner can:

- Explain **Agent loops, state, and memory** in the context of the course.
- Apply **Prompt injection and failure evaluation** in a problem, implementation, experiment, or design decision.

1. **Agent loops, state, and memory**
   - kind: `lesson`
2. **Prompt injection and failure evaluation**
   - kind: `lesson`
3. **Checkpoint: agent failure modes**
   - kind: `test`

4. **Micro-lab: Construct a benign injection test and verify the control blocks the unsafe path.**
   - kind: `lab`
#### Module 5 — Bounded RAG/Tool-Using Agent

**Reading:** **B38** Ch. 6; Ch. 4 (Evaluate AI Systems — evaluation pipelines); Ch. 10 (guardrails; logging and monitoring; user feedback).


1. **Build, evaluate, red-team, and document the Bounded RAG/Tool-Using Agent**
   - kind: `lab`

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

---

