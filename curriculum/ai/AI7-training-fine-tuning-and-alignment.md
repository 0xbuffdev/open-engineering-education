# AI7 — Training, Fine-Tuning & Alignment

**Track:** AI & ML · **Prerequisite:** AI6 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P8 LoRA comparison
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Learn how to adapt a pretrained model responsibly and prove whether the adaptation helped. You will compare prompting, full fine-tuning, and parameter-efficient tuning; design a fixed evaluation; and confront memorization, contamination, and preference optimization.

## Outcomes

You can:

- choose between prompting, RAG, full fine-tuning, and parameter-efficient tuning;
- prepare and document a supervised fine-tuning dataset;
- explain LoRA/QLoRA and calculate trainable parameters;
- implement a small fine-tuning run with checkpointing and rollback;
- design a fixed evaluation set and scoring rubric before training;
- detect regressions, memorization, and contamination;
- explain preference data, reward models, PPO, and DPO at a conceptual level;
- write stop/rollback conditions and a model-card update.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) | Ch. **7, 11–12** | Fine-tuning, tuning, and alignment |
| [LoRA paper](https://arxiv.org/abs/2106.09685) | Full | Low-rank adaptation |
| [QLoRA paper](https://arxiv.org/abs/2305.14314) | Full | Quantized adaptation |
| [InstructGPT paper](https://arxiv.org/abs/2203.02155) | Full | Instruction tuning and preference optimization |
| [DPO paper](https://arxiv.org/abs/2305.18290) | Full | Direct preference optimization |
| [PEFT docs](https://huggingface.co/docs/peft) | LoRA, adapters, saving/loading | Implementation |
| [TRL docs](https://huggingface.co/docs/trl) | SFT, DPO, evaluation | Implementation |
| [HELM](https://crfm.stanford.edu/helm/) or lm-evaluation-harness docs | Evaluation design | Honest comparison |

## Modules

### 1. Adaptation choices

- prompt engineering and few-shot prompting;
- retrieval-augmented generation;
- adapter layers;
- LoRA and rank/alpha/dropout;
- QLoRA and quantization;
- full fine-tuning;
- instruction tuning;
- catastrophic forgetting;
- cost and latency trade-offs.

### 2. Data for fine-tuning

- task definition and label schema;
- collecting or licensing data;
- deduplication and contamination;
- train/validation/test separation;
- prompt templates and formatting;
- class/domain balance;
- PII and copyright review;
- synthetic data risks;
- data versioning.

### 3. Training mechanics

- tokenization and sequence packing;
- loss masking;
- batch size and gradient accumulation;
- learning rate and schedules;
- gradient checkpointing;
- memory: weights, gradients, optimizer state, activations;
- mixed precision;
- checkpointing and resume;
- experiment tracking.

### 4. Evaluation integrity

- predeclared metrics and rubric;
- fixed prompts and decoding settings;
- held-out and adversarial sets;
- base versus adapted comparison;
- multiple seeds and confidence intervals;
- regressions on general capability;
- memorization probes;
- human evaluation and annotator agreement;
- cherry-picking and selective reporting.

### 5. Alignment concepts

- supervised fine-tuning;
- preference data and pairwise comparisons;
- reward modelling;
- PPO and KL constraints;
- DPO;
- constitutional/rule-based approaches (awareness);
- overoptimization and reward hacking;
- safety evaluation versus capability evaluation;
- rollback and staged release.

## Labs

### Lab 1 — Adaptation decision memo

For a concrete task, compare prompting, RAG, LoRA, and full fine-tuning on cost, data needs, latency, and risk. Choose one and justify it. State why the others are rejected.

### Lab 2 — Small LoRA run

Fine-tune a small licensed model on a benign, non-sensitive dataset. Record trainable parameter percentage, memory, time, and cost. Compare base and adapted outputs on a fixed prompt set.

### Lab 3 — Fixed evaluation

Build a held-out evaluation set before training. Use at least two metrics: task quality and one regression/format metric. Report confidence intervals or seed variance. Include examples of failures, not only successes.

### Lab 4 — Memorization and contamination

Probe exact/near-exact reproduction of training examples. Check for duplicates across splits. Show one case where an apparent improvement is explained by contamination or prompt leakage.

### Lab 5 — Preference optimization (concept or small run)

Using a tiny preference dataset, compare SFT-only with DPO (or simulate the objective). Explain the reward/KL trade-off, and identify one way the evaluation could be gamed. Do not claim alignment from a small run.

## Exercises

1. Calculate LoRA trainable parameters for a given rank and target modules.
2. Compare full fine-tuning and LoRA memory requirements.
3. Explain why lower loss does not guarantee a better assistant.
4. Design a prompt template and label mask for SFT.
5. Identify three contamination routes.
6. Write a predeclared evaluation rubric.
7. Explain DPO versus PPO at a high level.
8. Define a rollback threshold.
9. Explain catastrophic forgetting with an example.
10. State what a 100-example evaluation can and cannot establish.

## Project increment — P8 LoRA comparison

Add:

- a documented adaptation dataset;
- LoRA configuration and trainable-parameter calculation;
- base versus adapted evaluation on fixed prompts;
- regression and memorization checks;
- a cost/latency comparison;
- a model card update and rollback rule.

**Brief:** [P8 — tinygpt](../projects/project-ladder.md#p8--tinygpt)

## Exit check

- [ ] justify the adaptation method against simpler alternatives;
- [ ] show the trainable-parameter and memory calculation;
- [ ] reproduce the evaluation from fixed prompts and settings;
- [ ] report both improvement and regression;
- [ ] demonstrate a contamination/memorization check;
- [ ] state stop/rollback conditions and residual risk.

## Common failure modes

- Evaluating on examples seen during fine-tuning.
- Changing prompts, decoding, or test sets between comparisons.
- Reporting only the best checkpoint.
- Ignoring general-capability regression.
- Training on sensitive or unlicensed data.
- Treating DPO/RLHF as a safety guarantee.
- Confusing loss with task quality.

## Evidence to commit

- `labs/ai/AI7/` with adaptation memo, LoRA run, evaluation set, memorization probe
- P8 adapter/config, evaluation report, model card update
- `notes/ai/AI7/summary.md`
- `notes/ai/AI7/resources.md` with model license and compute cost

## Optional depth

- *Practical Deep Learning for Coders* selected fine-tuning lessons.
- Hugging Face `alignment-handbook`.
- InstructGPT, Constitutional AI, and LLaMA 2 papers.
- *Reinforcement Learning from Human Feedback* survey.
- `lm-evaluation-harness` task implementation.
