## AI3 — Deep Learning & Representation Learning

**Duration:** 6 weeks
**Expected workload:** 10–15 focused hours/week
**Prerequisite:** AI2

### Overview

Move from classical ML to neural networks through tensors, architectures, optimization, backpropagation, and representation learning. The course combines from-scratch reasoning with practical PyTorch development.

### Prerequisites

**AI2 — Machine Learning Foundations**

**Kind:** `course`

### Learning outcomes

By the end of the course, you will be able to:

- Explain the forward and backward passes of a neural network.
- Implement basic neural-network components and reason about tensors and gradients.
- Train and evaluate practical deep-learning models with controlled experiments.
- Diagnose common optimization and generalization failures.
- Use ablations and held-out evaluation to support architectural decisions.


### Resource map

**Required**

- **B36** Ch. 2, 5 and 7–12 (preliminaries; MLPs; CNNs; modern CNNs; RNNs; modern RNNs; attention; optimization) — added: ZtP AI4–AI5 name a PyTorch tutorial, a from-scratch NN resource and CS231n without chapters.
- **B16** Ch. 5 §5.6 and Ch. 7 — carried from ZtP AI2.
- **R45** PyTorch “Learn the Basics” · **R46** CS231n notes — carried from ZtP AI4–AI5.
- **R48** “A Recipe for Training Neural Networks”.

**Optional**

- **B36** Ch. 13 (Computational Performance).

### Modules

#### Module 1 — Tensors & Neural Networks

**Reading:** **B36** Ch. 2 §2.1 (Data Manipulation — tensors), §2.5 (Automatic Differentiation), Ch. 5 §§5.1–5.2 (Multilayer Perceptrons). **R45** Tensors; Build the Neural Network.


### Module outcomes

By the end of this module, the learner can:

- Explain **Tensors, parameters, and forward passes** in the context of the course.
- Apply **Activations and network structure** in a problem, implementation, experiment, or design decision.

1. **Tensors, parameters, and forward passes**
   - kind: `lesson`
2. **Activations and network structure**
   - kind: `lesson`
3. **Checkpoint: neural network basics**
   - kind: `test`

4. **Micro-lab: Trace a small network by hand and verify tensor shapes.**
   - kind: `lab`
#### Module 2 — Backpropagation & Optimization

**Reading:** **B36** Ch. 5 §5.3 (Forward Propagation, Backward Propagation, and Computational Graphs), §5.4 (Numerical Stability and Initialization), Ch. 8 §8.5 (Batch Normalization), Ch. 12 (Optimization Algorithms). **B16** Ch. 5 §5.6 (Backpropagation and Automatic Differentiation), Ch. 7 (Continuous Optimization). **R45** Automatic Differentiation with torch.autograd; Optimizing Model Parameters.


### Module outcomes

By the end of this module, the learner can:

- Explain **Backpropagation and gradients** in the context of the course.
- Apply **Optimization and normalization** in a problem, implementation, experiment, or design decision.

1. **Backpropagation and gradients**
   - kind: `lesson`
2. **Optimization and normalization**
   - kind: `lesson`
3. **Checkpoint: training mechanics**
   - kind: `test`

4. **Micro-lab: Compare an analytic gradient with a finite-difference estimate.**
   - kind: `lab`
#### Module 3 — Convolutional Representation

**Reading:** **B36** Ch. 7 (Convolutional Neural Networks), Ch. 8 §§8.1–8.6 (AlexNet through ResNet). **R46** the convolutional-network and architecture notes.


### Module outcomes

By the end of this module, the learner can:

- Explain **CNNs and spatial inductive bias** in the context of the course.
- Apply **Architecture choices for visual tasks** in a problem, implementation, experiment, or design decision.

1. **CNNs and spatial inductive bias**
   - kind: `lesson`
2. **Architecture choices for visual tasks**
   - kind: `lesson`
3. **Checkpoint: convolution**
   - kind: `test`

4. **Micro-lab: Change one convolutional design choice and measure the effect.**
   - kind: `lab`
#### Module 4 — Sequence Models & Attention

**Reading:** **B36** Ch. 9 (Recurrent Neural Networks), Ch. 10 (Modern Recurrent Neural Networks), Ch. 11 §§11.1–11.4 (Queries, Keys, and Values; Attention Pooling by Similarity; Attention Scoring Functions; the Bahdanau Attention Mechanism).


### Module outcomes

By the end of this module, the learner can:

- Explain **Sequence models and long dependencies** in the context of the course.
- Apply **Attention as a transition to transformers** in a problem, implementation, experiment, or design decision.

1. **Sequence models and long dependencies**
   - kind: `lesson`
2. **Attention as a transition to transformers**
   - kind: `lesson`
3. **Checkpoint: sequence reasoning**
   - kind: `test`

4. **Micro-lab: Trace attention inputs and outputs at a small sequence length.**
   - kind: `lab`
#### Module 5 — Small Deep Learning System

**Reading:** **B36** Ch. 6 (Builders' Guide). **R48** A Recipe for Training Neural Networks. **R45** Save and Load the Model. *Optional:* **B36** Ch. 13 (Computational Performance).


1. **Build, train, evaluate, and document the Small Deep Learning System**
   - kind: `lab`

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

---

