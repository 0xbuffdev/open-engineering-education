# AI1 — Data & Scientific Python

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** SEF2 and SEF6 *(legacy mapping; reconcile before activation)*
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Develop the data-handling skills required for AI engineering using Python, NumPy, pandas, visualization, cleaning, and reproducible analysis. You will learn to treat data quality and provenance as engineering concerns.

## Learning outcomes

- Load, inspect, clean, transform, and analyze structured datasets with Python.
- Use NumPy arrays and vectorized operations appropriately.
- Identify missing data, inconsistent values, leakage risks, and other data-quality issues.
- Produce reproducible analyses with clear data dictionaries and visualizations.
- Explain how preprocessing choices can affect downstream model evaluation.

## Modules

### Module 1 — NumPy & Array Thinking

#### Outcomes

By the end of this module, the learner can:

- Explain **Arrays, shapes, and vectorized computation** in the context of the course.
- Apply **Comparing vectorized operations with Python loops** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Arrays, shapes, and vectorized computation** — `lesson`
2. **Comparing vectorized operations with Python loops** — `lesson`
3. **Checkpoint: array reasoning** — `test`
4. **Micro-lab: Measure a loop and vectorized version of the same workload.** — `lab`

### Module 2 — DataFrames & Cleaning

#### Outcomes

By the end of this module, the learner can:

- Explain **pandas data structures and transformations** in the context of the course.
- Apply **Missing data, types, and quality checks** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **pandas data structures and transformations** — `lesson`
2. **Missing data, types, and quality checks** — `lesson`
3. **Checkpoint: data cleaning** — `test`
4. **Micro-lab: Clean a deliberately messy dataset and record each decision.** — `lab`

### Module 3 — Exploration & Visualization

#### Outcomes

By the end of this module, the learner can:

- Explain **Distributions and exploratory analysis** in the context of the course.
- Apply **Meaningful visualization and interpretation** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Distributions and exploratory analysis** — `lesson`
2. **Meaningful visualization and interpretation** — `lesson`
3. **Checkpoint: exploratory reasoning** — `test`
4. **Micro-lab: Create a visualization that answers a specific data question.** — `lab`

### Module 4 — Leakage, Splits & Reproducibility

#### Outcomes

By the end of this module, the learner can:

- Explain **Data leakage and train/validation/test splits** in the context of the course.
- Apply **Reproducible analysis workflows** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Data leakage and train/validation/test splits** — `lesson`
2. **Reproducible analysis workflows** — `lesson`
3. **Checkpoint: evaluation hygiene** — `test`
4. **Micro-lab: Re-run the analysis from a clean environment and compare outputs.** — `lab`

### Module 5 — Dataset Study

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Complete the Dataset Study with a data dictionary, analysis, visualizations, and quality report** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- NumPy
- pandas
- data cleaning
- data types
- missing data
- distributions
- visualization
- data leakage
- train/validation/test splits
- reproducibility

### Labs

- clean a messy dataset
- compare vectorized operations with loops
- detect data-quality problems
- build a reproducible analysis

### Substantial course lab

**Dataset Study**

Deliver:

- data dictionary
- reproducible notebook/script
- five meaningful visualizations
- quality report
- documented risks
