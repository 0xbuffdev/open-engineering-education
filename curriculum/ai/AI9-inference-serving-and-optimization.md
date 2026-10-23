# AI9 — Inference, Serving & Optimization

**Track:** AI & ML · **Prerequisite:** AI6; S9 recommended · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P9 serving benchmark

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Serve a model as a bounded, observable system. You will learn the inference path, KV-cache management, batching, quantization, queueing, and tail latency, then build a service that degrades predictably under overload.

## Outcomes

You can:

- explain prefill versus decode and the KV-cache lifecycle;
- calculate weights, KV-cache, and activation memory;
- design request/response and streaming APIs;
- implement admission control, timeouts, cancellation, and bounded queues;
- compare static and continuous batching;
- explain quantization, speculative decoding, and paged attention;
- measure throughput, latency percentiles, errors, and cost correctly;
- diagnose a tail-latency cause from metrics and traces;
- define an SLO and a rollout/rollback threshold.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [vLLM docs](https://docs.vllm.ai/) | Architecture, scheduler, PagedAttention, metrics | Production inference |
| [PagedAttention paper](https://arxiv.org/abs/2309.06180) | Full | KV-cache management |
| [FlashAttention paper](https://arxiv.org/abs/2205.14135) | Full | Attention memory behaviour |
| [Efficient Inference for LLMs](https://arxiv.org/abs/2211.05102) or survey | Selected | Batching, quantization, trade-offs |
| [Triton Inference Server docs](https://docs.nvidia.com/deeplearning/triton-inference-server/) | Architecture, batching, metrics | Serving alternative |
| [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/) | HTTP/GenAI conventions where stable | Observability |
| S13 | GPU architecture, serving, queueing | Systems foundation |

## Modules

### 1. Inference mechanics

- tokenization and prompt formatting;
- prefill and decode phases;
- KV cache and context length;
- batch composition;
- sampling;
- stop conditions;
- streaming;
- model loading and cold start;
- precision and quantization.

### 2. Serving architecture

- API gateway and auth;
- request validation and limits;
- queues and admission control;
- worker pool and model replicas;
- routing and model multiplexing;
- timeouts, cancellation, and retries;
- streaming backpressure;
- caching;
- fallback and degradation;
- multi-tenant isolation.

### 3. Performance and cost

- throughput: requests/s and tokens/s;
- latency: TTFT, inter-token latency, end-to-end p50/p95/p99;
- queueing and Little's law;
- batching trade-offs;
- GPU memory and utilization;
- cost per request/token;
- capacity planning;
- SLO and error budget (S15).

### 4. Optimization

- continuous batching;
- paged attention;
- KV-cache eviction/offload;
- speculative decoding;
- quantization (FP16/BF16/INT8/INT4);
- operator fusion and kernels (awareness);
- tensor parallelism;
- prefix caching;
- structured output and constrained decoding.

### 5. Evaluation and rollout

- quality under quantization;
- regression suites;
- load test design;
- open-loop versus closed-loop generators;
- warm-up and cache state;
- canary and rollback;
- incident handling;
- privacy of prompts/responses.

## Labs

### Lab 1 — Memory and capacity calculator

Calculate weights, KV cache, activations, and maximum concurrent requests for several model sizes, context lengths, dtypes, and GPU memory budgets. Validate one number against vLLM or a real model.

### Lab 2 — Toy inference service

Serve a small local model or deterministic simulator behind an HTTP API with streaming, request limits, timeouts, cancellation, structured logs, and metrics. Add an allowlisted health endpoint.

### Lab 3 — Load test

Use an open-loop generator with a fixed request distribution. Measure TTFT, inter-token latency, end-to-end p50/p95/p99, throughput, errors, queue depth, and GPU/CPU memory. Find the knee and report the test environment.

### Lab 4 — Batching/quantization experiment

Change one factor: batching policy, KV-cache size, context length, concurrency, or quantization. Measure quality and operational impact. State the trade-off and one case where the optimization is not worth it.

### Lab 5 — Overload and rollback

Send more load than the service can handle. Verify admission control, bounded memory, useful errors, and recovery. Deploy a known-bad configuration, detect it with the SLO/alert, and roll back.

## Exercises

1. Calculate KV-cache size for a 7B model at 8k context and batch 16.
2. Explain prefill versus decode and why they have different bottlenecks.
3. Compare TTFT and inter-token latency.
4. Explain continuous batching with a timeline.
5. Explain PagedAttention's memory benefit.
6. Compare top-k and top-p under load.
7. Design a streaming cancellation path.
8. Explain one source of p99 latency.
9. Define a quality regression test for quantization.
10. Write a rollback threshold for a model upgrade.

## Project increment — P9 serving benchmark

Add to P9 `doc-compass`:

- a serving API with streaming and limits;
- observability for TTFT, inter-token latency, errors, queue depth, and tokens/s;
- a reproducible load test;
- one optimization experiment with quality impact;
- SLO, alert, and rollback evidence;
- a cost and capacity section.

**Brief:** [P9 — doc-compass](../projects/project-ladder.md#p9--doc-compass)

## Exit check

- [ ] explain the full request path from HTTP to tokens;
- [ ] calculate weights and KV-cache memory;
- [ ] show a load test with p50/p95/p99 and a stated workload;
- [ ] demonstrate bounded behavior under overload;
- [ ] quantify one optimization's quality and operational trade-off;
- [ ] detect and roll back a bad configuration;
- [ ] state what the benchmark does not prove.

## Common failure modes

- Measuring tokens/s without latency or quality.
- Using a closed-loop generator and hiding queueing.
- Ignoring warm-up and cache state.
- Unbounded queues and request buffers.
- Comparing configurations at different loads.
- Reporting GPU utilization as efficiency.
- Logging private prompts without consent.
- Calling a quantized model equivalent without evaluation.

## Evidence to commit

- `labs/ai/AI9/` with calculator, service, load test, optimization study, rollback log
- P9 serving code, benchmark report, SLO/runbook
- `notes/ai/AI9/summary.md`
- `notes/ai/AI9/resources.md` with model, hardware, versions, and cost

## Optional depth

- *Programming Massively Parallel Processors* (Kirk & Hwu).
- vLLM source: scheduler and block manager.
- TensorRT-LLM and Triton backend docs.
- *Systems Performance* (Gregg), queueing and latency chapters.
- Speculative decoding and Medusa papers.
