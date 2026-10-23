# AI2 — Optimization & Probabilistic ML

**Track:** AI & ML · **Prerequisite:** F4 · **Core** · **Time:** 4 weeks, 60 hours · **Project:** P7 math checks

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Build the mathematical intuition that lets you debug models instead of guessing. You will derive gradients, implement optimization loops, reason about probability and uncertainty, and connect linear algebra to PCA and least squares.

## Outcomes

You can:

- compute gradients by hand and check them numerically;
- explain convexity, learning rate, momentum, and regularization;
- derive and implement batch/stochastic gradient descent;
- use probability distributions, conditional probability, and Bayes' rule correctly;
- compute maximum likelihood for common models;
- explain bias, variance, covariance, and correlation;
- derive PCA and interpret explained variance;
- state assumptions and failure modes of each method.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [Mathematics for Machine Learning](https://mml-book.github.io/) (MML) | Ch. **5–7** | Vector calculus, probability, continuous optimization |
| MML | Ch. **2–4, 10** (selected) | Linear algebra, analytic geometry, matrix decompositions, PCA |
| [Deep Learning](https://www.deeplearningbook.org/) (Goodfellow et al.) | Ch. **4, 5, 7** | Numerical computation, ML basics, regularization |
| [Probability for Data Science](https://probability4datascience.com/) or equivalent | Selected chapters | Conditional probability and distributions |
| [scipy.stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html) | Distributions, tests | Numerical checks |

## Modules

### 1. Linear algebra for models

- vectors, matrices, norms, inner products;
- rank, null space, projections;
- eigenvalues/eigenvectors and spectral decomposition;
- singular value decomposition;
- positive definiteness and quadratic forms;
- condition number and numerical stability.

### 2. Calculus and gradients

- partial derivatives and the chain rule;
- Jacobian and Hessian;
- gradient, directional derivative, Taylor expansion;
- convexity and local minima;
- Lagrange multipliers (intro);
- automatic differentiation versus symbolic versus finite differences.

### 3. Optimization

- empirical risk and loss functions;
- batch, stochastic, and mini-batch gradient descent;
- learning rate, momentum, RMSProp, Adam;
- learning-rate schedules;
- regularization (L1/L2);
- early stopping;
- convergence diagnostics;
- saddle points and ill-conditioning;
- constrained optimization (intro).

### 4. Probability

- sample spaces, events, conditional probability;
- independence and conditional independence;
- Bayes' rule and base rates;
- random variables, expectation, variance, covariance;
- Bernoulli, categorical, binomial, Poisson, Gaussian, exponential;
- joint, marginal, and conditional distributions;
- likelihood, log-likelihood, maximum likelihood;
- entropy, KL divergence, cross-entropy;
- sampling and Monte Carlo.

### 5. Statistics for ML

- estimators and bias/variance;
- standard error and confidence intervals;
- hypothesis tests and p-values (and misuse);
- correlation versus causation;
- maximum likelihood versus Bayesian thinking;
- calibration and proper scoring rules;
- uncertainty: aleatoric versus epistemic.

### 6. Dimensionality reduction

- covariance matrix and eigendecomposition;
- PCA derivation: variance maximization and reconstruction error;
- whitening;
- explained variance;
- when PCA is inappropriate;
- t-SNE/UMAP as visualization-only tools.

## Labs

### Lab 1 — Gradient derivation and check

Derive the gradient of least-squares linear regression. Implement the loss, analytic gradient, and finite-difference check. Report error versus epsilon and explain the trade-off.

### Lab 2 — Optimizer comparison

Implement batch and stochastic gradient descent on a small regression problem. Compare learning rates and one adaptive optimizer. Plot loss versus epochs and versus wall-clock; state what the plot does and does not show.

### Lab 3 — PCA from scratch

Implement PCA with NumPy using centering, covariance, and eigendecomposition. Compare with scikit-learn. Show explained variance, reconstruction error, and one misleading interpretation caused by scaling.

### Lab 4 — Probability simulation

Simulate a disease-testing base-rate problem, a Poisson process, and a bootstrap confidence interval. Compare simulation with the analytic answer and explain any discrepancy.

### Lab 5 — Maximum likelihood

Derive and implement maximum-likelihood estimation for a Bernoulli and a Gaussian. Show the likelihood surface and one case where the MLE is unstable or undefined.

## Exercises

1. Compute the gradient of a two-layer linear model by hand.
2. Check a gradient with central differences.
3. Explain why feature scaling changes gradient descent.
4. Derive the normal equation and state when it is a bad choice.
5. Apply Bayes' rule to a base-rate problem.
6. Compute expectation and variance for a sum of random variables.
7. Derive the MLE for a Bernoulli parameter.
8. Explain the bias-variance trade-off with a concrete example.
9. Show why correlation does not imply causation.
10. Derive the first principal component.

## Project increment — P7 math checks

Add to P7:

- a notebook/module of derivations with numerical checks;
- a written explanation of the loss and metric;
- baseline and optimizer diagnostics;
- calibration or uncertainty analysis;
- an assumptions/limitations section.

This is evidence of understanding, not a separate product.

**Brief:** [P7 — signal-score](../projects/project-ladder.md#p7--signal-score)

## Exit check

- [ ] derive a model's gradient and validate it numerically;
- [ ] explain a learning-rate failure from a loss curve;
- [ ] implement PCA and interpret it correctly;
- [ ] solve a conditional-probability problem without a calculator shortcut;
- [ ] derive an MLE and state its assumptions;
- [ ] explain one place where a statistical claim would be invalid.

## Common failure modes

- Using an optimizer without checking the gradient.
- Reporting training loss as evidence of generalization.
- Applying PCA without centering or scaling.
- Interpreting a t-SNE plot as a distance-preserving map.
- Confusing p-value with probability that the hypothesis is true.
- Ignoring numerical precision and ill-conditioning.
- Treating correlated features as causal.

## Evidence to commit

- `labs/ai/AI2/` with gradient check, optimizer comparison, PCA, probability simulations, MLE
- P7 math notebook and diagnostics
- `notes/ai/AI2/summary.md`

## Optional depth

- MML Ch. 8–12 (linear regression, density estimation, SVM, Gaussian processes).
- *Convex Optimization* (Boyd & Vandenberghe), Ch. 1–5.
- *All of Statistics* (Wasserman), selected chapters.
- *Probabilistic Machine Learning: An Introduction* (Murphy), Ch. 2–4.
- Automatic differentiation with JAX or PyTorch.
