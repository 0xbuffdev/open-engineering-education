# SEF8 — Mathematics for Computing & AI

**Program:** SEF — Software Engineering Foundations
**Type:** `course`
**Prerequisites:** [SEF2](SEF2.md)
**Duration:** 11–12 weeks
**Status:** `draft`
**Specification:** `v0.2.0`
**Expected workload:** 10–15 focused hours/week (provisional; calibrate with learner evidence)

> [Software Engineering Foundations](README.md) · [OEE curriculum](../README.md) · [Course format](../../spec/course-format.md)

## Overview

Build mathematical confidence from arithmetic and pre-algebra through logic, proofs, linear algebra, probability, statistics, calculus and numerical optimization. Learn to make a mathematical claim, solve examples by hand, verify computation in Python, and explain the assumptions and limits that make an answer meaningful. This course supplies mathematical foundations for algorithms and introductory AI, rather than demanding advanced mathematics before entry.

**There is no prerequisite algebra, calculus, probability or formal mathematics course.** SEF2 provides the only formal course prerequisite. SEF3–SEF7 may be taken concurrently; they are not entry gates. Module 1 offers an **ungraded entry diagnostic** in arithmetic, fractions, signed values, equations and function tables. It identifies individual support needs and must not be used to exclude learners or impose a fixed attempt count. The essential numeracy and pre-algebra capabilities remain required outcomes: learners can demonstrate them after practice and reassessment with unfamiliar examples before progressing into material that relies on those skills. Faster learners may show equivalent mastery without repeating every preparatory exercise.

Use Python 3.11 or later and its standard library, including `fractions`, `math`, `statistics`, `itertools`, `random` and `unittest`, plus paper or accessible digital mathematical work. Required assessments run offline without NumPy, external scientific libraries, paid books, network access or a proprietary grader. Optional packages may provide *additional* comparisons, not replace hand-worked answers or become hidden requirements. Record interpreter version, exact commands, calculation assumptions, random seeds, precision and numerical tolerances.

The ten original module subjects remain the instructional sequence. Eight summative assessments integrate related mathematical abilities and may reuse verified functions and evidence in a final notebook or small library. Optional practice supports preparation; there is no compulsory checkpoint-and-lab quota for every module and no duplicate final project. Duration is an initial estimate. The course remains `draft` pending independent learner and reviewer evidence.

## Learning outcomes

- **SEF8-O1:** Calculate and interpret signed and whole numbers, fractions, decimals, percentages, proportions, rates, units, powers, and numerical estimates with correct order of operations.
- **SEF8-O2:** Translate elementary notation into equations, inequalities, input-output functions and coordinate tables; solve and check results independently.
- **SEF8-O3:** Use exact and approximate computation in Python to verify mathematical work, distinguish rounding from conceptual errors, and report invalid inputs transparently.
- **SEF8-O4:** Form and negate propositions with quantifiers, operate on finite sets and functions, and correctly count arrangements and selections.
- **SEF8-O5:** Construct elementary direct or inductive arguments and counterexamples, apply graph-degree and relation properties, and distinguish a universal proof from finite enumeration.
- **SEF8-O6:** Compute vector sums, norms, dot products and compatible matrix products with correct dimensions and geometrical interpretation.
- **SEF8-O7:** Analyze small linear systems, basis, rank, singularity, null spaces and simple transformations, distinguishing unique, inconsistent and underdetermined cases.
- **SEF8-O8:** Calculate unconditional, conditional and Bayesian probabilities under stated assumptions, handling zero-probability conditioning and dependence explicitly.
- **SEF8-O9:** Calculate descriptive statistics, expected values and variance with appropriate population/sample definitions; reproduce and qualify seeded simulations.
- **SEF8-O10:** Interpret sampling bias, variability, standard errors, approximate confidence intervals and p-values without unsupported certainty or causal claims.
- **SEF8-O11:** Differentiate elementary functions, compute partial derivatives and gradients, and explain the chain rule and geometric meaning of a gradient.
- **SEF8-O12:** Approximate derivatives and gradients numerically while examining step size, truncation, floating-point rounding and justified error tolerances.
- **SEF8-O13:** Compare algorithmic growth and simple recurrence bounds analytically, explaining why finite measurement alone does not prove an asymptotic class.
- **SEF8-O14:** Model finite probability or statistical experiments with transparent estimands, assumptions and reproducible random seeds, and interpret their uncertainty.
- **SEF8-O15:** Analyze simple floating-point representation and cancellation failures, including the limits of exact equality and finite precision.
- **SEF8-O16:** Implement and analyze bounded gradient descent with explicit step sizes, stopping rules, invalid-input handling, and convergence/divergence examples.
- **SEF8-O17:** Build a reproducible standard-library numerical notebook or small library with hand-derived reference results, deterministic tests and appropriate error contracts.
- **SEF8-O18:** Defend mathematical assumptions, computational limits and a diagnosed failure using transparent evidence, independent reproduction and accessible reasoning.

## Modules

### Module 1 — Mathematical Literacy & Pre-Algebra

#### Outcomes

- SEF8-O1
- SEF8-O2
- SEF8-O3

#### Lessons

1. Course introduction: Mathematics for Computing & AI
2. Ungraded entry diagnostic (identify individual bridge practice)
3. What mathematics describes: quantities, patterns and relationships
4. Counting, whole numbers, place value and number lines
5. Addition, subtraction, multiplication and division
6. Order of operations, grouping and estimation
7. Negative numbers and absolute value
8. Fractions and their operations
9. Decimals, percentages and conversions
10. Ratios, proportions, rates and measurement units
11. Powers, roots and scientific notation
12. Symbols, variables and arithmetic expressions
13. Solving simple linear equations and checking answers
14. Inequalities and coordinate pairs
15. Functions, input-output tables and basic graphs

*Optional practice:* Attempt an ungraded entry check, then use number-line, fraction, ratio, function-table and equation examples to identify topics needing more practice.

### Module 2 — Logic, Sets & Discrete Reasoning

#### Outcomes

- SEF8-O4
- SEF8-O5

#### Lessons

1. Propositional logic
2. Quantifiers
3. Sets
4. Functions
5. Counting rules
6. Permutations and combinations
7. Proof by contradiction and induction
8. Relations, equivalence and orderings
9. Graphs as mathematical objects

*Optional practice:* Compare a finite truth table and combinatorial enumeration with a general logical or counting argument.

### Module 3 — Vectors & Matrices

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

### Module 5 — Derivatives, Gradients & Complexity

#### Outcomes

- SEF8-O11
- SEF8-O12
- SEF8-O13

#### Lessons

1. Derivatives
2. Numerical derivatives
3. Partial derivatives
4. Gradients
5. Growth of functions
6. Algorithm complexity
7. Chain rule and gradient interpretation
8. Finite-difference approximation error
9. Growth rates and numerical stability

*Optional practice:* Calculate a derivative by hand before testing forward and central finite differences over several step sizes.

### Module 6 — Proofs, Relations & Graph Mathematics

#### Outcomes

- SEF8-O4
- SEF8-O5
- SEF8-O13

#### Lessons

1. Direct proof and induction
2. Contradiction and counterexample
3. Equivalence relations and partitions
4. Graph degree, paths and connectivity
5. Recurrences and combinatorial reasoning

*Optional practice:* Check an induction step and a handshaking-lemma example, then find a counterexample to a plausible false graph claim.

### Module 7 — Linear Algebra for Computation

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

### Module 8 — Statistical Inference & Experimental Reasoning

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

### Module 9 — Numerical Methods & Optimization Foundations

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

### Module 10 — Numerical Computing Notebook

#### Outcomes

- SEF8-O3
- SEF8-O14
- SEF8-O15
- SEF8-O17
- SEF8-O18

#### Lessons

1. Notebook or small-library structure and independent mathematical oracles
2. Exact rational arithmetic and elementary function-table checks
3. Discrete reasoning and linear-algebra exercises
4. Bayesian probability, simulated sampling and labeled uncertainty
5. Differentiation, numerical error and bounded optimization
6. Clean-start documentation, tests and independent mathematical defense

*Optional practice:* Outline a lightweight Python numerical notebook with reference cases, explicit tolerances and a reproducible test harness.

## Completion requirements

### Bridge, environment and evidence

The introductory numeracy diagnostic is **ungraded**: it identifies useful preparation and cannot be used as an entry barrier or a fixed-attempt summative requirement. SEF8-AS1 assesses *demonstrated* arithmetic and pre-algebra readiness after instruction or equivalent prior mastery, with no fixed number of attempts. Learners can revise work and be reassessed with equivalent unfamiliar examples before taking on later dependent mathematics. Do not confuse readiness for advanced modules with prerequisites for enrolling in the course.

All required work uses Python 3.11+, its standard library and reviewable handwritten, typed, spoken or otherwise accessible reasoning. Record source revision, exact commands, interpreter version, random seeds, rounding or numerical tolerances, and expected versus observed results. Use independent mathematical calculations to check code; one function calling itself is not an independent test oracle. Scientific packages such as NumPy are optional second opinions, not hidden prerequisites.

The reviewer records the result for each required assessment, which outcomes were directly evidenced and any remediation. Exact rational identities should be checked exactly where feasible; approximate numerical claims require justified tolerances and explicit assumptions. Sampling frequencies are observations, not proofs of a population probability, and an interval method must be named and qualified. A clean test report, correct guessed number or worked example memorized from this public course is insufficient without reasoning on equivalent unfamiliar values.

### Required summative assessments

- **SEF8-AS1** (required arithmetic, pre-algebra and the mathematical bridge)
  - Outcomes: SEF8-O1, SEF8-O2, SEF8-O3, SEF8-O18
  - Work: Begin with an ungraded starting-point diagnostic and identify any learning gaps; its result is neither an admission score nor a completion attempt. After suitable practice, demonstrate signed arithmetic, fraction addition, decimal/percentage conversion, ratio with units, powers, order of operations, a simple equation and inequality, and an input-output function table using unfamiliar but equivalent numbers. Show reasoning by hand or accessible digital work, check an equation by substitution and estimate whether answers are reasonable. Verify selected results with Python using fractions.Fraction for exact rational values. Include a wrong result and reasoned correction, a zero-denominator case and a function-table input outside a memorized example.
  - Criteria: All essential number-sense, signs, fractions/percentages, ratios/rates and units, powers, equations, inequalities and function-table skills are correctly demonstrated and explained. Exact rational work agrees with independently calculated values; invalid division is not silently accepted and rounding is not mistaken for an arithmetic identity. A learner needing more practice may reassess each missing essential category with new inputs and no fixed penalty or attempt limit. The ungraded diagnostic is **not** counted as a required summative test or a prerequisite to enrolling.
  - Evidence: Optional diagnostic and individualized practice notes (without grades), independent calculations and checks, unfamiliar readiness examples with reviewer decisions, Python source and outputs, invalid case and corrected misconception, and interpreter/version information.

- **SEF8-AS2** (required logic, counting, proofs and graph identities)
  - Outcomes: SEF8-O4, SEF8-O5, SEF8-O13, SEF8-O18
  - Work: Construct a truth table for implication and its equivalent negation/disjunction form; negate a quantified universal claim correctly. Calculate set union/intersection/difference and count ordered versus unordered selections, comparing hand-derived values against itertools enumeration for small fixtures including zero and overlarge selections. Give a complete induction proof that the sum of the first n positive odd integers equals n squared. Prove the handshaking identity for finite undirected simple graphs and verify it on a small graph enumeration. Supply a counterexample to one plausible false general claim and explain what finite computation does **not** prove.
  - Criteria: Logical rows, quantified negations, set memberships and counts agree with independent derivations, including a five-choose-two count of 10 versus 20 ordered pairs. The induction argument includes base case, hypothesis and valid induction step; the graph argument counts incidences under declared assumptions. A counterexample actually refutes the stated false claim. The learner separates an analytic proof or recurrence bound from finite examples, discusses the hypothesis and validity of any growth assertion, and handles invalid counting input visibly.
  - Evidence: Truth tables, formal or accessible proof steps, hand-worked set/count fixtures, Python enumerations and graph-degree checks, boundary/invalid tests, a false claim and counterexample, and revised reasoning after a diagnosed error.

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

- **SEF8-AS5** (required calculus, numerical differentiation and growth)
  - Outcomes: SEF8-O11, SEF8-O12, SEF8-O13, SEF8-O15, SEF8-O3
  - Work: Differentiate f(x)=x squared + 3x, evaluate f'(2), and compute the gradient of g(x,y)=x squared + 3xy at (1,2). Explain a suitable chain-rule example and the interpretation of an instantaneous rate of change. Implement forward and central finite differences and compare their errors across several positive step sizes with h=0 rejected. Discuss floating-point cancellation at very small h and justify numeric tolerances against analytic derivative values. Compare n log n and n squared for growing positive n and show an elementary recurrence argument with assumptions, without using timing as proof of an asymptotic class.
  - Criteria: The analytic results f'(2)=7 and gradient (8,3) are correctly derived. Finite differences approach the correct result for suitable scales, but no monotonic-improvement claim is made as h tends to zero in finite precision. Undefined steps and non-finite inputs are handled, exact/approximate reasoning is distinguished, and the chain-rule computation is correct. Growth claims use explicit asymptotic reasoning or a valid bound, not merely a plot or measured values. An intentionally incorrect derivative or numerical approximation is diagnosed and corrected.
  - Evidence: Analytic working, Python finite-difference source, h versus absolute-error table, tolerance and invalid-input tests, chain-rule and recurrence reasoning, corrected error trace and complexity explanation.

- **SEF8-AS6** (required sampling uncertainty and responsible statistical inference)
  - Outcomes: SEF8-O9, SEF8-O10, SEF8-O14, SEF8-O18
  - Work: For 60 successes in 100 independent Bernoulli trials, compute the sample proportion, plug-in standard error and explicitly labeled approximate 95% normal interval. State the independence, sample-size and approximation assumptions; identify when the method fails for extreme proportions or very small samples. Simulate repeated samples under a fixed seed for a known probability, recording estimated interval coverage across at least 1,000 replicates and discussing Monte Carlo variability. Deliberately bias a second sample, describe how that changes inference, and explain a p-value without equating it to the probability the null hypothesis is true. Distinguish observed association from an established causal effect.
  - Criteria: The sample proportion is 0.6; standard error is sqrt(0.6*0.4/100), approximately 0.049, and the labeled normal 95% interval is approximately [0.504,0.696]. Calculations use the declared approximate method and appropriately reject or qualify pathological/invalid cases. Coverage is reported as an empirical estimate without imposing a fabricated exact frequency; seeds, replicate count and biased selection mechanism remain inspectable. A confidence interval, p-value, bias and causal claim are interpreted according to their actual assumptions and limits.
  - Evidence: Hand calculations and formula, labeled interval code, declared random process and seed, repeated-run coverage output, bias comparison, invalid input cases, and a short explanation addressing uncertainty, p-values and causality.

- **SEF8-AS7** (required floating-point behavior and bounded gradient descent)
  - Outcomes: SEF8-O11, SEF8-O12, SEF8-O15, SEF8-O16, SEF8-O18
  - Work: Analyze finite-precision rounding and cancellation with an elementary numeric example. Implement f(x)=(x-3) squared, its analytic gradient and finite-difference approximation with valid positive h. Perform gradient descent from x0=0 using a documented positive learning rate, bounded iteration count and stop criteria, recording x, f(x) and the residual each iteration. Hand-compute the first two iterations at learning rate 0.25; compare runs at rates 0.1, 0.25, 1.0 and 1.1 under the same initial state. Reject nonfinite inputs, invalid rates, zero finite-difference step and a nonconverging run without an indefinite loop.
  - Criteria: At rate 0.25 the first updates are x1=1.5 and x2=2.25; for the stated function/runs, rate 1.0 oscillates 0↔6 and 1.1 diverges from the minimizer. The test records both a finite iteration budget and a justified convergence criterion; absence of convergence is reported as a bounded result, not success. Numerical errors, truncation and rounding are distinguished, no unqualified exact float equality is required, and invalid rates/inputs fail predictably. The learner explains the mathematical recurrence behind the observed stability or divergence.
  - Evidence: Analytic update derivation, Python optimizer and finite-difference source, multi-rate iteration logs with stop reasons, expected/actual tests including failures and edge cases, controlled precision/tolerance notes, and a corrected defect.

- **SEF8-AS8** (required integrated mathematical computing notebook and defense)
  - Outcomes: SEF8-O1, SEF8-O2, SEF8-O3, SEF8-O4, SEF8-O5, SEF8-O6, SEF8-O7, SEF8-O8, SEF8-O9, SEF8-O10, SEF8-O11, SEF8-O12, SEF8-O13, SEF8-O14, SEF8-O15, SEF8-O16, SEF8-O17, SEF8-O18
  - Work: Assemble previously assessed work into a documented offline Python notebook, script package or small library using standard-library fractions, itertools, math, statistics, random and unittest as appropriate. Include an exact fraction and simple equation/function table, truth/count or graph proof/counterexample, vector/matrix and singular-system check, conditional probability/statistical summary, uncertainty-aware seeded simulation, analytic/numerical derivative, and finite gradient-descent experiment. Reuse inspected source and results from earlier assessments rather than reimplementing every function. For each core operation, provide a hand-derived or otherwise independent normal-case oracle, a boundary/invalid case and explicit numeric precision or probability assumptions. Document one discovered flaw and its repair; have an independent reviewer follow a clean checkout and reproduce an unfamiliar normal and failing case, then defend a nontrivial design choice.
  - Criteria: The documented test command succeeds from a fresh environment with no paid or external service; every claimed capability is supported by inspectable artifacts and realistic independent reference values. Exact computations and approximate measurements are not conflated, and invalid assumptions or singular/undefined cases are not turned into plausible-looking numbers. All declared random work is repeatable by seed and includes evidence limits; mathematical statements are defended with reasoning rather than green tests alone. Any uncorrected foundational error or hidden dependency prevents passing. Independent reviewer observations and responses are documented.
  - Evidence: Portable source and clean-start README, exact interpreter/test commands, reused artifact-to-outcome matrix, hand-derived oracle table, normal and failing fixture results, uncertainty/precision settings, review notes and response, a diagnosed-and-fixed defect, and an accessible technical defense.

### Completion decision

All **eight required summative assessments** must meet their published criteria, collectively demonstrating SEF8-O1 through SEF8-O18. Lessons and optional practice support learning but do not add compulsory tests or labs. The ungraded entry diagnostic remains separate from the required pre-algebra mastery demonstration, and essential gaps may be remediated and reassessed without a fixed attempt cap. The final notebook may reuse prior verified calculations, functions and tests.

Reviewers preserve inspectable decisions and evidence tied to actual outcomes; serious mathematical, assumption, reproducibility or interpretation errors must be corrected. An explanation or technical defense may be submitted in accessible written, recorded, live or equivalent form using the same public criteria. The course itself remains `draft` pending the independent learner and reviewer evidence thresholds in [Status Labels](../../spec/status-labels.md).
