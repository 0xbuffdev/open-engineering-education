## AI4 — Transformers & Large Language Models

**Duration:** 7 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** AI3

### Overview

Study the architecture and behavior of transformer-based language models, including tokenization, embeddings, attention, causal masking, positional information, and decoder-only training.

### Prerequisites

**AI3 — Deep Learning & Representation Learning**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain the major components of a transformer architecture.
- Calculate and reason about attention tensor shapes and causal masking.
- Explain how tokenization, embeddings, and positional information contribute to language modeling.
- Implement or inspect a minimal decoder-only transformer with understanding of its components.
- Distinguish training loss from evaluation evidence of useful model behavior.


### Resource map

**Required**

- **B37** Ch. 2–5 (text data; attention; GPT; pretraining) — the from-scratch LLM resource ZtP AI6 names without chapters.
- **B36** Ch. 11 §§11.5–11.7 (multi-head attention; self-attention and positional encoding; the Transformer architecture).
- **R49** The Illustrated Transformer · **R50** Attention Is All You Need — carried from ZtP AI6.

**Optional**

- **R51** Hugging Face LLM Course (tokenizers and the Transformers library).

### Modules

#### Module 1 — Tokenization & Representations

**Reading:** **B37** Ch. 2 (Working with Text Data — tokenization, byte pair encoding, sliding-window data sampling, token embeddings, positional encodings). **R50** §3.4 (Embeddings and Softmax), §3.5 (Positional Encoding).


### Module outcomes

By the end of this module, the learner can:

- Explain **Tokenization and vocabulary design** in the context of the course.
- Apply **Embeddings and positional information** in a problem, implementation, experiment, or design decision.

1. **Tokenization and vocabulary design**
   - kind: `lesson`
2. **Embeddings and positional information**
   - kind: `lesson`
3. **Checkpoint: representation basics**
   - kind: `test`

4. **Micro-lab: Inspect token sequences and reason about representation shapes.**
   - kind: `lab`
#### Module 2 — Attention & Causal Masking

**Reading:** **B37** Ch. 3 (Coding Attention Mechanisms — simple self-attention, trainable weights, causal attention, multi-head attention). **B36** §§11.5–11.6. **R50** §3.2 (Attention). **R49** the walkthrough.


### Module outcomes

By the end of this module, the learner can:

- Explain **Attention mechanics and tensor shapes** in the context of the course.
- Apply **Causal masking and autoregressive behavior** in a problem, implementation, experiment, or design decision.

1. **Attention mechanics and tensor shapes**
   - kind: `lesson`
2. **Causal masking and autoregressive behavior**
   - kind: `lesson`
3. **Checkpoint: attention reasoning**
   - kind: `test`

4. **Micro-lab: Calculate attention shapes for a tiny sequence and apply a causal mask.**
   - kind: `lab`
#### Module 3 — Transformer Architecture

**Reading:** **B37** Ch. 4 (Implementing a GPT Model from Scratch to Generate Text — layer normalization, GELU feed-forward network, shortcut connections, the transformer block, the GPT model). **B36** §11.7 (The Transformer Architecture). **R50** §3 (Model Architecture).


### Module outcomes

By the end of this module, the learner can:

- Explain **Transformer blocks and decoder architecture** in the context of the course.
- Apply **Residual paths and normalization concepts** in a problem, implementation, experiment, or design decision.

1. **Transformer blocks and decoder architecture**
   - kind: `lesson`
2. **Residual paths and normalization concepts**
   - kind: `lesson`
3. **Checkpoint: transformer architecture**
   - kind: `test`

4. **Micro-lab: Trace a token through a simplified decoder block.**
   - kind: `lab`
#### Module 4 — Language Model Training & Evaluation

**Reading:** **B37** Ch. 5 (Pretraining on Unlabeled Data — evaluating generative models, training, decoding strategies, loading pretrained weights), Ch. 7 (Fine-Tuning to Follow Instructions) and App. D (training-loop improvements). **B38** Ch. 3 (Evaluation Methodology — language-modeling metrics).


### Module outcomes

By the end of this module, the learner can:

- Explain **Language-model training objectives** in the context of the course.
- Apply **Held-out evaluation and fine-tuning concepts** in a problem, implementation, experiment, or design decision.

1. **Language-model training objectives**
   - kind: `lesson`
2. **Held-out evaluation and fine-tuning concepts**
   - kind: `lesson`
3. **Checkpoint: model evaluation**
   - kind: `test`

4. **Micro-lab: Define a simple evaluation split and explain what it can and cannot show.**
   - kind: `lab`
#### Module 5 — Tiny Decoder-Only Transformer

**Reading:** **B37** Ch. 4–5 and App. A (Introduction to PyTorch). **B36** §11.9 (Large-Scale Pretraining with Transformers).


1. **Train, evaluate, and document the Tiny Decoder-Only Transformer**
   - kind: `lab`

### Topics

- tokenization
- embeddings
- attention
- positional information
- causal masking
- transformer blocks
- decoder architecture
- language-model training
- evaluation
- fine-tuning concepts

### Labs

- calculate attention shapes by hand
- implement scaled dot-product attention
- implement a minimal transformer block
- inspect training loss
- evaluate generated outputs

### Substantial course lab

**Tiny Decoder-Only Transformer**

Train a small model on a licensed dataset and provide:

- training logs
- held-out evaluation
- limitations
- architecture diagram
- error analysis

---

