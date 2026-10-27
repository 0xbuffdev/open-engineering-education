# AI8 — Distributed & Large-Scale Training

**Track:** AI & ML · **Prerequisite:** AI7; S11 recommended · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P8 scaling report
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Understand why large-model training is a systems problem: memory, communication, parallelism, checkpointing, and failure recovery. You will estimate resource requirements, run or simulate a small distributed configuration, and report honestly what your hardware could establish.

## Outcomes

You can:

- calculate parameter, gradient, optimizer, and activation memory;
- explain data, tensor, pipeline, sequence, and sharded parallelism;
- explain all-reduce, all-gather, reduce-scatter, and communication bottlenecks;
- choose a parallelism strategy for a stated model and cluster;
- use gradient accumulation and mixed precision correctly;
- write checkpoint metadata that supports exact resume;
- inject a failure and prove recovery without corrupting evaluation provenance;
- distinguish weak and strong scaling;
- report throughput, memory, cost, and hardware limits.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [ZeRO paper](https://arxiv.org/abs/1910.02054) | Full | Memory partitioning |
| [Megatron-LM paper](https://arxiv.org/abs/1909.08053) | Full | Tensor parallelism |
| [GPipe paper](https://arxiv.org/abs/1811.06965) | Full | Pipeline parallelism |
| [PyTorch FSDP docs](https://pytorch.org/docs/stable/fsdp.html) | Overview and sharding strategy | Implementation |
| [DeepSpeed docs](https://www.deepspeed.ai/) | ZeRO stages, offload, checkpointing | Implementation |
| [Efficient Large-Scale Training](https://arxiv.org/abs/2004.05150) or survey | Selected | Systems trade-offs |
| [NCCL docs](https://docs.nvidia.com/deeplearning/nccl/) | Collectives, topology | Communication |
| S11 | Replication, failure models, idempotency | Distributed reasoning |

## Modules

### 1. Memory accounting

- parameters by dtype;
- gradients;
- optimizer state (Adam moments);
- activations and checkpointing;
- temporaries and fragmentation;
- KV cache during training/inference;
- activation recomputation trade-offs;
- CPU/NVMe offload.

### 2. Parallelism

- data parallelism;
- distributed data parallel and gradient buckets;
- tensor/model parallelism;
- pipeline parallelism and microbatching;
- sequence parallelism;
- fully sharded data parallelism (ZeRO-3/FSDP);
- expert parallelism (awareness);
- hybrid strategies;
- collective operations and topology.

### 3. Communication and scaling

- bandwidth, latency, and overlap;
- all-reduce, all-gather, reduce-scatter, broadcast;
- ring and tree algorithms;
- interconnect: PCIe, NVLink, InfiniBand;
- communication-to-computation ratio;
- weak versus strong scaling;
- stragglers;
- global batch size and learning-rate scaling.

### 4. Reliability and checkpointing

- failure during training;
- checkpoint contents: model, optimizer, scheduler, RNG, data position, config, code commit;
- atomic checkpoint writes;
- sharded checkpoints;
- resume validation;
- elastic training (awareness);
- data-loader determinism;
- experiment provenance;
- spot-instance preemption.

### 5. Cost and reporting

- GPU-hours and utilization;
- memory-bandwidth and compute roofline;
- cost per training run and per token;
- energy/carbon reporting;
- comparing runs at equal tokens or equal compute;
- what a single-node simulation cannot prove.

## Labs

### Lab 1 — Memory calculator

Write a calculator for weights, gradients, optimizer state, activations, and KV cache for several model sizes, batch sizes, sequence lengths, and parallelism settings. Validate one result against a real run or documented configuration.

### Lab 2 — Distributed baseline

If multiple GPUs are available, run a small model with DDP and one sharded configuration. If not, use a CPU/gloo multi-process run or simulate communication costs with a documented fallback. Compare throughput and memory.

### Lab 3 — Parallelism comparison

Compare at least two strategies (e.g., DDP versus gradient accumulation, or FSDP versus DDP) on the same model and global batch. Report throughput, memory, communication, and loss equivalence.

### Lab 4 — Checkpoint and restart

Interrupt training at a controlled step. Restore from checkpoint and prove that loss, optimizer state, scheduler, RNG, and data position resume correctly. Deliberately corrupt a checkpoint and verify rejection.

### Lab 5 — Scaling report

Produce a report with:

- hardware and interconnect;
- model and global batch;
- weak/strong scaling data;
- bottleneck analysis;
- failure/recovery evidence;
- cost and limitations;
- what would change at 10× scale.

## Exercises

1. Calculate Adam memory for a 1B-parameter model in FP16.
2. Estimate activation memory for a transformer block.
3. Explain why ZeRO reduces per-GPU memory.
4. Compare tensor and pipeline parallelism.
5. Calculate communication volume for an all-reduce.
6. Explain a global-batch learning-rate adjustment.
7. List checkpoint fields needed for exact resume.
8. Explain one straggler cause.
9. Distinguish weak and strong scaling.
10. State what a single-GPU benchmark cannot establish.

## Project increment — P8 scaling report

Add:

- a resource estimate for the model;
- a distributed or documented-simulation run;
- scaling table and bottleneck analysis;
- checkpoint/resume proof;
- cost and hardware limitations;
- a decision about whether scaling is justified.

**Brief:** [P8 — tinygpt](../projects/project-ladder.md#p8--tinygpt)

## Exit check

- [ ] calculate training memory and explain each term;
- [ ] explain the chosen parallelism strategy and its communication cost;
- [ ] show loss equivalence or a justified discrepancy across configurations;
- [ ] resume exactly after an interruption;
- [ ] report scaling data with hardware and batch size;
- [ ] distinguish measured results from simulated/estimated ones.

## Common failure modes

- Comparing throughput at different global batch sizes.
- Forgetting optimizer state in memory estimates.
- Checkpointing without data-loader position or RNG state.
- Assuming more GPUs always improve throughput.
- Ignoring communication topology.
- Reporting GPU utilization as efficiency.
- Hiding a single-device fallback as distributed evidence.
- Resuming with a different code/config revision.

## Evidence to commit

- `labs/ai/AI8/` with memory calculator, distributed run, scaling table, checkpoint test, report
- P8 scaling report
- `notes/ai/AI8/summary.md`
- `notes/ai/AI8/resources.md` with cluster, interconnect, versions, and cost

## Optional depth

- *Programming Massively Parallel Processors* (Kirk & Hwu), selected chapters.
- PyTorch Distributed overview and `torch.distributed` docs.
- DeepSpeed ZeRO stages and offload.
- Alpa, GSPMD, and Pathways papers.
- `nccl-tests` and network topology tools.
