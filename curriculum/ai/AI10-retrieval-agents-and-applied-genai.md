# AI10 — Retrieval, Agents & Applied GenAI

**Track:** AI & ML · **Prerequisite:** AI6 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P9 doc-compass

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Build an applied generative-AI system over a bounded corpus with citations, explicit authority limits, and evaluation. You will treat retrieval and tool use as engineering components with failure modes, not as prompt tricks.

## Outcomes

You can:

- design chunking, indexing, and retrieval for a documented corpus;
- build a retrieval-only baseline and a labelled evaluation set;
- evaluate retrieval (recall@k, MRR, nDCG) and answer quality separately;
- design an orchestration loop with bounded tools and stop conditions;
- defend against prompt injection, data exfiltration, and tool abuse within scope;
- stream answers with citations and abstention;
- measure latency, cost, and failure rates;
- write a system card with intended use, non-use, and residual risk;
- state why a fluent answer is not evidence.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [RAG paper](https://arxiv.org/abs/2005.11401) | Full | Retrieval-augmented generation |
| [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) | Units 1–3 | Tools, agents, evaluation |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) | Full, current edition | Threat taxonomy |
| [NIST AI RMF Generative AI Profile](https://www.nist.gov/itl/ai-risk-management-framework) | Selected | Risk management |
| [ReAct paper](https://arxiv.org/abs/2210.03629) | Full | Reasoning plus acting |
| [Lost in the Middle](https://arxiv.org/abs/2307.03172) | Full | Long-context retrieval behaviour |
| Framework docs (one of LangChain, LlamaIndex, Haystack) | Retrieval, tools, tracing | Implementation; pin one version |
| [Model Context Protocol](https://modelcontextprotocol.io/) | Overview and security | Tool boundary design |

## Modules

### 1. Corpus and retrieval

- corpus licensing and privacy;
- document parsing and structure;
- chunking: fixed, semantic, hierarchical;
- metadata and filters;
- embeddings and vector search;
- hybrid search (BM25 + dense);
- reranking;
- index freshness and deletion;
- retrieval evaluation.

### 2. Answer generation

- context construction and token budget;
- citation and provenance;
- abstention when evidence is missing;
- groundedness and attribution;
- long-context limits;
- prompt templates and versioning;
- structured output;
- hallucination detection.

### 3. Agents and tools

- tool schema and validation;
- allowlisted, read-only tools by default;
- planning versus reactive loops;
- max steps, timeouts, and budgets;
- human approval for consequential actions;
- idempotency and retries;
- tool-result injection;
- sandboxing and network egress;
- stop conditions.

### 4. Security and privacy

- prompt injection (direct and indirect);
- data exfiltration through citations/tools;
- retrieval poisoning;
- cross-tenant leakage;
- secrets in prompts/logs;
- output handling and rendering;
- denial of service and context flooding;
- authorization at the tool/data layer, not the prompt.

### 5. Evaluation

- retrieval metrics;
- answer correctness and faithfulness;
- citation accuracy;
- refusal/abstention quality;
- task success;
- latency and cost;
- adversarial/benign failure suite;
- human rubric and inter-rater agreement;
- regression tests for every repaired failure.

### 6. Operations

- tracing and request IDs;
- prompt/model/index versioning;
- caching;
- rate limits;
- feedback capture with privacy;
- incident and rollback;
- system card.

## Labs

### Lab 1 — Corpus and retrieval baseline

Use a small licensed, non-sensitive corpus (your own docs are ideal). Build chunking, an index, and a retrieval-only baseline. Create 30–50 labelled queries with relevant passages. Report recall@k and one retrieval failure.

### Lab 2 — Grounded answer with citations

Add generation with citations and abstention. Evaluate faithfulness and citation correctness on the labelled set. Show one fluent but unsupported answer and the control that catches it.

### Lab 3 — Bounded agent

Add two read-only tools with JSON schemas, max steps, timeout, and an explicit authority boundary. Test malformed tool arguments, denied tools, and a tool that returns malicious text. Log decisions without leaking private data.

### Lab 4 — Failure and injection suite

Create a benign local test suite for:

- irrelevant retrieval;
- stale document;
- prompt injection in a document;
- citation mismatch;
- tool denial;
- context overflow;
- rate limit.

For each repaired issue, add a regression test.

### Lab 5 — Evaluation and system card

Compare retrieval-only, RAG, and RAG+tools (if applicable) on quality, latency, and cost. Write a system card with intended users, non-users, data boundaries, evaluation limits, and residual risks.

## Exercises

1. Compare two chunking strategies with retrieval metrics.
2. Explain recall@k versus answer accuracy.
3. Design a citation format that supports verification.
4. Write an abstention policy.
5. Enumerate agent authority boundaries.
6. Turn a prompt-injection scenario into a harmless test.
7. Explain why prompt-level authorization is insufficient.
8. Design a tool schema that rejects malformed input.
9. Define a human-approval condition.
10. State what an offline RAG evaluation cannot prove.

## Project increment — P9 doc-compass

Build:

- documented corpus and data card;
- retrieval baseline and evaluation set;
- grounded generation with citations/abstention;
- allowlisted read-only tools with limits;
- injection/failure test suite;
- tracing, cost, and latency measurement;
- system card and incident/rollback plan.

**Brief:** [P9 — doc-compass](../projects/project-ladder.md#p9--doc-compass)

## Exit check

- [ ] show retrieval metrics on a labelled set;
- [ ] demonstrate citation correctness and one abstention case;
- [ ] trace a request through retrieval and generation;
- [ ] defend against one prompt-injection and one tool-abuse case;
- [ ] show bounded steps/timeouts/authority;
- [ ] report quality, latency, and cost together;
- [ ] state intended use, non-use, and residual risk.

## Common failure modes

- Evaluating only the final answer and not retrieval.
- Treating all retrieved text as trusted instructions.
- Granting shell, network, or write access by default.
- Citing a document without checking the cited passage.
- Letting an agent loop without a step/time budget.
- Logging private prompts or retrieved data.
- Calling a demo "safe" because a single injection failed.
- Using an LLM judge without calibration.

## Evidence to commit

- `labs/ai/AI10/` with retrieval baseline, labelled eval, agent, injection suite, report
- P9 repository, system card, evaluation set, incident plan
- `notes/ai/AI10/summary.md`
- `notes/ai/AI10/resources.md` with corpus license and framework version

## Optional depth

- *Designing Machine Learning Systems* Ch. 8–9 (drift, continual learning).
- *Building LLM Powered Applications* or equivalent applied text.
- RAGAS and TruLens evaluation docs.
- OWASP Agentic AI guidance and MITRE ATLAS.
- Vector database internals (HNSW, IVF) via S12.
