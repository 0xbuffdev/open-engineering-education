# AI2 — Machine Learning Foundations

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** AI1 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Study supervised learning, regression, classification, feature engineering, regularization, validation, metrics, calibration, and common failure modes using reproducible experiments.

## Learning outcomes

- Frame supervised-learning problems from concrete requirements.
- Build and compare baseline models using reproducible pipelines.
- Choose evaluation metrics that match the consequences of different errors.
- Detect leakage and poor validation practices.
- Interpret model performance through error analysis and calibration.

## Modules

### Module 1 — Supervised Learning

#### Outcomes

By the end of this module, the learner can:

- Explain **Problem setup and supervised learning** in the context of the course.
- Apply **Regression and classification** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Problem setup and supervised learning** — `lesson`
2. **Regression and classification** — `lesson`
3. **Checkpoint: learning setup** — `test`
4. **Micro-lab: Train a simple baseline and inspect its errors.** — `lab`

### Module 2 — Trees, Ensembles & Features

#### Outcomes

By the end of this module, the learner can:

- Explain **Decision trees and ensembles** in the context of the course.
- Apply **Feature engineering and representation** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Decision trees and ensembles** — `lesson`
2. **Feature engineering and representation** — `lesson`
3. **Checkpoint: model selection** — `test`
4. **Micro-lab: Compare a baseline with one justified feature change.** — `lab`

### Module 3 — Validation & Generalization

#### Outcomes

By the end of this module, the learner can:

- Explain **Cross-validation and evaluation metrics** in the context of the course.
- Apply **Overfitting and regularization** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Cross-validation and evaluation metrics** — `lesson`
2. **Overfitting and regularization** — `lesson`
3. **Checkpoint: generalization** — `test`
4. **Micro-lab: Plot training and validation behavior and diagnose overfitting.** — `lab`

### Module 4 — Leakage, Calibration & Error Analysis

#### Outcomes

By the end of this module, the learner can:

- Explain **Target leakage and contamination** in the context of the course.
- Apply **Calibration and structured error analysis** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Target leakage and contamination** — `lesson`
2. **Calibration and structured error analysis** — `lesson`
3. **Checkpoint: trustworthy evaluation** — `test`
4. **Micro-lab: Find a plausible leakage path and design a test for it.** — `lab`

### Module 5 — Evaluated ML Pipeline

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, evaluate, and document the Evaluated ML Pipeline** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

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
