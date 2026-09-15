# AI & Machine Learning Practice Guide

Every ML artifact needs a dataset card, explicit train/validation/test split, baseline, metric rationale, and error analysis. Use only licensed/public, non-sensitive data. Pin versions and seeds; do not commit weights, API keys, or large data files.

## AI1 — Python for Data and AI

### Labs

1. **Reproducible tabular analysis.** Choose one open, non-sensitive table; create a data dictionary, ingestion/cleaning script, five meaningful plots, and a notebook/report that runs from a clean environment.
2. **Data-quality audit.** Find missingness, duplicates, invalid ranges, leakage risks, and representation limits. Document which cleaning decision would change an analysis result.

### Exercises

1. reshape/filter/join/group a small table;
2. compare a vectorized operation with a Python loop for correctness and cost;
3. write a deterministic data split;
4. identify misleading plot scales/aggregations; and
5. make a minimal dataset card.

**Ready when:** the analysis is reproducible, not just an interactive notebook state.

## AI2 — Mathematics for Machine Learning

### Labs

1. **Gradient descent notebook.** Derive linear-regression gradients, implement batch gradient descent, and compare analytic and finite-difference gradients across step sizes.
2. **PCA inspection.** Implement or inspect PCA with NumPy on a small licensed dataset; show explained variance, reconstruction error, and one case where interpretation is misleading.

### Exercises

1. compute matrix/vector shapes through a linear model;
2. derive MSE gradient for a tiny dataset;
3. work conditional-probability and likelihood examples;
4. state train/validation/test assumptions; and
5. hand-check one PCA projection/reconstruction.

**Ready when:** the derivation, code, and numerical check agree within stated tolerance.

## AI3 — Classical Machine Learning

### Labs

1. **Tabular prediction baseline.** Build a leakage-resistant preprocessing/model pipeline with a trivial baseline, cross-validation, final held-out evaluation, calibration/error analysis, and model card.
2. **Failure-mode study.** Change one of class imbalance, group shift, threshold, feature availability, or leakage; show how the selected metric and model behaviour respond.

### Exercises

1. identify target leakage in supplied feature sets;
2. select metrics for false-positive versus false-negative costs;
3. implement stratified split and cross-validation reasoning;
4. inspect calibration/threshold trade-offs; and
5. write an error taxonomy from misclassified examples.

**Ready when:** the baseline is explicit and the model choice is justified against it.

## AI4 — Deep Learning Foundations

### Labs

1. **From-scratch backprop.** Implement a small autodiff/backprop exercise without PyTorch autograd; gradient-check it and test shape/error cases.
2. **Controlled MLP.** Train a PyTorch MLP with fixed splits/seeds and three one-variable ablations (for example learning rate, width, regularization). Log loss, metric, and compute cost.

### Exercises

1. trace a two-layer forward/backward pass;
2. compare activations and initialization failure modes;
3. diagnose underfit, overfit, divergence, and data bugs from curves;
4. calculate parameter counts/shapes; and
5. write a reproducible experiment command/config.

**Ready when:** a training claim is supported by a baseline and controlled ablations.

## AI5 — Vision and Sequence Architectures

### Labs

1. **Small CNN study.** Train a CNN on a licensed small image dataset; vary one architecture choice and report accuracy, classes/errors, compute, and limitations.
2. **Sequence-model comparison.** Train a compact sequence model on a benign/licensed sequence task. Compare an RNN-style model with an attention-based baseline or explicitly explain why the chosen resource prevents a fair comparison.

### Exercises

1. calculate convolution output shapes/receptive fields;
2. explain padding, stride, pooling, and inductive bias;
3. trace vanishing long-range information in a simple recurrence;
4. compare teacher forcing/training/inference; and
5. inspect class/sequence length imbalance.

**Ready when:** both models have documented dataset, split, baseline, and failure examples.

## AI6 — Transformers, NLP, and Large Language Models

### Labs

1. **Minimal decoder-only Transformer.** Train only a small, fully understood implementation or equivalent tutorial model on a small licensed corpus. Include held-out evaluation, fixed vocabulary/tokenizer, seed, and sampling controls.
2. **Attention inspection.** Record tensor shapes, causal-mask behaviour, context-length limit, and several error/failure outputs. Never treat fluent samples as the only evaluation.

### Exercises

1. calculate Q/K/V and attention tensor shapes;
2. hand-apply a causal mask to a tiny matrix;
3. distinguish token loss, perplexity, and task utility;
4. calculate parameter/memory implications of context length; and
5. define contamination-safe held-out data for a tiny corpus.

**Ready when:** causal masking and evaluation are demonstrated, not merely asserted.

## AI7 — Training, Fine-Tuning, and Alignment

### Labs

1. **Benign LoRA comparison.** Fine-tune a small licensed model on a benign, non-sensitive dataset. Compare base and adapted models against a fixed evaluation set; record configuration, compute, costs, and rollback rule.
2. **Evaluation integrity check.** Probe memorization, contamination, and cherry-picking using held-out examples, fixed prompts, and a predeclared scoring rule.

### Exercises

1. compare full fine-tuning, adapters, and prompting trade-offs;
2. calculate trainable parameter proportion;
3. design a small evaluation set and rubric;
4. identify invalid before/after comparisons; and
5. write stop/rollback conditions.

**Ready when:** apparent improvement survives the fixed evaluation and is paired with limitations.

## AI8 — Distributed and Large-Scale Training

### Labs

1. **Scaling/profile report.** Where resources allow, run a small model in one and more than one distributed configuration. Compare memory, throughput, communication, loss equivalence, checkpoint/restart, and bottleneck. A single-device simulation is an explicitly labelled fallback.
2. **Failure recovery.** Interrupt a controlled local run and prove checkpoint/resume behavior without corrupting evaluation provenance.

### Exercises

1. estimate model/optimizer/activation memory;
2. compare data, tensor, pipeline, and sharding trade-offs;
3. categorize a run as memory, compute, input, or communication bound;
4. reason about global batch-size changes; and
5. write checkpoint metadata requirements.

**Ready when:** the report states what the hardware could and could not establish.

## AI9 — Inference, Serving, and Optimization

### Labs

1. **Private toy-model service.** Serve a small local model or simulator with request limits, structured logs/metrics, timeouts, and a deterministic load generator.
2. **One-factor serving experiment.** Compare batch, cache, concurrency, or quantization configurations. Explain a p50/p95/p99 change using traces and state a cost/safety trade-off.

### Exercises

1. design request/response/error schemas;
2. define load, latency, throughput, and failure metrics;
3. calculate queueing/backpressure scenarios;
4. test timeout/cancellation/overload handling; and
5. write a safe rollout and rollback threshold.

**Ready when:** the service has bounded behavior and the benchmark is reproducible.

## AI10 — Retrieval, Agents, and Applied Generative AI

### Labs

1. **Bounded RAG service.** Build over a small licensed, non-sensitive corpus with citation display, retrieval-only baseline, allowlisted tools, human-stop control, and offline evaluation.
2. **Benign failure suite.** Test retrieval misses, stale context, prompt injection in a local test corpus, tool denial, and citation mismatch. Add automated checks for each repaired issue.

### Exercises

1. define chunking/retrieval assumptions;
2. build a labelled retrieval evaluation set;
3. compare answer quality with/without retrieval against a rubric;
4. enumerate agent authority boundaries; and
5. write safe tool schemas and rejection behavior.

**Ready when:** one retrieval and one agent failure are demonstrated and caught by repeatable evaluation.

## AI11 — MLOps and Production Deployment

### Labs

1. **Deployable earlier artifact.** Package an AI3/AI7/AI9 artifact with tests, locked dependency environment, container build, deployment manifest, versioned model/data/config, dashboard, alerts, and runbook.
2. **Bad-release rollback.** Deliberately deploy a known-bad local configuration/model, verify monitoring detects it, then restore a known-good version and preserve the incident timeline.

### Exercises

1. define model/data/config/version lineage;
2. write an SLO and alert condition;
3. distinguish offline metric, online metric, and operational metric;
4. review secrets and supply-chain boundaries; and
5. rehearse rollback from a clean checkout.

**Ready when:** rollback works in a controlled local environment and the runbook makes the decision auditable.

## AI12 — Responsible AI, Safety, Alignment, and Governance

### Labs

1. **System card and risk register.** Create these for AI9/AI10, naming intended users, non-users, data boundaries, evaluation limits, measurable controls, residual risks, and accountable owner.
2. **Benign red-team report.** Use only your controlled artifact to test documented misuse/failure cases; record scope, observations, remediation, and retest.

### Exercises

1. map harms to affected users and system controls;
2. distinguish capability evaluation from safety evaluation;
3. define an incident escalation path;
4. assess a change against the risk register; and
5. record guidance edition/date and why it may expire.

**Ready when:** every major risk has an owner, measurable control, and clearly stated residual risk.
