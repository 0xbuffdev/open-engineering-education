# AI6 — Transformers, NLP & LLMs

**Track:** AI & ML · **Prerequisite:** AI5 · **Core** · **Time:** 7 weeks, 105 hours · **Project:** P8 tinygpt

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Understand the Transformer and the language-model training loop well enough to implement, debug, evaluate, and explain a small LLM. You will build a decoder-only model, inspect attention and tokenization, and confront the gap between fluent samples and measured capability.

## Outcomes

You can:

- explain tokenization, embeddings, positional information, attention, MLP blocks, residual streams, and layer normalization;
- calculate parameter counts and activation/KV-cache memory;
- implement a decoder-only Transformer and a training loop;
- implement causal masking and verify it with a leakage test;
- explain pretraining objectives and next-token prediction;
- evaluate with loss/perplexity and task-level metrics;
- diagnose memorization, contamination, and sampling artifacts;
- control temperature, top-k, top-p, and repetition penalty;
- write a model card with limitations and intended use.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Full | Original Transformer |
| [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) | Full | Line-by-line implementation |
| D2L | Ch. **10–11, 14–15** | Attention, optimization, pretraining, applications |
| [nanoGPT](https://github.com/karpathy/nanoGPT) | `model.py`, `train.py` | Minimal decoder-only implementation |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Ch. **1–6** | Tokenizers, models, fine-tuning, evaluation |
| [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) (3rd ed. draft) | Ch. **2–3, 7–8** | Text normalization, embeddings, neural NLP |
| [GPT-2 paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | Full | Scaling and zero-shot behaviour |

## Modules

### 1. Text and tokenization

- Unicode, normalization, byte-pair encoding;
- vocabulary and special tokens;
- tokenizer training versus reuse;
- token counts and cost;
- unknown characters and byte fallback;
- tokenizer/model mismatch;
- data cleaning and deduplication.

### 2. Transformer architecture

- token embeddings;
- positional encodings (sinusoidal, learned, RoPE);
- scaled dot-product attention;
- multi-head attention;
- causal mask;
- feed-forward block;
- residual stream and layer norm;
- pre-norm versus post-norm;
- weight tying;
- output head and logits.

### 3. Training

- next-token prediction;
- cross-entropy and perplexity;
- teacher forcing and shifting;
- context length and packing;
- batch size and gradient accumulation;
- learning-rate warmup and cosine decay;
- AdamW;
- gradient clipping;
- mixed precision;
- checkpointing and resume;
- overfitting and early stopping.

### 4. Inference and sampling

- greedy, beam, temperature, top-k, top-p;
- repetition penalties;
- KV cache;
- context-window limits;
- deterministic decoding;
- streaming;
- prompt formatting;
- evaluation of generation beyond fluency.

### 5. Evaluation

- held-out loss/perplexity;
- task-specific benchmarks;
- exact match, F1, pass@k;
- contamination and memorization;
- prompt sensitivity;
- human/rubric evaluation;
- confidence intervals and sample size;
- what a small model can and cannot prove.

### 6. Safety and documentation

- data provenance and license;
- personal data and copyright;
- hallucination and calibration;
- prompt injection (preview of AI10/AI12);
- model card;
- intended use and non-use;
- compute and carbon reporting.

## Labs

### Lab 1 — Tokenizer audit

Train or load a tokenizer on a small licensed corpus. Measure vocabulary size, compression ratio, unknown/byte fallback, and tokenization of multilingual or code text. Show one failure caused by a tokenizer mismatch.

### Lab 2 — Attention and mask verification

Implement multi-head self-attention. Verify causal masking by checking that changing a future token cannot change an earlier position's output. Show tensor shapes for a small batch.

### Lab 3 — tinygpt training

Implement a decoder-only Transformer with configurable layers, heads, width, and context. Train on a small licensed corpus. Log loss, learning rate, gradient norm, and tokens/sec. Produce samples at several temperatures.

### Lab 4 — Evaluation beyond samples

Create a held-out split and at least one task-level evaluation (e.g., character-level exact match, classification probe, or a small multiple-choice set). Compare loss/perplexity with task performance. Identify one case where fluent output is wrong.

### Lab 5 — Memorization and contamination

Probe whether the model reproduces training examples. Check for duplicate/near-duplicate text across splits. Report what the evaluation cannot establish. Add a model card and a reproducible command.

## Exercises

1. Calculate the parameter count of a decoder block.
2. Hand-apply a causal mask to a 3×3 attention matrix.
3. Explain why scaled dot-product divides by √d.
4. Compare learned, sinusoidal, and RoPE positional information.
5. Explain the difference between perplexity and task accuracy.
6. Calculate KV-cache memory for a given model and context.
7. Explain top-k versus top-p sampling.
8. Design a contamination-resistant held-out set.
9. Explain why loss can improve while generation quality does not.
10. Write a model card non-use statement.

## Project increment — P8 tinygpt

Build:

- a tokenizer and documented corpus;
- a configurable decoder-only Transformer;
- a reproducible training loop with checkpoint/resume;
- held-out loss and one task-level evaluation;
- sampling controls and failure examples;
- a model card and compute report.

**Brief:** [P8 — tinygpt](../projects/project-ladder.md#p8--tinygpt)

## Exit check

- [ ] explain the full forward pass of your model from tokens to logits;
- [ ] demonstrate that causal masking prevents future-token leakage;
- [ ] train from a clean checkout and reproduce the evaluation;
- [ ] calculate parameter and KV-cache memory;
- [ ] show fluent-but-wrong outputs and a task-level metric;
- [ ] state contamination, data, and evaluation limits;
- [ ] explain one sampling parameter's effect with evidence.

## Common failure modes

- Evaluating on training text or near-duplicates.
- Forgetting to shift labels for next-token prediction.
- Masking after the softmax instead of before.
- Reporting samples as evaluation.
- Ignoring tokenizer/vocabulary mismatch.
- Training with a context length different from evaluation.
- Comparing models with different token counts or compute.
- Calling a tiny model "GPT-class" or claiming emergent abilities.

## Evidence to commit

- `labs/ai/AI6/` with tokenizer audit, mask test, training run, evaluation, memorization probe
- P8 tinygpt repository, config, checkpoint metadata, model card
- `notes/ai/AI6/summary.md`

## Optional depth

- *Natural Language Processing with Transformers* (Tunstall et al.).
- *Build a Large Language Model (From Scratch)* (Raschka).
- GPT-3, Chinchilla, LLaMA, and Mixtral papers.
- FlashAttention paper (connect to S13).
- `transformers`, `tokenizers`, and `datasets` documentation.
