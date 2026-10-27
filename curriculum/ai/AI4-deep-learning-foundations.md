# AI4 — Deep Learning Foundations

**Track:** AI & ML · **Prerequisite:** AI3 · **Core** · **Time:** 6 weeks, 90 hours · **Project:** P7 neural baseline
**Status:** `draft` · [status labels](../../spec/status-labels.md)

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../templates/progress.md)

## Purpose

Understand neural networks from the inside: tensors, computation graphs, backpropagation, optimization, and regularization. You will implement a small network without autograd, then train controlled models with PyTorch and diagnose them from evidence.

## Outcomes

You can:

- explain forward propagation, loss, backpropagation, and parameter updates;
- implement a two-layer network with NumPy and gradient-check it;
- use PyTorch tensors, autograd, `nn.Module`, datasets, and optimizers correctly;
- explain initialization, activations, normalization, dropout, and weight decay;
- diagnose underfitting, overfitting, divergence, and data-pipeline bugs;
- design controlled ablations with fixed seeds and budgets;
- measure compute and memory cost;
- document an experiment so it can be reproduced.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Dive into Deep Learning](https://d2l.ai/) (D2L) | Ch. **1–5** | Preliminaries, linear networks, MLPs, computation |
| D2L | Ch. **11.1–11.6** | Optimization algorithms |
| [Deep Learning](https://www.deeplearningbook.org/) (Goodfellow et al.) | Ch. **6–8** | Feedforward networks, regularization, optimization |
| [PyTorch tutorials](https://pytorch.org/tutorials/) | Tensors, autograd, neural networks, training loop | Practical implementation |
| [CS231n notes](https://cs231n.github.io/) | Backprop, neural nets, training | Clear derivations |
| [Reproducibility checklist](https://www.cs.mcgill.ca/~jpineau/ReproducibilityChecklist.pdf) | Full | Experiment discipline |

## Modules

### 1. Tensors and computation

- scalars, vectors, matrices, batches;
- shapes, broadcasting, contiguous memory;
- CPU/GPU transfer costs;
- dtype and numerical precision;
- computation graphs;
- forward and reverse-mode differentiation.

### 2. Neural network basics

- linear layer and matrix shapes;
- activation functions: ReLU, sigmoid, tanh, GELU;
- loss functions: MSE, cross-entropy, binary cross-entropy;
- logits versus probabilities;
- parameter initialization;
- universal approximation intuition and limits.

### 3. Backpropagation

- chain rule through layers;
- local gradients and vector-Jacobian products;
- gradient accumulation;
- gradient checking;
- vanishing/exploding gradients;
- clipping;
- residual connections (intro).

### 4. Training

- epochs, batches, steps;
- SGD, momentum, Adam, AdamW;
- learning-rate schedules and warmup;
- weight decay and decoupling;
- batch normalization, layer normalization;
- dropout;
- early stopping;
- mixed precision (awareness);
- overfitting and regularization.

### 5. Data pipelines

- `Dataset`/`DataLoader`;
- shuffling and deterministic workers;
- augmentation;
- class imbalance;
- input normalization;
- data loading bottlenecks;
- train/validation/test isolation;
- leakage through normalization or duplicates.

### 6. Experiment discipline

- fixed seeds and deterministic settings;
- one-variable ablations;
- baseline and compute budget;
- logging config, metrics, and artifacts;
- checkpoint metadata;
- plotting learning curves honestly;
- reporting variance across seeds.

## Labs

### Lab 1 — Backprop from scratch

Implement a two-layer MLP in NumPy: forward pass, softmax/cross-entropy or MSE, analytic gradients, and a gradient check. Train on a small synthetic dataset. Show one shape bug and its diagnosis.

### Lab 2 — PyTorch training loop

Implement the same model in PyTorch without `tensorboard` magic. Write the loop explicitly: zero gradients, forward, loss, backward, step. Compare outputs with the NumPy implementation on a fixed initialization.

### Lab 3 — Controlled ablations

Train an MLP on a licensed tabular or image dataset. Hold the split, seed budget, and preprocessing fixed. Run three one-variable ablations: learning rate, width/depth, and regularization. Report validation metric, loss curves, and compute.

### Lab 4 — Diagnose failure modes

Reproduce four failures: too-high learning rate, no normalization, overfitting, and a label-misalignment bug. For each, show the symptom, the evidence, the fix, and the regression check.

### Lab 5 — Neural baseline for P7

Add a small MLP to P7 using the same split as AI3. Compare with the classical baseline under the same evaluation protocol. State whether the added complexity is justified.

## Exercises

1. Compute the output shape of a stack of linear layers.
2. Derive the gradient of cross-entropy with softmax logits.
3. Explain why zero-initializing all weights fails.
4. Compare ReLU and sigmoid saturation.
5. Explain batch norm's train/eval difference.
6. Diagnose a loss that decreases then explodes.
7. Explain why validation loss can rise while training loss falls.
8. Calculate parameter count for a small MLP.
9. Design a controlled learning-rate ablation.
10. Explain one source of nondeterminism on GPU.

## Project increment — P7 neural baseline

Add:

- a small neural baseline using the same split and metric;
- a controlled ablation table;
- learning curves with seeds/variance;
- a compute and memory note;
- a conclusion about whether the neural model is worth its cost.

**Brief:** [P7 — signal-score](../projects/project-ladder.md#p7--signal-score)

## Exit check

- [ ] implement and gradient-check a two-layer network without autograd;
- [ ] write an explicit PyTorch training loop and explain each step;
- [ ] diagnose underfit, overfit, divergence, and a data bug;
- [ ] show a controlled ablation with fixed budget;
- [ ] compare the neural and classical baselines honestly;
- [ ] reproduce the result from a clean checkout and fixed seed.

## Common failure modes

- Calling `.backward()` without zeroing gradients.
- Forgetting `model.eval()`/`torch.no_grad()` at evaluation.
- Normalizing before splitting and leaking statistics.
- Comparing models with different budgets or splits.
- Reporting the best seed as the result.
- Using accuracy on badly imbalanced data.
- Assuming a GPU makes a bad data pipeline faster.
- Hiding nondeterminism instead of documenting it.

## Evidence to commit

- `labs/ai/AI4/` with NumPy MLP, PyTorch loop, ablation table, failure diagnosis
- P7 neural baseline and comparison report
- `notes/ai/AI4/summary.md`
- `notes/ai/AI4/resources.md` with hardware, versions, seeds

## Optional depth

- D2L Ch. 6–7 (CNNs) as a preview of AI5.
- *Deep Learning* Ch. 9 (convolutional networks), 11 (practical methodology).
- *Neural Networks and Deep Learning* (Nielsen), free online.
- `torch.profiler` and `torch.utils.benchmark`.
- JAX/Flax as an alternative autograd model.
