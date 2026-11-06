# SEF8 — Mathematics for Computing & AI

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 11–12 weeks
**Status:** `draft`
**Expected workload:** 10–15 focused hours/week

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

This course starts with mathematical literacy and pre-algebra, and then builds logic, sets, combinatorics, vectors, matrices, probability, statistics, derivatives, gradients and Big-O notation. Learners practice mathematical reasoning by hand and use Python to verify results.

- [**SEF2 — Programming & Computational Thinking**](SEF2.md)
- No prior algebra, calculus, probability or formal mathematics course is required.

SEF3–SEF7 are not prerequisites; this course may be taken alongside them. The opening mathematics bridge has an ungraded entry diagnostic and a mastery check. Learners needing more practice can extend its pace; those with prior knowledge may proceed after demonstrating the same required skills.

## Learning outcomes

By the end of the course, the learner will be able to:

- Use whole and signed numbers, fractions, decimals, percentages, rates and exponents correctly.
- Read mathematical notation and solve elementary equations, inequalities and input-output functions.
- Check mathematical calculations using estimates, substitution and simple Python programs.
- Use logical, set, and combinatorial reasoning in computational problems.
- Perform basic vector and matrix operations.
- Explain and calculate conditional probability and Bayes' rule.
- Work with basic descriptive statistics and probability distributions.
- Explain derivatives and gradients in the context of computation.
- Perform simple numerical experiments and verify mathematical results with code.
- Read and reason about mathematical notation commonly used in algorithms and machine learning.
- Apply proof, discrete mathematics, linear algebra, probability, statistics and numerical methods to computing problems, with assumptions and limits stated.

## Modules

### Module 1 — Mathematical Literacy & Pre-Algebra

#### Outcomes

- Represent and compare whole, signed, fractional, decimal and percentage quantities.
- Perform basic operations, interpret rates and powers, and check answers through estimates and units.
- Read symbols and expressions, solve elementary equations, and interpret inequalities, function tables and coordinates.
- Explain reasoning by hand and verify simple mathematical results using Python.

#### Lessons

1. **Course introduction: Mathematics for Computing & AI** — `lesson`

   Mathematics describes quantities, patterns, relationships and change. This course begins with arithmetic and simple algebraic reasoning instead of assuming prior mathematics study. Learners progress from number sense to logic, linear algebra, probability, statistics and numerical computing, using Python to check their work.
2. **Ungraded starting-point numeracy check** — `test`
3. **What mathematics describes: quantities, patterns and relationships** — `lesson`
4. **Counting, whole numbers, place value and number lines** — `lesson`
5. **Addition, subtraction, multiplication and division** — `lesson`
6. **Order of operations, grouping and estimation** — `lesson`
7. **Negative numbers and absolute value** — `lesson`
8. **Fractions and their operations** — `lesson`
9. **Decimals, percentages and conversions** — `lesson`
10. **Ratios, proportions, rates and measurement units** — `lesson`
11. **Powers, roots and scientific notation** — `lesson`
12. **Symbols, variables and arithmetic expressions** — `lesson`
13. **Solving simple linear equations and checking answers** — `lesson`
14. **Inequalities and coordinate pairs** — `lesson`
15. **Functions, input-output tables and basic graphs** — `lesson`
16. **Pre-algebra readiness checkpoint** — `test`
17. **Mathematics-to-Python workbook** — `lab`

### Module 2 — Logic, Sets & Discrete Reasoning

#### Outcomes

- Reason with propositions, quantifiers, sets, and functions.
- Count arrangements and selections with the standard counting rules.

- Use a short proof or counterexample to verify a combinatorial claim.

#### Lessons

1. **Propositional logic** — `lesson`
2. **Quantifiers** — `lesson`
3. **Sets** — `lesson`
4. **Functions** — `lesson`
5. **Counting rules** — `lesson`
6. **Permutations and combinations** — `lesson`
7. **Proof by contradiction and induction** — `lesson`
8. **Relations, equivalence and orderings** — `lesson`
9. **Graphs as mathematical objects** — `lesson`
10. **Discrete reasoning** — `test`
11. **Count and verify** — `lab`

### Module 3 — Vectors & Matrices

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

### Module 4 — Probability & Statistics

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

### Module 5 — Derivatives, Gradients & Complexity

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

### Module 6 — Proofs, Relations & Graph Mathematics

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

### Module 7 — Linear Algebra for Computation

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

### Module 8 — Statistical Inference & Experimental Reasoning

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

### Module 9 — Numerical Methods & Optimization Foundations

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

### Module 10 — Numerical Computing Notebook

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

- Calculate and verify signed numbers, fractions, percentages, elementary equations and function tables by hand and in Python.
- Implement vector operations.
- Implement matrix multiplication.
- Simulate probability distributions.
- Estimate a derivative numerically.
- Compare a numerical gradient with an analytic gradient.

**Module 1 — Mathematical Literacy & Pre-Algebra: assessment** — Required details

**Ungraded starting-point check:** Attempt comparable examples involving arithmetic, fractions, signed values, equations and a function table before instruction. This diagnostic identifies needed practice and is never a gatekeeping test; no entry score or prior algebra course is required.

**Required pre-algebra readiness questions (or equivalent previously unseen variations):**

- **Q1 — place value and comparison:** Write 307 in hundreds, tens and ones; compare 0.7 and 0.65.
  - Expected reasoning: 3 hundreds, 0 tens, 7 ones; 0.70 > 0.65.
- **Q2 — arithmetic order:** Evaluate `8 + 3 × 4` and `(8 + 3) × 4`.
  - Expected reasoning: 20 and 44, respectively; multiplication has precedence unless grouped.
- **Q3 — signed numbers:** Evaluate `-9 + 14` on a number line.
  - Expected reasoning: 5; start at -9 and move 14 positions to the right.
- **Q4 — fractions:** Evaluate `1/2 + 1/4` and justify the denominator.
  - Expected reasoning: 3/4; rewrite one-half as two-quarters and add the numerators.
- **Q5 — percentages:** Convert 0.35 to a percentage; find 20% of 150.
  - Expected reasoning: 35% and 30, respectively.
- **Q6 — ratios and rates:** A service processes 12 jobs in 3 minutes at a constant rate. How many jobs per minute and in 5 minutes?
  - Expected reasoning: 4 jobs/minute, then 20 jobs, conditional on the constant-rate assumption.
- **Q7 — powers and notation:** Expand `3.2 × 10³` and calculate `2³`.
  - Expected reasoning: 3,200 and 8.
- **Q8 — algebra and substitution:** Solve `3x + 4 = 19` and verify by substitution.
  - Expected reasoning: x = 5; 3×5+4 = 19.
- **Q9 — functions and coordinates:** For `f(x) = 2x + 1`, calculate f(3) and write its graph point.
  - Expected reasoning: f(3) = 7 and coordinate (3,7).
- **Q10 — inequalities and units:** Solve `x + 2 < 5`; express 6 metres in 3 seconds in metres per second.
  - Expected reasoning: x < 3 and 2 m/s. Explain the inequality and division of units.

**Checkpoint acceptance:** Demonstrate every essential skill: number sense and order of operations, signed arithmetic, fractions and percentages, ratios and units, powers, equations and coordinate/function interpretation. If a category is incorrect, teach it again and reassess with new numbers and a reasoned explanation. No penalty or fixed attempt limit applies. A correct guess without an explanation does not demonstrate mastery.

**Module 1 — Mathematics-to-Python workbook: required lab** — Required details

- **Objective:** Connect elementary mathematical reasoning to reproducible Python calculations and explain discrepancies.
- **Prerequisites:** Complete SEF2 and the bridge lessons, or demonstrate equivalent mastery in the readiness checkpoint.
- **Environment:** Local Python 3.11+ standard library, editor or REPL, and paper/digital notes. Record actual runtime version. No packages, payment or internet connection required.
- **Procedure:**
  1. Show handwritten or typed steps for a signed-number operation, a fraction addition, a percentage calculation and a simple linear equation.
  2. Verify the same examples with a short Python script. Use `fractions.Fraction` to represent exact rational numbers.
  3. Produce an input/output table for `f(x) = 2x + 1` at x = -2, -1, 0, 1 and 2; describe its coordinate points.
  4. Check normal and edge cases including division by zero, incorrect operator precedence and a fraction-denominator mistake.
  5. Reproduce one intentional incorrect calculation and explain the correction and which mathematical rule was applied.
- **Expected result:** Exact fractional results agree with the hand calculations; the function table is (-2,-3), (-1,-1), (0,1), (1,3), (2,5); invalid operations are handled or clearly explained.
- **Verification:** Run the documented Python script from a clean environment and compare its printed results with the independently computed expected values and manual work.
- **Evidence:** Calculations, Python source, commands, actual output, function table, wrong/corrected result, tool version and a brief reflection.
- **Failure analysis:** Distinguish a mathematical error from a precedence error or binary floating-point approximation.
- **Acceptance:** A reviewer can reproduce results and verify every required arithmetic/algebra capability; remediate any missing skill before Module 2.

**Expanded assessment and lab criteria:**

- **Module 2 checkpoint:** Use a short proof or counterexample to verify a combinatorial claim.
- **Module 3 checkpoint:** Classify a matrix computation and detect a singular system rather than silently returning a result.
- **Module 4 checkpoint:** Verify a probability claim analytically and by simulation, describing uncertainty.
- **Module 5 checkpoint:** Compare finite-difference gradients at different step sizes and explain error.

- **Module 6 — Verify graph and recurrence identities:**
  - Objective: Construct elementary proofs and identify false claims with counterexamples.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Prove or disprove a graph or counting statement for small examples with a simple enumeration program.
  - Verification: State conditions precisely and compare code outputs with an independently reasoned result.
  - Evidence: Proof, counterexample, enumerator and assumptions.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 7 — Check a linear transform:**
  - Objective: Interpret ranks, transformations and degeneracy in small numerical problems.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Implement a small matrix transform and validate identity, composition and degenerate cases.
  - Verification: Compute expected results by hand and compare with code, including a singular input.
  - Evidence: Computations, code and error analysis.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 8 — Analyze a simulated experiment:**
  - Objective: Interpret uncertainty and resist overclaiming from small samples.
  - Prerequisites: Complete the teaching lessons and conceptual checkpoint.
  - Environment: Record the language/runtime and tool versions and provide self-contained safe input fixtures.
  - Work: Simulate two populations, estimate uncertainty and compare means with a documented sampling plan.
  - Verification: Show coverage or uncertainty across repeated samples and explain what cannot be concluded.
  - Evidence: Scripts, plots or tables, assumptions and inference note.
  - Failure analysis: Explain at least one incorrect result, boundary condition or runtime failure and the correction.
- **Module 9 — Study gradient descent on a simple function:**
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
