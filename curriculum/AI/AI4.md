# AI4 — Transformers & Large Language Models

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** AI3 *(legacy mapping; reconcile before activation)*
**Duration:** 7 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study the architecture and behavior of transformer-based language models, including tokenization, embeddings, attention, causal masking, positional information, and decoder-only training.

## Learning outcomes

- Explain the major components of a transformer architecture.
- Calculate and reason about attention tensor shapes and causal masking.
- Explain how tokenization, embeddings, and positional information contribute to language modeling.
- Implement or inspect a minimal decoder-only transformer with understanding of its components.
- Distinguish training loss from evaluation evidence of useful model behavior.

## Modules

### Module 1 — Tokenization & Representations

#### Outcomes

By the end of this module, the learner can:

- Explain **Tokenization and vocabulary design** in the context of the course.
- Apply **Embeddings and positional information** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Tokenization and vocabulary design** — `lesson`
2. **Embeddings and positional information** — `lesson`
3. **Checkpoint: representation basics** — `test`
4. **Micro-lab: Inspect token sequences and reason about representation shapes.** — `lab`

### Module 2 — Attention & Causal Masking

#### Outcomes

By the end of this module, the learner can:

- Explain **Attention mechanics and tensor shapes** in the context of the course.
- Apply **Causal masking and autoregressive behavior** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Attention mechanics and tensor shapes** — `lesson`
2. **Causal masking and autoregressive behavior** — `lesson`
3. **Checkpoint: attention reasoning** — `test`
4. **Micro-lab: Calculate attention shapes for a tiny sequence and apply a causal mask.** — `lab`

### Module 3 — Transformer Architecture

#### Outcomes

By the end of this module, the learner can:

- Explain **Transformer blocks and decoder architecture** in the context of the course.
- Apply **Residual paths and normalization concepts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Transformer blocks and decoder architecture** — `lesson`
2. **Residual paths and normalization concepts** — `lesson`
3. **Checkpoint: transformer architecture** — `test`
4. **Micro-lab: Trace a token through a simplified decoder block.** — `lab`

### Module 4 — Language Model Training & Evaluation

#### Outcomes

By the end of this module, the learner can:

- Explain **Language-model training objectives** in the context of the course.
- Apply **Held-out evaluation and fine-tuning concepts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Language-model training objectives** — `lesson`
2. **Held-out evaluation and fine-tuning concepts** — `lesson`
3. **Checkpoint: model evaluation** — `test`
4. **Micro-lab: Define a simple evaluation split and explain what it can and cannot show.** — `lab`

### Module 5 — Tiny Decoder-Only Transformer

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Train, evaluate, and document the Tiny Decoder-Only Transformer** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

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
