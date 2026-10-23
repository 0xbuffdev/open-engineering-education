# F4 — Mathematics I: Discrete Math, Linear Algebra, Calculus & Probability

**Track:** Foundations · **Prerequisite:** F1 · **Core** · **Time:** 10 weeks, 150 hours · **Project:** math notebook

> **Navigate:** [Track](../README.md) · [Book maps](../books/README.md) · [Resources](../resources.md) · [Projects](../projects/README.md) · [Glossary](../appendices/glossary.md) · [Progress](../../progress.md)

## Purpose

Build the mathematical fluency that systems, ML, cryptography, and performance work assume. The old F4 crammed linear algebra, calculus, probability, and discrete math into four weeks. This version gives each area enough time to be usable, not just recognizable.

## Outcomes

You can:

- read and write logical statements, proofs, sets, relations, and functions;
- count with permutations/combinations and reason about graphs and modular arithmetic;
- perform matrix operations, solve linear systems, and interpret rank, eigenvalues, and SVD;
- differentiate scalar/vector/matrix expressions and explain a gradient;
- compute conditional probabilities, use Bayes' rule, and work with common distributions;
- estimate, test a hypothesis, and explain a confidence interval;
- implement numerical checks and compare them with hand calculations.

## Required reading

| Source | Sections | Why |
| --- | --- | --- |
| [*Mathematics for Machine Learning*](https://mml-book.github.io/) (MML) | Ch. **2–3** | Linear algebra, analytic geometry |
| MML | Ch. **5–6** | Vector calculus, probability, distributions |
| MML | Ch. **7** | Continuous optimization |
| MML | Ch. **10** | PCA (optional until AI2) |
| [MIT 6.042](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/) or *Discrete Mathematics and Its Applications* (Rosen) | Logic, proofs, sets, combinatorics, graphs, number theory | Discrete math spine |
| [3Blue1Brown](https://www.3blue1brown.com/topics/linear-algebra) | Essence of linear algebra | Intuition before formalism |

**Rule:** do the hand calculations before the code. A notebook that only calls NumPy is not a math lab.

## Modules

### 1. Logic, proofs, sets, relations

- propositions, truth tables, implication, converse, contrapositive;
- quantifiers and negation;
- proof methods: direct, contrapositive, contradiction, induction, strong induction;
- sets, subsets, power sets, Cartesian products;
- relations: reflexive, symmetric, transitive, equivalence, partial order;
- functions: injective, surjective, bijective, composition, inverse;
- cardinality and countability (intro).

### 2. Combinatorics and number theory

- sum/product rules, permutations, combinations, repetitions;
- pigeonhole principle, inclusion–exclusion;
- binomial coefficients and identities;
- recurrence relations (intro);
- divisibility, primes, gcd, Euclid's algorithm;
- modular arithmetic, inverses, Fermat's little theorem (intro);
- graphs: degree, paths, connectivity, trees, bipartite, planar (intro);
- hashing and modular arithmetic connections.

### 3. Linear algebra

- vectors, norms, dot product, angle, orthogonality;
- matrices, operations, transpose, inverse;
- systems of linear equations, Gaussian elimination, row echelon;
- rank, null space, column space, determinant;
- eigenvalues/eigenvectors, diagonalization;
- symmetric matrices, positive definiteness;
- orthogonality, projections, Gram–Schmidt;
- SVD and low-rank approximation;
- PCA as an application.

### 4. Calculus and optimization

- limits, continuity, derivative, rules;
- chain rule, partial derivatives, gradient, Jacobian, Hessian;
- Taylor expansion, linearization;
- integrals: antiderivative, definite integral, expectation connection;
- convexity, local/global minima, constraints;
- Lagrange multipliers (intro);
- gradient descent and step size;
- numerical differentiation and gradient checking.

### 5. Probability and statistics

- sample space, events, axioms;
- conditional probability, independence, Bayes' rule;
- random variables, PMF/PDF/CDF;
- expectation, variance, covariance, correlation;
- Bernoulli, binomial, geometric, Poisson, uniform, normal, exponential;
- joint/marginal/conditional distributions;
- law of large numbers, central limit theorem;
- estimation, bias/variance, maximum likelihood;
- confidence intervals, hypothesis testing, p-values, power;
- simulation and Monte Carlo.

### 6. Information theory (intro)

- entropy, cross-entropy, KL divergence;
- mutual information;
- why cross-entropy is used for classification;
- bits vs nats.

## Labs

### Lab 1 — Proof and combinatorics notebook

Write ten proofs and ten counting problems by hand. Include one induction proof, one contradiction, one pigeonhole, and one modular-arithmetic proof. Check two counting results with brute-force enumeration.

### Lab 2 — Linear algebra from scratch

Implement vector addition, dot product, matrix multiplication, transpose, determinant, and Gaussian elimination without NumPy. Verify against NumPy on random small inputs. Implement PCA on a small dataset and show explained variance and reconstruction error.

### Lab 3 — Numerical gradient check

Implement a small scalar/vector loss, derive its gradient, and compare it with finite differences across several step sizes. Plot or tabulate the error. Explain why the error is not monotonic.

### Lab 4 — Probability simulation

Simulate dice/coins/cards with a fixed seed. Compare empirical and expected probabilities at increasing sample sizes. Implement Bayes' rule from a contingency table and a Monte Carlo estimate. Include one case where intuition is wrong.

### Lab 5 — Statistics and hypothesis test

Take a small dataset, compute mean/median/variance, bootstrap a confidence interval, and run a simple hypothesis test. Explain what the test does and does not prove.

## Exercises

1. Translate ten English statements into logic and negate them.
2. Build truth tables for five compound statements.
3. Prove five set identities.
4. Solve ten counting problems with stated assumptions.
5. Compute gcd and modular inverses by hand.
6. Hand-multiply three matrix pairs and solve two linear systems.
7. Compute eigenvalues/eigenvectors for 2×2 matrices.
8. Differentiate ten functions and derive three gradients.
9. Compute ten conditional probabilities and two Bayes updates.
10. Compute mean/median/variance for a tiny sample and interpret a confidence interval.
11. Read summation, product, gradient, and Big-O notation from one formula per symbol.
12. Explain one case where correlation does not imply causation.

## Project increment — Math notebook

Create `labs/foundations/F4/math-notebook/` with:

- a handwritten or LaTeX proof section;
- a NumPy-free linear algebra module with tests;
- a gradient-check notebook;
- a probability simulation;
- a short "formula sheet" you can use in AI2/AI3.

## Exit check

- [ ] multiply small matrices by hand and explain each operation;
- [ ] solve a linear system and identify a singular case;
- [ ] compute eigenvalues/eigenvectors for a 2×2 matrix;
- [ ] derive a gradient and check it numerically;
- [ ] calculate a conditional probability and apply Bayes' rule;
- [ ] explain a confidence interval and a p-value correctly;
- [ ] read summation, gradient, and Big-O notation without hesitation.

## Common failure modes

- Watching math videos without doing problems.
- Using NumPy before understanding the operation.
- Treating a p-value as the probability the hypothesis is true.
- Confusing variance with standard deviation.
- Memorizing derivative rules without the chain rule.
- Skipping discrete math because "ML is continuous." Graph, crypto, and complexity work need it.

## Evidence to commit

- `labs/foundations/F4/math-notebook/`
- `exercises/foundations/F4/` with worked solutions
- `notes/foundations/F4/summary.md`
- a one-page formula sheet

## Optional depth

- *Linear Algebra Done Right* (Axler) for proof-heavy linear algebra.
- *Probability for Data Science* or *Introduction to Probability* (Blitzstein & Hwang).
- *Concrete Mathematics* for combinatorics.
- *Numerical Linear Algebra* (Trefethen & Bau) before AI2.
