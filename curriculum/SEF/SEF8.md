# SEF8 — Mathematics for Computing & AI

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md) (plus basic algebra)
**Duration:** 10 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course teaches the mathematics that software engineering and machine learning rely on: logic, sets, combinatorics, vectors, matrices, probability, statistics, derivatives, gradients, and Big-O notation. Each topic is applied in code rather than studied in isolation.

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
- Apply proof, discrete mathematics, linear algebra, probability, statistics and numerical methods to computing problems, with assumptions and limits stated.

## Modules

### Module 1 — Logic, Sets & Discrete Reasoning

#### Outcomes

- Reason with propositions, quantifiers, sets, and functions.
- Count arrangements and selections with the standard counting rules.

- Use a short proof or counterexample to verify a combinatorial claim.

#### Lessons

1. **Course introduction: Mathematics for Computing & AI** — `lesson`

   Mathematics supplies the exact language of computing and the foundation of machine learning. This course teaches the parts that later courses rely on and applies each one in code.
2. **Propositional logic** — `lesson`
3. **Quantifiers** — `lesson`
4. **Sets** — `lesson`
5. **Functions** — `lesson`
6. **Counting rules** — `lesson`
7. **Permutations and combinations** — `lesson`
8. **Proof by contradiction and induction** — `lesson`
9. **Relations, equivalence and orderings** — `lesson`
10. **Graphs as mathematical objects** — `lesson`
11. **Discrete reasoning** — `test`
12. **Count and verify** — `lab`

### Module 2 — Vectors & Matrices

#### Outcomes

- Compute with vectors, norms, dot products, and angles, and explain their geometry.
- Multiply matrices and use them to solve linear systems.

- Classify a matrix computation and detect a singular system rather than silently returning a result.

#### Lessons

1. **Vectors** — `lesson`
2. **Norms and distance** — `lesson`
3. **Dot products** — `lesson`
4. **Angles and orthogonality** — `lesson`
5. **Matrices** — `lesson`
6. **Matrix multiplication** — `lesson`
7. **Linear systems** — `lesson`
8. **Linear independence, span and basis** — `lesson`
9. **Matrix transformations and composition** — `lesson`
10. **Solutions of linear systems and singular cases** — `lesson`
11. **Linear algebra basics** — `test`
12. **Matrices without NumPy** — `lab`

### Module 3 — Probability & Statistics

#### Outcomes

- Compute probabilities, conditional probabilities, and apply Bayes' theorem.
- Describe data and random variables with distributions, expectation, variance, and summary statistics.

- Verify a probability claim analytically and by simulation, describing uncertainty.

#### Lessons

1. **Probability basics** — `lesson`
2. **Conditional probability** — `lesson`
3. **Independence** — `lesson`
4. **Bayes' theorem** — `lesson`
5. **Distributions** — `lesson`
6. **Expected value and variance** — `lesson`
7. **Descriptive statistics** — `lesson`
8. **Random variables and conditional distributions** — `lesson`
9. **Sampling variability and bias** — `lesson`
10. **Confidence intervals and uncertainty statements** — `lesson`
11. **Probabilistic reasoning** — `test`
12. **Simulate an experiment** — `lab`

### Module 4 — Derivatives, Gradients & Complexity

#### Outcomes

- Compute derivatives and gradients and approximate them numerically.
- Compare the growth of functions and state an algorithm's complexity.

- Compare finite-difference gradients at different step sizes and explain error.

#### Lessons

1. **Derivatives** — `lesson`
2. **Numerical derivatives** — `lesson`
3. **Partial derivatives** — `lesson`
4. **Gradients** — `lesson`
5. **Growth of functions** — `lesson`
6. **Algorithm complexity** — `lesson`
7. **Chain rule and gradient interpretation** — `lesson`
8. **Finite-difference approximation error** — `lesson`
9. **Growth rates and numerical stability** — `lesson`
10. **Calculus and complexity** — `test`
11. **Check a derivative** — `lab`

### Module 5 — Proofs, Relations & Graph Mathematics

#### Outcomes

- Construct elementary proofs and identify false claims with counterexamples.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Direct proof and induction** — `lesson`
2. **Contradiction and counterexample** — `lesson`
3. **Equivalence relations and partitions** — `lesson`
4. **Graph degree, paths and connectivity** — `lesson`
5. **Recurrences and combinatorial reasoning** — `lesson`
6. **Proofs, Relations & Graph Mathematics reasoning and diagnosis** — `test`
7. **Verify graph and recurrence identities** — `lab`

### Module 6 — Linear Algebra for Computation

#### Outcomes

- Interpret ranks, transformations and degeneracy in small numerical problems.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Vector spaces and linear independence** — `lesson`
2. **Basis, rank and null space** — `lesson`
3. **Matrix transformations and compositions** — `lesson`
4. **Eigenvectors and eigenvalues as introductory concepts** — `lesson`
5. **Numerical linear-system accuracy** — `lesson`
6. **Linear Algebra for Computation reasoning and diagnosis** — `test`
7. **Check a linear transform** — `lab`

### Module 7 — Statistical Inference & Experimental Reasoning

#### Outcomes

- Interpret uncertainty and resist overclaiming from small samples.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Sampling, bias and variability** — `lesson`
2. **Estimators and standard errors** — `lesson`
3. **Confidence intervals and interpretation** — `lesson`
4. **Hypothesis tests and p-values** — `lesson`
5. **Correlation versus causation** — `lesson`
6. **Basic experimental design and reproducibility** — `lesson`
7. **Statistical Inference & Experimental Reasoning reasoning and diagnosis** — `test`
8. **Analyze a simulated experiment** — `lab`

### Module 8 — Numerical Methods & Optimization Foundations

#### Outcomes

- Analyze basic numerical error and execute an iterative optimization with explicit stopping criteria.
- Demonstrate reasoning with both ordinary and deliberately failing inputs.

#### Lessons

1. **Floating-point error and representation** — `lesson`
2. **Truncation versus rounding error** — `lesson`
3. **Numerical derivatives and step-size trade-offs** — `lesson`
4. **Gradient descent and learning-rate behavior** — `lesson`
5. **Stopping criteria and convergence limitations** — `lesson`
6. **Numerical Methods & Optimization Foundations reasoning and diagnosis** — `test`
7. **Study gradient descent on a simple function** — `lab`

### Module 9 — Numerical Computing Notebook

#### Outcomes

- Complete and explain the **Numerical Computing Notebook** integration lab, demonstrating the relevant course outcomes and retained evidence.

#### Lessons

1. **Numerical Computing Notebook** — `lab`

   **Final integration lab — required work**

   **Numerical Computing Notebook**

   Build a small collection of numerical functions without scientific libraries first, then verify them with NumPy.

## Completion requirements

- Complete the required course exercises, checkpoints and evaluated labs below.
- Complete the final integrated `lab` in the last module and meet its observable exit criteria.
- Retain reproducible artifacts, verification results, design explanations, and a technical retrospective as required by the [OEE Evidence Rules](../../spec/evidence-rules.md).

Complete these required exercises:

**Practical practice:**

- Implement vector operations.
- Implement matrix multiplication.
- Simulate probability distributions.
- Estimate a derivative numerically.
- Compare a numerical gradient with an analytic gradient.

**Expanded assessment and lab criteria:**

- **Module 1 checkpoint:** Use a short proof or counterexample to verify a combinatorial claim.
- **Module 2 checkpoint:** Classify a matrix computation and detect a singular system rather than silently returning a result.
- **Module 3 checkpoint:** Verify a probability claim analytically and by simulation, describing uncertainty.
- **Module 4 checkpoint:** Compare finite-difference gradients at different step sizes and explain error.

- **Module 5 — Verify graph and recurrence identities:**
  - Objective: Construct elementary proofs and identify false claims with counterexamples.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Prove or disprove a graph or counting statement for small examples with a simple enumeration program.
  - Verification: State conditions precisely and compare code outputs with an independently reasoned result.
  - Evidence: Proof, counterexample, enumerator and assumptions.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 6 — Check a linear transform:**
  - Objective: Interpret ranks, transformations and degeneracy in small numerical problems.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Implement a small matrix transform and validate identity, composition and degenerate cases.
  - Verification: Compute expected results by hand and compare with code, including a singular input.
  - Evidence: Computations, code and error analysis.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 7 — Analyze a simulated experiment:**
  - Objective: Interpret uncertainty and resist overclaiming from small samples.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Simulate two populations, estimate uncertainty and compare means with a documented sampling plan.
  - Verification: Show coverage or uncertainty across repeated samples and explain what cannot be concluded.
  - Evidence: Scripts, plots or tables, assumptions and inference note.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 8 — Study gradient descent on a simple function:**
  - Objective: Analyze basic numerical error and execute an iterative optimization with explicit stopping criteria.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Implement numerical gradient checks and optimize a convex quadratic with multiple step sizes.
  - Verification: Report convergence, divergence conditions and analytic gradient comparison.
  - Evidence: Notebook, numerical traces, tests and limitations.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.

**Final integration lab extension:**

- The final integrated lab must demonstrate the existing course outcomes and the additional outcomes in this expanded mathematics pathway.
- Provide explicit negative tests, clean-checkout reproduction, explanation of assumptions, and a technical retrospective.

**Exit demonstration:**

The learner can calculate small matrix operations, conditional probabilities, and simple derivatives by hand and explain where these ideas appear in software and machine learning.
