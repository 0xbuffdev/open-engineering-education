# AI6 — Training, Fine-Tuning & Evaluation

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** AI4 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study fine-tuning, parameter-efficient adaptation, dataset construction, evaluation design, contamination, memorization, and experiment tracking. Learners compare adapted models against fixed baselines.

## Learning outcomes

- Prepare a fine-tuning dataset with documented assumptions and limitations.
- Apply parameter-efficient fine-tuning to a suitable model.
- Design fixed evaluation sets and compare adapted models with baselines.
- Identify signs of memorization, contamination, or cherry-picked evaluation.
- Report training configuration, compute cost, results, limitations, and rollback criteria.

## Modules

### Module 1 — Fine-Tuning Fundamentals

#### Outcomes

By the end of this module, the learner can:

- Explain **Fine-tuning objectives and adaptation** in the context of the course.
- Apply **LoRA/PEFT concepts** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Fine-tuning objectives and adaptation** — `lesson`
2. **LoRA/PEFT concepts** — `lesson`
3. **Checkpoint: fine-tuning methods** — `test`
4. **Micro-lab: Configure a small adaptation run and identify which parameters are trainable.** — `lab`

### Module 2 — Dataset Quality & Contamination

#### Outcomes

By the end of this module, the learner can:

- Explain **Dataset quality and memorization** in the context of the course.
- Apply **Contamination and data leakage** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Dataset quality and memorization** — `lesson`
2. **Contamination and data leakage** — `lesson`
3. **Checkpoint: data risks** — `test`
4. **Micro-lab: Design a test for possible contamination or memorization.** — `lab`

### Module 3 — Evaluation Design

#### Outcomes

By the end of this module, the learner can:

- Explain **Fixed evaluation suites** in the context of the course.
- Apply **Ablations and meaningful comparisons** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Fixed evaluation suites** — `lesson`
2. **Ablations and meaningful comparisons** — `lesson`
3. **Checkpoint: evaluation design** — `test`
4. **Micro-lab: Design one controlled ablation that can support a causal claim.** — `lab`

### Module 4 — Compute & Reproducibility

#### Outcomes

By the end of this module, the learner can:

- Explain **Compute cost and experiment tracking** in the context of the course.
- Apply **Reproducibility and rollback decisions** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Compute cost and experiment tracking** — `lesson`
2. **Reproducibility and rollback decisions** — `lesson`
3. **Checkpoint: reproducible experiments** — `test`
4. **Micro-lab: Record configuration, compute cost, and model/version identifiers for a run.** — `lab`

### Module 5 — Fine-Tuning Study

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Run, compare, and defend the Fine-Tuning Study** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- fine-tuning
- LoRA/PEFT
- dataset quality
- contamination
- memorization
- evaluation design
- ablations
- compute cost
- reproducibility
- experiment tracking

### Substantial course lab

**Fine-Tuning Study**

Compare a base model and adapted model using a fixed evaluation suite and document whether the improvement is real.
