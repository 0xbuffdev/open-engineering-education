# AI3 — Classical Machine Learning

**Track:** AI & ML · **Prerequisite:** AI1, AI2 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P7 signal-score

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn to build an honest predictive baseline on tabular data. The emphasis is on problem framing, leakage-resistant evaluation, error analysis, and calibration — not on collecting algorithms. A well-evaluated logistic regression is more professional than an unevaluated transformer.

## Outcomes

You can:

- frame a prediction problem and define the unit of analysis;
- choose a metric from the real cost of errors;
- build a leakage-resistant train/validation/test protocol;
- implement and tune linear, tree-based, and ensemble models;
- use cross-validation correctly, including grouped and time-series splits;
- diagnose underfitting, overfitting, and data bugs from learning curves;
- calibrate probabilities and choose thresholds;
- perform error analysis by subgroup and feature;
- write a model card and a reproducible evaluation report.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [An Introduction to Statistical Learning](https://www.statlearning.com/) (ISL, 2nd ed., free) | Ch. **2–6** | Learning, regression, classification, resampling, selection, regularization |
| ISL | Ch. **8–9** | Tree-based methods and SVMs |
| ISL | Ch. **13** (multiple testing) or selected | Honest inference and selection |
| [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) | Pipelines, model selection, metrics, calibration, preprocessing | Correct implementation |
| [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | Full | Documentation standard |
| [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) | Selected rules | Production heuristics |
| [Fairness and Machine Learning](https://fairmlbook.org/) | Ch. **1–3** | Harms, measurement, and allocative decisions |

## Modules

### 1. Problem framing

- prediction target and decision;
- unit of analysis and label definition;
- when a model is unnecessary;
- performance thresholds and human baseline;
- metric selection: accuracy, precision, recall, F1, ROC-AUC, PR-AUC, MAE, RMSE;
- class imbalance and cost-sensitive evaluation;
- distribution shift and temporal validity;
- ethical and legal constraints.

### 2. Data and leakage

- train/validation/test split;
- stratification;
- grouped splits (same patient/customer/device);
- temporal splits;
- target leakage;
- preprocessing inside the pipeline;
- duplicates across splits;
- feature availability at prediction time.

### 3. Linear models

- ordinary least squares;
- ridge and lasso;
- logistic regression;
- regularization strength and scaling;
- coefficients, odds, and interpretation;
- assumptions and failure modes.

### 4. Trees and ensembles

- decision trees: splits, impurity, pruning;
- bagging and random forests;
- gradient boosting (concept and practice);
- feature importance pitfalls;
- monotonic constraints (intro);
- hyperparameter search.

### 5. Evaluation and selection

- cross-validation;
- nested CV for honest tuning;
- learning and validation curves;
- model selection under uncertainty;
- repeated seeds;
- statistical versus practical significance;
- baseline comparisons.

### 6. Calibration and thresholds

- probability calibration;
- reliability diagrams;
- Brier score;
- threshold selection from costs;
- precision-recall trade-off;
- subgroup calibration.

### 7. Error analysis

- confusion matrix and per-class errors;
- slice analysis;
- nearest-neighbour inspection;
- label noise;
- spurious correlations;
- counterfactual checks;
- a written error taxonomy with examples.

## Labs

### Lab 1 — Baseline ladder

For P7, build:

1. a trivial baseline (majority/mean);
2. a single-feature rule;
3. logistic/linear regression;
4. one tree ensemble.

Use the same split and preprocessing. Report the metric with uncertainty across seeds.

### Lab 2 — Leakage hunt

Create three deliberately leaky variants (target-derived feature, duplicate rows, preprocessing before split). Show inflated validation scores and the corrected protocol. This lab is about detecting leakage, not exploiting it.

### Lab 3 — Cross-validation and tuning

Compare a single holdout with k-fold and grouped/time-series CV. Tune one hyperparameter. Show how random seed and fold choice change the conclusion. Use nested CV for the final estimate.

### Lab 4 — Calibration and threshold

Calibrate the best model. Plot reliability before and after. Choose a threshold from an explicit cost matrix and report the confusion matrix at that threshold. Explain who bears the errors.

### Lab 5 — Error analysis and model card

Inspect at least 30 errors. Group them into an error taxonomy. Identify one subgroup or slice with worse performance. Write a model card with intended use, non-use, limitations, and evaluation gaps.

## Exercises

1. Choose a metric for a screening problem with asymmetric costs.
2. Explain why accuracy fails under class imbalance.
3. Identify leakage in five feature tables.
4. Explain grouped versus stratified CV with an example.
5. Derive precision and recall from a confusion matrix.
6. Explain ROC-AUC versus PR-AUC.
7. Interpret a calibration curve.
8. Explain why feature importance can mislead.
9. Design a temporal validation split.
10. Write a model card section for a system you would not deploy.

## Project increment — P7 signal-score

Build the complete tabular ML baseline:

- dataset card and frozen split;
- trivial baseline plus at least two model families;
- leakage-resistant pipeline;
- cross-validation and held-out test;
- calibration and threshold rationale;
- error analysis and model card;
- one-command reproduction.

**Brief:** [P7 — signal-score](../projects/project-ladder.md#p7--signal-score)

## Exit check

- [ ] defend the metric from the decision and error costs;
- [ ] prove there is no target leakage or duplicate contamination;
- [ ] show a baseline comparison on an untouched test set;
- [ ] explain cross-validation choices, including groups or time;
- [ ] calibrate the model and justify a threshold;
- [ ] present an error taxonomy with concrete examples;
- [ ] state intended use, non-use, and evaluation limits.

## Common failure modes

- Tuning on the test set.
- Fitting scalers/imputers before splitting.
- Randomly splitting grouped or temporal data.
- Reporting one seed and calling it stable.
- Optimizing accuracy on imbalanced data.
- Treating feature importance as causation.
- Omitting the trivial baseline.
- Deploying a probability without checking calibration.

## Evidence to commit

- `labs/ai/AI3/` with baseline ladder, leakage study, CV/tuning, calibration, error analysis
- P7 model, evaluation report, and model card
- `notes/ai/AI3/summary.md`

## Optional depth

- ISL Ch. 7 (nonlinear models), 10 (deep learning), 11 (survival), 12 (unsupervised).
- *The Elements of Statistical Learning* (Hastie et al.), selected chapters.
- *Interpretable Machine Learning* (Molnar), selected chapters.
- `category_encoders`, `imbalanced-learn`, `Optuna`.
- Conformal prediction (intro) for distribution-free intervals.
