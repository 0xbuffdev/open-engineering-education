> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

# SEF8 — Mathematics for Computing & AI

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** SEF2 (plus basic algebra)
**Duration:** 5 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

## Overview

This course teaches the mathematics that software engineering and machine learning rely on: logic, sets, combinatorics, vectors, matrices, probability, statistics, derivatives, gradients, and Big-O notation. Each topic is applied in code rather than studied in isolation.

## Course brief

The course introduction is the first lesson of the first module. It combines the overview above with these fields.

- **Introduction:** Mathematics supplies the exact language of computing and the foundation of machine learning. This course teaches the parts that later courses rely on and applies each one in code.
- **History:** Boole's algebra of logic dates from the 1840s, Cayley formalized matrices in 1858, Newton and Leibniz developed calculus in the seventeenth century, and Bayes' theorem was published in 1763.
- **Usage:** The learner implements each idea without libraries first, then verifies the result against a scientific library.
- **Applications:** Algorithm analysis, graphics, data science, cryptography, and machine learning.
- **Strengths:** Exact definitions allow exact reasoning and results that can be checked.
- **Limitations:** Models simplify reality, numerical computation introduces rounding error, and mathematical correctness does not guarantee that software behaves as intended.
- **Key concepts:** proposition; set; function; counting; vector; matrix; probability; distribution; derivative; gradient; Big-O

## Prerequisites

- [**SEF2 — Programming & Computational Thinking**](SEF2.md)
- Basic high-school algebra.

SEF3–SEF7 are not prerequisites; this course may be taken alongside them.

## Learning outcomes

By the end of the course, the learner will be able to:

- Use logical, set, and combinatorial reasoning in computational problems.
- Perform basic vector and matrix operations.
- Explain and calculate conditional probability and Bayes' rule.
- Work with basic descriptive statistics and probability distributions.
- Explain derivatives and gradients in the context of computation.
- Perform simple numerical experiments and verify mathematical results with code.
- Read and reason about mathematical notation commonly used in algorithms and machine learning.

## Modules

### Module 1 — Logic, Sets & Discrete Reasoning

#### Module brief

- **Introduction:** Discrete mathematics is the language of correctness and counting. This module covers logic, sets, functions, and counting.
- **Overview:** It covers propositional logic, quantifiers, sets, functions, counting rules, permutations, and combinations.
- **History:** George Boole formalized logic in the 1840s and 1850s, and Georg Cantor developed set theory in the 1870s.
- **Key concepts:** proposition; quantifier; set; function; counting rule; permutation; combination

#### Module outcomes

By the end of this module, the learner can:

- Reason with propositions, quantifiers, sets, and functions.
- Count arrangements and selections with the standard counting rules.

1. **Course introduction: Mathematics for Computing & AI** — what the subject is, where it came from, where it is used, and its strengths and limits
2. **Introduction: Logic, Sets & Discrete Reasoning** — what the topic is, where it is used, and its strengths and limits
3. **Propositional logic**
4. **Quantifiers**
5. **Sets**
6. **Functions**
7. **Counting rules**
8. **Permutations and combinations**
9. **Discrete reasoning**
   - kind: `test`
10. **Count and verify**

- kind: `lab`

### Module 2 — Vectors & Matrices

#### Module brief

- **Introduction:** Data, images, graphics, and models are arrays of numbers. Linear algebra gives rules for working with them.
- **Overview:** It covers vectors, norms and distance, dot products, angles, matrices, matrix multiplication, and linear systems.
- **History:** Arthur Cayley formalized matrices in 1858, and Gauss's elimination method for linear systems is older still.
- **Limitations:** Numerical error accumulates, and large matrices use a lot of memory and computation.
- **Key concepts:** vector; norm; dot product; angle; matrix; matrix multiplication; linear system

#### Module outcomes

By the end of this module, the learner can:

- Compute with vectors, norms, dot products, and angles, and explain their geometry.
- Multiply matrices and use them to solve linear systems.

1. **Introduction: Vectors & Matrices** — what the topic is, where it is used, and its strengths and limits
2. **Vectors**
3. **Norms and distance**
4. **Dot products**
5. **Angles and orthogonality**
6. **Matrices**
7. **Matrix multiplication**
8. **Linear systems**
9. **Linear algebra basics**
   - kind: `test`
10. **Matrices without NumPy**

- kind: `lab`

### Module 3 — Probability & Statistics

#### Module brief

- **Introduction:** Uncertainty is everywhere in software, from random inputs to measurement error. Probability gives rules for reasoning about it.
- **Overview:** It covers probability spaces, conditional probability, independence, Bayes' theorem, distributions, expected value, variance, and descriptive statistics.
- **History:** Bayes' theorem was published posthumously in 1763 from the work of Thomas Bayes, and Pierre-Simon Laplace developed it further.
- **Limitations:** Results depend on model assumptions, and conditional probabilities are often misread.
- **Key concepts:** probability; conditional probability; independence; Bayes' theorem; distribution; expected value; variance

#### Module outcomes

By the end of this module, the learner can:

- Compute probabilities, conditional probabilities, and apply Bayes' theorem.
- Describe data and random variables with distributions, expectation, variance, and summary statistics.

1. **Introduction: Probability & Statistics** — what the topic is, where it is used, and its strengths and limits
2. **Probability basics**
3. **Conditional probability**
4. **Independence**
5. **Bayes' theorem**
6. **Distributions**
7. **Expected value and variance**
8. **Descriptive statistics**
9. **Probabilistic reasoning**
   - kind: `test`
10. **Simulate an experiment**

- kind: `lab`

### Module 4 — Derivatives, Gradients & Complexity

#### Module brief

- **Introduction:** Change and growth are central to optimization and performance. This module covers derivatives, gradients, and the growth of functions.
- **Overview:** It covers derivatives, numerical derivatives, partial derivatives, gradients, the growth of functions, and algorithm complexity.
- **History:** Newton and Leibniz developed calculus in the late seventeenth century, and Augustin-Louis Cauchy proposed gradient descent in 1847.
- **Limitations:** A gradient gives only local information, and numerical differentiation is sensitive to step size.
- **Key concepts:** derivative; partial derivative; gradient; numerical approximation; growth rate; Big-O

#### Module outcomes

By the end of this module, the learner can:

- Compute derivatives and gradients and approximate them numerically.
- Compare the growth of functions and state an algorithm's complexity.

1. **Introduction: Derivatives, Gradients & Complexity** — what the topic is, where it is used, and its strengths and limits
2. **Derivatives**
3. **Numerical derivatives**
4. **Partial derivatives**
5. **Gradients**
6. **Growth of functions**
7. **Algorithm complexity**
8. **Calculus and complexity**
   - kind: `test`
9. **Check a derivative**
   - kind: `lab`

### Module 5 — Numerical Computing Notebook

#### Module brief

- **Introduction:** This lab integrates the course. The learner builds numerical functions from first principles and verifies them against a scientific library.
- **Overview:** It combines vector and matrix operations, probability simulation, and derivative checking in one notebook.
- **Applications:** Graphics, data science, and machine learning all run on these operations.
- **Key concepts integrated:** vectors; matrices; probability; simulation; derivatives; verification

1. **Numerical Computing Notebook**
   - kind: `lab`

## Topics

- Logic and sets
- Functions
- Combinatorics
- Vectors
- Matrices
- Dot products
- Probability
- Conditional probability
- Bayes' rule
- Descriptive statistics
- Derivatives
- Gradients
- Big-O notation

## Practical exercises

2. Implement vector operations.
3. Implement matrix multiplication.
4. Simulate probability distributions.
5. Estimate a derivative numerically.
6. Compare a numerical gradient with an analytic gradient.

## Course lab

**Numerical Computing Notebook**

Build a small collection of numerical functions without scientific libraries first, then verify them with NumPy.

## Exit check

The learner can calculate small matrix operations, conditional probabilities, and simple derivatives by hand and explain where these ideas appear in software and machine learning.
