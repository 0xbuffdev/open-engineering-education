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

Use mathematics to explain and verify small numerical programs and to evaluate what their computed results can legitimately claim. Begin with domains, functions and limits; build dimensionally valid linear algebra; model probability before making statistical inferences; derive calculus results before numerically approximating them; then investigate floating-point errors and bounded gradient descent. Work from independently checkable derivations to Python computations, distinguishing exact identities, numerical approximations, statistical uncertainty and the limitations of finite evidence.

**SEF11 is the prerequisite**, providing arithmetic and algebraic fluency, logic, counting, proof, recurrence and graph reasoning for the numerical topics in this course. No separate entrance diagnostic is required here; mathematics support is available through formative review without an additional admission gate. SEF4 may proceed in parallel with SEF8 after SEF11, but both retain their own completion requirements.

Use Python 3.11+ and its standard library (`fractions`, `math`, `statistics`, `itertools`, `random`, `unittest`) alongside reviewable paper or accessible digital derivations. Paid books, proprietary assessment, NumPy, network services and other scientific packages are **not** required. Document calculation domains, platforms, actual commands, seeds, numeric tolerances and independent expected values.

The 12–14-week duration is provisional pending actual learner and reviewer calibration. Module and lesson boundaries follow distinct mathematical competencies and their prerequisites, not a preferred count. The six required assessments below measure those existing outcomes and may reuse earlier inspected calculations and code; their identifiers are intentionally nonconsecutive and do not imply missing exams. There is no mandatory quiz/lab quota per module or another hidden integrated project.

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

### Module 1 — Functions, Domains and Limits for Numerical Reasoning

#### Outcomes

- SEF8-O19
- SEF8-O3

#### Lessons

1. **What a numerical claim means** — Connect familiar SEF11 functions and arithmetic to real engineering uses such as rates, uncertainty and finite-precision calculations; distinguish an exact mathematical model from a Python result before assuming they agree.
2. **Domains and excluded inputs** — Evaluate polynomial and rational functions on declared domains, identify zero denominators, and give a counterexample when a function or composition is used outside its valid inputs.
3. **Algebraic equations and function composition** — Factor and solve simple equations with independent substitution checks; trace both stages of a composed function and reject an undefined intermediate value.
4. **Exponential growth and logarithms** — Apply exponent laws and inverse logarithm relationships with correct positive-argument restrictions, and distinguish a mathematical inverse from blindly reversing floating-point code.
5. **Graphs, secants and rates** — Calculate coordinates and finite secant slopes for a simple function; explain what the observed rate tells us and why a rate measured over an interval is not automatically a derivative at a point.
6. **Limits, continuity and algebraic justification** — Establish elementary polynomial/rational limits using a stated domain and algebra rather than just tables; distinguish the limit at a point from the value assigned at that point.
7. **Independent exact and approximate checks** — Use `fractions.Fraction` and selected `math` functions to compare hand-derived values with finite calculations, documenting invalid inputs and why rounded agreement does not prove a limiting claim.

*Optional practice:* Derive a small rational-function limit by simplifying on a punctured domain and independently check several nearby values without presenting the table as a proof.

### Module 2 — Linear Algebra, Systems and Transformations

#### Outcomes

- SEF8-O6
- SEF8-O7
- SEF8-O3
- SEF8-O18

#### Lessons

1. **Finite vectors and geometric meaning** — Represent a vector as an ordered list of coordinates in a declared space, perform componentwise addition and reject mismatched dimensions.
2. **Norms, distances and dot products** — Derive the Euclidean norm and dot product with independent numeric examples, distinguishing zero dot product/orthogonality from zero-length vectors.
3. **Matrices and valid multiplication** — State shape rules, calculate matrix-vector and rectangular matrix products, and detect ragged arrays or incompatible shapes before computing.
4. **Linear transformations and composition** — Interpret a matrix as a transformation of finite vectors, compare two transformations and show why reversing multiplication order can change the outcome.
5. **Elimination and unique solutions** — Work through a small nonsingular linear system using reversible row operations and independently verify the proposed solution in the original equations.
6. **Span, independence and basis** — Identify linearly dependent columns and construct a small basis by explicit linear-combination reasoning, not by counting coordinates alone.
7. **Rank and nonzero null vectors** — Find rank deficiency and a witness for the homogeneous null space, distinguishing a singular coefficient matrix from a necessarily inconsistent system.
8. **Inconsistent versus underdetermined systems** — Compare two systems with the same singular coefficient matrix but different right-hand sides; identify no solution versus infinitely many and reject a false unique-solution claim.
9. **Simple eigenpairs and substitution** — Verify an eigenvector and eigenvalue for a small diagonal matrix by direct multiplication; identify why a zero vector is not an eigenvector.
10. **Exact versus approximate linear-system checks** — Use small `fractions.Fraction` examples and labeled float approximations to show how rounding or input perturbation can affect a computed answer; state a justified tolerance rather than assuming numerical agreement proves uniqueness.

*Optional practice:* For a singular 2×2 matrix, exhibit a nonzero null vector, one consistent right-hand side and one inconsistent right-hand side, and independently check each claim.

### Module 3 — Probability, Random Variables and Descriptive Statistics

#### Outcomes

- SEF8-O8
- SEF8-O9
- SEF8-O14
- SEF8-O3

#### Lessons

1. **A finite probabilistic model** — Define events and an explicit sample space, calculate normalized probabilities with nonnegative weights, and separate an assumed model from observed frequencies.
2. **Conditional probability and impossible conditions** — Compute conditional event probabilities from a finite table, check the denominator and report conditioning on a zero-probability event as undefined rather than zero.
3. **Independence and dependent evidence** — Test the independence identity using actual values and show why assuming independence without support changes a computed posterior.
4. **Bayes' rule and base rates** — Derive a posterior from prevalence, sensitivity and false-positive rates using a joint-probability table, then challenge a tempting base-rate fallacy.
5. **Discrete random variables and distributions** — Construct a probability mass function on finite outcomes, validate support and total mass, and distinguish an outcome from the probability assigned to it.
6. **Expectation, variance and spread** — Derive a mean and population variance from a finite distribution; distinguish variability in outcomes from uncertainty about an estimated parameter.
7. **Descriptive data versus sampling estimators** — Compute the mean, population variance and sample variance of a small actual list using the correct denominator, checking against `statistics` and handling empty/one-element cases.
8. **Reproducible two-stage simulation** — Model a conditional synthetic test using explicit draws, a seed and a recorded contingency table; compare empirical frequencies with analytic probabilities without demanding exact equality across random trials.

*Optional practice:* Independently derive the expected positive-test posterior for a low-prevalence condition and reproduce the table using a fixed-seed Python simulation.

### Module 4 — Sampling Uncertainty and Responsible Statistical Inference

#### Outcomes

- SEF8-O9
- SEF8-O10
- SEF8-O14
- SEF8-O18

#### Lessons

1. **Population, sample, estimand and selection** — Distinguish what a population parameter means from a sample estimate, identify selection bias and explain why a large biased sample does not automatically solve the problem.
2. **Sampling variation and standard errors** — Derive the plug-in standard error of a Bernoulli sample proportion from its stated independent-trials model, separating standard deviation of observations from uncertainty in the estimator.
3. **An explicitly approximate 95% proportion interval** — Compute the elementary normal/Wald interval using a supplied approximate critical value of 1.96; state its assumptions and distinguish it from a guaranteed or exact interval.
4. **Coverage and boundary failures** — Simulate repeated independent samples and count how often a declared interval procedure covers the known probability; investigate extreme proportions or tiny samples where the normal approximation can be misleading.
5. **Hypothesis tests and p-value meaning** — Under a precisely specified null model, interpret a p-value as tail probability for a statistic at least as extreme, not as the probability that the null is true.
6. **Dependence, confounding and causal limits** — Compare an observational association with a justified causal statement, identify a selection or confounding mechanism and explain what randomization can and cannot establish in a bounded experiment.
7. **An inspectable inference report** — State the estimand, sampling process, approximation, seed, known bias, observed counts, interval/p-value interpretation and limits in an unfamiliar synthetic case with independent review.

*Optional practice:* Compute the 60-of-100 Bernoulli estimate and its explicitly approximate interval, then vary the sampling scheme to show why a correct formula does not repair biased selection.

### Module 5 — Analytic Calculus and Continuous Accumulation

#### Outcomes

- SEF8-O19
- SEF8-O20
- SEF8-O11
- SEF8-O3

#### Lessons

1. **Derivative as a limiting rate** — Connect the earlier secant slopes to a difference quotient and elementary limit; explain why finite observations support but do not prove the tangent slope.
2. **Derivative rules and justified substitutions** — Differentiate elementary polynomials and exponential functions and check answers with explicit analytic identities and valid domains.
3. **Chain rule and composed functions** — Derive the derivative of a meaningful composition, distinguish inner and outer changes, and locate an error in a plausible but incorrect chain-rule step.
4. **Partial derivatives and gradients** — Hold the other variable constant when differentiating a two-variable function, compute a gradient and interpret its components as local rates in the input directions.
5. **Directional change and gradient meaning** — Use a small two-variable example to connect a gradient with a first-order change and a steepest-ascent direction in Euclidean coordinates, not a blanket claim of global optimization.
6. **Riemann sums and signed accumulation** — Form and interpret finite rectangles, compare signed and unsigned contributions and explain why a definite integral represents the limit of sums under appropriate assumptions.
7. **Antiderivatives and a definite integral** — Verify an elementary antiderivative by differentiation and use the fundamental theorem to evaluate a simple bounded integral independently.
8. **Continuous probability density** — Define a nonnegative density with unit total area, calculate interval probability by integration, and explain why density at a point is not the probability of that exact point.

*Optional practice:* Derive the derivative and integral of simple polynomials by hand, then identify what a finite-difference or finite-sum check can validate without replacing the proof.

### Module 6 — Floating-Point Reliability, Numerical Gradients and Optimization

#### Outcomes

- SEF8-O3
- SEF8-O11
- SEF8-O12
- SEF8-O15
- SEF8-O16
- SEF8-O18

#### Lessons

1. **Binary floating-point is approximate** — Explain why many decimal fractions cannot be represented exactly in a finite binary format; compare `Fraction` with `float` and reject invalid or nonfinite numerical inputs.
2. **Rounding, cancellation and safe comparisons** — Diagnose subtractive cancellation, failed exact-equality expectations and scale-sensitive tolerances, stating when relative and absolute thresholds are justified.
3. **Forward finite differences** — Derive a difference quotient for a known analytic derivative, specify `h > 0` and compare approximation error over meaningful positive steps.
4. **Central differences and truncation behavior** — Derive the symmetric formula and compare the leading truncation behavior with forward differences for sufficiently smooth functions, without claiming that the smallest representable step is always best.
5. **Rounding-versus-step-size trade-off** — Observe decreasing truncation error followed by cancellation/roundoff deterioration where applicable, recording actual numeric ranges and invalid-step behavior without inventing a universal optimal step.
6. **Gradient components and numerical checks** — Approximate partial derivatives by varying one coordinate at a time, compare with a hand-derived analytic gradient, and account for function domains and independently justified tolerances.
7. **Gradient descent as a state recurrence** — Define the objective, gradient, positive learning rate, update rule and initial state for a bounded one-variable quadratic, deriving the first updates by hand before execution.
8. **Convergence, oscillation and divergence** — Analyze the update multiplier for a simple quadratic, show why a stable rate approaches the minimizer, a boundary rate oscillates and an excessive rate diverges; relate the claim to the actual initial condition.
9. **Stop contracts and honest failure reporting** — Enforce finite iteration budgets, nonfinite/invalid-input rejection and explicit convergence or nonconvergence status; reproduce one defect and defend why a green numeric test does not prove global convergence.

*Optional practice:* Compare a hand-derived two-step descent trace with actual runs at stable, oscillating and diverging learning rates, recording why each stopped.

### Module 7 — Integrated Numerical Work and Independent Defense

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

1. **Reuse existing derivations and code** — Gather the six published assessment artifacts into one navigable offline numerical notebook or small standard-library package without creating another independent project.
2. **Independent exact and approximate oracles** — Link function/domain, matrix/system, probability, calculus and descent claims to hand calculations or separately derived references, labeling every numerical tolerance.
3. **Invalid-input and failure contracts** — Reproduce singular/ragged matrix, impossible conditioning, empty sample, invalid derivative step, nonfinite value and nonconvergent optimization behavior with meaningful errors.
4. **Seeded experiments and uncertainty records** — Preserve actual random seeds, sample counts, stated estimands, assumptions, interval/coverage observations and known limitations instead of claiming simulated frequencies equal exact probabilities.
5. **Clean-start and accessible mathematical communication** — Document Python version, standard-library commands, input fixtures, proofs, tables and optional diagrams with an equally accessible text explanation and outcome-to-evidence map.
6. **Independent unfamiliar challenge and defense** — Give an independent reviewer one bounded new normal and failing case, record the actual reproduced results, diagnose a discrepancy and defend what the mathematics, tests and finite measurements can legitimately establish.

*Optional practice:* Ask a reviewer to change a matrix, a sampling assumption or a learning rate, predict the impact analytically and then compare it with actual standard-library results.

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
