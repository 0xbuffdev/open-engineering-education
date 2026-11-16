# SEF8 — Mathematics for Numerical Computing & AI

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF11](SEF11.md)
**Duration:** 12–14 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [Course format](../../spec/course-format.md)

## Overview

Study algebraic functions, exponentials, logarithms and limits, then linear algebra, probability and statistics, derivatives, elementary integration, floating-point behavior, numerical methods and introductory optimization. Develop independently checkable mathematical arguments before comparing them with Python calculations, and distinguish exact results, numerical estimates and uncertain statistical claims.

**SEF11 is the prerequisite**, providing arithmetic and algebraic fluency, logic, counting, proof, recurrence and graph reasoning for the numerical topics in this course. No separate entrance diagnostic is required here; mathematics support is available through formative review without an additional admission gate. SEF4 may proceed in parallel with SEF8 after SEF11, but both retain their own completion requirements.

Use Python 3.11+ and its standard library (`fractions`, `math`, `statistics`, `itertools`, `random`, `unittest`) alongside reviewable paper or accessible digital derivations. Paid books, proprietary assessment, NumPy, network services and other scientific packages are **not** required. Document calculation domains, platforms, actual commands, seeds, numeric tolerances and independent expected values.

The 12–14-week duration is provisional pending learner calibration. The six required assessments below are outcome-based; their identifiers are intentionally nonconsecutive and do not imply missing exams. There is no mandatory quiz/lab quota per module.

## Learning outcomes

- **SEF8-O19:** Analyze algebraic, polynomial, rational, exponential and logarithmic functions, their domains, composition, introductory limits and continuity required for calculus.
- **SEF8-O3:** Use exact and approximate computation in Python to verify mathematical work, distinguish rounding from conceptual errors, and report invalid inputs transparently.
- **SEF8-O6:** Compute vector sums, norms, dot products and compatible matrix products with correct dimensions and geometrical interpretation.
- **SEF8-O7:** Analyze small linear systems, basis, rank, singularity, null spaces and simple transformations, distinguishing unique, inconsistent and underdetermined cases.
- **SEF8-O8:** Calculate unconditional, conditional and Bayesian probabilities under stated assumptions, handling zero-probability conditioning and dependence explicitly.
- **SEF8-O9:** Calculate descriptive statistics, expected values and variance with appropriate population/sample definitions; reproduce and qualify seeded simulations.
- **SEF8-O10:** Interpret sampling bias, variability, standard errors, approximate confidence intervals and p-values without unsupported certainty or causal claims.
- **SEF8-O11:** Differentiate elementary functions, compute partial derivatives and gradients, and explain the chain rule and geometric meaning of a gradient.
- **SEF8-O12:** Approximate derivatives and gradients numerically while examining step size, truncation, floating-point rounding and justified error tolerances.
- **SEF8-O14:** Model finite probability or statistical experiments with transparent estimands, assumptions and reproducible random seeds, and interpret their uncertainty.
- **SEF8-O15:** Analyze simple floating-point representation and cancellation failures, including the limits of exact equality and finite precision.
- **SEF8-O16:** Implement and analyze bounded gradient descent with explicit step sizes, stopping rules, invalid-input handling, and convergence/divergence examples.
- **SEF8-O17:** Build a reproducible standard-library numerical notebook or small library with hand-derived reference results, deterministic tests and appropriate error contracts.
- **SEF8-O18:** Defend mathematical assumptions, computational limits and a diagnosed failure using transparent evidence, independent reproduction and accessible reasoning.
- **SEF8-O20:** Interpret accumulation, Riemann sums and elementary antiderivatives and definite integrals, connecting continuous probability densities to integration under stated assumptions.

## Modules

### Module 1 — Algebra, Functions and Limits

#### Outcomes

- SEF8-O19
- SEF8-O3

#### Lessons

1. **Function domains** — Evaluate domain, range, polynomial and rational functions, including excluded denominator values
2. **Algebraic manipulation** — Factor elementary polynomials and solve equations with substitution checks
3. **Coordinates and slopes** — Interpret elementary function graphs, secants and rates of change
4. **Exponential functions** — Apply exponent laws and explain exponential growth with stated domains
5. **Logarithms** — Use the inverse relation with exponentials, logarithm laws and positive arguments
6. **Function composition** — Compute composed functions and explain undefined intermediate expressions
7. **Limits and continuity** — Distinguish a limiting value from a finite sample or function value at a point
8. **Exact and approximate checking** — Verify independently derived examples with rational arithmetic and justified rounding

*Optional practice:* Predict a domain error and explain why a numerical table is not a proof of a limit.

### Module 2 — Vectors & Matrices

#### Outcomes

- SEF8-O6
- SEF8-O7

#### Lessons

1. Vectors
2. Norms and distance
3. Dot products
4. Angles and orthogonality
5. Matrices
6. Matrix multiplication
7. Linear systems
8. Linear independence, span and basis
9. Matrix transformations and composition
10. Solutions of linear systems and singular cases

*Optional practice:* Draw vectors and a matrix transformation, then test dimensions and a singular example with small exact numbers.

### Module 3 — Linear Algebra for Computation

#### Outcomes

- SEF8-O6
- SEF8-O7

#### Lessons

1. Vector spaces and linear independence
2. Basis, rank and null space
3. Matrix transformations and compositions
4. Eigenvectors and eigenvalues as introductory concepts
5. Numerical linear-system accuracy

*Optional practice:* Investigate null vectors of a rank-deficient matrix and compare exact rational calculations with rounded floats.

### Module 4 — Probability & Statistics

#### Outcomes

- SEF8-O8
- SEF8-O9
- SEF8-O14

#### Lessons

1. Probability basics
2. Conditional probability
3. Independence
4. Bayes' theorem
5. Distributions
6. Expected value and variance
7. Descriptive statistics
8. Random variables and conditional distributions
9. Sampling variability and bias
10. Confidence intervals and uncertainty statements

*Optional practice:* Count a conditional-probability table by hand and compare its ratios with a seeded synthetic simulation.

### Module 5 — Statistical Inference & Experimental Reasoning

#### Outcomes

- SEF8-O9
- SEF8-O10
- SEF8-O14

#### Lessons

1. Sampling, bias and variability
2. Estimators and standard errors
3. Confidence intervals and interpretation
4. Hypothesis tests and p-values
5. Correlation versus causation
6. Basic experimental design and reproducibility

*Optional practice:* Repeat a seeded Bernoulli experiment under a second seed and explain why observed coverage fluctuates.

### Module 6 — Differentiation, Integration and Numerical Gradients

#### Outcomes

- SEF8-O19
- SEF8-O20
- SEF8-O11
- SEF8-O12
- SEF8-O15
- SEF8-O3

#### Lessons

1. **Rates and derivatives** — Connect secant slopes, tangent slopes and the limit definition of derivative
2. **Derivative rules** — Differentiate polynomials and simple exponentials and justify a chain-rule computation
3. **Partial derivatives** — Compute a function's partial derivatives with other variables held fixed
4. **Gradients** — Derive and interpret the gradient of a two-variable function
5. **Accumulation and Riemann sums** — Interpret definite integrals as limits of sums, including signed accumulation
6. **Antiderivatives and the fundamental theorem** — Evaluate an elementary definite integral and check by differentiation
7. **Continuous probability** — Explain why interval probability is an integral of a nonnegative density
8. **Finite differences** — Compare forward and central derivative approximations with analytic results
9. **Truncation and rounding** — Diagnose invalid step sizes, finite precision and cancellation

*Optional practice:* By hand compute f'(2)=7 for f(x)=x²+3x and integral 0 to 1 of 2x = 1; compare with numerical estimates.

### Module 7 — Numerical Methods & Optimization Foundations

#### Outcomes

- SEF8-O11
- SEF8-O12
- SEF8-O15
- SEF8-O16

#### Lessons

1. Floating-point error and representation
2. Truncation versus rounding error
3. Numerical derivatives and step-size trade-offs
4. Gradient descent and learning-rate behavior
5. Stopping criteria and convergence limitations

*Optional practice:* Trace gradient descent updates by hand and compare a stable step size with a deliberately unstable one.

### Module 8 — Numerical Computing Notebook

#### Outcomes

- SEF8-O19
- SEF8-O3
- SEF8-O6
- SEF8-O7
- SEF8-O8
- SEF8-O9
- SEF8-O10
- SEF8-O11
- SEF8-O12
- SEF8-O14
- SEF8-O15
- SEF8-O16
- SEF8-O17
- SEF8-O18
- SEF8-O20

#### Lessons

1. Notebook or small-library structure and independent mathematical oracles
2. Exact rational arithmetic and elementary function-table checks
3. Algebraic functions, calculus and linear-algebra exercises
4. Bayesian probability, simulated sampling and labeled uncertainty
5. Differentiation, integration, numerical error and bounded optimization
6. Clean-start documentation, tests and independent mathematical defense

*Optional practice:* Outline a lightweight Python numerical notebook with reference cases, explicit tolerances and a reproducible test harness.

## Completion requirements

### Assessment environment and review

Each assessed executable artifact must be reproducible from a clean environment with Python's standard library, documented commands, independent references, actual observed results and meaningful error/failure behavior. For conceptual work, an inspectable derivation or explanation can establish the outcome. A green test, exact floating-point coincidence or simulation alone does not establish mathematical understanding, a general theorem or statistical certainty. Learners may reuse earlier verified components; optional practice is not a new mandatory submission. Unmet required criteria must be corrected and reassessed.

### Required summative assessments

- **SEF8-AS3** (required vectors, matrices and linear systems)
  - Outcomes: SEF8-O6, SEF8-O7, SEF8-O3, SEF8-O18
  - Work: Implement vector addition, dot product, norm and matrix/vector or rectangular matrix multiplication using the Python standard library, with explicit dimension and ragged-input validation. Hand-calculate the norm of (3,4), the dot product of (3,4) and (-4,3), and the product of A=[[1,2],[3,4]] with x=(2,-1). Show a rank-deficient example B=[[1,2],[2,4]] with an explicit nonzero null vector. Solve a small nonsingular system and reject or classify singular inconsistent versus non-unique cases. Explain one transformation composition and show a small diagonal eigenpair directly by substitution.
  - Criteria: Hand answers include norm 5, dot product 0, Ax=(0,2) and the correct singular rank/null-space reasoning. Matrix shape checks prevent silent mismatches, and the solver never claims a unique solution for a rank-deficient system. Composition order, basis/independence claims and selected transformation effects are interpreted consistently. Exact rational and approximate float comparisons are labeled with justified tolerances and independently checked examples, not arbitrary equality assumptions.
  - Evidence: Vector and matrix source, diagrams or hand calculations, singular/nonsingular fixtures, independent oracle results, dimension/bounds failures, documented numeric tolerance, and one diagnosed error or corrected interpretation.

- **SEF8-AS4** (required probability, bayes and descriptive statistics)
  - Outcomes: SEF8-O8, SEF8-O9, SEF8-O14, SEF8-O3
  - Work: Compute an explicit base-rate problem: prevalence 0.10, sensitivity 0.80 and false-positive rate 0.20, including the posterior for a positive result and what happens if the conditioning event has probability zero. State independence and conditioning assumptions. For values [2,4,6], derive the mean and both population and sample variances and compare to the Python statistics module. Model a synthetic two-stage conditional test with a fixed seed and at least 10,000 runs; record true-positive and false-positive counts, estimate the posterior and repeat with a second seed. Include invalid probabilities, empty samples and undefined sample variance.
  - Criteria: The analytic posterior is 4/13 and its denominator is justified by the relevant conditional event; the descriptive calculations produce mean 4, population variance 8/3, and sample variance 4. Probability inputs lie in valid bounds and impossible conditioning is rejected or labeled undefined. Sampling output is reproducible under the recorded seed, but exact frequencies are not incorrectly required to equal the mathematical probability. The learner distinguishes independence from conditional probability and random sampling variability from an algorithmic error.
  - Evidence: By-hand probability table and statistics calculations, implementation with input validation, deterministic seed/trial counts and observed contingency table, standard-library reference comparisons, invalid/empty cases and a reasoned simulation discrepancy.

- **SEF8-AS6** (required sampling uncertainty and responsible statistical inference)
  - Outcomes: SEF8-O9, SEF8-O10, SEF8-O14, SEF8-O18
  - Work: For 60 successes in 100 independent Bernoulli trials, compute the sample proportion, plug-in standard error and explicitly labeled approximate 95% normal interval. State the independence, sample-size and approximation assumptions; identify when the method fails for extreme proportions or very small samples. Simulate repeated samples under a fixed seed for a known probability, recording estimated interval coverage across at least 1,000 replicates and discussing Monte Carlo variability. Deliberately bias a second sample, describe how that changes inference, and explain a p-value without equating it to the probability the null hypothesis is true. Distinguish observed association from an established causal effect.
  - Criteria: The sample proportion is 0.6; standard error is sqrt(0.6*0.4/100), approximately 0.049, and the labeled normal 95% interval is approximately [0.504,0.696]. Calculations use the declared approximate method and appropriately reject or qualify pathological/invalid cases. Coverage is reported as an empirical estimate without imposing a fabricated exact frequency; seeds, replicate count and biased selection mechanism remain inspectable. A confidence interval, p-value, bias and causal claim are interpreted according to their actual assumptions and limits.
  - Evidence: Hand calculations and formula, labeled interval code, declared random process and seed, repeated-run coverage output, bias comparison, invalid input cases, and a short explanation addressing uncertainty, p-values and causality.

- **SEF8-AS9** (required algebra, limits, differentiation and integration)
  - Outcomes: SEF8-O19, SEF8-O20, SEF8-O11, SEF8-O12, SEF8-O3, SEF8-O18
  - Work: Solve an unfamiliar rational-function domain problem with excluded inputs and an exponential/logarithm identity with valid positive arguments. Give an algebraic limit argument and explain why finite numerical samples cannot prove the limit. Derive f'(2)=7 for f(x)=x²+3x and the gradient (8,3) of g(x,y)=x²+3xy at (1,2); give a distinct valid chain-rule example. Explain a finite Riemann sum and derive the definite integral of 2x from 0 to 1 (value 1) by an antiderivative. Explain interval probability for a nonnegative probability density. Implement forward and central finite-difference estimates, analyze their errors across positive step sizes, and detect invalid or non-finite inputs and cancellation.
  - Criteria: Domains, logarithm assumptions, algebraic limit arguments and derivative/gradient/integral derivations are correct. Finite evidence is not mistaken for analytic proof. Density values are not presented as interval probabilities, error tolerances and approximation limits are justified, and a deliberate calculation or code defect is diagnosed and repaired.
  - Evidence: Independent algebra, limit, derivative and integral working, Riemann-sum reasoning and density explanation, Python source with step-size/error table, invalid-input cases, checkable expected values and failure/repair record.

- **SEF8-AS7** (required floating-point behavior and bounded gradient descent)
  - Outcomes: SEF8-O11, SEF8-O12, SEF8-O15, SEF8-O16, SEF8-O18
  - Work: Analyze finite-precision rounding and cancellation with an elementary numeric example. Implement f(x)=(x-3) squared, its analytic gradient and finite-difference approximation with valid positive h. Perform gradient descent from x0=0 using a documented positive learning rate, bounded iteration count and stop criteria, recording x, f(x) and the residual each iteration. Hand-compute the first two iterations at learning rate 0.25; compare runs at rates 0.1, 0.25, 1.0 and 1.1 under the same initial state. Reject nonfinite inputs, invalid rates, zero finite-difference step and a nonconverging run without an indefinite loop.
  - Criteria: At rate 0.25 the first updates are x1=1.5 and x2=2.25; for the stated function/runs, rate 1.0 oscillates 0↔6 and 1.1 diverges from the minimizer. The test records both a finite iteration budget and a justified convergence criterion; absence of convergence is reported as a bounded result, not success. Numerical errors, truncation and rounding are distinguished, no unqualified exact float equality is required, and invalid rates/inputs fail predictably. The learner explains the mathematical recurrence behind the observed stability or divergence.
  - Evidence: Analytic update derivation, Python optimizer and finite-difference source, multi-rate iteration logs with stop reasons, expected/actual tests including failures and edge cases, controlled precision/tolerance notes, and a corrected defect.

- **SEF8-AS10** (required integrated numerical computing and defense)
  - Outcomes: SEF8-O3, SEF8-O6, SEF8-O7, SEF8-O8, SEF8-O9, SEF8-O10, SEF8-O11, SEF8-O12, SEF8-O14, SEF8-O15, SEF8-O16, SEF8-O17, SEF8-O18, SEF8-O19, SEF8-O20
  - Work: Assemble assessed numerical work into an offline Python notebook or portable small library using the standard library. Include independent expected results for a function/domain, derivative and integral, vector/matrix product, singular linear system, conditional probability, descriptive and inferential statistics with a seeded experiment, finite-precision counterexample and bounded gradient descent. Reuse earlier artifacts instead of making unrelated projects. Document clean-run commands, reproducible fixtures, exact and approximate assumptions, and obtain independent reproduction of an unfamiliar normal and failing case. Diagnose a fault and defend the algorithm and limitations.
  - Criteria: Every outcome has actual inspectable evidence rather than merely a declared ID. Mathematical working and tests agree on independent references; singular, invalid, non-finite or nonconvergent cases are not misrepresented as successes. Statistical simulations are reproducible without claiming exact frequencies or causation, and numerical tolerances are explained. No hidden paid tool, package or service is needed, and independent reproduction and defense establish personal understanding.
  - Evidence: Versioned portable source and README, exact clean-start commands and tool versions, mathematical oracle and test matrix, numeric tolerances and seeds, worked derivations, negative fixtures, reviewer observations, a fault correction and technical defense.

### Completion decision

All six required assessments (`SEF8-AS3`, `SEF8-AS4`, `SEF8-AS6`, `SEF8-AS7`, `SEF8-AS9`, `SEF8-AS10`) must pass; together they evaluate the fifteen current outcomes. The integrated notebook may reuse inspected work and does not demand a duplicate project.

Assessment identifiers are stable and intentionally nonconsecutive; the six assessments listed above are the complete current requirement. Mathematical preparation in discrete reasoning is established through SEF11, while numerical mathematics is assessed in this course. This course remains `draft` pending [readiness evidence](../../spec/status-labels.md).
