## AI6 — Training, Fine-Tuning & Evaluation

**Duration:** 5 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** AI4

### Overview

Study fine-tuning, parameter-efficient adaptation, dataset construction, evaluation design, contamination, memorization, and experiment tracking. Learners compare adapted models against fixed baselines.

### Prerequisites

**AI4 — Transformers & Large Language Models**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Prepare a fine-tuning dataset with documented assumptions and limitations.
- Apply parameter-efficient fine-tuning to a suitable model.
- Design fixed evaluation sets and compare adapted models with baselines.
- Identify signs of memorization, contamination, or cherry-picked evaluation.
- Report training configuration, compute cost, results, limitations, and rollback criteria.


### Resource map

**Required**

- **B38** Ch. 3–4 (evaluation), Ch. 7 (Finetuning) and Ch. 8 (Dataset Engineering).
- **B37** Ch. 6–7 and App. E (fine-tuning for classification and for instructions; LoRA).
- **R52** Hugging Face PEFT documentation — carried from ZtP AI7 · **R53** the LoRA paper.
- **B35** Ch. 6 (Model Development and Offline Evaluation — experiment tracking and versioning).

### Modules

#### Module 1 — Fine-Tuning Fundamentals

**Reading:** **B38** Ch. 7 (Finetuning — when to finetune; memory bottlenecks; finetuning techniques: PEFT, LoRA, QLoRA). **B37** Ch. 6–7 and App. E (Parameter-Efficient Finetuning with LoRA). **R52** PEFT quicktour and LoRA guide. **R53** the LoRA paper.


### Module outcomes

By the end of this module, the learner can:

- Explain **Fine-tuning objectives and adaptation** in the context of the course.
- Apply **LoRA/PEFT concepts** in a problem, implementation, experiment, or design decision.

1. **Fine-tuning objectives and adaptation**
   - kind: `lesson`
2. **LoRA/PEFT concepts**
   - kind: `lesson`
3. **Checkpoint: fine-tuning methods**
   - kind: `test`

4. **Micro-lab: Configure a small adaptation run and identify which parameters are trainable.**
   - kind: `lab`
#### Module 2 — Dataset Quality & Contamination

**Reading:** **B38** Ch. 8 (Dataset Engineering — data curation; augmentation and synthesis; data processing: inspection, deduplication, cleaning), Ch. 4 (data contamination in public benchmarks). **B35** Ch. 4 (Training Data).


### Module outcomes

By the end of this module, the learner can:

- Explain **Dataset quality and memorization** in the context of the course.
- Apply **Contamination and data leakage** in a problem, implementation, experiment, or design decision.

1. **Dataset quality and memorization**
   - kind: `lesson`
2. **Contamination and data leakage**
   - kind: `lesson`
3. **Checkpoint: data risks**
   - kind: `test`

4. **Micro-lab: Design a test for possible contamination or memorization.**
   - kind: `lab`
#### Module 3 — Evaluation Design

**Reading:** **B38** Ch. 3 (Evaluation Methodology — exact, subjective and comparative evaluation), Ch. 4 (Evaluate AI Systems — evaluation criteria; model selection; designing an evaluation pipeline). **B35** Ch. 6 (offline evaluation: baselines; evaluation methods).


### Module outcomes

By the end of this module, the learner can:

- Explain **Fixed evaluation suites** in the context of the course.
- Apply **Ablations and meaningful comparisons** in a problem, implementation, experiment, or design decision.

1. **Fixed evaluation suites**
   - kind: `lesson`
2. **Ablations and meaningful comparisons**
   - kind: `lesson`
3. **Checkpoint: evaluation design**
   - kind: `test`

4. **Micro-lab: Design one controlled ablation that can support a causal claim.**
   - kind: `lab`
#### Module 4 — Compute & Reproducibility

**Reading:** **B35** Ch. 6 (experiment tracking and versioning), Ch. 10 (Infrastructure and Tooling for MLOps). **B38** Ch. 7 (memory requirements for finetuning).


### Module outcomes

By the end of this module, the learner can:

- Explain **Compute cost and experiment tracking** in the context of the course.
- Apply **Reproducibility and rollback decisions** in a problem, implementation, experiment, or design decision.

1. **Compute cost and experiment tracking**
   - kind: `lesson`
2. **Reproducibility and rollback decisions**
   - kind: `lesson`
3. **Checkpoint: reproducible experiments**
   - kind: `test`

4. **Micro-lab: Record configuration, compute cost, and model/version identifiers for a run.**
   - kind: `lab`
#### Module 5 — Fine-Tuning Study

**Reading:** **B38** Ch. 7. **B37** Ch. 7. **R52** PEFT documentation.


1. **Run, compare, and defend the Fine-Tuning Study**
   - kind: `lab`

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

---

