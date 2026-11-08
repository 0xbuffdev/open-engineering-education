> Part of the [Zero to Software Engineer](../00-overview.md) curriculum · Program 4 of 5 · [Resource library](../resources/README.md) · [Shared standards](../shared/electives-assessment-graduation.md) · Previous: [SYS](03-SYS-systems-engineering.md) · Next: [SEC](05-SEC-security-engineering.md)

# PROGRAM 4 — AI
# AI Engineering

## Overview

AI Engineering turns the programming and mathematics from the foundations program into practical machine learning. You work through data, classical machine learning, deep learning, transformers and language models, retrieval and agents, training and evaluation, and production AI systems. The program stresses reproducible experiments and measurable evaluation, so you learn to operate models, measure their behavior, and document their limits.

## Prerequisites

**Program 1 — SEF — Software Engineering Foundations.**

Python and the mathematics covered in SEF6 are used throughout the program. Individual AI courses have their own explicit prerequisites; systems preparation is recommended where noted.

## Learning outcomes

By the end of this program, you will be able to:

- Prepare, inspect, and analyze datasets using reproducible scientific Python workflows.
- Explain and implement the mathematical and optimization foundations behind common machine-learning methods.
- Train, evaluate, and compare classical machine-learning and deep-learning models using appropriate baselines and metrics.
- Explain transformer architectures, attention, tokenization, causal masking, and the basic mechanics of language models.
- Build bounded retrieval and tool-using AI systems with explicit evaluation, permissions, and failure controls.
- Fine-tune and evaluate models while controlling for contamination, memorization, and misleading evaluation results.
- Deploy observable AI services and reason about latency, throughput, resource use, cost, rollback, and reliability.
- Identify AI risks, define measurable controls, and ship a production-grade AI system with documented limitations and safeguards.

## Program completion standard

The learner must demonstrate the knowledge, practical skills, and engineering judgment described by the program outcomes and successfully complete the program capstone.

---

---

## AI resource index

*Generated from the master library: 28 resources are used in this program. "Also used in" shows reuse by other programs. Full details: [books](../resources/books.md) · [online](../resources/online.md) · [matrix](../resources/matrix.md) · [glossary](../resources/glossary.md).*

> Access markers: 📚 local library · 🌐 free online/download · 🛒 obtain (borrow or buy) · 🔐 account, isolated lab or GPU needed.

### Books

| Code | Resource | Access | Courses in this program | Also used in |
|---|---|---|---|---|
| B3 | *Digital Design and Computer Architecture* — Harris & Harris | 📚 | AI7 | SEF, SYS |
| B6 | *What Every Programmer Should Know About Memory* — Ulrich Drepper | 📚 | AI7 | SYS |
| B16 | *Mathematics for Machine Learning* — Deisenroth, Faisal & Ong (Cambridge UP, 2020) | 🌐 | AI1, AI2, AI3 | SEF |
| B26 | *Site Reliability Engineering* — Beyer, Jones, Petoff & Murphy (O'Reilly, 2016) | 🌐 | AI7, AI8, AI9 | APP, SYS, SEC |
| B33 | *Python for Data Analysis*, 3rd ed. — Wes McKinney (O'Reilly, 2022) | 🌐 | AI1 | — |
| B34 | *An Introduction to Statistical Learning with Applications in Python* — James, Witten, Hastie, Tibshirani & Taylor (Springer, 2023) | 🌐 | AI2 | — |
| B35 | *Designing Machine Learning Systems* — Chip Huyen (O'Reilly, 2022) | 🛒 | AI1, AI2, AI6, AI7, AI8, AI9 | — |
| B36 | *Dive into Deep Learning* — Zhang, Lipton, Li & Smola | 🌐 | AI3, AI4 | — |
| B37 | *Build a Large Language Model (From Scratch)* — Sebastian Raschka (Manning, 2024) | 🛒 | AI4, AI6 | — |
| B38 | *AI Engineering* — Chip Huyen (O'Reilly, 2025) | 🛒 | AI4, AI5, AI6, AI7, AI8, AI9 | SEC |
| B39 | *Introduction to Information Retrieval* — Manning, Raghavan & Schütze (Cambridge UP, 2008) | 🌐 | AI5 | — |

### Online resources, standards and papers

| Code | Resource | Access | Courses in this program | Also used in |
|---|---|---|---|---|
| R6 | NumPy documentation — absolute basics and broadcasting (numpy.org/doc) | 🌐 | AI1 | SEF |
| R45 | PyTorch Tutorials — Learn the Basics (docs.pytorch.org/tutorials) | 🌐 | AI3 | — |
| R46 | Stanford CS231n — Convolutional Neural Networks for Visual Recognition (cs231n.github.io) | 🌐 | AI3 | — |
| R47 | scikit-learn User Guide (scikit-learn.org/stable/user_guide.html) | 🌐 | AI1, AI2 | — |
| R48 | “A Recipe for Training Neural Networks” — Andrej Karpathy (2019) (karpathy.github.io/2019/04/25/recipe) | 🌐 | AI3 | — |
| R49 | “The Illustrated Transformer” — Jay Alammar (jalammar.github.io/illustrated-transformer) | 🌐 | AI4 | — |
| R50 | “Attention Is All You Need” — Vaswani et al. (2017) (arxiv.org/abs/1706.03762) | 🌐 | AI4 | — |
| R51 | Hugging Face LLM Course (formerly NLP Course) (huggingface.co/learn) | 🌐 | AI4 | — |
| R52 | Hugging Face PEFT documentation (huggingface.co/docs/peft) | 🌐 | AI6 | — |
| R53 | “LoRA: Low-Rank Adaptation of Large Language Models” — Hu et al. (2021) (arxiv.org/abs/2106.09685) | 🌐 | AI6 | — |
| R54 | “Efficient Memory Management for LLM Serving with PagedAttention” (SOSP 2023) and vLLM documentation | 🌐 · 🔐 GPU preferred | AI7 | — |
| R55 | NIST AI Risk Management Framework 1.0 (AI 100-1) and Generative AI Profile (AI 600-1) (nist.gov/itl/ai-risk-management-framework) | 🌐 | AI8, AI9 | — |
| R56 | “Model Cards for Model Reporting” (Mitchell et al., 2019) and “Datasheets for Datasets” (Gebru et al.) | 🌐 | AI2, AI8, AI9 | — |
| R57 | “Building effective agents” — Anthropic (anthropic.com/engineering/building-effective-agents) | 🌐 | AI5 | — |
| R58 | “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” — Lewis et al. (2020) (arxiv.org/abs/2005.11401) | 🌐 | AI5 | — |
| R59 | “Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection” — Greshake et al. (2023) (arxiv.org/abs/2302.12173) | 🌐 | AI5 | SEC |
| R60 | OWASP Top 10 for LLM Applications 2025 (genai.owasp.org/llm-top-10) | 🌐 | AI5, AI8, AI9 | SEC |

---

