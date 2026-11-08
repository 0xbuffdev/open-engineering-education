## AI2 — Machine Learning Foundations

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** AI1

### Overview

Study supervised learning, regression, classification, feature engineering, regularization, validation, metrics, calibration, and common failure modes using reproducible experiments.

### Prerequisites

**AI1 — Data & Scientific Python**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Frame supervised-learning problems from concrete requirements.
- Build and compare baseline models using reproducible pipelines.
- Choose evaluation metrics that match the consequences of different errors.
- Detect leakage and poor validation practices.
- Interpret model performance through error analysis and calibration.


### Resource map

**Required**

- **B34** Ch. 2–6 and 8 (statistical learning; linear regression; classification; resampling; regularization; tree-based methods) — ZtP AI3 names ISLR without chapters.
- **B16** Ch. 7, 8 and 10 (continuous optimization; when models meet data; PCA) — Ch. 7 and 10 carried from ZtP AI2; Ch. 8 added.
- **R47** scikit-learn User Guide: supervised learning, model selection and evaluation, preprocessing, pipelines, calibration — carried from ZtP AI3.
- **B35** Ch. 5–6 (Feature Engineering; Model Development and Offline Evaluation) · **R56** Model Cards for Model Reporting.

### Modules

#### Module 1 — Supervised Learning

**Reading:** **B34** Ch. 2 (Statistical Learning), Ch. 3 (Linear Regression), Ch. 4 (Classification). **B16** Ch. 8 (When Models Meet Data), Ch. 9 (Linear Regression). **R47** supervised learning: linear models.


### Module outcomes

By the end of this module, the learner can:

- Explain **Problem setup and supervised learning** in the context of the course.
- Apply **Regression and classification** in a problem, implementation, experiment, or design decision.

1. **Problem setup and supervised learning**
   - kind: `lesson`
2. **Regression and classification**
   - kind: `lesson`
3. **Checkpoint: learning setup**
   - kind: `test`

4. **Micro-lab: Train a simple baseline and inspect its errors.**
   - kind: `lab`
#### Module 2 — Trees, Ensembles & Features

**Reading:** **B34** Ch. 8 (Tree-Based Methods). **B35** Ch. 5 (Feature Engineering). **B16** Ch. 10 (Dimensionality Reduction with PCA). **R47** decision trees; ensembles; preprocessing data.


### Module outcomes

By the end of this module, the learner can:

- Explain **Decision trees and ensembles** in the context of the course.
- Apply **Feature engineering and representation** in a problem, implementation, experiment, or design decision.

1. **Decision trees and ensembles**
   - kind: `lesson`
2. **Feature engineering and representation**
   - kind: `lesson`
3. **Checkpoint: model selection**
   - kind: `test`

4. **Micro-lab: Compare a baseline with one justified feature change.**
   - kind: `lab`
#### Module 3 — Validation & Generalization

**Reading:** **B34** Ch. 5 (Resampling Methods), Ch. 6 §6.2 (Shrinkage Methods — ridge and lasso), Ch. 2 §2.2 (Assessing Model Accuracy — the bias–variance trade-off). **B16** Ch. 7 (Continuous Optimization), Ch. 8 §§8.2–8.3 (empirical risk minimization; parameter estimation). **R47** cross-validation; metrics and scoring; tuning hyper-parameters.


### Module outcomes

By the end of this module, the learner can:

- Explain **Cross-validation and evaluation metrics** in the context of the course.
- Apply **Overfitting and regularization** in a problem, implementation, experiment, or design decision.

1. **Cross-validation and evaluation metrics**
   - kind: `lesson`
2. **Overfitting and regularization**
   - kind: `lesson`
3. **Checkpoint: generalization**
   - kind: `test`

4. **Micro-lab: Plot training and validation behavior and diagnose overfitting.**
   - kind: `lab`
#### Module 4 — Leakage, Calibration & Error Analysis

**Reading:** **B35** Ch. 5 (Feature Engineering — data leakage), Ch. 6 (Model Development and Offline Evaluation — baselines, evaluation methods, slice-based evaluation). **R47** common pitfalls and recommended practices; probability calibration.


### Module outcomes

By the end of this module, the learner can:

- Explain **Target leakage and contamination** in the context of the course.
- Apply **Calibration and structured error analysis** in a problem, implementation, experiment, or design decision.

1. **Target leakage and contamination**
   - kind: `lesson`
2. **Calibration and structured error analysis**
   - kind: `lesson`
3. **Checkpoint: trustworthy evaluation**
   - kind: `test`

4. **Micro-lab: Find a plausible leakage path and design a test for it.**
   - kind: `lab`
#### Module 5 — Evaluated ML Pipeline

**Reading:** **R47** pipelines and composite estimators. **R56** Model Cards for Model Reporting. **B35** Ch. 6. **B34** Ch. 5.


1. **Build, evaluate, and document the Evaluated ML Pipeline**
   - kind: `lab`

### Topics

- supervised learning
- regression
- classification
- trees
- ensembles
- feature engineering
- cross-validation
- metrics
- calibration
- overfitting
- regularization
- leakage
- error analysis

### Labs

- baseline versus model
- cross-validation experiment
- metric-selection exercise
- leakage investigation
- calibration comparison

### Substantial course lab

**Evaluated ML Pipeline**

A complete reproducible ML workflow with:

- baseline
- pipeline
- training
- evaluation
- error analysis
- model card

---

