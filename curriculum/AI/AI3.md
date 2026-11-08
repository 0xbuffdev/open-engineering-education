# AI3 — Deep Learning & Representation Learning

**Program:** AI — AI Engineering
**Type:** `course`
**Prerequisites:** AI2 *(legacy mapping; reconcile before activation)*
**Duration:** 6 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> **Unmigrated historical course — not OEE v0.2.0-conforming.** This educational outline was transferred from [the content repository](https://github.com/0xbuffdev/content/blob/0e14d4ff5808a4ea972206ed015a3e4737b33ad7/docs/curriculum/AI.md) before curriculum duplication is retired. The former `test` and `lab` labels are descriptions of historical activities, not automatic OEE completion requirements. Its outcome IDs, assessment IDs, criteria, and evidence still require v0.2.0 review. Reading and purchasing mappings remain in the content repository.

## Overview

Move from classical ML to neural networks through tensors, architectures, optimization, backpropagation, and representation learning. The course combines from-scratch reasoning with practical PyTorch development.

## Learning outcomes

- Explain the forward and backward passes of a neural network.
- Implement basic neural-network components and reason about tensors and gradients.
- Train and evaluate practical deep-learning models with controlled experiments.
- Diagnose common optimization and generalization failures.
- Use ablations and held-out evaluation to support architectural decisions.

## Modules

### Module 1 — Tensors & Neural Networks

#### Outcomes

By the end of this module, the learner can:

- Explain **Tensors, parameters, and forward passes** in the context of the course.
- Apply **Activations and network structure** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Tensors, parameters, and forward passes** — `lesson`
2. **Activations and network structure** — `lesson`
3. **Checkpoint: neural network basics** — `test`
4. **Micro-lab: Trace a small network by hand and verify tensor shapes.** — `lab`

### Module 2 — Backpropagation & Optimization

#### Outcomes

By the end of this module, the learner can:

- Explain **Backpropagation and gradients** in the context of the course.
- Apply **Optimization and normalization** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Backpropagation and gradients** — `lesson`
2. **Optimization and normalization** — `lesson`
3. **Checkpoint: training mechanics** — `test`
4. **Micro-lab: Compare an analytic gradient with a finite-difference estimate.** — `lab`

### Module 3 — Convolutional Representation

#### Outcomes

By the end of this module, the learner can:

- Explain **CNNs and spatial inductive bias** in the context of the course.
- Apply **Architecture choices for visual tasks** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **CNNs and spatial inductive bias** — `lesson`
2. **Architecture choices for visual tasks** — `lesson`
3. **Checkpoint: convolution** — `test`
4. **Micro-lab: Change one convolutional design choice and measure the effect.** — `lab`

### Module 4 — Sequence Models & Attention

#### Outcomes

By the end of this module, the learner can:

- Explain **Sequence models and long dependencies** in the context of the course.
- Apply **Attention as a transition to transformers** in a problem, implementation, experiment, or design decision.

#### Lessons

1. **Sequence models and long dependencies** — `lesson`
2. **Attention as a transition to transformers** — `lesson`
3. **Checkpoint: sequence reasoning** — `test`
4. **Micro-lab: Trace attention inputs and outputs at a small sequence length.** — `lab`

### Module 5 — Small Deep Learning System

#### Outcomes

*Outcome review pending against this course's required capabilities.*

#### Lessons

1. **Build, train, evaluate, and document the Small Deep Learning System** — `lab`

## Completion requirements

**Pending outcome-based migration:** Preserve and review the historical tasks and project requirements below. Before adopting this course against v0.2.0, assign stable outcome and summative assessment IDs, define published work/criteria/evidence, verify full outcome coverage and safety constraints, and distinguish formative practice from required work.

### Topics

- tensors
- neural networks
- forward pass
- backpropagation
- optimization
- activations
- normalization
- CNNs
- sequence models
- attention as a transition toward transformers

### Labs

- implement a tiny neural network without autograd
- derive gradients
- training-failure diagnosis
- CNN experiment
- sequence-model experiment

### Substantial course lab

**Small Deep Learning System**

Use PyTorch to build, train, evaluate, and document a model with controlled experiments.
