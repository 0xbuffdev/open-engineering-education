# S13 — AI Infrastructure (Systems Lens)

**Track:** Systems · **Prerequisite:** S8, S9, S11 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P9 serving/gateway

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

AI infrastructure is systems engineering with accelerators: memory hierarchies, batching, scheduling, queues, tail latency, and cost. You will learn where the time and memory actually go in inference, and how to build an observable gateway even if you do not own a GPU.

## Outcomes

You can:

- explain GPU architecture, SIMT execution, warps, occupancy, and memory hierarchy;
- explain the roofline for matrix multiply and attention;
- calculate model memory (weights, activations, KV cache, optimizer state);
- explain batching, continuous batching, paged attention, and KV-cache trade-offs;
- explain quantization, speculative decoding, and parallelism at a high level;
- build an inference gateway/simulator with queueing, limits, metrics, and backpressure;
- measure throughput, p50/p95/p99 latency, memory, and cost;
- state when a GPU is required and when a simulator is an honest fallback.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| B3 | §§**7.8.6–7.8.7**, §§**8.2–8.3** | SIMD, multithreading, memory-system performance, caches |
| B6 | Ch. **2–3, 5–7**, §**8.4** | DRAM, caches, NUMA, optimization, tools, vector operations |
| [CUDA C Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) | Programming model, memory, performance | GPU mental model |
| [vLLM docs](https://docs.vllm.ai/) | Architecture, scheduling, PagedAttention | Real inference server |
| [NVIDIA/AMD profiling docs](https://docs.nvidia.com/nsight-compute/) | Selected sections | Measurement |
| [FlashAttention paper](https://arxiv.org/abs/2205.14135) | Full | Attention memory behaviour |

## Modules

### 1. Accelerator architecture

- CPU vs GPU: latency vs throughput;
- SIMT, warps/wavefronts, lanes;
- registers, shared memory, L1/L2, HBM;
- occupancy and latency hiding;
- coalesced access;
- tiling and shared-memory reuse;
- tensor cores and mixed precision;
- roofline for GEMM and attention.

### 2. Model memory

- parameters and dtype;
- activations;
- KV cache growth with context length and batch;
- optimizer state (training);
- quantization (FP16/BF16/INT8/INT4);
- memory fragmentation;
- offload and paging.

### 3. Inference serving

- prefill vs decode;
- static vs continuous batching;
- scheduling and fairness;
- KV-cache management;
- paged attention;
- speculative decoding;
- tensor/pipeline parallelism;
- model multiplexing;
- cold start and model loading;
- rate limits, quotas, and admission control.

### 4. Measurement and operations

- throughput vs latency;
- p50/p95/p99 and tail amplification;
- queueing and Little's law;
- GPU utilization, memory, power, temperature;
- cost per token/request;
- autoscaling;
- capacity planning;
- SLOs and error budgets (S15).

### 5. Gateway design

- API schema and streaming;
- authentication and authorization;
- request limits and timeouts;
- retries and idempotency;
- prompt/response logging with privacy;
- caching;
- observability;
- fallback and circuit breaking.

## Labs

### Lab 1 — GPU/simulator architecture

If a GPU is available, write a simple CUDA/Triton kernel (vector add, reduction, tiled matmul) and profile it. If not, use a simulator or a CPU model and explicitly label the limitation. Measure memory bandwidth and compare with the roofline.

### Lab 2 — Memory calculator

Write a calculator for weights, activations, KV cache, and optimizer state for several model sizes, sequence lengths, batch sizes, and dtypes. Validate one result against a real model or documented configuration.

### Lab 3 — Inference gateway

Build a gateway that:

- accepts requests and streams responses;
- enforces per-client limits;
- queues with a bounded queue;
- tracks queue time, batch size, tokens/sec, memory, p50/p95/p99;
- handles timeout, cancellation, and overload;
- exposes metrics/logs.

Use a real small model or a deterministic simulator.

### Lab 4 — Batching experiment

Compare no batching, static batching, and continuous batching (or simulate). Measure throughput, latency, and memory. Explain the knee.

### Lab 5 — Quantization/cache experiment

Compare one factor: dtype/quantization, KV-cache size, context length, or concurrency. Report quality impact (perplexity or task metric) and operational impact. State the trade-off.

## Exercises

1. Calculate model weight memory for 7B/13B/70B at FP16/INT8/INT4.
2. Calculate KV-cache size for a given layers/heads/head-dim/context/batch.
3. Explain prefill vs decode.
4. Explain why continuous batching improves utilization.
5. Explain paged attention.
6. Explain speculative decoding and when it helps.
7. Explain tensor vs pipeline parallelism.
8. Explain one cause of p99 latency in serving.
9. Explain a GPU memory fragmentation failure.
10. State when a CPU/simulator result is not generalizable.

## Project increment — P9 serving/gateway

Add an inference gateway/simulator to P9:

- API and streaming;
- bounded queue and admission control;
- metrics and structured logs;
- load test with p50/p95/p99;
- one batching/cache/quantization experiment;
- a cost and limitation section.

**Brief:** [P9 — doc-compass](../projects/project-ladder.md#p9--doc-compass)

## Exit check

- [ ] explain a measured throughput/latency trade-off and its hardware or queueing cause;
- [ ] calculate model and KV-cache memory;
- [ ] demonstrate bounded behaviour under overload;
- [ ] explain one GPU-specific bottleneck;
- [ ] state when a simulator is and is not acceptable evidence;
- [ ] present a cost/quality trade-off.

## Common failure modes

- Measuring tokens/sec without latency or quality.
- Ignoring KV-cache memory.
- Unbounded queues and request buffers.
- Comparing batching configurations at different loads.
- Reporting GPU utilization as if it were efficiency.
- Using a simulator and hiding the limitation.
- Forgetting privacy in prompt/response logs.

## Evidence to commit

- `labs/systems/S13/` with architecture notes, memory calculator, gateway, batching experiment, report
- P9 gateway increment
- `notes/systems/S13/summary.md`

## Optional depth

- *Programming Massively Parallel Processors* (Kirk & Hwu).
- *Efficient Processing of Deep Neural Networks* (Sze et al.).
- vLLM, TensorRT-LLM, Triton Inference Server docs.
- Kubernetes GPU scheduling and autoscaling.
