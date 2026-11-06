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

   Build and explain a small collection of mathematical functions using Python's standard library, with hand-worked test cases and repeatable verification. Scientific packages such as NumPy may be used for optional cross-checks but are not required. The final project must connect the beginner arithmetic bridge to discrete reasoning, linear algebra, probability, statistics, differentiation and numerical optimization under the criteria below.

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

**Required assessments and reproducible lab criteria for Modules 2–10:**

These checkpoints assess mathematical reasoning, not memorization of published example answers. The two sample questions for each module include the expected result and decisive reasoning; reviewers may use equivalent unfamiliar prompts that assess the same outcomes. A module passes only when its stated foundational assumptions, calculations, and required practical evidence are correct. Errors are remediated and reassessed. The ungraded Module 1 diagnostic and mastery policy remain unchanged.

**Shared environment:**

Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.

**Shared acceptance and evidence rules:**

- Demonstrate each checkpoint's result and reasoning, not a guessed numerical output. Explain applicable definitions, constraints, approximation conditions and counterexamples.
- Complete each required module lab, including its normal, boundary and failure conditions, with independent expected values wherever possible.
- Identify actual run commands, versioned source, hand-worked calculations, test outputs, tool versions, seeds where applicable and a technical retrospective. Unsupported claims of correctness do not count as evidence.
- Provide clear remediation opportunities for mathematical misconceptions. Do not require payment, NumPy or pre-existing mathematical qualifications.

**Module 2 — Logic, Sets & Discrete Reasoning: checkpoint** — Required assessment details

- **Q1 (free):** A claim says 'every submitted program passes its tests'. State the logical negation and identify when an implication p → q is false.
  - Expected answer and scoring: The negation is 'there exists at least one submitted program that does not pass its tests'. p → q is false only when p is true and q is false; otherwise true. Explain the difference between a counterexample and a restatement.
- **Q2 (free):** From five distinct tasks, how many ways can two be selected if order does not matter, and how many if order matters?
  - Expected answer and scoring: C(5,2) = 5×4/2 = 10 unordered selections; P(5,2) = 5×4 = 20 ordered pairs. Explain why switching the tasks makes a new outcome only in the ordered case.

**Module 2 — Count and verify: required lab** — Required assessment details

- **Objective:** Represent elementary propositions, sets and finite selections and verify mathematical counts using code.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Write the full truth table for p → q and its equivalence with (not p) or q; explain the negation of a universal statement.
  2. Implement a small Python set exercise with union, intersection, difference and membership, including empty and overlapping sets.
  3. Use `itertools.combinations` and `itertools.permutations` to enumerate selecting two items from five and compare counts with hand calculations.
  4. Test boundary cases selecting zero items, all items and more items than exist; document valid behavior and an invalid request case.
- **Expected result:** All four truth-table rows match, set operations match hand-worked sets, and enumeration yields 10 combinations and 20 permutations for n=5, k=2.
- **Verification:** Assert truth-table equivalence, computed counts and set invariants with independently derived expected values; describe why finite examples do not prove a universal identity.
- **Evidence:** Truth tables, mathematical derivations, Python script, test output and documented boundary cases.
- **Failure analysis:** Explain a mistaken logical negation, order-sensitive counting error or an attempt to generalize from finite enumeration.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 3 — Vectors & Matrices: checkpoint** — Required assessment details

- **Q1 (free):** For vectors u=(3,4) and v=(-4,3), calculate ||u|| and u·v. What does the dot product reveal?
  - Expected answer and scoring: ||u|| = sqrt(3²+4²) = 5; u·v = 3×(-4)+4×3 = 0. Both vectors are nonzero, so they are orthogonal.
- **Q2 (free):** For matrix A=[[1,2],[3,4]] and column vector x=(2,-1), compute Ax. Explain why B=[[1,2],[2,4]] is singular.
  - Expected answer and scoring: Ax=(1×2+2×(-1),3×2+4×(-1))=(0,2). det(B)=1×4−2×2=0 and its rows are dependent, so B has no inverse.

**Module 3 — Matrices without NumPy: required lab** — Required assessment details

- **Objective:** Implement and explain vector/matrix arithmetic, dimensions and singular-system safeguards.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Implement vector addition, dot product and Euclidean norm in Python using lists without third-party numerical packages.
  2. Implement matrix multiplication for rectangular compatible shapes; reject mismatched dimensions and malformed ragged rows clearly.
  3. Compute Ax and the singular example in the checkpoint by hand, then verify the program's result.
  4. Test identity multiplication, zero vectors, rectangular dimensions and at least one intentionally incompatible shape.
  5. Record where exact integer/rational arithmetic applies and where floating-point rounding requires tolerances.
- **Expected result:** Ax = (0,2), dot product = 0, norm = 5; valid matrix products have correct dimensions; invalid shapes raise a documented error rather than a silent wrong answer.
- **Verification:** Compare small matrix products with independently worked examples and verify identity and distributive properties on seeded finite fixtures.
- **Evidence:** Manual calculations, Python source, dimension-check tests, failure logs and a note on numerical precision.
- **Failure analysis:** Identify a transposed-index or shape error, singular matrix mistaken for invertible, or exact-equality misuse with floating numbers.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 4 — Probability & Statistics: checkpoint** — Required assessment details

- **Q1 (free):** In a population 10% have condition D. A test detects D 80% of the time and gives a positive result to 20% of people without D. Compute P(D | positive).
  - Expected answer and scoring: P(D|+) = (0.8×0.1)/((0.8×0.1)+(0.2×0.9)) = 0.08/0.26 = 4/13 ≈ 0.3077. A positive result is not the same as an 80% chance of D.
- **Q2 (free):** For dataset [2,4,6], compute the mean, population variance and sample variance. State which denominator each uses.
  - Expected answer and scoring: Mean=4; squared deviations total 8; population variance=8/3; sample variance=8/(3−1)=4 when estimating from a sample. State explicitly whether the observed data is treated as a population or sample.

**Module 4 — Simulate an experiment: required lab** — Required assessment details

- **Objective:** Connect conditional probability and descriptive statistics to controlled sampling and measurable uncertainty.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Calculate the Bayesian test example by hand and validate its posterior using a Python function that checks probability inputs and nonzero conditioning probability.
  2. Simulate a two-stage test process with an explicitly chosen random seed and at least 10,000 synthetic cases; record observed true/false positive counts.
  3. Compute mean and both population/sample variances for [2,4,6] using direct arithmetic and compare with `statistics` functions.
  4. Compare simulation frequencies to analytically expected probabilities and discuss finite-sample variability; repeat with a second seed.
  5. Test boundary cases such as zero sample size and undefined P(D|+) when no positive results are possible.
- **Expected result:** The analytic posterior is 4/13; the sample calculations give 4, 8/3 and 4; simulated frequency estimates are near—not necessarily equal to—the analytical values.
- **Verification:** Assert deterministic analytic results, test probability bounds and undefined conditional cases, retain random seed and trial count, and report variability without requiring exact simulation counts.
- **Evidence:** Hand formulas, Python scripts, random seeds, simulated counts, variance checks and interpretation of uncertainty.
- **Failure analysis:** Explain base-rate neglect, confusion between sample and population variance, or treating Monte Carlo estimates as exact.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 5 — Derivatives, Gradients & Complexity: checkpoint** — Required assessment details

- **Q1 (free):** For f(x)=x²+3x, derive f'(x) and evaluate it at x=2. What should a central finite difference approach as h decreases while arithmetic remains sufficiently precise?
  - Expected answer and scoring: f'(x)=2x+3 and f'(2)=7. (f(2+h)−f(2−h))/(2h) approaches 7 as h→0; for this quadratic its real-arithmetic central difference is exactly 7 when h≠0, but finite-precision cancellation can cause error at tiny h.
- **Q2 (free):** For g(x,y)=x²+3xy, compute its gradient at (1,2). Explain how n·log(n) compares with n² for large n.
  - Expected answer and scoring: ∂g/∂x = 2x+3y, ∂g/∂y=3x, so ∇g(1,2)=(8,3). For n→∞, n log n grows asymptotically slower than n²; the logarithm base changes only a constant factor.

**Module 5 — Check a derivative: required lab** — Required assessment details

- **Objective:** Calculate analytic and numerical derivatives and distinguish numerical error from asymptotic growth.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Derive and implement f(x)=x²+3x and its derivative; compare forward and central finite differences across several positive h values, for example 10⁻¹ through 10⁻⁸.
  2. Calculate ∇g(1,2) analytically and compare with coordinate-wise finite differences.
  3. Create a table comparing n, n·log₂(n) and n² at increasing n; explain why observed finite values are not a proof of a growth bound.
  4. Record absolute derivative error, step size and floating-point considerations; reject h=0 explicitly.
  5. Repeat a failing variant with incorrectly signed finite differences or unsuitable tiny h, then explain the discrepancy.
- **Expected result:** Analytic values f'(2)=7 and ∇g(1,2)=(8,3) are reproduced within justified numerical tolerances; error behavior is explained rather than assumed monotonic.
- **Verification:** Use known polynomial derivatives as an oracle; show a table of h and error, with a clear treatment of cancellation at tiny step sizes.
- **Evidence:** Hand derivatives, code, numerical tables, tolerances, error/repair narrative and computational conditions.
- **Failure analysis:** Explain division by zero, subtraction cancellation, misuse of a one-sided formula or treating sample timings as a complexity proof.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 6 — Proofs, Relations & Graph Mathematics: checkpoint** — Required assessment details

- **Q1 (free):** Prove by induction that the sum of the first n positive odd integers equals n² for every integer n≥1.
  - Expected answer and scoring: Base n=1 gives 1=1². Assume sum of first n odds = n²; adding next odd 2n+1 yields n²+2n+1=(n+1)². State why base and induction imply the claim for all n≥1.
- **Q2 (free):** A simple undirected triangle graph has three edges. Compute the sum of its vertex degrees and generalize using the handshaking lemma.
  - Expected answer and scoring: Each vertex degree is 2, giving total 6 = 2×3 edges. In a finite undirected graph every edge contributes two incidences, so sum of degrees = 2|E| (counting a loop twice if loops are allowed).

**Module 6 — Verify graph and recurrence identities: required lab** — Required assessment details

- **Objective:** Construct small proofs, test finite counterexamples and explain what computation cannot establish universally.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Write a complete induction proof for the sum of the first n odd integers and verify the formula with a small Python summation for n=1..100.
  2. Represent finite undirected simple graphs using an edge set; compute degrees and check that the total equals twice the edge count.
  3. Enumerate all simple undirected graphs on up to four labeled vertices and check the degree identity for every case.
  4. Construct a false universal graph claim and demonstrate a minimal counterexample, clearly stating its assumptions.
  5. Distinguish a proof based on counting incidences from empirical enumeration of finitely many graphs.
- **Expected result:** The stated sum identity and handshaking lemma hold for all tested cases, with mathematical arguments establishing their general validity under the stated assumptions.
- **Verification:** Compare a hand-worked triangle and empty graph with code; retain proof steps, enumeration size and explicit counterexample.
- **Evidence:** Induction proof, graph fixtures/enumerator, tests, a false claim and counterexample, and limitations statement.
- **Failure analysis:** Explain invalid induction steps, double-counting edges, confusion about directed versus undirected degree or mistaken belief that exhaustive small tests prove every case.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 7 — Linear Algebra for Computation: checkpoint** — Required assessment details

- **Q1 (free):** For B=[[1,2],[2,4]], state its rank and give a nonzero vector in its null space.
  - Expected answer and scoring: rank(B)=1 because the second row is twice the first. (-2,1) lies in its null space since B(-2,1)=(0,0). Its columns are linearly dependent and the matrix is singular.
- **Q2 (free):** For D=[[2,0],[0,3]], verify one eigenvector for each eigenvalue and explain what the transformation does.
  - Expected answer and scoring: D(1,0)=(2,0)=2(1,0), so (1,0) is an eigenvector with λ=2. D(0,1)=(0,3)=3(0,1), so (0,1) has λ=3. The transformation independently scales the coordinate axes.

**Module 7 — Check a linear transform: required lab** — Required assessment details

- **Objective:** Demonstrate basis/rank and transform reasoning, including degenerate and invalid numerical cases.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Implement small 2×2 matrix-vector multiplication and composition using standard-library Python.
  2. Verify D's eigenpair examples and B's null-space example by direct multiplication.
  3. Solve a nonsingular two-equation system, explain the determinant or pivot condition and reject an inconsistent or underdetermined singular system when uniqueness is required.
  4. Test identity and composition on two example vectors, checking (AB)x=A(Bx) for compatible shapes.
  5. Compare numeric results against exact hand calculations and record any floating tolerance used.
- **Expected result:** The rank-one matrix is recognized as singular, its null vector maps to zero, the diagonal eigenpairs hold and a nonsingular system has its correct unique solution.
- **Verification:** Use reference calculations independent of the algorithm; include singular and mismatched-size negative cases and test all stated equalities.
- **Evidence:** Written derivations, Python tests, example transformations, singular-case trace and a brief condition/precision note.
- **Failure analysis:** Explain conflating any solution with a unique solution, matrix product order or unstable floating-point pivot checks.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 8 — Statistical Inference & Experimental Reasoning: checkpoint** — Required assessment details

- **Q1 (free):** For 100 independent Bernoulli trials with 60 successes, estimate the success probability, its plug-in standard error and an approximate 95% normal confidence interval. State the approximation's assumptions.
  - Expected answer and scoring: p̂=0.6, estimated SE = sqrt(0.6×0.4/100)=sqrt(0.0024)≈0.049. Wald normal approximation gives about 0.6±1.96×0.049 ≈ [0.504,0.696]. Requires representative independent draws and adequate success/failure counts; explain interval limitations and use a more suitable method when conditions fail.
- **Q2 (free):** What does a p-value mean, and can correlation by itself prove that an intervention caused an outcome?
  - Expected answer and scoring: A p-value is the probability, assuming a specified null model, of a result at least as extreme as the one observed under the defined test statistic. It is not P(the null hypothesis is true). Correlation alone does not establish causation because of confounding, selection and alternative explanations.

**Module 8 — Analyze a simulated experiment: required lab** — Required assessment details

- **Objective:** Quantify sampling uncertainty and interpret simulated experiment results without unsupported causal claims.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Using a fixed seed, simulate independent Bernoulli observations for populations with known p values, for example 0.5 and 0.6, under a documented sampling plan.
  2. Compute observed proportions and standard-error estimates using Python standard library; implement and label the specified approximate interval, with conditions for when it is inappropriate.
  3. Repeat many samples (for example at least 1,000), compare nominal 95% interval coverage with observed coverage and discuss why estimates vary.
  4. Add a deliberately biased sampling rule and observe how its estimates differ; identify whether the resulting difference can be interpreted causally.
  5. Test zero sample size, very small samples and extreme proportions explicitly instead of applying the normal approximation indiscriminately.
- **Expected result:** The estimated proportion and standard-error calculations match independent formulas; empirical results show sampling variation and approximate coverage with explicit limitations.
- **Verification:** Retain seeds, sample sizes, conditions, calculations and coverage counts; check analytic cases and avoid requiring simulated values to match a fixed number.
- **Evidence:** Simulation source, random seeds, parameter table, coverage/uncertainty results, biased-sample comparison and interpretation.
- **Failure analysis:** Explain misinterpretations of p-values, biased data, invalid approximation conditions or unearned causal claims.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 9 — Numerical Methods & Optimization Foundations: checkpoint** — Required assessment details

- **Q1 (free):** For f(x)=(x−3)², give f'(x). Starting x₀=0 and learning rate η=0.25, calculate the first two gradient-descent updates.
  - Expected answer and scoring: f'(x)=2(x−3). x₁=0−0.25×(−6)=1.5; x₂=1.5−0.25×(−3)=2.25. The minimizer is x=3; explain the stopping criterion.
- **Q2 (free):** For the same function, what happens at constant learning rate η=1 starting from x₀=0, and why does decreasing h indefinitely not always improve finite differences?
  - Expected answer and scoring: With η=1, x₁=6 and x₂=0; the sequence oscillates rather than converging. In floating point, tiny h can amplify rounding/cancellation even though truncation error decreases for a suitable finite-difference scheme.

**Module 9 — Study gradient descent on a simple function: required lab** — Required assessment details

- **Objective:** Implement finite differences and gradient descent while documenting convergence, divergence and stopping behavior.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Implement f(x)=(x−3)² and its exact derivative plus a finite-difference approximation at several h values.
  2. Implement gradient descent with a fixed iteration limit, explicit learning rate, and termination based on a documented derivative or step-size tolerance.
  3. Start at x₀=0 and compare η=0.1, 0.25, 1.0 and 1.1; report iteration-by-iteration x and f(x), convergence or lack thereof.
  4. Reproduce the first two η=0.25 updates by hand, then verify code output and numerical behavior.
  5. Test invalid learning rates, zero step size in finite differences, nonfinite inputs and a nonconverging run.
- **Expected result:** For η=0.25, x₁=1.5 and x₂=2.25, then x approaches 3; η=1 oscillates 0↔6, and η=1.1 diverges from the minimizer for the stated starting point.
- **Verification:** Check the first two analytic updates, record a fixed stopping rule and iteration cap, and compare exact versus approximated gradients under documented tolerances.
- **Evidence:** Source, analytic derivation, iteration tables, plotted or tabulated trajectories, exceptions and a reflection on numerical limits.
- **Failure analysis:** Explain an unstable learning rate, an invalid termination condition, floating cancellation or unbounded iterations.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Module 10 — Numerical Computing Notebook: checkpoint** — Required assessment details

- **Q1 (free):** Given A=[[1,2],[3,4]] and x=(1,1), compute Ax and describe why an implementation must check dimensions.
  - Expected answer and scoring: Ax=(3,7). A has shape 2×2 and x has length 2; a mismatch must be rejected instead of silently truncating or indexing incorrectly.
- **Q2 (free):** A simulation produces 58 successes in 100 independent fair-coin trials. Does that prove the chance of success is 0.58? Explain and connect your claim to a mathematical check.
  - Expected answer and scoring: No. The observed proportion is 0.58, which varies across finite samples even when the model probability is 0.5. Quantify uncertainty or compare against a suitable sampling distribution; a single sample does not identify the true probability exactly.

**Module 10 — Numerical Computing Notebook: required lab** — Required assessment details

- **Objective:** Integrate introductory mathematical reasoning, standard-library computation and independent verification in one reproducible project.
- **Prerequisites:** Complete the module's lessons and explain its checkpoint questions; retain prior modules' essential prerequisites.
- **Environment:** Use a local Python 3.11+ environment and its standard library; record the exact interpreter version and operating system. Keep scripts, fixtures and repeatable tests under version control; use `python3 -m unittest discover -s tests -v` or another fully documented test command. Scientific packages may cross-check results but are never required. Use explicit random seeds where sampling is involved.
- **Procedure:**
  1. Create a repository or notebook with clear modules for exact rational arithmetic, set/counting exercises, vector and matrix operations, simple probability/statistics, numerical differentiation, and basic gradient descent.
  2. Include a proof/counterexample exercise or graph-degree invariant and a seeded sampling experiment with documented uncertainty, connecting the result to its mathematical assumptions.
  3. For each function, supply at least one hand-computed normal case plus a boundary/invalid case and define numerical tolerance where an exact assertion is unsuitable.
  4. Demonstrate the course's basic numeracy bridge in the same environment, including fraction arithmetic and a simple equation/function table.
  5. Use only the Python 3.11+ standard library for required work; NumPy may be used as an optional second implementation to cross-check results, never as an undisclosed requirement.
  6. Provide a clean-checkout README, a single repeatable test command, expected/actual output comparison and an outcomes-to-evidence table; have a reviewer reproduce and question one implementation choice.
- **Expected result:** Every declared operation produces the independently worked values on supplied fixtures; unsupported inputs fail transparently; the integrated project includes both exact and appropriately approximate reasoning.
- **Verification:** Run the full repository from a clean environment and compare its tests to hand calculations, exact fraction examples and analytic derivatives, retaining all random seeds and numerical tolerances.
- **Evidence:** Version-controlled implementation, hand work, CLI/notebook instructions, test logs, seeded data, derivations, failure analysis and a reviewer reproduction record.
- **Failure analysis:** Explain a mathematically wrong but numerically plausible result, an invalid assumption, hidden dependency or a claim overstating finite-sample evidence.
- **Acceptance:** All listed observable behaviors are demonstrated, invalid/boundary cases are handled and the mathematical reasoning is correct under documented assumptions. An independent reviewer can reproduce the work; unresolved required failures block completion.

**Exit demonstration:**

The learner can calculate small matrix operations, conditional probabilities, and simple derivatives by hand and explain where these ideas appear in software and machine learning.
