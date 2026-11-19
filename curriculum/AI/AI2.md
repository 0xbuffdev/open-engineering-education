# AI2 — Mathematics of Statistical and Neural Models

**Program:** AI — AI Engineering
**Type:** course
**Prerequisites:** [AI1](AI1.md) — Scientific Computing & Data Engineering for AI (completed)
**Duration:** 16–20 weeks
**Status:** draft
**Specification:** v0.2.0
**Expected workload:** 10–15 focused hours/week (provisional; approximately 160–300 focused hours)

> [AI Engineering](README.md) · [Curriculum design guide](../DESIGN-GUIDE.md) · [Course format](../../spec/course-format.md) · [Evidence rules](../../spec/evidence-rules.md)

## Overview

**AI2 develops the mathematics needed to explain, derive, diagnose and defend learning-model objectives, rather than merely operate a machine-learning package.** Learners connect an explicit statistical model and a declared sample-generating process to a loss function, likelihood, parameter geometry, gradients, uncertainty, regularization and a computationally feasible optimization method. They must be able to distinguish a correct symbolic derivation from a numerically stable implementation and distinguish an optimized objective from evidence of a valid statistical claim. These are the quantitative prerequisites for AI4's statistical machine-learning comparisons and AI5's deep-network optimization, not substitutes for either specialized course.

**Where this subject fits.** Mathematical models of data precede modern machine learning: least squares connects observations to parameter estimation, likelihood connects probabilistic assumptions to objectives, regularization constrains fit, and gradient-based methods support optimization at scale. Differentiable computational graphs and numerical linear algebra make these ideas applicable to neural models, but automatic differentiation and hardware acceleration do not erase assumptions, conditioning or statistical uncertainty. This course asks learners to derive what an optimization result means and identify when the result has little evidential value.

**Prerequisite boundary.** All eleven SEF courses are already completed before entry into AI through SEF10; AI1 additionally assesses scientific arrays, sample identity, tabular semantics, provenance, leakage-resistant partitions and reproducible data pipelines. Apply **SEF8** functions, probability, Bayes' rule, elementary continuous density/integration, vector/matrix products, rank, partial derivatives, gradients, chain rule, floating-point and introductory gradient descent; do **not** re-teach elementary arithmetic, calculus or Python. AI2 develops **new** claims: design matrices and identifiability; model-specific derivatives/Jacobians; likelihood-based estimators and priors; posterior uncertainty; proper probabilistic objectives; mathematical regularization and optimizer diagnostics. Do not repeat AI1's parsing, plotting, join/cardinality investigations or split mechanics.

**Deliberate exclusions.** AI2 does not teach the full library of supervised learners, trees, ensembles, cross-validation or model selection (AI4); backward propagation through large learned networks, architectures or tensor training loops (AI5); reinforcement learning (AI6); generative transformer design (AI9); model-serving optimization (AI15); or production safety/governance (AI14). A small one-layer differentiable map is used for mathematical reasoning, **not** as a compulsory neural-network training project. No APP or SYS course is a prerequisite for AI2.

**Access, safety and reproducibility.** Use paper or accessible digital derivations plus local Python 3 with standard-library arithmetic and NumPy when useful; a small automatic-differentiation package is optional only for verification, never an authority for the expected answer. Reference cases fit on an ordinary CPU. Synthetic data, documented independent computations, free software and written/table-based visual equivalents must suffice. No GPU, specialized cloud, paid textbook, model API, private dataset or hidden grading service is required. Specify math conventions, numeric precision, tolerances, seeds and the limits of each example. Fractions or hand derivations are preferable where an exact reference is possible. A sufficiently explained counterexample or well-defended negative result is valid mathematical work.

**Assessment philosophy and pacing.** The modules follow the mathematical dependencies from model definition and derivation to probabilistic reasoning, optimization, uncertainty and independent defense. Lesson boundaries keep mechanisms, counterexamples and checks together rather than treating every error case or presentation stage as another subject. Five cumulative required assessments separately judge matrix/objective reasoning, probabilistic inference, stable scoring/uncertainty, optimizer and regularization behavior, and unfamiliar independent mathematical defense. Worked traces and optional formative problems support understanding without separate compulsory per-module tests or labs. The 16–20-week estimate covers derivation, coding, debugging, counterexamples, assessment, explanation and revision at 10–15 focused hours/week; it is provisional until genuine learner evidence supports calibration. Status remains draft; source checks are not educational verification.

## Learning outcomes

- **AI2-O1:** Translate a bounded prediction or estimation question into observations, feature and target variables, parameter spaces, model assumptions and the limits of the intended mathematical claim.
- **AI2-O2:** Construct and reason about design matrices, linear/affine predictors, vector and matrix dimensions, ranks and parameter identifiability, including ambiguous or incompatible cases.
- **AI2-O3:** Derive and independently check gradients, Jacobians, Hessians or relevant directional derivatives for elementary statistical and one-layer differentiable objectives, applying correct chain and matrix-calculus rules.
- **AI2-O4:** Define empirical objectives, loss scales, weighting and reduction conventions, and show how a changed objective or denominator alters parameter updates and interpretations.
- **AI2-O5:** Formulate likelihood and negative log-likelihood from explicit conditional sampling assumptions; derive simple maximum-likelihood estimates and demonstrate when the assumptions fail.
- **AI2-O6:** Construct and interpret a small Bayesian posterior and posterior-predictive calculation, with transparent prior, likelihood, support and limits; compare MAP to MLE without equating them.
- **AI2-O7:** Derive and interpret entropy, cross-entropy, KL divergence and stable log-domain computations for finite distributions, disclosing zero-probability and support constraints.
- **AI2-O8:** Connect regression/classification losses to probability models and scoring incentives, distinguish scores, likelihoods and probabilities, and explain why optimization of a proper loss alone does not guarantee calibrated deployment predictions.
- **AI2-O9:** Implement and analyze first-order optimization with justified derivatives, step sizes, stopping decisions, independent gradient checks and demonstrable stable/unstable cases.
- **AI2-O10:** Analyze curvature, conditioning, stationary points and optimizer failure using small matrix/Hessian examples, distinguishing convex guarantees from unsupported nonconvex claims.
- **AI2-O11:** Formulate and evaluate parameter constraints, explicit regularization and equivalent probabilistic interpretations where valid, explaining the effects of scale, penalty placement and bias/variance trade-offs.
- **AI2-O12:** Distinguish parameter uncertainty, sampling variability, objective curvature, model misspecification and distribution shift; identify which inferences are unsupported by a fitted point estimate.
- **AI2-O13:** Construct a clean-state reproducible mathematical investigation whose independent symbolic/numeric oracles and negative cases establish the stated computations rather than treating tool output as proof.
- **AI2-O14:** Diagnose and repair an unfamiliar bounded model/objective/optimizer defect, independently verify a new case and defend the mathematical assumptions and unresolved limitations.

## Modules

### Module 1 — Learning Problems as Mathematical Contracts

#### Outcomes

- AI2-O1
- AI2-O4
- AI2-O12

#### Lessons

1. **Modeling versus data description** — Turn an AI1-certified dataset into a conditional quantitative question; define which variables are observations, decisions, targets, features and latent assumptions. Explain why a data-quality report is necessary but insufficient for statistical inference.
2. **Population, sampling process and model family** — Specify the target population, how records become observations and which modeled relationship is assumed; distinguish a convenient function class from a causal or probabilistic statement.
3. **Parameter, prediction and estimand** — Separate a model parameter, fitted estimate, predicted quantity and scientific population target, using a small linear prediction as a concrete trace.
4. **Costs, losses and scientific objectives** — Identify why squared error, absolute error and log-loss encode different judgments about errors. Define weights, reductions and whether the objective sums or averages losses.
5. **Trainable quantity versus fixed convention** — Mark intercepts, transformed features, selected fixed constants and constraints. Identify when a choice of units or loss normalization changes the meaning of a learning-rate value.
6. **Assumptions and falsifying examples** — Define two observable cases that would challenge independence, noise shape, a linear mean relationship or a fixed label interpretation, while distinguishing a violated mathematical assumption from a bad CSV parse.

*Optional feedback:* Given repeated measurements per subject, specify the target prediction, parameter and statistical assumption at risk; do not reimplement AI1's partitioning exercise.

### Module 2 — Linear Model Geometry and Identifiability

#### Outcomes

- AI2-O1
- AI2-O2
- AI2-O10

#### Lessons

1. **Design-matrix and affine-map semantics** — Represent n observations and d feature coordinates as an n-by-d design matrix; trace predictions, parameter dimensions, intercept columns and single-record evaluation. Distinguish a linear map from an affine predictor, explain what happens when an intercept is omitted or penalized, and reject an incompatible matrix product before trusting a NumPy result.
2. **Column space and projection** — Interpret a least-squares fit as choosing a model prediction inside the span of the observed feature columns, distinguishing what can be represented from what is statistically justified.
3. **Normal-equation reasoning** — Derive the stationary condition for finite least squares with correct dimensions, including when a closed-form unique solution exists; do not present an unstable matrix inverse as the preferred numerical algorithm.
4. **Rank deficiency and nonidentifiability** — Construct collinear features, a duplicate intercept and a truly redundant column; exhibit distinct coefficient vectors with the same predictions. Distinguish parameter identifiability from a fitted prediction and use an explicit null direction to diagnose the failure, not just a solver warning.
5. **Scaling and ill-conditioning** — Show how meters versus millimeters and a zero-variance feature affect the design and numerical conditioning; predict when an optimizer trace or parameter interpretation changes without changing the underlying observations.
6. **Solving without explicit inversion** — Interpret residuals and compare a transparent small least-squares result with QR or SVD, including well-conditioned and singular inputs. Explain which shape or rank assumption is required before accepting a solution and why blindly inverting X-transpose-X is unsound.

### Module 3 — Derivatives of Statistical and One-Layer Objectives

#### Outcomes

- AI2-O3
- AI2-O4
- AI2-O9
- AI2-O10

#### Lessons

1. **Scalar objectives over parameter vectors** — Trace a map from parameter vector to predictions to residuals to a scalar objective, explicitly naming the shapes of each intermediate.
2. **Jacobian orientation and matrix conventions** — Compute the Jacobian of a small affine map, choose a row/column convention and show that consistent notation prevents apparently valid dimension mistakes.
3. **Squared-error gradient and scale checks** — Derive the gradient of J(theta) = (1/(2n)) ||X theta - y|| squared and verify it against a hand-calculable fixture. Trace a wrong denominator, reversed sign or axis swap to the incorrect update rather than relying on a successful broadcast.
4. **Hessian and directional curvature** — Derive X-transpose-X/n for the same objective; use a nonzero direction to interpret local quadratic curvature and the effect of a singular design.
5. **Chain rule for composed mappings** — Differentiate a small affine-plus-elementwise-nonlinearity map with a scalar loss. Identify the proper Jacobian-vector or vector-Jacobian product and locate a missing chain factor or incompatible intermediate shape before an autodiff check.
6. **Finite-difference gradient checks and failure diagnosis** — Compare analytic gradients with central finite differences across justified step sizes. Diagnose truncation, cancellation, incorrect reductions or regularization of the wrong parameter using independent expected values rather than treating one numerical match as proof.
7. **Nondifferentiability and subgradients** — Explain the absolute-error cusp and simple piecewise activations, the conditions under which a subgradient is useful and what smooth-gradient assumptions do not apply.

*Optional feedback:* For the public three-row design matrix at theta = (0,1), predict the mean half-squared-loss gradient before using a library. Then alter one observation weight or add one feature and defend the new gradient and intermediate shapes against a hand-computed reference.

### Module 4 — Likelihoods, Estimators and Statistical Assumptions

#### Outcomes

- AI2-O1
- AI2-O4
- AI2-O5
- AI2-O8

#### Lessons

1. **Conditional likelihood is a model of observations** — Distinguish p(data | parameters) from a posterior p(parameters | data), explain what is held fixed during maximization and identify the support of the assumed distribution.
2. **Bernoulli and categorical observations** — Derive the likelihood and log-likelihood for independent binary observations and identify why a probability of exactly zero can invalidate a claimed positive observation.
3. **Gaussian measurement model** — Derive squared-error-like negative log-likelihood from independent Gaussian noise with specified variance; explain how unequal variances change weighting.
4. **MLE for simple families** — Derive the Bernoulli success proportion and the Gaussian sample mean under their assumptions; inspect boundary cases and the effect of correlated records.
5. **Logistic link and binary cross-entropy** — Derive sigmoid likelihood and the binary log-loss from a linear score; compute the derivative with respect to a logit at zero without assuming a model library.
6. **Weights, imbalance and objective meaning** — Explain why class weighting, sample weighting or averaging conventions change the estimand or trade-off; distinguish a mathematically minimized reweighted objective from a calibrated population probability.
7. **Misspecified likelihoods and invalid comparisons** — Construct a heavy-tail or dependent-observation case in which Gaussian or iid likelihood assumptions fail. Explain why a higher maximized training likelihood cannot, on its own, establish better out-of-sample prediction; actual model selection and empirical generalization belong to AI4.

### Module 5 — Priors, Posteriors and Predictive Uncertainty

#### Outcomes

- AI2-O5
- AI2-O6
- AI2-O12

#### Lessons

1. **From Bayes' rule to estimation** — Extend SEF8's probability calculation to an unknown parameter with an explicitly stated prior, likelihood, normalization and conditional interpretation.
2. **Discrete posterior by enumeration** — Compute posterior weights for a small finite hypothesis set and verify that the probabilities normalize; distinguish prior preference from impossible likelihood.
3. **Beta–Bernoulli update** — Derive the posterior shape parameters and predictive probability for bounded coin-observation data; check zero observations and the effect of nonuniform priors.
4. **Posterior mean, mode and MLE** — Explain why these quantities can differ, including at boundaries. Do not report an undefined boundary mode using an interior formula that assumes shape parameters greater than one.
5. **MAP as penalized estimation** — Demonstrate a legitimate connection between Gaussian parameter priors and squared L2 penalties under a declared likelihood scale, while explaining dependence on parameterization and prior variance.
6. **Uncertainty is not a single score** — Distinguish posterior spread, uncertainty from finite samples, predictive noise and possible model misspecification; identify which requires assumptions not supplied by the fixture.
7. **Prior sensitivity, dependence and auditable inference** — Compare justified priors on a small dataset and explain why correlated observations need not provide the advertised independent information. Report the posterior, predictive result, assumptions, a checkable counterexample and the exact uncertainty claim an independent reviewer can verify without a probabilistic-programming service.

### Module 6 — Information Measures and Probabilistic Scoring

#### Outcomes

- AI2-O7
- AI2-O8
- AI2-O12

#### Lessons

1. **Self-information and units** — Define negative log probability, distinguish nats from bits and specify the behavior when an event is assigned zero probability.
2. **Entropy of a discrete distribution** — Compute Bernoulli entropy, justify the 0 log 0 limit and compare certainty with maximum uncertainty on an explicitly finite support.
3. **Cross-entropy and mismatch** — Compute expected log-loss of one distribution under another and explain why a predicted distribution different from the reference incurs excess loss.
4. **KL divergence and support** — Calculate a small exact KL expression, interpret nonnegativity and asymmetry, and explain when KL becomes infinite because the reference assigns positive probability where the comparator assigns zero.
5. **Proper scores and honest probabilities** — Demonstrate on a finite Bernoulli example why expected log loss is minimized at the true probability under the stated data-generating assumptions; distinguish this result from an empirical guarantee for one small dataset.
6. **Stable log-domain computation** — Compare naïve softmax and log-sum-exp or softplus with numerically stabilized forms. Examine ±1000 logits, avoiding overflow and cancellation while retaining the mathematical objective.
7. **Calibration and threshold distinction** — Distinguish a probability forecast, its loss, a decision threshold and an action cost; explain why discrimination, proper scoring, empirical calibration and a business decision cannot be reduced to one unqualified accuracy number.

*Optional feedback:* For a fair binary event, compare predictions p = 0.5 and p = 0.9 with expected log-loss by hand; state when the comparison reverses for a different true event probability.

### Module 7 — Optimization Dynamics and Numerical Failure

#### Outcomes

- AI2-O3
- AI2-O9
- AI2-O10
- AI2-O13

#### Lessons

1. **Gradient descent as a discrete update** — Derive one step of theta-next = theta - eta gradient J; identify which part is a mathematical objective and which part is an algorithm choice.
2. **Step size on quadratic objectives** — Use a one-dimensional convex quadratic to demonstrate convergence, oscillation and divergence; relate a safe constant step-size bound to actual curvature in that example only.
3. **Full-batch and stochastic gradients** — Differentiate an exact full-data gradient from an unbiased stochastic estimate under appropriate sampling; explain variance, minibatches and why equal gradient expectations do not imply identical traces.
4. **Momentum as stateful dynamics** — Trace a two-step momentum method for specified initialization and coefficients; show how state can improve or destabilize behavior without treating hyperparameters as universal.
5. **Adaptive scaling limitations** — Explain coordinatewise adaptive updates and their dependence on gradient magnitude history; compare on a toy ill-scaled objective rather than asserting Adam always converges or outperforms alternatives.
6. **Stationary points and nonconvex structure** — Compare minima, maxima, saddles and flat regions; use a simple nonconvex scalar example to show why zero gradient is not proof of a useful global solution.
7. **Condition numbers and update geometry** — Investigate a positive definite quadratic with differently scaled eigen-directions; justify why a step suited to one direction may be unstable in another.
8. **Stopping criteria and numerical failure diagnostics** — Contrast gradient norm, step norm, objective improvement and fixed iteration counts. Detect premature stopping, nonfinite losses, wrong-sign or stale gradients, missing reduction scales and incompatible shapes with independent expected values; implement a safe failure or refusal rather than reporting convergence from a successful autograd call.

### Module 8 — Regularization, Constraints and Model Stability

#### Outcomes

- AI2-O2
- AI2-O10
- AI2-O11
- AI2-O12

#### Lessons

1. **Ill-posed fits, ridge penalties and MAP assumptions** — Start from multiple parameter vectors with equal observed predictions; derive the squared-loss plus L2 penalty gradient and stationary point and state whether the intercept is penalized. Where appropriate, connect a Gaussian prior to the resulting MAP objective under an explicit likelihood scale, and identify how units, prior variance or normalization invalidate an unqualified equivalence.
2. **L1, sparsity and nondifferentiable objectives** — Explain the absolute-value penalty and why a zero coefficient/subgradient differs from smooth ridge shrinkage; no generic solver package survey is needed.
3. **Constraints and projected updates** — Work a bounded parameter example with feasible sets and projection; show a step that must be corrected to meet the declared constraint.
4. **Feature scaling and parameter meaning** — Compare penalty effects before and after a deterministic unit transformation and justify when normalization or domain-informed regularization is defensible.
5. **Bias, variance and underfitting** — Analyze why a penalty can reduce sensitivity but introduce bias; use a small controlled simulation to identify limited observed behavior without claiming general proof of predictive improvement.
6. **Ill-conditioning versus lack of identification** — Build a nearly collinear example and a truly rank-deficient example; explain why a regularized unique solution does not magically identify parameters from the data alone.

### Module 9 — Evidence, Generalization Boundaries and Model Claims

#### Outcomes

- AI2-O1
- AI2-O4
- AI2-O11
- AI2-O12
- AI2-O13

#### Lessons

1. **Empirical risk versus population risk** — Define the two mathematical objects and the assumptions required to connect them; explain why the observed minimum does not identify the population optimum.
2. **Dependence, reweighting and representativeness** — Analyze an example with repeated related observations and unequal sampling where naïve iid or uniform weighting overstates information or misrepresents the intended population.
3. **An optimized objective is not a validated claim** — Contrast a correctly minimized training loss with incorrect label semantics, dependent sampling, a wrong likelihood, poor held-out behavior and a shifted population. State which new model-selection and deployment claims belong to later AI courses rather than importing their deliverables into this mathematical investigation.
4. **Uncertainty from finite experiments** — Use reproducible repeated synthetic samples to estimate observed variability; disclose simulation assumptions and avoid claiming an actual confidence bound from a convenient empirical trace alone.
5. **Mathematical evidence and counterexamples** — Decide what is established by a proof, exact finite fixture, numerical approximation or randomized trial and what remains unresolved.

### Module 10 — Integrated Derivation, Reproduction and Defense

#### Outcomes

- AI2-O1
- AI2-O3
- AI2-O4
- AI2-O5
- AI2-O6
- AI2-O7
- AI2-O8
- AI2-O9
- AI2-O10
- AI2-O11
- AI2-O12
- AI2-O13
- AI2-O14

#### Lessons

1. **Frame one auditable mathematical investigation** — Select one or two bounded synthetic least-squares and probabilistic questions, declare assumptions, and construct independently known hand-derived gradients, exact numerical reference values and a tiny transparent implementation. Distinguish exact checks from finite-precision comparisons before inspecting the implementation.
2. **Predict, reproduce and correct a mathematical failure** — Introduce rank deficiency, a wrong reduction, impossible likelihood, unstable log expression or mis-scaled update. Predict its failure signature from the stated mathematics, reproduce it with independent reference values, and defend the corrected objective or algorithm against the original baseline and its limits.
3. **Answer an unfamiliar bounded challenge** — Adapt the source to a reviewer-changed feature, loss scale, prior or constraint; re-derive the relevant result rather than editing parameters until a test passes.
4. **Independent technical explanation** — Defend assumptions, signs, shapes, objective scales, numerical validity, support constraints, uncertainty and the difference between mathematical fit and trustworthy AI competence.

The modules are a learning sequence, **not ten mandatory assessment submissions**. Optional prompts, explanations, worked examples and practice traces are formative. Every required assessed performance is defined below.

## Completion requirements

### Public reference cases and evaluation conventions

The following small fixtures anchor the required mathematical checks. Alternative learner-owned fixtures are acceptable if their exact expected values, failure cases and evaluation criteria are equally explicit. An assessor may supply bounded unseen numeric variants while preserving these public criteria.

**Linear objective fixture L1.** For x = (1, 2) and targets y = (2, 4), use the one-parameter predictor y-hat_i = theta x_i and mean half-squared error J(theta) = [sum_i (theta x_i - y_i)^2]/(2n), with n = 2. Exactly, J(theta) = (5/4)(theta - 2)^2; gradient J-prime(theta) = (5/2)(theta - 2); Hessian J-double-prime(theta) = 5/2. At theta = 0, J = 5 and gradient = -5; one step with eta = 1/5 yields theta = 1 and J = 5/4. Constant-step gradient descent converges for 0 < eta < 4/5 on this quadratic; eta = 4/5 oscillates without convergence from a non-optimal start, and eta > 4/5 diverges (absent the exact optimum). A separate L2 penalty lambda theta-squared/2 with lambda = 1 changes the optimum to theta = 10/7; explain the altered objective rather than substituting the unpenalized answer.

**Design-matrix fixture L2.** X is the 3-by-2 matrix with rows (1,0), (1,1), (1,2); y is (1,2,3), and theta is initially (0,1). Define J = ||X theta - y|| squared/(2n), n = 3. Predictions are (0,1,2), residuals are (-1,-1,-1), J = 1/2, and gradient = X-transpose(X theta - y)/3 = (-1,-1). The Hessian is X-transpose X /3 = [[1,1],[1,5/3]], positive definite because its determinant equals 2/3. A step with eta = 1/10 yields theta = (1/10,11/10) and J = 97/300. Duplicate the second column as a third feature to produce a rank-deficient design with multiple parameter vectors giving the same predictions; an inverse of X-transpose X is then unjustified. Numeric reference work must explicitly distinguish exact rational checks from approximate floating-point output.

**Probabilistic fixture P1.** For independent Bernoulli trials with a Beta(2,2) prior and observations of three successes and one failure, the posterior is Beta(5,3) and the next-trial posterior-predictive success probability is 5/8. The Bernoulli MLE is 3/4; the interior MAP estimate under the specified prior is (5-1)/(5+3-2) = 2/3. State what each figure means and why the four observed trials do not justify certainty or exchangeability under unexamined conditions.

**Probabilistic fixture P2.** With a binary target y = 1 and logit z = 0, sigmoid(z) = 1/2; binary logistic negative log-likelihood is log 2 and derivative with respect to z is -1/2. For distribution p = (3/4, 1/4) versus q = (1/2, 1/2), KL(p||q) = (3/4) ln(3/2) + (1/4) ln(1/2), approximately 0.130812 nats. Explain why the reversed KL differs. Stable softplus(z) = max(z,0) + log(1 + exp(-abs(z))) must remain finite for z = +1000 and z = -1000 (with ordinary finite IEEE-754 doubles), whereas direct log(1 + exp(1000)) is not a safe formula. Logits of magnitude 1000 are a **numerical stress case**, not realistic evidence of population probabilities or calibration.

**General evaluation rules.** A correct answer must state the adopted mathematical convention. Scores, log probabilities and likelihoods cannot be substituted for one another; likelihood is not a probability distribution over parameter values without an explicit prior/normalization. An autodiff result or successful numerical solver **cannot** replace an independent derivation where reasoning is assessed. No commercial service, substantial GPU computation, third-party private grader, or real personal data may be compulsory. Required code must run from a clean documented local environment. Small symbolic work may be submitted as accessible text, handwritten derivation digitized legibly, or equivalent reviewable form.

### Required summative assessments

- **AI2-AS1** (required model geometry and objective derivation)
  - **Outcomes:** AI2-O1, AI2-O2, AI2-O3, AI2-O4, AI2-O10.
  - **Work:** Define a concrete estimation question with observation/feature/parameter meanings; work both L1 and L2 from the published independent references. Derive predictions, gradient, Hessian, dimensions and the single-step result. Introduce an intercept or duplicate feature to show a rank-deficient case; propose a defensible numerical solution strategy and explain limits of parameter identification. Include a wrong reduction or dimensional-case counterexample and its corrected derivation.
  - **Criteria:** Hand-derived L1 objective, derivative, curvature, exact update and ridge optimum match the published results; L2 residual, gradient, Hessian, determinant and updated loss agree within justified arithmetic tolerance; shape and rank claims are correct; the singular construction has a clearly exhibited nonzero null direction or multiple equivalent parameter vectors. One unexplained solver output or numeric coincidence does not pass the derivation requirements.
  - **Evidence:** Reviewable mathematical derivation and dimensional trace, source or transparent reference calculation, independent expected values, a normal and invalid/rank-deficient case, and a brief statement of assumptions and nonidentifiability.

- **AI2-AS2** (required likelihood and posterior inference)
  - **Outcomes:** AI2-O1, AI2-O5, AI2-O6, AI2-O12.
  - **Work:** Specify a Bernoulli observation model, justify the likelihood, derive MLE, use the P1 Beta prior to calculate the posterior and posterior-predictive probability, and distinguish the posterior mean, mode/MAP and MLE. Extend the example to a prior sensitivity comparison or a dependent-observation counterexample. Derive a Gaussian mean likelihood from a small separately defined independent fixture and explain its squared-loss relationship.
  - **Criteria:** P1 yields posterior Beta(5,3), mean/predictive 5/8, MLE 3/4 and MAP 2/3 with clearly named assumptions; Gaussian negative log-likelihood is derived up to parameter-independent constants, not asserted by memorization; boundary or dependence counterexample is valid; posterior uncertainty is not mistaken for guaranteed coverage under misspecification. Prior and likelihood are not interchanged.
  - **Evidence:** Prior/likelihood/posterior expressions, small data fixture, symbolic and independently calculated numerical results, sensitivity or failed-assumption example, and a bounded written explanation of what uncertainty is and is not measured.

- **AI2-AS3** (required information measures and stable probabilistic objectives)
  - **Outcomes:** AI2-O3, AI2-O4, AI2-O7, AI2-O8, AI2-O13.
  - **Work:** Derive binary cross-entropy from a Bernoulli likelihood and show the P2 gradient at logit zero. Compute entropy, cross-entropy and KL for a declared finite distribution, including a zero-support edge case. Implement or transparently calculate the stable softplus/log-domain expression at logits 0, +1000 and -1000; compare with a naïve overflow-prone implementation. Explain when log-loss is a proper score and why minimizing empirical loss cannot establish deployment calibration.
  - **Criteria:** Log-loss and gradient for P2 match log 2 and -1/2; KL(p||q) is approximately 0.130812 nats with the correct orientation; correct zero-support and unit conventions are stated; extreme-logit calculations produce finite justified values or an explicitly safe refusal rather than overflow; derived score and probabilistic interpretation are distinguished. No unsupported performance or calibration claim passes.
  - **Evidence:** Mathematical derivations, independently calculated reference numbers, local script or accessible computation record, normal/invalid/extreme cases, and interpretation of numeric precision and score meaning.

- **AI2-AS4** (required optimizer and regularization experiment)
  - **Outcomes:** AI2-O3, AI2-O4, AI2-O9, AI2-O10, AI2-O11, AI2-O13.
  - **Work:** Implement a small first-order optimizer for L1 or L2 with an explicit gradient and independent finite-difference/reference checks. Compare stable, oscillating and divergent constant step-size choices on the exact L1 quadratic; explain which mathematical conditions justify the observed result. Add L2 regularization with a declared coefficient, derive the modified optimum, examine one ill-scaled or rank-deficient design and demonstrate a nonfinite or incorrectly scaled-update guard. Compare at least two optimizer configurations without claiming generic superiority from one fixture.
  - **Criteria:** At eta = 1/5 the L1 first update is theta = 1 with J = 5/4; eta = 4/5 from a non-optimal start oscillates, and a larger step diverges under a sufficiently explicit trace; ridge lambda = 1 yields theta = 10/7 as the mathematical minimum; analytic and independently computed gradients agree within a justified tolerance; sign/scale, nonfinite state and stopping safeguards behave as documented; the learner differentiates objective correctness, convergence on this example and prediction validity.
  - **Evidence:** Reproducible local source, explicit objective and update equations, exact oracle, selected traces, gradient-check method/tolerances, failed-case reproduction and interpretation of conditional guarantees and remaining numerical limitations.

- **AI2-AS5** (required integrated mathematical investigation and unfamiliar defense)
  - **Outcomes:** AI2-O1, AI2-O2, AI2-O3, AI2-O4, AI2-O5, AI2-O6, AI2-O7, AI2-O8, AI2-O9, AI2-O10, AI2-O11, AI2-O12, AI2-O13, AI2-O14.
  - **Work:** Extend the same **one** source/evidence collection from AI2-AS1–AS4 into a clean-state reproducible investigation. Choose one or two small justified problems; provide mathematical assumptions, model/objective, reference derivations, stable numerical procedures, controlled error/failure experiments, uncertainty limits and independent checks. An assessor provides an unfamiliar **bounded** change (for example, altered sample weights, a duplicated column, changed objective denominator, a different prior count, a constrained parameter or an extreme logit). Explain and independently calculate the expected consequences, adapt the implementation where relevant, and defend the change in an accessible written, recorded or live technical explanation.
  - **Criteria:** The reviewer can independently reproduce all claimed executable evidence and inspect conceptual derivations without hidden source or private accounts; the unexpected case receives a valid independently derived expected result, a correct implementation or justified refusal, and regression verification of previously established results; the learner explains parameter, statistical and numerical limitations and makes no claim of real-world model calibration or superior generalization without evidence. A copied library result, vague intuition, unseen unexplained weights or empty reflection cannot establish outcome AI2-O14.
  - **Evidence:** A single coherent versioned source tree or equivalent inspectable collection; executable commands/dependency assumptions; reviewable derivations and independent reference calculations; normal, negative and changed-case traces; concise assumptions/uncertainty report; and an individually attributable technical defense. Previously submitted artifacts can be linked and **reused**, not recreated or redundantly resubmitted.

### Required outcome-to-assessment coverage

| Required outcome | Evidence source |
| --- | --- |
| AI2-O1 | AI2-AS1, AI2-AS2, AI2-AS5 |
| AI2-O2 | AI2-AS1, AI2-AS5 |
| AI2-O3 | AI2-AS1, AI2-AS3, AI2-AS4, AI2-AS5 |
| AI2-O4 | AI2-AS1, AI2-AS3, AI2-AS4, AI2-AS5 |
| AI2-O5 | AI2-AS2, AI2-AS5 |
| AI2-O6 | AI2-AS2, AI2-AS5 |
| AI2-O7 | AI2-AS3, AI2-AS5 |
| AI2-O8 | AI2-AS3, AI2-AS5 |
| AI2-O9 | AI2-AS4, AI2-AS5 |
| AI2-O10 | AI2-AS1, AI2-AS4, AI2-AS5 |
| AI2-O11 | AI2-AS4, AI2-AS5 |
| AI2-O12 | AI2-AS2, AI2-AS5 |
| AI2-O13 | AI2-AS3, AI2-AS4, AI2-AS5 |
| AI2-O14 | AI2-AS5 |

All fourteen outcomes must receive satisfactory, inspectable decisions across the five required summative evaluations under the source revision used. Summative work is cumulative: a reviewer may use previous AI2-AS1–AS4 artifacts as evidence in AI2-AS5 and evaluate only the new integration and unfamiliar transfer, not force four additional independent submissions. Formative problems, time spent, passing automated scripts, attendance or copied derivations are not substitutes for the published outcomes. Do not award AI4's empirical modeling or AI5's deep-network capabilities for completing this mathematical preparation.

### Optional open technical and academic references

- [Stanford CS229 syllabus](https://cs229.stanford.edu/syllabus-new.html) — machine-learning mathematical assumptions, estimation and optimization context; not a mandate to copy course packaging.
- [MIT 6.790 Machine Learning](https://gradml.mit.edu/) — empirical-risk and statistical-inference depth, distinct from introductory programming.
- [Deep Learning, Goodfellow, Bengio and Courville](https://www.deeplearningbook.org/) — freely readable mathematical, optimization and information-theoretic context.
- [NumPy numerical computing](https://numpy.org/doc/stable/) — implementation behavior to test against independent mathematical expectations.
- [scikit-learn log loss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html) — a practical probabilistic objective reference, not a required dependency or grading oracle.

These references are optional, freely accessible supporting material; all required competency standards and acceptance criteria are already public in this course.
