# AI5 — Vision & Sequence Architectures

**Track:** AI & ML · **Prerequisite:** AI4 · **Core** · **Time:** 5 weeks, 75 hours · **Project:** P8 architecture study

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Learn the architectural ideas behind modern vision and sequence models: locality, weight sharing, recurrence, attention, and inductive bias. You will train small models, inspect their behaviour, and compare architectures under a fair budget.

## Outcomes

You can:

- explain convolution, pooling, stride, padding, and receptive fields;
- calculate output shapes and parameter counts for CNNs;
- explain residual connections, batch/layer normalization, and modern CNN blocks;
- explain RNN/LSTM/GRU recurrence, truncation, and vanishing gradients;
- explain attention as content-based retrieval and its quadratic cost;
- train a small CNN and a small sequence model;
- compare architectures with the same data, split, and compute budget;
- analyze errors by class, sequence length, and subgroup;
- state when an architecture is unjustified for the data size.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| D2L | Ch. **6–9** | CNNs, modern CNNs, RNNs, modern RNNs |
| D2L | Ch. **10.1–10.4** | Attention basics and scoring functions |
| [CS231n notes](https://cs231n.github.io/) | CNNs, training, RNNs | Clear explanations and shape practice |
| [Deep Learning](https://www.deeplearningbook.org/) | Ch. **9, 10** | Convolution and sequence modelling |
| [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Full | Intuition for attention (preview of AI6) |
| [Sequence Modeling with CTC](https://distill.pub/2017/ctc/) | Full | Alignment for variable-length sequences |

## Modules

### 1. Convolutional networks

- convolution as local weighted sum;
- channels, filters, kernels;
- stride, padding, dilation;
- pooling and global pooling;
- receptive field;
- parameter sharing and translation equivariance;
- output-shape arithmetic;
- residual connections;
- batch normalization and its pitfalls;
- modern blocks: bottleneck, depthwise separable, squeeze-and-excitation (awareness).

### 2. Vision training and evaluation

- image preprocessing and augmentation;
- class imbalance and long tails;
- top-1/top-k accuracy;
- confusion matrix and per-class error;
- shortcut learning;
- distribution shift;
- compute budgets;
- transfer learning (intro).

### 3. Sequence models

- sequence representation and padding;
- RNN recurrence and backpropagation through time;
- vanishing/exploding gradients;
- LSTM and GRU gates;
- bidirectional models;
- teacher forcing;
- sequence classification and generation;
- CTC and alignment (intro);
- truncated BPTT and state management.

### 4. Attention

- query/key/value;
- scaled dot-product attention;
- self-attention and cross-attention;
- causal masking;
- multi-head attention;
- positional information;
- quadratic time and memory;
- attention visualization limits.

### 5. Comparative evaluation

- same split, preprocessing, and budget;
- parameter-matched comparisons;
- compute-matched comparisons;
- variance across seeds;
- error analysis by length/class;
- ablation design;
- reporting negative results.

## Labs

### Lab 1 — CNN shape and parameter calculator

Write a small calculator for convolution/pooling output shapes and parameter counts. Verify it against PyTorch for five architectures. Explain one off-by-one error.

### Lab 2 — Small CNN study

Train a CNN on a licensed small image dataset. Establish a trivial baseline and a small MLP baseline. Ablate one factor (depth, kernel size, augmentation, or normalization). Report accuracy, per-class errors, compute, and limitations.

### Lab 3 — Recurrent sequence model

Train an RNN/LSTM/GRU on a benign licensed sequence task (e.g., synthetic sequence classification or character-level text). Show padding/masking correctness and one long-range dependency failure. Compare a bidirectional and causal setup where appropriate.

### Lab 4 — Attention inspection

Implement scaled dot-product attention and a causal mask in NumPy/PyTorch. Show tensor shapes, mask values, and a case where attention weights do not explain the output. Do not treat attention maps as a complete explanation.

### Lab 5 — Architecture comparison

Compare the CNN and sequence model only if the task permits; otherwise compare two CNN variants and two sequence variants. Use the same split, training budget, and seeds. State which differences are within noise.

## Exercises

1. Calculate the receptive field of a three-layer CNN.
2. Compute output shape with stride and padding.
3. Explain why 1×1 convolutions are useful.
4. Explain the vanishing-gradient problem in an RNN.
5. Draw LSTM gates and their roles.
6. Compute attention scores for a 3-token example by hand.
7. Explain causal masking and where it is required.
8. Compare parameter counts of an RNN and a small Transformer.
9. Identify a shortcut in an image classifier.
10. Design a length-stratified error analysis.

## Project increment — P8 architecture study

Add to P8 `tinygpt`:

- a documented tokenizer/vocabulary;
- a small baseline architecture;
- one architecture ablation with matched budget;
- error analysis by sequence length;
- a compute/memory note and negative results.

**Brief:** [P8 — tinygpt](../projects/project-ladder.md#p8--tinygpt)

## Exit check

- [ ] calculate CNN shapes and parameter counts without a library;
- [ ] train a CNN and diagnose one failure from evidence;
- [ ] explain recurrence, gates, and vanishing gradients;
- [ ] hand-compute a tiny attention operation;
- [ ] show a fair architecture comparison with variance;
- [ ] state which architectural complexity is not justified by the data.

## Common failure modes

- Comparing models with different parameter or compute budgets.
- Ignoring padding/mask bugs in sequence models.
- Using attention weights as proof of causal reasoning.
- Reporting one seed.
- Augmenting the validation/test set.
- Training a large model on a tiny dataset and calling it deep learning.
- Ignoring class/length imbalance in error analysis.

## Evidence to commit

- `labs/ai/AI5/` with shape calculator, CNN study, RNN study, attention notebook, comparison report
- P8 architecture study
- `notes/ai/AI5/summary.md`

## Optional depth

- D2L Ch. 14–15 (pretraining and applications).
- *Deep Learning* Ch. 12 (applications).
- CS231n assignments (selected).
- *Speech and Language Processing* (Jurafsky & Martin), sequence labelling chapters.
- Vision Transformer and ConvNeXt papers.
